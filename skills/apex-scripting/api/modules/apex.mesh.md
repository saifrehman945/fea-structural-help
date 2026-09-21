# apex.mesh

(apex.mesh module) mesh (SurfaceMesh, SolidMesh, CurveMesh, HexMesh) creation and editing functions.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.mesh.BiasType`: `EndBias`, `MiddleBias`
  - Type of EdgeSeed bias. EndBias - The seed points will be biased towards one end of the target. MiddleBias - The seed points will be biased towards the middle of the target

`apex.mesh.ConflictResolveOption`: `AllowDuplicateIds`, `AutomaticResolve`
  - Conflict Resolve Options in Apex. DEPRECATED: PLEASE USE THE NEW apex.mesh.IDConflictResolveMethod ENUMERATION INSTEAD

`apex.mesh.CurvatureType`: `EdgeOnly`, `EdgeAndFace`
  - Curvature refinement type

`apex.mesh.ElementOrder`: `Linear`, `Quadratic`
  - Possible ElementOrder Options in Apex

`apex.mesh.ElementTopology`: `Bar2`, `Bar3`, `Tria3`, `Tria6`, `Quad4`, `Quad8`, `Quad5`, `Quad9`, `Tetra4`, `Tetra10`, `Penta6`, `Penta15`, `Hexa8`, `Hexa20`, `Pyramid5`, `Pyramid13`
  - Type of Element Topology in Apex

`apex.mesh.FEModelFormat`: `NastranBulk`
  - Possible FEModelFormat Options in Apex

`apex.mesh.FEModelImportOrganizationOptions`: `ByMaterial`, `ByProperty`, `ByContiguousMesh`, `ByElementType`, `SinglePart`
  - Possible FEModelImportOrganizationOptions in Apex

`apex.mesh.FEModelType`: `Nastran`
  - Possible FEModelType Options in Apex

`apex.mesh.FeatureMeshType`: `Fillet`, `Chamfer`, `Cylinder`, `CylinderPartial`, `Washer`, `FourSidedFace`, `ArbirtaryHole`
  - Type of FeatureMesh in Apex

`apex.mesh.HexMeshMethod`: `Auto`, `Loft`, `Sweep`
  - Possible HexMeshMethod Options in Apex

`apex.mesh.HybridCoreType`: `Tet`, `HexPrismatic`
  - Core type has two types of hex dominant available in the Distene mesher API, and one for just tets

`apex.mesh.HybridSkinType`: `QuadDominant`, `Tria`
  - Skin can be auto-generated using quad dominant or tria. This only applies to unmeshed faces of the solid or cell

`apex.mesh.IDConflictResolveMethod`: `AllowDuplicates`, `ResolveAuto`
  - Options available to resolve ID conflicts in Apex

`apex.mesh.MeshFlow`: `Grid`, `FollowEdges`
  - Type of MeshFlow in Apex

`apex.mesh.MeshTopology`: `PointMeshTopology`, `CurveMeshTopology`, `SurfaceMeshTopology`, `SolidMeshTopology`, `HexMeshTopology`
  - Type of Mesh Topology in Apex

`apex.mesh.MeshZone`: `Exterior`, `Interior`
  - How the target can be meshed for creating shrink wrap mesh

`apex.mesh.OrphanBodySetting`: `WithinAndBetween`, `Between`, `Within`, `BetweenParts`
  - Possible OrphanBodySetting Options in Apex

`apex.mesh.RetainId`: `LowerId`, `HigherId`
  - Possible RetainId Options in Apex

`apex.mesh.SolidMeshElementShape`: `Tetra`, `Pyramid`
  - Possible SolidMeshElementShape Options in Apex

`apex.mesh.SplitPattern`: `Cross`
  - SplitPattern for element split

`apex.mesh.SurfaceMeshElementShape`: `Mixed`, `Quadrilateral`, `Triangle`
  - Possible SurfaceMeshElementShape Options in Apex

`apex.mesh.SurfaceMeshMethod`: `Auto`, `Pave`, `Mapped`
  - Possible SurfaceMeshMethod Options in Apex

## Module functions

### `apex.mesh.alignElementEdgeToGeometryEdge(target: apex.EntityCollection, director: apex.EntityCollection) -> {str:apex.mesh.ElementCollection}`
Aligns the "1-2" edge of 2D elements with geometry Edges and returns a dictionary containing two ElementCollections - successfully modified and unmodified elements.

- `target` — Collection of 2D elements to align.
- `director` — Collection of geometry edges to align with

Returns: The returned dictionary has a string key type and an ElementCollection value type. Valid values for the keys are "aligned" and "notAligned". The ElementCollection associated with the "aligned" key contains all 2D elements that were successfully aligned by the method. The ElementCollection associated with the "notAligned" key contains all 2D elements that were NOT successfully aligned by the method. If no elements were aligned or not aligned the associated ElementCollections will be empty

### `apex.mesh.alignElementEdgeToVector(target: apex.EntityCollection, director: apex.construct.Vector3D) -> {str:apex.mesh.ElementCollection}`
Aligns the "1-2" edge of 2D elements with 3D vector and returns a dictionary containing two ElementCollections - successfully modified and unmodified elements.

- `target` — Collection of 2D elements to align.
- `director` — 3D vector to align with

Returns: The returned dictionary has a string key type and an ElementCollection value type. Valid values for the keys are "aligned" and "notAligned". The ElementCollection associated with the "aligned" key contains all 2D elements that were successfully aligned by the method. The ElementCollection associated with the "notAligned" key contains all 2D elements that were NOT successfully aligned by the method. If no elements were aligned or not aligned the associated ElementCollections will be empty

### `apex.mesh.alignNodeAlongCurve(nodes: NodeCollection, curve: apex.geometry.Edge) -> [apex.Coordinate]`
Distributes nodes evenly along a single edge using the order they are in the input collection.

- `nodes` — A row of nodes
- `curve` — a single geomtry edge to align nodes to.

### `apex.mesh.alignNodeAlongPath(nodes: NodeCollection, path: apex.ILocationCollection, asPolyline: bool) -> apex.ILocationCollection`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. Distributes nodes evenly along a path using the order they are in the input collection.

- `nodes` — A row of nodes
- `path` — list of coordinates defining a path.
- `asPolyline` — true, then polyline path used, else curved path.

### `apex.mesh.createCurveMesh(name: str, target: apex.EntityCollection, meshSize: float, elementOrder: ElementOrder) -> apex.mesh.ZResultCreateCurveMesh`
create curve mesh.

- `name` — Name of the new curve mesh.
- `target` — Homogeneous List of Geometry objects to be meshed. Only Curve and Edge are supported - any other Geometry types will be skipped by the method.
- `meshSize` — Specify the Global Edge Length to use in meshing the selected geometry.
- `elementOrder` — Enumeration defining which mesh element type to use to create the CurveMesh. Options are: 1. CurveMeshElementType.Linear

### `apex.mesh.createEdgeSeedBiasedByLength(target: apex.EntityCollection, biasType: apex.mesh.BiasType, reverseBias: bool, edgeLengthL1: float, edgeLengthL2: float) -> apex.mesh.EdgeSeedCollection`
Create a biased Edge Seed on a target Edge or MeshDependentTie by defining the required Maximum and Minimum element edge lengths.

- `target` — Collection of entities that the EdgeSeed will be applied to. Edge seeds can be applied to geometry Edges and MeshDependentTies.
- `biasType` — Enumeration to define whether the seed is biased towards an end of the Edge or towards the middle.
- `reverseBias` — Boolean value to indicate whether the bias direction should be reversed or not.
- `edgeLengthL1` — This value is required if defineL1L2 enumeration is set to defineL1L2.MaxMinEdgeLength. Float value to specify the element size at the beginning of the edge.
- `edgeLengthL2` — This value is required if defineL1L2 enumeration is set to defineL1L2.MaxMinEdgeLength. Float value to specify the element size at the end of the edge.

### `apex.mesh.createEdgeSeedBiasedByNumber(target: apex.EntityCollection, biasType: apex.mesh.BiasType, reverseBias: bool, numberElementEdges: int, biasRatio: float) -> apex.mesh.EdgeSeedCollection`
Create a biased Edge Seed on a target Edge or MeshDependentTie by defining the required number of element edges and a Max/Min element edge length ratio.

- `target` — Collection of entities that the EdgeSeed will be applied to. Edge seeds can be applied to geometry Edges and MeshDependentTies.
- `biasType` — Enumeration to define whether the seed is biased towards an end of the Edge or towards the middle.
- `reverseBias` — Boolean value to indicate whether the bias direction should be reversed or not. If the bias is defined to be an end bias, the system will by default create smaller elements towards the first end of the Edge. Setting this argument to True will cause the smaller elements to be created towards the second end of the Edge If the bias is defined to be an middle bias, the system will by default create smaller elements towards the middle of the Edge. Setting this argument to True will cause the smaller elements to be created towards the ends of the Edge and larger elements to be created in the middle.
- `numberElementEdges` — This value is required if defineL1L2 enumeration is set to defineL1L2.NumberElementsRatio. Integer value to specify the number of elements to be created along the selected edge.
- `biasRatio` — This value is required if defineL1L2 enumeration is set to defineL1L2.NumberElementsRatio. Float value to specify the ratio of shortest to longest element edge.

### `apex.mesh.createEdgeSeedUniformByLength(target: apex.EntityCollection, elementEdgeLength: float) -> apex.mesh.EdgeSeedCollection`
Define the number of elements along a particular edge of the model to create an "EdgeSeed" by specifying the target element edge length. This length, in conjunction wit the target edge length, will be used to determine the number of seed points to create.

- `target` — Collection of entities that the EdgeSeed will be applied to. Edge seeds can be applied to geometry Edges and MeshDependentTies.
- `elementEdgeLength` — The target element edge length. The system will uses this value in conjunction with the actual Edge length to determine how many seed points to create on the Edge.

### `apex.mesh.createEdgeSeedUniformByNumber(target: apex.EntityCollection, numberElementEdges: int) -> apex.mesh.EdgeSeedCollection`
Define the number of elements along a particular edge of the model to create a "EdgeSeed" by specifying a uniformly spaced number of elements.

- `target` — Collection of entities that the EdgeSeed will be applied to. Edge seeds can be applied to geometry Edges and MeshDependentTies.
- `numberElementEdges` — Integer value to specify the number of elements to be created along the selected edge.

### `apex.mesh.createHexMesh(name: str, target: apex.EntityCollection, meshSize: float, surfaceMeshMethod: SurfaceMeshMethod, mappedMeshDominanceLevel: int, elementOrder: ElementOrder, refineMeshUsingCurvature: bool, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, createFeatureMeshOnWashers: bool, createFeatureMeshOnArbitraryHoles: bool, preserveWasherThroughMesh: bool, sweepFace: apex.EntityCollection, hexMeshMethod: HexMeshMethod, projectMidsideNodesToGeometry: bool) -> apex.mesh.ZResultCreateHexMesh`
create hex mesh.

- `name` — Name of the new hex mesh.
- `target` — Homogeneous List of Solid objects to be meshed.
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
- `sweepFace` — Missing, add it for avoiding warning.
- `hexMeshMethod` — Selects a hex meshing method or algorithms. The hex meshing method is slected using the apex.mesh.HexMeshMethod enumeration with constants Auto Loft Sweep Undefined. The argument is optional and will default to "Auto".
- `projectMidsideNodesToGeometry` — indicates whether the mid-side nodes of higher order Hexa/Penta elements will be projected onto the target geometry or not during update. Setting this argument to True will cause the mid-side nodes of all higher order Hexa/Penta elements to be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.

### `apex.mesh.createHybridMesh(name: str, target: apex.EntityCollection, meshSize: float, elementOrder: ElementOrder, coreType: HybridCoreType, skinType: HybridSkinType, useMeshFlowOptimization: bool = False, meshFlow: MeshFlow = apex.mesh.MeshFlow.Grid, refineMeshUsingCurvature: bool, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, growFaceMeshSize: bool, faceMeshGrowthRatio: float, createFeatureMeshes: bool, featureMeshTypes: [apex.mesh.FeatureMeshTypeNS.value], projectMidsideNodesToGeometry: bool) -> apex.mesh.ZResultCreateSolidMesh`
Create hybrid mesh, where quad or adjacent hexes on the bodies faces are transitioned to tets via pyramid elements. An optional Hex core can be requested where tets transition back to hexes via a layer of pyramid elements. If the outer layers are all tria or adjacent tets, and if no hex core is requested, then the result will be entirely tet elements. In that case, the tet mesher should be used instead.

- `name` — Name of the new hybrid mesh.
- `target` — Homogeneous List of Solid objects to be meshed.
- `meshSize` — Specify the Global Edge Length to use in meshing the selected geometry.
- `elementOrder` — Enumeration defining the order of the elements to be created for the HexMesh Options are: 1. MeshOrder.Linear 2. MeshOrder.Quadratic.
- `coreType` — Enumeration defining the core type, default for tet core, the other for cartesian oriented hex core. Options are: 1. HybridCoreType.Tet 2. HybridCoreType.HexPrismatic.
- `skinType` — Enumeration defining the skin can be auto-generated using quad dominant or tria. This only applies to unmeshed faces of the solid or cell. Ideally, we should use the best quality quad and tria mesh, and to day that is the new Crossfield and Asterisk field meshers.
- `useMeshFlowOptimization` — Enhance mesh flow to improve quality. Options are: True, Enable mesh flow. False, Disable mesh flow.
- `meshFlow` — Enumeration defining what type of MeshFlow to use for the skin surface mesh. Options are: 1, MeshFlow.Grid, Internal pattern forms grid for flat surfaces. 2, MeshFlow.FollowEdges, Internal pattern flows with edges for flat surfaces.
- `refineMeshUsingCurvature` — Flag to enable the curvature refinement option of the surface meshing algorithm.
- `elementGeometryDeviationRatio` — Value to control the maximum deviation between and element edge and it's correpsonding geometry edge during curvature refinement. Takes a value between 0.0 and 1.0. *Must be defined if enableCurvatureRefinement is True, otherwise it is ignored.
- `elementMinEdgeLengthRatio` — Value to control the minimum element edge length relative to the global element edge length during curvature refinement. *Must be defined if enableCurvatureRefinement is True, otherwise it is ignored.
- `growFaceMeshSize` — Flag to enable the face mesh growth.
- `faceMeshGrowthRatio` — This property will be a single floating point number between 0 and 1 that defines the size ratio of adjacent elements. A growth factor of 0 is interpreted to mean that no change in size will be supported between adjacent elements. A growth factor of 1 is interpreted to mean that element size may double between adjacent element faces on the free surface of the mesh. A suitable default value will be determined during development of the capability based on testing of representative models.
- `createFeatureMeshes` — optional boolean argument (Default = False) that controls whether or not this method will cause creation of feature meshes around identified geometric features. If False (Default), no feature meshes will be created If True, Feature meshes will be created around the set of feature types activated by the argument.
- `featureMeshTypes` — optional argument controlling the types of feature meshes that this method will attempt to create. This argument is silently ignored unless createFeatureMeshes is enabled.featureMeshTypes is List of apex.mesh.FeatureMeshType enumerations. Feature meshes will be created for each apex.mesh.FeatureMeshType included in the List if an underlying geometry feature of that type is identified. If omitted and createFeatureMeshes is enabled, the method will attempt to create Feature meshes for every supported FeatureMeshType.
- `projectMidsideNodesToGeometry` — indicates whether the mid-side nodes of higher order Hexa/Penta elements will be projected onto the target geometry or not during update. Setting this argument to True will cause the mid-side nodes of all higher order Hexa/Penta elements to be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.

### `apex.mesh.createNodeByCurveArcCenter(target: apex.EntityCollection) -> NodeCollection`
create a collection of nodes by Curve Arc Center.

- `target` — Collection of Curves

### `apex.mesh.createNodeByCurveIntersection(target: apex.EntityCollection) -> NodeCollection`
create a collection of nodes by Curve Intersection.

- `target` — Collection of Curves

### `apex.mesh.createNodeByLocation(coordinates: apex.Coordinate = apex.Coordinate(0.0, 0.0, 0.0), referenceSystem: apex.construct.CoordinateSystem, analysisSystem: apex.construct.CoordinateSystem, isInGlobal: bool = False, pathName: str) -> Node`
Create a node by 3D location.

- `coordinates` — The 3D location of the node to be created. By default, it is representing the x, y and z coordinates of the location in the global cartesian coordinate system. Each of the values in the list represents a Length value and is in the units of Length from the active script unit system. If argument "referenceSystem" is used and defined on a cartesian coordinate system, it is representing the x, y and z coordinates of the location in the local cartesian coordinate system. If argument "referenceSystem" is used and defined on a cylindrical coordinate system, it is representing the r, theta and z coordinates of the location in the local cylindrical coordinate system. r and z represent a Length quantity and are in the units of Length from the active script unit system, theta represents an Angle quantity and is in the units of Angle from the active script unit system. If argument "referenceSystem" is used and defined on a spherical coordinate system, it is representing the r, theta and phi coordinates of the location in the local spherical coordinate system. r represents a Length quantity and is in the units of Length from the active script unit system, theta and phi represent an Angle quantities and are in the units of Angle from the active script unit system.
- `referenceSystem` — Optional argument to define which Coordinate System in which the location of the Node are defined.
- `analysisSystem` — Optional argument to define analysis Coordinate System to be assign to the node.
- `isInGlobal` — Optional argument to convert the location from local to global coordinate system after creation. This argument is only available when "referenceSystem" is defined, otherwise it is silently ignored. If it is true, the system will store the node location in global coordinate system. If it is false, the system will store the node location in local coordinate system.
- `pathName` — Optional argument to specify the part where the node is created, if ignored, the node will be crated under current part.

### `apex.mesh.createNodeByPickLocation(target: apex.Entity, location: apex.ILocation) -> Node`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. create a collection of nodes by Pick Location.

- `target` — geom or fem entity
- `location` — create node location

### `apex.mesh.createSeedPointBySelectedLocation(target: apex.Entity, location: apex.ILocation, searchDistance: float, cleanupTolerance: float) -> SeedPoint`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. Creates and returns a SeedPoint on the "target" (Face, Edge) at the point where "location" projects onto the target. The method will not create a SeedPoint and will throw an exception if any of the belwo conditions exist, 1) If the distance between the "location" and the projected point on the "target" exceeds the "searchDistance" 2) If the projected point lies on a Face and is within "cleanupTolerance" of an existing Edge 3) If the projected point lies on an Edge and is within "cleanupTolerance" of an existing Vertex 4) If the projected point lies on the "target" and is within "cleanupTolerance" of an existing SeedPoint.

- `target` — Geometry Face or Edge on which the SeedPoint will be created
- `location` — the desired location of the SeedPoint. The actual seedPoint location will be determined by projecting this location onto the target
- `searchDistance` — a tolerance that defines the maximum allowable distance between the supplied location and the projected point on the target. If the distance between location and its projection point on the target exceeds this value the SeedPoint will not be created and the method will throw an exception.
- `cleanupTolerance` — a tolerance to prevent SeedPoints from being created close to Edges or Vertices or existing SeedPoints. If the projection of the input location point lies on a Face and is within "cleanupTolerance" of an existing Edge or lies on an Edge and is within "cleanupTolerance" of an existing Vertex or lies on the "target" and is within "cleanupTolerance" of an existing SeedPoint, the SeedPoint will not be created and the method will throw an exception

Returns: created seed point

### `apex.mesh.createSeedPointsBySourceTarget(sources: apex.EntityCollection, targets: apex.EntityCollection, searchDistance: float, cleanupTolerance: float) -> apex.mesh.SeedPointCollection`
create a collection of seed points by source vertex and target edge/face.

- `sources` — a collection of geometry vertex entities
- `targets` — a collection of geometry edge/face entities
- `searchDistance` — the search distance
- `cleanupTolerance` — the cleanup tolerance

Returns: the collectin of created seed points

### `apex.mesh.createShrinkWrapMesh(name: str, target: apex.EntityCollection, meshSize: float, meshType: SurfaceMeshElementShape, elementOrder: ElementOrder, improveQuality: bool, meshingZone: MeshZone, offsetDistance: float, enableFillHole: bool, maxHoleSize: float, minCavityVolume: float) -> SurfaceMeshCollection`
create shrink wrap mesh.

- `name` — Name of the new surface mesh.
- `target` — Homogeneous List of Geometry objects to be meshed. Only Solids and Surfaces - any other Geometry types will be skipped by the method.
- `meshSize` — An optional mesh size. The mesher will attempt to create shell elements with lengths equal to the value. meshSize represents a Length quantity and must be defined in the units of Length in the active script units system.
- `meshType` — Enumeration defining what type of elements can be included in the shrink wrap. Options are: SurfaceMeshElementShape.Mixed and SurfaceMeshElementShape.Triangle. Default is Triangle.
- `elementOrder` — Enumeration defining the order of the elements to be created for the SurfaceMesh Options are: MeshOrder.Linear, MeshOrder.Quadratic.
- `improveQuality` — Remesh initial shrink wrap shells to improve quality. Will takes extra time. Default = True.
- `meshingZone` — Enumeration defining how the target can be meshed. Options are: MeshZone.Exterior, MeshZone.Interior. Default is Exterior.
- `offsetDistance` — Optional distance to apply an offset to the resulting mesh from the target geometry. Default = 0.0, which will place the mesh directly on geometry faces.
- `enableFillHole` — enables hole filling. If this flag is off, hole size is not enabled. Default = False.
- `maxHoleSize` — Optional size value representing an approximate hole diameter. All holes under this specified size will be filled when meshing. Default = 5.0mm, If set to Zero, no holes are filled, even with enableFillHole set to true.
- `minCavityVolume` — This is the minimum volume that will be meshed. This parameter only applies when meshingZone is set to MeshZone.Interior. Default = 0.0.

### `apex.mesh.createSolidMesh(name: str, target: apex.EntityCollection, meshSize: float, meshType: SolidMeshElementShape, elementOrder: ElementOrder, refineMeshUsingCurvature: bool, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, autoimprove: bool, growFaceMeshSize: bool, faceMeshGrowthRatio: float, coarsenMeshInternally: bool, gradeFactor: float, interiorCoarseningFactor: float, ignoreBadEdges: bool, collapseShortElementEdges: bool, collapseElementEdgesShorterThan: float, edgeLengthCollapseLimit: float, createFeatureMeshes: bool, featureMeshTypes: [apex.mesh.FeatureMeshType], createFeatureMeshOnFillets: bool, createFeatureMeshOnChamfers: bool, createFeatureMeshOnCylinders: bool, createFeatureMeshOnSemiCylinders: bool, createFeatureMeshOnWashers: bool, createFeatureMeshOnQuadFaces: bool, createLayeredMesh: bool, thinSectionThreshold: float, numLayers: int, projectMidsideNodesToGeometry: bool, createMinLayers: bool, approximateNumLayers: float) -> apex.mesh.ZResultCreateSolidMesh`
Creates and returns one or more tetrahedral solid meshes using the input geometry and meshing parameters.

- `name` — An optional name for the created mesh. If multiple meshes are created this name will be used for the first mesh created and each subsequent mesh will use this name as a prefix to which a unique integer will be concatenated to ensure name uniqueness. For example with name defined to be 'My Mesh' the first mesh will be named "My Mesh", and any subsequent meshes will be named 'My Mesh 1', 'My mesh 2' etc.
- `target` — A collection of geometry Solids and/or Cells to mesh.
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
- `projectMidsideNodesToGeometry` — indicates whether the mid-side nodes of higher order solid elements will be projected onto the target geometry or not during update. Setting this argument to True will cause the mid-side nodes of all higher order solid elements to be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.
- `createMinLayers` — This parameter when on, will set the approximate minimum number of layers of the body. The local density of thin areas as define by meshSize/numLayers will be adjusted to facilitate the requested number of layers. Giving a mesh size of 40mm, and numLayers set to 3, then any area thinner than 13.33 will have the mesh size locally adjusted smaller. Since numLayers is a real number, finer adjustments can be made as needed.
- `approximateNumLayers` — default is 2.0. This is an approximate value. it might be required that 2.1 or 2.2 be used to achieve the desired result in all locations. The large the approximate number of layers, the more instable the result is likely to be, so adjustments up or down may be needed.

### `apex.mesh.createSurfaceMesh(name: str, target: apex.EntityCollection, meshSize: float, meshType: SurfaceMeshElementShape, meshMethod: SurfaceMeshMethod, mappedMeshDominanceLevel: int, elementOrder: ElementOrder, meshUsingPrincipalAxes: bool, allQuadBoundary: bool, applyTriaReduction: bool, triaReductionStrength: int, refineMeshUsingCurvature: bool, curvatureType: CurvatureType, elementGeometryDeviationRatio: float, elementMinEdgeLengthRatio: float, proximityRefinement: bool, growFaceMeshSize: bool, faceMeshGrowthRatio: float, createFeatureMeshes: bool, featureMeshTypes: [apex.mesh.FeatureMeshType], createFeatureMeshOnFillets: bool, createFeatureMeshOnChamfers: bool, createFeatureMeshOnWashers: bool, createFeatureMeshOnArbitraryHoles: bool, createFeatureMeshOnQuadFaces: bool, projectMidsideNodesToGeometry: bool, useMeshFlowOptimization: bool, meshFlow: MeshFlow, minimalMesh: bool, meshControlFeature: ElementCollection, snapMeshFeature: bool, searchDistance: float, cleanupTolerance: float) -> apex.mesh.ZResultCreateSurfaceMesh`
create surface mesh.

- `name` — Name of the new surface mesh.
- `target` — Homogeneous List of Geometry objects to be meshed. Only Solids, Surfaces and Faces are supported - any other Geometry types will be skipped by the method.
- `meshSize` — Specify the Global Edge Length to use in meshing the selected geometry.
- `meshType` — Enumeration defining what type of elements can be included in the create SurfaceMesh. Options are: 1. SurfaceMeshElementShape.Mixed 2. SurfaceMeshElementShape.Quadrilateral 3. SurfaceMeshElementShape.Triangle
- `meshMethod` — Enumeration defining which mesh algorithm to use to create the SurfaceMesh. Options are: 1. SurfaceMeshMethod.Auto 2. SurfaceMeshMethod.Pave 3. SurfaceMeshMethod.Mapped
- `mappedMeshDominanceLevel` — Value to control how aggressively the algorithm will be in forcing creation of a mapped mesh. Varies from 1 (least aggressive) to 5 (most aggressive). Must be defined if meshMethod is SurfaceMeshMethod.Mapped.
- `elementOrder` — Enumeration defining the order of the elements to be created for the SurfaceMesh Options are: 1. MeshOrder.Linear 2. MeshOrder.Quadratic.
- `meshUsingPrincipalAxes` — DEPRECATION NOTICE: This parameter has been deprecated and we intend to remove it in the next Apex release. Users are advised to transition their code to use the new extended option "useMeshFlowOptimization" as quickly as possible to avoid future problems. It was used to enable/disable the principal axis guided meshing algorithm causing the mesher to attempt to create elements with edges aligned wit the principal axes of the target faces.
- `allQuadBoundary` — Flag to enable All Quad Boundary Mesh option of the surface meshing algorithm.
- `applyTriaReduction` — turns on tria reduction process. This process will attempted to remove tria from a mesh found in specific patterns. Not all triangle elements can be removed without reducing mesh quality too far. This feature is ignored if growFaceMeshSize or refineMeshUsing Curvature is on.
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
- `projectMidsideNodesToGeometry` — indicates whether the mid-side nodes of higher order shell elements will be projected onto the target geometry or not during update. Setting this argument to True will cause the mid-side nodes of all higher order shell elements to be projected onto the target geometry causing the element edges to follow the curvature of the geometry. Setting this argument to False will cause the mid-side nodes to be positioned at the mid-point of a straight line between the two corner nodes.If the target geometry is curved, the mid-side nodes will not lie directly on the geometry.
- `useMeshFlowOptimization` — Enhance mesh flow to improve quality. Options are: True, Enable mesh flow. False, Disable mesh flow.
- `meshFlow` — Enumeration defining what type of MeshFlow to use in the SurfaceMesh. Options are: 1, MeshFlow.Grid, Internal pattern forms grid for flat surfaces. 2, MeshFlow.FollowEdges, Internal pattern flows with edges for flat surfaces.
- `minimalMesh` — This setting is an optional argument for special meshing cases. Its default = False. If true, it is only active when meshType = apex.mesh.SurfaceMeshElementShape.Triangle. When true with triangle mesh, the mesher will only create nodes at vertexes, mesh seeds, seed points, or at nodes on adjacent meshes on boundaries. If an edge has no vertex, such as some holes, or in some other cases, the mesh will fail.
- `meshControlFeature` — Optional element collection of 2d elements. They must be orphan elements not associated to other geometry. They can be multiple groups of connected elements in the list. Each set of connected elements must fall within the same face. If supplied, the element nodes must be within cleanupTolerance of a face.
- `snapMeshFeature` — This is an optional argument. The default is True if not specified. It is only used if an meshControlFeature list is specified. This argument specifies if the input meshControlFeature element nodes are to be snapped on to the geometry faces, edges and vertices, or remain in their original locations. Large deviations can produce a poor or invalid mesh if not snapped. Snapping will only within the specified cleanupTolerance.
- `searchDistance` — This is an optional argument. It is only in effect if a meshControlFeature list is supplied. Default is 0.1mm. Element nodes supplied in meshControlFeature must be within this tolerance to be valid.
- `cleanupTolerance` — This is an optional argument. It is only in effect if a meshControlFeature list is supplied. Default is 0.1mm. Element nodes supplied in meshControlFeature must be within this tolerance to be valid. The nodes will be snapped to the geometry if snaMeshFeature is true.

### `apex.mesh.getCurveMeshes(list: [{str:str}]) -> CurveMeshCollection`
Get a collection of CurveMeshes, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the Curve meshes to retrieve. Valid keys are 'path' and 'name'.

Returns: a CurveMeshCollection of the requested CurveMeshes

### `apex.mesh.getDuplicatedSubMeshes() -> apex.mesh.ZResultDuplicatedSubMeshes`
Renumber elements or nodes id in target parts or assembles By Offset Id with different options.

Returns: duplicated SubMeshes

### `apex.mesh.getElements(list: [{str:str}]) -> ElementCollection`
Get a collection of Element, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the elements to retrieve. Valid keys are 'path', 'indices', and 'ids'.

Returns: a ElementCollection of the requested Elements

### `apex.mesh.getHexMeshes(list: [{str:str}]) -> HexMeshCollection`
Get a collection of HexMeshes, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the Hex meshes to retrieve. Valid keys are 'path' and 'name'.

Returns: a HexMeshCollection of the requested HexMeshes

### `apex.mesh.getMesh(pathName: str) -> MeshBody`
Get a MeshBody in a Model.

- `pathName` — of the part to get including the model name as in 'MyModel/Assembly1/Part1/Mesh1'.

Returns: the created MeshBody

### `apex.mesh.getMeshes(list: [{str:str}]) -> MeshBodyCollection`
Get a collection of MeshBodies, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the meshes to retrieve. Valid keys are 'path' and 'name'.

Returns: a MeshBodyCollection of the requested Meshes

### `apex.mesh.getNodes(list: [{str:str}]) -> NodeCollection`
Get a collection of Nodes, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the nodes to retrieve. Valid keys are 'path', 'indices', and 'ids'.

Returns: a NodeCollection of the requested Nodes

### `apex.mesh.getNodesByAnalysisSystem(targets: apex.EntityCollection, coordinateSystem: apex.construct.CoordinateSystem) -> NodeCollection`
Retrieve a Node Collection from the target part/assembly/mesh body using analysis coordinate system referencing to node.

- `targets` — Optional argument to choose target part/assembly/mesh body to identify nodes referencing analysis coordinate system. If it is undefined, the target will be the whole model including all parts/assemblies/mesh bodies. If the targets are not part/assembly/mesh body, returns an exception: Unsupported targets to find nodes referencing to analysis coordinate system.
- `coordinateSystem` — coordinate system that used to defined analysis coordinate system of node.

### `apex.mesh.getPointMeshes(list: [{str:str}]) -> PointMeshCollection`
Get a collection of PointMeshes, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the Point meshes to retrieve. Valid keys are 'path' and 'name'.

Returns: a PointMeshCollection of the requested PointMeshes

### `apex.mesh.getSolidMeshes(list: [{str:str}]) -> SolidMeshCollection`
Get a collection of SolidMeshes, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the Solid meshes to retrieve. Valid keys are 'path' and 'name'.

Returns: a SolidMeshCollection of the requested SolidMeshes

### `apex.mesh.getSurfaceMeshes(list: [{str:str}]) -> SurfaceMeshCollection`
Get a collection of SurfaceMeshes, specified by list of key:value string dictionaries.

- `list` — of dictionaries (string:string) specifying the Surface meshes to retrieve. Valid keys are 'path' and 'name'.

Returns: a SurfaceMeshCollection of the requested SurfaceMeshes

### `apex.mesh.mergeNodes(target: apex.EntityCollection, mergeTolerance: float, evaluateFreeEdgeOnly: bool, mergeBehavior: OrphanBodySetting, retainId: RetainId) -> None`
Merges nodes, deleting merged nodes.

- `target` — Collection of nodes or meshbody or part to search in when merging.
- `mergeTolerance` — tolerance.
- `evaluateFreeEdgeOnly` — If True, only evaulate free edge nodes out of selected list.
- `mergeBehavior` — Enumeration defining orphan body merge behavior Options are: 1. OrphanBodySetting.WithinAndBetween 2. OrphanBodySetting.Between 3. OrphanBodySetting.Within 4. OrphanBodySetting.BetweenParts.
- `retainId` — Enumeration defining retain id Options are: 1. RetainId.LowerId 2. RetainId.HigherId

### `apex.mesh.meshBodyCollection(meshList: [MeshBody] = []) -> MeshBodyCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.mesh.MeshBodyCollection().

