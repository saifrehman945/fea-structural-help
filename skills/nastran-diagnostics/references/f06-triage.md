# Triaging a failed or suspect run

A method for working through Nastran output. **Almost nothing on this page is
quoted from the message catalogue** — the catalogue explains individual messages,
not how to diagnose a run. Treat this file as engineering method, and say so when
you use it: it is exactly the material `references/answering-rules.md` requires
you to mark as reasoning rather than documentation.

What *is* documented is each message's own text and `User action`, which
`tools/fetch_message.py` retrieves. Quote that; reason with this.

## Order of work

1. **Find the first `*** USER FATAL` or `*** SYSTEM FATAL`, not the last.**
   A fatal often reports the consequence of something a warning flagged earlier.
2. **Read that message properly** — `python tools/fetch_message.py <number>` —
   including its module, which disambiguates reused numbers.
3. **Read the warnings above it.** Singularity, constraint and geometry warnings
   usually precede the fatal that stops the run.
4. **Only then form a hypothesis about the model**, and label it as such.

## Severity codes

Verified from the catalogue itself:

| Code | Meaning |
|---|---|
| `UFM` | user fatal — the run stops |
| `SFM` | system fatal — the run stops |
| `UWM` | user warning — the run continues |
| `SWM` | system warning — the run continues |
| `UIM` / `SIM` | information |

A warning that the run survived can still be the reason the answer is wrong. Do
not dismiss warnings because the job completed.

## Symptom → where to look

Engineering method, not documentation. Each row is a place to look, not a
diagnosis.

| Symptom | Look at |
|---|---|
| Run stops immediately, no results | first fatal; deck syntax; missing referenced ID |
| "Not a valid entry" style fatals | the entry in `nastran-reference` — field position matters |
| Singular matrix / constraint fatals | grounding, AUTOSPC report, unconnected parts, coincident-but-unmerged nodes |
| Free-free or rigid-body behaviour | expected in an unconstrained modal run; a defect in a static one |
| Results exist but look wrong | applied load resultant vs reaction resultant; units; property assignment |
| Wildly high displacement | a part connected only through a weak or missing link |
| Contact or nonlinear run will not converge | increments, contact definitions, initial penetration or gap |

## Things worth checking in any `.f06`

Engineering method. These are the standard health indicators of a static run:

- the **applied load resultant** against the **reaction resultant** — they should
  balance; a difference means load is going somewhere unintended
- the **total mass** — against what the part should weigh, which catches unit and
  density errors faster than anything else
- **singularity / AUTOSPC output** — what the solver removed to make the model
  solvable is often what you forgot to connect
- **epsilon and matrix-conditioning figures** — large values indicate an
  ill-conditioned model even when nothing failed
- **element quality warnings** at the top of the run

## When the model came out of Apex

Apex writes the deck, so a deck-level complaint usually traces back to a
modelling decision in Apex rather than hand-edited cards. Two skills share the
work: `nastran-reference` explains what the entry the solver is complaining about
is supposed to contain, and `apex-docs` explains how that entry gets created in
the GUI. Hand over rather than guessing at either end.

## What this skill cannot tell you

- Whether a result is physically believable — that is judgement, and
  `fea-modelling-strategy` is where that conversation belongs.
- Element formulation or solver theory — not in the Apex or Nastran HTML
  documentation this plugin indexes.
- Anything about a message number that is not in the catalogue. Say so.
