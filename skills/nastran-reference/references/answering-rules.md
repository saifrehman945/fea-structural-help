# Answering rules

The contract for every answer this skill produces. It mirrors `apex-docs`, for
the same reason: the documentation describes **what a keyword is and what its
fields mean**, and says comparatively little about *why* you would choose one
modelling approach over another. The user must always be able to tell which is
which.

## The two kinds of statement

**1. Documented.** Taken from a fetched page. It carries a citation.

> `PSHELL` MID2 is the material identification number for bending. Leaving it
> blank means no bending stiffness is generated.
> — [PSHELL, MSC Nastran 2025.2 QRG](https://nexus.hexagon.com/documentationcenter/en-US/bundle/MSC_Nastran_2025.2/page/Nastran/Quick_Reference_Guide/Bulk_Data_Entries/Entries_P/...)

**2. Extrapolated.** Engineering reasoning the documentation does not state.

> **Not found in the documentation — general engineering knowledge:** leaving
> MID2 blank turns the shell into a membrane, which is usually a modelling
> mistake on a part carrying out-of-plane load.

Never blur the two. If a sentence mixes both, split it.

## Citing

Cite the keyword, the release, and the public URL:

```
— [<KEYWORD>, MSC Nastran <release> <book>](https://nexus.hexagon.com/documentationcenter/en-US/bundle/<bundle>/page/<path>)
```

Take the path from `index/keywords.md` and the bundle from `config.md`; never
construct one from memory. `python tools/fetch_page.py <KEYWORD> --url` prints
the exact citation URL.

**Always state the release.** Bulk data entries gain and lose fields between
versions, so "MID4 exists" is only true of a particular solver.

## Required disclosures

| Situation | Say |
|---|---|
| The page could not be fetched | that you could not retrieve it, and give the URL — never reconstruct a field table |
| The keyword is not in the index | that it is not in the QRG/Reference Guide index, before asserting it does not exist |
| The user's solver release differs from `config.md` | which release your answer describes, and that fields may differ |
| The question is about an error message | that error messages are the `nastran-diagnostics` skill, and hand over |
| You are reasoning past the field descriptions | mark it as engineering knowledge |

## What never to do

1. **Never invent a field name, a field position, or a default.** Nastran field
   layout is positional and unforgiving; a wrong field number produces a deck
   that runs and gives wrong answers. If you have not fetched the entry, do not
   state its format.
2. Never guess a keyword's existence from a plausible name. Nastran has many
   near-miss names (`CQUAD4`/`CQUADR`/`CQUAD8`, `PBAR`/`PBARL`, `RBE2`/`RBE3`).
3. Never present the Reference Guide's theory sections as if they justified a
   specific modelling choice unless they actually say so.
4. Never write or debug Apex Python here — that is `apex-scripting`.

## Answer shape

1. **What the keyword is** — one line.
2. **The format** — the field layout, quoted from the entry, when the question is
   about usage.
3. **The fields that matter** to the question, with their documented meaning and
   constraints.
4. **Caveats** — release, interactions with other entries, and anything you
   reasoned rather than read.

The user is an experienced FEA engineer. Give the field semantics and the
consequence, not an introduction to finite elements.