- `meshList` — optional list of Mesh Bodies to add to the collection.

### `apex.mesh.moveNodeAlongFace(node: Node, location: apex.ILocation) -> None`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. Moves a mesh body node along the surface or on mesh facets. The inputs are a single node, and a destination xyz location.

- `node` — Node Being Moved.
- `location` — XYZ Location of destination.

### `apex.mesh.moveNodeNormalFace(node: Node, distance: float) -> None`
Moves a mesh body node in the normal direction possitive or negatively.

- `node` — Node Being Moved.
- `distance` — distance of destination.

### `apex.mesh.moveNodeToNode(target: Node, destinationNode: Node) -> None`
Moves a mesh body node To another node, and merges with that node if possible. This can collapse elements from quad to tria, or delete a tria if one if its edges are collapsed.

- `target` — Node Being Moved.
- `destinationNode` — Node that is the destination.

### `apex.mesh.reduceTria(targets: apex.EntityCollection, lockTargets: apex.EntityCollection, minSizeRatio: float, maxSizeRatio: float, skewAngleDeviation: float) -> SurfaceMeshCollection`
Reduct triangle elements.

- `targets` — Mesh body, Sub-mesh or elements.
- `lockTargets` — optional list of elements and nodes to lock.
- `minSizeRatio` — Minimum Allowable Deviation from Current Mesh Size. Default is 0.5.
- `maxSizeRatio` — : Maximum Allowable Deviation from Current Mesh Size. Default is 1.4.
- `skewAngleDeviation` — : Maximum Skew during Tria Reduction. Default = 45.0 degree.

