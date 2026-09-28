# Run digest: reading a run without reading its files

A production `.f06` is routinely 100–500 MB and the deck 1M+ lines. Neither
goes into the conversation. `tools/run_digest.py` streams them once and writes a
small digest plus an index; everything after that is a capped query.

## Contents

- [Running it](#running-it)
- [What the digest contains](#what-the-digest-contains)
- [Querying](#querying)
- [Finding codes](#finding-codes)
- [Limits](#limits)

## Running it

```
python tools/run_digest.py --f06 RUN.f06 --f04 RUN.f04 --log RUN.log [--bdf DECK.bdf] [-o OUT]
```

- Any subset of files works. With only an `.f06`, the deck is rebuilt from its
  SORTED BULK DATA ECHO (which is the whole bulk deck); file:line references
  then point into `OUT/deck_echo.bdf`.
- Give `--bdf` when the user has the deck: case control and header comments
  (unit system) come from it, and file:line points at their real files.
  `-I DIR` adds INCLUDE search directories.
- The output folder defaults to `<first file>_digest` next to the input. Work
  on the user's files where they are; never copy a 200 MB file into context.
- Runtime is roughly 30–40 s per million cards. scipy is used when present for
  the coincident-node search; without it a pure-Python search gives the same
  answer.
- Stdout is the digest itself; progress goes to stderr.

## What the digest contains

`OUT/digest.md` is capped at 12,000 characters, whatever the model size.

| Section | From | Holds |
|---|---|---|
| Run | .log, .f04, .f06 | version, exit code, DOF, USET totals, last f04 step, slowest steps, SOL, case control, deck header |
| Messages | .f06 | each message once with its count, first line and entities; **first fatal** and the warnings before it; short dossiers for the grids or elements a warning or fatal names |
| Solution health | .f06 | MAXRATIO lines, condition number, epsilon, OLOAD / SPCFORCE / MPCFORCE resultant totals, whether GPWG, singularity and eigenvalue tables exist, geometry-check extremes |
| Deck checks | deck | findings (codes below), errors and warnings in full, info one line each |
| Model | deck | mass estimate, units and g, load resultants in basic, active sets, parts table, contact pairs mapped to parts, coincident-grid counts |
| Where the f06 lines went | .f06 | line count per section, which shows what output bloated the file |

Other files in `OUT/`: `findings.json`, `run.json`, `messages.jsonl`,
`sections.tsv`, `deck_echo.bdf`, `index.sqlite`.

### Parts

A *part* is a set of grids joined by elements, rigid elements, or MPCs that are
active in the case control. Contact/glue is **not** part of this: the digest
reports how contact pairs join parts into assemblies (*groups*). This is what
exposes a load path that exists only through glue, or an assembly that has no
path to an SPC at all.

## Querying

```
python tools/nastran_query.py OUT <command> [args]
```

| Command | Use it for |
|---|---|
| `findings [CODE]` | every finding, or one code, with ids, file:line and the route to fix it |
| `grid ID` / `elem ID` | dossier: the card, part, attachments, property → material chain, SPCs and loads on it, findings naming it |
| `card NAME ID` | one bulk entry, every field (blank fields shown as `.`) |
| `part N` / `pair ID` | one part or one contact pair as the checks resolved it |
| `msg NUM [--limit N]` | the occurrences of a message, with their text as printed in this run |
| `section NAME [--lines N]` | one f06 section or captured block: `OLOAD`, `SPCFORCE`, `WEIGHT`, `SINGULARITY`, `EIGENVALUES`, `GEOMETRY`… |
| `grep REGEX [--file f06/f04/log/deck] [--limit] [--ctx]` | last resort; skips the f06 echo, capped |

Every command caps its output at `--max` characters (default 4,000).

## Finding codes

Severity: **error** means the run will fail or its answer is invalid;
**warn** means the answer is suspect; **info** is context. Every finding is
*computed from this deck*, the third kind of statement in
[answering-rules.md](answering-rules.md).

| Code | Sev | Meaning | What usually caused it |
|---|---|---|---|
| `INCLUDE_MISSING` | error | an INCLUDE could not be found; the deck checked is incomplete | a relative path or another directory; rerun with `-I` |
| `PARSE_PROBLEM` | warn | lines that are not cards, or cards that could not be interpreted | hand edits, tabs, truncated file |
| `DUPLICATE_ID` | error | same ID defined twice (grids; elements incl. rigid and mass; properties; materials; coords) | merged include files |
| `MISSING_GRID` | error | element/rigid/mass/SPC/load uses a grid that does not exist | deleted geometry, partial export |
| `MISSING_PROPERTY` | error | element PID not defined | property not exported or deleted |
| `PROPERTY_TYPE_MISMATCH` | error | e.g. CQUAD4 pointing at a PSOLID | PID collision between parts |
| `MISSING_MATERIAL` | error | property MID not defined | |
| `MISSING_SET` | error | LOAD/SPC/MPC in case control or a LOAD combination refers to an undefined set | renamed or deleted load set |
| `UNCONSTRAINED_GROUP` | error | an assembly (parts plus active contact) has no path to any SPC, in a static run without INREL/SUPORT | missing connection or glue; missing SPC |
| `LOAD_ON_UNATTACHED` | error | a load on a grid with no stiffness | load point left behind after remeshing |
| `SPC_ON_DEPENDENT` | error | SPC on a dependent DOF of an RBE2/RBE3/RBAR | constraint applied to an RBE spider node |
| `DOUBLE_DEPENDENT` | error | one DOF dependent in two rigid elements | overlapping RBEs |
| `FLOATING_MASS` | warn | lumped mass on a grid attached to nothing | missing RBE3/RBE2 to the structure |
| `GLUE_DEPENDENT_LOAD_PATH` | warn | the loaded part reaches its SPC only through contact/glue | intentional in assemblies; means interface quality governs the result |
| `GLUE_COARSE_SECONDARY` | warn | the secondary (tied) side of a pair is >2× coarser than the main | source/target chosen the wrong way round |
| `GLUE_UNRESOLVED` | warn | a contact pair's surface did not resolve to elements | |
| `CONTACT_NOT_ANALYSED` | warn | BGSET/BCTSET/BCTABLE present; not traced, so the part conclusions ignore them | |
| `COINCIDENT_UNMERGED` | warn | coincident grids in parts that are neither mesh-connected nor glued | missing node merge (equivalence) |
| `MIXED_UNITS` | warn | isotropic materials differ >10× in √(E/ρ) | a material in another unit system |
| `SPC_ON_UNATTACHED` | warn | SPC on a grid with nothing attached | |
| `ZERO_DENSITY` | info/warn | a material in use has ρ = 0 (warn outside statics) | |
| `POINT_LOAD_ONLY` | info | only point forces; structural inertia unloaded. Gives the equivalent g-level on the model mass when units are known | inertial case modelled as one force |
| `ORPHAN_GRID` | info | grids nothing uses | leftovers |
| `UNUSED_PROPERTY` | info | unreferenced properties/materials | leftovers |
| `UNUSED_CONTACT_SURFACE` | info | contact surfaces/bodies no active pair uses | |
| `GLUE_SAME_COMPONENT` | info | a pair joins surfaces already mesh-connected | |
| `WTMASS` | info | PARAM,WTMASS ≠ 1 scales all mass | |
| `OUTPUT_GAP` | info | no SPCFORCE request / no PARAM,GRDPNT, so reactions or mass cannot be checked | |
| `NO_CASE_CONTROL` | info | no case control found; every set treated as active | bulk-only file |

Each finding carries `route`: the `nastran-reference` entries to look up and
the `apex-docs` question to ask. Use both before telling the user how to fix it.

## Limits

State these when they matter to the answer:

- **Mass** is an estimate from geometry and density: thickness overrides,
  offsets and beam sections other than ROD/TUBE/BAR/BOX/I/CHAN/T/L are
  ignored (`not_estimated` lists what was skipped). Grid point weight output is
  authoritative.
- **Contact** is traced for BCONECT with BCSURF, BCBODY/BCBODY1 → BSURF or
  BCPROP, selected through BCTABL1. BGSET, BCTSET and BCTABLE are reported but
  not traced.
- **Coincident tolerance** is 1e-5 × model diagonal.
- **Elements** outside the connectivity table (CWELD, CFAST, CSEAM, fluid,
  axisymmetric) don't join parts; `card types not interpreted` lists them.
  CFAST/CWELD-joined models will show extra parts.
- **Messages**: the digest shows each message as printed in this run. Its
  catalogue meaning still comes from `tools/fetch_message.py`.
- **Deck from echo**: comments and INCLUDE structure are lost. The unit system
  is read from the f06 parameter echo when the header comments are there.
- **Vendor**: tested on MSC Nastran 2024–2025 output. Simcenter/NX output mostly
  parses (same banners), but its health sections may be missed.
