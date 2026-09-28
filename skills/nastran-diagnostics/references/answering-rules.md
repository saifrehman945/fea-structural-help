# Answering rules

Debugging is where confident invention does the most damage: a plausible-sounding
explanation of a message number sends someone rebuilding a model for the wrong
reason. So this skill is strict about the line between what the message
catalogue says and what you are inferring.

## The three kinds of statement

**1. Documented.** The message text, and its `User information` / `User action`
prose, exactly as published.

> `*** USER FATAL MESSAGE 740 (RDASGN)` — UNIT NUMBER %1 HAS ALREADY BEEN
> ASSIGNED TO THE LOGICAL NAME %2
> *User action:* CHANGE THE UNIT NUMBER ON THE ASSIGN STATEMENT …
> — MSC Nastran 2025.1 error message list

**2. Extrapolated.** Why it happened *in this model*, and what to do about it.

> **Not found in the documentation — general engineering knowledge:** in an Apex
> export this usually means two ASSIGN statements collided …

**3. Computed.** A fact about *this* deck or run produced by the tools:
a finding from `run_digest.py` / `deck_checks.py`, a query result, a figure
read from the `.f06`. Cite the finding code or the query.

> **From your deck (`UNCONSTRAINED_GROUP`):** part 2 (9 grids, PSHELL 2) has no
> path to any SPC and carries LOAD 10.

Computed facts are neither catalogue text nor guesswork, but they have limits
(mass is an estimate, contact is traced only for some card families; see
[run-digest.md](run-digest.md#limits)). State the limit when the answer leans
on it. *Why* the deck ended up that way is still extrapolation.

The catalogue tells you what a message means. It almost never tells you why your
particular model produced it. **That second half is nearly always extrapolation,
and must be marked**, however obvious it feels.

## Always read the message before explaining it

Do not explain a message number from memory. Run:

```
python tools/fetch_message.py <number>
```

It slices the single message out of the range file, so this costs a few hundred
characters. Message numbers are reused across severities and modules — the same
number can be a UFM in one module and a UWM in another — so the module in the
banner matters.

If the fetch fails, `index/messages-*.md` still has the message text. Say that
the cause and action prose could not be retrieved rather than supplying your own
in its place.

## Required disclosures

| Situation | Say |
|---|---|
| The message could not be fetched | that you have the index text only, and give the URL |
| The number has several variants | which module's variant you are describing, and that others exist |
| The number is not in the catalogue | plainly — numbers are sparse and some ranges are unpublished |
| You are diagnosing the model, not the message | mark it as engineering reasoning |
| A statement comes from the digest or a query | say so, and name the finding code |
| The digest's conclusions are partial (missing INCLUDE, untraced contact) | say what was not checked |
| The run's real problem is upstream of the message | say so — the first fatal is often a symptom |

## What never to do

1. **Never invent a message number, its text, or its module.** If
   `fetch_message.py` returns nothing, the answer is "not in the catalogue".
2. Never treat the last fatal message as the cause. Nastran often reports a
   consequence; the useful message is usually the **first** warning or fatal in
   the `.f06`.
3. Never assert a solver behaviour the message does not state. Whether a model
   is under-constrained, ill-conditioned, or simply mis-specified is a
   conclusion you reach, not something the catalogue says.
4. Never write or debug Apex Python here — that is `apex-scripting`.
5. Never explain a bulk data entry's fields from memory; that is
   `nastran-reference`, which has the QRG index.
6. Never `Read` a raw `.f06`, `.bdf`, `.dat` or `.pch` into the conversation.
   Run `tools/run_digest.py` and query the result.

## Answer shape

1. **What the message says** — quoted, with its severity and module.
2. **What that means** — the published `User information` / `User action`.
3. **What the deck shows**: the relevant computed findings, cited by code.
4. **What to check in this model**, marked as engineering reasoning and ordered
   most-likely first.
5. **What to look for elsewhere in the `.f06`**: preceding warnings, the
   epsilon/MAXRATIO lines, the mass and applied-load summaries. The digest has
   them already.
6. **How to fix it**, via the finding's route to `nastran-reference` and
   `apex-docs`.

The user is an experienced FEA engineer. Give the diagnosis and the next check,
not a tutorial on finite elements.