### `apex.mesh.renumberByOffset(target: apex.EntityCollection, nodeOffset: int int = 0, elementOffset: int int = 0, coordinateSystemOffset: int int = 0, conflictResolveMethod: apex.mesh.IDConflictResolveMethod = apex.mesh.IDConflictResolveMethod.ResolveAuto, conflictResolveOption: apex.mesh.ConflictResolveOption = apex.mesh.ConflictResolveOption.Undefined) -> apex.mesh.ZRenumberByOffset`
Renumber entities by applying an offset value to the existing ID. Currently supports renumbering of Nodes, Elements and Coordinate Systems only.

- `target` — The collection of Entities that will be renumbered.
- `nodeOffset` — The offset that will be applied to all Node ID's in target to determine the new Node ID.
- `elementOffset` — The offset that will be applied to all Element ID's in target to determine the new Element ID.
- `coordinateSystemOffset` — The offset that will be applied to all CoordinateSystem ID's in target to determine the new CoordinateSystem ID.
- `conflictResolveMethod` — conflict Resolve Method.
- `conflictResolveOption` — conflict Resolve Method.

### `apex.mesh.renumberByStartId(target: apex.EntityCollection, startNodeId: int int int = 0, startElementId: int int int = 0, startCoordinateSystem: int int int = 0, conflictResolveMethod: apex.mesh.IDConflictResolveMethod = apex.mesh.IDConflictResolveMethod.ResolveAuto, conflictResolveOption: apex.mesh.ConflictResolveOption = apex.mesh.ConflictResolveOption.Undefined) -> apex.mesh.ZRenumberByStartId`
Renumber entities by supplying a starting ID.

