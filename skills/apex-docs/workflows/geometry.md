# Geometry — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [2 Point Rectangle](#2-point-rectangle-node-983)
- [3 Point Arc](#3-point-arc-node-990)
- [3 Point Circle](#3-point-circle-node-986)
- [3 Point Rectangle](#3-point-rectangle-node-984)
- [Auto Offset](#auto-offset-node-1494)
- [Boolean](#boolean-node-1509)
- [Box](#box-node-2493)
- [Center Arc](#center-arc-node-989)
- [Center Circle](#center-circle-node-985)
- [Chamfer](#chamfer-node-994)
- [Constant Thickness](#constant-thickness-node-1056)
- [Curves](#curves-node-951)
- [Cylinder](#cylinder-node-2507)
- [Datum Plane](#datum-plane-node-3023)
- [Defeature](#defeature-node-924)
- [Distance Offset](#distance-offset-node-1057)
- [Edit Sketch](#edit-sketch-node-999)
- [Ellipse](#ellipse-node-991)
- [Ellipsoid](#ellipsoid-node-2509)
- [Facet to NURBS](#facet-to-nurbs-node-2585)
- [Filler](#filler-node-949)
- [Fillet](#fillet-node-993)
- [Geometry Body Property](#geometry-body-property-node-3018)
- [Geometry Cleanup](#geometry-cleanup-node-1079)
- [Geometry From Mesh](#geometry-from-mesh-node-2342)
- [Incremental Midsurface](#incremental-midsurface-node-1273)
- [Point](#point-node-995)
- [Point Create](#point-create-node-952)
- [Polyline](#polyline-node-987)
- [Project Sketch](#project-sketch-node-998)
- [Push/Pull](#push-pull-node-906)
- [Revolve/Sweep](#revolve-sweep-node-2339)
- [Sphere](#sphere-node-2508)
- [Spline](#spline-node-988)
- [Split](#split-node-997)
- [Split Curves](#split-curves-node-948)
- [Split Surfaces](#split-surfaces-node-947)
- [Split Tool](#split-tool-node-1510)
- [Stitch Geometry](#stitch-geometry-node-946)
- [Suppress/Unsuppress](#suppress-unsuppress-node-945)
- [Surface Extend](#surface-extend-node-1088)
- [Surface Loft](#surface-loft-node-2382)
- [Taper Midsurface Creation](#taper-midsurface-creation-node-1275)
- [Trim](#trim-node-996)
- [Vertex Add/Remove](#vertex-add-remove-node-950)
- [Vertex Edge Drag](#vertex-edge-drag-node-944)

---

## 2 Point Rectangle (node 983)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/983.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**2 Point Rectangle**

1. Click once to define the 1st vertex of the rectangle
2. Move cursor then click again to define the 2nd vertex of the rectangle and hence complete the creation of the rectangle

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit lengths of the rectangle edges

---

## 3 Point Arc (node 990)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/990.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**3 Point Arc**

1. Click once to define one end of the arc
2. Move cursor then click a 2nd time to define the other end of the arc
3. Move cursor then click a final 3rd click to define the location of the point on the circumference of the arc

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit the circumference and radius of the arc

---

## 3 Point Circle (node 986)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/986.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**3 Point Circle**

1. Click to define the 1st circumference point of the circle
2. Move cursor then click again to define the 2nd circumference point of the circle
3. Move cursor then click again to complete the circle

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension box to edit the radius of the circle

---

## 3 Point Rectangle (node 984)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/984.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**3 Point Rectangle**

1. Click once to define the 1st vertex of the rectangle
2. Move cursor then click again to define the 2nd vertex of the rectangle
3. Move cursor then click a 3rd time to complete the rectangle

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit lengths of the rectangle edges

---

## Auto Offset (node 1494)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1494.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Dismiss midsurface manipulator |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |

**Semi-Auto Offset - Auto mode**

1. Select solid face(s) to create offset
2. Click either balls of the manipulator to offset to those preset locations
3. Just type in a value into the dimension box and press ENTER
4. Drag, the far end of the manipulator, the one that is located opposite from the originating face, to any other vertex, node or a location on any edge in order to modify the offset location

**Semi-Auto Offset - Manual mode**

1. Select solid face(s) to create offset
2. Click MMB to create the offset surface(s)
3. Click either balls of the manipulator to offset to those preset locations
4. Just type in a value into the dimension box and press ENTER
5. Drag, the far end of the manipulator, the one that is located opposite from the originating face, to any other vertex, node or a location on any edge in order to modify the offset location

**Semi-Auto Offset - Upto Alignment - Auto mode**

1. Select the surface you want to move
2. Select a vertex, node, marker, edge or face you want to align to

**Semi-Auto Offset - Upto Alignment - Manual mode**

1. Select the surface you want to move
2. Select a vertex, node, marker, edge or face you want to align to
3. Click MMB to complete alignment

**Semi-Auto Offset - Auto mode**

1. Select solid face(s) to create offset from
2. Click either balls of the manipulator to offset to those preset locations
3. Just type in a value into the dimension box and press ENTER
4. Drag, the far end of the manipulator, the one that is located opposite from the originating face, to any other vertex, node or a location on any edge in order to modify the offset location

**Semi-Auto Offset - Manual mode**

1. Select solid face(s) to create offset from
2. Click MMB to create the offset surface(s)
3. Click either balls of the manipulator to offset to those preset locations
4. Just type in a value into the dimension box and press ENTER
5. Drag, the far end of the manipulator, the one that is located opposite from the originating face, to any other vertex, node or a location on any edge in order to modify the offset location

Tips:

- If you want to move the offset to preset locations
- If you want to enter your own offset distance value
- If you want to manually manipulate based on particular locations on the screen
- You can click the 'half/full' toggle button to switch between half or the full manipulator length
- You can click the 'half/full' toggle button to switch between half or the full offset length

---

## Boolean (node 1509)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1509.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Merge method - Auto mode**

1. Select bodies you want to merge

**Merge method - Manual mode**

1. Select bodies you want to merge
2. Click MMB

**Subtraction method - Auto mode**

1. Select the bodies you want to subtract other bodies from
2. Select the bodies you want to subtract from your target

**Subtraction method - Manual mode**

1. Select the bodies you want to subtract other bodies from
2. Click MMB
3. Select the bodies you want to subtract from your target
4. Click MMB

**Intersection method - Auto mode**

1. Select the bodies you want to generate the intersection from

**Intersection method - Manual mode**

1. Select the bodies you want to generate the intersection from
2. Click MMB

**Merge method - Auto mode**

1. Select cells within one solid to merge

**Merge method - Manual mode**

1. Select cells within one solid to merge
2. Click MMB

Tips:

- To multi select multiple entities simply hold down the SHIFT or the CTRL key, then select the entities you want, then release the SHIFT or CTRL or window pick to multi select them

---

## Box (node 2493)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2493.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `R` | Change manipulator to Rotation mode |
| `T` | Change manipulator to Translate mode |
| `SHIFT+MMB` | Transitions to previous selection stage |

**Box Primitive with External Coordinate System**

1. Select Coordinate(s) to place the Box(es).
2. Click MMB or Apply button to create the Box.

**Box Primitive Integrated**

1. Select a location to place the Box.
2. Use the manipulator as needed to orient the box.
3. Click MMB or Apply button to create the Box.

**Box Primitive - Manual mode**

1. Select the entity to define the Box Primitive origin location and click MMB.
2. Select an entity or existing coordinate system or specify Euler angle to define the Box Primitive orientation, then click MMB to complete or click MMB to complete directly.

**Box Primitive - Auto mode**

1. Select the entity to define the Box Primitive origin location.

Tips:

- You can click MMB to complete in stage2 without defining orientation, the system will align the orientation to the entities in Stage1.
- Once you select the entities in the stage 1, the stage 2 will be skipped and the Box Primitive will be created with an orientation automatically, this orientation will align to the entities in Stage1. Switch to manual mode to sequentially execute all stages.

---

## Center Arc (node 989)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/989.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort drawing midway |

**Center Point Arc**

1. Click once to define the center of the arc
2. Move cursor then click again to define the 1st endpoint of arc
3. Move cursor then click one last time to define the 2nd endpoint of the arc

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit the circumference or radius of the arc

---

## Center Circle (node 985)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/985.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**Center Circle**

1. Click once to create the circle center
2. Move cursor then click again to complete the creation of the circle

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension box to edit the radius of the circle

---

## Chamfer (node 994)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/994.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**Chamfer**

1. Select two adjacent lines, OR, select a corner vertex
2. Move the cursor and adjust the chamfer to preview the chamfer
3. Click one last time to finalize the chamfer

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension box to edit the length of the chamfer

---

## Constant Thickness (node 1056)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1056.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |

**Constant thickness Offset - Auto Mode**

1. Select the solid body(ies) to create offsets from

**Constant thickness Offset - Manual Mode**

1. Select the solid body(ies) to create offsets from
2. Click MMB to create the offset

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key

---

## Curves (node 951)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/951.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SHIFT` | Modify spline to polyline |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |
| `CTRL` | Toggle multi select |
| `CTRL + SHIFT` | Pure deselection |

**Procedure**

1. Click on multiple geometry entities or nodes or markers to define curve
2. Double click or MMB to complete the curve creation

**Curve Offset - Automatic**

1. select edge to offset

**Edge Offset - Manual(Default)**

1. Select the edges of a surface or solid to offset, then click MMB

**Edge Offset - Automatic**

1. Select the edges of a surface or solid to offset

**Curve Intersect - Manual Mode**

1. Select faces or planes to intersect, then click MMB
2. Select faces or planes to intersect with, then click MMB to create the curves

**Curve Intersect - Auto Mode**

1. Select faces or planes to intersect
2. Select faces or planes to intersect with

**Procedure**

1. Select three locations to define an Arc or Circle

**Extract Curves - Manual**

1. Select curve, surface or solid edges to create curves from, then click MMB

**Extract Curves - Automatic**

1. Select curve, surface or solid edges to create curves from

**Project - Manual mode - Normal Projection ( Default )**

1. Select edges to project, then Click MMB
2. Select faces or planes to project onto. Click MMB to perform the projection

**Project - Auto mode - Normal Projection**

1. Select edges to project
2. Select faces or planes to project onto

**Project - Manual mode - Vector Projection**

1. Select edges to project, then Click MMB
2. Select faces or planes to project onto. Click MMB
3. Select location(s) to define projection vector, then adjust manipulator as desired. Click MMB to perform the projection

**Project - Auto mode - Vector Projection**

1. Select edges to project
2. Select faces or planes to project onto
3. Select two location(s) to define projection vector

**Curve Offset - Manual(Default)**

1. select edges to offset, then click MMB

Tips:

- To modify the spline to a polyline while drawing, hold down SHIFT key while drawing
- When connected touching edges are offset together, they will form one curve with multiple edges
- Input edges must be close to coplanar, or the offset could fail
- The offset must remain inside the body, and not overlap non-manifolded parts of the body (where 3 or more faces share an edge)
- To intersect every face with every face, the full set in both lists

---

## Cylinder (node 2507)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2507.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `CTRL` | Toggle Multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previously hidden faces |
| `R` | Change manipulator to rotation mode |
| `T` | Change manipulator to translation mode |
| `SHIFT + H` | Display previous hidden faces |
| `SHIFT+MMB` | Transitions to previous selection stage |

**Cylinder Primitive with External Coordinate System**

1. Select Coordinate(s) to place the Cylinder(s)
2. Click MMB or Apply button to create the Cylinder

**Cylinder Primitive Integrated**

1. Select a location to place the Cylinder
2. Use the manipulator as needed to orient the Cylinder
3. Click MMB or Apply button to create the Cylinder

**Cylinder Primitive - Manual mode**

1. Select the entity to define the Cylinder Primitive origin location and click MMB.
2. Select an entity or existing coordinate system or specify Euler angle to define the Cylinder Primitive orientation, then click MMB to complete or click MMB to complete directly.

**Cylinder Primitive - Auto mode**

1. Select the entity to define the Cylinder Primitive origin location.

Tips:

- Use the T and R keys to change the manipulator between translate and rotate modes.
- You can click MMB to complete in stage2 without defining orientation, the system will align the orientation to the entities in Stage1.
- Once you select the entities in the stage 1, the stage 2 will be skipped and the Cylinder Primitive will be created with an orientation automatically, this orientation will align to the entities in Stage1. Switch to manual mode to sequentially execute all stages.

---

## Datum Plane (node 3023)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3023.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `R` | Change transform manipulator as rotate mode when defining plane |
| `T` | Change transform manipulator as move mode when defining plane |

**Define Plane by 3 points - Manual mode**

1. Select 1 to 3 locations to define a plane
2. Optionally adjust the plane location using the Manipulator
3. Click MMB to define the plane

**Define Plane by 3 points - Auto mode**

1. Select 1 to 3 locations to define a plane

**Define Plane by Geometry - Manual mode**

1. Select the location on geometry that defines the desired plane
2. Optionally adjust the plane location
3. Click MMB to define the plane

**Define Plane by Geometry - Auto mode**

1. Select the location on geometry that defines the desired plane

**Define Plane by Coordinate System - Manual mode**

1. Specify which axis will be normal to the Plane
2. Select a coordinate system
3. Optionally adjust the plane location using the Manipulator
4. Click MMB to define the plane

**Define Plane by Coordinate System - Auto mode**

1. Specify which axis will be normal to the Plane
2. Select a coordinate system

Tips:

- To select multiple locations in Auto mode, hold down the SHIFT or the CTRL key, then select the locations you want, then release the SHIFT or CTRL

---

## Defeature (node 924)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/924.html

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
| `ALT+Double Click` | Auto-extend picked target list |

**Defeature Automatically - Auto**

1. Select a feature, a face or an edge

**Defeature using user defined features - Manual**

1. Select edges to define the feature
2. Click MMB
3. Select the faces that you want those newly defined features removed from
4. Click MMB
5. Deselect the features that you want to keep
6. Click MMB

**Defeature Editing Detected Faces - Manual**

1. Select a face / edge of a feature to remove.
2. Select faces/edges to Add or remove to properly define the entire feature, then MMB to remove.

**Defeature By Select Entire Feature Manually - Auto**

1. Select all faces of one or more features.

**Defeature By Select Entire Feature Manually - Manual**

1. Select all faces of one or more features, then MMB to defeature.

**Defeature Automatically - Manual**

1. Select a feature, a face or an edge
2. Click MMB to remove feature(s)

**Defeature Explicitly - Auto**

1. Select a feature, a face or an edge

**Defeature Explicitly - Manual**

1. Select a feature, a face or an edge
2. Click MMB to remove feature(s)

**Defeature by Automatically Detecting Entire Feature - Auto**

1. Select a face / edge of one or more features.

**Defeature by Automatically Detecting Entire Feature - Manual**

1. Select a face/edge of one or more features, then click MMB to defeature.

**DeFeature By Identified Feature - Auto**

1. Select body or bodies to start identifying features
2. Select the feature type from the list
3. Define the different ranges of features by clicking slightly right or left to the range
4. Select entities in viewport or LMB click on the range slider

**DeFeature By Identified Feature - Manual**

1. Select the body or bodies to start identifying features
2. Click MMB to transition to selecting feature types and their ranges
3. Select the feature type from the list
4. Define the different ranges of features by clicking slightly right or left to the range
5. Select entities in viewport or LMB click on the range slider
6. MMB click in the viewport to remove the highlight feature

**Defeature using user defined features - Auto**

1. Select edges to define the feature
2. Select the faces that you want those newly defined features removed from

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key
- Added faces/edges must be connected to the existing selected faces/edges.
- Use Exclusive Picking on the pick filter to aide in box picking small features with many faces, such as logos and lettering.
- To multi-select, just continue to click on the entities, they will accumulate
- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key. Be aware that only connected features should be selected in Explicit mode.
- To multi-select, just continue to click on the entities, they will accumulate. Be aware that only connected features should be selected in Explicit mode.
- You can click in the max range dimension box to lower it if you want to narrow the range
- If you want to defeature these features ...

---

## Distance Offset (node 1057)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1057.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |

**Distance Offset - Auto mode**

1. Define the distance you want to offset the face
2. Select solid face(s) to create the offset from

**Distance Offset - Manual mode**

1. Define the distance you want to offset the face
2. Select solid face(s) to create the offset from
3. Click MMB to create the offset

Tips:

- If you want to offset to half that distance then check the '1/2 Offset' check box
- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key
- If you want to offset to half that distance then check the half check box
- The '1/2 Offset' check box is checked, the offset will half the distance the edit box shows

---

## Edit Sketch (node 999)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/999.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `F` | Brings grid parallel to screen |

**Edit sketch**

1. Select the sketch you want to edit
2. Enter a new dimension value into the dimension box

Tips:

- Pressing F will bring the sketch grid parallel to the screen

---

## Ellipse (node 991)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/991.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort drawing midway |

**Ellipse**

1. Click once to define the center of ellipse
2. Move cursor then click again to define the 1st axis's radius
3. Move cursor then click a final 3rd time to define the 2nd axis's radius

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit the length of the ellipse axes

---

## Ellipsoid (node 2509)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2509.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `CTRL` | Toggle Multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previously hidden faces |
| `R` | Change manipulator to rotation mode |
| `T` | Change manipulator to translation mode |
| `SHIFT + H` | Display previous hidden faces |
| `SHIFT+MMB` | Transitions to previous selection stage |

**Ellipsoid Primitive with External Coordinate System**

1. Select Coordinate(s) to place the Ellipsoid(s)
2. Click MMB or Apply button to create the Ellipsoid

**Ellipsoid Primitive Integrated**

1. Select a location to place the Ellipsoid
2. Use the manipulator as needed to orient the Ellipsoid
3. Click MMB or Apply button to create the Ellipsoid

**Ellipsoid Primitive - Manual mode**

1. Select the entity to define the Ellipsoid Primitive origin location and click MMB.
2. Select an entity or existing coordinate system or specify Euler angle to define the Ellipsoid Primitive orientation, then click MMB to complete or click MMB to complete directly.

**Ellipsoid Primitive - Auto mode**

1. Select the entity to define the Ellipsoid Primitive origin location.

Tips:

- Use the T and R keys to change the manipulator between translate and rotate modes.
- You can click MMB to complete in stage2 without defining orientation, the system will align the orientation to the entities in Stage1.
- Once you select the entities in the stage 1, the stage 2 will be skipped and the Ellipsoid Primitive will be created with an orientation automatically, this orientation will align to the entities in Stage1. Switch to manual mode to sequentially execute all stages.

---

## Facet to NURBS (node 2585)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2585.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `P` | Toggle visibility picking vs. occluded |

**Create NURBS Geometry from STL faceted body - Manual Mode**

1. Select a faceted body
2. Click MMB to preview identified faces
3. Select green checkbox to generate NURBS

**Create NURBS Geometry from STL faceted body - Automatic Mode**

1. Select facet body, then MMB to create NURBS faces

Tips:

- If NURBS fail to create, try reducing the Tessellation Size or increase NURBS Face Density.
- Increasing NURBS Face Density increases the number of faces, but also reduces their complexity.

---

## Filler (node 949)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/949.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |

**Surface Fill/Create - Auto**

1. Select vertices, nodes, markers or edges

**Surface Fill/Create - Manual**

1. Select vertices, nodes, markers or edges
2. Click MMB to create surface

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key
- If you click at least one edge it will try to fill the surface immediately

---

## Fillet (node 993)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/993.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**Fillet**

1. Select two adjacent lines, OR, select a corner vertex
2. Move the cursor and adjust the fillet to preview the fillet
3. Click one last time to finalize the fillet

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension box to edit the radius of the fillet

---

## Geometry Body Property (node 3018)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3018.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**User Defined Reference System**

1. Select a coordinate system
2. Click MMB or Apply

---

## Geometry Cleanup (node 1079)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1079.html

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

**Geometry Simplify - Auto**

1. Set the desired Simplify options and tolerances
2. Select solid bodies or sheet bodies or general bodies or faces or edges

**Geometry Simplify - Manual**

1. Set the desired Simplify options and tolerances
2. Select solid bodies or sheet bodies or general bodies or faces or edges
3. Click MMB to perform the operations

**Find & Fix Small Features with Auto Fix Checked off - Auto**

1. Select the types want to find and fix
2. Select solid bodies or sheet bodies
3. Select small features on model browser
4. Click Auto Fix button to fix the small features selected

**Geometry Find & Fix Small Features with Auto Fix Checked on - Auto**

1. Select the types want to find and fix
2. Checked on the Auto Fix option
3. Select solid bodies or sheet bodies

**Find & Fix Small Features with Auto Fix Checked off - Manual**

1. Select the types want to find and fix
2. Select solid bodies or sheet bodies
3. Click MMB to find small features
4. Select small features on model browser
5. Click Auto Fix button to fix the small features selected

**Geometry Find & Fix Small Features with Auto Fix Checked on - Manual**

1. Select the types want to find and fix
2. Checked on the Auto Fix option
3. Select solid bodies or sheet bodies
4. Click MMB to find and fix small features

**Find & Fix Small Surface/Wire Body Features with Auto Fix Checked off - Auto**

1. Set the desired options and tolerances
2. Select solid bodies, sheet bodies, wire bodies, or general bodies to find small surface/wire body features
3. Select small surface/wire body features on model browser
4. Click Auto Fix button to fix the small surface/wire body features selected

**Find & Fix Small Surface/Wire Body Features with Auto Fix Checked on - Auto**

1. Set the desired options and tolerances
2. Checked on the Auto Fix option
3. Select solid bodies, sheet bodies, wire bodies, or general bodies to find and fix small surface/wire body features

**Find & Fix Small Surface/Wire Body Features with Auto Fix Checked off - Manual**

1. Set the desired options and tolerances
2. Select solid bodies, sheet bodies, wire bodies or general bodies
3. Click MMB to find small surface/wire body features
4. Select small surface/wire body features on model browser
5. Click Auto Fix button to fix the small surface/wire body features selected

**Find & Fix Small Surface/Wire Body Features with Auto Fix Checked on - Manual**

1. Set the desired options and tolerances
2. Checked on the Auto Fix option
3. Select solid bodies, sheet bodies, wire bodies, or general bodies
4. Click MMB to find and fix small surface/wire body features

**Find geometry faults - Auto**

1. Select solid bodies or sheet bodies or general bodies to find geometry fault

**Find geometry faults - Manual**

1. Select solid bodies or sheet bodies or general bodies
2. Click MMB to find geometry fault

---

## Geometry From Mesh (node 2342)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2342.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `P` | Toggle visibility picking vs. occluded |

**Create Topology - Manual mode**

1. Select one or more orphan mesh body to convert to geometry or one body already associated to facet body to make topology changes.
2. Click MMB to preview identified topology and make edits.

**Add/Remove Edges/Vertex - Manual mode**

1. Select Identified edges/vertex to remove, and then MMB to apply changes.
2. Select element edges or nodes to add in missing topology, and then click on MMB to apply changes.

**Merge Faces - Manual mode**

1. Select adjacent faces to merge, and then click MMB to apply changes.

**Create Faceted Bodies - Automatic mode**

1. Select one or more mesh bodies to convert to geometry.

**Add/Remove Edge/Vertex - Automatic mode**

1. Select Identified edges/vertices to remove.
2. Select element edges or nodes to add in missing topology.

**Merge Faces - Automatic mode**

1. Select adjacent faces to merge.

**Create NURBS Geometry and Faceted Body - Manual mode**

1. Click MMB or Apply check box to generate faceted body and also NURBS geometry

**Create NURBS Geometry and Faceted Body - Automatic mode**

1. Click MMB or Apply check box to generate faceted body and also NURBS geometry

Tips:

- If multiple bodies are selected, they cannot be both associated to geometry and orphan mesh.
- If the selected mesh body is already associated with faceted geometry, all mesh associations with the original geometry will be deleted and assigned to the new faceted geometry. All model attribute associations, such as materials and loads or boundary conditions will be lost.
- Adjust Level Of Detail slider until surface subdivisions are split up as much or slightly more than needed before beginning topology editing in the next stage. The changes are viewed as topology preview in the edit stage.
- Make sure the initial geometry subdivisions are split up as much or slightly more than needed. Go back to stage 1 and adjust Level Of Detail as needed to achieve this before manual editing.
- Use the add/remove/toggle behavior settings to remove or add many at one time with box picking, or keep it in toggle mode for individual changes.
- To get exportable geometry, turn on "Create Both faceted and NURBS Geom." Tip 2: For successful NURBS extraction, faces must be broken up to simple faces. Tip 3: If NURBS are not correctly generated for some faces, hit undo, and try again after breaking these into smaller faces. Cylinders, Cones or circular fillets may need to be broken up into 180 or 90 degree faces in some cases. Tip 4: Faces are color coded by detected face types: Red- Cylinder, Blue - Planar, Purple - Torus, Yellow - Cone, Green - Sphere, Gray - None
- To get exportable geometry, turn on "Create Both faceted and NURBS Geom." Tip 2: For successful NURBS extraction, faces must be broken up to simple faces. Tip 3: If NURBS are not correctly generated for some faces, hit undo, and try again after breaking these into smaller faces. Cylinders, Cones or circular fillets may need to be broken up into 180 or 90 degree faces in some cases.

---

## Incremental Midsurface (node 1273)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1273.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `P` | Toggle visibility picking versus occluded |
| `SPACEBAR` | Pop up offset type choices |
| `ESC` | Exit Preview mode or Abort operation midway |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |

**Incremental mid-surface(extract pairs) using - Auto mode**

1. Select a solid body in order to automatically identify the face pair groups

**Change midsurface offset type - Manual mode**

1. Select face pairs whose offset type you want to modify
2. Select the offset type that you wish to define for those selected face pairs
3. Click MMB to modify the offset type for those pairs

**Extract face pairs from solid - Manual mode**

1. Select the solid body whose face pairs you want to extract & display
2. Click MMB to perform the extraction

**Incremental mid-surface(merge pairs) using - Auto mode**

1. Select the face pair groups in order to automatically merge the face pair groups

**Merge face pairs - Manual mode**

1. Select the face pairs that you want to merge
2. Click MMB to perform the merge

**Incremental mid-surface(edit pairs) using - Auto mode**

1. Select face pair to automatically edit
2. Select faces to add or remove from A side
3. Select faces to add or remove from B side

**Incremental mid-surface(create pairs) using - Auto mode**

1. Select non face pair to automatically create
2. Select faces to add or remove from B side

**Edit face pairs - Manual mode**

1. Select your face pair
2. Click MMB to edit the pair
3. Select faces to add or remove from this side
4. Click MMB
5. Select faces to add or remove from this side
6. Click MMB to finalize the pair

**Incremental mid-surface(Extract Midsurface) using - Auto mode**

1. Select the face pair groups in order to automatically create midsurface

**Extract midsurfaces - Manual mode**

1. Select face pairs

**Step 2 (optional): Click preview to preview your midsurface**

1. Click MMB to extract the midsurface(s) from the pairs you selected

**Incremental mid-surface(Define Offset Type) using - Auto mode**

1. Select the face pair groups in order to automatically modify offset type

Tips:

- If you want to indentify the other solid body, you will only select the body
- If you hover over a face pair and press the SPACEBAR, it will launch a pop up to alter the offset type for that pair. To see a preview of the midsurface, you can toggle on/off the preview button on the pop up.
- Warning! - After the face pairs have been extracted & displayed, selecting another solid and clicking MMB will clear all the face pairs of what was extracted for the previous solid and extract and display the face pairs of the new solid you selected
- If you want to go back to (de/re)selecting faces, hold SHIFT + click MMB and it will put you back in the previous selection stage. Then this will put you back in step 3.
- If you switch the show/hide pairs to HIDE mode, then it will HIDE all used face pairs that were used in any midsurface creation in this method, and everytime you extract a new midsurface, it will hide the faces of the pairs that were used in that creation. If you switch the show/hide pairs to SHOW then it will display all the face pairs used or otherwise, and as long as the setting is on SHOW the next time you extract a midsurface we will leave the face pairs visible.

---

## Point (node 995)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/995.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**Point**

1. Click anywhere to create a point

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit the location of the point

---

## Point Create (node 952)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/952.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

**By point & click**

1. Click on any geometry entity, node or marker to create a point

**By Intersecting curves - Auto**

1. Select curve(s) or edge(s)
2. Select the intesecting curve(s) or edge(s) to create point at their intersection

**By Intersecting curves - Manual**

1. Select curve(s) or edge(s)
2. Click MMB to transition to selecting intersecting curve(s) or edge(s)
3. Select curve(s) or edge(s) that intersect with the other curves(s) or edge(s) to create point at their intersection
4. Click MMB to create intersecting point(s)

**By Intersecting curves & surfaces - Auto**

1. Select curve(s) or edge(s)
2. Select the face(s) / plane(s) that intersect with the curve(s) or edge(s) to create a point at their intersection

**By Intersecting curves & surfaces - Manual**

1. Select curve(s) or edge(s)
2. Click MMB to transition to selecting faces as tools to split with
3. Select the face(s) / plane(s) that intersect with the curve(s) or edge(s) to create point at their intersection
4. Click MMB to create intersecting point(s)

**By Entering Coordinates**

1. Define your X,Y,Z coordinates in the tool properties panel
2. Click apply button to create the point

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key

---

## Polyline (node 987)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/987.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**Polyline**

1. Click consecutively to create a polyline
2. To end the polyline double click or click MMB

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- You can click into the dimension boxes to edit the length of one segment of the polyline

---

## Project Sketch (node 998)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/998.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `F` | Brings grid parallel to screen |
| `ESC` | Abort selections |

**Sketch project**

1. Select a face or an edge or a vertex or a node, in order to project the edges of the face or the edge of the edge or the vertex or the node onto the sketch plane/grid.

Tips:

- Pressing F will bring the sketch grid parallel to the screen

---

## Push/Pull (node 906)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/906.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `X` | Cut through solids in one shot |
| `Z/C` | Enlarge / shrink snap box |
| `F` | Cycle through the methods |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |

**Normal method**

1. Drag face(s) OR Select either face(s) or solid edge(s)
2. Drag face or drag on canvas
3. Drag OR select then drag one of the 2 double arrow manipulators

**Normal method with upto**

1. Drag face(s) to a target face OR Select face(s)
2. Select the upto target face

**Fillet method**

1. Drag solid edge or existing fillet OR select solid edge first or existing fillet then drag on canvas

**Fillet method with upto**

1. Drag existing fillet to a target fillet OR Select fillet without dragging
2. Select the upto target fillet

**Chamfer method**

1. Drag solid edge or existing chamfer OR select solid edge first or existing chamfer then drag on canvas

**Chamfer method with upto**

1. Drag existing chamfer to a target chamfer OR select chamfer
2. Select the upto target face

Tips:

- If you selected face(s)
- If you selected solid edge(s)
- If you hold the Alt key while dragging you can snap to a target face
- You can enter a value into the dimension box when you have the manipulator in a settled state
- If you selected the face of a single surface you can press "X" and it will automatically cut through the solid bodies
- If you are dragging and you move cursor to a target face you can snap upto that target face
- If you selected fillet(s)
- If you are dragging and you move cursor to target face you can snap upto that target face
- If you selected chamfer(s)

---

## Revolve/Sweep (node 2339)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2339.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL + SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Set the angle and optional offset then**

1. Select points, curves, or faces to revolve
2. Select location(s) to define axis of revolution

**Set the angle and optional offset then**

1. Select points, curves, or faces to revolve, then click MMB
2. Select location(s) to define axis of revolution, then adjust manipulator as desired. Click MMB to perform the revolve

**Set the extrude distance and optional offset then**

1. Select points, curves, or faces to extrude
2. Select location(s) to define extrude vector

**Set the extrude distance and optional offset then**

1. Select points, curves, or faces to extrude, then click MMB
2. Select location(s) to define extrude vector, then adjust manipulator as desired. Click MMB to perform the extrude.

**Sweep - Auto mode**

1. Select curves or faces to sweep
2. Select contiguous curves or a curve body to define the sweep path

**Sweep - Manual mode**

1. Select curves or faces to sweep, then click MMB
2. Select contiguous curves or a curve body to define the sweep path, then click MMB to perform the sweep operation.

Tips:

- To multi select, hold down the SHIFT or the CTRL key and when finished release the key

---

## Sphere (node 2508)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2508.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `CTRL` | Toggle Multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previously hidden faces |
| `R` | Change manipulator to rotation mode |
| `T` | Change manipulator to translation mode |
| `SHIFT + H` | Display previous hidden faces |
| `SHIFT+MMB` | Transitions to previous selection stage |

**Sphere Primitive with External Coordinate System**

1. Select Coordinate(s) to place the Sphere(s)
2. Click MMB or Apply button to create the Sphere

**Sphere Primitive Integrated**

1. Select a location to place the Sphere
2. Use the manipulator as needed to orient the Sphere
3. Click MMB or Apply button to create the Sphere

**Sphere Primitive - Manual mode**

1. Select the entity to define the Sphere Primitive origin location and click MMB.
2. Select an entity or existing coordinate system or specify Euler angle to define the Sphere Primitive orientation, then click MMB to complete or click MMB to complete directly.

**Sphere Primitive - Auto mode**

1. Select the entity to define the Sphere Primitive origin location.

Tips:

- Use the T and R keys to change the manipulator between translate and rotate modes.
- You can click MMB to complete in stage2 without defining orientation, the system will align the orientation to the entities in Stage1.
- Once you select the entities in the stage 1, the stage 2 will be skipped and the Sphere Primitive will be created with an orientation automatically, this orientation will align to the entities in Stage1. Switch to manual mode to sequentially execute all stages.

---

## Spline (node 988)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/988.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `Z/C` | Enlarge / shrink snap box |
| `SHIFT` | Force spline to a polyline |
| `F` | Brings grid parallel to screen |
| `ESC` | Abort operation midway |

**Spline**

1. Click consecutively to create a spline
2. To end the spline double click or click MMB

Tips:

- Pressing F will bring the sketch grid parallel to the screen
- Holding down on the SHIFT key while drawing the spline will turn it into a polyline

---

## Split (node 997)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/997.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `F` | Brings grid parallel to screen |
| `ESC` | Aborts selection |

**Split sketch**

1. Select a sketched line
2. Select either an intersecting sketched line OR click somewhere on the same line to split it at that point

Tips:

- Pressing F will bring the sketch grid parallel to the screen

---

## Split Curves (node 948)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/948.html

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
| `ALT+Double Click` | Auto-extend picked target list |

**Split with Curve(s) - Auto**

1. Select curve(s) to split
2. Select curves to split other curve(s) with

**Split with Point(s) - Manual**

1. Select curve(s) you want to split
2. Click MMB to transition to pick point
3. Click anywhere on the curve to split at that point
4. Click MMB to perform the split
5. Select curve(s) you want to delete
6. Click MMB to delete the curve(s)

**Split with Face(s) - Auto**

1. Select curve(s) to split
2. Select face(s) / plane(s) to split curve(s) with
3. Select curve(s) to delete

**Split with Face(s) - Manual**

1. Select curve(s) you want to split
2. Click MMB to transition to selecting faces to split with
3. Select face(s) / plane(s) to split curve(s) with
4. Click MMB to perform the split
5. Select curve(s) you want to delete
6. Click MMB to delete the curve(s)

**Split with Curve(s) - Manual**

1. Select curve(s) you want to split
2. Click MMB to transition to selecting other curves to split with
3. Select curves to split other curve(s) with
4. Click MMB to perform the split

**Split with Point(s) - Auto**

1. Select curve(s) to split
2. Pick vertices or nodes to split the curves

**Split with Point(s) - Manual**

1. Select curve(s) you want to split
2. Click MMB to transition to pick point
3. Pick vertices or nodes, then click MMB to split the curves

**Split with Face(s) - Auto**

1. Select curve(s) to split
2. Select face(s) / plane(s) to split curve(s) with

**Split with Face(s) - Manual**

1. Select curve(s) you want to split
2. Click MMB to transition to selecting faces to split with
3. Select face(s) / plane(s) to split curve(s) with
4. Click MMB to perform the split

**Split with Curve(s) - Auto**

1. Select curve(s) to split
2. Select curves to split other curve(s) with
3. Select curve(s) to delete

**Split with Curve(s) - Manual**

1. Select curve(s) you want to split
2. Click MMB to transition to selecting other curves to split with
3. Select curves to split other curve(s) with
4. Click MMB to perform the split
5. Select curve(s) you want to delete
6. Click MMB to delete the curve(s)

**Split with Point(s) - Auto**

1. Select curve(s) to split
2. Click anywhere on the curve to split at that point
3. Select curve(s) to delete

Tips:

- To multi-select, hold down CTRL or SHIFT key, & when finished, release the key
- If you want to go back to (de)selecting curves, hold SHIFT then click MMB then deselect the surfaces, then proceed as you would from step 1
- If you want to go back to (de)selecting faces, hold SHIFT then click MMB then deselect the surfaces, then proceed as you would from step 1
- If both selection stages have inputs and you want to advance directly from step 1 double click MMB
- If you want to go back to (de)selecting curve(s), hold SHIFT then click MMB then (de)select the curve(s), then proceed as you would from step 1

---

## Split Surfaces (node 947)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/947.html

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
| `ALT+Double Click` | Auto-extend picked target list |

**Split with Curve(s) - Auto**

1. Select face(s) to split
2. Select curve(s) to split face(s) with

**Split with Drawn Path(s) - Manual**

1. Select face(s) you want to split
2. Click MMB to transition to drawing the path
3. Draw path to use as splitting tool by clicking points on face(s)
4. Click MMB to perform the split
5. Select face(s) you want to delete
6. Click MMB to delete the face(s)

**Split with Face(s) - Auto**

1. Select face(s) to split
2. Select face(s) / plane(s) to split other face(s) with
3. Select face(s) to delete

**Split with Face(s) - Manual**

1. Select face(s) you want to split
2. Click MMB to transition to selecting other faces to split with
3. Select face(s) / plane(s) to split face(s) with
4. Click MMB to perform the split
5. Select face(s) you want to delete
6. Click MMB to delete the face(s)

**Split with Curve(s) - Manual**

1. Select face(s) you want to split
2. Click MMB to transition to selecting curve(s)
3. Select curve(s) to split face(s) with
4. Click MMB to perform the split

**Split with Drawn Path(s) - Auto**

1. Select face(s) to split
2. Draw split path by picking locations on surface, edge, vertex, node or marker
3. When finished drawing, click MMB to perform split

**Split with Drawn Path(s) - Manual**

1. Select face(s) you want to split
2. Click MMB to transition to drawing the path
3. Draw split path by picking locations on surface, edge, vertex, node or marker
4. Click MMB to perform the split

**Split with Face(s) - Manual**

1. Select face(s) you want to split
2. Click MMB to transition to selecting other faces to split with
3. Select face(s) / plane(s) to split face(s) with
4. Click MMB to perform the split

**Split with Curve(s) - Auto**

1. Select face(s) to split
2. Select curve(s) to split face(s) with
3. Select face(s) to delete

**Split with Curve(s) - Manual**

1. Select face(s) you want to split
2. Click MMB to transition to selecting curve(s)
3. Select curve(s) to split face(s) with
4. Click MMB to perform the split
5. Select face(s) you want to delete
6. Click MMB to delete the face(s)

**Split with Drawn Path(s) - Auto**

1. Select face(s) to split
2. Draw path to use as splitting tool by clicking points on face(s)
3. When finished drawing, click MMB to perform split
4. Select face(s) to delete

Tips:

- To multi-select, hold down CTRL or SHIFT key, when finished, release the key
- To modify spline to polyline, hold down SHIFT while drawing
- If you want to go back to (de)selecting faces, hold SHIFT then click MMB then deselect the surfaces, then proceed as you would from step 1
- If both selection stages have inputs and you want to advance directly from step 1 double click MMB
- If you have trim option selected:

---

## Split Tool (node 1510)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1510.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `ALT+Double Click` | Auto-extend picked target list |
| `R` | Change transform manipulator as rotate mode when defining split plane |
| `T` | Change transform manipulator as move mode when defining split plane |

**Split Bodies - Manual mode**

1. Select the entities you want to split
2. Click MMB to select split tool face(s)
3. Select the entities you want to split with
4. Click MMB to split

**Split Bodies - Auto mode**

1. Select the entities you want to split
2. Select the entities you want to split with

**Split Bodies(By Plane) - Manual mode**

1. Select the entities you want to split
2. Click MMB to define split plane
3. Select/define the location of your plane
4. Click MMB to split

**Split Bodies(By Plane) - Auto mode**

1. Select the entities you want to split
2. Select/define the location of your plane

**Split on Offset - Auto mode**

1. Select the entities you want to split or partition
2. Select the faces or surfaces you want to split on their offset

**Split on Offset - Manual mode**

1. Select the entities you want to split or partition
2. Select the faces or surfaces you want to split on their offset, then click MMB to split

Tips:

- Tip 1 - To multi-select multiple entities simply hold down the SHIFT or the CTRL key, then select the entities you want, then release the SHIFT or CTRL
- Tip 1 - You can drag the plane when the transform manipulator shown
- Tip 1 - Adjust the offset by moving the blue offset preview ball to an edge or vertex.
- Tip 2 - Adjust the offset value on the GUI or on the preview to change the offset.

---

## Stitch Geometry (node 946)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/946.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Stitch - Automatic**

1. Select surfaces or curves you want to perform stitch

**Stitch - Manual**

1. Select surfaces or curves you want to stitch
2. Click MMB to perform stitch

**Unstitch method - Automatic**

1. Select surfaces or curves you want to perform unstitch

**Unstitch method - Manual**

1. Select surfaces or curves you want to unstitch
2. Click MMB to perform unstitch

Tips:

- tolerances only apply to surfaces, curves must have near zero gap to stitch
- To unstitch a face or edge from a body simply select the individual face/edge then click MMB
- To convert a general body to a minimum set of manifolded bodies, pick the body, then MMB

---

## Suppress/Unsuppress (node 945)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/945.html

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
| `ALT+Double Click` | Auto-extend picked target list |

**Toggle Suppress/unsuppress - Auto**

1. Select edges and/or vertices to suppress/unsuppress

**Toggle Suppress/unsuppress - Manual**

1. Select edge(s) and/or vertice(s) you want to suppress/unsuppress
2. Click MMB to suppress/unsuppress

**Toggle Suppress only - Auto**

1. Select edges and/or vertices to suppress

**Suppress only - Manual**

1. Select edge(s) and/or vertice(s) you want to suppress
2. Click MMB to suppress

**Toggle UnSuppress only - Auto**

1. Select edges and/or vertices to unsuppress

**UnSuppress only - Manual**

1. Select edge(s) and/or vertice(s) you want to unsuppress
2. Click MMB to unsuppress

Tips:

- To multi-select, hold down CTRL or SHIFT key, when finished, release the key
- No modifier needed to toggle multi select.
- No modifier needed to toggle multi select

---

## Surface Extend (node 1088)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1088.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Extend Surfaces - Auto**

1. Select sheet or general bodies

**Extend Surfaces - Manual**

1. Select sheet or general bodies
2. Click MMB or Apply Button to finish the operation

---

## Surface Loft (node 2382)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2382.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |
| `ALT+Double Click` | Auto-extend picked target list |

**Surface Loft - Manual mode**

1. Select list two or more edge(s)/Wirebody(s) to define the loft
2. Click MMB to create surface

**Surface Loft - Auto mode**

1. Begin selecting edge(s)/Wirebody(s), as soon as two are more are selected, the surface will be created

Tips:

- Curves must be picked in loft order
- Hold down Shift key to pick more than two curves, or switch tool to Manual Selection Mode.

---

## Taper Midsurface Creation (node 1275)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1275.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `P` | Toggle visiblity picking versus occluded |

**Tapered mid surface using auto-pairing - Auto mode**

1. Select a solid face in order to automatically find the opposite side and create the midsurface

**Tapered mid surface using auto-pairing - Manual mode**

1. Select the solid faces that you want to find the opposite sides for
2. Click MMB to find and display the opposite sides to the selected face
3. You can deselect existing faces or reselect new faces at this point to change your face pairings
4. Click MMB to generate the midsurfaces

**Tapered mid surface without auto-pairing - Auto mode**

1. Select a solid face as the 1st side of your face pairing
2. Select the solid face to complete the pairing and generate the midsurface

**Tapered mid surface without auto-pairing - Manual mode**

1. Select the solid faces that represent the 1st sides of your face pairings
2. Click MMB to switch over & select the solid faces that represent the 2nd sides of the face pairings
3. Select the solid faces that represent the 2nd sides of your face pairings
4. Click MMB to create the midsurfaces based on your face pairings or SHIFT + MMB to change the selections of the 1st sides

Tips:

- If you want to multi select, hold the CTRL or the SHIFT key, then select the solid faces then release the CTRL/SHIFT key and it will execute and find the face pairings for all the faces you selected and then generate the midsurfaces
- Whenever you have at least one face pair and you are in stage where you are selecting faces for the 2nd side you can always click SHIFT + MMB and switch back to change your selection for the 1st sides of the face pairings. We will NOT clear out the selections you made for your 2nd sides but only change their color to pink, holding them for you so you can come back to them.
- Whether you have face pairings selected or not, if you find yourself in the stage of selecting the first side, you can always hold CTRL then click MMB to automatically create the midsurfaces directly.
- If you already have face pairings selected and you are in the stage of re-selecting the 1st sides, you can always immediately jump ahead to create the midsurfaces by holding CTRL and clicking on the MMB.

---

## Trim (node 996)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/996.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `F` | Brings grid parallel to screen |

**Trim sketch**

1. Select the portion of the line you want to trim

Tips:

- Pressing F will bring the sketch grid parallel to the screen

---

## Vertex Add/Remove (node 950)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/950.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

**Add Vertex**

1. Click on an edge or a curve to create a new vertex

**Remove Vertex**

1. Click on an existing vertex to remove it

Tips:

- To multi-select, hold down CTRL or SHIFT key, when finished, release the key

---

## Vertex Edge Drag (node 944)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/944.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SHIFT` | Force curved lines to straight lines |
| `Z/C` | Enlarge / shrink snap box |
| `F` | Cycle through edge behaviors |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Dragging vertices**

1. Drag vertex to either another vertex, node, marker, edge, edge extension/guide, face or release it in empty space

**Dragging edges or curves**

1. Drag edge/curve to either another edge, edge extension/guide or face or release it in empty space

Tips:

- To force attached lines from curved to straight, hold SHIFT down while dragging
- To enlarge snap box press 'Z', to shrink snap box press 'C'
