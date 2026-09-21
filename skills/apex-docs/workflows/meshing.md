# Meshing and finite elements — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [2.5D hex mesh](#2-5d-hex-mesh-node-1267)
- [3D Element Test](#3d-element-test-node-2990)
- [Curve Meshing](#curve-meshing-node-957)
- [Define Mesh Control Curve](#define-mesh-control-curve-node-2432)
- [Element Orientation](#element-orientation-node-1403)
- [Element Separate](#element-separate-node-2586)
- [Feature Mesh Setting](#feature-mesh-setting-node-961)
- [Hex Meshing](#hex-meshing-node-3053)
- [Mesh Control](#mesh-control-node-1268)
- [Node Align](#node-align-node-962)
- [Node Create](#node-create-node-956)
- [Node Merge](#node-merge-node-2023)
- [Node Move](#node-move-node-907)
- [Renumber Entities](#renumber-entities-node-2277)
- [Seeding](#seeding-node-960)
- [Shrink Wrap Mesh](#shrink-wrap-mesh-node-3120)
- [Solid Meshing](#solid-meshing-node-959)
- [Split Element](#split-element-node-965)
- [Surface Meshing](#surface-meshing-node-958)
- [Tria Reduction](#tria-reduction-node-3167)

---

## 2.5D hex mesh (node 1267)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1267.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SPACEBAR` | Launch mesh property popup |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**2.5D hex mesh – Auto mode**

1. Select a green solid to Hex Mesh

**2.5D hex mesh – Manual mode**

1. Select a green solid to Hex Mesh
2. Click MMB

**2.5D hex mesh – Auto mode**

1. Select a green solid
2. Select a starting face arrow to Hex Mesh

**2.5D hex mesh – Manual mode**

1. Select a green solid
2. Click MMB
3. Select a starting face arrow to Hex Mesh
4. Click MMB

Tips:

- Red solids means they cannot be hex meshed, yellow solids means there is some conflicting mesh control, and green solids means the solid is hex meshable.
- To multi select solids hold down either CTRL or SHIFT, select the solids you want to hex mesh then release the CTRL or SHIFT key.
- Choosing the User Defined Sweep Face option can sometimes be used to improve mesh quality by changing the initial mesh and starting face.
- Purple arrow is default.

---

## 3D Element Test (node 2990)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2990.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Assign 3D Element Properties - Auto**

1. Select the entities to assign the selected 3D Element Properties to.

**Assign 3D Element Properties - Manual**

1. Select the entities to assign the 3D Element Properties to.
2. Click middle mouse button (MMB) or Apply button when you are ready.

---

## Curve Meshing (node 957)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/957.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SPACEBAR` | Launch mesh property popup |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Curve Meshing - Auto**

1. Define mesh size in the tool properties
2. Select curve or edge to mesh

**Curve Meshing - Manual**

1. Define mesh size in the tool properties
2. Select curve or edge you want to mesh
3. Click MMB to create the mesh

**Curve Meshing - Manual**

1. Define mesh size in the tool properties
2. Select curve or edge to mesh
3. Click MMB to create the mesh

Tips:

- If you hover over the mesh then hit the SPACEBAR you will get a mesh property pop up
- The mesh property pop up lets you change the mesh size, copy a mesh size to be used again somewhere else, and launch the full mesh property by clicking the gear icon
- If you want to copy multiple times, double click the copy button then click away on as many objects to paste that mesh size onto them

---

## Define Mesh Control Curve (node 2432)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2432.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Define Mesh Control Curve - Manual mode**

1. Select curve(s) or edges(s) to define the source entity for your mesh control curve
2. Click MMB
3. Select geometry face(s) to specify the target of the mesh control curve.
4. Click MMB to complete mesh control curve creation

**Define Mesh Control Curve - Auto mode**

1. Select curve(s) or edges(s) to define the source entity for your mesh control curve
2. Select geometry face(s) to specify the target of the mesh control curve and complete the creation of the mesh control curve.

**Seed point by source and target method - Manual mode**

1. Select point(s) or node(s) to define the source entity for your seed point
2. Click MMB
3. Select edge(s) or face(s) to define the target of your seed point
4. Click MMB to complete seed point creation

**Seed point by source and target method - Auto mode**

1. Select point(s) or node(s) to define the source entity for your seed point
2. Select edge(s) or face(s) to define the target of your seed point and complete the creation of the seed point

**Seed by point on location**

1. Select a location on a face or an edge where you want to create the seed point

---

## Element Orientation (node 1403)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1403.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Reverse element orientation - Manual**

1. Select 2D elements or geometry face that you want to modify the element orientation.
2. Click MMB to reverse orientation.

**Auto align element orientation - Auto**

1. Select 2D elements that you want to do auto-align or just click MMB to do auto-align with all visible 2D elements.
2. Select one guide element to do auto-align.

**Auto align element orientation - Manual**

1. Select 2D elements that you want to do auto-align or just click MMB to do auto-align with all visible 2D elements.
2. Select one guide element to do auto-align.
3. Click MMB to auto-align

**Element Orient to Vector - Manual**

1. Select 2D elements to modify orientation, and then Click MMB.
2. Select one or two locations to define orientation vector, and then Click MMB to adjust orientation.

**Element Orient to Vector - Auto**

1. Select 2D elements to modify orientation.
2. Select geometry edge to define tangent vector and orient the elements.

**Element Orient to Curve - Manual**

1. Select 2D elements to modify orientation, and then Click MMB.
2. Select one or more curves to orient elements with, and then Click MMB to adjust orientation.

**Element Orient to Curve- Auto**

1. Select 2D elements to modify orientation.
2. Select curve to orient elements with.

Tips:

- Selecting geometry edge will orient to its tangent, and face to its normal.
- Use Ctrl key to pick two points to define vector.
- use multiple curves, and each element will try to orient to its closest curve.
- Use Ctrl key to multiple curves.

---

## Element Separate (node 2586)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2586.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Element Separate - Manual**

1. Select Parts/Meshes
2. Click middle mouse button (MMB) or Apply button when you are ready

**Element Separate - Automatic**

1. Select Parts/Meshes

---

## Feature Mesh Setting (node 961)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/961.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Feature mesh configuration**

1. Select the feature type you want to configure for
2. Define the ranges for the feature type
3. Set the parameters for the feature mesh configuration for each range

Tips:

- You can set the parameters for the different ranges of measure of the feature type
- The ranges are defined by the slider and you can click on the left or right side of the slider to create a new range
- Make sure you define the correct max value in the range otherwise you may notice that your feature meshes are not taking effect when you proceed to mesh after
- The changes you make take effect immediately once you set them
- You may now go to your meshing tools and turn on the feature meshing option to leverage these settings

---

## Hex Meshing (node 3053)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3053.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SPACEBAR` | Launch mesh property popup |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Hybrid Meshing - Auto**

1. Select any solid or cell to create Hybrid Mesh

**Hybrid Meshing - Manual**

1. Select any solid or cell to create Hybrid Mesh
2. Click MMB

Tips:

- To multi select solids hold down either CTRL or SHIFT, select the solids you want to hex mesh then release the CTRL or SHIFT key.

---

## Mesh Control (node 1268)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/1268.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT + H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Seed point by source and target method - Manual mode**

1. Select point(s) or node(s) to define the source entity for your seed point
2. Click MMB
3. Select edge(s) or face(s) to define the target of your seed point
4. Click MMB to complete seed point creation

**Seed point by source and target method - Auto mode**

1. Select point(s) or node(s) to define the source entity for your seed point
2. Select edge(s) or face(s) to define the target of your seed point and complete the creation of the seed point

**Seed by point on location**

1. Select a location on a face or an edge where you want to create the seed point

---

## Node Align (node 962)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/962.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SHIFT` | Modifies spline into polyline |
| `CTRL` | Toggle multi select |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Node Align by Curve(s)/Edge(s) - Auto**

1. Select the starting node from the row of nodes that you want to align
2. Select the ending node of the row of nodes that you want to align
3. Select the curve or edge to which you want to align the node(s) to

**Node Align by Curve(s)/Edge(s) - Manual**

1. Select the starting node from the row of nodes that you want to align
2. Click MMB to transition to selecting the ending node of the row of nodes
3. Select the ending node of the row of nodes that you want to align
4. Click the MMB to transition to selecting the curves or edges you want the nodes to align to
5. Select the curve or edge to which you want to align the node(s) to
6. Click MMB to align the nodes

**Node Align by Path - Auto**

1. Select the starting node from the row of nodes that you want to align
2. Select the ending node of the row of nodes that you want to align
3. Draw the spline you want to use to align the nodes to

**Node Align by Path - Manual**

1. Select the starting node from the row of nodes that you want to align
2. Select the ending node of the row of nodes that you want to align
3. Click the MMB to transition to drawing the path you want use to align the nodes
4. Draw the line or spline you want to use to align the nodes by selecting the points of the path
5. Click MMB to align the nodes

**Node Align by Curve(s)/Edge(s) - Manual**

1. Select the starting node from the row of nodes that you want to align
2. Select the ending node of the row of nodes that you want to align
3. Click the MMB to transition to selecting the curves or edges you want the nodes to align to
4. Select the curve or edge to which you want to align the node(s) to
5. Click MMB to align the nodes

Tips:

- To make a spline a polyline just press down on the SHIFT key

---

## Node Create (node 956)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/956.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Node create at a location**

1. Click where you want on a geometry or FE entity to create a node

**Node create on Arc - Auto**

1. Select an arc or a circle to create a node at its center

**Node create on Arc - Manual**

1. Select an arc or a circle to create a node at its center
2. Click MMB to create the node(s)

**Node create at intersection - Auto**

1. Select at least 2 curves or edges to create a node at their intersection

**Node create at intersection - Manual**

1. Select at least 2 curves or edges to create node(s) at their intersections
2. Click MMB to create the node(s)

**Node delete - Auto**

1. Select the node(s) you want to delete

**Node delete - Manual**

1. Select the node(s) you want to delete
2. Click MMB to delete the node(s)

**Create Node by 3D Location**

1. Define the 3D location in the text box
2. Select a coordinate system in which the location of the Node is defined
3. Click MMB or Apply

**Create Node by 3D Location**

1. Define the 3D location in the text box
2. Select a node analysis coordinate system
3. Click MMB or Apply

**Create Node by 3D Location**

1. Define the 3D location in the text box
2. Select a coordinate system in which the location of the Node is defined
3. Select a node analysis coordinate system
4. Click MMB or Apply

**Create Node by 3D Location**

1. Define the 3D location in the text box
2. Click MMB or apply

**Node create at intersection - Auto**

1. Select at least 2 curves or edges to create a node a their intersection

**Node create at intersection - Manual**

1. Select at least 2 curves or edges to create node(s) a their intersections
2. Click MMB to create the node(s)

Tips:

- if the node is defined on local coordinate system, the node location will be persisted in global instead of local coordinate system while the option "Convert and persist node coordinates in Global" is on.

---

## Node Merge (node 2023)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2023.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |

**Node Merge – Manual mode**

1. Nodes or Mesh Body(s) as targets to search for nodes to merge
2. Click MMB to begin the operation

**Node Merge – Auto mode**

1. Nodes or Mesh Body(s) as targets to search for nodes to merge

**Node Merge - Manual mode**

1. Select Nodes, Mesh Body(s) or Parts as targets to search for nodes to merge
2. Click middle mouse button (MMB) or Apply button when you are ready

**Node Merge - Auto mode**

1. Select Nodes, Mesh Body(s) or Parts as targets to search for nodes to merge

Tips:

- Use the toggles and buttons on the GUI to adjust the node merge behavior.The more restrictive the search, such as Only Free Edges, or Only Merge within a body, the faster the operation will be.

---

## Node Move (node 907)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/907.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Node move along a surface**

1. Drag nodes along the surface's curvature

**Node move normal to a surface**

1. Drag nodes normal to the surface

**Node move**

1. Click and hold on left mouse button to move node.
2. Move node to desired location.

Tips:

- A node can be moved to any pickable location, such as any other node, point, location on curve, or location on a surface.
- Associated to Geometry: Nodes associated to geometry can be moved arbitrarily along the geometry or snapped to vertices.
- Unassociated Nodes: Nodes not associated to geometry (Orphan Mesh), have two drag behaviors in addition to the normal node placement options that all nodes have.
- Element Face: In this mode, nodes are dragged along any element edge or face.
- Element Surface: In this mode, nodes are moved along a local approximated curvature. This is used for highly curved meshes. This can have a more restrictive domain where nodes can be moved. Nodes on feature edges will only have free movement along this edge.
- Feature Angle: This setting is used to define interior edge features. This is used to help guide node movement to preserve current mesh features.

---

## Renumber Entities (node 2277)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/2277.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `ESC` | Abort operation midway |

**Renumber Tool**

1. Select the object you want to renumber.
2. Define Renumber Method and Renumber Setting in the tool properties.
3. Enter the Starting ID or Offset IDs for the entity type to renumber.
4. Click the Apply button or MMB to renumber.

---

## Seeding (node 960)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/960.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SPACEBAR` | Launch mesh property popup |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**# of uniformly spaced elements - Auto**

1. Define the number of seeds from the tool properties
2. Select the curve(s) or edge(s) you want to create seeds on

**# of uniformly spaced elements - Manual**

1. Define the number of seeds from the tool properties
2. Select the curve(s) or edge(s) you want to create seeds on
3. Click MMB to create seeds

**Size of uniformly spaced elements - Auto**

1. Define the element size from the tool properties
2. Select the curve(s) or edge(s) you want to create seeds on

**Size of uniformly spaced elements - Manual**

1. Define the element size from the tool properties
2. Select the curve(s) or edge(s) you want to create seeds on
3. Click MMB to create seeds

**Bias method - Auto**

1. Define the bias parameters from the tool properties
2. Select the curve(s) or edge(s) you want to create seeds on

**Bias method - Manual**

1. Define the bias parameters from the tool properties
2. Select the curve(s) or edge(s) you want to create seeds on
3. Click MMB to create seeds

Tips:

- If you hover over the mesh then hit the SPACEBAR you will get a seed property pop up
- The seed property pop up lets you change the seed number, copy a seed number to be used again somewhere else, and launch the full seed property by clicking the gear icon
- If you want to copy multiple times, double click the copy button then click away on as many edges/curves to paste that seed number onto them

---

## Shrink Wrap Mesh (node 3120)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3120.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Shrink Wrap Meshing - Auto**

1. Define mesh size in the tool properties
2. Select bodies to mesh over

**Shrink Wrap Meshing - Manual**

1. Define mesh size in the tool properties
2. Select body(ies) to mesh
3. Click MMB to create the mesh

Tips:

- Unlike other mesh tools, this mesh is not associated to any geometry, so multiple meshes can be created from the same source.

---

## Solid Meshing (node 959)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/959.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SPACEBAR` | Launch mesh property popup |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visiblity picking versus occluded |

**Solid Meshing - Auto**

1. Define mesh size in the tool properties
2. Select solid body(ies) to mesh

**Solid Meshing - Manual**

1. Define mesh size in the tool properties
2. Select solid body(ies) to mesh
3. Click MMB to create the mesh

Tips:

- If you hover over the mesh then hit the SPACEBAR you will get a mesh property pop up
- The mesh property pop up lets you change the mesh size, copy a mesh size to be used again somewhere else, and launch the full mesh property by clicking the gear icon
- If you want to copy multiple times, double click the copy button then click away on as many objects to paste that mesh size onto them

---

## Split Element (node 965)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/965.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SHIFT` | Modifies spline into polyline |
| `CTRL` | Toggle multi select |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Element/Mesh Split by Curve(s)/Edge(s)/Surface(s) - Auto**

1. Select Elements or Mesh(es) that you want to split
2. Select the geometry entity(ies) that you want split with

**Element/Mesh/Surface Split by Curve(s)/Edge(s) - Manual**

1. Select Elements or Mesh(es) that you want to split
2. Click MMB to transition to selecting the curve or edge or surface you want to split with
3. Select the curve(s) or edge(s) that you want split with
4. Click MMB to split the elements or meshes

**Element/Mesh Split by Path - Auto**

1. Select Elements or Mesh(es) that you want to split
2. Draw the spline/polyline that you want to use to split with

**Element/Mesh Split by Path - Manual**

1. Select Elements or Mesh(es) that you want to split
2. Draw Click MMB to transition to selecting the curve or edge you want to split with
3. Draw the spline/polyline that you want to use to split with
4. Click MMB to split the elements or meshes

**Element/Mesh Split by Curve(s)/Edge(s)/Surface(s) - Manual**

1. Select Elements or Mesh(es) that you want to split
2. Click MMB to transition to selecting the curve or edge or surface you want to split with
3. Select the curve(s) or edge(s) that you want split with
4. Click MMB to split the elements or meshes

**Element/Mesh Split by Path - Manual**

1. Select Elements or Mesh(es) that you want to split
2. Click MMB to transition to draw split path
3. Draw the spline/polyline that you want to use to split with
4. Click MMB to split the elements or meshes

**Split by Pattern - Auto mode**

1. Select the elements you want to split

**Split by Pattern - Manual mode**

1. Select the elements you want to split and then click MMB

Tips:

- To make a spline a polyline just press down on the SHIFT key
- Change the N,M values if you want to split more quad elements
- When N=M, you only need to select elements, but when N ≠M, you need to select one geometry edge or element edge to orient "N"

---

## Surface Meshing (node 958)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/958.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `SPACEBAR` | Launch mesh property popup |
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ALT+Double Click` | Auto-extend picked target list |
| `H` | Hide preselected faces |
| `SHIFT+H` | Re-display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded |

**Surface Meshing - Auto**

1. Define mesh size in the tool properties
2. Select surface or face to mesh

**Surface Meshing - Manual**

1. Define mesh size in the tool properties
2. Select surface or face you want to mesh
3. Click MMB to create the mesh

**Incremental Surface Meshing - Edit Washer Settings**

1. Select feature type to edit
2. Select features to edit on the canvas
3. Move to next Step to mesh

**Incremental Surface Meshing - Edit Arbitrary Hole Settings**

1. Select feature type to edit
2. Select features to edit on the canvas
3. Move to next Step to mesh

**Incremental Surface Meshing - Create Surface Mesh**

1. Adjust the mesh type settings, then click MMB to mesh

**Incremental Meshing - Auto**

1. Define mesh size in the tool properties
2. Select body to mesh to show feature mesh Preview
3. Select feature to edit local settings
4. Click MMB to move to meshing stage, then MMB to mesh

**Incremental Surface Meshing - Manual**

1. Select Target Body with Features, then MMB
2. Change to Next Step then select features to edit
3. Change to Meshing stage to mesh

Tips:

- If you hover over the mesh then hit the SPACEBAR you will get a mesh property pop up
- The mesh property pop up lets you change the mesh size, copy a mesh size to be used again somewhere else, and launch the full mesh property by clicking the gear icon
- If you want to copy multiple times, double click the copy button then click away on as many objects to paste that mesh size onto them
- Use the copy button to copy settings to other features
- Final meshing can be done in this tool or the regular mesher
- Use ESC key to complete washer rotation mode
- Final meshing can be done in the regular shell mesher, tet mesher or hex mesher
- Hover over face and press SPACBAR to get to the property panel pop up to edit face mesh settings
- The pop up editor can also be used to copy settings to other faces
- Mesh Flow Optimization does not currently support Facet bodies
- Click on gear in tool property to change global feature settings
- Click on washer, then center disk to edit its settings
- Click on rotation handle to initiate washer rotation mode, then click on ring to rotate washer mesh
- Click the copy button on local washer settings. then click on other washers to copy the settings
- Meshing can also be completed in regular shell meshing, tet meshing or hex meshing after editing features

---

## Tria Reduction (node 3167)

Reference page: https://nexus.hexagon.com/documentationcenter/en-US/bundle/msc_apex_help/page/node/3167.html

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi select |
| `SHIFT` | Pure accumulation |
| `CTRL+SHIFT` | Pure deselection |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |

**Tri Reduction Without Locked entities - Auto mode**

1. Optionally adjust thresholds to control allowable element quality
2. Select meshes or elements associated to geometry to reduce Tria elements

**Tri Reduction Without Locked entities - Manual mode**

1. Optionally adjust thresholds to control allowable element quality
2. Select meshes or elements associated to geometry to reduce Tria elements then press MMB