- `target` — The collection of Entities that will be renumbered.
- `startNodeId` — The ID to use as the starting ID for renumbering of Nodes.
- `startElementId` — The ID to use as the starting ID for renumbering of Elements.
- `startCoordinateSystem` — The ID to use as the starting ID for renumbering of CoordinateSystems.
- `conflictResolveMethod` — conflict Resolve Method.
- `conflictResolveOption` — conflict Resolve Method.

### `apex.mesh.reverseElement(target: apex.EntityCollection) -> None`
reverses the orientation of the element by changing the node connectivity. Also reverses the associated geometry of elements are associated, and ALL other elements associated to the same geometry even if not in put list.

- `target` — Collection of 2D elements or faces to reverse.

### `apex.mesh.reverseOrientShells(target: ElementCollection, referenceElement: Element, featureAngle: float, stopAtMeshJunctions: bool) -> ElementCollection`
tries to match guiding element orientation based on sheet orientation rules. Will also reverse any associated goemtry and ALL other elements associated to that geometry even if not in input list.

- `target` — Collection of 2D elements to reverse.
- `referenceElement` — single shell element to use as reference.
- `featureAngle` — feature angle used in algorithm.
- `stopAtMeshJunctions` — behavior toggle. This controls if algorithm ignore T-junctions when grouping areas to reverse or stops at them.

