# Attribution: materials, properties, fields — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [Assign Attributes](#assign-attributes-node-1074)
- [Assign Material](#assign-material-node-3051)
- [Auto Thickness](#auto-thickness-node-1089)
- [Auto-Thickness Field](#auto-thickness-field-node-3050)
- [Behaviors](#behaviors-node-1075)
- [Fields](#fields-node-3049)
- [Interface](#interface-node-2201)
- [Material Orientation Field](#material-orientation-field-node-3040)
- [Material Orientation Field](#material-orientation-field-node-3048)
- [Nonstructural Mass](#nonstructural-mass-node-2455)
- [NSM Combination (NSMADD)](#nsm-combination-nsmadd-node-3144)
- [Panels](#panels-node-2229)
- [Point Mass](#point-mass-node-1452)
- [Thickness and Offset Field](#thickness-and-offset-field-node-3065)

---

## Assign Attributes (node 1074)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1074.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Assign Attributes - Auto**

1. If an attribute (i.e. material, section or behavior) is already selected from their respective panel, then proceed to Step 2, otherwise create the attribute(s) and select the attribute of choice.
2. Select the entities to assign the selected attribute to.

**Assign Attributes - Manual**

1. If an attribute (i.e. material, section or behavior) is already selected from their respective panel, then proceed to Step 2, otherwise create the attribute(s) and select the attribute of choice.
2. Select the entities that you want to assign the selected attribute to.
3. Click MMB to execute the assignment operation.

**Assign Sections - Auto**

1. Select the entities to assign the section to.

**Assign Sections - Manual**

1. Select the entities to assign the section to.
2. Click middle mouse button (MMB) or Apply button when you are ready.

Tips:

- To assign the same attribute to several entities, simply select those entities. Window picking helps to select many items in one shot.
- To change your attribute simply select the new attribute then select the entity
- To delete an assigned attribute, double click on the Part to get the object properties and delete the attribute of choice from the list.

---

## Assign Material (node 3051)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3051.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Assign Materials - Auto**

1. Select the entities to assign the selected material to.

**Assign Materials - Manual**

1. Select the entities to assign the selected material to.
2. Click middle mouse button (MMB) or Apply button when you are ready.

---

## Auto Thickness (node 1089)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1089.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Auto Thickness Assignment**

1. Select sheet bodies, general bodies or faces
2. Click MMB to transition to selecting Solids
3. Select the solid(s) to use for calculating the thickness
4. Click MMB to calculate thickness

**Auto Thickness Assignment**

1. Select meshed face as middle face
2. Click MMB to transition to select top face(s)
3. Click MMB to transition to select bottom face(s)
4. Click MMB to calculate thickness

Tips:

- Adjust the Max Thickness to limit the thickness in very thick areas. Make sure this thickness is larger than the maximum acceptable thickness.

---

## Auto-Thickness Field (node 3050)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3050.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure de-selection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Variable Auto-Thickness- Manual mode**

1. Select the midsurface with mesh assigned and Click MMB to recalculate the thickness/offset based on current face pairs and new midsurface target
2. Define constant thickness/offset value in the tool properties to overwrite the auto-calculated thickness/offset value
3. Click Apply button in the tool property panel when you are ready

**Create Constant Auto-Thickness- Manual mode**

1. Select the midsurface with mesh assigned and Click MMB to recalculate the thickness/offset based on current face pairs and new midsurface target
2. Define constant thickness/offset value in the tool properties to overwrite the auto-calculated thickness/offset value
3. Click Apply button in the tool property panel when you are ready

---

## Behaviors (node 1075)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1075.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Assign Behaviors - Auto**

1. Select the entities to assign the behavior to.

**Assign Behaviors - Manual**

1. Select the entities to assign the behavior to.
2. Click middle mouse button (MMB) or Apply button when you are ready.

Tips:

- To assign the same attribute to several entities, simply select those entities. Window picking helps to select many items in one shot.
- To change your attribute simply select the new attribute then select the entity
- To delete an assigned attribute, double click on the Part to get the object properties and delete the attribute of choice from the list.

---

## Fields (node 3049)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3049.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure de-selection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Variable Thickness/Offset - Manual mode**

1. Select the target entity and Click MMB
2. Define mesh/thickness or offset data and Apply
3. Click Apply button in the tool property panel when you are ready

**Create Variable Material Orientation - Manual mode**

1. Select the target entity and Click MMB
2. Define mesh/angle or coordinate system ID and Apply
3. Click Apply button in the tool property panel when you are ready

**Create Constant Thickness/Offset - Manual mode**

1. Select the target entity and Click MMB
2. Define constant thickness or offset value in the tool property page
3. Click Apply button in the tool property panel when you are ready

---

## Interface (node 2201)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2201.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT+MMB` | Transitions to previous selection stage |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure de-selection |

**Interface Point - Auto mode**

1. Select an entity to create & associate an interface point to it at its location.

**Interface Point - Manual mode**

1. Select an entity to create & associate an interface point to it at its location, then click MMB.
2. Select an existing coordinate system or specify Euler angle to define orientation, then click MMB or click MMB to complete directly.

**Interface Point - Auto mode**

1. Select the entities attaching to an interface point.

**Interface Point - Manual mode**

1. Select the entities attaching to interface point and click MMB.
2. Select the entity to define the interface point location and click MMB.
3. Select an existing coordinate system or specify Euler angle to define orientation, then click MMB to complete or click MMB to complete directly.

Tips:

- Once you select the entity in the stage 1, the stage 2 will be skipped and the interface point will be created with default or user defined orientation automatically. Switch to manual mode to sequentially execute all stages.
- If you want to specify orientation prior to stage 1, specify Euler angles in the orientation text box or activate selection stage 2 to select existing coordinate system.
- If the orientation is undefined in orientation stage, the system will provide a default orientation.
- You can click MMB to complete in stage 2 without defining orientation, the system will align the interface point to global orientation.
- Once you select the entities in the stage 1, the stage 2 and stage 3 will be skipped and the interface point will be created with default location and default or user defined orientation automatically. Switch to manual mode to sequentially execute all stages.
- If you want to specify orientation prior to stage 1, specify Euler angles in the orientation text box or activate selection stage 3 to select existing coordinate system.
- You can click MMB to complete in stage3 without defining orientation, the system will align the interface point to global orientation.

---

## Material Orientation Field (node 3040)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3040.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure de-selection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Material orientation Assignment - Auto mode**

1. Select the entities to assign the material orientation to
2. Select the entity to align the material orientation

**Material orientation Assignment - Manual mode**

1. Select the entities to assign the material orientation to
2. Click middle mouse button (MMB)
3. Select the entity to align the material orientation
4. Click middle mouse button (MMB) or Apply button when you are ready

---

## Material Orientation Field (node 3048)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3048.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure de-selection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Variable Auto-Thickness - Auto mode**

1. Select the midsurface with mesh assigned and Click MMB to recalculate the thickness/offset based on current face pairs and new midsurface target
2. Define mesh/thickness/offset data and Apply to overwrite the auto-calculated thickness/offset value
3. Click Apply button in the tool property panel when you are ready

**Create Constant Auto-Thickness - Manual mode**

1. Select the midsurface with mesh assigned and Click MMB to recalculate the thickness/offset based on current face pairs and new midsurface target
2. Define constant thickness/offset value in the tool properties to overwrite the auto-calculated thickness/offset value
3. Click Apply button in the tool property panel when you are ready

**Create Variable Thickness/Offset - Manual mode**

1. Select the target entity and Click MMB
2. Define mesh/thickness or offset data and Apply
3. Click Apply button in the tool property panel when you are ready

**Create Variable Material Orientation - Manual mode**

1. Select the target entity and Click MMB
2. Define mesh/angle or coordinate system ID and Apply
3. Click Apply button in the tool property panel when you are ready

**Create Constant Thickness/Offset - Manual mode**

1. Select the target entity and Click MMB
2. Define constant thickness or offset value in the tool property page
3. Click Apply button in the tool property panel when you are ready

---

## Nonstructural Mass (node 2455)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2455.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previously hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Nonstructural Mass - Auto mode**

1. Select entities to apply nonstructural mass

**Nonstructural Mass - Manual mode**

1. Select entities to apply nonstructural mass
2. Click MMB or Apply

Tips:

- The total mass method will apply total mass to selected entities. You can either select 2D entities or 1D entities to apply; it will not support both at the same time.

---

## NSM Combination (NSMADD) (node 3144)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3144.html

**NSM Combination**

1. Select nonstructural mass that you want to combine in data grid.
2. Click MMB or Apply button to complete.

---

## Panels (node 2229)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2229.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `UP/Down arrows` | Progress through Ply Lists |
| `Left/Right arrows` | Progress through Zones |
| `CTRL+Click` | De-select the selected ply or zone |

**Use this tab to define the properties of the entire panel**

1. Select a single surface to be used as the tool surface
2. Click MMB
3. Adjust properties of the panel if desired
4. Progress to the Plies tab to build the laminate

**Use this tab to build up the laminate with plies**

1. Define the properties of the ply to be added (optional)
2. Press "Add Ply" button
3. Specify ply coverage by selecting contiguous faces, zones or the entire tool surface
4. Click MMB to manifest the ply
5. Continue adding plies by specifying coverage and clicking MMB
6. Click "Done" when finished adding plies

Tips:

- •adjust the offset via the glyph or entering a value
- •adjust the material orientation via the glyph or entering Euler angles
- •flip the build direction in which plies will be stacked
- Use the focus control icons to alter the scope of the view: Current Panel or Full Mechanical System
- Use the "Switch Surface" button to select a different tool surface
- Use Material tool to create and edit ply materials
- Use the Plies table to edit the properties of any ply
- Use Zones to identify contiguous regions of consistent layup as well as alter the position of plies within a layup
- Set the Zone properties if needed, leaving Zone properties blank will use the panel properties

---

## Point Mass (node 1452)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1452.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure de-selection |
| `Z/C` | Enlarge/shrink snap box |
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Point Mass - Auto mode**

1. Select an entity to create and associate a point mass to it at its location.

**Point Mass - Manual mode**

1. Select the entity(ies) that you want to create and associate point masses to, at their location.
2. Click MMB to execute the creation of the point masses.

**Point Mass**

1. Enter the coordinates of where you want this point mass to be created.
2. Define the moments of inertia.
3. Click MMB or press the apply button.

**Point Mass - Auto mode**

1. Select an entity to create and associate a point mass to it.
2. Select an entity to use as the reference to define the location of the point mass.

**Point Mass - Manual mode**

1. Select the entity(ies) that you want to associate the point mass to.
2. Click MMB to switch to selecting the 0D entity you want to use as reference to define the location of the point mass.
3. Select the 0D entity you want to use as a reference for the location of the point mass.
4. Click MMB to execute the creation of the point masses.

Tips:

- If you want to create point masses on multiple selections hold down the SHIFT or the CTRL key, then select the entities, then release your finger from the key. This will create a unique point mass associated to each unique 0D entity and located at the position of each unique 0D entity.
- You can redefine the location of the point mass by entering new coordinates in the coordinate's box that is associated to the transform manipulator.
- If you want to go back to (de)selecting entities that you are associating the point mass to, hold SHIFT then click MMB then deselect the entities, then proceed as you would from step 1.
- You can also edit the location of point mass by using the transform manipulator. To translate drag the axes. To change from translation to rotation select the center rings component. To rotate drag the rotation rings. You can always drag and snap to a particular target entity.
- If you want to associate the point mass to multiple 0D entities, hold down the SHIFT or the CTRL key, then select the entities, and then release your finger from the key. This will associate the entities you selected to that single point mass.

---

## Thickness and Offset Field (node 3065)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3065.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Auto mode**

1. Specify a thickness value.
2. Select a target to apply.

**Manual mode**

1. Specify a thickness value.
2. Select a target to complete.
3. Click MMB.

**Auto mode**

1. Specify an offset value.
2. Select a target to apply.

**Manual mode**

1. Specify an offset value.
2. Select a target to complete.
3. Click MMB.
