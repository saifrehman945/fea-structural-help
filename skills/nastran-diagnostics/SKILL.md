---
name: nastran-diagnostics
description: Diagnose failed or suspect MSC Nastran runs. Use when a solve has stopped, errored, or produced results that look wrong, and when the user quotes a Nastran message number or message text (UFM, SFM, UWM, SWM, "USER FATAL MESSAGE 740", "singular matrix", "rigid body modes"), pastes .f06 or .log output, or asks why a run failed, would not converge, or gave implausible answers. Covers the MSC Nastran error message catalogue and a triage method for reading solver output. For what a bulk data entry or case control command means, use nastran-reference. For the Apex GUI, use apex-docs. For writing Apex Python, use apex-scripting.
---

# Nastran diagnostics

## Overview

Explain what a Nastran message means, and help work out why *this* run produced
it — keeping those two things visibly separate.

The message catalogue is published only in the MSC Nastran 2025.1 "Combined
Book", as ~20 range files of roughly 680 KB each. This skill indexes every
message locally (number, severity, module, text) and pulls the full
`User information` / `User action` prose one message at a time, so a lookup
costs a few hundred characters rather than a whole page.

## Required workflow

1. **Find the first fatal, not the last.** Nastran commonly reports a
   consequence; the cause is usually an earlier warning. If the user pasted
   output, read upward from the failure.
2. **Read the message properly** — never from memory:
   ```
   python tools/fetch_message.py <number>
   ```
   Message numbers are reused across modules, so the module in the banner
   matters. `--all` shows every variant of a number.
3. **Quote what the catalogue says** — the message text and its `User action`.
4. **Then diagnose the model**, clearly marked as engineering reasoning. Use
   [references/f06-triage.md](references/f06-triage.md) for the method.
5. **Hand over** anything that belongs to a sibling skill.

## The citation contract

The catalogue tells you what a message *means*. It almost never tells you why
your model produced it. That second half is extrapolation and must be marked.

**Documented:**

> `*** USER FATAL MESSAGE 740 (RDASGN)` — UNIT NUMBER %1 HAS ALREADY BEEN
> ASSIGNED TO THE LOGICAL NAME %2.
> *User action:* CHANGE THE UNIT NUMBER ON THE ASSIGN STATEMENT …
> — MSC Nastran 2025.1 error message list

**Not documented:**

> **Not found in the documentation — general engineering knowledge:** with an
> Apex-exported deck this usually means …

Never invent a message number, its text, or its module. If
`fetch_message.py` finds nothing, the answer is "not in the catalogue" — numbers
are sparse and some ranges are unpublished.

## What is here

| Surface | Holds |
|---|---|
| `index/messages-*.md` | every indexed message: number, severity, module, text |
| `index/ranges.md` | which range file holds a number, and its source page |
| `tools/fetch_message.py` | the full cause/action prose for one message |
| `references/f06-triage.md` | how to work through solver output |
| `references/answering-rules.md` | the citation and extrapolation contract |

Severity codes: `UFM` user fatal, `SFM` system fatal, `UWM` user warning,
`SWM` system warning, `UIM`/`SIM` information.

To search by symptom rather than number, grep the indexes:

```
grep -i "singular" index/messages-*.md
```

## Answering rules

1. Lead with what the message says, then what to check, then the caveats.
2. A warning the run survived can still be why the answer is wrong. Do not
   dismiss warnings because the job completed.
3. Say when you are reasoning about the model rather than quoting the
   catalogue — which is most of any useful diagnosis.
4. If the fetch fails, `index/messages-*.md` still has the message text. Say the
   cause/action prose could not be retrieved; do not supply your own in its
   place.
5. State the release. The catalogue is 2025.1; a different solver may word or
   number things differently.
6. The user is an experienced FEA engineer. Give the diagnosis and the next
   check, not an FEA tutorial.

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
python tools/validate.py                  # must exit 0
```

The portal refuses sustained request bursts, surfacing as DNS or
connection-reset errors rather than a 429. Both tools retry with backoff, and
`--resume` skips ranges already built.

## References

- [references/answering-rules.md](references/answering-rules.md): citation and extrapolation contract
- [references/f06-triage.md](references/f06-triage.md): how to triage a failed or suspect run
