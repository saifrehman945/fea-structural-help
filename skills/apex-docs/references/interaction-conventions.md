# Apex interaction conventions

Patterns that hold across most Apex tools, mined from the in-product workflow
database (the counts are how many of the 168 documented tools declare each key).
Knowing these lets you read a terse procedure correctly, and explain a step the
page leaves implicit.

## The middle mouse button drives everything

**141 of 168 documented tools use MMB.** It is the universal "I am done with this
stage" signal — it ends a selection, advances to the next stage, or commits the
operation. A procedure that says only *"Select the bodies"* almost always implies
an MMB click to move on.

Many tools have an **Auto** and a **Manual** variant, differing by exactly this:

> **Solid Meshing – Auto:** 1. Define mesh size 2. Select solid body(ies)
> **Solid Meshing – Manual:** 1. Define mesh size 2. Select solid body(ies)
> 3. Click MMB to create the mesh
> — workflows/959-solid-meshing.md

Auto applies on selection; Manual waits for MMB. `SHIFT+MMB` (12 tools) steps
*back* to the previous selection stage.

## Near-universal keys

| Key | Count | Meaning |
|---|---|---|
| `ESC` | 154 | Abort the operation midway |
| `P` | 143 | Toggle visibility picking versus occluded picking |
| `CTRL` | 84 | Toggle multi-select |
| `SHIFT` | 84 | Pure accumulation (add to selection) |
| `CTRL+SHIFT` | 73 | Pure deselection |
| `H` | 83 | Hide preselected faces |
| `SHIFT+H` | 65 | Re-display previously hidden faces |
| `ALT+Double Click` | 21 | Auto-extend the picked target list |

`P` matters more than its terse description suggests: **occluded picking is how
you select something inside or behind a solid** without moving or hiding it. It
is frequently the missing half of a question about reaching interior geometry.

`H` / `SHIFT+H` are the quickest way to look inside a part during a tool
operation, and they are scoped to the tool rather than changing model visibility.

## Tool-specific keys worth knowing

| Key | Tools | Meaning |
|---|---|---|
| `SPACEBAR` | meshing | Launch the property pop-up for the hovered entity |
| `R` / `T` | transform, joints | Switch the manipulator to rotate / move |
| `F` | sketching, push/pull | Bring the grid parallel to screen; cycle methods |
| `X` | push/pull | Cut through solids in one shot |
| `Z` / `C` | push/pull | Enlarge / shrink the snap box |

## Reading a workflow file

`workflows/*.md` are transcriptions of the in-product help, so they are written
for someone already looking at the tool. They name the stage, not the pixel. When
a step says "Select entities", the pick filter and the tool's active stage decide
what is selectable — which is why `P`, `CTRL` and `SHIFT` appear so often.

Where a step is genuinely ambiguous without seeing the screen, say so and give
the page URL or the relevant image rather than inventing a control name.
