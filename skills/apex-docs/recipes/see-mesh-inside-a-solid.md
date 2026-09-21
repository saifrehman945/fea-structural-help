# Seeing the mesh inside a solid

**The documentation does not give this as a single procedure.** There is no
modelling-time clipping plane in Apex. This recipe is a synthesis of several
documented controls; each step is cited, and the synthesis itself is flagged.

Bundle for the URLs below: see `config.md`. Substitute your own if pinned.

## Short answer

While modelling, use **transparency** or **entity-type display**, not a section
cut. A true cutting plane (**Cut View**) exists only in postprocessing.

## Why there is no section cut while modelling

The three features whose names suggest one all do something else — see
`references/known-gaps.md`:

- **Cut View** places a real cutting plane, but *"is active during
  postprocessing"*. — [Cut View, node 2948](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2948.html)
- **Section View** is a Model Browser grouping by shell section property, not a
  geometric cut, and it was removed after `apex_2022.1`.
  — [Section View, node 2179](https://nexus.hexagon.com/documentationcenter/en-US/bundle/apex_2022.1/page/node/2179.html)
- **X-Section Force Sensor** uses a cutting plane to *sum internal forces*; it
  measures rather than reveals. — [X-Section Force Sensor, node 2169](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2169.html)

## Option 1 — Transparency (usually what you want)

Make the geometry translucent and the solid mesh shows through it.

Transparency is a Model Browser render control:

> *"Transparency — This option, only valid when Shaded or Shaded with Edge is
> selected, allows the transmission of light through the entity. The slider
> controls the amount of transparency as a percentage. Click the Transparency
> button to activate transparency, click again to turn off transparency."*
> — [Render, node 1013](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1013.html)

So: set the render style to **Shaded** or **Shaded with Edges** first, or the
transparency control will not apply.
— [Render Styles, node 941](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/941.html)

## Option 2 — Hide the geometry, show only 3-D elements

Geometry and FEM entity types are toggled independently in the Viewport Display
Controls. Documented separately controllable types:

- geometry: Vertices, Points, Curves, Surfaces, **Solids**
- FEM: Mesh Seeds, Nodes, 1-D Elements, 2-D Elements, **3-D (Solid) Elements**

— [Entity Type Displays, node 942](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/942.html)

Turning **Solids** off while leaving **3-D Elements** on leaves the mesh visible
with the geometry out of the way. Combine with **Wireframe** or **Shaded with
Edges** to read element boundaries — *"Shaded with Edges … allows you to display
element edges on filled 2-D and 3-D entities."*
— [Render Styles, node 941](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/941.html)

## Option 3 — Isolate interior elements by quality

If the goal is finding bad elements buried inside the solid rather than surveying
the mesh, the Element Quality tool isolates them directly:

> *"The 'Isolate and enhance' command … displays only the elements in the
> selected quality range, and in doing so creates 'globs' of contiguous elements
> … The Globs panel lists the distinct contiguous meshed regions … You may also
> toggle the visibility of each glob individually."*

and to work outward from them:

> *"By clicking the Grow 2D Mesh icon in the Viewport Display Controls, you can
> show elements adjacent to those already displayed. This process may be
> repeated."*

— [Element Quality, node 1064](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1064.html)

## Option 4 — Reach interior entities without changing the view

Two interaction conventions from the in-product workflow database
(`references/interaction-conventions.md`), available inside most tools:

- **`P`** toggles visibility picking versus occluded picking — occluded picking
  is how you select something behind or inside a solid without hiding anything.
  Declared by 143 of 168 documented tools.
- **`H`** hides preselected faces, **`SHIFT+H`** restores them — a fast temporary
  look inside, scoped to the tool. Declared by 83 and 65 tools respectively.

## In postprocessing — the real cutting plane

Once results are loaded, Cut View gives an actual plane with these controls:
**Only Slice** (show only the cut plane, no geometry either side), **Reverse**
(switch visible side), **Transform** (reposition by translation or rotation;
press **R** for rotation manipulators), and buttons to align the plane normal to
each global axis.
— [Cut View, node 2948](https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2948.html)

## Caveats

- **Not found in the documentation — general engineering knowledge:**
  transparency is the closest analogue to a section cut for mesh inspection, but
  it shows the whole depth of the model at once, so on a thick or nested
  assembly it reads as clutter. Hiding all but the part of interest first
  (`Show Only`, node 1020) usually beats turning transparency up further.
- **Not found in the documentation — general engineering knowledge:** if the
  purpose is checking interior mesh quality rather than looking at it, Option 3
  is a better use of time than any visual approach, because it finds the bad
  elements instead of relying on you to spot them.
- The four display pages above document their procedures **only by video**, and
  no video file is present in the archive, so no written click-by-click steps
  exist for them. The control names quoted here are documented; the order of
  operations is this recipe's synthesis.
