"""Build the navigation indexes that make the documentation findable.

The published docs are a JavaScript SPA: not crawlable, no listing, no full-text
search, and the raw backend only answers if you already know the node ID. These
indexes are what turn a user's question into an ID to fetch.

    python tools/build_indexes.py [path to Documentation]

Writes index/pages.md, index/keywords.md, index/topics.md.
"""
import glob
import html
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import OrderedDict, defaultdict

from common import (CITE_URL, FETCH_URL, PKG, find_archive, fix_text,
                    read_config, strip_tags, write)

OUT = os.path.join(PKG, "index")

JUNK_TITLE = re.compile(r"^\s*(access denied|page not found)\s*$", re.I)
TITLE_RE = re.compile(r"(?is)<title>([^<|]*)")
UP_RE = re.compile(r'(?is)<a href="(\d+)\.html"[^>]*class="page-up"')


def load_pages(doc):
    """node id -> {title, parent, status}"""
    node_dir = os.path.join(doc, "UI", "node")
    pages = {}
    for p in sorted(glob.glob(os.path.join(node_dir, "*.html"))):
        pid = os.path.splitext(os.path.basename(p))[0]
        if not pid.isdigit():
            continue
        s = open(p, encoding="utf-8", errors="replace").read()
        m = TITLE_RE.search(s)
        title = fix_text(html.unescape(m.group(1).strip())) if m else ""
        status = "ok"
        if JUNK_TITLE.match(title):
            status = title.lower().replace(" ", "-")
            title = ""
        up = UP_RE.search(s)
        pages[pid] = {
            "title": title,
            "parent": up.group(1) if up else "",
            "status": status,
        }
    return pages


def load_keywords(doc):
    """keyword -> {ids}, plus id -> (title, description, category)."""
    xml = os.path.join(doc, "UI", "XmlFiles", "docSearchData_Apex_1.0_en.xml")
    kw = defaultdict(set)
    meta = {}
    if not os.path.exists(xml):
        return kw, meta
    root = ET.parse(xml).getroot()
    for listname in ("AdvancedTooltipList", "DocumentationSearchList"):
        sec = root.find(listname)
        if sec is None:
            continue
        for n in sec:
            nid = (n.findtext("NodeId") or n.findtext("EntityId") or "").strip()
            if not nid.isdigit():
                continue
            k = fix_text((n.findtext("Keyword") or "").strip()).lower()
            title = fix_text((n.findtext("Title") or "").strip())
            desc = fix_text((n.findtext("Description")
                             or n.findtext("tooltipExtendText") or "").strip())
            cat = fix_text((n.findtext("Category") or "").strip())
            if k:
                kw[k].add(nid)
            if nid not in meta or (not meta[nid][1] and desc):
                meta[nid] = (title, desc, cat)
    return kw, meta


def toc_path(pid, pages, _cache={}):
    """Walk page-up links to the root, guarding against cycles."""
    if pid in _cache:
        return _cache[pid]
    seen, chain, cur = set(), [], pid
    while cur and cur in pages and cur not in seen:
        seen.add(cur)
        t = pages[cur]["title"] or ("node %s" % cur)
        chain.append(t)
        cur = pages[cur]["parent"]
    chain.reverse()
    _cache[pid] = chain
    return chain


