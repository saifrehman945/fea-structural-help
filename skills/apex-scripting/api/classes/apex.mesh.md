# apex.mesh — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.mesh.CurveMesh`  (extends `MeshBody`)
CurveMesh Class Object. extends MeshBody Class Object.
Properties: `elementOrder`, `meshSize`, `target`

Methods:

- `getElementOrder() -> apex.mesh.ElementOrder` — return the elementOrder of the curve mesh.
- `getMeshSize() -> float` — return the meshsize of the curve mesh.
- `getTarget() -> apex.EntityCollection` — return the list of edges which are meshed.
#### `update(name: str, meshSize: float, elementOrder: apex.mesh.ElementOrder) -> apex.mesh.ZResultCreateCurveMesh`
update one or more of this curve mesh properties.

- `name` — Name of the new curve mesh.
- `meshSize` — Specify the Global Edge Length to use in meshing the selected geometry.
- `elementOrder` — Enumeration defining which mesh element type to use to create the CurveMesh. Options are: 1. CurveMeshElementType.Linear


## `apex.mesh.CurveMeshCollection`  (extends `MeshBodyCollection`)
Iterable collection of Meshs, based on apex::EntityCollection.

Methods:

- `CurveMeshCollection() -> None` — Construct a new CurveMeshCollection.
#### `appendList(curveMeshList: [apex.mesh.CurveMesh]) -> None`
Add CurveMesh from a list to the end of this collection.

- `curveMeshList` — list of CurveMesh to add to the collection.

For example:


## `apex.mesh.EdgeSeed`  (extends `Entity`)
EdgeSeed Class Object. Class that represents the collection of MeshControlPoints on a geometry Edge. EdgeSeeds are created interactively using the Mesh Seeding tool. EdgeSeeds compose 2 or more MeshControlPoints. Each 'point" on the Edge created by and EdgeSeed is a MeshControlPoint.
Properties: `biasType`, `edge`, `elementEdgeLength`, `numElementEdges`

Methods:

- `getBiasType() -> apex.mesh.BiasType`
- `getEdge() -> apex.geometry.Edge`
- `getElementEdgeLength() -> float`
- `getNumElementEdges() -> int`
#### `update(numElementEdges: int, elementEdgeLength: float) -> None`
This methods is used to update one or more public attributes of the EdgeSeed.

- `numElementEdges` — The number of element edges that the seed will cause to be created - this always one less than the number of seed points that.
- `elementEdgeLength` — The target element size to use to determine how many seed points will be created.


## `apex.mesh.EdgeSeedCollection`  (extends `EntityCollection`)
Iterable collection of EdgeSeed, based on EntityCollection.

Methods:

- `EdgeSeedCollection() -> None` — Construct a new EdgeSeedCollection.
#### `appendList(edgeSeedList: [apex.mesh.EdgeSeed]) -> None`
Add EdgeSeed from a list to the end of this collection.

- `edgeSeedList` — list of EdgeSeed to add to the collection.

For example:


## `apex.mesh.Element`  (extends `Entity`, `IIdentifier`, `IPhysical`)
Element Class Object.
Properties: `behavior`, `connectedElements`, `constraints`, `edges`, `elementProperty2D`, `elementProperty3D`, `faces`, `initialConditions`, `loads`, `material`, `nodeIds`, `nodes`, `normal`, `offset`, `parent`, `referencedBy`, `section`, `span`, `thickness`, `topology`

Methods:

#### `assignMaterial(material: apex.attribute.Material) -> bool`
assign a material to this element.

Returns: status of true or false (bool)

#### `assignShellSection(section: apex.attribute.ShellSection) -> bool`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.attribute.createFieldThicknessOffsetConstant. assign a shell section to this element.

Returns: status of true or false (bool)

#### `getBehavior() -> apex.attribute.ShellBehavior`
Returns the Behavior associated with this element. The Behavior may be indirectly associated with the element through the parent Part, GeometryBody, Face or MeshBody. If no Behavior is associated with this element the method will return a None value.

Returns: the Behavior associated with this element.

- `getConnectedElements() -> ElementCollection` — Returns a collection of all elements that are connected to this element by sharing one or more nodes. Node Ties are not returned by this method.
- `getConstraints() -> apex.EntityCollection` — Returns a collection of all Constraints that are applied to this Element. The Constraints may be applied directly to the Element or to its parent GeometryBody, Face, Edge, Vertex, or MeshBody. If no Constraints are associated with the Element the method will return an empty EntityCollection.
#### `getEdges() -> ElementEdgeCollection`
Returns a read only ElementEdgeCollection of the edges of this element. The element edges are ordered to reflect the edge ordering of Apex elements. This method will return an empty collection if called on 0D elements.

Returns: a read only ElementEdgeCollection of the edges of this element.

- `getElementProperty2D() -> apex.attribute.PropertiesElement2D` — Returns the ElementProperty2D associated with this element. Gets an instance of the ElementProperty2D associated with this element. The ElementProperty2D may be indirectly associated to the element through the parent Part, GeometryBody, Face or MeshBody. If no ElementProperty2D is associated with this element the method will return a None value.
- `getElementProperty3D() -> apex.attribute.PropertiesElement3D` — Returns the ElementProperty3D associated with this element. The ElementProperty3D may be indirectly associated to the element through the parent Part, GeometryBody or MeshBody. If no ElementProperty3D is associated with this element the method will return a None value.
#### `getFaces() -> ElementFaceCollection`
Returns a read only ElementFaceCollection of the faces of this element. The element faces are ordered to reflect the face ordering of Apex elements. This method will return an empty collection if called on 0D or 1D elements.

Returns: a read only ElementFaceCollection of the faces of this element.

#### `getFields() -> apex.attribute.DiscreteFEMFieldCollection`
Returns all fields associated with this element. The Field may be indirectly associated to the element through the parent Part, GeometryBody, Face or MeshBody. If no Field is associated with this element the method will return a None value.

Returns: all fields associated with this element.

- `getInitialConditions() -> apex.EntityCollection` — Returns a collection of all InitialConditions that are applied to this Element. The InitialConditions may be applied directly to the Element or to its parent GeometryBody, Face, Edge, Vertex, or MeshBody. If no InitialConditions are associated with the Element the method will return an empty EntityCollection.
- `getLoads() -> apex.EntityCollection` — Returns a collection of all Loads that are applied to this element. The Loads may be applied directly to the element or to its parent Surface, Face, Edge, Vertex, MeshBody or Part. If no Loads are associated with the element the method will return an empty LoadCollection.
#### `getMaterial() -> apex.attribute.Material`
Returns the material associated with this element. The Material may be indirectly associated to the element through the parent Part, GeometryBody, Face, Edge or MeshBody. If no material is associated with this element the method will return a None value.

Returns: the material associated with this element.

- `getNodeIds() -> [int int int]` — Returns an ordered List of the Node ID's that define the topology of the element.
- `getNodes() -> NodeCollection` — A read only ordered collection of the nodes that define the element topology. Each element topology defines a fixed order for the nodes.
#### `getNormal() -> apex.construct.Vector3D`
returns a vector representing the outward normal of the element. This method is only available on 2D elements and will throw an exception if called from 0D, 1D or 3D elements.

Returns: a vector representing the outward normal of the element.

- `getOffset() -> float` — Returns the offset of the element when the element is 2D element. The offset may come from the PropertiesElement2D or Section. This method will return an "NAN" when the element is 1D or 3D element. If the element is assigned with Layered Panel, element.offset should return the zone offset distance.
#### `getParent() -> MeshBody`
Returns the parent MeshBody for this element.

Returns: the parent MeshBody for this element.

- `getReferencedBy() -> apex.EntityCollection` — returns a collection of all entities that directly Reference this Element
#### `getSection() -> apex.attribute.ShellSection`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.mesh.element.getFields Returns the Section associated with this element. The Section may be indirectly associated to the element through the parent Part, GeometryBody, Face or MeshBody. If no Section is associated with this element the method will return a None value.

Returns: the Section associated with this element.

#### `getSpan() -> apex.attribute.BeamSpan`
Returns the BeamSpan associated with this element. If the element is not associated with a BeamSpan the method will return None.

Returns: the BeamSpan associated with this element.

- `getThickness() -> float` — Returns the thickness of the element when the element is 2D element. The thickness may come from the PropertiesElement2D or Section. This method will return an "NAN" when the element is 1D or 3D element. If the element is assigned with Layered Panel, then element.thickness should return the zone thickness.
- `getTopology() -> ElementTopology` — Returns the topology of this element as an apex.mesh.ElementTopology enumeration.
- `reverse() -> Element` — Reverses the Element Node order and returns the Element For example a linear Quadrilateral element with original node ordering of 1-2-3-4 will be modified to have the node ordering 1-4-3-2.
#### `set12Edge(node_1: int int int, node_2: int int int) -> Element`
Sets the desired 1-2 edge of the element and returns the Element. The desired 1-2 edge is identified using the ID's of the Nodes that define the edge. Only corner nodes may be used to identify the 1-2 edge - if an ID is provided that represents a mid-side node the method will throw an exception. If a single Node ID is provided, the existing element edge that starts with that Node will become the 1-2 edge. If two nodes ID's are provided they must be associated with opposite ends of the same element edge, otherwise the method will throw an exception. If two nodes are used to define the 1-2, the first node will be used to define the starting end of the 1-2 edge and the second node will define the second end of the 1-2 edge. This can result in the element being reversed in addition to modifying the 1-2 edge.

- `node_1` — The ID of the Node that will become the first Node on the 1-2 Edge.
- `node_2` — The ID of the Node that will defined the end of the Element 1-2 Edge.If this argument is omitted, the existing element edge that starts with the node_1 node will become the 1-2 edge


## `apex.mesh.ElementCollection`  (extends `IPhysicalCollection`)
Iterable collection of Elements, based on apex::EntityCollection.