### `apex.mesh.separateElements(target: apex.EntityCollection) -> None`
Separte elements. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with separateElementByBody()

- `target` — Collection of parts or meshbody when separating.

### `apex.mesh.separateElementsByBody(target: apex.EntityCollection) -> None`
Separte elements.

- `target` — Collection of parts or meshbody when separating.

### `apex.mesh.splitElementByPattern(elementList: ElementCollection, nTargetEdge: apex.mesh.ElementEdge = None, pattern: apex.mesh.SplitPattern = apex.mesh.SplitPattern.Cross, nNumberElementEdges: int = 2, mNumberElementEdges: int = 2) -> None`
Splits a collection of elements by specific pattern. Default is to split the elements by 2*2 cross pattern. Note that an element edge is needed to orient "N" side of target elements when nNumberElementEdges != mNumberElementEdges

- `elementList` — Collection of shell elements to split
- `nTargetEdge` — The optional element edge oriented "N". If can be omitted when nNumberElementEdges = mNumberElementEdges.
- `pattern` — Pattern used to split the elements. If omitted system uses "apex.mesh.SplitPattern.Cross" by default.
- `nNumberElementEdges` — The number of elements edges on "N" side. If omitted the number is 2 by default.
- `mNumberElementEdges` — The number of elements edges on "M" side. If omitted the number is 2 by default.

