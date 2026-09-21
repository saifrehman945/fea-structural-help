# Postprocessing — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [Plot Target Tool](#plot-target-tool-node-2744)

---

## Plot Target Tool (node 2744)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2744.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Plot target - Auto mode**

1. Select entities you want to set as plot target

**Create Plot target - Manual mode**

1. Select the entities you want to set a plot target
2. Click MMB or Apply.

**Targeting objects in 3D View for XY Chart Curve Plotting**

1. Select 3D View Containing Model/Scenario consistent with active XY Chart View scenario
2. Click MMB to select 3D view and move the Stage 2
3. Select objects in 3D view
4. Click MMB or Check to select objects
5. Select Result to add to XY Chart

**Targeting objects in 3D View for XY Chart Curve Plotting**

1. Select 3D View Containing Model/Scenario consistent with active XY Chart View scenario
2. Select objects in 3D view
3. Select Result to add to XY Chart

Tips:

- There are two uses for the tool when it is opened:
- Selecting plot targets directly (which occurs when there are no other plots created and/or no plot edit buttons on the tool are pressed) will cause the bottom panel of the model display panel to be updated with available results and plot methods. Selecting Model, Assemblies or Parts as the Plot Target will target all structural elements contained in those objects, and return the available results.
- Plot Editing . If the user presses a plot edit button, when the user selects new objects to be plot target Apex will update the plot with the new plot target using all of the existing plot settings (with automatic or manual activation).
