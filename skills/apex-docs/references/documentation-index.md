# Documentation index

What is in this skill and the order to use it.

## Layout

```
apex-docs/
  SKILL.md
  config.md          which release bundle to fetch; archive location
  references/        how to answer — read these first
  workflows/         11 files, 168 tools, 1,849 steps, shortcuts  <- PRIMARY
  recipes/           hand-written multi-page syntheses, fully cited
  index/
    workflows-index.md  tool name -> workflows/<area>.md#anchor
    keywords.md         1,690 keywords -> page IDs (the vocabulary bridge)
    topics.md           the documentation book tree
    pages.md            589 pages -> title, summary, section, URLs
  cache/             pages fetched from the web, reused
  tools/             build and validation scripts
```

## Lookup order

1. **`index/keywords.md`** — map the user's wording to page IDs. Apex's own
   in-product search keywords, so `cutting plane` and `section view` both reach
   Cut View (2948) even though the page contains neither phrase. Start here; it
   is what makes the user's vocabulary work against the docs' vocabulary.
2. **`index/workflows-index.md`** — if a named tool is involved. `workflows/`
   holds the only real numbered procedures in the whole corpus, and that content
   exists nowhere online.
3. **`index/topics.md`** — once roughly located, related material is almost
   always a sibling in the book tree.
4. **grep `index/pages.md`** — every page's title and one-line summary, in
   Apex's own phrasing. This is the full-text surface; page prose is not stored.
5. **`python tools/fetch_page.py <id>`** — the only source of page text.
   See [fetching.md](fetching.md).
6. **`recipes/`** — check whether the question is already a solved hard case.

## By question type

| The user asks | Go to |
|---|---|
| "How do I *do* X?" | `workflows/` first, then the page text |
| "What does this control do?" | page text via `fetch_page.py` |
| "Where is X?" | `index/keywords.md`, then `index/topics.md` |
| "Why would I do X?" | mostly extrapolation — see [answering-rules.md](answering-rules.md) |
| Anything about the Python API | the `apex-scripting` skill |
| How scripting/custom tools work | ordinary pages: 2156, 2178, 2259, 2260, 2262, 2380, 2401, 2403, 2422, 2423–2443, 2952 |
| "Write me a script" | not this skill — point at `apex-scripting` |
| A term that sounds like a feature | [known-gaps.md](known-gaps.md) first; Apex has real false friends |

## References

- [answering-rules.md](answering-rules.md) — citation and extrapolation contract.
  The core of this skill; read before answering anything.
- [known-gaps.md](known-gaps.md) — what the docs do not contain, and the false
  friends. Stops fruitless searching.
- [fetching.md](fetching.md) — why the portal URL cannot be fetched, the raw
  backend, bundles, offline fallback, images.
- [interaction-conventions.md](interaction-conventions.md) — MMB, `ESC`, `P`,
  `H`, Auto vs Manual: how to read a terse procedure correctly.

## Provenance

| Part | Source | Published online? |
|---|---|---|
| `workflows/` | `docSearchData_Apex_1.0_en.xml`, the in-product help database | **No** — ships with the product |
| `index/keywords.md` | same file | **No** |
| `index/pages.md`, `index/topics.md` | `UI/node/*.html` + help DB, ≈2021.4 archive | page text yes, summaries no |
| live page text | `documentation-be.hexagon.com` raw backend | Yes |

No page text is bundled: the published documentation is the single source of
truth, fetched on demand. What is bundled is everything that is *not* published —
the procedures, the keyword bridge, the API reference — plus the indexes needed
to find a page at all. The archive is required only to re-run the build scripts.