Methods:

- `ElementCollection() -> None` — Construct a new ElementCollection.
#### `appendList(elemList: [apex.mesh.Element]) -> None`
Add Element from a list to the end of this collection.

- `elemList` — list of Element to add to the collection.

For example:


## `apex.mesh.ElementEdge`  (extends `Entity`, `IIdentifier`, `IPhysical`)
Class representing the Edge of an Element.
Properties: `connectedElements`, `constraints`, `initialConditions`, `loads`, `nodes`, `parent`

Methods:

- `getAxisAlignedBoundingBox() -> apex.AxisAlignedBoundingBox` — Returns the axis aligned bounding box around the object in space.
- `getConnectedElements() -> ElementCollection` — Returns a collection of all elements that are connected to this element edge by sharing one or more nodes. The parent element will NOT be returned. To retreive the parent element from an ElementEdge use the ElementEdge.parent property. Node Ties are not returned by this method.
- `getConstraints() -> apex.EntityCollection` — Returns a collection of all Constraints that are applied to this ElementEdge. The Constraints may be applied directly to the ElementEdge or to its parent Surface, Face, Edge,MeshBody or Part. If no Constraints are associated with the ElementEdge the method will return an empty ConstraintCollection.
- `getInitialConditions() -> apex.EntityCollection` — Returns a collection of all InitialConditions that are applied to this ElementEdge. The InitialConditions may be applied directly to the ElementEdge or to its parent its parent Surface, Face, Edge, MeshBody or Part. If no InitialConditions are associated with the ElementEdge the method will return an empty EntityCollection.
- `getLoads() -> apex.EntityCollection` — Returns a collection of all Loads that are applied to this ElementEdge. The Loads may be applied directly to the ElementEdge or to its parent its parent Surface, Face, Edge, MeshBody or Part. If no Loads are associated with the ElementEdge the method will return an empty LoadCollection.
- `getNodes() -> NodeCollection` — Returns an ordered collection of the nodes that define this ElementEdge.
- `getParent() -> Element` — Returns the parent element from this ElementEdge.

## `apex.mesh.ElementEdgeCollection`  (extends `IPhysicalCollection`)
Iterable collection of ElementEdges based on apex.EntityCollection.

Methods:

- `ElementEdgeCollection() -> None` — Construct a new ElementEdgeCollection.
#### `appendList(elemEdgeList: [apex.mesh.ElementEdge]) -> None`
Add ElementEdge from a list to the end of this collection.

- `elemEdgeList` — list of ElementEdge to add to the collection.

For example:


## `apex.mesh.ElementFace`  (extends `Entity`, `IIdentifier`, `IPhysical`)
Class representing the Face of an Element.
Properties: `connectedElements`, `displacementConstraints`, `edges`, `loads`, `nodes`, `normal`, `parent`

Methods:

- `clearHighlight() -> None` — Removes highlighting from the object. The method has no effect if the object is not already highlighted.
- `getAxisAlignedBoundingBox() -> apex.AxisAlignedBoundingBox` — Returns the axis aligned bounding box around the object in space.
- `getConnectedElements() -> ElementCollection` — Returns a collection of all elements that are connected to this element face by sharing one or more nodes. The parent element will NOT be returned. To determine the parent element from an ElementFace use the ElementFace.parent property. Node Ties are not returned by this method.
- `getDisplacementConstraints() -> apex.environment.DisplacementConstraintCollection` — Returns a collection of all DisplacementConstraints that are applied to this ElementFace. The DisplacementConstraints may be applied directly to the ElementFace or to its parent Surface, Face, MeshBody or Part. If no DisplacementConstraints are associated with the ElementFace the method will return an empty DisplacementConstraintCollection.
- `getEdges() -> ElementEdgeCollection` — Returns the element edges that comprise this ElementFace as an ElementEdgeCollection.
- `getLoads() -> apex.EntityCollection` — Returns a collection of all Loads that are applied to this ElementFace. The Loads may be applied directly to the element face or to its parent Surface, Face, Edge, MeshBody or Part. If no Loads are associated with the element face the method will return an empty LoadCollection.
- `getNodes() -> NodeCollection` — Returns an ordered collection of the nodes that define this ElementFace.
- `getNormal() -> apex.construct.Vector3D` — Returns the outward normal of the element face using the right hand rule with respect to the face node order.
- `getParent() -> Element` — Returns the parent element from this ElementFace.
- `highlight(colorRGB: apex.ColorRGB, lineWidth: int, pointSize: int) -> None` — Highlights the object using the highlight parameters in the argument list.
- `highlightColorRGB() -> apex.ColorRGB` — The highlight color assigned to the object as a ColorRGB object that support 8 bit RGB color definitions.
- `highlightEdgeWeight() -> int` — The edge weight assigned to the object.
- `highlightPointSize() -> int` — The highlight point size assigned to the object.
- `isHighlighted() -> bool` — Boolean indicating whether the object is highlighted or not.

## `apex.mesh.ElementFaceCollection`  (extends `IPhysicalCollection`)
Iterable collection of ElementFaces, based on apex::EntityCollection.
Properties: `elementFaceDictionary`

Methods:

- `ElementFaceCollection() -> None` — Construct a new ElementFaceCollection.
#### `appendList(elemFaceList: [apex.mesh.ElementFace]) -> None`
Add ElementFace from a list to the end of this collection.

- `elemFaceList` — list of ElementFace to add to the collection.

For example:

- `getElementFaceDictionary() -> {str:{apex.mesh.ElementTopologyNS.value:{str:[int int int int]}}}` — Gets the ID's and topologies of the element faces in the ElementFaceCollection using a nested dictionary. Apex supports Elements that may have duplicate ID's across Parts therefore an Element cannot be uniquely identified solely by its ID. elementFaceDictionary returns the element face ID's and topologies partitioned by MeshBody. elementFaceDictionary is the primary dictionary and uses a string type key to identify the MeshBody using its unique pathName. The associated value is a dictionary type referred to here as the secondary dictionary. The secondary dictionary further partitions data by element type and has key of type apex.mesh.ElementTopology. The value associated with this dictionary key is another dictionary referred to here as the tertiary dictionary. The tertiary dictionary contains the actual element face ID's and topologies. The tertiary dictionary supports three string type keys - 'ids', 'topologies_id' and 'topologies_index'. The values associated with these three keys are 'ids' - an Array/List of integers identifying the ids of the elements to which the element face is associated 'face_ids' - an Array/List of integers identifying the ids of the element faces 'topologies_id' - an Array/List of integers identifying the topology of the element faces using Node IDs 'topologies_index' - an Array/List of integers identifying the topology of the element faces using Node indices Example : ElementFaceDictionary defined on three nodes as follow {"Model_1/Part 1/Mesh 1" : {"12" : { 'face_ids': [0, 1, 2, 3, 4, 5], 'ids': [3567], 'topologies_id': [1427, 1428, 1458, 1468, 1559, 1560, 4331, 4341], 'topologies_index': [1426, 1427, 1457, 1467, 1558, 1559, 4330, 4340]} } }

## `apex.mesh.ElementIdSet`  (extends `Entity`)
ElementIdSet Class Object. A set (list of unique) Element IDs .

## `apex.mesh.ElementIdSetCollection`  (extends `EntityCollection`)
Iterable collection of ElementIdSet objects, based on apex::EntityCollection.

Methods:

- `ElementIdSetCollection() -> None` — Construct a new ElementIdSetCollection.
#### `appendList(elemIdSetList: [apex.mesh.ElementIdSet]) -> None`
Add ElementIdSet from a list to the end of this collection.

- `elemIdSetList` — list of ElementIdSet to add to the collection.

For example:


## `apex.mesh.HexMesh`  (extends `MeshBody`)
HexMesh Class Object. extends MeshBody Class Object.
Properties: `elementGeometryDeviationRatio`, `elementMinEdgeLengthRatio`, `elementOrder`, `mappedMeshDominanceLevel`, `meshAlgorithm`, `meshMethod`, `meshSize`, `refineMeshUsingCurvature`, `target`

Methods:

- `getElementGeometryDeviationRatio() -> float` — return the value of elementGeometryDeviationRatio.
- `getElementMinEdgeLengthRatio() -> float` — return the value of elementMinEdgeLengthRatio.
- `getElementOrder() -> apex.mesh.ElementOrder` — return the elementOrder of the hex mesh.
- `getMappedMeshDominanceLevel() -> signed int int` — return the value of mappedMeshDominanceLevel.
- `getMeshAlgorithm() -> apex.mesh.HexMeshMethod` — return the value of meshAlgorithm.
- `getMeshMethod() -> apex.mesh.SurfaceMeshMethod` — return the meshMethod of the hex mesh.
- `getMeshSize() -> float` — return the meshsize of the hex mesh.
- `getRefineMeshUsingCurvature() -> bool` — return flag: enable/disable the curvature refinement option.
- `getTarget() -> apex.geometry.Solid` — return solid which are meshed.
#### `update(name: str, meshSize: float, surfaceMeshMethod: apex.mesh.SurfaceMeshMethod, mappedMeshDominanceLevel: int, elementOrder: apex.mesh.ElementOrder, refineMeshUsingCurvature: apex.ApexBool, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, createFeatureMeshOnWashers: apex.ApexBool, createFeatureMeshOnArbitraryHoles: apex.ApexBool, preserveWasherThroughMesh: apex.ApexBool, hexMeshMethod: apex.mesh.HexMeshMethod, projectMidsideNodesToGeometry: apex.ApexBool) -> apex.mesh.ZResultCreateHexMesh`
update one or more of this hex mesh properties.

