"""Validate the apex-docs skill: citations resolve, links work, nothing invented.

    python tools/validate.py [--offline]

Exit 0 if clean, 1 if any check fails. Warnings never fail the run.
"""
import argparse
import glob
import os
import re
import sys

from common import PKG, read_config

os.chdir(PKG)

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def known_page_ids():
    ids = set()
    p = os.path.join("index", "pages.md")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r"^\|\s*`(\d+)`\s*\|", line)
            if m:
                ids.add(m.group(1))
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true",
                    help="skip the live fetch smoke test")
    a = ap.parse_args()

    bundle = read_config()["bundle"]
    ids = known_page_ids()
    if not ids:
        err("index/pages.md missing or empty - run tools/build_indexes.py")

    # ---- expected artefacts ----
    for d, minimum in (("workflows", 10), ("index", 4),
                       ("references", 5), ("recipes", 1)):
        n = len(glob.glob(os.path.join(d, "*.md"))) + len(glob.glob(os.path.join(d, "*.txt")))
        if n < minimum:
            err("%s/ has %d files, expected at least %d" % (d, n, minimum))

    for f in ("SKILL.md", "config.md", "index/keywords.md", "index/topics.md",
              "index/pages.md", "index/workflows-index.md"):
        if not os.path.exists(f):
            err("missing %s" % f)

    # ---- every workflow has a step ----
    orphan_workflows = []
    tools_seen = []
    for f in glob.glob("workflows/*.md"):
        s = open(f, encoding="utf-8").read()
        if not re.search(r"^1\. \S", s, re.M):
            err("%s has no numbered step" % f)
        # Every tool entry must carry its node id in the heading.
        entries = re.findall(r"^## .+ \(node ([^)]+)\)$", s, re.M)
        if not entries:
            err("%s has no '## <tool> (node <id>)' headings" % f)
        for eid in entries:
            # Expected: the workflow DB covers tools whose reference page is
            # absent from the archive, present only in some release, or (e.g.
            # node 3051) published nowhere at all. The procedure is still good,
            # and is sometimes the only surviving documentation for that tool.
            if eid.isdigit() and ids and eid not in ids:
                orphan_workflows.append(eid)
        tools_seen.extend(entries)

    # ---- cited node IDs must exist ----
    cite_re = re.compile(r"/page/node/(\d+)\.html")
    for f in (glob.glob("*.md") + glob.glob("references/*.md")
              + glob.glob("recipes/*.md")):
        s = open(f, encoding="utf-8").read()
        for nid in set(cite_re.findall(s)):
            if ids and nid not in ids:
                # legitimate when citing a page only present in another bundle,
                # but it must be stated as such nearby
                if re.search(r"apex_20\d\d\.\d/page/node/%s\.html" % nid, s):
                    warn("%s cites node %s from a non-default bundle" % (f, nid))
                else:
                    err("%s cites node %s which is not in index/pages.md" % (f, nid))

    # ---- markdown links resolve ----
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for f in (glob.glob("*.md") + glob.glob("references/*.md")
              + glob.glob("recipes/*.md") + glob.glob("index/*.md")):
        base = os.path.dirname(f)
        for t in link_re.findall(open(f, encoding="utf-8").read()):
            if t.startswith(("http://", "https://", "#")):
                continue
            path, _, frag = t.partition("#")
            target = os.path.normpath(os.path.join(base, path))
            if not os.path.exists(target):
                err("%s: broken link -> %s" % (f, t))
                continue
            # a heading anchor must actually exist in the target
            if frag and target.endswith(".md"):
                body = open(target, encoding="utf-8").read()
                slugs = set()
                for h in re.findall(r"^#{1,6} (.+?)\s*$", body, re.M):
                    slugs.add(re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-"))
                if frag not in slugs:
                    err("%s: link anchor not found -> %s" % (f, t))

    # ---- the skill must not claim to write code ----
    skill = open("SKILL.md", encoding="utf-8").read()
    if "apex-scripting" not in skill:
        err("SKILL.md must redirect code and API-reference questions to "
            "apex-scripting")

    # ---- live fetch smoke test ----
    if not a.offline:
        import subprocess
        r = subprocess.run([sys.executable, "tools/fetch_page.py", "1064",
                            "--no-cache"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace",
                           env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        if r.returncode != 0:
            warn("live fetch failed (offline?): %s"
                 % (r.stderr or "").strip().splitlines()[:1])
        elif "Element Quality" not in (r.stdout or ""):
            warn("live fetch returned unexpected content for node 1064")

    if orphan_workflows:
        print("NOTE  %d workflows describe tools with no page in the local "
              "archive: %s%s"
              % (len(orphan_workflows), " ".join(sorted(orphan_workflows)[:8]),
                 " ..." if len(orphan_workflows) > 8 else ""))
        print("      Expected. Use `fetch_page.py <id> --find-bundle` to locate "
              "a release that has the page; some exist in none, and the")
        print("      workflow is then the only surviving documentation.")

    # ---- report ----
    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)
    print("\n%d error(s), %d warning(s)   bundle=%s   pages=%d   workflows=%d"
          % (len(errors), len(warnings), bundle, len(ids),
             len(glob.glob("workflows/*.md"))))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
