# Anatomy of a Nastran deck

Which part of the input file a keyword belongs to, and which index covers it.
Getting the section wrong is a common source of confusion: the same word can be
a case control command and a bulk data entry, and they mean different things.

The section order below is the order the documentation itself is organised in —
`index/keywords.md` records which section each keyword came from.

## The sections, in file order

| # | Section | What it does | Index |
|---|---|---|---|
| 1 | `NASTRAN` statement | system cells: memory, machine and solver behaviour before anything else runs | `nastran-statement.md` |
| 2 | File Management | `ASSIGN`, `DBLOCATE`, database and file attachment | `file-management.md` |
| 3 | Executive Control | `SOL` (which solution sequence), `TIME`, `DIAG`, ends at `CEND` | `executive-control.md` |
| 4 | Case Control | what to solve and what to output: `SUBCASE`, `LOAD`, `SPC`, `DISPLACEMENT`, `STRESS`. Ends at `BEGIN BULK` | `case-control.md` |
| 5 | Bulk Data | the model: grids, elements, properties, materials, loads, constraints. `BEGIN BULK` to `ENDDATA` | `bulk-data.md` |

Reference Guide material — element formulations, solution sequence descriptions,
grid points and coordinate systems — is in `reference-guide.md` and describes
behaviour rather than syntax.

## The distinction that trips people up

**Case control selects; bulk data defines.** A load is defined in the bulk data
with an ID, and *selected* for a subcase by a case control command referring to
that ID. Asking "what does LOAD do" has two valid answers depending on which
section is meant, and `index/keywords.md` will show both.

The same applies to `SPC`, `MPC`, `TEMPERATURE` and several others.

## Reading an entry's format

Bulk data entries are **positional**, laid out in ten fields across a line, with
continuations. The documentation shows a numbered format table, then a
"Describer / Meaning" table giving each field's type and valid range.

Two things to carry into any answer:

- **Field position matters as much as field name.** A value in the wrong field
  is usually still a legal deck, so the solver runs and the answer is wrong.
- **Blank is not zero.** Many fields mean something specific when left blank,
  and the Describer table says what. Never assume a default you have not read.

## What is not here

- **Message numbers and run failures** — `nastran-diagnostics`.
- **How Apex writes any of this** — `apex-docs`. Apex generates the deck, so the
  question "why is this entry like that" is often really a question about a
  modelling choice in Apex.
- **Which approach to choose** — `fea-modelling-strategy`. The QRG says what a
  keyword does, not when to use it.
