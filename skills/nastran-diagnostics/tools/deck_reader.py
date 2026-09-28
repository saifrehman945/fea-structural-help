"""Tolerant Nastran deck reader - stdlib only, never raises on bad input.

Why not pyNastran: it is strict about field formats and rejects card types it
does not know (all of the BCONECT/BCSURF glue family, for example), and a deck
that crashes a parser is exactly the deck being diagnosed. This reader only
tokenises; it knows nothing about card meaning. deck_checks.py interprets.

Field addressing ("flattened" fields), used everywhere downstream:

    fields[0]              card name, upper case, '*' stripped
    fields[1..8]           data fields of the first physical line
    fields[9..16]          data fields of the first continuation
    fields[8k+1..8k+8]     data fields of continuation k

so the QRG's "field n on line k" is fields[8*k + n - 1]. Small field, large
field (16-character, '*'), free field (commas) and mixed continuations all land
in the same layout.

    for card in read_deck("model.bdf"):
        card.name, card.fields, card.file, card.line
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

__all__ = ["Card", "Deck", "read_deck", "read_sections", "to_int", "to_float"]


@dataclass
class Card:
    name: str
    fields: list
    file: str
    line: int

    def f(self, i, default=""):
        return self.fields[i] if i < len(self.fields) else default

    def i(self, i, default=None):
        return to_int(self.f(i), default)

    def r(self, i, default=None):
        return to_float(self.f(i), default)

    @property
    def loc(self):
        return "%s:%d" % (os.path.basename(self.file), self.line)


@dataclass
class Deck:
    """What read_sections() returns besides the bulk cards."""
    executive: list = field(default_factory=list)      # (text, file, line)
    case_control: list = field(default_factory=list)   # (text, file, line)
    comments: list = field(default_factory=list)       # header $ comments (first 200)
    includes: list = field(default_factory=list)       # (path, found)
    problems: list = field(default_factory=list)       # (file, line, message)
    has_cend: bool = False
    has_begin_bulk: bool = False
    has_enddata: bool = False


# ------------------------------------------------------------------ values
_RX_NASTRAN_EXP = re.compile(r"^([+-]?(?:\d+\.?\d*|\.\d+))([+-]\d+)$")


def to_int(s, default=None):
    s = (s or "").strip()
    if not s:
        return default
    try:
        return int(s)
    except ValueError:
        return default


def to_float(s, default=None):
    """Nastran reals: 1.5, 1.5E-3, 1.5D-3, 1.5-3, .5+2, 12."""
    s = (s or "").strip().upper().replace("D", "E")
    if not s:
        return default
    try:
        return float(s)
    except ValueError:
        m = _RX_NASTRAN_EXP.match(s)
        if m:
            try:
                return float(m.group(1) + "E" + m.group(2))
            except ValueError:
                return default
        return default


# ------------------------------------------------------------------ lines -> fields
def _split_physical(line: str):
    """One physical line -> (head, [8 data fields], is_large).

    head is field 1 (name or continuation marker)."""
    body = line.split("$", 1)[0].rstrip("\r\n")
    if "," in body[:80]:
        toks = [t.strip() for t in body.split(",")]
        head = toks[0]
        data = toks[1:]
        large = head.endswith("*")
        if large:
            # free-field large: 4 data fields per physical line
            data = (data + [""] * 4)[:4] + [""] * 0
            return head, data, True
        return head, (data + [""] * 8)[:8], False
    body = body.expandtabs(8)
    head = body[:8].strip()
    if head.endswith("*") or head.startswith("*"):
        data = [body[8 + 16 * k: 24 + 16 * k].strip() for k in range(4)]
        return head, data, True
    data = [body[8 + 8 * k: 16 + 8 * k].strip() for k in range(8)]
    return head, data, False


def _is_continuation(line: str) -> bool:
    s = line.split("$", 1)[0]
    if not s.strip():
        return False
    c = s[:1]
    if c in "+*,":
        return True
    # blank field 1 means continuation in fixed format
    return s[:8].strip() == "" and len(s.rstrip()) > 8


class _Builder:
    def __init__(self, head, data, large, file, line):
        self.name = head.rstrip("*").strip().upper()
        self.file, self.line = file, line
        self.fields = [self.name]
        self.half = None           # pending first half of a large-field pair
        self._add(data, large)

    def _add(self, data, large):
        if large:
            if self.half is None:
                self.half = data
            else:
                self.fields += self.half + data
                self.half = None
        else:
            if self.half is not None:            # large line not paired - pad
                self.fields += self.half + [""] * 4
                self.half = None
            self.fields += data

    def add(self, head, data, large):
        self._add(data, large)

    def card(self):
        if self.half is not None:
            self.fields += self.half + [""] * 4
        f = self.fields
        while len(f) > 1 and f[-1] == "":
            f.pop()
        return Card(self.name, f, self.file, self.line)


# ------------------------------------------------------------------ files
_RX_INCLUDE = re.compile(r"^\s*INCLUDE\s+(.*)$", re.I)


def _resolve_include(spec, cur_file, include_dirs):
    spec = spec.strip().strip("'\"").strip()
    cands = [spec, os.path.join(os.path.dirname(cur_file), spec)]
    cands += [os.path.join(d, spec) for d in include_dirs]
    for c in cands:
        if os.path.isfile(c):
            return c
    base = os.path.basename(spec.replace("\\", "/"))
    for d in [os.path.dirname(cur_file)] + list(include_dirs):
        c = os.path.join(d, base)
        if os.path.isfile(c):
            return c
    return None


def _lines(path, deck, include_dirs, depth=0):
    """Yield (file, lineno, text) following INCLUDEs."""
    try:
        fh = open(path, "r", errors="replace")
    except OSError as e:
        deck.problems.append((path, 0, "cannot open: %s" % e))
        return
    with fh:
        pending = None
        for n, line in enumerate(fh, 1):
            m = _RX_INCLUDE.match(line) if pending is None else None
            if pending is not None or m:
                txt = (pending or "") + (m.group(1) if m else line.strip())
                if txt.count("'") == 1 or txt.count('"') == 1:
                    pending = txt                     # quoted path continues
                    continue
                pending = None
                inc = _resolve_include(txt, path, include_dirs)
                deck.includes.append((txt.strip().strip("'\""), bool(inc)))
                if not inc:
                    deck.problems.append((path, n, "INCLUDE not found: %s" % txt.strip()))
                elif depth > 20:
                    deck.problems.append((path, n, "INCLUDE nesting too deep"))
                else:
                    yield from _lines(inc, deck, include_dirs, depth + 1)
                continue
            yield path, n, line


def read_sections(path, include_dirs=()):
    """Return (deck, bulk_card_iterator). Consume the iterator once."""
    deck = Deck()
    gen = _lines(path, deck, include_dirs)

    # Is there an executive/case section? Peek for CEND/BEGIN BULK.
    buf = []
    mode = "bulk"
    for item in gen:
        buf.append(item)
        u = item[2].strip().upper()
        if u.startswith("CEND") or u.startswith("SOL ") or u.startswith("BEGIN BULK") \
                or u.startswith("BEGIN SUPER") or u.startswith("SUBCASE"):
            mode = "exec"
            break
        if len(buf) > 400:
            break
    if mode == "exec":
        # all lines so far are executive (or case control)
        pass

    def all_lines():
        yield from buf
        yield from gen

    def bulk():
        section = "exec" if mode == "exec" else "bulk"
        cur = None
        for fname, n, line in all_lines():
            s = line.rstrip("\r\n")
            if section != "bulk":
                u = s.strip().upper()
                if s.lstrip().startswith("$"):
                    if len(deck.comments) < 200:
                        deck.comments.append(s.strip().lstrip("$").strip())
                    continue
                if u.startswith("BEGIN") and "BULK" in u:
                    deck.has_begin_bulk = True
                    section = "bulk"
                    continue
                if section == "exec":
                    if u.startswith("CEND"):
                        deck.has_cend = True
                        section = "case"
                        continue
                    if u:
                        deck.executive.append((s.strip(), fname, n))
                    continue
                if u.startswith("BEGIN") and "BULK" in u:
                    deck.has_begin_bulk = True
                    section = "bulk"
                    continue
                if u:
                    deck.case_control.append((s.strip(), fname, n))
                continue
            # ---- bulk
            if not s.strip() or s.lstrip().startswith("$"):
                if s.lstrip().startswith("$") and len(deck.comments) < 200:
                    deck.comments.append(s.strip().lstrip("$").strip())
                continue
            if s.strip().upper().startswith("ENDDATA"):
                deck.has_enddata = True
                break
            if s.strip().upper().startswith("BEGIN"):
                continue
            try:
                head, data, large = _split_physical(s)
            except Exception as e:  # noqa: BLE001 - never raise
                deck.problems.append((fname, n, "unreadable line: %s" % e))
                continue
            if cur is not None and _is_continuation(s):
                cur.add(head, data, large)
                continue
            if cur is not None:
                yield cur.card()
            if not head or not re.match(r"^[A-Za-z][A-Za-z0-9]*\*?$", head):
                deck.problems.append((fname, n, "not a card: %r" % s[:40]))
                cur = None
                continue
            cur = _Builder(head, data, large, fname, n)
        if cur is not None:
            yield cur.card()

    return deck, bulk()


def read_deck(path, include_dirs=()):
    """Convenience: iterate bulk cards only."""
    _, it = read_sections(path, include_dirs)
    yield from it


# ------------------------------------------------------------------ case control
_RX_CC = re.compile(r"^\s*([A-Z][A-Z0-9]*)(\([^)]*\))?\s*=\s*(.+?)\s*$", re.I)


def parse_case_control(lines):
    """[(text,...)] -> {'global': {KEY: val}, 'subcases': {id: {KEY: val}}, 'params': [..]}."""
    out = {"global": {}, "subcases": {}, "params": []}
    cur = out["global"]
    for item in lines:
        t = item[0] if isinstance(item, tuple) else item
        t = t.split("$", 1)[0].strip()
        if not t:
            continue
        u = t.upper()
        if u.startswith("SUBCASE"):
            sid = to_int(u.split()[1] if len(u.split()) > 1 else "", 0)
            cur = out["subcases"].setdefault(sid, {})
            continue
        if u.startswith("PARAM"):
            out["params"].append(u)
            continue
        m = _RX_CC.match(t)
        if m:
            key = m.group(1).upper()
            cur[key] = m.group(3).strip().upper()
    return out