- `name` — Name of the new hex mesh.
- `meshSize` — Specify the Global Edge Length to use in meshing the selected geometry.
- `surfaceMeshMethod` — Enumeration defining which mesh algorithm to use to create the SurfaceMesh. Options are: 1. SurfaceMeshMethod.Auto 2. SurfaceMeshMethod.Pave 3. SurfaceMeshMethod.Mapped
- `mappedMeshDominanceLevel` — Value to control how aggressively the algorithm will be in forcing creation of a mapped mesh. Varies from 1 (least aggressive) to 5 (most aggressive). Must be defined if meshMethod is SurfaceMeshMethod.Mapped.
- `elementOrder` — Enumeration defining the order of the elements to be created for the HexMesh Options are: 1. MeshOrder.Linear 2. MeshOrder.Quadratic.
- `refineMeshUsingCurvature` — Flag to enable the curvature refinement option of the surface meshing algorithm.
- `elementGeometryDeviationRatio` — Value to control the maximum deviation between and element edge and it's correpsonding geometry edge during curvature refinement. Takes a value between 0.0 and 1.0. *Must be defined if enableCurvatureRefinement is True, otherwise it is ignored.
- `elementMinEdgeLengthRatio` — Value to control the minimum element edge length relative to the global element edge length during curvature refinement. *Must be defined if enableCurvatureRefinement is True, otherwise it is ignored.
- `createFeatureMeshOnWashers` — Enables the washer feature mesh option in hex meshing.
- `createFeatureMeshOnArbitraryHoles` — Enables the arbitrary hole feature mesh option in hex meshing.
- `preserveWasherThroughMesh` — Attempt to extrude all washer feature through entire mesh in hex meshing.
- `hexMeshMethod` — hex algorithm option.
- `projectMidsideNodesToGeometry` — optional Boolean argument (default = True) that specifies whether the mid-side nodes of higher order Hexa/Penta elements will be projected onto the target Geometry or not. By default (True), the mid-side nodes of all higher order Hexa/Penta elements will be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.


## `apex.mesh.HexMeshCollection`  (extends `MeshBodyCollection`)
Iterable collection of Meshs, based on apex::EntityCollection.

Methods:

- `HexMeshCollection() -> None` — Construct a new HexMeshCollection.
#### `appendList(hexMeshList: [apex.mesh.HexMesh]) -> None`
Add HexMesh from a list to the end of this collection.

- `hexMeshList` — list of HexMesh to add to the collection.

For example:


## `apex.mesh.MeshBody`  (extends `Entity`, `IDisplayable`, `IPhysical`, `IUserAttributes`, `IName`, `IActivatable`)
MeshBody Class Object.
Properties: `associatedGeometry`, `elementConnectivities`, `elementEdges`, `elementFaces`, `elementIDs`, `elements`, `nodeCoordinates`, `nodeIDs`, `nodes`, `parent`, `referenceSystem`, `subMeshes`

Methods:

#### `asEntity() -> apex.Entity`
return the (base) Entity Object of this MeshBody.

Returns: this MeshBody Entity object

#### `assignMaterial(pMat: apex.attribute.Material) -> bool`
assign a material to this MeshBody.

Returns: status of true or false (bool)

#### `assignShellSection(pSection: apex.attribute.ShellSection) -> bool`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.attribute.createFieldThicknessOffsetConstant. assign a shell section to this MeshBody.

Returns: status of true or false (bool)

#### `createElement(topologyType: apex.mesh.ElementTopology, nodes: [int int int]) -> apex.mesh.Element`
Creates an element in this MeshBody. The element topology type is provided as input and the topology is defined using Node ID's The Nodes used to define the topology must exit in this MeshBody.

- `topologyType` — The topology type for this element as an apex.mesh.ElementTopology enumeration.
- `nodes` — The nodes that define this element.The nodes are provided as an ordered List of integer Node ID's.The number of nodes and the node ordering is dependent on the Element topology.

Returns: the created element.

#### `createElements(topologyType: apex.mesh.ElementTopology, nodes: [int int int]) -> apex.mesh.ElementCollection`
Creates multiple Elements in this MeshBody. The element topology type is provided as input and the topology is defined using Node ID's The Nodes used to define the topology must exit in this MeshBody To create multiple element types in the same MeshBody the method must be called at least once for each ElementTopology type.

- `topologyType` — The topology type for this element as an apex.mesh.ElementTopology enumeration.
- `nodes` — The nodes that define this element.The nodes are provided as an ordered List of integer Node ID's.The number of nodes and the node ordering is dependent on the Element topology.

Returns: the created elements.

#### `createNode(location: apex.ILocation, csys: int = 0) -> apex.mesh.Node`
Creates a Node in this MeshBody at the provided location and returns it.

- `location` — The location of the Node in 3D space as an ILocation. Any Apex objects that inherits form ILocation can be used to provide the location, including apex.Coordinate.
- `csys` — The ID of the coordinate system in which the location coordinates are defined.The coordinate system must exist and may be rectangular, cylindrical or spherical.

Returns: a Node at the provided location in this MeshBody.

#### `createNodes(locations: [float], csys: int = 0) -> apex.mesh.NodeCollection`
Creates and returns a series of Nodes at the provided locations in this MeshBody.

- `locations` — The locations of the Nodes in 3D space.The locations are defined using a repeating sequence of x, y and z coordinate values of float type. The first three values define the x, y and z coordinates of the first Node, the second three values define the coordinates of the second Node and so on.The List must contain a multiple of three entries otherwise the method will throw an exception.
- `csys` — The ID of the coordinate system in which the location coordinates are defined.The coordinate system must exist and may be rectangular, cylindrical or spherical.

Returns: a series of Nodes at the provided locations in this MeshBody.

#### `deleteElements(elementIDs: [int int int], elementIDsEncoded: str, removeUnreferencedNodes: bool) -> None`
Deletes elements, and optionally any resulting unreferenced Nodes, from this MeshBody.

- `elementIDs` — A List of the integer ID's of the elements to delete. If an ID is provided that does not exist in this MeshBody it will be silently ignored. This method supports two alternate ways to define the ID's of the elements to be deleted. This argument (List if integer IDs) and the alternate elementIDsEncoded argument that supports identification of the element using a run length encoded string. Only one or these two argument must be supplied otherwise the method will throw an exception.
- `elementIDsEncoded` — A run length encoded string defining the ID's of the elements to delete. Run length encoding enables ranges of consecutive ID;s to be defined in a compact form - "1, 3, 5, 7-1006, 1000-20000:2" If an ID is provided that does not exist in this MeshBody it will be silently ignored. This method supports two alternate ways to define the ID's of the elements to be deleted. This argument (run length encoded string) and the alternate elementIDs argument that supports identification of the elements using a List of Integer IDs. Only one or these two argument must be supplied otherwise the method will throw an exception
- `removeUnreferencedNodes` — An optional boolean argument to control deletion of any Nodes that become unreferenced after deleti0on of the element. If True (default), any Nodes that were originally referenced by any of the Elements that were deleted by this method that are no longer referenced by any other element or NodeTie will also be deleted. If False, no Nodes will be deleted.

- `deleteUnreferencedNodes() -> None` — Removes all Nodes in this MeshBody that are not referenced by any other Element or Node Tie in the Model.
- `disassociateFromGeometry() -> MeshBody` — Disassociates this MeshBody from Geometry if it is in fact associated. If the MeshBody is not associated to Geometry the method will simply return the MeshBody. If the MeshBody is associated to Geometry and the Geometry is referenced by Materials, Sections, Behaviors, Loads, Constraints, MeshIndependentTies or NodeTies, these associations will NOT be transferred from the Geometry to the MeshBody. (This capability will be added in a future release). NOTE : If the parent Geometry is referenced by a MeshDependentTie or a BeamSpan these associations will NOT be transferred to the MeshBody since Apex does not currently support MeshDependentTies or BeamSpans on orphan meshes. This limitation will be removed in a future Apex release.
#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports the contents of the MeshBody to a Nastran file. All Nodes and Elements in the Part, plus all Materials and Properties that are associated by the MeshBody will be exported. Only bulk data entries are exported when this method is called from the MeshBody class - to export Case (and other Nastran file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf"
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field)
- `exportAbstractions` — A Boolean quantity to control whether the exported data contains Apex Engineering Abstractions.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

#### `exportMarc(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, inputType: apex.attribute.MarcInputType = apex.attribute.MarcInputType.Dat, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, apexEngineeringAbstractions: bool = False) -> None`
Exports the contents of the MeshBody to a Marc file. All Nodes and Elements in the Part, plus all Materials and Properties that are associated by the MeshBody will be exported. Only bulk data entries are exported when this method is called from the MeshBody class - to export Case (and other Nastran file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf"
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field)
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hiearchical include files that mirrors the Assmbly/Part product structure, or as a singel Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the xport) to be written
- `inputType` — An enumeration to define which Marc input file format will be requested in the exported file. The default is DAT input file
- `renumberMethod` — Nastran jobs require Node, Element and other ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model and "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex
- `apexEngineeringAbstractions` — A Boolean quantity to control whether the exported data contains Apex Engineering Abstractions.

#### `getAssociatedGeometry() -> apex.geometry.GeometryBody`
returns the GeometryBody that this MeshBody is associated with or 'None' if the MeshBody is an orphan mesh and not associated to geometry.

Returns: the GeometryBody that this MeshBody is associated with.

#### `getElement(id: int, index: int) -> apex.mesh.Element`
Get the element in this MeshBody.

- `id` — the id of element
- `index` — the index of element