### `apex.mesh.splitElementOnCurve(elementList: ElementCollection, curves: apex.EntityCollection, useCleanUpTolerance: bool, tolerance: float) -> None`
This splits a collection of elements.

- `elementList` — Collection of shell elements to split
- `curves` — Collection of geomtry edges to split on.
- `useCleanUpTolerance` — Toggle that turns on use of cleanup tolerance.
- `tolerance` — Only needed when useCleanUpTolerance is True.

### `apex.mesh.splitElementOnPath(elementList: ElementCollection, path: apex.ILocationCollection, asPolyline: bool, useCleanUpTolerance: bool, tolerance: float) -> None`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. Splits a collection of elements on a path defined by a list of locations.

- `elementList` — Collection of shell elements to split
- `path` — List of locations defining the split path.
- `asPolyline` — true, then polyline path used, else curved path.
- `useCleanUpTolerance` — Toggle that turns on use of cleanup tolerance.
- `tolerance` — Only needed when useCleanUpTolerance is True.

## Classes in this module

Full method signatures are in `api/classes/apex.mesh.md`.

`CurveMesh`, `CurveMeshCollection`, `EdgeSeed`, `EdgeSeedCollection`, `Element`, `ElementCollection`, `ElementEdge`, `ElementEdgeCollection`, `ElementFace`, `ElementFaceCollection`, `ElementIdSet`, `ElementIdSetCollection`, `HexMesh`, `HexMeshCollection`, `MeshBody`, `MeshBodyCollection`, `Node`, `NodeCollection`, `NodeIdSet`, `NodeIdSetCollection`, `PointMesh`, `PointMeshCollection`, `SeedPoint`, `SeedPointCollection`, `SolidMesh`, `SolidMeshCollection`, `SubMesh`, `SubMesh0D`, `SubMesh1D`, `SubMesh2D`, `SubMesh3D`, `SubMeshCollection`, `SurfaceMesh`, `SurfaceMeshCollection`, `ZRenumberByOffset`, `ZRenumberByStartId`, `ZResultCreateCurveMesh`, `ZResultCreateHexMesh`, `ZResultCreateMesh`, `ZResultCreateSolidMesh`, `ZResultCreateSurfaceMesh`

