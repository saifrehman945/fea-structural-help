"""Shared helpers for the apex-docs build scripts.

Paths are derived from this file's location so the skill works from any
directory. The Apex documentation archive is located via, in order:
  1. an explicit command-line argument
  2. the APEX_DOCS_ARCHIVE environment variable
  3. config.md's `archive:` line
  4. a few conventional locations relative to the skill
"""
import html
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)

# The Zoomin backend that serves real page text; the public portal is a JS shell.
FETCH_URL = ("https://documentation-be.hexagon.com/bundle/{bundle}"
             "/raw/resource/enus/node/{id}.html")
# What a human opens in a browser, and what we cite.
CITE_URL = ("https://nexus.hexagon.com/documentationcenter/en-US/bundle/{bundle}"
            "/page/node/{id}.html")
DEFAULT_BUNDLE = "msc_apex_help"


def read_config():
    """Parse the simple `key: value` lines out of config.md."""
    cfg = {"bundle": DEFAULT_BUNDLE, "archive": ""}
    path = os.path.join(PKG, "config.md")
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^\s*-?\s*(bundle|archive)\s*:\s*(\S.*?)\s*$", line)
            if m and not m.group(2).startswith("<"):
                cfg[m.group(1)] = m.group(2).strip().strip("`")
    return cfg


def find_archive(argv_path=None):
    """Locate the Documentation folder of the Apex archive."""
    cands = []
    if argv_path:
        cands.append(argv_path)
    if os.environ.get("APEX_DOCS_ARCHIVE"):
        cands.append(os.environ["APEX_DOCS_ARCHIVE"])
    cfg = read_config().get("archive")
    if cfg:
        cands.append(cfg)
    parent = os.path.dirname(PKG)
    cands += [
        os.path.join(parent, "Archive", "Documentation"),
        os.path.join(parent, "Documentation"),
    ]
    for c in cands:
        if not c:
            continue
        c = os.path.abspath(os.path.expanduser(c))
        if os.path.isdir(os.path.join(c, "UI")):
            return c
        # tolerate being handed the archive root rather than Documentation/
        alt = os.path.join(c, "Documentation")
        if os.path.isdir(os.path.join(alt, "UI")):
            return alt
    sys.exit(
        "Could not find the Apex documentation archive.\n"
        "Pass it explicitly:   python tools/<script>.py <path to Documentation>\n"
        "or set APEX_DOCS_ARCHIVE, or add an `archive:` line to config.md.\n"
        "Tried:\n  " + "\n  ".join(cands))


# Some source files are cp1252 bytes decoded as UTF-8; undo the common cases.
MOJIBAKE = {
    "Â·": "·", "â€œ": "“",
    "â€": "”", "â€™": "’",
    "â€‘": "‘", "â€“": "–",
    "â€”": "—", "Â ": " ", "Â": "",
}


def fix_text(s):
    if not s:
        return ""
    for bad, good in MOJIBAKE.items():
        if bad in s:
            s = s.replace(bad, good)
    s = unicodedata.normalize("NFC", s)
    s = s.replace(" ", " ")
    return s


def strip_tags(frag):
    """HTML fragment -> plain text."""
    frag = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", frag)
    txt = re.sub(r"(?s)<[^>]+>", " ", frag)
    txt = html.unescape(txt)
    txt = re.sub(r"\s+", " ", txt)
    return fix_text(txt).strip()


def slug(s, maxlen=48):
    s = strip_tags(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:maxlen].rstrip("-")) or "untitled"


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text)
