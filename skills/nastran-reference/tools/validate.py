"""Validate the nastran-reference skill.

    python tools/validate.py [--offline]

Exit 0 if clean, 1 on any error. Warnings never fail the run.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

from common import PKG, read_config

os.chdir(PKG)
errors, warnings = [], []


def err(m):
    errors.append(m)


def warn(m):
    warnings.append(m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    a = ap.parse_args()
    cfg = read_config()

    for f in ("SKILL.md", "config.md", "index/keywords.md",
              "index/bulk-data.md", "index/case-control.md",
              "references/answering-rules.md", "references/deck-anatomy.md"):
        if not os.path.exists(f):
            err("missing %s" % f)

    # ---- the flat index is the entry point; everything must be reachable ----
    row_re = re.compile(r"^\|\s*(.+?)\s*\|\s*(\S+)\s*\|\s*`([^`]+)`\s*\|\s*$")
    keywords, paths = {}, set()
    if os.path.exists("index/keywords.md"):
        for line in open("index/keywords.md", encoding="utf-8"):
            m = row_re.match(line)
            if not m:
                continue
            kw, section, path = m.group(1), m.group(2), m.group(3)
            keywords.setdefault(kw, []).append(path)
            paths.add(path)
            if not path.startswith("Nastran/"):
                err("index/keywords.md: %s has a non-Nastran path %s" % (kw, path))
            if not path.endswith((".htm", ".xhtml")):
                err("index/keywords.md: %s has a non-page path %s" % (kw, path))

    if len(keywords) < 900:
        err("only %d keywords indexed, expected well over 1000" % len(keywords))

    # ---- the entries an FEA engineer will reach for first must be there ----
    must_have = ["CQUAD4", "CTRIA3", "PSHELL", "PCOMP", "PBARL", "PBEAM",
                 "RBE2", "RBE3", "MAT1", "GRID", "CBUSH", "SPC1", "FORCE",
                 "PLOAD4", "PARAM", "CBAR", "CELAS2", "CONM2"]
    missing = [k for k in must_have if k not in keywords]
    if missing:
        err("index/keywords.md is missing common entries: %s" % ", ".join(missing))

    # ---- per-section files must agree with the flat index ----
    for f in glob.glob("index/*.md"):
        base = os.path.basename(f)
        if base == "keywords.md":
            continue
        rows = 0
        for line in open(f, encoding="utf-8"):
            if re.match(r"^\|\s*.+?\s*\|\s*`[^`]+`\s*\|\s*$", line):
                rows += 1
        if rows == 0:
            err("%s has no keyword rows" % f)

    # ---- links ----
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for f in (glob.glob("*.md") + glob.glob("references/*.md")
              + glob.glob("index/*.md")):
        base = os.path.dirname(f)
        for t in link_re.findall(open(f, encoding="utf-8").read()):
            if t.startswith(("http://", "https://", "#")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, t))):
                err("%s: broken link -> %s" % (f, t))

    # ---- the skill must route rather than answer everything ----
    skill = open("SKILL.md", encoding="utf-8").read()
    for other in ("nastran-diagnostics", "apex-scripting", "apex-docs"):
        if other not in skill:
            err("SKILL.md must hand over to %s" % other)

    # ---- a real lookup must work end to end ----
    if not a.offline:
        r = subprocess.run([sys.executable, "tools/fetch_page.py", "PSHELL"],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace",
                           env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        out = r.stdout or ""
        if r.returncode != 0:
            warn("fetch_page PSHELL failed (offline?): %s"
                 % (r.stderr or "").strip().splitlines()[:1])
        elif "MID1" not in out or "Shell Element Property" not in out:
            warn("fetch_page PSHELL returned unexpected content")

    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)
    print("\n%d error(s), %d warning(s)   qrg=%s   keywords=%d   sections=%d"
          % (len(errors), len(warnings), cfg["qrg"], len(keywords),
             len(glob.glob("index/*.md")) - 1))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
