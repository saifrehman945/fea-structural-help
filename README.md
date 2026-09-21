# fea-structural-help

Five skills covering structural FEA work in **MSC Apex** and **MSC Nastran**,
organised around the engineering workflow rather than around document
categories.

| Stage | Skill | Answers |
|---|---|---|
| Plan / interpret | `fea-modelling-strategy` | idealisation, joint representation, what to expect, is this believable |
| Build | `apex-docs` | how to do it in the Apex GUI |
| Automate | `apex-scripting` | write and debug Apex Python and custom tools |
| Solve | `nastran-reference` | what a deck keyword, field or solution sequence does |
| Debug | `nastran-diagnostics` | what a message means, why the run failed |

Skills are namespaced: `/fea-structural-help:apex-docs`, and so on.

## The rule every skill follows

Documentation is quoted and cited. Anything beyond it is labelled:

> **Not found in the documentation — general engineering knowledge:** …

This matters because the Apex and Nastran documentation contain almost no
engineering theory. Most "why" answers are necessarily reasoning, and you should
always be able to tell which half of an answer is which.

## How it gets its content

The Hexagon documentation portal is a JavaScript application: fetching a page URL
returns an empty shell, there is no listing, and there is no full-text search. The
portal reads its content from a raw backend that serves plain HTML, and that is
what these skills fetch.

So each skill bundles **only what cannot be fetched or found** — indexes,
procedures and generated references — and pulls page text live:

| Bundled locally | Why |
|---|---|
| Apex tool procedures (168 tools, 1,849 steps) | ship inside Apex; published nowhere online |
| Apex keyword index (1,690 aliases) | the portal cannot be searched |
| Apex Python API reference | the Doxygen pages 404 on every bundle |
| Nastran keyword index | the portal cannot be crawled; topic pages have no links |
| Nastran message index (5,552 messages) | source files are ~680 KB each; the index makes lookup cheap |

Page prose is never stored. It is fetched, cited, and — for Nastran messages —
sliced to the single message asked about, so reading one costs a few hundred
characters rather than a whole page.

## Documentation releases

Set per skill in each `config.md`, because the best source differs by book:

- Apex GUI — `msc_apex_help` (rolling)
- Nastran QRG and Reference Guide — `MSC_Nastran_2025.2`
- Nastran messages — `MSC_Nastran_2025.1` (the only release publishing them as HTML)
- Apex Python API — Iberian Lynx FP2

Every citation records its release, because bulk data fields and Apex API
signatures both change between versions.

## Installing

```
claude --plugin-dir ./fea-structural-help     # try it
claude plugin validate ./fea-structural-help  # check the manifest
```

`cache/` directories are created at runtime by the fetch tools and are not part
of the plugin. Clear them before packaging or uploading, or they inflate the
file count:

```
find . -type d -name cache -exec rm -rf {} +
```

## Rebuilding

Each skill has its own tools and validator:

```
python skills/nastran-reference/tools/build_index.py
python skills/nastran-diagnostics/tools/build_messages.py --resume
python skills/apex-scripting/tools/gen_api.py <path to ScriptingXML>
```

Then run every validator; each must exit 0:

```
python skills/apex-docs/tools/validate.py
python skills/apex-scripting/tools/validate_references.py
python skills/nastran-reference/tools/validate.py
python skills/nastran-diagnostics/tools/validate.py
```

The portal refuses sustained request bursts, reporting it as a DNS or
connection-reset error rather than an HTTP 429. The builders retry with backoff;
`--resume` picks up ranges that still failed.

## Known limits

- The raw documentation endpoint is undocumented and MSC Apex and Nastran are
  moving from Hexagon to Cadence. If it goes away, the indexes, procedures and
  API reference keep working; live page prose does not.
- The Apex archive the indexes were built from is a ~2021.4 snapshot, while the
  page text fetched is current. `apex-docs` flags the skew.
- No element theory or solver theory exists in either corpus. That is what
  `fea-modelling-strategy` is for, and why it marks its reasoning.
