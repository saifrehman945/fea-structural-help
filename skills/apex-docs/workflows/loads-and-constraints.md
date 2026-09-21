# Loads and constraints — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [1D Axial Deformation](#1d-axial-deformation-node-3084)
- [Acceleration Load](#acceleration-load-node-3093)
- [Beam Distributed Load](#beam-distributed-load-node-3082)
- [Beam Temperature](#beam-temperature-node-3089)
- [Constraint](#constraint-node-3075)
- [Constraint Combination](#constraint-combination-node-3095)
- [Create Constant Pressure](#create-constant-pressure-node-1272)
- [Create Constant Temperature Load](#create-constant-temperature-load-node-2601)
- [Displacement Constraints](#displacement-constraints-node-2024)
- [Dynamic Load](#dynamic-load-node-3087)
- [Enforced Motion](#enforced-motion-node-3083)
- [Enforced Motion - Abandoned](#enforced-motion-abandoned-node-2093)
- [Exclude Degrees of Freedom from AUTOSPC](#exclude-degrees-of-freedom-from-autospc-node-3078)
- [Field](#field-node-3119)
- [Force](#force-node-3079)
- [Force Moment - Abandoned](#force-moment-abandoned-node-2025)
- [Gravity Load](#gravity-load-node-1453)
- [Initial Beam Temperature](#initial-beam-temperature-node-3070)
- [Initial Displacement and Velocity](#initial-displacement-and-velocity-node-3073)
- [Initial Strain](#initial-strain-node-3071)
- [Initial Stress](#initial-stress-node-3072)
- [Initial Temperature](#initial-temperature-node-3096)
- [Load Combination](#load-combination-node-3086)
- [Load Mapping](#load-mapping-node-2454)
- [Load Scale Factor](#load-scale-factor-node-3085)
- [Lug Load](#lug-load-node-2746)
- [Moment](#moment-node-3080)
- [Multi-Component Force](#multi-component-force-node-3113)
- [Phase Lead](#phase-lead-node-3102)
- [Point Motion](#point-motion-node-3001)
- [Pressure](#pressure-node-3081)
- [Rotational Force](#rotational-force-node-3094)
- [Single Component Torque](#single-component-torque-node-2999)
- [Support](#support-node-3076)
- [Temperature](#temperature-node-3088)
- [Time Delay](#time-delay-node-3101)
- [Traction Load](#traction-load-node-2729)

---

## 1D Axial Deformation (node 3084)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3084.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create 1D Axial Deformation - Auto mode**

1. Enter the deformation value.
2. Select the entities you want to apply the 1d axial deformation to.

**Create 1D Axial Deformation - Manual mode**

1. Enter the deformation value.
2. Select the entities you want to apply the 1d axial deformation to and click MMB.

---

## Acceleration Load (node 3093)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3093.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Acceleration Load**

1. Enter the acceleration component values.
2. Select the load variation direction.
3. Enter the locations and scale factors along the direction.
4. Click Apply button or MMB to create the acceleration load.

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the acceleration load to.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the acceleration load to and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the acceleration load to.
2. Select/define the location of the acceleration load.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the acceleration load to and click MMB.
2. Select/define the location of the acceleration load and click MMB.

Tips:

- If the acceleration load components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport.

---

## Beam Distributed Load (node 3082)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3082.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Beam Distributed Load to 2-noded beam element - Auto mode**

1. Select the entities that you want to apply the load to.

**Create Beam Distributed Load to 2-noded beam element - Manual mode**

1. Select the entities that you want to apply the pressure to and click MMB.

**Create Beam Distributed Load to 3-noded beam element - Auto mode**

1. Select the entities that you want to apply the load to.

**Create Beam Distributed Load to 3-noded beam element - Manual mode**

1. Select the entities that you want to apply the load to and click MMB.

Tips:

- If X1 = X2, or X2 is blank, a concentrated load of value P1 will be applied at position X1.
- If X1 != X2, a linearly varying distributed load will be applied to the element between positions X1 and X2, having an intensity per unit length of bar equal to P1 at X1 and equal to P2 at X2 except the scale type is fractional/length projected.
- If P1 = P2 and X1!=X2, a uniform distributed load of intensity per unit length equal to P1 will be applied between positions X1 and X2 except the scale type is fractional/length projected.
- The load at each location is equal to load vector multiplies the magnitude and the scale factor.

---

## Beam Temperature (node 3089)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3089.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Beam Temperature to 2-noded beam element - Auto mode**

1. Enter the temperatures on end A and end B
2. Select the entities you want to apply the temperature load to.

**Create Beam Temperature to 2-noded beam element - Manual mode**

1. Enter the temperatures on end A and end B
2. Select the entities you want to apply the temperature load to and click MMB.

**Create Beam Temperature to 3-noded beam element- Auto mode**

1. Enter the temperatures on end A, end B and mid C.
2. Select the entities you want to apply the temperature load to.

**Create Beam Temperature to 3-noded beam element - Manual mode**

1. Enter the temperatures on end A, end B and mid C.
2. Select the entities you want to apply the temperature load to and click MMB.

Tips:

- Enter effective linear temperature gradient to define linear distributed temperature across the section.
- Enter temperature at point C, D, E, F for stress recovery. If not provided, linear temperature gradient is assumed for stress recovery.

---

## Constraint (node 3075)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3075.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Select the entities you want to constrain with the desired constraint type.

**Direct Approach - Manual mode**

1. Select the entities you want to constrain with the desired constraint type and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the constraint to.
2. Select/define the location of the constraint.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the constraint to and click MMB.
2. Select/define the location of the constraint.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the constraint to and click MMB.
2. Select/define the location of the constraint and click MMB.

Tips:

- In general constraint type, you can define the enforced displacement on each degree of freedom.

---

## Constraint Combination (node 3095)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3095.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Constraint Combination**

1. Check on the constraints that you want to combine.
2. Click MMB or Apply button to create the constraint combination.

---

## Create Constant Pressure (node 1272)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1272.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Constant Pressure - Auto mode**

1. Define parameters in the tool properties panel
2. Select either geometry faces, 2D mesh bodies, 2D elements, or free faces of solid elements that you want to apply the pressure to. To multi select hold SHIFT or CTRL or window pick and on release the pressure will be applied to the selected objects

**Create Constant Pressure - Manual mode**

1. Define parameters in the tool properties
2. Select either geometry faces, 2D mesh bodies, 2D elements, or free faces of solid elements that you want to apply the pressure to. To multi select hold SHIFT or CTRL or window pick, then click MMB or Apply button the pressure will be applied to the selected objects.

**Create Variable Pressure - Auto mode**

1. Select the target entity
2. Define mesh/pressure data and Apply

**Create Variable Pressure - Manual mode**

1. Select the target entity and Click MMB
2. Define mesh/pressure data and Apply
3. Click Apply button in the tool property panel when you are ready

---

## Create Constant Temperature Load (node 2601)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2601.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Constant Temperature Load - Auto mode**

1. Enter a constant temperature value.
2. Select the entities you want to apply the temperature load to.

**Create Constant Temperature Load - Manual mode**

1. Enter a constant temperature value.
2. Select the entities you want to apply the temperature load to.
3. Click middle mouse button (MMB) or Apply when you are ready.

**Create Variable Temperature Load - Auto mode**

1. Select the entities you want to apply the Temperature to.
2. Define the mesh/temperature table and Click Apply.

**Create Variable Temperature Load - Manual mode**

1. Select the entities you want to apply the Temperature to, then click MMB.
2. Define the mesh/temperature table and Click Apply to close the table.
3. Click MMB or Apply button.

Tips:

- To select multiple entities at the same time, hold down the SHIFT or the CTRL key, then select the entities you want. Alternatively, you can use box picking to select the region to apply constant temperature load.

---

## Displacement Constraints (node 2024)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2024.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

**Constrain using direct method - Manual mode**

1. Select the entities you want to constrain with the desired constraint type. Click middle mouse button (MMB) or Apply button when you are ready.

**Name and description: You have the option to customize the constraint name and description.**

1. Define your constraint orientation with the universal transform manipulator (UTM) or by specifying α, β and ɣ. By default the constraint will align with the global frame. Click MMB or Apply button when you are ready.

**Constrain using remote method - Auto mode**

1. Select the entities you want to constrain with the desired constraint type.

**Name and description: You have the option to customize the constraint name and description.**

1. Select the location of your constraint.

**Constrain using remote method - Manual mode**

1. Select the entities you want to constrain with the desired constraint type. Click middle mouse button (MMB) or Apply button when you are ready.

**Name and description: You have the option to customize the constraint name and description.**

1. Select the location of your constraint. Click MMB or Apply button when you are ready.
2. Define your constraint orientation with the universal transform manipulator (UTM) or by specifying α, β and ɣ. By default the constraint will align with the global frame. Click middle mouse button (MMB) or Apply button when you are ready.

**Concentrate Force**

1. Define the magnitude of your force and the direction from the tool properties panel
2. Select the entity(ies) you want to apply the force to using these 3 possible methods:

**Step 2.3: Window select the entities to apply one applied force to those entities upon release**

1. To modify the direction of the force you just created, you can do it in either of these 2 possible methods:

**Fixed Constraint**

1. Define the degrees of freedom of the constraint you want to create
2. Select the entity(ies) you want to apply the constraint to using these 3 possible methods:

**Step 2.3: Window select the entities to apply one applied constraint to those 0D entities**

1. To modify the degrees of freedom of the constraint you create just simply select/deselect either the arrows to turn on or off translational degrees of freedom or the rotational arrows to turn on or off the rotational degrees of freedom

**Procedure**

1. Then select the entity(ies) you want to apply that new force or constraint to, in the model

Tips:

- To select multiple entities at the same time, hold down the SHIFT or the CTRL key, then select the entities you want. Alternatively, you can use box picking to select the region to constrain.
- Double click the constraint on the viewport to EDIT.
- To apply the constraint at a special construction location (e.g. the center of the 2D hole, the mid-point of a curve), activate the UTM by selecting the Origin, hover the cursor over the desired Geometry entity, and select the desired construction marker.
- If you held SHIFT or CTRL you can accumulate multiple entities to apply an applied force to each entity but using the same force onto those entities.
- If you want to just modify the magnitude or the direction of the force you can do this by selecting the force during the tool.
- If you exited the tool you can, at anytime, double click the force or applied force object or the arrow glyph to put the force in an edit mode to modify it.
- If you want to relocate this applied force just exit the tool, and double click on the applied force object in the model browser or the force glyph on canvas and then you can relocate the force to a new entity.
- If you want to reuse an existing force definition in several locations please RMB click on the force object in the model browser and click "Apply" context menu, then select the entity(ies) you want to apply that force to.
- If you held SHIFT or CTRL you can accumulate multiple 0D entities to apply an applied constraint to each entity but using the same constraint definition.
- If you want to just modify the degrees of freedoms you can do this by reselecting the constraint during the tool, then select and deselect the degrees of freedom you want to remove or add.
- If you exited the tool you can, at anytime, double click the constraint or applied constraint object or the constraint glyph from the screen and put it in edit mode and modify the degrees of freedom.
- If you want to relocate this applied constraint just exit the tool, and double click on the applied constraint object and then you can relocate the applied constraint to a new entity.
- If you want to reuse an existing constraint definition in several locations please RMB click on the constraint object in the model browser and click "Apply" context menu, then select the entity(ies) you want to apply that constraint to.

---

## Dynamic Load (node 3087)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3087.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Dynamic Load - Frequency dependent, real/imag - Manual Mode**

1. Select the excitation loads for the dynamic load and click MMB.

**Create Dynamic Load – Acoustic Source - Auto Mode**

1. Select a load scale factor for the dynamic load.

**Create Dynamic Load - Frequency dependent, mag/phase - Manual Mode**

1. Select the excitation load for the dynamic load and click MMB.

**Create Dynamic Load - Time dependent form 1 - Manual Mode**

1. Select the excitation load for the dynamic load and click MMB.

**Create Dynamic Load - Time dependent form 2 - Manual Mode**

1. Select the excitation load for the dynamic load and click MMB.

**Create Dynamic Load – Acoustic Source - Manual Mode**

1. Select a load scale factor for the dynamic load and click MMB.

**Create Dynamic Load - Frequency dependent, real/imag - Auto Mode**

1. Select the excitation loads for the dynamic load.

**Create Dynamic Load - Frequency dependent, mag/phase - Auto Mode**

1. Select the excitation load for the dynamic load.

**Create Dynamic Load - Time dependent form 1 - Auto Mode**

1. Select the excitation load for the dynamic load.

**Create Dynamic Load - Time dependent form 2 - Auto Mode**

1. Select the excitation load for the dynamic load.

Tips:

- The excitation loads determine the dynamic load type and the amplitude of the frequency response function.
- Enter a value or define a dynamic load table to define the real and imaginary parts of the frequency response function.
- Enter a value or create the object to define the time delay and phase lead of the frequency response function.
- Enter a value or define a dynamic load table to define the magnitude and phase angle of the frequency response function.
- Enter a value or define a table to define the time delay and phase lead of the frequency response function.
- The excitation loads determine the dynamic load type and the amplitude of the time response function.
- Enter a value or define a dynamic load table to define the time response function.
- Enter a value or define a table to define the time delay of the time response function.

---

## Enforced Motion (node 3083)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3083.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the enforced motion to.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the enforced motion to and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the enforced motion to.
2. Select/define the location of the enforced motion.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the enforced motion to and click MMB.
2. Select/define the location of the enforced motion and click MMB.

Tips:

- If the enforced motion components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport.

---

## Enforced Motion - Abandoned (node 2093)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2093.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `O` | Cycle pick selections in aperture |

**Direct Approach - Auto mode**

1. Select entitles you want to apply Enforced - Motion to.

**Direct Approach - Manual mode**

1. Select entitles you want to apply Enforced - Motion to.
2. Click MMB.

**Remote Approach - Auto**

1. Select entitles you want to apply Enforced - Motion to.
2. Select/define the location of the Enforced - Motion.

**Remote Approach - Manual**

1. Select entitles you want to apply Enforced - Motion to.
2. Click MMB.
3. Select/define the location of the Enforced - Motion.
4. Click MMB.

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key.

---

## Exclude Degrees of Freedom from AUTOSPC (node 3078)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3078.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Exclude degrees of freedom from AUTOSPC - Auto mode**

1. Check on the degrees of freedom to be excluded.
2. Select the entities you want to exclude the degrees of freedom from.

**Exclude degrees of freedom from AUTOSPC - Manual mode**

1. Check on the degrees of freedom to be excluded.
2. Select the entities you want to exclude the degrees of freedom from and click MMB.

---

## Field (node 3119)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3119.html

**Create Discrete FEM Field - Auto mode**

1. Enter the field default properties.
2. Select the entities that you want to add/remove/toggle in the field.
3. Click Apply button to create the field.

**Create Discrete FEM Field - Manual mode**

1. Enter the field default properties.
2. Select the entities that you want to add/remove/toggle in the field and then click MMB.
3. Click Apply button to create the field.

Tips:

- You can manually edit or define the property values in the field table.
- Import a csv file to create the field table. Note that the column headers must be consistent with the field column header with units, you can export the data as csv file to check the correct column headers.

---

## Force (node 3079)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3079.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the force to.

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the force to.
2. Select two points to define the 1st vector.
3. Select two points to define the 2nd vector.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the force to and click MMB.
2. Select two points to define the 1st vector and click MMB.
3. Select two points to define the 2nd vector and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the force to.
2. Select/define the location of the force.
3. Select a point to define the starting point.
4. Select a point to define the end point.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the force to and click MMB.
2. Select/define the location of the force and click MMB.
3. Select a point to define the starting point and click MMB.
4. Select a point to define the end point and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the force to
2. Select/define the location of the force.
3. Select two points to define the 1st vector.
4. Select two points to define the 2nd vector.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the force to and click MMB.
2. Select/define the location of the force and click MMB.
3. Select two points to define the 1st vector and click MMB.
4. Select two points to define the 2nd vector and click MMB.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the force to and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the force to.
2. Select/define the location of the force.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the force to and click MMB.
2. Select/define the location of the force and click MMB.

**Create Discrete FEM Field - Auto mode**

1. Enter the field default properties.
2. Select the entities that you want to add in the field.
3. Click Apply button to create the field.

**Create Discrete FEM Field - Auto mode**

1. Enter the field default properties.
2. Select the entities that you want to remove from the field.
3. Click Apply button to create the field.

**Create Discrete FEM Field - Auto mode**

1. Enter the field default properties.
2. Select the entities that you want to toggle in the field.
3. Click Apply button to create the field.

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the force to.
2. Select a point to define the starting point.
3. Select a point to define the end point.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the force to and click MMB.
2. Select a point to define the starting point and click MMB.
3. Select a point to define the end point and click MMB.

Tips:

- If the force components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport.

---

## Force Moment - Abandoned (node 2025)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2025.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Select entitles you want to apply Force - moment to.

**Direct Approach - Manual mode**

1. Select entitles you want to apply Force - moment to.
2. Click MMB.

**Remote Approach - Auto**

1. Select entitles you want to apply Force - moment to.
2. Select/define the location of the Force - Moment.

**Remote Approach - Manual**

1. Select entitles you want to apply Force - moment to.
2. Click MMB.
3. Select/define the location of the Force - Moment.
4. Click MMB.

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key.

---

## Gravity Load (node 1453)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1453.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |

**Create gravity load**

1. Enter desired values into the tool property editor
2. Click MMB or Apply button to complete the creation of the gravity load

**Modify gravity load while in the tool**

1. Select then Double Click on the gravity load object
2. Enter data into the pop up dialog
3. Click in canvas or ESC to exit edit mode

**Modify gravity load when outside the tool**

1. Double Click on the gravity load object
2. Enter data into the gravity properties dialog
3. Click Apply button to complete the modification of the gravity load and exit edit mode

---

## Initial Beam Temperature (node 3070)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3070.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Beam Temperature to 2-noded beam element - Auto mode**

1. Enter the temperatures on end A and end B.
2. Select the entities you want to apply the initial temperature to.

**Create Beam Temperature - Manual mode**

1. Enter the temperatures on end A and end B.
2. Select the entities you want to apply the initial temperature to and click MMB.

**Create Beam Temperature to 3-noded beam element- Auto mode**

1. Enter the temperatures on end A, end B and mid C.
2. Select the entities you want to apply the initial temperature to.

**Create Beam Temperature to 3-noded beam element - Manual mode**

1. Enter the temperatures on end A, end B and mid C.
2. Select the entities you want to apply the initial temperature to and click MMB.

Tips:

- Enter effective linear temperature gradient to define linear distributed temperature across the section.
- Enter temperature at point C, D, E, F for stress recovery. If not provided, linear temperature gradient is assumed for stress recovery.

---

## Initial Displacement and Velocity (node 3073)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3073.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Initial Displacement and Velocity- Auto mode**

1. Enter the initial displacement and velocity values.
2. Select the entities you want to apply the initial displacement and velocity to.

**Create Initial Displacement and Velocity- Manual mode**

1. Enter the initial displacement and velocity values.
2. Select the entities you want to apply the initial displacement and velocity to and click MMB.

---

## Initial Strain (node 3071)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3071.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Initial Strain - Auto mode**

1. Enter the strain component values.
2. Enter the element layer and integration point values.
3. Select the entities you want to apply the initial strain to.

**Create Initial Strain - Manual mode**

1. Enter the strain component values.
2. Enter the element layer and integration point values.
3. Select the entities you want to apply the initial strain to and click MMB.

---

## Initial Stress (node 3072)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3072.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Initial Stress - Auto mode**

1. Enter the stress component values.
2. Enter the element layer and integration point values.
3. Select the coordinate system that the stresses are evaluated.
4. Select the entities you want to apply the initial stress to.

**Create Initial Stress - Manual mode**

1. Enter the stress component values.
2. Enter the element layer and integration point values.
3. Select the coordinate system that the stresses are evaluated.
4. Select the entities you want to apply the initial stress to and click MMB.

---

## Initial Temperature (node 3096)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3096.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Temperature Nodal- Auto mode**

1. Enter the temperature value.
2. Select the entities you want to apply the initial temperature to.

**Create Temperature Nodal- Manual mode**

1. Enter the temperature value.
2. Select the entities you want to apply the initial temperature to and click MMB.

**Create Surface Temperature- Auto mode**

1. Enter the temperature at reference plane.
2. Select the entities you want to apply the initial temperature to.

**Create Surface Temperature - Manual mode**

1. Enter the temperatures on end A and end B.
2. Select the entities you want to apply the initial temperature to and click MMB.

**Create Heat Transfer Temperature - Auto mode**

1. Enter the temperature values on top/bottom/mid across the thickness direction.
2. Select the entities you want to apply the initial temperature to.

**Create Temperature Load - Manual mode**

1. Enter the temperature values on top/bottom/mid across the thickness direction.
2. Select the entities you want to apply the initial temperature to and click MMB.

**Create Default Temperature**

1. Enter the default temperature value and click MMB.

Tips:

- Enter effective linear temperature gradient to define linear distributed temperature across the section.
- Enter temperature at lower and upper surfaces for stress recovery.
- This temperature load should be only applied to the nodes of 2d elements with PSHLN1 property that ANAL is "IH" or "ISH"
- This temperature load is only used in nonlinear scenario, steady-state heat transfer analysis and transient heat analysis.
- This temperature load should be only applied to the nodes of 2d elements with PSHLN1 property that ANAL is "IH" or "ISH" and used in nonlinear scenario.
- This temperature load is only used in nonlinear scenario, steady-state heat transfer analysis and transient heat transfer analysis.
- The default temperature is a global environment temperature. It is implicitly applied to all nodes in the model that have not been applied with other temperature loads.

---

## Load Combination (node 3086)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3086.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Static Load Combination**

1. Check on the loads that you want to combine.
2. Click MMB or Apply button to create the load combination.

**Create Dynamic Load Combination**

1. Select the dynamic loads that you want to combine.
2. Click MMB or Apply button to create the load combination.

Tips:

- A static load combination can combine other existing static load combinations to create a nested static load combination object.

---

## Load Mapping (node 2454)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2454.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Procedure**

1. Select an Adams part or Apex part/assembly in viewport and click MMB to confirm

**Procedure**

1. Select an interface point in Adams viewport
2. Select a node tie in Apex viewport

**Procedure**

1. Select a transient dynamic scenario to list the critical response points
2. Select or deselect the critical response points that you need or do not need
3. Click Create new Quasi-Static Scenario button to create scenario

**Procedure**

1. Select an interface point in Adams viewport
2. Click MMB
3. Select a node tie in Apex viewport
4. Click MMB

Tips:

- Re-select an interface point which is already associated with a node tie will clear the previous association
- You can associate multiple interface points to one node tie if necessary

---

## Load Scale Factor (node 3085)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3085.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the load scale factor to.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the load scale factor to and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the load scale factor to.
2. Select/define the location of the load scale factor.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the load scale factor to and click MMB.
2. Select/define the location of the load scale factor and click MMB.

Tips:

- If the load scale factor components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport.
- If the load scale factor components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport

---

## Lug Load (node 2746)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2746.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Lug Load Tool- Auto mode**

1. Select a cylinder face or circle edge to apply the lug load.

**Lug Load Tool - Manual mode**

1. Select a cylinder face or circle edge to apply the lug load.
2. Click MMB or Apply button to create the lug load.

Tips:

- Only circle edge or cylinder face can be selected.
- Split the edge or face to adjust mesh distribution.

---

## Moment (node 3080)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3080.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the moment to.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the moment to and click MMB.
2. Select/define the location of the moment and click MMB.
3. Select a point to define the starting point and click MMB.
4. Select a point to define the end point and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to apply the Moment to.
2. Select/define the location of the moment.
3. Select two points to define the 1st vector.
4. Select two points to define the 2nd vector.

**Remote Approach - Manual mode**

1. Select the entities that you want to apply the Moment to and click MMB.
2. Select/define the location of the moment and click MMB.
3. Select two points to define the 1st vector and click MMB.
4. Select two points to define the 2nd vector and click MMB

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the moment to and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the moment to.
2. Select/define the location of the moment.

**Remote Approach - Manual mode**

1. Select the entities that you want to distribute the moment to and click MMB.
2. Select/define the location of the moment and click MMB.

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the Moment to.
2. Select a point to define the starting point.
3. Select a point to define the end point.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the Moment to and click MMB.
2. Select a point to define the starting point and click MMB.
3. Select a point to define the end point and click MMB.

**Direct Approach - Auto mode**

1. Select the entities that you want to apply the Moment to.
2. Select two points to define the 1st vector.
3. Select two points to define the 2nd vector.

**Direct Approach - Manual mode**

1. Select the entities that you want to apply the Moment to and click MMB.
2. Select two points to define the 1st vector and click MMB.
3. Select two points to define the 2nd vector and click MMB.

**Remote Approach - Auto mode**

1. Select the entities that you want to distribute the moment to.
2. Select/define the location of the moment.
3. Select a point to define the starting point.
4. Select a point to define the end point.

Tips:

- If the moment components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport.

---

## Multi-Component Force (node 3113)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3113.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining axis location |
| `R` | Change transform manipulator as rotate mode when defining axis orientation |

**Creation method - 2 Bodies, 1 Locations - Automatic Mode**

1. Enter a function or the component values or expressions that define the force
2. Select the entities for the action part
3. Select the entities for the reaction part
4. Select the entity to orient the first axis of the force
5. Select the entity to orient the second axis of the force

**Creation method - 2 Bodies, 1 Locations - Manual Mode**

1. Enter a function or the component values or expressions that define the force
2. Select the entities for the action part
3. Click MMB
4. Select the entities for the reaction part
5. Click MMB
6. Select the entities to locate the force
7. Click MMB
8. Select the entity to orient the first axis of the force
9. Click MMB
10. Select the entity to orient the second axis of the force
11. Click MMB
12. Select the entities for the reference part
13. Click MMB

**Creation method - 3 Interfaces - Automatic Mode**

1. Enter a function or the component values or expressions that define the force
2. Select the interface for the action part
3. Select the floating marker for the reaction part
4. Select the interface to orient the force

**Creation method - 3 Interfaces - Manual Mode**

1. Enter a function or the component values or expressions that define the force
2. Select the interface for the action part
3. Click MMB
4. Select the floating marker for the reaction part
5. Click MMB
6. Select the interface to orient the force
7. Click MMB

Tips:

- To multi select in either end, hold down the CTRL or SHIFT key and select the entities

---

## Phase Lead (node 3102)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3102.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Phase Lead - Auto Mode**

1. Enter the phase lead value on the degrees of freedom applied with the excitation loads.
2. Select the entities that you want to apply with phase leads.

**Create Phase Lead - Manual Mode**

1. Enter the phase lead value on the degrees of freedom applied with the excitation loads.
2. Select the entities that you want to apply with phase leads and click MMB.

Tips:

- The nodes applied with the phase lead should be the same with the target nodes of the excitation loads.
- The degrees of freedom applied with phase lead should be the same with the excitation loads.

---

## Point Motion (node 3001)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3001.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Point Motion - Auto mode**

1. Enter a function that defines the motion with respect to time
2. Select the moving part
3. Select the reference part

**Point Motion - Manual mode**

1. Enter a function that defines the motion with respect to time
2. Select the moving part
3. Click MMB
4. Select the reference part
5. Click MMB
6. Select the entity to locate the motion
7. Click MMB
8. Select the entity to orient the motion
9. Click MMB

**Point Motion - Manual mode**

1. Enter a function that defines the motion with respect to time
2. Select the moving part
3. Click MMB
4. Select the entity to locate the motion for the moving part
5. Click MMB
6. Select the entity to orient the motion for the moving part
7. Click MMB
8. Select the reference part
9. Click MMB
10. Select the entity to locate the motion for the reference part
11. Click MMB
12. Select the entity to orient the motion for the reference part
13. Click MMB

**Point Motion - Auto mode**

1. Enter a function that defines the motion with respect to time
2. Select the interface that identifies the moving part
3. Select the interface that identifies the reference part

**Point Motion - Manual mode**

1. Enter a function that defines the motion with respect to time
2. Select the interface that identifies the moving part
3. Click MMB
4. Select the interface that identifies the reference part
5. Click MMB

Tips:

- To multi-select at either end, hold down the CTRL or SHIFT key and select the entities

---

## Pressure (node 3081)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3081.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Plane Pressure - Auto mode**

1. Select arbitrary three or four non-collinear points to apply the pressure to.

**Create Total Load - Manual mode**

1. Select the entities that you want to apply the total load to and click MMB or Apply button.

**Create Plane Pressure - Manual mode**

1. Select arbitrary three or four non-collinear points to apply the pressure to and click MMB.

**Create 2D Surface Pressure - Auto mode**

1. Select the entities that you want to apply the pressure to.

**Create 2D Surface Pressure - Manual mode**

1. Select the entities that you want to apply the pressure to and click MMB.

**Create Pressure - Auto mode**

1. Select the entities that you want to apply the pressure to.

**Create Pressure - Manual mode**

1. Select the entities that you want to apply the pressure to and click MMB.

**Create Distributed Load- Auto mode**

1. Select the entities that you want to apply the distributed load to.

**Create Distributed Load - Manual mode**

1. Select the entities that you want to apply the distributed load to and click MMB.

**Create Total Load - Auto mode**

1. Select the entities that you want to apply the total load to.

Tips:

- The total load is evenly applied to the points as concentrated load.
- The total load components are defined in the basic coordinate system by default, select a coordinate system object or enter a coordinate system id to define a different orientation.
- The vector components(N1, N2, N3) is only used to determine the load direction.
- Enter a coordinate system ID or select a coordinate system if the vector components are not defined in the basic coordinate system.

---

## Rotational Force (node 3094)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3094.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Rotational Force**

1. Enter the rotation vector components.
2. Select a point as the rotation center or skip the selection to use the absolute origin as the rotation center.

Tips:

- If the rotation components are not defined in the basic coordinate system, enter a coordinate system ID or select a coordinate system from viewport.

---

## Single Component Torque (node 2999)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2999.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Single Component Torque - Manual mode**

1. Enter a function that defines the torque
2. Select the entities for the point of application that defines the torque
3. Click MMB
4. Select the entities to locate the torque
5. Click MMB
6. Select the entities to orient the torque
7. Click MMB

**Single Component Torque - Auto mode**

1. Enter a function that defines the torque
2. Select the interface for the point of application that defines the torque
3. Select the interface on part ground whose Z axis orients the torque

**Single Component Torque - Manual mode**

1. Enter a function that defines the torque
2. Select the interface for the action part
3. Click MMB
4. Select the interface for the reaction part
5. Click MMB

**Single Component Torque - Auto mode**

1. Enter a function that defines the torque
2. Select the interface for the action part
3. Select the interface for the reaction part

**Single Component Torque - Manual mode**

1. Enter a function that defines the torque
2. Select the interface for the point of application
3. Click MMB
4. Select the interface for the moving reference part whose Z axis orients the torque
5. Click MMB

**Single Component Torque - Auto mode**

1. Enter a function that defines the torque
2. Select the interface for the point of application
3. Select the interface for the moving reference part whose Z axis orients the torque

**Single Component Torque - Auto mode**

1. Enter a function that defines the torque
2. Select the entities for the point of application that defines the torque

**Single Component Torque - Manual mode**

1. Enter a function that defines the torque
2. Select the entities for the point of application
3. Click MMB
4. Select the entities for the moving reference frame
5. Click MMB
6. Select the entities to locate the torque on the part
7. Click MMB
8. Select the entities for the location on the reference part
9. Click MMB
10. Select the entities that orient the torque
11. Click MMB

**Single Component Torque - Auto mode**

1. Enter a function that defines the torque
2. Select the entities for the point of application
3. Select the entities for the moving reference frame

**Single Component Torque - Manual mode**

1. Enter a function or spring stiffness and damping coefficients that define the torque
2. Select the entities for the action part
3. Click MMB
4. Select the entities for the reaction part
5. Click MMB
6. Select the entities to locate the torque for the action part
7. Click MMB
8. Select the entities to locate the torque for the reaction part
9. Click MMB

**Single Component Torque - Auto mode**

1. Enter a function or spring stiffness and damping coefficients that define the torque
2. Select the entities for the action part
3. Select the entities for the reaction part

**Single Component Torque - Manual mode**

1. Enter a function that defines the torque
2. Select the interface for the point of application that defines the torque
3. Click MMB
4. Select the interface on ground whose Z axis orients the torque
5. Click MMB

**Single Component Torque - Auto mode**

1. Enter a function that defines the torque
2. Select the interface for the point of application that defines the torque
3. Select the interface on ground whose Z axis orients the torque

**Single Component Torque - Manual mode**

1. Enter a function that defines the torque
2. Select the interface that defines the location of the torque
3. Click MMB
4. Select the interface on part ground whose Z axis orients the torque
5. Click MMB

Tips:

- To multi-select at either end, hold down the CTRL or SHIFT key and select the entities

---

## Support (node 3076)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3076.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Direct Approach - Auto mode**

1. Check on the degrees of freedom to be constrained.
2. Select the entities you want to constrain.

**Direct Approach - Manual mode**

1. Check on the degrees of freedom to be constrained.
2. Select the entities you want to constrain and click MMB.

**Remote Approach - Auto mode**

1. Check on the degrees of freedom to be constrained.
2. Select the entities that you want to distribute the support to.
3. Select/define the location of the support.

**Remote Approach - Manual mode**

1. Check on the degrees of freedom to be constrained.
2. Select the entities that you want to distribute the support to and click MMB.
3. Select/define the location of the support and click MMB.

---

## Temperature (node 3088)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3088.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Temperature Nodal- Auto mode**

1. Enter the temperature value.
2. Select the entities you want to apply the temperature load to.

**Create Temperature Nodal- Manual mode**

1. Enter the temperature value.
2. Select the entities you want to apply the temperature load to and click MMB.

**Create Surface Temperature- Auto mode**

1. Enter the temperature at reference plane.
2. Select the entities you want to apply the temperature load to.

**Create Surface Temperature - Manual mode**

1. Enter the temperatures on end A and end B.
2. Select the entities you want to apply the temperature load to and click MMB.

**Create Heat Transfer Temperature - Auto mode**

1. Enter the temperature values on top/bottom/mid across the thickness direction.
2. Select the entities you want to apply the temperature load to.

**Create Temperature Load - Manual mode**

1. Enter the temperature values on top/bottom/mid across the thickness direction.
2. Select the entities you want to apply the temperature load to and click MMB.

**Create Default Temperature**

1. Enter the default temperature value and click Apply button.

Tips:

- Enter effective linear temperature gradient to define linear distributed temperature across the section.
- Enter temperature at lower and upper surfaces for stress recovery.
- This temperature load should be only applied to the nodes of 2d elements with PSHLN1 property that ANAL is "IH" or "ISH"
- This temperature load is only used in nonlinear scenario, steady-state heat transfer analysis and transient heat analysis.
- This temperature load should be only applied to the nodes of 2d elements with PSHLN1 property that ANAL is "IH" or "ISH" and used in nonlinear scenario.
- This temperature load is only used in nonlinear scenario, steady-state heat transfer analysis and transient heat transfer analysis.
- The default temperature is a global environment temperature. It is implicitly applied to all nodes in the model that have not been applied with other temperature loads.

---

## Time Delay (node 3101)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3101.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Create Time Delay - Auto Mode**

1. Enter the time delay value on the degrees of freedom applied with the excitation loads.
2. Select the entities that you want to apply with time delays.

**Create Time Delay - Manual Mode**

1. Enter the time delay value on the degrees of freedom applied with the excitation loads.
2. Select the entities that you want to apply with time delays and click MMB.

Tips:

- The nodes applied with the time delay should be the same with the target nodes of the excitation loads.
- The degrees of freedom applied with time delay should be the same with the excitation loads.

---

## Traction Load (node 2729)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2729.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Traction Load Tool - Auto mode**

1. Select the entities that you want to apply the traction load to.

**Traction Load Tool - Manual mode**

1. Select the entities you want to apply traction load to.
2. Click MMB to adjust traction load orientation.
3. Click MMB or Apply button to create the traction load.

Tips:

- In Auto mode, traction load is automatically created by default orientation. If you want to adjust the orientation, please use manual mode.