- `getElementConnectivities() -> {ElementTopologyNS.value:[int]}` — Returns a Dictionary containing the Element connectivity for every element, by element topology type, in this MeshBody. The element connectivity is defined using Node indices, NOT Node ID's. The Dictionary key is of type apex.mesh.ElementTopology and the value type is an array of integers. The Dictionary will contain an item for every element topology type in this MeshBody. The item key identifies the element topology type and the item value contains the element node indices for every element of this type in this MeshBody. The number of node indices in this array will be equal to the number of elements of this type in the mesh times the number of nodes per element for this element topology type. The connectivity for each element is provided in element index order - the same element index order used to recover the element ID's using the elementIDs property of this MeshBody.
- `getElementEdge(strElementEdge: str = "") -> apex.mesh.ElementEdge` — this method is used to search and return a specified ElementEdge by giving an element edge's combineID(ElementID + EdgeID) in string. Please note that the format of combineID is composed of ElementID and EdgeID, such as 10.1,
#### `getElementEdges(target: str = "") -> apex.mesh.ElementEdgeCollection`
Returns an ElementEdgeCollection of the element edges requested in the target argument.

- `target` — A text string that identifies the element edges. Each element edge is identifies using a two part key as follows, <ELEMENT_ID.EDGE_ID> For example "13.4" Multiple edges may be encoded into the string, each separated by a comma. For example "13.4, 15.2, 193.1" All element topologies in Apex support Edge ID's (Need a reference for this somewhere in the docs) An four node quad element is defined as follows, <ELEMENT_ID, N1, N2, N3, N4> For this element topology, Edge 1 links N1 and N2. Edge 2 links N2 and N3. Edge 3 links N3 and N4. Edge 4 links N4 and N1.

Returns: an ElementEdgeCollection of the element edges requested in the target argument.

#### `getElementFaces(target: {int int:[int]} = {}) -> apex.mesh.ElementFaceCollection`
get element face collection.

- `target` — dict of element index to its element face Ids.

Returns: element face collection. If the given sub face ids is empty, reurns all sub faces of the element.

#### `getElementFacesById(target: {str:[int int int]}) -> apex.mesh.ElementFaceCollection`
get element face collection.

- `target` — dict of element id to its element face Ids.

Returns: element face collection.

- `getElementIDs() -> {ElementTopologyNS.value:[int int int int]}` — Returns a Dictionary containing the Element ID's for every element, by element topology type, in this MeshBody. The Dictionary key is of type apex.mesh.ElementTopology and the value type is an array of integers. The Dictionary will contain an item for every element topology type in this MeshBody. The item key identifies the element topology type and the item value contains the element ids for every element of this type in this MeshBody. The element ID's are provided in Element index order - NOT element ID order. The order of Element ID's is the same order used to return the element Connectivity information form the elementConnectivities property of this MeshBody.
#### `getElements(ids: str, indices: str) -> apex.mesh.ElementCollection`
Get a collection of Element in this MeshBody.

- `ids` — the ids of elements which was ranged with "-" and separated with ","., e.g "9-9,50-52"
- `indices` — the indices of elements which was ranged with "-" and separated with ","., e.g "8-8,49-51"

Returns: a ElementCollection of the requested Elements in this MeshBody

#### `getNode(id: int, index: int) -> apex.mesh.Node`
Get the node in this MeshBody.

- `id` — the id of node
- `index` — the index of node

- `getNodeCoordinates() -> [float]` — Returns an array of node coordinates for every Node in this MeshBody. The coordinates are returned as 1D array of floats representing the x, y and z coordinates of each Node in this MeshBody in node index order [X1, Y1, Z1, X2, Y2, Z2, etc] where 1, 2 etc. represents the node index. This array will contain 3 times the number entries as there are Nodes in this MeshBody. The order of node coordinates in this array is the same as the order of the nodal ID's returned in the nodeIDs property of this MeshBody.
- `getNodeIDs() -> [int int int int]` — Returns an array of Node ID's for all Nodes in this MeshBody. The Node ID's are returned in Node index order, NOT in Node ID order. The order of Node ID's in this array is the same as the order of the nodal coordinates returned in the nodeCoordinates property.
#### `getNodes(ids: str, indices: str) -> apex.mesh.NodeCollection`
Get a collection of Node in this MeshBody.

- `ids` — the ids of nodes which was ranged with "-" and separated with ","., e.g "9-9,50-52"
- `indices` — the indices of nodes which was ranged with "-" and separated with ","., e.g "8-8,49-51"

Returns: a NodeCollection of the requested nodes in this MeshBody

- `getParent() -> apex.Part` — Get the parent Part for this MeshBody.
- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
#### `getSubMesh(id: int) -> apex.mesh.SubMesh`
returns the subMesh in this MeshBody.

- `id` — the id of subMesh

- `getSubMeshes() -> apex.mesh.SubMeshCollection` — returns a collection of SubMeshes from this MeshBody as a SubMeshCollection.
#### `setParent(parent: apex.Part) -> None`
Set a Part to be the new parent for this MeshBody.

- `parent` — to be assigned the new parent of this MeshBody

- `setReferenceSystem(refSysPair: ( apex.ILocation,apex.IOrientation )) -> None`
#### `update(color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this mesh body properties.

- `color` — updates the color of this mesh body. 3 vector(list) specifying the Red, Green, and Blue component of the color. Each value should be in the range 0-255.
- `renderStyle` — updates the render style of this mesh body. RenderStyle is the enumeration for the render style.
- `enableTransparency` — Boolean to enable setting transparency. Default: False.
- `transparencyLevel` — The Transparency Level. This is an integer representing the transparency value from 0 (No Transparency) to 100 (Completely Transparent). Any value specified less than 0 will be treated as 0. Any value greater than 100 will be treated as 100. This value is required if enableTransparency is set to True.


## `apex.mesh.MeshBodyCollection`  (extends `IPhysicalCollection`)
Iterable collection of MeshBodies, based on EntityCollection.

Methods:

- `MeshBodyCollection() -> None` — Construct a new MeshBodyCollection.
#### `appendList(meshBodyList: [apex.mesh.MeshBody]) -> None`
Add MeshBody from a list to the end of this collection.

- `meshBodyList` — list of MeshBody to add to the collection.

For example:


## `apex.mesh.Node`  (extends `Entity`, `IIdentifier`, `IPhysical`)
Node Class Object.
Properties: `analysisSystem`, `constraints`, `coordinates`, `displacementConstraints`, `elements`, `initialConditions`, `isInGlobal`, `loads`, `parent`, `referencedBy`, `referenceSystem`

Methods:

#### `assignAnalysisSystem(coordinateSystem: apex.construct.CoordinateSystem) -> bool`
assign a coordinate system as analysis coordinate system to the target Node.

- `coordinateSystem` — the coordinate system to be assigned to targets.

#### `getAnalysisSystem() -> apex.construct.CoordinateSystem`
The analysis coordinate system of the Node. Displacements, degrees of freedom,constraints, are defined in this system. Returns the analysis coordinate system associated with this node. The analysis coordinate system may be indirectly associated to the node through the parent Assembly, Part, GeometryBody, Cell, Face, Edge, Vertex, MeshBody or Elements. If no analysis coordiante system is associated with this node the method will return a None value.

Returns: the analysis coordinate system associated with this node.

#### `getConstraints() -> apex.EntityCollection`
Returns a collection of all Constraints that are applied to this Node. The Constraints may be applied directly to the Node or to its parent Surface, Face, Edge, Vertex, MeshBody or Part. If no Constraints are associated with the Node the method will return an empty EntityCollection.

Returns: a collection of all Constraints that are applied to this Node.

#### `getCoordinates() -> apex.Coordinate`
Returns the coordinates of this Node in 3D space as an apex.Coordinate.

Returns: the coordinates of this Node in 3D space as an apex.Coordinate.

#### `getDisplacementConstraints() -> apex.environment.DisplacementConstraintCollection`
Returns a collection of all Constraints that are applied to this Node. The Constraints may be applied directly to the Node or to its parent Surface, Face, Edge, Vertex, MeshBody or Part. If no Constraints are associated with the Node the method will return an empty ConstraintCollection.

Returns: a collection of all Constraints that are applied to this Node.

#### `getElements() -> ElementCollection`
Returns a collection of all Elements that reference this Node. The returned element collection does NOT include NodeTies that reference this Node.

Returns: a collection of all Elements that reference this Node.

- `getInitialConditions() -> apex.EntityCollection` — Returns a collection of all InitialConditions that are applied to this Node. The InitialConditions may be applied directly to the Node or to its parent GeometryBody, Face, Edge, Vertex, or MeshBody. If no InitialConditions are associated with the Node the method will return an empty EntityCollection. Apex only supports initialTemperature in this release.
#### `getIsInGlobal() -> bool`
Returns the True or False status if the node stored in global or not. If it is true, the 3D coordinates stores in global coordinate system. If it is false, the 3D coordinates stores in local coordinate system defined in referenceCoord.

Returns: the True or False status if the node stored in global or not.

#### `getLoads() -> apex.EntityCollection`
Returns a collection of all Loads that are applied to this Node. The Loads may be applied directly to the Node or to its parent GeometryBody, Face, Edge, Vertex, or MeshBody. If no Loads are associated with the Node the method will return an empty LoadCollection.

Returns: a collection of all Loads that are applied to this element.

#### `getParent() -> MeshBody`
Returns the parent MeshBody for this Node.

Returns: the parent MeshBody for this Node.

#### `getReferenceSystem() -> apex.construct.CoordinateSystem`
CoordinateSystem in which the coordinates of the node is defined. Returns the reference coordinate system of the node. If no reference coordiante system is defined in this node, return None.

Returns: the reference coordinate system of the node.

- `getReferencedBy() -> apex.EntityCollection` — returns a collection of all entities that directly Reference this Node
#### `update(coordinates: apex.Coordinate, referenceSystem: apex.construct.CoordinateSystem, analysisSystem: apex.construct.CoordinateSystem, isInGlobal: bool = False, enableReferenceSystem: bool, enableAnalysisSystem: bool) -> Node`
Updates the node including location, definition location coordinate system and analysis coordinate system assigned to the node.

