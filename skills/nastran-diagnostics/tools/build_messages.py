"""Build the Nastran error message index.

The catalogue is published as ~20 range files (errors 0-999, 1000-1999, ...),
each around 680 KB. This walks the overview page for the range->file map,
fetches each range once, and writes a compact index per range: number, severity,
module and the message text.

Full `User information` / `User action` prose is NOT stored -- `fetch_message.py`
slices it out of the source page on demand, so a lookup costs a few hundred
characters rather than 680 KB.

    python tools/build_messages.py [--bundle MSC_Nastran_2025.1] [--resume]

Writes index/messages-*.md and index/ranges.md. Needs network access.
"""
import argparse
import os
import re
import sys
import urllib.error
import urllib.request

from common import (BOOK, CITE_URL, FETCH_URL, OVERVIEW, PKG, first_line,
                    page_text, read_config, robust_fetch, split_messages, write)

OUT = os.path.join(PKG, "index")
UA = "Mozilla/5.0 (compatible; nastran-diagnostics-skill)"
# Overview links look like: /csh?context=error1_XREF_36966_Errors_0_999&...
CTX_RE = re.compile(r"context=(error\d+)_XREF_\d+_Errors_(\d+)_(\d+)")


def fetch(path, bundle, timeout=60):
    url = FETCH_URL.format(bundle=bundle, path=path)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", "replace")


def ranges(bundle):
    """-> [(file_stem, low, high)] from the overview page."""
    page = robust_fetch(fetch, OVERVIEW, bundle)
    out, seen = [], set()
    for stem, lo, hi in CTX_RE.findall(page):
        if stem in seen:
            continue
        seen.add(stem)
        out.append((stem, int(lo), int(hi)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default=None)
    ap.add_argument("--resume", action="store_true",
                    help="skip ranges whose index file already exists")
    a = ap.parse_args()
    bundle = a.bundle or read_config()["bundle"]

    try:
        rs = ranges(bundle)
    except Exception as e:
        sys.exit("could not read the error overview page: %s" % e)
    if not rs:
        sys.exit("no message ranges found on the overview page")
    print("message ranges: %d" % len(rs))

    # Two stems can publish the same numeric range (error12 and error13 both
    # cover 11000-11999). Accumulate per range and write once at the end, or the
    # second stem's file silently replaces the first's.
    by_range = {}

    for stem, lo, hi in rs:
        path = "%s/%s/%s.xhtml" % (BOOK, stem, stem)
        name = "messages-%05d-%05d" % (lo, hi)
        bucket = by_range.setdefault(
            (lo, hi), {"rows": [], "paths": [], "name": name, "stems": [],
                       "prebuilt": False})

        if a.resume and os.path.exists(os.path.join(OUT, "%s.md" % name)):
            bucket["prebuilt"] = True
            bucket["stems"].append(stem)
            bucket["paths"].append(path)
            print("  %-9s %5d-%-5d  already built (skipped)" % (stem, lo, hi))
            continue

        try:
            html_doc = robust_fetch(fetch, path, bundle)
        except urllib.error.HTTPError as e:
            print("  %-9s %5d-%-5d  HTTP %s (skipped)" % (stem, lo, hi, e.code))
            continue
        except Exception as e:
            print("  %-9s %5d-%-5d  %s (skipped)" % (stem, lo, hi, e))
            continue

        msgs = split_messages(page_text(html_doc))
        if not msgs:
            print("  %-9s %5d-%-5d  no messages parsed (skipped)" % (stem, lo, hi))
            continue

        rows, dropped = [], 0
        for num, code, module, block in msgs:
            # An ordinal-looking line inside a table ("3.0") reads as a message
            # boundary. A range file only ever contains its own range, so a
            # number outside it is parse noise, not a message.
            if not lo <= num <= hi:
                dropped += 1
                continue
            text = first_line(block).replace("|", "/")
            if len(text) > 300:
                text = text[:297].rsplit(" ", 1)[0] + "..."
            rows.append((num, code, module, text))

        bucket["rows"] += rows
        bucket["paths"].append(path)
        bucket["stems"].append(stem)
        print("  %-9s %5d-%-5d  %4d messages%s"
              % (stem, lo, hi, len(rows),
                 "  (%d out-of-range dropped)" % dropped if dropped else ""))

    total, built = 0, []
    for (lo, hi), b in sorted(by_range.items()):
        if b["prebuilt"] and not b["rows"]:
            built.append((b["stems"][0], lo, hi, -1, b["name"]))
            continue
        if not b["rows"]:
            continue

        seen, merged = set(), []
        for r in sorted(b["rows"]):
            key = (r[0], r[1], r[2])
            if key in seen:
                continue
            seen.add(key)
            merged.append(r)

        srcs = ", ".join("`%s`" % x for x in b["paths"])
        L = ["# Nastran messages %d - %d" % (lo, hi), "",
             "Release: `%s`. Source: %s." % (bundle, srcs), "",
             "This index carries the message text only. For the `User "
             "information` and `User action` prose, which is what actually tells "
             "you what to do, read the message itself:", "",
             "```", "python tools/fetch_message.py <number>", "```", "",
             "Severity: `UFM` user fatal, `SFM` system fatal, `UWM` user warning, "
             "`SWM` system warning, `UIM`/`SIM` information, `-` no severity "
             "banner in the source.", "",
             "| No. | Severity | Module | Message |", "|---|---|---|---|"]
        for num, code, module, text in merged:
            L.append("| %d | %s | %s | %s |" % (num, code, module, text))
        write(os.path.join(OUT, "%s.md" % b["name"]), "\n".join(L) + "\n")

        built.append((b["stems"][0], lo, hi, len(merged), b["name"]))
        total += len(merged)

    # range map, so a number resolves to a file without opening any of them
    L = ["# Message ranges", "",
         "Which index file holds a message number, and which source file it came "
         "from. Release: `%s`." % bundle, "",
         "`fetch_message.py` uses this map; you rarely need it directly.", "",
         "| Range | Messages | Index | Source |", "|---|---|---|---|"]
    for stem, lo, hi, n, name in built:
        L.append("| %d - %d | %s | [%s.md](%s.md) | `%s/%s/%s.xhtml` |"
                 % (lo, hi, "?" if n < 0 else n, name, name, BOOK, stem, stem))
    L += ["", "Citation URL for any message:", "", "```",
          CITE_URL.format(bundle=bundle, path=BOOK + "/<stem>/<stem>.xhtml"),
          "```"]
    write(os.path.join(OUT, "ranges.md"), "\n".join(L) + "\n")

    print("-" * 46)
    print("ranges built    : %d" % len(built))
    print("messages indexed: %d" % total)
    print("output: %s" % os.path.relpath(OUT, PKG))


if __name__ == "__main__":
    main()
