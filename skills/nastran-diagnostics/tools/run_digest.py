#!/usr/bin/env python3
"""Digest a Nastran run so it can be diagnosed without reading the raw files.

    python tools/run_digest.py --f06 run.f06 [--f04 run.f04] [--log run.log]
                               [--bdf model.bdf] [-I include_dir] [-o outdir]

Any subset of the files works. The raw files never need to enter the
conversation: this writes

    outdir/digest.md      what to read first - capped at ~12k characters
    outdir/findings.json  deck findings (code, severity, ids, file:line, route)
    outdir/run.json       every extracted fact, machine readable
    outdir/messages.jsonl every message occurrence
    outdir/sections.tsv   f06 section map (name, start line, line count)
    outdir/deck_echo.bdf  bulk data rebuilt from the f06 echo (when present)
    outdir/index.sqlite   cards, grid-element links, components, messages
                          -> query with tools/nastran_query.py

Deck source: --bdf if given, otherwise the SORTED BULK DATA ECHO in the f06.
Case control: from the .bdf if it has one, otherwise from the f06 echo.
Stdlib only; scipy is used for the coincident-node search when available.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sqlite3
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_checks import build_model, run_checks  # noqa: E402

DIGEST_CAP = 12000
SEV = {("USER", "FATAL"): "UFM", ("SYSTEM", "FATAL"): "SFM",
       ("USER", "WARNING"): "UWM", ("SYSTEM", "WARNING"): "SWM",
       ("USER", "INFORMATION"): "UIM", ("SYSTEM", "INFORMATION"): "SIM"}
SEV_RANK = {"SFM": 0, "UFM": 1, "SWM": 2, "UWM": 3, "SIM": 4, "UIM": 5}
RX_BANNER = re.compile(
    r"^[\s0]*\*\*\*\s+(USER|SYSTEM)\s+(FATAL|WARNING|INFORMATION)\s+MESSAGE\s*(\d*)\s*\((.*?)\)?\s*$")
RX_PAGE = re.compile(r"^1.*\bPAGE\s+\d+\s*$")
RX_SPACED = re.compile(r"^[ 0]+((?:[A-Z0-9/()\-.] ){3,}[A-Z0-9/()\-.](?:  +(?:[A-Z0-9/()\-.] ?)+)*)\s*$")
RX_ECHO = re.compile(r"^\s+(\d+)-(.*)$")
RX_NUM = r"[-+]?\d*\.?\d+(?:E[-+]?\d+)?"
RX_IDS = re.compile(r"\b(GRID|POINT|ELEMENT|ELEM|EID|GID|NODE)\S*\s*(?:ID)?\s*(?:NO\.?)?\s*=?\s*(\d{1,10})\b")
GRAB_LINES = {  # text in line -> (key, lines to keep)
    "OLOAD    RESULTANT": ("OLOAD", 12), "SPCFORCE RESULTANT": ("SPCFORCE", 12),
    "MPCFORCE RESULTANT": ("MPCFORCE", 12), "MAXIMUM  DISPLACEMENTS": ("MAX_DISP", 8),
    "MAXIMUM  SPCFORCES": ("MAX_SPCF", 8), "MAXIMUM  APPLIED LOADS": ("MAX_LOAD", 8),
}
GRAB_SECTIONS = {"OUTPUTFROMGRIDPOINTWEIGHTGENERATOR": ("GPWG", 30),
                 "GRIDPOINTSINGULARITYTABLE": ("SINGULARITY", 30),
                 "REALEIGENVALUES": ("EIGENVALUES", 25)}
ENTITY_WORDS = {"GRID": "grid", "POINT": "grid", "NODE": "grid", "GID": "grid",
                "ELEMENT": "elem", "ELEM": "elem", "EID": "elem"}


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def norm_spaced(s):
    return " ".join(w.replace(" ", "") for w in re.split(r"\s{2,}", s.strip()))


def body_key(lines):
    t = " ".join(l.strip() for l in lines[:3])
    return re.sub(r"[-+]?\d[\d.E+-]*", "#", t)[:160]


# ---------------------------------------------------------------------- f06
def scan_f06(path, out):
    res = {"file": os.path.abspath(path), "lines": 0, "version": None, "sol": None,
           "case_control": [], "exec_control": [], "header_comments": [], "sections": [],
           "messages": {}, "health": {}, "echo_cards": collections.Counter(),
           "geom_summary": [], "has_echo": False, "terminated": []}
    msgs = res["messages"]
    sec_name, sec_start, sec_lines = "PREAMBLE", 1, 0
    sections, in_echo, cur, grab = [], False, None, None
    fmsg = open(os.path.join(out, "messages.jsonl"), "w")
    fdeck = None

    def close():
        nonlocal cur
        if not cur:
            return
        m = cur
        key = "%s|%s|%s|%s" % (m["sev"], m["num"], m["module"], body_key(m["body"]))
        e = msgs.setdefault(key, {"sev": m["sev"], "num": m["num"], "module": m["module"], "count": 0,
                                  "first_line": m["line"], "lines": [], "samples": [],
                                  "entities": collections.Counter()})
        e["count"] += 1
        if len(e["lines"]) < 50:
            e["lines"].append(m["line"])
        if len(e["samples"]) < 3 and m["body"] not in e["samples"]:
            e["samples"].append(m["body"])
        for ln in m["body"]:
            for w, i in RX_IDS.findall(ln.upper()):
                e["entities"]["%s %s" % (ENTITY_WORDS.get(w, w.lower()), i)] += 1
        fmsg.write(json.dumps(m) + "\n")
        cur = None

    with open(path, "r", errors="replace") as f:
        for n, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            res["lines"] = n
            if res["version"] is None and n < 300:
                mv = re.search(r"Version\s+([\w.\-]+)", line)
                if mv:
                    res["version"] = mv.group(1)
            if RX_PAGE.match(line):
                close()
                continue
            ms = RX_SPACED.match(line)
            if ms and "***" not in line:
                name = norm_spaced(ms.group(1))
                if name != sec_name:
                    sections.append((sec_name, sec_start, sec_lines))
                    sec_name, sec_start, sec_lines = name, n, 0
                    in_echo = "SORTEDBULKDATAECHO" in name.replace(" ", "")
                    key = name.replace(" ", "")
                    grab = (GRAB_SECTIONS[key][0], GRAB_SECTIONS[key][1], [line.rstrip()]) \
                        if key in GRAB_SECTIONS else grab
                close()
            sec_lines += 1
            sname = sec_name.replace(" ", "")

            if in_echo:
                me = RX_ECHO.match(line)
                if me:
                    if fdeck is None:
                        fdeck = open(os.path.join(out, "deck_echo.bdf"), "w")
                        fdeck.write("BEGIN BULK\n")
                        res["has_echo"] = True
                    body = me.group(2)
                    card = body[8:] if len(body) > 8 else body.strip()
                    fdeck.write(card.rstrip() + "\n")
                    head = card[:8].strip()
                    if head and not head.startswith(("+", "*")):
                        res["echo_cards"][head.split(",")[0].rstrip("*").upper()] += 1
                    continue
                if "ENDDATA" in line:
                    if fdeck:
                        fdeck.write("ENDDATA\n")
                    in_echo = False
                continue

            if sname.startswith("CASECONTROLECHO"):
                m = re.match(r"^\s+\d+\s{2,}(.*\S)", line)
                if m and not m.group(1).startswith("$") and not m.group(1).upper().startswith("BEGIN BULK"):
                    res["case_control"].append(m.group(1))
            elif sname.startswith("NASTRANEXECUTIVECONTROLECHO") and line.strip():
                res["exec_control"].append(line.strip())
                mm = re.match(r"\s*SOL\s+(\S+)", line)
                if mm:
                    res["sol"] = mm.group(1)
            elif sname.startswith("NASTRANFILEANDSYSTEMPARAMETERECHO") and line.strip().startswith("$"):
                t = line.strip().strip("$").strip()
                if t:
                    res["header_comments"].append(t)

            mb = RX_BANNER.match(line)
            if mb:
                close()
                who, kind, num, mod = mb.groups()
                cur = {"line": n, "sev": SEV[(who, kind)], "num": num or "", "module": (mod or "").strip(),
                       "body": []}
                continue
            if cur is not None:
                s = line.strip()
                if not s or s.startswith("^^^") or len(cur["body"]) >= 25:
                    close()
                else:
                    cur["body"].append(s)
            if re.search(r"FATAL ERROR|JOB TERMINATED|EXECUTION TERMINATED|ANALYSIS TERMINATED", line):
                if len(res["terminated"]) < 5:
                    res["terminated"].append((n, line.strip()[:160]))

            h = res["health"]
            if "MATRIX-TO-FACTOR-DIAGONAL RATIO" in line:
                v = re.findall(RX_NUM, line)
                h.setdefault("max_ratio", []).append({"value": float(v[-1]), "line": n,
                                                      "text": re.sub(r"\s+", " ", line.strip())[:140]})
            if "Condition number of stiffness matrix" in line:
                h["condition_number"] = {"value": float(re.findall(RX_NUM, line)[-1]), "line": n}
            if "LOAD SEQ. NO." in line and "EPSILON" in line:
                h["_eps"] = True
            elif h.get("_eps"):
                p = line.split()
                if len(p) >= 3 and p[0].isdigit():
                    try:
                        h.setdefault("epsilon", []).append({"load_seq": int(p[0]), "epsilon": float(p[1]),
                                                            "external_work": float(p[2].strip("*")),
                                                            "flagged": "*" in line, "line": n})
                    except ValueError:
                        h["_eps"] = False
                elif p and not p[0].isdigit():
                    h["_eps"] = False
            started = False
            for k, (key, cnt) in GRAB_LINES.items():
                if k in line:
                    grab = (key, cnt, [line.rstrip()])
                    started = True
                    break
            if not started and grab and not (ms and "***" not in line):
                key, left, buf = grab
                if line.strip():
                    buf.append(line.rstrip())
                left -= 1
                if left <= 0 or (key in ("OLOAD", "SPCFORCE", "MPCFORCE") and "TOTALS" in line):
                    h.setdefault(key, []).append({"line": n, "text": buf})
                    grab = None
                else:
                    grab = (key, left, buf)
            if "PRODUCED" in line and "TOLERANCE" in line:
                res["geom_summary"].append(re.sub(r"\s+", " ", line.strip()))
    close()
    sections.append((sec_name, sec_start, sec_lines))
    fmsg.close()
    if fdeck:
        fdeck.close()
    res["health"].pop("_eps", None)
    merged = []
    for s in sections:
        if merged and merged[-1][0] == s[0]:
            merged[-1] = (s[0], merged[-1][1], merged[-1][2] + s[2])
        else:
            merged.append(s)
    res["sections"] = merged
    with open(os.path.join(out, "sections.tsv"), "w") as f:
        f.write("section\tstart_line\tlines\n")
        for s in merged:
            f.write("%s\t%d\t%d\n" % s)
    return res


# ---------------------------------------------------------------------- f04 / log
def scan_f04(path):
    rx = re.compile(r"^\s*(\d\d:\d\d:\d\d)\s+(\d+:\d\d)\s+([\d.]+)\s+([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(.*)$")
    last, slow, n, fatal = None, [], 0, []
    with open(path, errors="replace") as f:
        for line in f:
            if "FATAL" in line and len(fatal) < 5:
                fatal.append(line.strip()[:160])
            m = rx.match(line)
            if not m:
                continue
            n += 1
            last = {"time": m.group(1), "elapsed": m.group(2), "step": re.sub(r"\s+", " ", m.group(7).strip())}
            d = float(m.group(6))
            if d > 5:
                slow.append((d, last["step"], m.group(2)))
    slow.sort(reverse=True)
    return {"file": os.path.abspath(path), "steps": n, "last_step": last, "fatal_lines": fatal,
            "slowest": [{"del_cpu_s": d, "step": s, "at": t} for d, s, t in slow[:6]]}


def scan_log(path):
    txt = open(path, errors="replace").read()

    def g(rx):
        m = re.search(rx, txt, re.M)
        return m.group(1).strip() if m else None
    res = {"file": os.path.abspath(path), "version": g(r"^MSC Nastran (V\S+)") or g(r"(Simcenter Nastran \S+)"),
           "exit": g(r"NSEXIT:\s*(EXIT\(\d+\))"), "analysis_complete": g(r"Analysis complete\s+(\d+)"),
           "elapsed": g(r"Total job elapsed time\s*:\s*(.*)"), "mem": g(r"^MEM=(\S+)"),
           "dof": g(r"model generated (\d+) degrees of freedom"), "solver": g(r"Solver:(\S+)"),
           "mem_solver_available": g(r"Memory available\s*:\s*(\d+ MB)"),
           "mem_solver_used": g(r"Memory used\s*:\s*(\d+ MB)"),
           "errors": [l.strip()[:200] for l in re.findall(
               r"^.*(?:FATAL|[Ee]rror|not enough|insufficient|[Ll]icense.*(?:fail|denied)|disk.*full).*$",
               txt, re.M)][:8]}
    m = re.search(r"DOF SET\s+(.+?)\n\s*DOF SET TOTALS\s+(.+?)\n", txt)
    if m:
        res["uset"] = dict(zip(m.group(1).split(), [int(x) for x in m.group(2).split()]))
    m = re.search(r"Warning/Fatal Message Summary.*?\n(.*?)\n\s*=+", txt, re.S)
    if m:
        res["message_summary"] = [re.sub(r"\s+", " ", l.strip()) for l in m.group(1).splitlines() if l.strip()]
    return res


# ---------------------------------------------------------------------- index
def open_index(out):
    p = os.path.join(out, "index.sqlite")
    if os.path.exists(p):
        os.remove(p)
    db = sqlite3.connect(p)
    db.executescript("""
        PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF;
        CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
        CREATE TABLE cards(name TEXT, id INTEGER, file TEXT, line INTEGER, fields TEXT);
        CREATE TABLE conn(gid INTEGER, eid INTEGER, kind TEXT, role TEXT);
        CREATE TABLE comp(gid INTEGER PRIMARY KEY, label INTEGER);
        CREATE TABLE messages(line INTEGER, sev TEXT, num TEXT, module TEXT, body TEXT);
        CREATE TABLE findings(code TEXT, severity TEXT, title TEXT, json TEXT);
    """)
    return db


class CardSink:
    def __init__(self, db):
        self.db, self.buf = db, []

    def __call__(self, c):
        cid = c.fields[1] if len(c.fields) > 1 else ""
        try:
            cid = int(cid)
        except ValueError:
            cid = None
        self.buf.append((c.name, cid, os.path.basename(c.file), c.line, "|".join(c.fields[1:])))
        if len(self.buf) >= 50000:
            self.flush()

    def flush(self):
        if self.buf:
            self.db.executemany("INSERT INTO cards VALUES (?,?,?,?,?)", self.buf)
            self.buf = []


def fill_index(db, m, aux, findings, out):
    rows = []
    for eid, (n, pid, nodes, loc, _) in m.elems.items():
        rows += [(g, eid, n, "node") for g in nodes]
    for eid, (n, ind, dep, _, loc) in m.rigids.items():
        rows += [(g, eid, n, "independent") for g in ind] + [(g, eid, n, "dependent") for g in dep]
    for eid, (n, g, mass, loc) in m.masses.items():
        rows.append((g, eid, n, "mass=%g" % mass))
    db.executemany("INSERT INTO conn VALUES (?,?,?,?)", rows)
    lab = aux["label"]
    db.executemany("INSERT INTO comp VALUES (?,?)", [(g, lab[c]) for g, c in aux["comp_of"].items()])
    db.executemany("INSERT INTO findings VALUES (?,?,?,?)",
                   [(f["code"], f["severity"], f["title"], json.dumps(f)) for f in findings])
    db.execute("CREATE INDEX ic ON cards(name, id)")
    db.execute("CREATE INDEX ic2 ON cards(id)")
    db.execute("CREATE INDEX ig ON conn(gid)")
    db.execute("CREATE INDEX ie ON conn(eid)")


# ---------------------------------------------------------------------- digest
def fmt_list(xs, n=8):
    xs = list(xs)
    return ", ".join(str(x) for x in xs[:n]) + (" (+%d)" % (len(xs) - n) if len(xs) > n else "")


def entity_dossier(db, kind, id_, m):
    if db is None or m is None:
        return None
    if kind == "grid":
        g = m.grids.get(id_)
        if not g:
            return "GRID %s: not in deck" % id_
        att = db.execute("SELECT kind, eid, role FROM conn WHERE gid=? LIMIT 6", (id_,)).fetchall()
        comp = db.execute("SELECT label FROM comp WHERE gid=?", (id_,)).fetchone()
        return "GRID %s at %s (%s), component %s, attached: %s" % (
            id_, tuple(round(x, 3) for x in (m.pos(id_) or (0, 0, 0))), g[6], comp[0] if comp else "-",
            fmt_list(["%s %s%s" % (k, e, "" if r == "node" else " " + r) for k, e, r in att], 6) or "nothing")
    e = m.elems.get(id_) or m.rigids.get(id_) or m.masses.get(id_)
    if not e:
        return "ELEMENT %s: not in deck" % id_
    if id_ in m.elems:
        n, pid, nodes, loc, _ = e
        p = m.props.get(pid)
        return "%s %s (%s) PID %s %s, grids %s" % (n, id_, loc, pid, p.name if p else "MISSING", fmt_list(nodes, 8))
    return "%s %s (%s)" % (e[0], id_, e[-1])


def write_digest(out, f06, f04, lg, deck_info, F, S, m, db):
    L = ["# Nastran run digest", ""]
    L.append("Read this, then query specifics with `tools/nastran_query.py %s <command>`. "
             "Never Read the raw .f06 / .bdf." % out)
    # ---- run
    L += ["", "## Run"]
    if lg:
        L.append("- %s, exit %s, analysis complete %s, elapsed %s" % (lg["version"], lg["exit"],
                                                                     lg["analysis_complete"], lg["elapsed"]))
        L.append("- DOF %s, solver %s, solver memory used/available %s/%s, MEM=%s" % (
            lg["dof"], lg["solver"], lg["mem_solver_used"], lg["mem_solver_available"], lg["mem"]))
        if lg.get("uset"):
            L.append("- USET totals: " + ", ".join("%s=%s" % kv for kv in lg["uset"].items()))
        if lg.get("errors"):
            L.append("- log error lines: " + " | ".join(lg["errors"][:4]))
    if f04 and f04["last_step"]:
        L.append("- f04 last step: %s at %s%s" % (f04["last_step"]["step"], f04["last_step"]["elapsed"],
                                                   ("; FATAL: " + f04["fatal_lines"][0]) if f04["fatal_lines"] else ""))
        if f04["slowest"]:
            L.append("- slowest: " + "; ".join("%s %.0fs" % (s["step"], s["del_cpu_s"]) for s in f04["slowest"][:3]))
    if f06:
        L.append("- SOL %s, f06 %s lines, version %s" % (f06["sol"], "{:,}".format(f06["lines"]), f06["version"]))
        for t in f06["terminated"][:2]:
            L.append("- termination text at line %d: %s" % t)
        hc = [c for c in f06["header_comments"] if re.search(r"UNIT|LENGTH|MASS\b|TIME|FORCE|CREATED BY", c)]
        if hc:
            L.append("- deck header: " + " / ".join(hc[:7]))
        L.append("- case control: " + " ; ".join(f06["case_control"][:25]))

    # ---- messages
    if f06:
        L += ["", "## Messages (deduplicated; catalogue text via tools/fetch_message.py)"]
        ms = sorted(f06["messages"].values(), key=lambda x: (SEV_RANK[x["sev"]], x["first_line"]))
        fatal = [x for x in ms if x["sev"] in ("UFM", "SFM")]
        if fatal:
            ff = min(fatal, key=lambda x: x["first_line"])
            L.append("- **first fatal: %s %s (%s) at f06 line %d**" % (ff["sev"], ff["num"], ff["module"], ff["first_line"]))
            before = [x for x in ms if x["first_line"] < ff["first_line"] and x["sev"] in ("UWM", "SWM")]
            if before:
                L.append("- warnings before it: " + fmt_list(["%s %s (%s) x%d" % (x["sev"], x["num"], x["module"], x["count"])
                                                             for x in sorted(before, key=lambda x: x["first_line"])], 8))
        else:
            L.append("- no fatal messages")
        noise = 0
        shown = 0
        for x in ms:
            if x["sev"] in ("UIM", "SIM") and (x["module"].lower().startswith("crdb") or not x["num"]):
                noise += x["count"]
                continue
            if shown >= 14:
                noise += x["count"]
                continue
            shown += 1
            ents = [k for k, _ in x["entities"].most_common(6)]
            L.append("- **%s %s (%s)** x%d, first line %d%s" % (x["sev"], x["num"], x["module"], x["count"],
                                                               x["first_line"], (", entities: " + ", ".join(ents)) if ents else ""))
            for b in (x["samples"][0][:3] if x["samples"] else []):
                L.append("    > " + b[:130])
            if x["sev"] in ("UFM", "SFM", "UWM", "SWM") and ents and db is not None:
                for k in ents[:3]:
                    kind, i = k.split()
                    d = entity_dossier(db, kind, int(i), m)
                    if d:
                        L.append("    - " + d)
        if noise:
            L.append("- (+%d further information messages - `msg` command lists them)" % noise)

        # ---- health
        L += ["", "## Solution health (from the f06)"]
        h = f06["health"]
        for r in h.get("max_ratio", [])[:3]:
            L.append("- " + r["text"])
        if "condition_number" in h:
            L.append("- stiffness condition number %.3e" % h["condition_number"]["value"])
        for e in h.get("epsilon", [])[:6]:
            L.append("- epsilon load seq %d: %.3e (external work %.4e)%s" % (
                e["load_seq"], e["epsilon"], e["external_work"], "  **FLAGGED**" if e["flagged"] else ""))
        for key in ("OLOAD", "SPCFORCE", "MPCFORCE"):
            blks = h.get(key, [])
            for b in blks[:3]:
                tot = [t for t in b["text"] if "TOTALS" in t]
                L.append("- %s resultant (line %d): %s" % (key, b["line"], re.sub(r"\s+", " ", tot[0].strip()) if tot else "see section"))
            if not blks and key != "MPCFORCE":
                L.append("- %s resultant: **not in f06**" % key)
        L.append("- grid point weight (mass) table: " + ("present - `section GRID POINT WEIGHT`" if "GPWG" in h else "**not in f06**"))
        if "SINGULARITY" in h:
            L.append("- grid point singularity table present - `section SINGULARITY`")
        if "EIGENVALUES" in h:
            L.append("- eigenvalue table present - `section EIGENVALUES`")
        for g_ in f06["geom_summary"][:6]:
            L.append("- geometry: " + g_)

    # ---- deck
    if F is not None:
        L += ["", "## Deck checks (computed from the deck: %s)" % deck_info["source"]]
        items = F.sorted()
        if not items:
            L.append("- no findings")
        for f in items:
            if f["severity"] == "info":
                continue
            L.append("- **%s %s** - %s" % (f["severity"].upper(), f["code"], f["title"]))
            if f["detail"]:
                L.append("    " + f["detail"][:420])
            if f["ids"]:
                L.append("    ids: %s%s" % (fmt_list(f["ids"], 8), ("   at " + ", ".join(f["locs"][:2])) if f["locs"] else ""))
        info = [f for f in items if f["severity"] == "info"]
        for f in info:
            L.append("- INFO %s - %s%s%s" % (f["code"], f["title"],
                                              (": " + f["detail"][:220]) if f["detail"] else "",
                                              ("; ids " + fmt_list(f["ids"], 5)) if f["ids"] else ""))
        # load path / components
        L += ["", "## Model (computed)"]
        mass = S["mass"]
        L.append("- mass estimate %.5g (elements %.5g + lumped %.5g)%s; WTMASS %g%s" % (
            mass["total_estimate"], mass["total_estimate"] - mass["lumped"], mass["lumped"],
            (", not estimated: %s" % mass["not_estimated"]) if mass["not_estimated"] else "", mass["wtmass"],
            "" if f06 is None or "GPWG" not in f06["health"] else " - compare with GPWG"))
        u = S.get("units") or {}
        if u.get("g"):
            L.append("- units: length %s, mass %s, time %s, force %s (g = %.6g)" % (
                u.get("length"), u.get("mass"), u.get("time"), u.get("force"), u["g"]))
        for lid, ld in S["loads"].items():
            L.append("- LOAD %s: %s, force resultant (basic) %s, moment about origin %s%s, applied at grids %s" % (
                lid, ld["cards"], ld["force_resultant_basic"], ld["moment_about_origin"],
                (", GRAV %s" % ld["grav"]) if ld["grav"] else "", fmt_list(ld["point_grids"], 4)))
        L.append("- active sets: %s" % S["active"])
        L.append("- %d connected parts (elements + rigid + active MPC), %d after contact:" % (
            S["components_total"], S["groups_total"]))
        L.append("  | part | grids | elements | top PIDs | SPC grids | loaded | lumped mass | elem mass |")
        L.append("  |---|---|---|---|---|---|---|---|")
        for c in S["components"][:10]:
            L.append("  | %d | %d | %d | %s | %d | %d | %.4g | %.4g |" % (
                c["component"], c["grids"], c["elements"], ",".join(str(k) for k in c["props"]),
                c["spc_grids"], c["loaded_grids"], c["lumped_mass"], c["element_mass"]))
        pairs = S["contact"].get("pairs", [])
        if pairs:
            L.append("- contact pairs (secondary -> main; part numbers as above):")
            for p in pairs[:16]:
                L.append("  - %s: %s parts %s (%d el, size %.3g) -> %s parts %s (%d el, size %.3g), IGLUE %s" % (
                    p["id"], p["secondary"], p["sec_comp_labels"], p["sec_elems"], p["sec_size"] or 0,
                    ", ".join(p["main"]), p["main_comp_labels"], p["main_elems"], p["main_size"] or 0, p["iglue"]))
            for nt in S["contact"].get("notes", []):
                L.append("  - note: " + nt)
        if S.get("coincident"):
            c = S["coincident"]
            L.append("- coincident grids (tol %.3g): %d pairs, %d across glued parts, %d across unconnected parts" % (
                c["tolerance"], c["pairs_total"], c["across_glued_components"], c["across_unconnected_components"]))
        if S.get("cards_not_checked"):
            L.append("- card types not interpreted: " + fmt_list(["%s %d" % kv for kv in S["cards_not_checked"].items()], 10))
    elif deck_info.get("reason"):
        L += ["", "## Deck checks", "- not run: " + deck_info["reason"]]

    if f06:
        L += ["", "## Where the f06 lines went"]
        agg = collections.Counter()
        for name, start, n in f06["sections"]:
            agg[name] += n
        for name, n in agg.most_common(6):
            L.append("- %s: %s lines (%.1f%%)" % (name, "{:,}".format(n), 100.0 * n / max(1, f06["lines"])))
    text = "\n".join(L) + "\n"
    if len(text) > DIGEST_CAP:
        text = text[:DIGEST_CAP] + "\n\n[digest truncated at %d chars - query run.json / findings.json]\n" % DIGEST_CAP
    open(os.path.join(out, "digest.md"), "w").write(text)
    return text


# ---------------------------------------------------------------------- main
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--f06"); ap.add_argument("--f04"); ap.add_argument("--log")
    ap.add_argument("--bdf", help="input deck (else rebuilt from the f06 echo)")
    ap.add_argument("-I", "--include-dir", action="append", default=[])
    ap.add_argument("-o", "--out")
    ap.add_argument("--no-deck", action="store_true", help="skip deck checks")
    ap.add_argument("--no-index", action="store_true", help="skip index.sqlite")
    ap.add_argument("--no-coincident", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="do not print the digest")
    a = ap.parse_args(argv)
    first = a.f06 or a.bdf or a.log or a.f04
    if not first:
        ap.error("give at least one of --f06 --f04 --log --bdf")
    out = a.out or os.path.splitext(first)[0] + "_digest"
    os.makedirs(out, exist_ok=True)
    t0 = time.time()

    lg = scan_log(a.log) if a.log else None
    f04 = scan_f04(a.f04) if a.f04 else None
    f06 = None
    if a.f06:
        log("scanning f06 ...")
        f06 = scan_f06(a.f06, out)
        log("  f06: %d lines in %.1fs" % (f06["lines"], time.time() - t0))

    deck_info, F, S, m, db = {"source": None}, None, None, None, None
    deck_path, cc_lines = None, None
    if a.bdf:
        deck_path = a.bdf
        deck_info["source"] = os.path.basename(a.bdf)
    elif f06 and f06["has_echo"]:
        deck_path = os.path.join(out, "deck_echo.bdf")
        deck_info["source"] = "rebuilt from the f06 bulk data echo - file:line refers to deck_echo.bdf"
    else:
        deck_info["reason"] = "no --bdf given and the f06 has no bulk data echo"
    if a.no_deck:
        deck_path, deck_info["reason"] = None, "--no-deck"

    if deck_path:
        db = None if a.no_index else open_index(out)
        sink = CardSink(db) if db else None
        log("reading deck ...")
        m = build_model(deck_path, a.include_dir, sink=sink, log=log)
        if sink:
            sink.flush()
        cc_lines = m.deck.case_control or (f06["case_control"] if f06 else [])
        hint = " ".join(f06["header_comments"]) if f06 else ""
        sol = (f06 or {}).get("sol")
        if not sol:
            sol = next((t.split()[1] for t, *_ in m.deck.executive
                        if t.upper().startswith("SOL ") and len(t.split()) > 1), None)
        F, S, aux = run_checks(m, cc_lines, sol, unit_hint=hint, coincident=not a.no_coincident, log=log)
        if db:
            fill_index(db, m, aux, F.sorted(), out)
    if db and f06:
        rows = []
        with open(os.path.join(out, "messages.jsonl")) as fh:
            for line in fh:
                x = json.loads(line)
                rows.append((x["line"], x["sev"], x["num"], x["module"], "\n".join(x["body"])))
        db.executemany("INSERT INTO messages VALUES (?,?,?,?,?)", rows)
    if db:
        meta = {"f06": f06["file"] if f06 else "", "f04": f04["file"] if f04 else "",
                "log": lg["file"] if lg else "", "deck": os.path.abspath(deck_path) if deck_path else ""}
        db.executemany("INSERT INTO meta VALUES (?,?)", list(meta.items()))
        db.commit()

    text = write_digest(out, f06, f04, lg, deck_info, F, S, m, db)
    if F is not None:
        json.dump(F.sorted(), open(os.path.join(out, "findings.json"), "w"), indent=1, default=str)
    if f06:
        f06 = dict(f06, echo_cards=dict(f06["echo_cards"]),
                   messages=[dict(v, entities=dict(v["entities"].most_common(30))) for v in f06["messages"].values()])
    json.dump({"f06": f06, "f04": f04, "log": lg, "deck": deck_info, "summary": S}, open(
        os.path.join(out, "run.json"), "w"), indent=1, default=str)
    if db:
        db.close()
    if not a.quiet:
        print(text)
    log("[digest %d chars ~%d tokens; total %.1fs; output in %s]" % (len(text), len(text) // 4, time.time() - t0, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
