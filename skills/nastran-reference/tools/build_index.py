"""Build the Nastran keyword indexes from the published documentation.

The portal cannot be searched or crawled from outside: it is a JavaScript app
with no listing and no full-text search. But each chapter has a landing page
(`0_<Chapter>.htm`) that links to every topic in it, WITH the keyword as the
anchor text -- so a bounded walk over landing pages yields the whole index
without opening most topic pages.

    python tools/build_index.py [--bundle MSC_Nastran_2025.2] [--max-pages N]

Writes index/*.md. Needs network access; takes a few minutes.
"""
import argparse
import os
import sys
import urllib.error
import urllib.request

from common import (CITE_URL, FETCH_URL, PKG, links_with_text, norm_path,
                    read_config, robust_fetch, write)

OUT = os.path.join(PKG, "index")
UA = "Mozilla/5.0 (compatible; nastran-reference-skill)"
QRG = "Nastran/Quick_Reference_Guide"
RG = "Nastran/Reference_Guide"

# Seeds: chapter landing pages, plus the list pages that some chapters use
# instead of linking their topics directly from the landing.
SEEDS = [
    QRG + "/Bulk_Data_Entries/0_Bulk_Data_Entries.htm",
    QRG + "/Case_Control_Commands/Case_Control_Commands/0_Case_Control_Commands.htm",
    QRG + "/Case_Control_Commands/Case_Control_Commands/11_Case_Control_Commands.htm",
    QRG + "/Executive_Control_Statements/0_Executive_Control_Statements.htm",
    QRG + "/File_Management_Statements/0_File_Management_Statements.htm",
    QRG + "/NASTRAN_Statement/0_NASTRAN_Statement.htm",
    RG + "/Structural_Elements/0_Structural_Elements.htm",
    RG + "/Solution_Sequences/0_Solution_Sequences.htm",
    RG + "/Grid_Points_and_Coordinate_Systems/0_Grid_Points_and_Coordinate_Systems.htm",
]

# A page belongs to the section whose path prefix it matches, longest match
# first. Classifying by path rather than by which seed reached it keeps the
# section label honest -- the walk crosses freely between books.
SECTIONS = [
    (QRG + "/Bulk_Data_Entries", "bulk-data", "Bulk Data Entries"),
    (QRG + "/Case_Control_Commands", "case-control", "Case Control Commands"),
    (QRG + "/Executive_Control_Statements", "executive-control",
     "Executive Control Statements"),
    (QRG + "/File_Management_Statements", "file-management",
     "File Management Statements"),
    (QRG + "/NASTRAN_Statement", "nastran-statement",
     "NASTRAN Statement and System Cells"),
    (QRG + "/Parameters", "parameters", "Parameters"),
    (QRG, "qrg-other", "Quick Reference Guide - other"),
    (RG, "reference-guide", "Reference Guide"),
    ("Nastran/Getting_Started_Guide", "getting-started", "Getting Started Guide"),
    ("Nastran/DMAP_Programmers_Guide", "dmap", "DMAP Programmer's Guide"),
    ("Nastran/Installation_and_Operations_Guide", "install-operations",
     "Installation and Operations Guide"),
]
OTHER = ("other-books", "Other books")

SKIP_LABELS = {"$", "/", ""}
PROBE_PER_DIR = 2


def fetch(path, bundle, timeout=30):
    url = FETCH_URL.format(bundle=bundle, path=path)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", "replace")


def is_landing(path):
    return os.path.basename(path).startswith("0_")


def section_of(path):
    best = None
    for prefix, key, title in SECTIONS:
        if path.startswith(prefix) and (best is None or len(prefix) > len(best[0])):
            best = (prefix, key, title)
    return (best[1], best[2]) if best else OTHER


