"""Check every apex.* name used in the skill's prose and templates really exists.

Cross-checks SKILL.md, references/ and assets/ against the generated index in
api/. Exits non-zero if anything is unverifiable, so it can gate a change.

    python tools/validate_references.py

The package root is derived from this file's location.
"""
import re, os, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)

funcs, enums, classes, methods = set(), {}, set(), set()
for line in open("api/functions-index.md", encoding="utf-8"):
    m = re.match(r"- `([\w.]+)`", line)
    if m:
        funcs.add(m.group(1))
for line in open("api/enums.md", encoding="utf-8"):
    m = re.match(r"- `([\w.]+)`: (.+)", line)
    if m:
        enums[m.group(1)] = set(re.findall(r"`(\w+)`", m.group(2)))
for line in open("api/classes.md", encoding="utf-8"):
    m = re.match(r"- `([\w.]+)`", line)
    if m:
        classes.add(m.group(1))
for f in glob.glob("api/classes/*.md"):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"- `(\w+)\(", line)
        if m:
            methods.add(m.group(1))

srcs = []
for pat in ("*.md", "references/*.md", "assets/**/*.py", "assets/**/*.md"):
    for f in glob.glob(pat, recursive=True):
        n = f.replace(os.sep, "/")
        if n not in srcs:
            srcs.append(n)

print("FILES CHECKED (%d):" % len(srcs))
for s in srcs:
    print("   ", s)

bad = []
for p in srcs:
    s = open(p, encoding="utf-8").read()
    for m in re.finditer(r"\bapex(?:\.\w+)+(?=\()", s):
        n = m.group(0)
        if n in funcs or n.split(".")[-1] in methods or n in classes:
            continue
        bad.append((p, "CALL", n))
    for m in re.finditer(r"\bapex\.(?:\w+\.)?[A-Z]\w+\.[A-Z]\w+\b", s):
        n = m.group(0)
        en, mem = n.rsplit(".", 1)
        if en in enums:
            if mem not in enums[en]:
                bad.append((p, "ENUM MEMBER", n))
        elif en not in classes:
            bad.append((p, "UNKNOWN ENUM", n))

print("\nISSUES: %d" % len(bad))
for p, k, n in bad:
    print("  %-13s %-50s <- %s" % (k, n, p))

sys.exit(1 if bad else 0)