- `coordinates` — The 3D location of the node to be updated.
- `referenceSystem` — Optional argument to define which Coordinate System in which the location of the Node are defined.
- `analysisSystem` — Optional argument to define analysis Coordinate System to be assign to the node.
- `isInGlobal` — Optional argument to convert the location from local to global coordinate system after creation. This argument is only available when "referenceSystem" is defined, otherwise it is silently ignored. If it is true, the system will store the node location in global coordinate system. If it is false, the system will store the node location in local coordinate system.
- `enableReferenceSystem` — Optional Boolean to enable or disable the reference system to be used. If it is omitted or true and "referenceSystem" argument is defined, the reference system will be used. If it is false, the reference system will not be used and will be removed if exists.
- `enableAnalysisSystem` — Optional Boolean to enable or disable the analysis system to be used. If it is omitted or true and "analysisSystem" argument is defined, the analysis system will be used. If it is false, the analysis system will not be used and will be removed if exists.

#### `updateCoordinates(coordinate: apex.ILocation) -> Node`
Updates the spatial coordinates of the Node.

- `coordinate` — The new coordinates of the Node. Any Apex object that implements ILocation (including apex.Coordinate) can be used to define the coordinates.

Returns: this Node.


## `apex.mesh.NodeCollection`  (extends `IPhysicalCollection`)
Iterable collection of Nodes, based on apex::EntityCollection.

Methods:

- `NodeCollection() -> None` — Construct a new NodeCollection.
#### `appendList(nodeList: [apex.mesh.Node]) -> None`
Add Node from a list to the end of this collection.

- `nodeList` — list of Node to add to the collection.

For example:


## `apex.mesh.NodeIdSet`  (extends `Entity`)
NodeIdSet Class Object. A set (list of unique) Node IDs .

## `apex.mesh.NodeIdSetCollection`  (extends `EntityCollection`)
Iterable collection of NodeIdSet objects, based on apex::EntityCollection.

Methods:

- `NodeIdSetCollection() -> None` — Construct a new NodeIdSetCollection.
#### `appendList(nodeIdSetList: [apex.mesh.NodeIdSet]) -> None`
Add NodeIdSet from a list to the end of this collection.

- `nodeIdSetList` — list of NodeIdSet to add to the collection.

For example:


## `apex.mesh.PointMesh`  (extends `MeshBody`)
PointMesh Class Object. extends Mesh Class Object.

Methods:

#### `update(name: str) -> None`
update name of this point mesh.

- `name` — Name of the new curve mesh.


## `apex.mesh.PointMeshCollection`  (extends `MeshBodyCollection`)
Iterable collection of Meshs, based on apex::EntityCollection.

Methods:

- `PointMeshCollection() -> None` — Construct a new PointMeshCollection.
#### `appendList(pointMeshList: [apex.mesh.PointMesh]) -> None`
Add PointMesh from a list to the end of this collection.

- `pointMeshList` — list of PointMesh to add to the collection.

For example:


## `apex.mesh.SeedPoint`  (extends `Entity`)
SeedPoint Class Object.
Properties: `cleanupTolerance`, `searchDistance`, `source`, `target`

Methods:

#### `getCleanupTolerance() -> float`
retrieve the cleanup tolerance of the Seed Point

Returns: the cleanup tolerance

#### `getSearchDistance() -> float`
retrieve the search distance of the Seed Point

Returns: the search distance

#### `getSource() -> apex.geometry.Point`
retrieve the source body of the Seed Point

Returns: the source body

#### `getTarget() -> apex.geometry.GeometryTopology`
retrieve the target edge/face of the Seed Point

Returns: the target edge/face


## `apex.mesh.SeedPointCollection`  (extends `EntityCollection`)
Iterable collection of SeedPoints, based on EntityCollection.

Methods:

- `SeedPointCollection() -> None` — Construct a new SeedPointCollection.
#### `appendList(seedPointList: [apex.mesh.SeedPoint]) -> None`
Add SeedPoint from a list to the end of this collection.

- `seedPointList` — list of SeedPoint to add to the collection.

For example:


## `apex.mesh.SolidMesh`  (extends `MeshBody`)
SolidMesh Class Object. extends MeshBody Class Object.
Properties: `approximateNumLayers`, `autoimprove`, `coarsenMeshInternally`, `collapseElementEdgesShorterThan`, `collapseShortElementEdges`, `coreType`, `createFeatureMeshes`, `createFeatureMeshOnChamfers`, `createFeatureMeshOnCylinders`, `createFeatureMeshOnFillets`, `createFeatureMeshOnQuadFaces`, `createFeatureMeshOnSemiCylinders`, `createFeatureMeshOnWashers`, `createLayeredMesh`, `createMinLayers`, `edgeLengthCollapseLimit`, `elementGeometryDeviationRatio`, `elementMinEdgeLengthRatio`, `elementOrder`, `faceMeshGrowthRatio`, `featureMeshtypes`, `gradeFactor`, `growFaceMeshSize`, `ignoreBadEdges`, `interiorCoarseningFactor`, `meshFlow`, `meshSize`, `meshType`, `projectMidsideNodesToGeometry`, `refineMeshUsingCurvature`, `skinType`, `target`, `thinSectionThreshold`, `useMeshFlowOptimization`

Methods:

- `getApproximateNumLayers() -> float` — return the value of approximate layer number.
- `getAutoimprove() -> bool` — boolean property that indicates whether automatic element quality improvement was performed on this mesh when it was created.
- `getCoarsenMeshInternally() -> bool` — return flag: enable/disable the internalCoarsen option.
- `getCollapseShortElementEdges() -> bool` — return flag: enable/disable the collapseShortElementEdges option.
- `getCoreType() -> apex.mesh.HybridCoreType` — return the value of hybrid mesh core type.
- `getCreateFeatureMeshOnChamfers() -> bool` — return flag: enable/disable the create Chamfer option.
- `getCreateFeatureMeshOnCylinders() -> bool` — return flag: enable/disable the create Cylinder option.
- `getCreateFeatureMeshOnFillets() -> bool` — return flag: enable/disable the create Fillet option.
- `getCreateFeatureMeshOnQuadFaces() -> bool` — return flag: enable/disable the create QuadFaces option.
- `getCreateFeatureMeshOnSemiCylinders() -> bool` — return flag: enable/disable the create SemiCylinder option.
- `getCreateFeatureMeshOnWashers() -> bool` — return flag: enable/disable the create Washer option.
- `getCreateFeatureMeshes() -> bool` — return flag: enable/disable the create FeatureMeshes option.
- `getCreateLayeredMesh() -> bool` — return flag: enable/disable the create QuadFaces option.
- `getCreateMinLayers() -> bool` — return flag: enable/disable the create mininal layers option.
- `getEdgeLengthCollapseLimit() -> float` — return the value of collapseShortElementEdges.
- `getElementGeometryDeviationRatio() -> float` — return the value of elementGeometryDeviationRatio.
- `getElementMinEdgeLengthRatio() -> float` — return the value of elementMinEdgeLengthRatio.
- `getElementOrder() -> apex.mesh.ElementOrder` — return the elementOrder of the solid mesh.
- `getFaceMeshGrowthRatio() -> float` — return the value of face mesh growth size.
- `getFeatureMeshtypes() -> [apex.mesh.FeatureMeshTypeNS.value]` — return optional argument controlling the types of feature meshes that this method will attempt to create.
- `getGrowFaceMeshSize() -> bool` — return flag: enable/disable the grow face mesh size option.
- `getIgnoreBadEdges() -> bool` — return flag: enable/disable the ignoreBadEdges option.
- `getInteriorCoarseningFactor() -> float` — return the value of interiorCoarseningFactor.
- `getMeshFlow() -> apex.mesh.MeshFlow` — return the type of MeshFlow to use for skin surface mesh in the SolidMesh.
- `getMeshSize() -> float` — return the meshsize of the solid mesh.
- `getMeshType() -> apex.mesh.SolidMeshElementShape` — return the meshType of the solid mesh.
- `getProjectMidsideNodesToGeometry() -> bool` — return flag: enable/disable the project middle nodes to geometry option.
- `getRefineMeshUsingCurvature() -> bool` — return flag: enable/disable the curvature refinement option.
- `getSkinType() -> apex.mesh.HybridSkinType` — return the value of hybrid mesh skin face type.
- `getTarget() -> apex.geometry.Solid` — return the Solid which are meshed.
- `getThinSectionThreshold() -> float` — return the value of thinSectionThreshold.
- `getUseMeshFlowOptimization() -> bool` — return flag: enable/disable enhance mesh flow to improve quality.
#### `update(name: str, meshSize: float, meshType: apex.mesh.SolidMeshElementShape, elementOrder: apex.mesh.ElementOrder, refineMeshUsingCurvature: apex.ApexBool, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, autoimprove: apex.ApexBool, growFaceMeshSize: apex.ApexBool, faceMeshGrowthRatio: float, coarsenMeshInternally: apex.ApexBool, gradeFactor: float, interiorCoarseningFactor: float, ignoreBadEdges: apex.ApexBool, collapseShortElementEdges: apex.ApexBool, collapseElementEdgesShorterThan: float, edgeLengthCollapseLimit: float, createFeatureMeshes: apex.ApexBool, featureMeshTypes: [apex.mesh.FeatureMeshType], createFeatureMeshOnFillets: apex.ApexBool, createFeatureMeshOnChamfers: apex.ApexBool, createFeatureMeshOnCylinders: apex.ApexBool, createFeatureMeshOnSemiCylinders: apex.ApexBool, createFeatureMeshOnWashers: apex.ApexBool, createFeatureMeshOnQuadFaces: apex.ApexBool, createLayeredMesh: apex.ApexBool, thinSectionThreshold: float, numLayers: int, projectMidsideNodesToGeometry: apex.ApexBool, createMinLayers: bool, approximateNumLayers: float, coreType: HybridCoreType, skinType: HybridSkinType, useMeshFlowOptimization: apex.ApexBool, meshFlow: apex.mesh.MeshFlow) -> apex.mesh.ZResultCreateSolidMesh`
Updates one or more properties of this SolidMesh. All modifiable properties of the SolidMesh are supported as optional arguments and multiple properties may be updated in a single call. Any properties not included in the argument list are unchanged by this method.

