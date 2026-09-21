---
name: fea-modelling-strategy
description: Think through structural FEA modelling decisions and interpret results. Use when the user is deciding how to model something rather than how to operate a tool — idealisation (shell vs solid, beam vs shell, 1D vs 3D), how to represent a joint, bolt, weld or bearing, where to constrain, how to apply load, what mesh density is enough, what result to expect before running, whether a result is believable, or how to plan an analysis. Also for open-ended "what are my options" and "how should I approach this" discussions. This skill reasons from engineering knowledge and says so; it cites Apex and Nastran documentation only where that documentation actually covers the point, and routes to apex-docs, apex-scripting, nastran-reference or nastran-diagnostics for anything they can ground.
---

# FEA modelling strategy

## Overview

This is the judgement skill. The other four answer "what does this do" from
documentation; this one answers "what should I do, and will I believe the
answer" — and that is almost never in the documentation.

**The Apex and Nastran documentation contain essentially no engineering theory.**
Verified across both corpora: no element theory, no solver theory, no mesh
convergence guidance, no discussion of when to choose one idealisation over
another. One Apex page derives Von Mises stress, and its equations are images.
Occasional one-line rationale is scattered in feature pages.

So this skill reasons from engineering knowledge. That is legitimate and useful —
provided it is never dressed up as documentation.

## The contract

Every claim falls into one of two buckets, and the user must always be able to
tell which.

**Engineering reasoning — the default here.** Mark it:

> **Not from the documentation — engineering reasoning:** an RBE3 distributes
> load to the attached nodes without adding stiffness between them, so for a
> bolt into a bore it will not artificially stiffen the hole the way an RBE2
> would. The trade is that RBE3 cannot carry the joint's rotational constraint
> on its own.

**Documented — cite it.** When a point *is* covered, quote and cite rather than
reasoning it out. Known documented fragments worth citing:

- RBE3 as a "compliant connection which will not add stiffness to the model" —
  Apex node 1452 (`apex-docs`)
- element quality bands and the Isolate-and-Enhance workflow — Apex node 1064
- a bulk data entry's fields and defaults — `nastran-reference`
- a message's meaning and `User action` — `nastran-diagnostics`

If a sibling skill can ground part of the answer, **use it** rather than
reasoning from memory. Mixed answers are fine; unmarked ones are not.

## How to work

1. **Establish the question behind the question.** "Should I use RBE2 or RBE3"
   usually means "will this joint behave right", which depends on what the model
   is for.
2. **Ask what the analysis is for** when it changes the answer — stiffness,
   strength, fatigue, modal, buckling. Do not ask when it does not.
3. **Say what you expect before proposing a build.** A predicted order of
   magnitude, load path or mode shape is the cheapest error check available.
4. **Name the failure modes of the approach** you recommend, not just its
   merits.
5. **Give the check** that would catch it if you are wrong.

## Sanity checks worth stating

Engineering method, not documentation. Offer the ones that fit:

- **Load path** — trace load from application to reaction by hand. If you cannot,
  the model will not either.
- **Equilibrium** — applied load resultant against reaction resultant.
- **Mass and units** — total mass against what the part should weigh. Catches
  unit and density errors faster than anything else.
- **Order of magnitude** — a hand calculation on a simplified section.
- **Constraint** — is the model held exactly, over- or under-constrained? What
  did AUTOSPC remove?
- **Mesh sensitivity** — would refining change the answer where it matters?
- **Stress singularities** — sharp re-entrant corners and point loads do not
  converge; do not report their peak values.

## Handing over

| The question is really about | Skill |
|---|---|
| Where a tool is, or how to drive the Apex GUI | `apex-docs` |
| Writing or fixing Apex Python | `apex-scripting` |
| What a deck keyword or field means | `nastran-reference` |
| A message number, or why a run failed | `nastran-diagnostics` |

Route rather than guess. A wrong field description invented here is far more
damaging than one fetched correctly there.

## Tone

The user is an experienced FEA engineer. Give the reasoning and the trade-off,
at the level of one engineer talking to another. No FEA tutorials, no restating
what they already know, and no hedging a recommendation you have reasons for —
give the recommendation, then its limits.