def crawl(bundle, max_pages, probe_topics=True):
    """One walk from all seeds -> ({path: label}, pages_walked).

    Landing pages are walked first and exhaustively: they are cheap and yield
    whole chapters at once. Topic pages are walked only afterwards, and only to
    exhaust the page budget, because their cross-references are the only way to
    discover books the seeds never mention (no book-level TOC is served).
    """
    queue, later = list(SEEDS), []
    visited, found, probed = set(), {}, {}
    while (queue or (probe_topics and later)) and len(visited) < max_pages:
        cur = queue.pop(0) if queue else later.pop(0)
        if cur in visited:
            continue
        visited.add(cur)
        try:
            page = robust_fetch(fetch, cur, bundle)
        except urllib.error.HTTPError as e:
            if cur in SEEDS:
                print("  !! seed %s -> HTTP %s" % (cur, e.code))
            continue
        except Exception as e:
            print("  !! %s -> %s" % (cur, e))
            continue

        for href, label in links_with_text(page):
            path = norm_path(cur, href)
            if not path.startswith("Nastran/") or label in SKIP_LABELS:
                continue
            found.setdefault(path, label)
            if path in visited:
                continue
            if is_landing(path):
                queue.append(path)
            elif probe_topics:
                # Probing exists only to discover books the seeds never
                # mention, and a chapter's cross-references repeat. A couple of
                # topics per directory finds them; probing all 959 bulk data
                # entries would spend the whole budget learning nothing.
                d = os.path.dirname(path)
                if probed.get(d, 0) < PROBE_PER_DIR:
                    probed[d] = probed.get(d, 0) + 1
                    later.append(path)
        if len(visited) % 25 == 0:
            print("  ... %d pages walked, %d topics found"
                  % (len(visited), len(found)))
    return found, len(visited)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default=None)
    ap.add_argument("--max-pages", type=int, default=400)
    ap.add_argument("--no-probe", action="store_true",
                    help="landing pages only; fast but shallow")
    a = ap.parse_args()
    bundle = a.bundle or read_config()["qrg"]

    print("crawling %s ..." % bundle)
    found, walked = crawl(bundle, a.max_pages,
                          probe_topics=not a.no_probe)
    if not found:
        sys.exit("no topics found - check network access and the bundle name")

    buckets = {}
    for path, label in found.items():
        key, title = section_of(path)
        buckets.setdefault(key, (title, []))[1].append((label, path))

    for key, (title, rows) in sorted(buckets.items()):
        rows.sort(key=lambda r: r[0].lower())
        L = ["# %s" % title, "",
             "Release: `%s`. Every indexed topic in this book or chapter." % bundle,
             "",
             "Look a keyword up here or in `keywords.md`, then read the page:", "",
             "```", "python tools/fetch_page.py <KEYWORD>", "```", "",
             "| Keyword | Path |", "|---|---|"]
        for label, path in rows:
            L.append("| %s | `%s` |" % (label.replace("|", "/"), path))
        write(os.path.join(OUT, "%s.md" % key), "\n".join(L) + "\n")

    # flat lookup across everything
    L = ["# Nastran keyword index", "",
         "Every indexed keyword across the Nastran documentation, flat and "
         "greppable. **Grep here first**, then fetch the page.", "",
         "Release: `%s` (see `config.md`). Error messages are not here — they "
         "belong to the `nastran-diagnostics` skill." % bundle, "",
         "| Keyword | Section | Path |", "|---|---|---|"]
    flat = sorted(((lbl, section_of(p)[0], p) for p, lbl in found.items()),
                  key=lambda r: (r[0].lower(), r[2]))
    for label, key, path in flat:
        L.append("| %s | %s | `%s` |" % (label.replace("|", "/"), key, path))
    L += ["", "## URL patterns", "", "```",
          "cite  : " + CITE_URL.format(bundle=bundle, path="<path>"),
          "fetch : " + FETCH_URL.format(bundle=bundle, path="<path>"), "```"]
    write(os.path.join(OUT, "keywords.md"), "\n".join(L) + "\n")

    print("-" * 46)
    for key, (title, rows) in sorted(buckets.items()):
        print("  %-20s %5d topics" % (key, len(rows)))
    print("-" * 46)
    print("pages walked  : %d" % walked)
    print("topics indexed: %d" % len(found))
    print("output: %s" % os.path.relpath(OUT, PKG))


if __name__ == "__main__":
    main()