- `name` — An optional name for the created mesh. If multiple meshes are created this name will be used for the first mesh created and each subsequent mesh will use this name as a prefix to which a unique integer will be concatenated to ensure name uniqueness. For example with name defined to be 'My Mesh' the first mesh will be named "My Mesh", and any subsequent meshes will be named 'My Mesh 1', 'My mesh 2' etc.
- `meshSize` — An optional mesh size. The mesher will attempt to create tetrahedral elements with lengths equal to this value. Note that existing mesh seeds, short geometry edges, curved geometry or other arguments provided on this method may cause elements sizes smaller or larger than this target to be created. meshSize represents a Length quantity and must be defined in the units of Length in the active script units system.
- `meshType` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. This method can only create meshes containing tetrahedral elements therefore this argument is no longer required.
- `elementOrder` — optional enumeration defining the order of the elements to be created for the SolidMesh. apex.mesh.ElementOrder.Quadratic (Default) will cause creation of tetrahedral elements with mid edge nodes apex.mesh.ElementOrder.Linear will cause creation of tetrahedral elements without mid edge nodes
- `refineMeshUsingCurvature` — Optional boolean argument (Default = True) that controls whether the method will locally refine the mesh in regions where the geometry is curved or not. If True (Default) element faces on the surface of the mesh will be refined in areas of geometry curvature to ensure a minimum deviation of the element from the geometry (The amount of deviation enforced is controlled by the elementGeometryDeviationRatio argument). If False, no local refinement will be applied
- `elementGeometryDeviationRatio` — An optional argument (Default = 0.1) defining how much spatial deviation is allowed between the mesh and the geometry in areas of geometry curvature. This quantity is expressed as the ratio of two lengths. The numerator length is the maximum distance from any point on the element edge to the geometry edge. The denominator length is the element edge length. The default value of 0.1 will ensure that the maximum distance between any point on the element edge and the associated geometry edge will be no more than 10% of the element edge length. This argument is ignored unless refineMeshUsingCurvature is enabled.
- `elementMinEdgeLengthRatio` — optional argument (Default = 0.2) that controls the minimum element edge length when curvature based mesh refinement is enabled The quantity represents the ratio of the element edge length to the global element size. The default value of 0.2 will ensure that the curvature refinement algorithm will not create elements with edges that are less than 20% of the global element size. Note that this meshing parameter has priority over the elementGeometryDeviationRatio argument and may cause elements to be created that deviate from the geometry by more than the distance implied by elementGeometryDeviationRatio.
- `autoimprove` — optional boolean argument (Default = True) that controls whether this method will perform additional mesh modification steps after initial meshing to improve the mesh quality. If enabled (True), the initial mesh will be modified to ensure that all elements in the mesh satisfy the following element quality metrics Aspect Ratio Jacobian The values of these element quality metrics form the ???? are used.
- `growFaceMeshSize` — Flag to enable the face mesh growth.
- `faceMeshGrowthRatio` — This property will be a single floating point number between 0 and 1 that defines the size ratio of adjacent elements. A growth factor of 0 is interpreted to mean that no change in size will be supported between adjacent elements. A growth factor of 1 is interpreted to mean that element size may double between adjacent element faces on the free surface of the mesh. A suitable default value will be determined during development of the capability based on testing of representative models.
- `coarsenMeshInternally` — optional boolean argument that controls whether the method will attempt to create elements larger than meshSize in interior regions of the mesh. If True (Default), the method will attempt to create elements with edges longer than meshSize in interior regions of the mesh, away from the free surface. The rate at which element sizes grow with distance from the free surface is controlled by the gradeFactor argument.
- `gradeFactor` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the equivalent interiorCoarseningFactor instead optional argument (Default = 0.1) that controls how rapidly element sizes will increase from the free surface of the mesh to the interior. This argument is silently ignored unless coarsenMeshInternally is enabled. The value represents the change in element size between adjacent elements in the direction from the free surface of the mesh towards the interior. The default value of 0.1 will cause adjacent elements to be no more than 10% larger then their immediate neighbor.
- `interiorCoarseningFactor` — optional argument (Default = 0.1) that controls how rapidly element sizes will increase from the free surface of the mesh to the interior. This argument is silently ignored unless coarsenMeshInternally is enabled. The value represents the change in element size between adjacent elements in the direction from the free surface of the mesh towards the interior. The default value of 0.1 will cause adjacent elements to be no more than 10% larger then their immediate neighbor.
- `ignoreBadEdges` — optional boolean argument (Default = True) that controls whether or not this method will create element edges on ALL geometry Edges, including very short or poorly shaped edges) or not. If True (Default), the method will ignore very short or poorly shaped geometry edges. NOTE : If the Edge is referenced by a Load or a Constraint or some other simulation attribute it will ALWAYS be meshed, irrespective of the value of this argument to ensure that the Load/Constrain is included in the simulation.
- `collapseShortElementEdges` — optional boolean argument (Default = False) that controls whether or not this method will collapse element edges that are shorter than a predefined minimum length (specified by the collapseElementEdgesShorterThan argument). If False (Default) the mesher will create elements with no lower bound limit on edge length. If True the method will collapse element edges shorter than the associate collapseElementEdgesShorterThan value.
- `collapseElementEdgesShorterThan` — THIS ARGUMENT IS DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. Use the equivalent ??? argument instead. an optional argument defining the minimum element edge length that will be created by this method, This argument is silently ignored unless the associated collaspeShortElementEdges argument is enabled (True) collapseElementEdgesShorterThan represents a Length quantity and must be provided in the units of Length in the active script unit system.
- `edgeLengthCollapseLimit` — optional argument defining the minimum element edge length that will be created by this method, This argument is silently ignored unless the associated collaspeShortElementEdges argument is enabled (True) collapseElementEdgesShorterThan represents a Length quantity and must be provided in the units of Length in the active script unit system.
- `createFeatureMeshes` — optional boolean argument (Default = False) that controls whether or not this method will cause creation of feature meshes around identified geometric features. If False (Default), no feature meshes will be created If True, Feature meshes will be created around the set of feature types activated by the argument.
- `featureMeshTypes` — optional argument controlling the types of feature meshes that this method will attempt to create. This argument is silently ignored unless createFeatureMeshes is enabled. featureMeshTypes is List of apex.mesh.FeatureMeshType enumerations. Feature meshes will be created for each apex.mesh.FeatureMeshType included in the List if an underlying geometry feature of that type is identified. If omitted and createFeatureMeshes is enabled, the method will attempt to create Feature meshes for every supported FeatureMeshType.
- `createFeatureMeshOnFillets` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the optional featuremeshsettings argument instead optional argument (Default - True) controlling whether or not feature meshes will be created around geometry features that are identified as Fillets. If True (Default) fillet feature meshes will be created around all geometry faces that are identified as fillets. The parameters of the fillet feature mesh will be determined by the Fillet Feature Mesh settings in the active Feature Mesh Settings.
- `createFeatureMeshOnChamfers` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the optional featuremeshsettings argument instead optional argument (Default - True) controlling whether or not feature meshes will be created around geometry features that are identified as Chamfers. If True (Default) chanfer feature meshes will be created around all geometry faces that are identified as chamfers. The parameters of the chamfer feature mesh will be determined by the CHamfer Feature Mesh settings in the active Feature Mesh Settings.
- `createFeatureMeshOnCylinders` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the optional featuremeshsettings argument instead optional argument (Default - True) controlling whether or not feature meshes will be created around geometry features that are identified as Cylinders. If True (Default) cylinder feature meshes will be created around all geometry faces that are identified as cylinders. The parameters of the cylinder feature mesh will be determined by the Cylinder Feature Mesh settings in the active Feature Mesh Settings.
- `createFeatureMeshOnSemiCylinders` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the optional featuremeshsettings argument instead optional argument (Default - True) controlling whether or not feature meshes will be created around geometry features that are identified as Semi-clinders. If True (Default) semi-sylinder feature meshes will be created around all geometry faces that are identified as semi-cylinders. The parameters of the semi-cylinder feature mesh will be determined by the Semi-Cylinder Feature Mesh settings in the active Feature Mesh Settings.
- `createFeatureMeshOnWashers` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the optional featuremeshsettings argument instead optional argument (Default - True) controlling whether or not feature meshes will be created around geometry features that are identified as Washers. If True (Default) washer feature meshes will be created around all geometry faces that are identified as washers. The parameters of the washer feature mesh will be determined by the Washer Feature Mesh settings in the active Feature Mesh Settings.
- `createFeatureMeshOnQuadFaces` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the optional featuremeshsettings argument instead optional argument (Default - True) controlling whether or not feature meshes will be created around geometry features that are identified as Quad Faces. If True, quad face feature meshes will be created around all geometry faces that are identified as quad faces. The parameters of the quad face feature mesh will be determined by the Quad Face Feature Mesh settings in the active Feature Mesh Settings.
- `createLayeredMesh` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. optional argument controlling whether or not a layered mesh will be created in areas of the solid where the wall thickness or "section" is "thin". If True, the method will attempt to create regular layers of elements in sections of the solid geometry model that are identified to be thin. Additional arguments (thinSectionThreshold, numLayers) are provided to control which regions are considered to be thin and the number of element layers crated in these regions.
- `thinSectionThreshold` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. optional argument defining a characteristic thickness to identify thin sections of the solid geometry. Regions of the model with face pairs that are approximately parallel and separated by a distance no greater than this value are considered to represent a thin section and will be targeted for layered meshing thinSectionThreshold represents a Length quantity and must be provided in the units of Length from the active script unit system.
- `numLayers` — THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Defines the number of layers of elements to create in areas of the model where the section is thinner than the dimension defined by "thinSectionThreshold".
- `projectMidsideNodesToGeometry` — optional Boolean argument (default = True) that specifies whether the mid-side nodes of higher order solid elements will be projected onto the target Geometry or not. By default (True), the mid-side nodes of all higher order solid elements will be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.
- `createMinLayers` — This parameter when on, will set the approximate minimum number of layers of the body. The local density of thin areas as define by meshSize/numLayers will be adjusted to facilitate the requested number of layers. Giving a mesh size of 40mm, and numLayers set to 3, then any area thinner than 13.33 will have the mesh size locally adjusted smaller. Since numLayers is a real number, finer adjustments can be made as needed.
- `approximateNumLayers` — default is 2.0. This is an approximate value. it might be required that 2.1 or 2.2 be used to achieve the desired result in all locations. The large the approximate number of layers, the more instable the result is likely to be, so adjustments up or down may be needed.
- `coreType` — Enumeration defining the core type has two types of hex dominant available in the Distene mesher API, and one for just tets. Options are: 1. Tet 2. Hex 3. HexPrismatic.
- `skinType` — Enumeration defining the skin can be auto-generated using quad dominant or tria. This only applies to unmeshed faces of the solid or cell. Ideally, we should use the best quality quad and tria mesh, and to day that is the new Crossfield and Asterisk field meshers.
- `useMeshFlowOptimization` — Enhance mesh flow to improve quality. Options are: True, Enable mesh flow. False, Disable mesh flow.
- `meshFlow` — Enumeration defining what type of MeshFlow to use for the skin surface mesh. Options are: 1, MeshFlow.Grid, Internal pattern forms grid for flat surfaces. 2, MeshFlow.FollowEdges, Internal pattern flows with edges for flat surfaces.


