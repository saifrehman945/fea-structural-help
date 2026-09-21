"""Fetch a documentation page's real text from the published docs.

The public portal (nexus.hexagon.com) is a Zoomin JavaScript app: fetching it
returns an empty shell. The SPA reads its content from a raw backend, and that
backend serves plain HTML:

    https://documentation-be.hexagon.com/bundle/<bundle>/raw/resource/enus/node/<id>.html

Usage:
    python tools/fetch_page.py <id> [--bundle apex_2025.2] [--raw] [--no-cache]
    python tools/fetch_page.py <id> --find-bundle
    python tools/fetch_page.py 1064

Prints the page as text and caches it under cache/<bundle>/<id>.txt.

Pages come and go between releases, so a 404 is not proof a feature never
existed: node 2024 lives only in apex_2022.1, node 2234 only in apex_2025.2.
`--find-bundle` probes every known bundle and reports which ones have the page.

Exit codes: 0 ok, 3 not found in this bundle, 4 network error.
"""
import argparse
import html
import os
import re
import sys
import urllib.error
import urllib.request

from common import CITE_URL, FETCH_URL, PKG, fix_text, read_config, write

CACHE = os.path.join(PKG, "cache")
UA = "Mozilla/5.0 (compatible; apex-docs-skill)"
BUNDLES = ["msc_apex_help", "apex_2025.2", "apex_2025.1", "apex_2024.1",
           "apex_2023.1", "apex_2022.1"]
TITLE_RE = re.compile(r"(?is)<title>([^<|]*)")
IMG_RE = re.compile(r'(?i)<img[^>]*?src="([^"]+)"[^>]*>')


def to_text(s):
    s = re.sub(r"(?is)<(script|style|head|nav|footer)\b.*?</\1>", " ", s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    s = re.sub(r"(?is)</(p|div|tr|li|h[1-6]|table)>", "\n", s)
    s = re.sub(r"(?is)</t[dh]>", " | ", s)
    s = re.sub(r"(?is)<h([1-6])[^>]*>",
               lambda m: "\n" + "#" * int(m.group(1)) + " ", s)
    s = IMG_RE.sub(lambda m: " [image: %s] "
                   % os.path.basename(m.group(1).split("?")[0]), s)
    t = re.sub(r"(?s)<[^>]+>", " ", s)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
    return fix_text(t).strip()


def fetch(node_id, bundle, timeout=25):
    url = FETCH_URL.format(bundle=bundle, id=node_id)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", "replace")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("id")
    ap.add_argument("--bundle", default=None)
    ap.add_argument("--raw", action="store_true", help="print HTML, not text")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--find-bundle", action="store_true",
                    help="report which release bundles contain this page")
    a = ap.parse_args()

    bundle = a.bundle or read_config()["bundle"]

    if a.find_bundle:
        found = []
        for b in BUNDLES:
            try:
                fetch(a.id, b, timeout=15)
                found.append(b)
                print("  %-16s has node %s" % (b, a.id))
            except urllib.error.HTTPError as e:
                if e.code != 404:
                    print("  %-16s HTTP %s" % (b, e.code))
            except Exception as e:
                print("  %-16s error: %s" % (b, e))
        if not found:
            print("\nnode %s is in no known bundle." % a.id)
            print("If workflows/ has a procedure for it, that procedure is the "
                  "only surviving documentation - cite it as such.")
            return 3
        print("\nFetch with: python tools/fetch_page.py %s --bundle %s"
              % (a.id, found[0]))
        return 0
    cache_file = os.path.join(CACHE, bundle, "%s.txt" % a.id)

    if not a.no_cache and not a.raw and os.path.exists(cache_file):
        sys.stdout.write(open(cache_file, encoding="utf-8").read())
        return 0

    try:
        doc = fetch(a.id, bundle)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.stderr.write(
                "node %s is not in bundle '%s'.\n"
                "Pages come and go between releases - find one that has it:\n"
                "  python tools/fetch_page.py %s --find-bundle\n"
                "If no bundle has it, check workflows/ and index/pages.md, and say "
                "you could not retrieve the page rather than reconstructing "
                "it.\n" % (a.id, bundle, a.id))
            return 3
        sys.stderr.write("HTTP %s fetching node %s\n" % (e.code, a.id))
        return 4
    except Exception as e:
        sys.stderr.write(
            "network error fetching node %s: %s\n"
            "Page text is only available online. Use workflows/ and "
            "index/pages.md, and say the page could not be retrieved.\n"
            % (a.id, e))
        return 4

    if a.raw:
        sys.stdout.write(doc)
        return 0

    m = TITLE_RE.search(doc)
    title = fix_text(m.group(1).strip()) if m else "(untitled)"
    text = to_text(doc)
    out = ("%s | node %s | bundle %s\n%s\n%s\n%s\n"
           % (title, a.id, bundle, CITE_URL.format(bundle=bundle, id=a.id),
              "-" * 60, text))

    if not a.no_cache:
        write(cache_file, out)
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
