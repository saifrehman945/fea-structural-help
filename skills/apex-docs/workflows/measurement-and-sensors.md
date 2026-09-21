# Measurement, sensors and coordinate tools — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [Angle](#angle-node-970)
- [Assign Coordinate System](#assign-coordinate-system-node-2730)
- [Clearance Sensor](#clearance-sensor-node-2234)
- [Coordinate System](#coordinate-system-node-2341)
- [Diameter](#diameter-node-969)
- [Distance](#distance-node-968)
- [Motion Envelope](#motion-envelope-node-2235)
- [Point Sensor](#point-sensor-node-2079)
- [Probe](#probe-node-2289)
- [Reference System](#reference-system-node-3054)
- [Transform](#transform-node-966)
- [X-Section Force Sensor](#x-section-force-sensor-node-2169)

---

## Angle (node 970)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/970.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Dismiss measured dimensions |
| `P` | Toggle visibility picking versus occluded |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

**Procedure**

1. Select the 1st edge/curve of the angle you want to measure
2. Select the 2nd edge/curve of the angle you want to measure

**Procedure**

1. Select the 1st location forming the angle you want to measure
2. Select the 2nd location forming the angle you want to measure
3. Select the 3rd location forming the angle you want to measure

---

## Assign Coordinate System (node 2730)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2730.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Assign Coord System - Auto mode**

1. Select the entities you want to assign
2. Select a coordinate system

**Assign Coord System - Manual mode**

1. Select the entities you want to assign
2. Click MMB
3. Select a coordinate system
4. Click MMB or apply

---

## Clearance Sensor (node 2234)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2234.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Clearance Sensor tool - Manual mode**

1. Select the Parts to create Clearance Sensors between.
2. Click MMB to complete selection.

**Clearance Sensor tool - Auto mode**

1. Select the Parts to create Clearance Sensors between.

---

## Coordinate System (node 2341)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2341.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT+MMB` | Transitions to previous selection stage |

**Euler angle Method - Manual mode**

1. Select the location to define origin of coordinate system
2. Click MMB

**Euler angle Method - Auto mode**

1. Select the location to define origin of coordinate system

**1-3 points Method - Manual mode**

1. Select the location to define origin of coordinate system
2. Click MMB
3. Select the location to define an axis of coordinate system
4. Click MMB
5. Select the location to define a plane of coordinate system
6. Click MMB or apply

**1-3 points Method - Manual mode**

1. Select the location to define origin of coordinate system
2. Select the location to define an axis of coordinate system
3. Select the location to define a plane of coordinate system

Tips:

- Euler angles are defined with 313 sequence, specify the angle in reference to the Global coordinate system
- Drag the translate Manipulator to change the Origin or drag the rotation Manipulator to change the orientation of coordinate system
- If want to complete the default orientation of the coordinate system in each selection stage, double click MMB

---

## Diameter (node 969)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/969.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Dismiss measured dimensions |
| `P` | Toggle visibility picking versus occluded |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

1. Select a circular or curved-like edge to measure its diameter

Tips:

- To multi select multiple circles, hold down CTRL key and select the circles, then to execute press MMB

---

## Distance (node 968)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/968.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Dismiss measured dimensions |
| `P` | Toggle visibility picking versus occluded |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

1. Select an entity as the starting point of your measurement
2. Select the second entity which is the end point of your measurement

Tips:

- To measure multiple entities at the same time, select the first entity to measure from, then window pick the other entities
- If you do multiple measurements in one shot, the Red measurement line means it is the largest length of the combination, Green means it is the smallest length, Orange is for the rest.

---

## Motion Envelope (node 2235)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2235.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Envelope Sensor tool - Manual mode**

1. Select the entities to create a Motion Envelope. Select MMB to complete selection.
2. Select the Primary Part to calculate the Motion Envelope relative to. Then click MMB to complete selection.

**Envelope Sensor tool - Auto mode**

1. Select the entities to create a Motion Envelope

---

## Point Sensor (node 2079)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2079.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Point Sensor tool - Manual mode**

1. Select the node or vertex you want to associate the Point Sensor with.
2. Click MMB.

**Point Sensor tool - Auto mode**

1. Select the node or vertex you want to associate the Point Sensor with.

**Point Sensor tool - Manual mode**

1. Select the node you want to associate the Point Sensor with.
2. Click MMB.

**Point Sensor tool - Auto mode**

1. Select the node you want to associate the Point Sensor with.

---

## Probe (node 2289)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2289.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Probe By Selection Method - Auto**

1. Select an entity (or entities) to display ID(s).

**Probe By Selection Method - Manual**

1. Select an entity (or entities).
2. Click the Apply button or MMB to display ID(s).

**Probe By ID Method**

1. Select entity type and enter ID(s) to search for.
2. Set the zoom setting.
3. Set isolate label setting.
4. Click the Apply button or MMB to display ID(s).

**Probe By ID Method**

1. Select entity type and enter ID(s) to search for.
2. Set the zoom setting.
3. Click the Apply button or MMB to display ID(s).

**Plot probe - Auto mode**

1. Select an entity (or entities) to display the plot value(s) and add to a data grid.

**Plot probe - Manual mode**

1. Select an entity (or entities) to display the plot value(s).
2. Click the Apply button or MMB to add the plot value(s) to a data grid.

**By Node method - Manual**

1. Select nodes, in order, to create a probe path.
2. Click MMB to create 1D probe.

Tips:

- Hover over an entity to display the plot value.

---

## Reference System (node 3054)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3054.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle Multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previously hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT+MMB` | Transitions to previous selection stage |

**User defined reference system​**

1. Select the entity to define location of the reference system, then click MMB.
2. Select the entity to define orientation of the reference system, then click MMB or Apply.

---

## Transform (node 966)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/966.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `T` | Switch to Translation mode, or cycle through selecting the axes |
| `R` | Switch to Rotation mode, or cycle through selecting the rings |
| `U` | Lock/Unlock the manipulator; unlock to relocate the manipulator on the selected body |
| `SPACEBAR` | Display tool property pop up panel |
| `ESC` | Abort operation |
| `P` | Toggle visibility picking versus occluded |
| `F` | Cycle through the axes |
| `S` | Change the axis sign (+/-) |

**Transform Method - Auto mode**

1. Select the body you want to transform
2. Drag a manipulator component to translate or rotate OR select a manipulator component

**Mirror Method - Manual mode**

1. Select the entities that you want to mirror
2. Click MMB
3. Select where you want to place your mirror plane
4. Click MMB
5. Using the Transform Manipulator, position and orient your mirror plane

**Step ii: Click MMB to execute the transformation**

1. Click MMB

**Transform manipulator UNLOCKED - Auto mode**

1. Select the body you want to transform
2. Select UNLOCK option from the tool property panel or tool property pop up panel
3. Drag a manipulator component to translate or rotate OR select a manipulator component

**Transform Method - Manual mode**

1. Select the body you want to transform, then MMB
2. Drag a manipulator component to translate or rotate OR select a manipulator component, then MMB.

**Transform manipulator UNLOCKED - Manual mode**

1. Select the body you want to transform, then MMB
2. Select UNLOCK option from the tool property panel or tool property pop up panel
3. Drag a manipulator component to translate or rotate, then MMB OR select a manipulator component

**Mirror Method - Auto mode**

1. Select the entities that you want to mirror
2. Select where you want to place your mirror plane
3. Using the Transform Manipulator, position and orient your mirror plane

**Step ii: Click MMB to execute the transformation**

1. Click MMB to execute mirror

Tips:

- If you want to Copy besides Transform, select the Copy option from the tool property panel or pop up by hovering over a manipulator component or pressing the Space key.
- If you selected a manipulator component (including the origin), to translate or rotate by input values,
- If you selected an axis to translate along the axis,
- If you selected the origin to translate it to a target location,
- If you selected the origin to translate along a vector
- If you double click on any manipulator component to translate from one point to another
- If you selected the origin to align
- If you selected a ring to rotate around the ring
- If you want to mirror copy instead of mirror move, select the copy option from the tool properties
- To keep copying double click the copy button
- To use the manipulator follow these steps:
- If you selected a manipulator component
- To cycle through the manipulator components for translation press T repeatedly
- To switch to rotation mode press R, to switch back to translation mode press T
- To cycle through the manipulator components for rotation press R repeatedly
- You can enter a value anytime the manipulator is settled and one of the components is selected
- If you selected a manipulator component (including the origin),
- If you selected the origin,
- If you selected a manipulator component as the upto source,
- If you want to mirror copy instead of mirror move, toggle ON the copy button from the tool properties

---

## X-Section Force Sensor (node 2169)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2169.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Cross Section Sensor tool - Manual mode**

1. Select entities you want to create Cross Section Sensor for.
2. Click MMB.
3. Select face/edge/vertex/node that you want to locate cutting plane.
4. Click MMB to complete the creation.

**Cross Section Sensor tool - Auto mode**

1. Select entities you want to create Cross Section Sensor for.
2. Select face/edge/vertex/node that you want to locate cutting plane.

**Cross Section Sensor Array tool**

1. Select entities you want to create Cross Section Sensor for.
2. Click MMB.
3. LMB click either Array End-Point glyph to to re-location, re-size, and re-orient the Array.
4. Click MMB to complete the creation.