## `apex.mesh.SolidMeshCollection`  (extends `MeshBodyCollection`)
Iterable collection of Meshs, based on apex::EntityCollection.

Methods:

- `SolidMeshCollection() -> None` — Construct a new SolidMeshCollection.
#### `appendList(solidMeshList: [apex.mesh.SolidMesh]) -> None`
Add SolidMesh from a list to the end of this collection.

- `solidMeshList` — list of SolidMesh to add to the collection.

For example:


## `apex.mesh.SubMesh`  (extends `Entity`, `IIdentifier`, `IPhysical`, `IUserAttributes`)
Base class representing a region of a MeshBody. Submesh is specialized to Submesh1D, Submesh2D and Submesh3D. The topology of MeshBodies that are associated with GeometryBodies reflect the topology of the GeometryBody. A Geometry Solid is composed of one or more Cells and the mesh that is associated with this Solid will compose a corresponding Submesh (Submesh3D) for each Cells. The same pattern is supported for Surfaces (1 Submesh2D for each Surface Face of the Surface) and Curves (1 Submesh1D for each Edge of the Curve)
Properties: `elements`, `nodes`, `parent`

Methods:

#### `asEntity() -> apex.Entity`
return the (base) Entity Object of this SubMesh.

Returns: this SubMesh Entity object

#### `getElements() -> apex.mesh.ElementCollection`
returns a collection of Elements composed by this submesh.

Returns: ElementCollection

- `getIndex() -> int` — SubMesh only has id, but does not have index. Index of zero will be returned always.
#### `getNodes() -> apex.mesh.NodeCollection`
returns a collection of Nodes referenced by this submesh.

Returns: NodeCollection

#### `getParent() -> apex.mesh.MeshBody`
returns the MeshBody that composes this submesh.

Returns: MeshBody Entity object


## `apex.mesh.SubMesh0D`  (extends `SubMesh`)
Class representing regions of a PointMesh. extends SubMesh Class Object.

Methods:

- `getIndex() -> int` — SubMesh only has id, but does not have index. Index of zero will be returned always.

## `apex.mesh.SubMesh1D`  (extends `SubMesh`)
Class representing regions of a CurveMesh. The topology of CurveMeshes that are associated with geometry Curves reflect the topology of the Curve. A Curve is composed of one or more Edges and the CurveMesh that is associated with this Curve will compose a corresponding Submesh1D for each Edge. extends SubMesh Class Object.
Properties: `edge`

Methods:

#### `getEdge() -> apex.geometry.Edge`
returns the Edge associated with this Submesh1D or 'None' if the Submesh is not associated to geometry (orphan mesh).

Returns: the Edge associated with this Submesh1D.

- `getIndex() -> int` — SubMesh only has id, but does not have index. Index of zero will be returned always.

## `apex.mesh.SubMesh2D`  (extends `SubMesh`)
Class representing regions of a SurfaceMesh. The topology of SurfaceMeshes that are associated with geometry Surfaces reflect the topology of the Surface. A Surface is composed of one or more Faces and the SurfaceMesh that is associated with this Surface will compose a corresponding Submesh2D for each Surface. extends SubMesh Class Object.
Properties: `face`

Methods:

#### `getFace() -> apex.geometry.Face`
returns the Face associated with this Submesh2D or 'None' if the submesh is not associated to geometry (orphan mesh).

Returns: the Face associated with this Submesh2D.

- `getIndex() -> int` — SubMesh only has id, but does not have index. Index of zero will be returned always.

## `apex.mesh.SubMesh3D`  (extends `SubMesh`)
Class representing regions of a SolidMesh or HexMesh. The topology of SolidMeshes and HexMeshes that are associated with geometry Solids reflect the topology of the Solid. A Solid is composed of one or more Cells and the SolidMesh or HexMesh that is associated with this Solid will compose a corresponding Submesh3D for each Cell. extends SubMesh Class Object.
Properties: `cell`

Methods:

#### `getCell() -> apex.geometry.Cell`
returns the Cell associated with this Submesh3D or 'None' if the submesh is not associated to geometry (orphan mesh).

Returns: the Cell associated with this Submesh3D.

- `getIndex() -> int` — SubMesh only has id, but does not have index. Index of zero will be returned always.

## `apex.mesh.SubMeshCollection`  (extends `EntityCollection`)
Iterable collection of SubMesh, based on EntityCollection.

Methods:

- `SubMeshCollection() -> None` — Construct a new SubMeshCollection.
#### `appendList(subMeshList: [apex.mesh.SubMesh]) -> None`
Add SubMesh from a list to the end of this collection.

- `subMeshList` — list of SubMesh to add to the collection.

For example:


## `apex.mesh.SurfaceMesh`  (extends `MeshBody`)
SurfaceMesh Class Object. extends MeshBody Class Object.
Properties: `applyTriaReduction`, `createFeatureMeshes`, `curvatureRefinement`, `elementGeometryDeviationRatio`, `elementMinEdgeLengthRatio`, `elementOrder`, `faceMeshGrowthRatio`, `featureMeshtypes`, `growFaceMeshSize`, `mappedMeshDominanceLevel`, `meshFlow`, `meshMethod`, `meshSize`, `meshType`, `projectMidsideNodesToGeometry`, `target`, `triaReductionStrength`, `useMeshFlowOptimization`

Methods:

- `getApplyTriaReduction() -> bool` — return flag: enable/disable tria reduction process.
- `getCreateFeatureMeshes() -> bool` — return flag: enable/disable the UseMeshFlowOptimization option.
- `getCurvatureRefinement() -> bool` — return flag: enable/disable the curvature refinement option.
- `getElementGeometryDeviationRatio() -> float` — return the value of elementGeometryDeviationRatio.
- `getElementMinEdgeLengthRatio() -> float` — return the value of elementMinEdgeLengthRatio.
- `getElementOrder() -> apex.mesh.ElementOrder` — return the elementOrder of the surface mesh.
- `getFaceMeshGrowthRatio() -> float` — return the value of face mesh growth size.
- `getFeatureMeshtypes() -> [apex.mesh.FeatureMeshTypeNS.value]` — return optional argument controlling the types of feature meshes that this method will attempt to create.
- `getGrowFaceMeshSize() -> bool` — return flag: enable/disable the grow face mesh size option.
- `getMappedMeshDominanceLevel() -> signed int int` — return the value of mappedMeshDominanceLevel.
- `getMeshFlow() -> apex.mesh.MeshFlow` — return the type of MeshFlow to use in the SurfaceMesh.
- `getMeshMethod() -> apex.mesh.SurfaceMeshMethod` — return the meshMethod of the surface mesh.
- `getMeshSize() -> float` — return the meshsize of the surface mesh.
- `getMeshType() -> apex.mesh.SurfaceMeshElementShape` — return the meshType of the surface mesh.
- `getProjectMidsideNodesToGeometry() -> bool` — return flag: enable/disable the project middle nodes to geometry option.
- `getTarget() -> apex.EntityCollection` — return the list of faces which are meshed.
- `getTriaReductionStrength() -> signed int int` — return the value of triaReductionStrength.
- `getUseMeshFlowOptimization() -> bool` — return flag: enable/disable enhance mesh flow to improve quality.
#### `update(name: str, meshSize: float, meshType: apex.mesh.SurfaceMeshElementShape, meshMethod: apex.mesh.SurfaceMeshMethod, mappedMeshDominanceLevel: int, elementOrder: apex.mesh.ElementOrder, meshUsingPrincipalAxes: apex.ApexBool, allQuadBoundary: apex.ApexBool, applyTriaReduction: apex.ApexBool, triaReductionStrength: int, refineMeshUsingCurvature: apex.ApexBool, curvatureType: apex.mesh.CurvatureType, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, proximityRefinement: apex.ApexBool, growFaceMeshSize: apex.ApexBool, faceMeshGrowthRatio: float, createFeatureMeshes: apex.ApexBool, featureMeshTypes: [apex.mesh.FeatureMeshType], createFeatureMeshOnFillets: apex.ApexBool, createFeatureMeshOnChamfers: apex.ApexBool, createFeatureMeshOnWashers: apex.ApexBool, createFeatureMeshOnArbitraryHoles: apex.ApexBool, createFeatureMeshOnQuadFaces: apex.ApexBool, projectMidsideNodesToGeometry: apex.ApexBool, useMeshFlowOptimization: apex.ApexBool, meshFlow: apex.mesh.MeshFlow) -> apex.mesh.ZResultCreateSurfaceMesh`
update one or more of this surface mesh properties.

