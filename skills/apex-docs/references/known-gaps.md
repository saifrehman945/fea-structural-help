# Known gaps and false friends

What the Apex documentation does **not** contain, and where its vocabulary will
mislead you. Consult this before an exhaustive search — most of the searching
that feels unproductive is a search for something that was never written down.

## Not in the documentation at all

**Engineering and solver theory.** There is no element theory, no solver theory,
no convergence discussion, and no systematic guidance on choosing an approach.
The one page with real derivation is node 2236 (Von Mises Stress Calculation),
whose equations are rendered as images and so are unreadable as text. Anything
about *why* — shell vs solid, tet vs hex, mesh convergence, why midsurface — is
extrapolation and must be marked as such.

Occasional one-line rationale is scattered in feature pages, and it should be
cited when found rather than presented as your own reasoning. Known fragments:

- *"an RBE3 style compliant connection which will not add stiffness to the
  model"* — [Point Mass, node 1452](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1452.html)
- *"Internal Coarsen … allows a larger model to be meshed with fewer elements in
  the middle of the geometry, where loads are less likely to be placed"*
  — [Solid Meshing, node 959](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/959.html)

Search `index/pages.md` summaries and `index/keywords.md` for the concept, then
fetch the likeliest page, before assuming nothing is documented — a fragment is
worth citing, and the extrapolation then starts from it.

**Quality metric definitions.** Node 1064 explains the Invalid/BAD/POOR/GOOD
colour bands and the Isolate-and-Enhance workflow, but never defines aspect
ratio, Jacobian, warp or skew mathematically.

**Solver error messages.** Nastran error and fatal codes are not here; they are
in the separate MSC Nastran Error Messages Guide. Do not guess a code's meaning.

**Tutorial instruction.** The 17 tutorials are video-only. Roughly 120 tutorial
pages carry 5–19 words each — a caption and a duration — and **no `.mp4` exists
in the archive**. The Camtasia table-of-contents tracks survive, so the tutorials
still tell you the *order* of a workflow, never how to perform a step.

**Procedures for view and display tools.** The in-product workflow database
covers 168 tools, weighted to modelling and loads/BCs. Cut View (2948), Render
Styles (941), Entity Type Displays (942) and Meshing (954) have **no workflow
entries**. For display questions, only the reference prose exists.

## False friends

Apex vocabulary that means something other than the obvious.

| Term | What a user usually means | What Apex means |
|---|---|---|
| **Section View** (2179) | a geometric section cut | a *Model Browser grouping mode* that organises entities by shell section property. Nothing to do with cutting geometry. Also **removed after `apex_2022.1`**. |
| **Cut View** (2948) | a clipping plane while modelling | a clipping plane available **only during postprocessing** |
| **X-Section Force Sensor** (2169) | a visual cross section | a *results sensor* that sums internal forces on a plane. It has a cutting plane, but it measures — it does not reveal mesh. |
| **Cross section** (2286, 2294, 1474) | a section cut | in beam contexts, the *profile* of a beam |
| **Core Sample** (2230) | a section through a solid | a composites tool for inspecting **plies** |

Because of these, a keyword hit is not a match. Confirm the page actually does
what the user wants before building an answer on it.

## Structural limits of the corpus

- **`UI/node` is a reference manual, not a procedural one.** 589 pages, median
  217 words; exactly one contains the string "Step 1". Pages describe what a
  control *is*. The real numbered procedures are in `workflows/`, and nowhere
  else — check there first.
- **79% of pages depend on screenshots**, and icons are often identified only by
  the image. A fetched page keeps image filenames inline as `[image: name.jpg]`
  and those are semantic; where they are not enough, say the control is shown in
  a screenshot and give the page URL rather than inventing a label.
- **The indexes are built from a ≈2021.4 archive; the page text is live.** So
  the catalog can lag the documentation: node 3218 has no index entry but exists
  in `apex_2025.1`. If a user names a feature absent from `index/pages.md`, it
  may still exist — try `--find-bundle` before concluding otherwise.
- **Pages come and go between releases, in both directions.** Node 2179 exists
  only in `apex_2022.1`; node 2234 only in `apex_2025.2`/`2025.1`. A 404 on one
  bundle is not proof the feature never existed — run
  `python tools/fetch_page.py <id> --find-bundle` to see which releases have it.
- **Some tools have a procedure but no page anywhere.** 21 of the 168 workflows
  describe tools with no page in the local archive, and a few (node 3051, Assign
  Material) are in **no** published bundle either. For those the workflow file is
  the only surviving documentation; cite it as such rather than reporting that
  the feature is undocumented.
- **Seven pages are gated or missing** in the archive (1074, 1216, 1267, 1272,
  2601, 2729, 2634). Several still have workflow entries, so the procedure may be
  available even when the page is not.

## The canonical hard case

*"Put a cross section on the current view so I can see the mesh inside a solid."*

No page documents this. Cut View is postprocessing-only; Section View is a
browser grouping and is gone after 2022.1; the X-Section sensor measures force.
Answering it requires synthesising render style (941), entity type display (942),
visibility (1011/1019/1020) and element quality isolation (1064) — and saying
plainly that the documentation does not give it as one procedure. See
`recipes/see-mesh-inside-a-solid.md`.
