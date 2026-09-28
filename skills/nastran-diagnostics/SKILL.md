---
name: nastran-diagnostics
description: Diagnose failed or suspect MSC Nastran runs. Use when a solve has stopped, errored, or produced results that look wrong; when the user attaches or points at .f06, .f04, .log or .bdf/.dat files (of any size) and asks what went wrong or whether the model is sound; and when the user quotes a Nastran message number or message text (UFM, SFM, UWM, SWM, "USER FATAL MESSAGE 740", "singular matrix", "rigid body modes"), or asks why a run failed, would not converge, or gave implausible answers. Digests huge output and decks without reading them into context, checks the deck for connectivity, load-path, constraint, mass and reference faults, and explains messages from the MSC Nastran error catalogue. For what a bulk data entry or case control command means, use nastran-reference. For the Apex GUI, use apex-docs. For writing Apex Python, use apex-scripting.
---

# Nastran diagnostics

## Overview

Work out why a Nastran run failed or gave suspect answers, keeping three kinds
of statement visibly separate:

1. **Documented**: what a message means, from the MSC Nastran 2025.1 catalogue.
2. **Computed**: facts about *this* deck and run, produced by the tools here.
3. **Extrapolated**: engineering reasoning about why, which is marked as such.

Run files are too big to read. A production `.f06` is hundreds of MB and the
deck a million lines. **Never `Read`, `cat` or paste a raw .f06, .bdf, .dat or
.pch.** Digest it, then query it.

## Required workflow

0. **Digest the run first** whenever files are available, even if the user only
   asks about one message:
   ```
   python tools/run_digest.py --f06 RUN.f06 --f04 RUN.f04 --log RUN.log [--bdf DECK.bdf] -o OUT
   ```
   Pass whichever files exist. Without `--bdf`, the deck is rebuilt from the
   f06 bulk data echo. The command prints `OUT/digest.md` (≤12k characters):
   exit status, deduplicated messages with the first fatal, solution health,
   deck findings, parts and contact load path, mass, units and loads. Read it
   before anything else. Details: [references/run-digest.md](references/run-digest.md).
1. **Find the first fatal, not the last.** The digest names it and lists the
   warnings before it. A clean exit is not a clean model: go through the deck
   findings even when `EXIT(0)`.
2. **Read each message properly**, never from memory:
   ```
   python tools/fetch_message.py <number>
   ```
   Message numbers are reused across modules, so the module in the banner
   matters. `--all` shows every variant.
3. **Pull specifics with capped queries, not file reads:**
   ```
   python tools/nastran_query.py OUT findings [CODE]
   python tools/nastran_query.py OUT grid <id> | elem <id> | card <NAME> <id>
   python tools/nastran_query.py OUT part <n> | pair <id> | msg <num> | section <name>
   ```
4. **Tie messages to findings.** A singularity fatal plus
   `UNCONSTRAINED_GROUP`, or a MAXRATIO warning plus `GLUE_COARSE_SECONDARY`,
   is a diagnosis. Use the grid and element dossiers to connect the IDs a
   message names to the part and card they belong to.
5. **Quote what the catalogue says**: the message text and its `User action`.
6. **Diagnose the model**, citing the computed facts and marking the reasoning.
   Use [references/f06-triage.md](references/f06-triage.md) for the method.
7. **Route the fix.** Each finding's `route` names the `nastran-reference`
   entries and the `apex-docs` question. Look them up; don't describe card
   fields or GUI steps from memory.

## The citation contract

**Documented**, quoted from the catalogue:

> `*** USER FATAL MESSAGE 740 (RDASGN)` - UNIT NUMBER %1 HAS ALREADY BEEN
> ASSIGNED TO THE LOGICAL NAME %2.
> *User action:* CHANGE THE UNIT NUMBER ON THE ASSIGN STATEMENT …
> - MSC Nastran 2025.1 error message list

**Computed** from this run, with the finding code or query as the source:

> **From your deck (`FLOATING_MASS`):** CONM2 6700330 (0.16) sits on GRID
> 7131745, which no element or RBE connects to.

**Not documented**, general engineering knowledge:

> **Not found in the documentation - general engineering knowledge:** with an
> Apex-exported deck this usually means …

Never invent a message number, its text, or its module. If `fetch_message.py`
finds nothing, the answer is "not in the catalogue". Numbers are sparse and
some ranges are unpublished. Never present a computed figure (mass, resultant,
part count) as if the solver printed it; say where it came from and its limits.

## What is here

| Surface | Holds |
|---|---|
| `tools/run_digest.py` | streams .f06/.f04/.log (+ deck) into `digest.md`, `findings.json`, `index.sqlite` |
| `tools/nastran_query.py` | capped lookups into a digest: findings, grid/element dossiers, cards, parts, contact pairs, messages, sections |
| `tools/deck_checks.py` | the deck checks on their own: `python tools/deck_checks.py DECK.bdf` |
| `tools/deck_reader.py` | tolerant tokenizer: small/large/free field, continuations, INCLUDE |
| `tools/fetch_message.py` | the full cause/action prose for one message |
| `index/messages-*.md` | every indexed message: number, severity, module, text |
| `index/ranges.md` | which range file holds a number, and its source page |
| `references/run-digest.md` | digest contents, query commands, **finding codes**, limits |
| `references/f06-triage.md` | how to work through solver output |
| `references/answering-rules.md` | the citation and extrapolation contract |

The tools are stdlib-only Python 3; scipy is used when present.

Severity codes: `UFM` user fatal, `SFM` system fatal, `UWM` user warning,
`SWM` system warning, `UIM`/`SIM` information.

To search the catalogue by symptom rather than number:

```
grep -i "singular" index/messages-*.md
```

## Answering rules

1. Lead with the verdict: failed or not, and the first thing that is wrong.
   Then what the messages say, what the deck shows, what to check, and caveats.
2. A warning the run survived can still be why the answer is wrong, and so can
   a deck finding with no message at all. Don't dismiss either because the job
   completed.
3. Say which statements are catalogue, which are computed, and which are
   reasoning. Most of a useful diagnosis is the last two.
4. If the fetch fails, `index/messages-*.md` still has the message text. Say the
   cause/action prose could not be retrieved; don't supply your own.
5. State the release. The catalogue is 2025.1; a different solver may word or
   number things differently.
6. The user is an experienced FEA engineer. Give the diagnosis and the next
   check, not an FEA tutorial.
7. If the digest reports `INCLUDE_MISSING`, `CONTACT_NOT_ANALYSED` or card types
   not interpreted, say the conclusions are partial and why.

## Handing over

| The question is really about | Skill |
|---|---|
| What a bulk data entry or case control command does | `nastran-reference` |
| How to change the model in the Apex GUI | `apex-docs` |
| Writing or fixing Apex Python | `apex-scripting` |
| Whether the result is believable, or how to model it better | `fea-modelling-strategy` |

## Maintenance

```
python tools/build_messages.py --resume   # fetch any missing ranges
python tools/validate.py                  # must exit 0; --offline skips the network check
```

`validate.py` also runs the digest tools against `tests/fixtures/`: a deck
seeded with one of each fault, a glued assembly, and a synthetic f06. When you
add a check, seed its fault there too.

The portal refuses sustained request bursts, surfacing as DNS or
connection-reset errors rather than a 429. Both tools retry with backoff, and
`--resume` skips ranges already built.

## References

- [references/run-digest.md](references/run-digest.md): digest, queries, finding codes, limits
- [references/answering-rules.md](references/answering-rules.md): citation and extrapolation contract
- [references/f06-triage.md](references/f06-triage.md): how to triage a failed or suspect run
