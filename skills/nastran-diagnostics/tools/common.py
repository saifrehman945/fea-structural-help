"""Shared helpers for the nastran-diagnostics build and fetch scripts.

MSC Nastran's error message catalogue is published only in the 2025.1 "Combined
Book", as ~20 range files (errors 0-999, 1000-1999, ...). Each range file is
~680 KB, so nothing here ever loads one whole: the index is built once, and
lookups slice a single message out of the fetched page.
"""
import html
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)

# Raw backend: serves real HTML. The portal URL is a JavaScript shell.
FETCH_URL = ("https://documentation-be.hexagon.com/bundle/{bundle}"
             "/raw/resource/enus/{path}")
CITE_URL = ("https://nexus.hexagon.com/documentationcenter/en-US/bundle/{bundle}"
            "/page/{path}")

DEFAULT_BUNDLE = "MSC_Nastran_2025.1"
BOOK = "Nastran_Combined_Book/errormsg"
OVERVIEW = BOOK + "/em_overview/TOC.MSC.Nastran.Error1.xhtml"

# Every message begins with this banner. There is no per-message element in the
# markup -- the whole range file is flat <p class="FM_Body"> -- so this boundary
# is what makes single-message extraction possible.
MSG_RE = re.compile(
    r"\*\*\*\s*(USER|SYSTEM)\s+(FATAL|WARNING|INFORMATION)\s+MESSAGE\s+"
    r"(\d+)\s*\(([^)]*)\)")

# Each entry is preceded by its ordinal on a line of its own: "740.0", or
# "7.1" for the second variant of message 7.
ORD_RE = re.compile(r"^[ 	]*(\d+)\.(\d+)[ 	]*$", re.M)

SEVERITY = {
    ("USER", "FATAL"): "UFM", ("SYSTEM", "FATAL"): "SFM",
    ("USER", "WARNING"): "UWM", ("SYSTEM", "WARNING"): "SWM",
    ("USER", "INFORMATION"): "UIM", ("SYSTEM", "INFORMATION"): "SIM",
}


def read_config():
    cfg = {"bundle": DEFAULT_BUNDLE}
    path = os.path.join(PKG, "config.md")
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^\s*-?\s*bundle\s*:\s*(\S+)\s*$", line)
            if m and not m.group(1).startswith("<"):
                cfg["bundle"] = m.group(1).strip().strip("`")
    return cfg


def fix_text(s):
    if not s:
        return ""
    s = s.replace("Â ", " ").replace(" ", " ")
    return unicodedata.normalize("NFC", s)


def page_text(s):
    """Range-file HTML -> flat text, one paragraph per line."""
    s = re.sub(r"(?is)<(script|style|head)\b.*?</\1>", " ", s)
    s = re.sub(r"(?is)</p>", "\n", s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    t = re.sub(r"(?s)<[^>]+>", " ", s)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return fix_text(t)


def tidy(block):
    """Clean one extracted message block."""
    lines = [ln.strip() for ln in block.splitlines()]
    lines = [ln for ln in lines if ln]
    # The next message's ordinal ("320.0") trails the previous block.
    while lines and re.fullmatch(r"\d+(\.\d+)?", lines[-1]):
        lines.pop()
    return "\n".join(lines).strip()


def split_messages(text):
    """-> [(number, severity_code, module, block_text)] in document order.

    Blocks are delimited by the ordinal that precedes each entry ("740.0",
    "7.1" = message 7, variant 1), NOT by the `*** ... MESSAGE n` banner. Whole
    message families -- the 15000s among them -- carry no banner at all and are
    invisible to a banner-based split.
    """
    hits = list(ORD_RE.finditer(text))
    out = []
    for i, h in enumerate(hits):
        start = h.end()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        block = text[start:end]
        num = int(h.group(1))
        banner = MSG_RE.search(block)
        if banner:
            code = SEVERITY.get((banner.group(1), banner.group(2)),
                                banner.group(1)[0] + "?M")
            module = banner.group(4).strip()
            # trust the banner's number over the ordinal when they disagree
            num = int(banner.group(3))
        else:
            code, module = "-", ""
        body = tidy(block)
        if body:
            out.append((num, code, module, body))
    return out


def first_line(block):
    """The message text itself, without the banner line."""
    lines = block.splitlines()
    body = [ln for ln in lines[1:]
            if not re.match(r"(?i)^(user|system) (information|action)\s*:", ln)]
    return body[0] if body else (lines[0] if lines else "")


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
