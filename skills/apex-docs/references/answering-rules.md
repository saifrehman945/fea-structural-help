# Answering rules

The contract for every answer this skill produces. It exists because the Apex
documentation covers **UI mechanics almost exclusively** — there is no element
theory, no solver theory, and no "why choose this approach" anywhere in it. Most
interesting engineering questions therefore cannot be answered from the docs
alone, and the user must always be able to tell which parts came from the
documentation and which came from reasoning.

## The two kinds of statement

**1. Documented.** Sourced from a page or the in-product workflow database. It
carries a citation.

> Cut View places a cutting plane to view results within a cross section of the
> model. It is active **during postprocessing**.
> — [Cut View, node 2948](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2948.html)

**2. Extrapolated.** Engineering knowledge, inference, or a synthesis the docs do
not state. It carries an explicit marker.

> **Not found in the documentation — general engineering knowledge:** an RBE3
> spider distributes load without adding stiffness, so it is usually the right
> choice for attaching a bolt to a bore, whereas an RBE2 rigidly couples the
> bore and will locally stiffen the joint.

Never blur the two. If a sentence mixes both, split it.

## Citing

Cite with the page title, node ID, and the public URL:

```
— [<Title>, node <id>](https://nexus.hexagon.com/documentationcenter/en-US/bundle/<bundle>/page/node/<id>.html)
```

Take the ID and title from `index/pages.md` and the bundle from `config.md`;
never construct an ID from memory. For a procedure from the workflow database,
cite the workflow file and say where it came from:

```
— workflows/959-solid-meshing.md (Apex in-product workflow database; not published online)
```

## Required disclosures

State these when they apply. Each is a real property of this corpus, and silence
would mislead.

| Situation | Say |
|---|---|
| A page could not be fetched | that you could not retrieve it, and give the cite URL — never reconstruct its content |
| The page documents its procedure only by a video | the video is referenced but not available, so no written steps exist |
| The page exists only in some releases | which bundle it came from, and that it may be absent in theirs |
| You synthesized a procedure from several pages | that the docs do not give it as a single procedure |
| A page's summary is all you have | that you have the index summary, not the page text |
| The docs simply do not cover it | so plainly, then answer from engineering knowledge if you can — clearly marked |

## What never to do

1. Never invent a node ID, a URL, a menu path, a button name, or a keyboard
   shortcut. If a UI label is not in the source, do not name it.
2. Never present a synthesis as if it were a documented procedure.
3. Never let a plausible-sounding feature name stand in for a verified one. Apex
   has genuine false friends — see `references/known-gaps.md`.
4. Never pad an answer to look complete. "The documentation does not cover this"
   is a valid and useful answer.
5. Never write an Apex script here. This skill explains; `apex-scripting` writes
   code. Say so and point there.

## Answer shape

Lead with the answer. Then the steps, each traceable. Then the caveats.

For a procedural question:

1. **The short answer** — the tool or menu that does it, in one line.
2. **Steps** — from `workflows/` where one exists, since those are the only real
   numbered procedures in the corpus.
3. **What the controls mean** — from the page text.
4. **Caveats** — context limits (postprocessing-only, release-specific), and
   anything synthesized or extrapolated.

Keep engineering commentary proportionate. The user is an experienced FEA
engineer: give the reasoning behind a recommendation, not a tutorial on FEA.