def main():
    doc = find_archive(sys.argv[1] if len(sys.argv) > 1 else None)
    bundle = read_config()["bundle"]

    pages = load_pages(doc)
    kw, meta = load_keywords(doc)

    # fill missing titles from the XML metadata
    for pid, p in pages.items():
        if not p["title"] and pid in meta and meta[pid][0]:
            p["title"] = meta[pid][0]

    # ---- pages.md ----
    L = ["# Page catalog", "",
         "Every documentation page, with a one-line summary of what it covers. "
         "Bundle: `%s` (see `config.md`)." % bundle, "",
         "**This is the primary search surface.** The page text itself is not "
         "stored locally — the published documentation is the source of truth "
         "— so grep the titles and summaries here to pick an ID, then fetch "
         "it with `python tools/fetch_page.py <id>`. Search "
         "`index/keywords.md` first if the user's wording is not literal.", "",
         "Summaries come from the Apex in-product help database, so they use "
         "Apex's own phrasing for the feature.", "",
         "| ID | Title | Summary | Section |", "|---|---|---|---|"]
    ok = 0
    for pid in sorted(pages, key=int):
        p = pages[pid]
        chain = toc_path(pid, pages)
        section = " › ".join(chain[1:-1][:3]) if len(chain) > 2 else ""
        title = p["title"] or "(untitled)"
        if p["status"] == "ok":
            ok += 1
        desc = meta.get(pid, ("", "", ""))[1]
        desc = re.sub(r"\s+", " ", desc).strip()
        if len(desc) > 200:
            desc = desc[:197].rsplit(" ", 1)[0] + "..."
        desc = desc.replace("|", "/")
        if p["status"] != "ok":
            desc = (desc + " ") if desc else ""
            desc += "[%s in archive]" % p["status"].replace("-", " ")
        L.append("| `%s` | %s | %s | %s |" % (pid, title, desc, section))
    L += ["", "## URL patterns", "",
          "```", "cite  : " + CITE_URL.format(bundle=bundle, id="<id>"),
          "fetch : " + FETCH_URL.format(bundle=bundle, id="<id>"), "```"]
    write(os.path.join(OUT, "pages.md"), "\n".join(L) + "\n")

    # ---- keywords.md ----
    L = ["# Keyword index", "",
         "The vocabulary bridge. Apex's own in-product search keywords mapped to "
         "page IDs, so a user's wording reaches the right page even when the page "
         "never uses that word. `section view` and `cutting plane` both resolve to "
         "Cut View (2948), which contains neither phrase.", "",
         "**Search this file first**, then `index/pages.md` summaries, then "
         "`index/topics.md`. Page text itself lives online, not here — "
         "fetch it once you have an ID.", "",
         "| Keyword | Page IDs | Titles |", "|---|---|---|"]
    for k in sorted(kw):
        ids = sorted(kw[k], key=int)
        titles = "; ".join(
            (pages.get(i, {}).get("title") or meta.get(i, ("", "", ""))[0] or i)
            for i in ids[:4])
        L.append("| %s | %s | %s |"
                 % (k, " ".join("`%s`" % i for i in ids[:6]), titles))
    write(os.path.join(OUT, "keywords.md"), "\n".join(L) + "\n")

    # ---- topics.md ----
    kids = defaultdict(list)
    roots = []
    for pid, p in pages.items():
        if p["parent"] and p["parent"] in pages:
            kids[p["parent"]].append(pid)
        else:
            roots.append(pid)
    for v in kids.values():
        v.sort(key=int)

    L = ["# Topic hierarchy", "",
         "The documentation book tree, rebuilt from each page's parent link. Use "
         "it to find neighbouring pages once you have landed somewhere roughly "
         "right — related material is almost always a sibling.", ""]

    def emit(pid, depth, seen):
        if pid in seen or depth > 8:
            return
        seen.add(pid)
        t = pages[pid]["title"] or "(untitled)"
        L.append("%s- `%s` %s" % ("  " * depth, pid, t))
        for c in kids.get(pid, []):
            emit(c, depth + 1, seen)

    seen = set()
    for r in sorted(roots, key=int):
        if kids.get(r):
            emit(r, 0, seen)
    orphans = [p for p in sorted(pages, key=int) if p not in seen]
    if orphans:
        L += ["", "## Not reachable from a root", ""]
        for p in orphans:
            L.append("- `%s` %s" % (p, pages[p]["title"] or "(untitled)"))
    write(os.path.join(OUT, "topics.md"), "\n".join(L) + "\n")

    print("pages         : %d  (%d ok, %d gated/missing)"
          % (len(pages), ok, len(pages) - ok))
    print("keywords      : %d unique -> %d distinct page ids"
          % (len(kw), len(set().union(*kw.values())) if kw else 0))
    print("tree          : %d reachable, %d orphans" % (len(seen), len(orphans)))
    print("output        : %s" % os.path.relpath(OUT, PKG))


if __name__ == "__main__":
    main()
