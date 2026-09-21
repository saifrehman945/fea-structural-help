"""Read a Nastran documentation page by keyword.

The published portal is a JavaScript app: fetching its page URL returns an empty
shell. The SPA reads content from a raw backend that serves plain HTML, and that
is what this fetches. Results are cached under cache/.

    python tools/fetch_page.py PSHELL          # by keyword, via index/keywords.md
    python tools/fetch_page.py CQUAD4 --brief  # first ~1500 chars only
    python tools/fetch_page.py --path Nastran/Quick_Reference_Guide/... # direct
    python tools/fetch_page.py PSHELL --url    # just print the citation URL

Exit codes: 0 ok, 2 keyword not in the index, 3 page not found, 4 network error.
"""
import argparse
import os
import re
import sys
import urllib.error
import urllib.request

from common import (CITE_URL, FETCH_URL, PKG, read_config, to_text, write)

CACHE = os.path.join(PKG, "cache")
INDEX = os.path.join(PKG, "index", "keywords.md")
UA = "Mozilla/5.0 (compatible; nastran-reference-skill)"
ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(\S+)\s*\|\s*`([^`]+)`\s*\|\s*$")


def lookup(keyword):
    """-> [(keyword, section, path)] matching, exact first then case-insensitive."""
    if not os.path.exists(INDEX):
        sys.exit("index/keywords.md missing - run tools/build_index.py first")
    exact, loose = [], []
    for line in open(INDEX, encoding="utf-8"):
        m = ROW_RE.match(line)
        if not m:
            continue
        kw, section, path = m.group(1), m.group(2), m.group(3)
        if kw == keyword:
            exact.append((kw, section, path))
        elif kw.lower() == keyword.lower():
            loose.append((kw, section, path))
    return exact or loose


def fetch(path, bundle, timeout=30):
    url = FETCH_URL.format(bundle=bundle, path=path)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keyword", nargs="?")
    ap.add_argument("--path", default=None, help="fetch this exact path instead")
    ap.add_argument("--bundle", default=None)
    ap.add_argument("--brief", action="store_true", help="first ~1500 chars only")
    ap.add_argument("--url", action="store_true", help="print the citation URL only")
    ap.add_argument("--no-cache", action="store_true")
    a = ap.parse_args()

    cfg = read_config()
    bundle = a.bundle or cfg["qrg"]
    label = a.keyword or "(path)"

    if a.path:
        path = a.path
    elif a.keyword:
        hits = lookup(a.keyword)
        if not hits:
            sys.stderr.write(
                "'%s' is not in index/keywords.md.\n"
                "Grep the index for a partial match before concluding it does "
                "not exist:\n"
                "  grep -i '%s' index/keywords.md\n"
                "Remember the index covers the QRG and Reference Guide only; "
                "error messages live in the nastran-diagnostics skill.\n"
                % (a.keyword, a.keyword[:12]))
            return 2
        if len(hits) > 1:
            sys.stderr.write("'%s' matches %d topics:\n" % (a.keyword, len(hits)))
            for kw, sec, p in hits:
                sys.stderr.write("  %-16s %-18s %s\n" % (kw, sec, p))
            sys.stderr.write("Fetching the first.\n\n")
        label, _, path = hits[0]
    else:
        ap.error("give a keyword or --path")

    cite = CITE_URL.format(bundle=bundle, path=path)
    if a.url:
        print(cite)
        return 0

    cache_file = os.path.join(CACHE, bundle, path.replace("/", "_") + ".txt")
    if not a.no_cache and os.path.exists(cache_file):
        out = open(cache_file, encoding="utf-8").read()
    else:
        try:
            doc = fetch(path, bundle)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                sys.stderr.write(
                    "%s is not in bundle '%s'.\n"
                    "Entries are added and removed between releases - try "
                    "another, e.g. --bundle MSC_Nastran_2024.1.\n" % (path, bundle))
                return 3
            sys.stderr.write("HTTP %s fetching %s\n" % (e.code, path))
            return 4
        except Exception as e:
            sys.stderr.write(
                "network error fetching %s: %s\n"
                "Page text is only available online. Use index/keywords.md to "
                "say what exists, and give the user the URL:\n  %s\n"
                % (path, e, cite))
            return 4
        out = "%s | %s | bundle %s\n%s\n%s\n%s\n" % (
            label, path, bundle, cite, "-" * 60, to_text(doc))
        if not a.no_cache:
            write(cache_file, out)

    if a.brief:
        head, _, body = out.partition("-" * 60)
        out = head + "-" * 60 + body[:1500] + (
            "\n\n[truncated - rerun without --brief for the full entry]"
            if len(body) > 1500 else "")
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
