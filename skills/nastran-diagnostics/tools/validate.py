"""Validate the nastran-diagnostics skill.

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
    bundle = read_config()["bundle"]

    for f in ("SKILL.md", "config.md", "index/ranges.md",
              "references/answering-rules.md", "references/f06-triage.md"):
        if not os.path.exists(f):
            err("missing %s" % f)

    msg_files = sorted(glob.glob("index/messages-*.md"))
    if len(msg_files) < 15:
        err("only %d message index files, expected ~20" % len(msg_files))

    # ---- message rows ----
    total, ranges_seen = 0, []
    row_re = re.compile(r"^\|\s*(\d+)\s*\|\s*(\S+)\s*\|")
    for f in msg_files:
        m = re.match(r"index/messages-(\d+)-(\d+)\.md$", f.replace("\\", "/"))
        if not m:
            err("%s does not follow messages-<lo>-<hi>.md" % f)
            continue
        lo, hi = int(m.group(1)), int(m.group(2))
        ranges_seen.append((lo, hi))
        rows = 0
        for line in open(f, encoding="utf-8"):
            r = row_re.match(line)
            if not r:
                continue
            rows += 1
            num = int(r.group(1))
            if not lo <= num <= hi:
                err("%s: message %d is outside its range %d-%d" % (f, num, lo, hi))
        if rows == 0:
            err("%s has no message rows" % f)
        total += rows
    if total < 4000:
        err("only %d messages indexed, expected ~5500" % total)

    # ---- ranges.md must cover every index file, without duplicates ----
    mapped = set()
    rng_re = re.compile(r"^\|\s*(\d+)\s*-\s*(\d+)\s*\|")
    for line in open("index/ranges.md", encoding="utf-8"):
        m = rng_re.match(line)
        if not m:
            continue
        pair = (int(m.group(1)), int(m.group(2)))
        if pair in mapped:
            err("index/ranges.md lists %d-%d twice" % pair)
        mapped.add(pair)
    for pair in ranges_seen:
        if pair not in mapped:
            err("index/ranges.md is missing range %d-%d" % pair)

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

    # ---- the skill must route, not answer everything ----
    skill = open("SKILL.md", encoding="utf-8").read()
    for other in ("nastran-reference", "apex-scripting", "apex-docs"):
        if other not in skill:
            err("SKILL.md must hand over to %s" % other)

    # ---- a real lookup must work end to end ----
    if not a.offline:
        r = subprocess.run([sys.executable, "tools/fetch_message.py", "740"],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace",
                           env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        out = r.stdout or ""
        if r.returncode != 0:
            warn("fetch_message 740 failed (offline?): %s"
                 % (r.stderr or "").strip().splitlines()[:1])
        elif "RDASGN" not in out or "User action" not in out:
            warn("fetch_message 740 returned unexpected content")
        elif len(out) > 4000:
            err("fetch_message 740 returned %d chars - it should slice one "
                "message, not the whole range file" % len(out))

    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)
    print("\n%d error(s), %d warning(s)   bundle=%s   ranges=%d   messages=%d"
          % (len(errors), len(warnings), bundle, len(msg_files), total))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
