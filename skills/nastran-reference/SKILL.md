---
name: nastran-reference
description: Look up MSC Nastran deck keywords and solver reference material. Use when the user asks what a bulk data entry, case control command, executive control statement, parameter or system cell does (CQUAD4, PSHELL, RBE2, RBE3, PCOMP, PARAM, SPC, LOAD, SUBCASE, SOL), what a field or its default means, which entry to use for something, how a Nastran deck is structured, or what a solution sequence covers. Grounded in the published MSC Nastran Quick Reference Guide and Reference Guide, with citations. For diagnosing a failed run or a message number, use nastran-diagnostics. For the Apex GUI, use apex-docs. For writing Apex Python, use apex-scripting.
---

# Nastran reference

## Overview

Answer questions about Nastran deck keywords from the published documentation,
with citations, and mark clearly anything that goes beyond what the docs say.

The portal cannot be searched: it is a JavaScript app with no listing and no
full-text search, and individual topic pages carry no outbound links. The
bundled index is how a keyword becomes a page; `tools/fetch_page.py` is how you
read one.

**Nastran fields are positional.** A wrong field number produces a deck that
runs and gives wrong answers, silently. Never state an entry's format without
fetching it.

## Required workflow

1. **Find the keyword.** Grep `index/keywords.md` — every indexed keyword across
   the Quick Reference Guide and Reference Guide, flat. Nastran has many
   near-miss names (`CQUAD4`/`CQUADR`/`CQUAD8`, `PBAR`/`PBARL`), so confirm you
   have the one the user means.
2. **Read the page** — never answer an entry's format from memory:
   ```
   python tools/fetch_page.py PSHELL
   python tools/fetch_page.py PSHELL --brief   # first ~1500 chars
   ```
3. **Answer under the contract** in
   [references/answering-rules.md](references/answering-rules.md): cite what is
   documented, mark what is not.
4. **State the release.** Entries gain and lose fields between versions.

## The citation contract

**Documented** — cite keyword, release and URL:

> `PSHELL` MID2 is the material identification number for bending.
> — [PSHELL, MSC Nastran 2025.2 QRG](https://nexus.hexagon.com/...)

`python tools/fetch_page.py <KEYWORD> --url` prints the exact citation URL.

**Not documented** — say so in the sentence:

> **Not found in the documentation — general engineering knowledge:** leaving
> MID2 blank makes the shell a membrane, which is usually wrong on a part
> carrying bending.

Never invent a field name, a field position, or a default.

## What is here

| Surface | Holds |
|---|---|
| `index/keywords.md` | every indexed keyword, flat and greppable — **start here** |
| `index/bulk-data.md` | bulk data entries |
| `index/case-control.md` | case control commands |
| `index/executive-control.md`, `index/file-management.md` | deck control statements |
| `index/nastran-statement.md` | the NASTRAN statement and system cells |
| `index/reference-guide.md` | Reference Guide topics: elements, solution sequences, grid points |
| `tools/fetch_page.py` | read a page by keyword |

Releases are set per book in `config.md`: the Quick Reference Guide and
Reference Guide come from **2025.2**.

## Answering rules

1. Lead with what the keyword is, then the fields that matter to the question,
   then the caveats.
2. Quote the field layout when the question is about usage. Describe fields by
   name *and* position.
3. Note documented interactions — many entries are only meaningful alongside
   another (a property entry with its element entry, a load with its `LOAD`
   case control command).
4. Say when the user's solver release may differ from the indexed one.
5. If a keyword is not in the index, say it is not in the indexed QRG/Reference
   Guide — not that it does not exist. Some books are not indexed, and
   error messages are a separate skill.
6. The user is an experienced FEA engineer. Give field semantics and
   consequences, not an introduction to finite elements.

## Handing over

| The question is really about | Skill |
|---|---|
| A message number, or why a run failed | `nastran-diagnostics` |
| Doing it in the Apex GUI | `apex-docs` |
| Writing or fixing Apex Python | `apex-scripting` |
| Which modelling approach to choose | `fea-modelling-strategy` |

## Maintenance

```
python tools/build_index.py     # rebuild indexes (network, a few minutes)
python tools/validate.py        # must exit 0
```

The portal refuses sustained request bursts, surfacing as DNS or
connection-reset errors rather than a 429; the builder retries with backoff.

## References

- [references/answering-rules.md](references/answering-rules.md): citation and extrapolation contract
- [references/deck-anatomy.md](references/deck-anatomy.md): how a Nastran deck is structured, and which index covers each section
