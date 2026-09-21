"""Shared helpers for the nastran-reference build and fetch scripts.

The Hexagon documentation portal (nexus.hexagon.com) is a Zoomin JavaScript app:
fetching a page URL returns an empty shell. The SPA reads its content from a raw
backend that serves plain HTML, and that is what these scripts use.

Nastran pages are addressed by PATH, not by the numeric node id Apex uses.
"""
import html
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)

# Raw backend: serves real HTML. Path-addressed for Nastran.
FETCH_URL = ("https://documentation-be.hexagon.com/bundle/{bundle}"
             "/raw/resource/enus/{path}")
# What a human opens in a browser, and what we cite.
CITE_URL = ("https://nexus.hexagon.com/documentationcenter/en-US/bundle/{bundle}"
            "/page/{path}")

# Books live in different releases: the QRG and Reference Guide are richest in
# 2025.2, but the error message list only exists in the 2025.1 "Combined Book".
DEFAULT_BUNDLES = {
    "qrg": "MSC_Nastran_2025.2",
    "reference": "MSC_Nastran_2025.2",
    "errors": "MSC_Nastran_2025.1",
}


def read_config():
    """Parse `key: value` lines out of config.md."""
    cfg = dict(DEFAULT_BUNDLES)
    path = os.path.join(PKG, "config.md")
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^\s*-?\s*(qrg|reference|errors)\s*:\s*(\S+)\s*$", line)
            if m and not m.group(2).startswith("<"):
                cfg[m.group(1)] = m.group(2).strip().strip("`")
    return cfg


MOJIBAKE = {
    "Â·": "·", "â€œ": "“",
    "â€": "”", "â€™": "’",
    "â€“": "–", "â€”": "—",
    "Â ": " ",
}


def fix_text(s):
    if not s:
        return ""
    for bad, good in MOJIBAKE.items():
        if bad in s:
            s = s.replace(bad, good)
    s = unicodedata.normalize("NFC", s)
    return s.replace(" ", " ")


def strip_tags(frag):
    frag = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", frag)
    txt = re.sub(r"(?s)<[^>]+>", " ", frag)
    txt = re.sub(r"\s+", " ", html.unescape(txt))
    return fix_text(txt).strip()


TABLE_RE = re.compile(r"(?is)<table\b.*?</table>")
ROW_RE = re.compile(r"(?is)<tr\b.*?</tr>")
CELL_RE = re.compile(r"(?is)<t[dh]\b[^>]*>(.*?)</t[dh]>")


def _table_to_text(block):
    """Render a table as one line per row.

    Bulk data entries document their field layout as a table, and the field
    POSITION is the meaning -- `PSHELL PID MID1 T MID2 ...` is only useful if
    the row stays on one line. Cells contain block tags, so the generic
    newline-per-block rule has to be bypassed here or every cell lands on its
    own line and the layout is destroyed.
    """
    lines = []
    for row in ROW_RE.findall(block):
        cells = [strip_tags(c) for c in CELL_RE.findall(row)]
        if any(cells):
            lines.append(" | ".join(cells))
    return "\n" + "\n".join(lines) + "\n" if lines else "\n"


def to_text(s):
    """Full page HTML -> readable text, keeping headings, tables and images."""
    s = re.sub(r"(?is)<(script|style|head|nav|footer)\b.*?</\1>", " ", s)
    # tables first, so their rows survive the block-level newline rules below
    s = TABLE_RE.sub(lambda m: _table_to_text(m.group(0)), s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    s = re.sub(r"(?is)</(p|div|li|h[1-6])>", "\n", s)
    s = re.sub(r"(?is)<h([1-6])[^>]*>",
               lambda m: "\n" + "#" * int(m.group(1)) + " ", s)
    s = re.sub(r'(?i)<img[^>]*?src="([^"]+)"[^>]*>',
               lambda m: " [image: %s] " % os.path.basename(
                   m.group(1).split("?")[0]), s)
    t = re.sub(r"(?s)<[^>]+>", " ", s)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return fix_text(t).strip()


LINK_RE = re.compile(r'<a[^>]+href="([^"#][^"]*\.x?htm[^"]*)"[^>]*>(.*?)</a>',
                     re.S | re.I)


def links_with_text(page_html):
    """[(href, anchor text)] for internal doc links, in document order."""
    out = []
    for href, label in LINK_RE.findall(page_html):
        label = strip_tags(label)
        if label:
            out.append((html.unescape(href), label))
    return out


def norm_path(base, href):
    """Resolve an href relative to the directory of `base`, portal-style."""
    href = href.split("#")[0]
    joined = os.path.normpath(os.path.join(os.path.dirname(base), href))
    return joined.replace(os.sep, "/")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text)


def robust_fetch(fetch_fn, path, bundle, tries=4, base_delay=2.0):
    """fetch_fn with backoff. The portal intermittently refuses sustained
    request bursts, surfacing as DNS or connection-reset errors rather than a
    429, so transient failures must be retried rather than treated as 404s."""
    import time
    import urllib.error
    last = None
    for attempt in range(tries):
        try:
            return fetch_fn(path, bundle)
        except urllib.error.HTTPError:
            raise                      # a real 404/500 is not worth retrying
        except Exception as e:
            last = e
            if attempt < tries - 1:
                time.sleep(base_delay * (2 ** attempt))
    raise last