- `name` — Name of the new surface mesh.
- `meshSize` — Specify the Global Edge Length to use in meshing the selected geometry.
- `meshType` — Enumeration defining what type of elements can be included in the create SurfaceMesh. Options are: 1. SurfaceMeshElementShape.Mixed 2. SurfaceMeshElementShape.Quadrilateral 3. SurfaceMeshElementShape.Triangle
- `meshMethod` — Enumeration defining which mesh algorithm to use to create the SurfaceMesh. Options are: 1. SurfaceMeshMethod.Auto 2. SurfaceMeshMethod.Pave 3. SurfaceMeshMethod.Mapped
- `mappedMeshDominanceLevel` — Value to control how aggressively the algorithm will be in forcing creation of a mapped mesh. Varies from 1 (least aggressive) to 5 (most aggressive). Must be defined if meshMethod is SurfaceMeshMethod.Mapped.
- `elementOrder` — Enumeration defining the order of the elements to be created for the SurfaceMesh Options are: 1. MeshOrder.Linear 2. MeshOrder.Quadratic.
- `meshUsingPrincipalAxes` — DEPRECATION NOTICE: This parameter has been deprecated and we intend to remove it in the next Apex release. Users are advised to transition their code to use the new extended option "useMeshFlowOptimization" as quickly as possible to avoid future problems. It was used to enable/disable the principal axis guided meshing algorithm causing the mesher to attempt to create elements with edges aligned wit the principal axes of the target faces.
- `allQuadBoundary` — Flag to enable All Quad Boundary Mesh option of the surface meshing algorithm.
- `applyTriaReduction` — turns on tria reduction process. This process will attempted to remove tria from a mesh found in specific patterns. Not all triangle elements can be removed without reducing mesh quality too far. This feature is ignored if growFaceMeshSize or refineMeshUsing Curvature is on. In addition, higher order elements are not currently supported. If higher order elements are needed, use reduction first, then switch mesh to higher order by double clicking on the mesh body in the Model Browser, or from API, use update() to change elementOrder.
- `triaReductionStrength` — This parameter, integer 1 to 5, with default set to 2, will control how aggressively triangle elements will be removed. if the input is 0, then no elements will be removed, all values over 5 will behave the same as 5. At each level between 1 and 5, the element size deviation from the specified mesh size, and the allowable quad distortion will be more permissive. The result will be that more tria can be removed the higher the level, but with the consequence of reduced quality mesh.
- `refineMeshUsingCurvature` — Flag to enable the curvature refinement option of the surface meshing algorithm.
- `curvatureType` — Enumeration defining curvature type.
- `elementGeometryDeviationRatio` — Value to control the maximum deviation between and element edge and it's correpsonding geometry edge during curvature refinement. Takes a value between 0.0 and 1.0. *Must be defined if enableCurvatureRefinement is True, otherwise it is ignored.
- `elementMinEdgeLengthRatio` — Value to control the minimum element edge length relative to the global element edge length during curvature refinement. *Must be defined if enableCurvatureRefinement is True, otherwise it is ignored.
- `proximityRefinement` — Flag to enable proximity mesh refinement.
- `growFaceMeshSize` — Flag to enable the face mesh growth.
- `faceMeshGrowthRatio` — This property will be a single floating point number between 0 and 1 that defines the size ratio of adjacent elements. A growth factor of 0 is interpreted to mean that no change in size will be supported between adjacent elements. A growth factor of 1 is interpreted to mean that element size may double between adjacent element faces on the free surface of the mesh. A suitable default value will be determined during development of the capability based on testing of representative models.
- `createFeatureMeshes` — optional boolean argument (Default = False) that controls whether or not this method will cause creation of feature meshes around identified geometric features. If False (Default), no feature meshes will be created If True, Feature meshes will be created around the set of feature types activated by the argument.
- `featureMeshTypes` — optional argument controlling the types of feature meshes that this method will attempt to create. This argument is silently ignored unless createFeatureMeshes is enabled. featureMeshTypes is List of apex.mesh.FeatureMeshType enumerations. Feature meshes will be created for each apex.mesh.FeatureMeshType included in the List if an underlying geometry feature of that type is identified. If omitted and createFeatureMeshes is enabled, the method will attempt to create Feature meshes for every supported FeatureMeshType.
- `createFeatureMeshOnFillets` — Enables the fillet feature mesh option in surface meshing.
- `createFeatureMeshOnChamfers` — Enables the chamfer feature mesh option in surface meshing.
- `createFeatureMeshOnWashers` — Enables the washer feature mesh option in surface meshing.
- `createFeatureMeshOnArbitraryHoles` — optional boolean argument to request the creation of arbitrary hole feature meshes during surface meshing. When enabled, the mesher will create feature meshes around geometry features that are identified as arbitrary holes. The parameters of the arbitrary hole feature mesh will be defined using the values defined in the active FeatureMeshRuleSet. When disabled, no arbitrary hole feature meshes will be created.
- `createFeatureMeshOnQuadFaces` — Enables the four sided face feature mesh option in surface meshing.
- `projectMidsideNodesToGeometry` — optional Boolean argument (default = True) that specifies whether the mid-side nodes of higher order shell elements will be projected onto the target Geometry or not. By default (True), the mid-side nodes of all higher order shell elements will be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.
- `useMeshFlowOptimization` — Enhance mesh flow to improve quality. Options are: True, Enable mesh flow. False, Disable mesh flow.
- `meshFlow` — Enumeration defining what type of MeshFlow to use in the SurfaceMesh. Options are: 1, MeshFlow.Grid, Internal pattern forms grid for flat surfaces. 2, MeshFlow.FollowEdges, Internal pattern flows with edges for flat surfaces.


## `apex.mesh.SurfaceMeshCollection`  (extends `MeshBodyCollection`)
Iterable collection of Meshs, based on apex::EntityCollection.

Methods:

- `SurfaceMeshCollection() -> None` — Construct a new SurfaceMeshCollection.
#### `appendList(surfaceMeshList: [apex.mesh.SurfaceMesh]) -> None`
Add SurfaceMesh from a list to the end of this collection.

- `surfaceMeshList` — list of SurfaceMesh to add to the collection.

For example:


## `apex.mesh.ZRenumberByOffset`
Properties: `maxCoordinateSystemId`, `maxElementId`, `maxNodeId`, `minCoordinateSystemId`, `minElementId`, `minNodeId`

Methods:

- `ZRenumberByOffset() -> None`
#### `getMaxCoordinateSystemId(: None) -> int int int`
return the largest Coordinate System ID that was assigned during renumbering

Returns: The max Coordinate System ID

#### `getMaxElementId(: None) -> int int int`
return the max element id

Returns: The max element id

#### `getMaxNodeId(: None) -> int int int`
return the max node id

Returns: The max node id

#### `getMinCoordinateSystemId(: None) -> int int int`
return the smallest Coordinate System ID that was assigned during renumbering

Returns: The min Coordinate System ID

#### `getMinElementId(: None) -> int int int`
return the min element id

Returns: The min element id

#### `getMinNodeId(: None) -> int int int`
return the min node id

Returns: The min node id


## `apex.mesh.ZRenumberByStartId`
Properties: `endCoordinateSystemId`, `endElementId`, `endNodeId`

Methods:

- `ZRenumberByStartId() -> None`
#### `getEndCoordinateSystemId(: None) -> int int int`
return the highest Coordinate System ID that was assigned during the renumber operation

Returns: The end Coordinate System ID

#### `getEndElementId(: None) -> int int int`
return the end element id

Returns: The end element id

#### `getEndNodeId(: None) -> int int int`
return the end node id

Returns: The end node id


## `apex.mesh.ZResultCreateCurveMesh`  (extends `ZResultCreateMesh`)
Properties: `curveMeshes`

Methods:

#### `getCurveMeshes(: None) -> CurveMeshCollection`
return a Collection of CurveMeshes that were succesfully created

Returns: Collection of CurveMeshes that were succesfully created


## `apex.mesh.ZResultCreateHexMesh`  (extends `ZResultCreateMesh`)
Properties: `hexMeshes`

Methods:

#### `getHexMeshes(: None) -> HexMeshCollection`
return a Collection of HexMeshes that were succesfully created

Returns: Collection of HexMeshes that were succesfully created


## `apex.mesh.ZResultCreateMesh`
Properties: `numElementsCreated`, `unmeshedGeometry`

Methods:

#### `getNumElementsCreated(: None) -> int`
return The total number of elements created

Returns: The total number of elements created

#### `getUnmeshedGeometry(: None) -> apex.EntityCollection`
return a Collection of Geometry (Surfaces/Solids/Faces) that failed to mesh

Returns: Collection of Geometry (Surfaces/Solids/Faces) that failed to mesh


## `apex.mesh.ZResultCreateSolidMesh`  (extends `ZResultCreateMesh`)
Properties: `solidMeshes`

Methods:

#### `getSolidMeshes(: None) -> SolidMeshCollection`
return a Collection of SolidMeshes that were succesfully created

Returns: Collection of SolidMeshes that were succesfully created


## `apex.mesh.ZResultCreateSurfaceMesh`  (extends `ZResultCreateMesh`)
Properties: `surfaceMeshes`

Methods:

#### `getSurfaceMeshes(: None) -> SurfaceMeshCollection`
return a Collection of SurfaceMeshes that were succesfully created

Returns: Collection of SurfaceMeshes that were succesfully created


