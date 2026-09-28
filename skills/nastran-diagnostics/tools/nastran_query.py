#!/usr/bin/env python3
"""Targeted, capped lookups into a run digest (the output folder of run_digest.py).

    python tools/nastran_query.py <digest_dir> <command> [args] [--max CHARS]

Commands
    findings [CODE]            deck findings, optionally one code, with ids and file:line
    card NAME ID               one bulk entry (all its fields) and where it is
    grid ID                    dossier: position, part, everything attached, SPC/load/mass
    elem ID                    dossier: card, property and material chain, grids and parts
    part N                     one connected part: size, properties, SPC/load, contact pairs
    pair ID                    one contact pair as resolved by the checks
    msg NUM [--limit N]        occurrences of a message number with their text
    section NAME [--lines N]   lines of one f06 section (name substring, e.g. "OLOAD", "WEIGHT")
    grep REGEX [--file f06|f04|log|deck] [--limit N] [--ctx N]
                               regex search; the f06 bulk-data echo is skipped (use --file deck)

Every command prints at most --max characters (default 4000), so the output
is always safe to put into the conversation.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys


class Out:
    def __init__(self, cap):
        self.cap, self.buf, self.n = cap, [], 0

    def __call__(self, s=""):
        if self.n > self.cap:
            return
        self.buf.append(s)
        self.n += len(s) + 1

    def done(self):
        text = "\n".join(self.buf)
        if len(text) > self.cap:
            text = text[: self.cap] + "\n[... capped at %d chars - narrow the query]" % self.cap
        print(text)


def load(dirpath):
    run = json.load(open(os.path.join(dirpath, "run.json")))
    dbp = os.path.join(dirpath, "index.sqlite")
    db = sqlite3.connect(dbp) if os.path.exists(dbp) else None
    return run, db


def fields_of(row):
    name, cid, f, line, flds = row
    return name, flds.split("|"), "%s:%s" % (f, line)


def show_card(o, db, name, cid):
    r = db.execute("SELECT name,id,file,line,fields FROM cards WHERE name=? AND id=?", (name.upper(), cid)).fetchall()
    if not r:
        o("%s %s: not found in the deck" % (name.upper(), cid))
        return None
    for row in r[:3]:
        n, f, loc = fields_of(row)
        o("%s %s   (%s)" % (n, "  ".join(x if x else "." for x in f[:8]), loc))
        for k in range(8, len(f), 8):
            o("  +      " + "  ".join(x if x else "." for x in f[k:k + 8]))
    if len(r) > 1:
        o("  ** defined %d times **" % len(r))
    return fields_of(r[0])


def find_card_by_id(db, cid, names):
    q = "SELECT name,id,file,line,fields FROM cards WHERE id=? AND name IN (%s)" % ",".join("?" * len(names))
    return db.execute(q, [cid] + list(names)).fetchone()


PROPS = ("PSHELL", "PCOMP", "PCOMPG", "PSOLID", "PBAR", "PBARL", "PBEAM", "PBEAML", "PROD", "PBUSH",
         "PELAS", "PGAP", "PSHEAR", "PTUBE", "PLSOLID", "PCOMPS", "PBUSH1D", "PDAMP")
MATS = ("MAT1", "MAT2", "MAT8", "MAT9", "MAT3", "MAT10", "MATHE", "MATHP", "MATEP")


def findings_for(db, ident):
    out = []
    for code, sev, title, js in db.execute("SELECT code,severity,title,json FROM findings"):
        if ident in json.loads(js).get("ids", []):
            out.append("%s %s - %s" % (sev.upper(), code, title))
    return out


def cmd_grid(o, db, gid):
    r = show_card(o, db, "GRID", gid)
    if r is None:
        return
    comp = db.execute("SELECT label FROM comp WHERE gid=?", (gid,)).fetchone()
    o("part: %s" % (comp[0] if comp else "none (not attached)"))
    att = db.execute("SELECT kind,eid,role FROM conn WHERE gid=? LIMIT 30", (gid,)).fetchall()
    tot = db.execute("SELECT COUNT(*) FROM conn WHERE gid=?", (gid,)).fetchone()[0]
    o("attached (%d): %s" % (tot, ", ".join("%s %s%s" % (k, e, "" if ro == "node" else " [%s]" % ro)
                                             for k, e, ro in att) or "nothing"))
    for name in ("SPC1", "SPC", "FORCE", "MOMENT", "SPCD", "FORCE1", "FORCE2"):
        rows = db.execute("SELECT name,id,file,line,fields FROM cards WHERE name=? AND "
                          "('|'||fields||'|') LIKE ?", (name, "%%|%d|%%" % gid)).fetchall()
        for row in rows[:4]:
            n, f, loc = fields_of(row)
            if name == "SPC1" and str(gid) not in f[2:] and "THRU" not in [x.upper() for x in f]:
                continue
            o("%s set %s: %s (%s)" % (n, f[0], "  ".join(x or "." for x in f[1:8]), loc))
    for x in findings_for(db, gid):
        o("finding: " + x)


def cmd_elem(o, db, eid):
    r = db.execute("SELECT name,id,file,line,fields FROM cards WHERE id=? AND name NOT IN "
                   "('GRID','SPC1','SPC','FORCE','MOMENT','LOAD','PARAM','SPCADD','MPCADD','MPC','GRAV') "
                   "AND name NOT LIKE 'P%%' AND name NOT LIKE 'MAT%%' AND name NOT LIKE 'CORD%%' "
                   "AND name NOT LIKE 'B%%' AND name NOT LIKE 'SET%%'", (eid,)).fetchall()
    if not r:
        o("element %s: not found" % eid)
        return
    name, f, loc = fields_of(r[0])
    show_card(o, db, name, eid)
    if name.startswith("C") and name not in ("CONM2", "CONM1", "CMASS1", "CMASS2") and len(f) > 1:
        pid = f[1]
        pr = find_card_by_id(db, int(pid), PROPS) if pid.strip().lstrip("-").isdigit() else None
        if pr:
            pn, pf, ploc = fields_of(pr)
            o("property: %s %s (%s): %s" % (pn, pid, ploc, " ".join(x for x in pf[1:8] if x)))
            mids = set()
            if pn in ("PSHELL",):
                mids = {pf[1], pf[3], pf[5]}
            elif pn in ("PCOMP",):
                mids = {pf[j] for j in range(8, len(pf), 4)}
            elif pn in ("PCOMPG",):
                mids = {pf[8 * k + 1] for k in range(1, len(pf) // 8 + 1) if 8 * k + 1 < len(pf)}
            else:
                mids = {pf[1]}
            for mid in sorted(x for x in mids if x and x.isdigit()):
                mr = find_card_by_id(db, int(mid), MATS)
                if mr:
                    mn, mf, mloc = fields_of(mr)
                    o("material: %s %s (%s): %s" % (mn, mid, mloc, " ".join(x for x in mf[1:8] if x)))
                else:
                    o("material: MID %s MISSING" % mid)
        else:
            o("property: PID %s MISSING" % pid)
    grids = [g for (g,) in db.execute("SELECT gid FROM conn WHERE eid=?", (eid,))]
    parts = db.execute("SELECT DISTINCT label FROM comp WHERE gid IN (%s)" % ",".join("?" * len(grids)),
                       grids).fetchall() if grids else []
    o("grids: %s   part(s): %s" % (" ".join(map(str, grids[:20])), [p[0] for p in parts]))
    for x in findings_for(db, eid):
        o("finding: " + x)


def cmd_part(o, run, db, n):
    comps = (run.get("summary") or {}).get("components", [])
    c = next((x for x in comps if x["component"] == n), None)
    if not c:
        o("part %s not in the component table (%d listed)" % (n, len(comps)))
        return
    o(json.dumps(c))
    for p in (run["summary"].get("contact") or {}).get("pairs", []):
        if n in p["sec_comp_labels"] + p["main_comp_labels"]:
            o("contact pair %s: %s %s -> %s %s" % (p["id"], p["secondary"], p["sec_comp_labels"],
                                                   p["main"], p["main_comp_labels"]))
    if db:
        g = db.execute("SELECT gid FROM comp WHERE label=? LIMIT 5", (n,)).fetchall()
        o("sample grids: %s" % [x[0] for x in g])


def cmd_msg(o, db, run, num, limit):
    if db:
        rows = db.execute("SELECT line,sev,num,module,body FROM messages WHERE num=? ORDER BY line LIMIT ?",
                          (str(num), limit)).fetchall()
        tot = db.execute("SELECT COUNT(*) FROM messages WHERE num=?", (str(num),)).fetchone()[0]
    else:
        rows, tot = [], 0
        for line in open(run["_dir"] + "/messages.jsonl"):
            x = json.loads(line)
            if x["num"] == str(num):
                tot += 1
                if len(rows) < limit:
                    rows.append((x["line"], x["sev"], x["num"], x["module"], "\n".join(x["body"])))
    o("%d occurrence(s) of message %s; showing %d" % (tot, num, len(rows)))
    for line, sev, n, mod, body in rows:
        o("--- f06 line %d: %s %s (%s)" % (line, sev, n, mod))
        o(body)
    o("catalogue text: python tools/fetch_message.py %s" % num)


def cmd_section(o, run, name, nlines):
    f06 = (run.get("f06") or {}).get("file")
    if not f06:
        o("no f06 in this digest")
        return
    key = name.upper().replace(" ", "")
    secs = [s for s in run["f06"]["sections"] if key in s[0].replace(" ", "")]
    health = run["f06"].get("health", {})
    hk = [k for k in health if key in k.upper() or k.upper() in key
          or (key.startswith("WEIGHT") and k == "GPWG") or (key.startswith("SINGULAR") and k == "SINGULARITY")]
    if hk and not secs:
        for k in hk:
            for blk in health[k][:3] if isinstance(health[k], list) else [health[k]]:
                if isinstance(blk, dict) and "text" in blk:
                    o("=== %s (f06 line %s)" % (k, blk.get("line")))
                    for t in blk["text"][:nlines]:
                        o(t[:160])
                else:
                    o("=== %s: %s" % (k, json.dumps(blk)[:400]))
        return
    if not secs:
        o("no section matching %r. Sections: %s" % (name, sorted({s[0] for s in run["f06"]["sections"]})[:40]))
        return
    for sname, start, cnt in secs[:3]:
        o("=== %s (line %d, %d lines)" % (sname, start, cnt))
        with open(f06, errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                if i < start:
                    continue
                if i >= start + min(cnt, nlines):
                    break
                if line.strip():
                    o(line.rstrip()[:160])


def cmd_grep(o, run, pattern, which, limit, ctx):
    rx = re.compile(pattern, re.I)
    path = {"f06": (run.get("f06") or {}).get("file"), "f04": (run.get("f04") or {}).get("file"),
            "log": (run.get("log") or {}).get("file"),
            "deck": run["_deck"]}.get(which)
    if not path or not os.path.exists(path):
        o("no %s file recorded in this digest" % which)
        return
    skip = []
    if which == "f06":
        skip = [(s[1], s[1] + s[2]) for s in run["f06"]["sections"] if "SORTEDBULKDATAECHO" in s[0].replace(" ", "")]
    hits, prev = 0, []
    with open(path, errors="replace") as fh:
        after = 0
        for i, line in enumerate(fh, 1):
            if skip and any(a <= i < b for a, b in skip):
                continue
            if after:
                o("  %d: %s" % (i, line.rstrip()[:160]))
                after -= 1
            if rx.search(line):
                hits += 1
                if hits > limit:
                    o("[more matches - stopped at %d]" % limit)
                    break
                for j, pl in prev:
                    o("  %d: %s" % (j, pl.rstrip()[:160]))
                o("> %d: %s" % (i, line.rstrip()[:160]))
                after = ctx
            prev = (prev + [(i, line)])[-ctx:] if ctx else []
    if hits == 0:
        o("no matches")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir")
    ap.add_argument("command")
    ap.add_argument("args", nargs="*")
    ap.add_argument("--max", type=int, default=4000)
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--lines", type=int, default=60)
    ap.add_argument("--ctx", type=int, default=2)
    ap.add_argument("--file", default="f06")
    a = ap.parse_args()
    run, db = load(a.dir)
    run["_dir"] = a.dir
    run["_deck"] = (db.execute("SELECT v FROM meta WHERE k='deck'").fetchone() or [None])[0] if db else None
    o = Out(a.max)
    c = a.command.lower()
    need_db = c in ("card", "grid", "elem", "findings")
    if need_db and db is None:
        o("no index.sqlite in %s (run_digest.py was run with --no-index or without a deck)" % a.dir)
    elif c == "findings":
        rows = db.execute("SELECT json FROM findings" + (" WHERE code=?" if a.args else ""),
                          a.args[:1]).fetchall()
        for (js,) in rows:
            f = json.loads(js)
            o("%s %s - %s" % (f["severity"].upper(), f["code"], f["title"]))
            if f["detail"]:
                o("  " + f["detail"])
            if f["ids"]:
                o("  ids (%d): %s" % (f["count"], f["ids"]))
            if f["locs"]:
                o("  at: %s" % ", ".join(f["locs"]))
            o("  fix via nastran-reference %s; apex-docs: %s" % (f["route"]["nastran-reference"], f["route"]["apex-docs"]))
    elif c == "card":
        show_card(o, db, a.args[0], int(a.args[1]))
    elif c == "grid":
        cmd_grid(o, db, int(a.args[0]))
    elif c == "elem":
        cmd_elem(o, db, int(a.args[0]))
    elif c == "part":
        cmd_part(o, run, db, int(a.args[0]))
    elif c == "pair":
        p = next((p for p in ((run.get("summary") or {}).get("contact") or {}).get("pairs", [])
                  if p["id"] == int(a.args[0])), None)
        o(json.dumps(p, indent=1) if p else "pair %s not found" % a.args[0])
        if p and db:
            show_card(o, db, "BCONECT", p["id"])
    elif c == "msg":
        cmd_msg(o, db, run, a.args[0], a.limit)
    elif c == "section":
        cmd_section(o, run, " ".join(a.args), a.lines)
    elif c == "grep":
        cmd_grep(o, run, a.args[0], a.file, a.limit, a.ctx)
    else:
        o("unknown command %r - see --help" % c)
    o.done()


if __name__ == "__main__":
    sys.exit(main())
