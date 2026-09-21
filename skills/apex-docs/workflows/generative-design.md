# Generative design — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [Build Direction](#build-direction-node-2788)
- [Design Region](#design-region-node-2291)
- [Design Variable](#design-variable-node-2947)
- [Machining Allowance](#machining-allowance-node-2584)
- [Manufacturing Constraints](#manufacturing-constraints-node-2420)

---

## Build Direction (node 2788)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2788.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Build Direction - Manual Define**

1. Select an entity to define the build direction.
2. Click MMB or Apply.

Tips:

- The default build direction is the X axis of the global coordinate system.
- The coordinate system of the build direction will overwrite the material orientation of the design space when outputting the GD configure file.

---

## Design Region (node 2291)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2291.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Design Region - Auto mode**

1. Select the entities you want to include in the Design Region.
2. Select the entities you want to include in the Exclusion Region.

**Create Design Region - Manual mode**

1. Select the entities you want to include in the Design Region.
2. Click MMB.
3. Select the entities you want to include in the Exclusion Region.
4. Click MMB.

---

## Design Variable (node 2947)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2947.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT+MMB` | Transitions to previous selection stage |

**Design Variable Value - Manual mode**

1. Enter desired values into the tool property editor
2. Click MMB or Apply button to complete the creation of the design variable

**Design Variable String - Manual mode**

1. Enter desired strings into the tool property editor
2. Click MMB or Apply button to complete the creation of the design variable

**Design Variable Expression - Manual mode**

1. Enter desired expression into the tool property editor
2. Click MMB or Apply button to complete the creation of the design variable

---

## Machining Allowance (node 2584)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2584.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `Shift` | Pure accumulation |
| `CTRL + Shift` | Pure deselection |
| `H` | Hide preselected faces |
| `Shift + H` | Display previously hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Machining Allowance - Auto mode**

1. Set the machining allowance value.
2. Select the entities you want to apply machining allowance.

**Machining Allowance - Manual mode**

1. Set the machining allowance value.
2. Select the entities you want to apply machining allowance.
3. Click MMB.

---

## Manufacturing Constraints (node 2420)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2420.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Symmetry Constraint - Auto mode**

1. Select the Design Region to apply Symmetry Constraint to
2. Define the location of the symmetry plane

**Create Symmetry Constraint - Manual mode**

1. Select the Design Region to apply Symmetry Constraint to
2. Click middle mouse button (MMB) or Apply button when you are ready
3. Define the location of the symmetry plane
4. Click middle mouse button (MMB) or Apply button when you are ready

**Create Casting Constraint - Auto mode**

1. Select the Design Region to apply Casting Constraint to
2. Define the casting direction

**Create Casting Constraint - Manual mode**

1. Select the Design Region to apply Casting Constraint to
2. Click middle mouse button (MMB) or Apply button when you are ready
3. Define the casting direction
4. Click middle mouse button (MMB) or Apply button when you are ready

**Create Overhand Constraint - Auto mode**

1. Select the Design Region to apply Overhand Constraint to
2. Define the build direction

**Create Overhand Constraint - Manual mode**

1. Select the Design Region to apply Overhand Constraint to
2. Click middle mouse button (MMB) or Apply button when you are ready
3. Define the build direction
4. Click middle mouse button (MMB) or Apply button when you are ready
