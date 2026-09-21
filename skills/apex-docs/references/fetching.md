# Fetching live documentation

## Why fetching at all

**The published documentation is the single source of truth.** No page text is
bundled with this skill. Fetching is how you read a page, not an enhancement —
so an answer that quotes page content must come from a fetch.

## Why the public URL cannot be fetched directly

`nexus.hexagon.com` is a Zoomin JavaScript application. Fetching a page URL
returns an empty shell whose only text is *"Powered by Zoomin Software"*. Do not
try to read documentation with a plain web fetch of that URL, and do not conclude
from an empty result that the page does not exist.

The SPA loads its content from a raw backend, which serves plain HTML:

```
https://documentation-be.hexagon.com/bundle/<bundle>/raw/resource/enus/node/<id>.html
```

## Two ways to fetch

**1. A plain web fetch of that URL — preferred.** The raw backend returns
ordinary HTML, so the built-in web-fetch tool reads it directly. Verified: a
fetch of node 2948 returns the real Cut View text. This needs no shell and no
local Python, so it works wherever the skill is installed.

**2. `tools/fetch_page.py`** — same endpoint, plus text extraction, caching under
`cache/<bundle>/`, and bundle probing. Use it when a shell with network access is
available, and for `--find-bundle`.

```
python tools/fetch_page.py 1064                        # default bundle
python tools/fetch_page.py 2179 --bundle apex_2022.1   # a specific release
python tools/fetch_page.py 2234 --find-bundle          # which releases have it
python tools/fetch_page.py 1064 --raw                  # HTML instead of text
```

Exit codes: `0` ok, `3` not in that bundle, `4` network error.

If neither route has network access, say so — `workflows/`, `index/` and
`recipes/` still work, and none of that is published online anyway.

## Bundles

Set the default in `config.md`. Verified available:

| Bundle | Notes |
|---|---|
| `msc_apex_help` | rolling/current; the default |
| `apex_2025.2`, `apex_2025.1`, `apex_2024.1`, `apex_2023.1`, `apex_2022.1` | pinned releases |

Match the user's installed release when you know it. Pages are added and removed
between releases in both directions, so **a 404 in one bundle is not proof the
feature never existed** — node 2179 (Section View) exists only in `apex_2022.1`,
node 2234 (Clearance Sensor) only in `apex_2025.2`/`2025.1`.

When a page 404s, find a release that has it:

```
python tools/fetch_page.py 2234 --find-bundle
```

If it is in no bundle at all (node 3051 is one such), check `workflows/` — for
21 tools the workflow procedure is the only documentation that survives.

## When a fetch fails

Do not invent the content. In order:

1. `--find-bundle` — the page may live in another release.
2. Check `workflows/` — for 21 tools the procedure is local and the page is not
   needed at all.
3. Use the summary in `index/pages.md` and say that is all you have, giving the
   user the cite URL to read themselves.

If the network is unavailable, say so plainly. `workflows/`, `index/` and
`recipes/` still work offline; page prose does not.

## Citing

Always cite the human-readable portal URL, which renders properly in a browser
with its screenshots:

```
https://nexus.hexagon.com/documentationcenter/en-US/bundle/<bundle>/page/node/<id>.html
```

Never cite the `documentation-be` URL — it is an undocumented internal endpoint
and means nothing to the user.

## Images

Documentation images are not bundled, and 79% of pages lean on them — icons are
frequently identified *only* by the picture. A fetched page keeps its image
filenames inline as `[image: name.jpg]`, and those filenames are semantic
(`cut_view_controls.jpg`, `transform_along_axis_step2.jpg`), which is often
enough to describe a control.

When it is not, give the user the cite URL and say the control is shown in a
screenshot rather than named in the text. Do not guess a button's label from its
filename.

## Robustness

The raw endpoint is undocumented and could change, particularly as MSC Apex
moves from Hexagon to Cadence. That risk is accepted deliberately: keeping a
local copy of the page text was not worth its bulk.

If fetching stops working, `workflows/` (the procedures), `index/` (titles,
summaries, keywords, tree) and `recipes/` remain fully usable —
and none of that is published online anyway. What is lost is page prose. Say so
rather than reconstructing it, and rebuild the skill against a newer archive if
the endpoint has genuinely moved.
