"""Read one Nastran error message, including its User information / User action.

The catalogue is published as ~680 KB range files with no per-message anchor.
This fetches the right range file and slices out ONLY the requested message, so
a lookup costs a few hundred characters of context instead of the whole page.

    python tools/fetch_message.py 740
    python tools/fetch_message.py 2101 --all     # every variant of that number
    python tools/fetch_message.py 740 --url      # just the citation URL

Exit codes: 0 ok, 2 no such message, 3 range file unavailable, 4 network error.
"""
import argparse
import os
import re
import sys
import urllib.error
import urllib.request

from common import (BOOK, CITE_URL, FETCH_URL, PKG, page_text, read_config,
                    split_messages, write)

CACHE = os.path.join(PKG, "cache")
RANGES = os.path.join(PKG, "index", "ranges.md")
UA = "Mozilla/5.0 (compatible; nastran-diagnostics-skill)"
ROW_RE = re.compile(r"^\|\s*(\d+)\s*-\s*(\d+)\s*\|\s*\d+\s*\|[^|]*\|\s*`([^`]+)`")


def range_for(num):
    """-> (low, high, source path) for the range file holding this number."""
    if not os.path.exists(RANGES):
        sys.exit("index/ranges.md missing - run tools/build_messages.py first")
    for line in open(RANGES, encoding="utf-8"):
        m = ROW_RE.match(line)
        if m and int(m.group(1)) <= num <= int(m.group(2)):
            return int(m.group(1)), int(m.group(2)), m.group(3)
    return None


def fetch(path, bundle, timeout=60):
    url = FETCH_URL.format(bundle=bundle, path=path)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", "replace")


def load_range(path, bundle, use_cache=True):
    """Range file as flat text, cached so repeat lookups cost nothing."""
    cache_file = os.path.join(CACHE, bundle, path.replace("/", "_") + ".txt")
    if use_cache and os.path.exists(cache_file):
        return open(cache_file, encoding="utf-8").read()
    doc = fetch(path, bundle)
    text = page_text(doc)
    if use_cache:
        write(cache_file, text)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("number", type=int)
    ap.add_argument("--bundle", default=None)
    ap.add_argument("--all", action="store_true",
                    help="print every variant sharing this number")
    ap.add_argument("--url", action="store_true")
    ap.add_argument("--no-cache", action="store_true")
    a = ap.parse_args()

    bundle = a.bundle or read_config()["bundle"]
    hit = range_for(a.number)
    if not hit:
        sys.stderr.write(
            "message %d is outside every documented range.\n"
            "Check index/ranges.md for what is covered. Nastran message numbers "
            "are not contiguous, and some ranges are not published.\n" % a.number)
        return 2
    lo, hi, path = hit
    cite = CITE_URL.format(bundle=bundle, path=path)

    if a.url:
        print(cite)
        return 0

    try:
        text = load_range(path, bundle, use_cache=not a.no_cache)
    except urllib.error.HTTPError as e:
        sys.stderr.write("HTTP %s fetching the %d-%d range file.\n"
                         "Use index/messages-%05d-%05d.md for the message text; "
                         "the cause and action prose is only online.\n"
                         % (e.code, lo, hi, lo, hi))
        return 3
    except Exception as e:
        sys.stderr.write(
            "network error fetching the %d-%d range file: %s\n"
            "index/messages-%05d-%05d.md still has the message text. Say the "
            "cause/action prose could not be retrieved and give the user:\n  %s\n"
            % (lo, hi, e, lo, hi, cite))
        return 4

    blocks = [b for b in split_messages(text) if b[0] == a.number]
    if not blocks:
        sys.stderr.write(
            "message %d is not in the %d-%d range file, although the range "
            "covers it. Numbers are sparse; check "
            "index/messages-%05d-%05d.md.\n" % (a.number, lo, hi, lo, hi))
        return 2

    if not a.all:
        blocks = blocks[:1]
    print("Nastran message %d | %s | bundle %s" % (a.number, path, bundle))
    print(cite)
    print("-" * 60)
    for i, (num, code, module, block) in enumerate(blocks):
        if i:
            print()
        print(block)
    if not a.all:
        others = sum(1 for b in split_messages(text) if b[0] == a.number) - 1
        if others > 0:
            print("\n[%d more variant(s) of message %d - rerun with --all]"
                  % (others, a.number))
    return 0


if __name__ == "__main__":
    sys.exit(main())
