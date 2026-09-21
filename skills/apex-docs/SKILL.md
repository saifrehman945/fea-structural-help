---
name: apex-docs
description: Answer questions about MSC Apex from its documentation — how to perform an operation in the Apex GUI, what a tool or control does, where a feature lives, what a setting means, or how macros and custom tools work. Trigger on questions like "how do I create a cross section", "how do I mesh this", "what does this option do", "where is the element quality tool", or any request for step-by-step instructions or documentation lookup for geometry, meshing, materials, loads and constraints, connections, analysis scenarios, results and postprocessing, the model browser or viewport display. Answers are grounded in the documentation with citations. For writing Apex Python or looking up an API signature, use apex-scripting. For Nastran deck keywords use nastran-reference, and for solver messages use nastran-diagnostics.
---

# Apex documentation

## Overview

Answer questions about MSC Apex from its documentation, with citations, and mark
clearly anything that goes beyond what the documentation says.

Two things make this corpus unusual, and both shape how you work:

- **The published documentation is the source of truth, and it is not
  searchable.** `nexus.hexagon.com` is a JavaScript app; fetching a page URL
  returns an empty shell, and there is no listing or full-text search. No page
  text is stored in this skill. The bundled indexes are how you find a page at
  all, and `tools/fetch_page.py` is how you read one.
- **The pages describe controls, not procedures.** Of 589 pages, exactly one
  contains the string "Step 1". The real numbered procedures live in
  `workflows/`, extracted from Apex's in-product help database, and are published
  nowhere online.

This skill explains Apex. It does not write Apex code — that is `apex-scripting`.

## Required workflow

1. **Check for a false friend.** Several Apex feature names mean something other
   than the obvious: Section View is a browser grouping, Cut View is
   postprocessing-only, X-Section Force Sensor measures force. Scan
   [references/known-gaps.md](references/known-gaps.md) before building an answer
   on a name that merely sounds right.
2. **Find the page.** `index/keywords.md` first — it maps the user's wording onto
   page IDs using Apex's own search keywords. Then grep the titles and summaries
   in `index/pages.md`, then `index/topics.md` for neighbours.
3. **Prefer a workflow.** If a named tool is involved, look it up in
   `index/workflows-index.md` and read its entry in the matching `workflows/`
   file. Those are the only genuine step-by-step procedures in the corpus.
4. **Fetch the live page.** This is the only source of page text. Fetch
   `https://documentation-be.hexagon.com/bundle/<bundle>/raw/resource/enus/node/<id>.html`
   directly with a web fetch — the raw backend returns plain HTML, unlike the
   portal URL. `python tools/fetch_page.py <id>` does the same with caching and
   `--find-bundle`, where a shell is available. If a page 404s, try another
   bundle; if nothing can be retrieved, say so rather than guessing.
5. **Answer under the contract** in
   [references/answering-rules.md](references/answering-rules.md): cite what is
   documented, explicitly mark what is not.

## The citation contract

Non-negotiable, because the docs contain almost no engineering theory — most
"why" answers are necessarily extrapolation, and the user must be able to tell.

**Documented** — cite title, node ID and the public URL:

> Cut View is active during postprocessing.
> — [Cut View, node 2948](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2948.html)

**Not documented** — say so in the sentence:

> **Not found in the documentation — general engineering knowledge:** an RBE3
> spider distributes load without adding stiffness…

Never invent a node ID, URL, menu path, button name or keyboard shortcut. If a
control is not named in the source, do not name it.

## Lookup surfaces

| Surface | Holds | Online? |
|---|---|---|
| `workflows/` | 168 tools in 11 files, 1,849 numbered steps, shortcuts, tips | **No** |
| `index/keywords.md` | 1,690 keywords → page IDs | **No** |
| `index/pages.md` | 589 pages: title, summary, section, URLs | **No** (summaries) |
| `index/topics.md` | the documentation book tree | — |
| `recipes/` | solved multi-page hard cases, fully cited | — |
| live fetch | current, release-matched page text | yes |

Full navigation in
[references/documentation-index.md](references/documentation-index.md).

## Answering rules

1. Lead with the answer, then steps, then caveats.
2. Take steps from `workflows/` where one exists; take control meanings from the
   page text.
3. Read a terse procedure using
   [references/interaction-conventions.md](references/interaction-conventions.md)
   — MMB ends a stage in 141 of 168 tools, `P` toggles occluded picking in 143,
   and Auto vs Manual variants differ by exactly that MMB click.
4. Say when a page documents its procedure only by video — ~120 do, and no video
   file exists in the archive.
5. Say when a page exists only in some releases. A 404 on one bundle does not
   mean the feature never existed (node 2179 lives only in `apex_2022.1`).
6. When several pages must be combined, say the documentation does not give it as
   one procedure. See `recipes/see-mesh-inside-a-solid.md` for the shape.
7. If the documentation does not cover it, say so plainly, then answer from
   engineering knowledge if you can — clearly marked. Do not pad.
8. The user is an experienced FEA engineer. Give reasoning, not an FEA tutorial.

## Scripting questions

Answer them; do not write code.

- **API surface** — arguments, modules, enum members — belongs to the
  `apex-scripting` skill, which carries the generated reference (989 functions,
  237 enums, 733 classes, with per-argument documentation). It is not published
  online, so do not try to fetch it. Hand the question over rather than
  answering from memory.
- **How scripting works** — object model, custom tools, GUI SDK, macros, remote
  control — are ordinary pages: 2156, 2178, 2259, 2260, 2262, 2380, 2401, 2403,
  2422, 2423–2443, 2952. Fetch and cite them normally.

If the user wants a script written, debugged or generated, say that is
`apex-scripting` and point there.

## Maintenance

Regenerate from the archive (see `config.md` for its location):

```
python tools/build_workflows.py    # -> workflows/ (11 grouped files), index/
python tools/build_indexes.py      # -> index/pages.md, keywords.md, topics.md
python tools/validate.py           # must exit 0
```

## References

- [references/answering-rules.md](references/answering-rules.md): citation and extrapolation contract
- [references/known-gaps.md](references/known-gaps.md): what the docs lack, and the false friends
- [references/fetching.md](references/fetching.md): the raw backend, bundles, what to do when a fetch fails
- [references/interaction-conventions.md](references/interaction-conventions.md): MMB, `ESC`, `P`, `H`, Auto vs Manual
- [references/documentation-index.md](references/documentation-index.md): full navigation and provenance
- [recipes/see-mesh-inside-a-solid.md](recipes/see-mesh-inside-a-solid.md): worked example of a multi-page synthesis
