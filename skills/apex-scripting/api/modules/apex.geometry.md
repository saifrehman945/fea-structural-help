# apex.geometry

(apex.geometry module) Geometry Editing functions: Drag, Push/Pull, Defeature, Stitch, MidSurface, etc.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.geometry.CADFormat`: `ParasolidText`, `ParasolidBinary`, `STLText`, `STLBinary`, `ACISText`, `IGES_5_3`, `STP_AP214`
  - Possible CADFormat Options in Apex

`apex.geometry.CleanupOperation`: `CleanUp`, `RemoveSmallFeatures`, `FindSmallFeatures`, `RemoveSurfaceFeatures`, `FindSurfaceFeatures`
  - Possible CleanupOperation Options in Apex

`apex.geometry.CurveBehavior`: `Spline`, `Polyline`, `Circle`, `Arc`
  - Possible CurveBehavior Options in Apex

`apex.geometry.DefeatureOperation`: `Unknown`, `Automatic`, `RemoveSelected`, `EditOrDeleteFaces`, `FeatureIdentify`, `SelectedDefeature`
  - Possible DefeatureOperation Options in Apex

`apex.geometry.DragEdgeBehavior`: `Follow`, `Extrude`, `Stretch`
  - Possible DragEdgeBehavior Options in Apex

`apex.geometry.DragVertexBehavior`: `ForceStraight`, `KeepCurved`
  - Possible DragVertexBehavior Options in Apex

`apex.geometry.GeometryFaultType`: `Sliver`, `SmallEdge`, `SmallFace`, `Overhang`, `Gap`, `Crack`, `Spike`

`apex.geometry.GeometryFeatureType`: `Hole2D`, `Fillet2D`, `Chamfer2D`, `Hole3D`, `Fillet3D`, `Chamfer3D`

`apex.geometry.GeometrySplitBehavior`: `Split`, `Partition`
  - Possible GeometrySplitBehavior Options in Apex

`apex.geometry.GeometrySplitLineType`: `Spline`, `Polyline`
  - Possible Geometry Line Types Options for use in geometry surface splitting operations

`apex.geometry.LoftClampingMethod`: `No`, `Tangent`, `Curvature`
  - Possible surface loft methods in Apex

`apex.geometry.MidSurfaceIncrementalMethod`: `Tapered`, `Left`, `Right`, `Planar`
  - Possible MidSurfaceIncrementalMethod Options in Apex

`apex.geometry.OffsetBehavior`: `Sharp`, `Rounded`
  - Offset behavior for offset edges

`apex.geometry.PushPullBehavior`: `FollowShape`, `Extrude`, `Stretch`
  - Possible PushPullBehavior Options in Apex

`apex.geometry.PushPullMethod`: `Normal`, `Fillet`, `Chamfer`
  - Possible PushPullMethod Options in Apex

`apex.geometry.STLImportBodyType`: `Mesh`, `Faceted`
  - Possible STLImportBodyType Options in Apex

`apex.geometry.SnapModeType`: `OnEdge`, `Extension`, `OnSurface`, `SnapNone`, `MidPoint`, `Vertex`, `Tangent`, `Perpendicular`
  - Possible SnapModeType Options in Apex

`apex.geometry.SweepProfileAlignmentMethod`: `Normal`, `Parallel`, `Arclength`
  - Four alternate methods that control the orientation of the profile relative to the normal plane of the director path

`apex.geometry.SweepProfileClampingMethod`: `No`, `Smooth`, `Sharp`
  - Possible sweep clamping Types Options for use in geometry sweep profile operations

## Module functions

### `apex.geometry.addVertex(target: apex.Entity, locationTarget: apex.ILocation) -> apex.Entity`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. add vertex on edge at selected location.

- `target` — the selected edge/curve for adding the vertex
- `locationTarget` — selected location on target edge to add vertex

Returns: newly created vertex

### `apex.geometry.assignConstantThicknessMidSurface(target: apex.EntityCollection, autoAssignThickness: bool, autoAssignTolerance: float) -> DllExport apex.EntityCollection`
creates mid-surface body for each constant thickness solid in the target list. Can also auto-assign a constant thickness if toggle is on

- `target` — Target solid collection
- `autoAssignThickness` — Automatically assigns thickness if True
- `autoAssignTolerance` — Tolerance for merging similar sections

Returns: Collection of created bodies

### `apex.geometry.autoOffsetAlignMidSurface(target: apex.EntityCollection, uptoEntity: apex.Entity) -> DllExport[float]`
this offsets all bodies associated with the faces selected up to the input uptoEntity. This is a rigid transformation based on closest approach projection to the body.

- `target` — collection of surface faces of bodies to align with uptoEntity
- `uptoEntity` — Specify which Point, Edge or Face to use for offset distance calculation for align

Returns: Distances of align offset.

### `apex.geometry.autoOffsetMidSurface(target: apex.EntityCollection) -> DllExport apex.EntityCollection`
create mid surface. User inputs one or more solid faces. for each connected set of manifolded solid faces, one surface body is created. The offset found is based on the auto-offset algorithm. This is noromally the 1/2 way to smallest opposite distance found.

- `target` — collection of solid face or faces to do auto-offset calcuation from

Returns: Collection of created bodies

### `apex.geometry.autoOffsetUpdateMidSurface(target: apex.EntityCollection, uptoEntity: apex.Entity = None, offsetDistance: float = 0.0, offsetHalfway: bool = False) -> DllExport apex.EntityCollection`
create midsurface

- `target` — Solid face or faces to do auto-offset calcuation from, this assumes there is existing surfaces assciated with the target body face list
- `uptoEntity` — Optional Upto entity (Point or Edge) for updating the offset. This reference location overides the calculated opposite side, or a prevoius update uptoEntity API call. If not set, must be null, if it is set, offsetDistance must be null or exception is returned
- `offsetDistance` — Explicit distance to offset. Ignores half way setting, it always offset this full distance
- `offsetHalfway` — If this toggle is True, then the offset will be half of the calculated distance. Either using the explicit uptoEntity or the auto-calculated side.

Returns: surface body updated

### `apex.geometry.createBoxByLocationOrientation(name: str = "BOX", description: str = "", length: float = 200.0, height: float = 200.0, depth: float = 200.0, origin: apex.ILocation = None, orientation: apex.IOrientation = None, useLocalValue: bool = True) -> apex.geometry.Box`
Creates and returns a parametric geometry Box using an input origin, orientation, length width and height.

- `name` — An optional name for the Box that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'Box ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Box 1234'.
- `description` — An optional description for the Box that will be created. If omitted the description will be left blank.
- `length` — The length of the Box - Length is associated with the X-axis of the orientation/coordinate system associated with the Box. length is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem
- `height` — The height of the Box - height is associated with the Y-axis of the orientation/coordinate system associated with the Box. height is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem
- `depth` — The depth of the Box - depth is associated with the Z-axis of the orientation/coordinate system associated with the Box. depth is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem.
- `origin` — The origin of the Box. The length, depth and height of the box emanate from the origin.
- `orientation` — The orientation of Box that defines the length, height and depth directions of the Box.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.

Returns: created Box

### `apex.geometry.createCurve(target: apex.ILocationCollection, behavior: CurveBehavior) -> apex.geometry.Curve`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. create curves.

- `target` — locations to define a curve
- `behavior` — switch between spline, polyline

Returns: Created curve

### `apex.geometry.createCurve3DNurb(controlPoints: apex.ILocationCollection, knotPoints: [float], degree: int, weights: [float] = []) -> Curve`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. Creates a Curve in the current Part based on NURB mathematics.

- `controlPoints` — objects that represent the control points of the NURB curve
- `knotPoints` — A list of double values that represent the knot vector of the NURB curve
- `degree` — The order (or degree) of the NURB curve
- `weights` — A List of weight values. The List must contains the same number of entries as controlPoints and the weights will be assigned to the control point at the corresponding position in the controlPoint collection. If the weights are omitted, the curve will be created using wight values of 1.0 for each control point.

Returns: Curve

### `apex.geometry.createCurve3Pnt(point1: apex.Coordinate, point2: apex.Coordinate, point3: apex.Coordinate, behavior: CurveBehavior) -> apex.geometry.Curve`
Creates an arc with three points.

- `point1` — Start Point.
- `point2` — Mid Point.
- `point3` — End Point.
- `behavior` — Switch between Circle, Arc.

Returns: Created curve

### `apex.geometry.createCurveIntersect(faces: apex.EntityCollection, intersectingFaces: apex.EntityCollection, planeLength: float = NAN) -> apex.geometry.CurveCollection`
Create one or more Curves from the intersection of two or more faces or planes. One curve is created from each contiguously connected set of intersections from the same pair of bodies.

- `faces` — Input target faces or datum planes to intersect.
- `intersectingFaces` — faces or datum planes to intersect with.
- `planeLength` — specifies the length of all Planes that will be used in any plane to plane intersections.

Returns: Created curves

### `apex.geometry.createCurveProject(edges: apex.geometry.EdgeCollection, faces: apex.EntityCollection, direction: apex.construct.Vector3D) -> apex.geometry.GeometryBodyCollection`
Creates a set collection of Curves or Points from the projection of Edges onto Faces. One Curve or Point created for each set of contiguous edges. when the curve orthogonal to a surface, creates a point.

- `edges` — Connection of input edges specifying the sources of the projection.
- `faces` — Target collection of Faces to project target Edge collection onto.
- `direction` — Optional argument defining the direction of the projection Edges. If omitted, the edges will be projected Normal to the surface.

Returns: Created curves or points

### `apex.geometry.createCurvesFromEdges(edges: apex.geometry.EdgeCollection) -> apex.geometry.CurveCollection`
Create and returns Curves from input Edges. One discrete Curve will be created for each set of contiguous edges. These can be manifolded and non-manifolded curves.

- `edges` — Collections of Edges from which the Curves will be created.

Returns: Created curves

### `apex.geometry.createCylinderByLocationOrientation(name: str = "Cylinder", description: str = "", length: float = 50.0, radius: float = 400.0, sweepangle: float = 360, origin: apex.ILocation = None, orientation: apex.IOrientation = None, useLocalValue: bool = True) -> apex.geometry.Cylinder`
Creates and returns a parametric geometry Cylinder (or partial Cylinder) using an input origin, orientation, length, radius and sweepangle.

- `name` — An optional name for the Cylinder that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'CYlinder ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Cylinder 1234'.
- `description` — An optional description for the Cylinder that will be created. If omitted the description will be left blank.
- `length` — The length of the Cylinder - Length is associated with the Z-axis of the orientation/coordinate system associated with the Box. length is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem.
- `radius` — The radius of the Cylinder. radius is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem.
- `sweepangle` — An optional sweepangle for the Cylinder. If supplied, sweepangle must have a value greater than zero and less than 360 degrees (or equivalent values in alternate unit systems). This will cause a partial cylinder to be created - for example supplying a value of 180 degrees will create a semi-cylinder, 90 degrees a quarter cylinder etc. sweepangle is an Angle quantity and must be defined in the units of Angle in the active ScriptUnitSystem.
- `origin` — The origin of the Cylinder. The origin defines the center of the bottom circular face of the Cylinder.
- `orientation` — The orientation of Cylinder that defines the cylinder axis along which the length is measured.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.

Returns: created Cylinder

### `apex.geometry.createEdgeOffset(target: apex.geometry.EdgeCollection, offsetDistance: float, offsetBehavior: apex.geometry.OffsetBehavior = apex.geometry.OffsetBehavior.Sharp) -> apex.geometry.EdgeCollection`
Creates new Edges on Surface or Solid Faces by offsetting the input Edges by the input offset distance. Care must be taken to specify an offsetDistance that will cause some portion of the new Edge to remain within the Body that composes the input Edge. The offset edge can be offset with sharp corners or rounded corners.

- `target` — List of edges in a body to offset.
- `offsetDistance` — Distance to offset the input Edges. Represents a Length quantity and must be specified using the units of Length from the active script unit system.
- `offsetBehavior` — An Optional enumeration that determines the shape of the offset edge where there are corners at adjacent edges. The sharp behavior will maintain sharp corners, and the round behavior will smooth out the sharp corner by introducing an arc of the same radius as the offset distance.

Returns: Created edges

### `apex.geometry.createEllipsoidByLocationOrientation(name: str = "Ellipsoid", description: str = "", xradius: float = 100.0, yradius: float = 200.0, zradius: float = 100.0, origin: apex.ILocation = None, orientation: apex.IOrientation = None, useLocalValue: bool = True) -> apex.geometry.Ellipsoid`
Creates and returns a parametric geometry solid Ellipsoid using an input origin, orientation, and three orthogonal "radii" - xradius, yradius and zradius.

- `name` — An optional name for the Ellipsoid that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'Ellipsoid ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Ellipsoid 1234'.
- `description` — An optional description for the Ellipsoid that will be created. If omitted the description will be left blank.
- `xradius` — The 'radius' of the Ellipsoid in the x direction. xradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system.
- `yradius` — The 'radius' of the Ellipsoid in the y direction. yradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system.
- `zradius` — The 'radius' of the Ellipsoid in the z direction. zradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system.
- `origin` — The origin of the Ellipsoid. The radii of the Ellipsoid emanate from the origin.
- `orientation` — The orientation of the Ellipsoid that defines the directions of the axes along which the xradius, yradius and zradius dimensions are measured.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.

Returns: created Ellipsoid

### `apex.geometry.createEnvelope(generator: apex.EntityCollection, relativeTo: apex.EntityCollection, name: str = "", interpolationSteps: int = 0, description: str = "", modelAssoName: str = "") -> apex.EntityCollection`
create envelope sensor The input

- `generator` — collection of parts/bodies/faces
- `relativeTo` — collection of parts
- `name` — envelope sensor name
- `interpolationSteps` — the interpolation step of envelope sensor
- `description` — the description of envelope sensor
- `modelAssoName` — the association model name

Returns: created envelope sensor

### `apex.geometry.createFacetedBodies(tessellations: [apex.utility.PolyData], meshBody: apex.mesh.MeshBodyCollection = 0, name: str = "", part: apex.Part = 0, autoSmoothAnalyticFace: bool = True, createNURBS: bool = False, createNURBSWithAnalyticalFace: bool = True, cleanupNURBS: bool = True, convertToSolid: bool = True, smoothLevel: int = 2) -> DllExport apex.geometry.GeometryBodyCollection`
Creates one or more FacetedCurve/FacetedSurface/FacetedSolid and optionally one or more NURBS GeometryBodies from one or more sets of tessellation (PolyData) objects and optional mesh data. It adds all of the the created geometry to the specified input part, or to the Parts they are members of if none specified. The faceted bodies and the optional NURBS bodies are returned as a list of GeometryBodyCollections. One GeometryBodyCollection for each polydata tessellation object, and in the output will be in the same order as the input data. If the input tessellation consists of more than one contiguous region of cells, one discrete faceted body and optionally one discrete NURBS GeometryBody will be generated for each contiguous region. If the input tessellation was generated using a CurveMesh/SurfaceMesh/SolidMesh, that mesh will be associated to the corresponding faceted body types.

- `tessellations` — A list of Tessellation objects from which the faceted and optional NURBS bodies will be created from. The bodies will be created using the points and cells from the Tessellations. The topology of the bodies (Vertices,Edges and Faces) will be created using the points, edges and faces provided by the vertex, edge and face properties of the Tessellation objects. The tessellation objects could be discontinuous, which would then end up creating more than one facet body for one tessellation object.
- `meshBody` — An optional argument that to supply a list of MeshBodies. If supplied, the attributes of the MeshBodies (Materials, Sections) and Loads or Constraints that are applied to the MeshBodies will be transferred from the MeshBodies to the FacetedSurfaces. The MeshBodies are expected to be the same meshBodies used to generate the tessellations and the method will threw an exception if the MeshBodies and the Tessellations are not matched. If a MeshBodies are not supplied, no attribute, load or constraint mapping will be performed
- `name` — The root name (optional) that will be assigned to the generated bodies. If supplied, the name must be unique within the parent Part of the generated body otherwise the system will automatically rename the body to ensure name uniqueness within the Part If omitted, the system will provide a default name - "Faceted Surface <n>" or "Faceted Solid <n>", "NURBS Solid <n>", etc. where <n> is the lowest possible integer to ensure name uniqueness If multiple bodies are generated, the supplied name value will be used as a name prefix and integers will be appended to create the full name and ensure name uniqueness within the Part
- `part` — The a Part that the input meshBody generated bodies will be added to. This argument may be omitted if the meshBodyCollection argument is present in which case the generated bodies will be added to the Part that parents the meshBody. If both meshBodyCollection AND PartCollection are supplied the part argument will be silently ignored and the generated bodies will be added to the Part that parents the meshBody. If both meshBody and part are omitted the method will throw an exception
- `autoSmoothAnalyticFace` — This setting controls whether facet bodies created that match analytical faces should be smoothed. This allows remeshing of analytical faces to be remeshed more accurately. If faces are falsely identified as analytical faces, such as faces on an organic shaped model with no analytical faces, the end result could introduce errors to the face shapes.
- `createNURBS` — An optional boolean argument (default=False) to request creation of NURBS geometry bodies as well as faceted geometry bodies. When True, one NURBS geometry body will be created for each faceted geometry body that is generated. When False, only faceted bodies will be created
- `createNURBSWithAnalyticalFace` — If this setting is ON, then the system will try to replace the NURBS face with an analytical faces if it matches one within tolerance. This can give a superior result for NURBS created from mesh that originated from CAD geometry. It is not useful, and can give poor results if the model is an organic shape with no real analytical shapes in it.
- `cleanupNURBS` — An optional argument (default = True) to control cleanup of any NURBS geometry bodies that are created. If True, all geometry bodies will processed to remove faults and to replace NURBS based topology with analytical representations where possible. If False, no processing will be carried out on the generated URBS bodies. This argument will be silently ignored if createNURBS is False (no NURBS bodies requested)
- `convertToSolid` — An optional boolean argument (default = True) to control whether or not watertight/closed NURBS Surfaces should be converted to Solids or left as Surfaces. If True, all NURBS geometry bodies will processed to determine if they represent a closed volume and if so the body will be converted to a NURBS Solid, otherwise the body will be a Surface. If False, no processing will be carried out on the generated NURBS bodies and they will remain as Surfaces This argument will be silently ignored if createNURBS is False (no NURBS bodies requested)
- `smoothLevel` — This controls how much smoothing will be applied to the created NURBS faces. High values can lose some detail in the face or lose its curvature. Low values can allow noise or rough faces to be created if the input data is not very clean.

### `apex.geometry.createFacetedBody(tessellation: apex.utility.PolyData, meshBody: apex.mesh.MeshBody = None, name: str = "", part: apex.Part = None, autoSmoothAnalyticFace: bool = True, createNURBS: bool = False, createNURBSWithAnalyticalFace: bool = True, cleanupNURBS: bool = True, convertToSolid: bool = True, smoothLevel: int = 2) -> DllExport apex.geometry.GeometryBodyCollection`
Creates one or more FacetedSurfaces/FacetdSolids from the input Tesselation2D and adds it to the input Part. The FacetedSurfaces/FacetdSolids are returned as a FacetedSurfaceCollection/FacetedSolidCollection If the input PolyData consists of more than one contiguous region of cells, one FacetedSurface/FacetedSolid will be generated for each contiguous region. If the input PolyData was generated using a SurfaceMesh/SolidMesh, that SurfaceMesh/SolidMesh will be associated to the FacetedSurface/FacetedSolid. If that SurfaceMesh/SolidMesh consisted of more than one contiguous mesh region, multiple FacetedSurfaces/FacetSolids will be created, one for each contiguous mesh region and each contiguous region of the original SurfaceMesh/SolidMesh will become a distinct SurfaceMesh/SolidMesh associated to the corresponding FacetedSurface/FacetedSolid.

- `tessellation` — The Tessellation object from which the faceted surface/Solid will be created. The FacetedSurface/FacetedSolid will be created using the points and cells from the Tessellation. The topology of the FacetedSurface/FacetedSolid (Vertices,Edges and Faces) will be created using the points, edges and faces provided by the vertex, edge and face properties of the Tesselation object.
- `meshBody` — An optional argument that to supply a MeshBody. If supplied, the attributes of the MeshBody (Materials, Sections) and Loads or Constraints that are applied to the MeshBody will be transferred from the MeshBody to the FacetedSurface/FacetedSolid. The MeshBody is expected to be the same meshBody used to generate the polyData and the method will threw an exception if the MeshBody and the polyData are not matched. If a MeshBody is not supplied, no attribute, load or constraint mapping will be performed
- `name` — The name (optional) that will be assigned to the FacetedSurface/FacetedSolid. If supplied, the name must be unique within the parent Part of the FacetedSurface/FacetedSolid otherwise the system will automatically rename the FacetedSurface/FacetedSolid to ensure name uniqueness. If omitted, the system will provide a default name - "Faceted Surface <n>" or "Faceted Solid <n>", where <n> is the lowest possible integer to ensure name uniqueness
- `part` — The Part that the FacetedSurface/FacetedSolid will be added to. This argument may be omitted if the meshBody argument is present in which case the FacetedSurface/FacetedSolid will be added to the Part that parents the meshBody. If both meshBody AND part are supplied the part argument will be silently ignored and the FacetedSurface/FacetedSolid will be added to the Part that parents the meshBody. If both meshBody and part are omitted the method will throw an exception
- `autoSmoothAnalyticFace` — An optional boolean argument (default =True) to identify analytic faces When True, all identified analytic faces will be display as blue color then original mesh will be automatically smoothed and used for faceted geometry body creation. When False, original orphan mesh will be used for facet geometry body creation.
- `createNURBS` — An optional boolean argument(default=False) to request creation of NURBS geometry bodies as well as feaceted geometry bodies. When True, one NURBS geometry body will be created for each faceted geometry body that is generated. When False, only faceted bodies will be created.
- `createNURBSWithAnalyticalFace` — An optional boolean argument (default =True) to identify analytic faces When True, all identified analytic faces will be display as blue color then original mesh will be automatically smoothed and used for NURBS body creation. When False, original orphan mesh will be used for NURBS body creation.
- `cleanupNURBS` — An optional argument(default=True) to control cleanup of any NURBS geometry bodies that are created. If True, all geometry bodies will be processed to remove faults and to replace NURBS based topology with analytical representations where possible. If False, no processing will be carried out on the generated NURBS bodies. This argument will be silently ignored if createNURBS is False(no NURBS bodies requested).
- `convertToSolid` — An optional boolean argument(default=True) to control whether or not watertight/closed surfaces should be converted to Solids or left as Surfaces. If True, all geometry bodies will be processed to determine if they represent a closed volume and if so the body will be converted to a Solid, otherwise the body will be a Surface. If False, no processing will be carried out on the generated bodies and they will remain as Surfaces.
- `smoothLevel` — An optional integer(default is 2) that will be used to determine how smoothly the created NURBS surface is. The valid range is 1 to 3 while level 3 will be smoothest and most of the noises from original mesh will be ignored.

### `apex.geometry.createGeometryExtrude(target: apex.EntityCollection, extrudeVector: apex.construct.Vector3D, extrusionDistance: float = 10, startOffsetDistance: float = 0) -> {apex.Entity:apex.geometry.GeometryBody}`
Creates GeometryBodies (Surfaces, Curves, Points) by extruding Surfaces, Faces, Edges, Vertices or Points along a vector.

- `target` — A collection of curve, wire body, surface, surface body, point, vertex
- `extrudeVector` — One or two point 3d locations up to three xyz locations defining direction
- `extrusionDistance` — The total extrude distance
- `startOffsetDistance` — The initial offset, or starting bound distance

Returns: Each Surface, Face, Curve, Edge, Point and Vertex in the input target is returned as a key and the associated value is the GeometryBody

### `apex.geometry.createGeometryRevolve(target: apex.EntityCollection, axisVector: apex.construct.Vector3D, axisPoint: apex.ILocation, angleOfRevolution: float = 360, startOffsetAngle: float = 0) -> {apex.Entity:apex.geometry.GeometryBody}`
Creates GeometryBodies (Surfaces, Curves, Points) by revolving Surfaces, Faces, Edges, Vertices or Points around an axis.

- `target` — A collection of curve, wire body, surface, surface body, point, vertex
- `axisVector` — One or two point 3d locations defining axis direction
- `axisPoint` — The location point of axis
- `angleOfRevolution` — The total rotation angle
- `startOffsetAngle` — A starting offset angle

Returns: Each Surface, Face, Curve, Edge, Point and Vertex in the input target is returned as a key and the associated value is the GeometryBody

### `apex.geometry.createGeometrySweepGuides(target: apex.EntityCollection, path: apex.EntityCollection, guides: apex.EntityCollection, profileSweepAlignmentMethod: apex.geometry.SweepProfileAlignmentMethod = apex.geometry.SweepProfileAlignmentMethod.Normal, islocked: bool = False, lockVector: apex.construct.Vector3D = apex.construct.Vector3D(0, 0, 0)) -> apex.geometry.GeometryBody`
Creates and returns a GeometryBody (Solid or Surface) by sweeping a profile (Surface, Faces, Curve or Edges) along a director path defined by a Curve or by multiple contiguous Edges and extended control of the shape of the generated body provided by additional guide paths.

- `target` — A collection of curve, wire body, surface, surface body
- `path` — The Sweep path(Curves, Edges) can be defined using a Curve or collection of contiguous Edges as it is swept along the lenght of it, it must always be smooth (no sharp corners)
- `guides` — The guides do not need to be smooth, but if any of them are not smooth (contain sharp corners) only a single profile can be supplied
- `profileSweepAlignmentMethod` — The Sweep Alignment option.
- `islocked` — wheather to use Lock Direction
- `lockVector` — define The Lock Direction

Returns: The resulting Geometry Body is added to the parent Part of the profile entity

### `apex.geometry.createGeometrySweepPath(target: apex.EntityCollection, path: apex.EntityCollection, scale: float = 0, twist: float = 0, profileSweepAlignmentMethod: apex.geometry.SweepProfileAlignmentMethod = apex.geometry.SweepProfileAlignmentMethod.Normal, islocked: bool = False, lockDirection: apex.construct.Vector3D = apex.construct.Vector3D(0, 0, 0), profileClamp: apex.geometry.SweepProfileClampingMethod = apex.geometry.SweepProfileClampingMethod.Smooth) -> apex.geometry.GeometryBody`
Creates and returns a GeometryBody (Solid, Surface) by sweeping target profile(s) represented by Surfaces, Faces, Curves or Edges along a director path defined using a Curve or collection of contiguous Edges. The cross section of the generated body matches the shape of the profile(s).

- `target` — A collection of curve, wire body, surface, surface body
- `path` — The Sweep path(Curves, Edges) can be defined using a Curve or collection of contiguous Edges as it is swept along the lenght of it
- `scale` — The Sweep scale that controls the shape of the generated body
- `twist` — The Sweep twist angle that controls the shape of the generated body
- `profileSweepAlignmentMethod` — An enumeration that controls the orientation of the profile relative to the normal plane of the director path
- `islocked` — wheather to use Lock Direction
- `lockDirection` — define The Lock Direction
- `profileClamp` — The Sweep Clamping magnitude option

Returns: the Geometry Body that is created is added to the parent Part of the target profile

### `apex.geometry.createGeometrySweepPathAlignFace(target: apex.EntityCollection, path: apex.EntityCollection, scale: float = 0, orientationSurface: apex.EntityCollection = None) -> apex.geometry.GeometryBody`
Creates and returns a GeometryBody by sweeping an input target profile along a director path and controlling the orientation of the profile using a Surface or collection of faces Faces.

- `target` — A collection of curve, wire body, surface, surface body
- `path` — The Sweep path(Curves, Edges) can be defined using a Curve or collection of contiguous Edges as it is swept along the lenght of it
- `scale` — The Sweep scale that controls the shape of the generated body
- `orientationSurface` — The Faces that guide the orientation of the target along the length of the director path are determined automatically by the method based on their proximity to the director path

Returns: The Geometry Body that is created is added to the parent Part of the target profile

### `apex.geometry.createMeshControlEdges(target: apex.EntityCollection, guides: apex.EntityCollection, touchingCurveSearchTolerance: float = NAN) -> apex.geometry.MeshControlEdgeCollection`
Creates and returns MeshControlEdges on the input target Faces using the input edges and curves. The input Curves and Edges are projected onto the target Solids, Surfaces and Faces. If a curve/edge has a valid projection onto a target Face, a MeshControlEdge is created on the Face. All MeshControlEdges that are created by the method are returned as a MeshControlEdgeCollection. If no MeshControlEdges are created, an empty collection is returned.

- `target` — collection of Faces
- `guides` — collection of Edges and Curves
- `touchingCurveSearchTolerance` — An optional tolerance (default = 10mm) controlling whether WireEdge that do not lie entirely ON the Faces/Surfaces of target will cause MeshControlEdges to be created. Under these circumstances, this tolerance can be used to create MeshControlEdges even though a substantial gap may exits between the WireEdge and the target Faces touchingCurveSearchTolerance represents a Length quantity and must be defined using the units of Length from the active script unit system.

Returns: created MeshControlEdges

### `apex.geometry.createMidSurfaceBetweenFaces(target1: apex.EntityCollection, target2: apex.EntityCollection = None, autoPair: bool = True) -> DllExport apex.EntityCollection`
creates mid-surface body for each face pair in the target list.

- `target1` — collection of solid face side A, always required
- `target2` — collection. Not required if auto pair is on
- `autoPair` — when on finds target 2 automatically

Returns: Collection of created bodies

### `apex.geometry.createMidSurfaceFixedOffset(target: apex.EntityCollection, oneHalf: bool, offsetDistance: float) -> DllExport apex.EntityCollection`
creates mid-surface body for each solid in the target list.

- `target` — collection of solid face
- `oneHalf` — Offsets half input value if True
- `offsetDistance` — Offset distance

Returns: Collection of created bodies

### `apex.geometry.createNurbsFromFacetedBody(facetbody: apex.geometry.GeometryBody, facesize: float = 0.0, densityLevel: int = 4) -> apex.geometry.GeometryBody`
This is the simple form of the Automatic Create NURBS From Facet Body tool. This takes as input a single Facetbody Surface or Solid, and returns a real geometry (NURBS) solid or surface. Never more than one solid or Surface will be returned. The size parameter is used to determine the approximate size of the created Faces. If the target is a Faceted Solid body, the output will usually be solid body, and if a Faceted Surface body, the result will normally be a single Surface Body. If the size is not specified, or the size is less than or equal to 0.0, Then it will be calculated automatically based on a fraction of the over all input Body.

- `facetbody` — Facet body (Surface or Solid) that will used as a target to extract a NURBS body. Only one is valid,and it is a required input.
- `facesize` — This is the optional face size to use when partitioning the facet body to create NURBS. If specified, or input is less than or equal to zero then the auto-size algorithm is used, else use the input length size.
- `densityLevel` — This parameter controls the face partition algorithm. The input is an integer in the range of 1 to 10. The higher the value, the more faces will be created, but each face will be less curved. The lower the value, the fewer faces will be created, then they will be larger and more complicated. The default value is 4.

### `apex.geometry.createPointCurveIntersect(targetCurves: apex.EntityCollection, intersectingCurves: apex.EntityCollection, allowDuplicatePoints: bool, createPointsAtClosestApproach: bool, createPointOnBothSides: bool) -> apex.EntityCollection`
create a point

- `targetCurves` — first collection of curves for intersection
- `intersectingCurves` — collection of curves to form intersections
- `allowDuplicatePoints` — Prevents duplicate intersections from creating duplicate points when True
- `createPointsAtClosestApproach` — Intersections are found at cloasest approach even if the curves to not intersect within modeling tolerance
- `createPointOnBothSides` — when curves do not intersect, then if createPointsAtClosestApproach is True, a point is created on both curves at closest approach when True. When False, the point is created only on the curve in stage 2.

Returns: Collection of created entities

### `apex.geometry.createPointCurveSurface(targetCurves: apex.EntityCollection, intersectingSurfaces: apex.EntityCollection) -> apex.EntityCollection`
Creates and returns Points at ther intersections of the input Curves and Surfaces/Faces/DatumPlanes.

- `targetCurves` — collection containing one or more Curves or Edges that will be evaluated for intersection with the intersectingSurfaces. Enitites int the collection that are not Curves or Edges will be silently ignored. Duplicate entities in the collection will be ignored.
- `intersectingSurfaces` — collection containing one or more Surfaces, Faces or DatumPlanes that will be evaluated for intersection with the targetCurves. Enitites int the collection that are not Surfaces, Faces or DatumPlanes will be silently ignored. Duplicate entities in the collection will be ignored.

Returns: Collection of created entities

### `apex.geometry.createPointLocation(target: apex.ILocationCollection) -> apex.EntityCollection`
DEPRECATED: In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. create a point.

- `target` — selected locations to create point

Returns: Collection of created entities

### `apex.geometry.createPointPickedLocation(target: apex.ILocationCollection) -> apex.EntityCollection`
DEPRECATED: This function has been deprecated since Jaguar and we intend to remove it in the next Apex release. Instead use api apex.geometry.createPointLocation(). create a point.

- `target` — selected locations to create point

Returns: Collection of created entities

### `apex.geometry.createPointXYZ(x: float, y: float, z: float) -> apex.geometry.Point`
create a point

- `x` — x coordinate
- `y` — y coordinate
- `z` — z coordinate

Returns: Created point

### `apex.geometry.createPolyData(target: apex.mesh.MeshBody, faceFeatureAngle: float = 40.0, edgeFeatureAngle: float = 40.0, useMaterialRegions: bool = True, useSectionRegions: bool = True, useLoadConstraintRegions: bool = True, splitFaceByFeature: bool = True, detailLevel: int = 3) -> DllExport apex.utility.PolyData`
Creates and returns a PolyData object from an input SurfaceMesh or SolidMesh. Based on the input arguments, the method determines which Nodes, Element Edges and Elements will best represent the Vertices, Edges and Faces of an equivalent geometry Surface/Solid and includes them as member data in the returned PolyData. The PolyData object can then be used as input to create a FacetedSurface/FacetedSolid although more usually some adjustment of the automatically calculated Vertex, Edge and Face topology groupings is required using the methods supplied by the PolyData class.

- `target` — The SurfaceMesh or SolidMesh from which the PolyData will be created
- `faceFeatureAngle` — An optional angle (default is 40 degrees) that will be used to automatically identify topology edges based on the angle between adjacent face normals in the tessellation. When a PolyData edge is shared by two faces and the angle between the face normals is greater than the faceFeatureAngle a topology edge will be created. This argument represents a measure of angle and must be supplied in the angle units defined in the active ScriptUnitSystem.
- `edgeFeatureAngle` — An optional angle (default is 40 degrees) that will be used to automatically identify topology Vertices based on the angle between adjacent edge normals in the PolyData. When a PolyData vertex is shared by two edges and the angle between the edge normals is greater than the edgeFeatureAngle a topology Vertex will be created. This argument represents a measure of angle and must be supplied in the angle units defined in the active ScriptUnitSystem.
- `useMaterialRegions` — An optional boolean value that indicates whether Material boundaries should be used to identify topology edges or not. The default value of True will cause topology edges to be created on all shared element edges where different materials are associated to each of the two elements. Setting the value to False causes the method to ignore material boundaries when determining the topology
- `useSectionRegions` — An optional boolean value that indicates whether Section boundaries should be used to identify topology edges or not. The default value of True will cause topology edges to be created on all shared element edges where different Sections are associated to each of the two elements. Setting the value to False causes the method to ignore Section boundaries when determining the topology
- `useLoadConstraintRegions` — An optional boolean value that indicates whether Load and Constraint application region boundaries will be used to identify topology edges or not. The default value of True will cause topology edges to be created on all shared element edges where different Load or Constraints are associated to each of the two elements. Setting the value to False causes the method to ignore Load and Constraint application region boundaries when determining the topology
- `splitFaceByFeature` — An optional boolean value that indicates whether basic geometry primitive will be identified and created as face or not, including sphere, cylinder, plane, fillet, torus, cone.
- `detailLevel` — An optional integer (default is 3 ) that will be used to decide how much details is going to be provided during identify basic geometry primitive. The valid range is 1 to 5 while level 5 will provide the most details and most number of faces will be created.

### `apex.geometry.createPolyDataList(target: apex.mesh.MeshBodyCollection, faceFeatureAngle: float = 40.0, edgeFeatureAngle: float = 40.0, useMaterialRegions: bool = True, useSectionRegions: bool = True, useLoadConstraintRegions: bool = True, splitFaceByFeature: bool = True, detailLevel: int = 3) -> DllExport[apex.utility.PolyData]`
Creates and returns a list of PolyData objects matching up with an input MeshBodyCollection. Based on the input arguments, the method determines which Nodes, Element Edges and Elements will best represent the Vertices, Edges and Faces of an equivalent MeshBody and includes them as member data in each returned PolyData object in the list. The PolyData object can then be used as input to create a FacetedBodies although more usually some adjustment of the automatically calculated Vertex, Edge and Face topology groupings is required using the methods supplied by the PolyData class.

- `target` — a MeshBodyCollection from which a list of PolyData will be created
- `faceFeatureAngle` — An optional angle (default is 40 degrees) that will be used to automatically identify topology edges based on the angle between adjacent face normals in the tessellation. When a PolyData edge is shared by two faces and the angle between the face normals is greater than the faceFeatureAngle a topology edge will be created. This argument represents a measure of angle and must be supplied in the angle units defined in the active ScriptUnitSystem.
- `edgeFeatureAngle` — An optional angle (default is 40 degrees) that will be used to automatically identify topology Vertices based on the angle between adjacent edge normals in the PolyData. When a PolyData vertex is shared by two edges and the angle between the edge normals is greater than the edgeFeatureAngle a topology Vertex will be created. This argument represents a measure of angle and must be supplied in the angle units defined in the active ScriptUnitSystem.
- `useMaterialRegions` — An optional boolean value that indicates whether Material boundaries should be used to identify topology edges or not. The default value of True will cause topology edges to be created on all shared element edges where different materials are associated to each of the two elements. Setting the value to False causes the method to ignore material boundaries when determining the topology
- `useSectionRegions` — An optional boolean value that indicates whether Section boundaries should be used to identify topology edges or not. The default value of True will cause topology edges to be created on all shared element edges where different Sections are associated to each of the two elements. Setting the value to False causes the method to ignore Section boundaries when determining the topology
- `useLoadConstraintRegions` — An optional boolean value that indicates whether Load and Constraint application region boundaries will be used to identify topology edges or not. The default value of True will cause topology edges to be created on all shared element edges where different Load or Constraints are associated to each of the two elements. Setting the value to False causes the method to ignore Load and Constraint application region boundaries when determining the topology
- `splitFaceByFeature` — This parameter turns on more advanced face identification. It will group faces by common curvature and mesh size in an attempt to reverse engineer the original CAD faces used to create the mesh. This algorithm will assume the mesh was created on traditional CAD geometry. This setting is not appropriate for organic shares, and facets/meshes that came from scan data, or topology optimization.
- `detailLevel` — An optional integer (default is 3 ) that will be used to decide how much details is going to be provided during identify basic geometry primitive. The valid range is 1 to 5 while level 5 will provide the most details and most number of faces will be created.

### `apex.geometry.createSphereByCoordinateSystem(name: str = "Sphere", description: str = "", radius: float = 100, coordinateSystem: apex.construct.CoordinateSystem = None, useLocalValue: bool = True) -> apex.geometry.Sphere`
Creates and returns a parametric geometry solid Sphere using an external coordinate system to define the origin and orientation of the Sphere and radius to define its size.

- `name` — An optional name for the Sphere that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'Sphere ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Sphere 1234'.
- `description` — An optional description for the Sphere that will be created. If omitted the description will be left blank.
- `radius` — The radius of the Sphere. radius is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem.
- `coordinateSystem` — The CoordinateSystem that defines the origin and orientation of the Sphere.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.

Returns: created Sphere

### `apex.geometry.createSphereByLocationOrientation(name: str = "Sphere", description: str = "", radius: float = 100, origin: apex.ILocation = None, orientation: apex.IOrientation = None, useLocalValue: bool = True) -> apex.geometry.Sphere`
Creates and returns a parametric geometry solid Sphere using an input origin, orientation and radius.

- `name` — An optional name for the Sphere that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'Sphere ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Sphere 1234'.
- `description` — An optional description for the Sphere that will be created. If omitted the description will be left blank.
- `radius` — The radius of the Sphere. radius is a Length quantity and must be defined in the units of Length in the active ScriptUnitSystem.
- `origin` — The origin of the Sphere as an ILocation.
- `orientation` — The orientation of Sphere as an IOrientation.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.

Returns: created Sphere

### `apex.geometry.createSurfaceLofted(name: str, target: [apex.EntityCollection], loftClampingMethod: LoftClampingMethod = apex.geometry.LoftClampingMethod.No, clampStartProfile: bool = True, clampEndProfile: bool = True, stitch: bool = True) -> apex.geometry.GeometryBody`
boolean subtract subtractingEntity from target

- `name` — name of created solid
- `target` — collection of edges
- `loftClampingMethod` — switch between No, Tangent and Curvature
- `clampStartProfile` — Wether to clamp at start profile.
- `clampEndProfile` — Wether to clamp at end profile.
- `stitch` — Wether to stitch loft body wiht original body.

Returns: created body

### `apex.geometry.curveCollection(curveList: [Curve] = []) -> CurveCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.CurveCollection().

- `curveList` — optional list of Curves to add to the collection.

### `apex.geometry.defeature(target: GeometryFeatureCollection, createSeedPointInDefaturedHole: bool = False) -> apex.geometry.ZResultDefeature`
Remove features on the selected geometries.

- `target` — the collection of features be removed.
- `createSeedPointInDefaturedHole` — whether create seed point

### `apex.geometry.defeatureByFeatureRange(target: GeometryFeatureCollection, maxFeatureSize: float, minFeatureSize: float, createSeedPointInDefaturedHole: bool = False) -> apex.geometry.ZResultDefeature`
Remove features on the selected geometries.

- `target` — the collection of features be removed.
- `maxFeatureSize` — the max Feature size
- `minFeatureSize` — the min Feature size
- `createSeedPointInDefaturedHole` — whether create seed point

Returns: Defeature results

### `apex.geometry.defeatureCustomFeature(target: apex.EntityCollection, featureTemplate: apex.EntityCollection, lentghTolerance: float, angleTolerance: float, retainedFeatures: apex.EntityCollection) -> apex.geometry.ZResultDefeatureCustomFeature`
this method finds all features in the target bodiy list, and returns them in a list of lists.

- `target` — collection of surface bodies to search for features in
- `featureTemplate` — collection of contigous edges in a body defining feature template
- `lentghTolerance` — length tolerance for finding feature
- `angleTolerance` — angle tolerance for finding feature
- `retainedFeatures` — collection of edges to retain. Any found feature that contains any of these edges will not be defeatured

Returns: ZResultIdentifyCustomFeature

### `apex.geometry.defeatureTopology(target: apex.EntityCollection, createSeedPointInDefaturedHole: bool = False) -> apex.geometry.ZResultDefeature`
Remove features on the selected geometries.

- `target` — the collection of topology entities from which the features are to be removed.
- `createSeedPointInDefaturedHole` — whether create seed point

Returns: Defeature results

### `apex.geometry.deletePairIncrementalMidSurface(targetPairs: apex.EntityCollection) -> DllExport None`
delete pairs

- `targetPairs` — collection of faces, one from each pair to delete

### `apex.geometry.displayRenderStyle(renderStyle: apex.session.DisplayRenderStyle) -> None`
Model Browser control for render style display in the model.

- `renderStyle` — the enumeration for the render style type DisplayRenderStyle.HiddenLinesDisplayRenderStyle.WireframeDisplayRenderStyle.ShadedDisplayRenderStyle.ShadedWithEdges

Returns: None

### `apex.geometry.dragEdge(targetEdge: apex.Entity, snapEntity: apex.Entity = None, distance: float = 0.0, dragEdgeBehavior: apex.geometry.DragEdgeBehavior = apex.geometry.DragEdgeBehavior.Follow, lineBehavior: apex.geometry.DragVertexBehavior = apex.geometry.DragVertexBehavior.KeepCurved) -> Entity`
drag edges

- `targetEdge` — edge being dragged
- `snapEntity` — Optianal argument used if the extent of the drag operation is defined by another object(up to). Support entities are Face, Edge, Vertex and DatumPlane.
- `distance` — Drag distance. distance is a Length quantity and must be provided in the units of Length in the active ScriptingUnitSystem.
- `dragEdgeBehavior` — Edge Drag Behavior Methods: Options are: 1. apex::geometry::DragEdgeBehavior.Follow 2. apex::geometry::DragEdgeBehavior.Extrude 3. apex::geometry::DragEdgeBehavior.Stretch
- `lineBehavior` — Dragging edge's adjacent edge behavior: Options are: apex::geometry::DragVertexBehavior.ForceStraightapex::geometry::DragVertexBehavior.KeepCurved

Returns: dragged edge

### `apex.geometry.dragVertex(targetVertex: apex.Entity, snapMode: SnapModeType, location: apex.ILocation, snapEntity: apex.Entity = None, dragVertexBehavior: apex.geometry.DragVertexBehavior = apex.geometry.DragVertexBehavior.ForceStraight) -> Entity`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. drag vertex.

- `targetVertex` — vertex or point being dragged
- `snapMode` — snap type Snap Mode Type. Options are: SnapModeType.OnEdgeSnapModeType.ExtensionSnapModeType.OnSurfaceSnapModeType.NoneSnapModeType.MidPointSnapModeType.VertexSnapModeType.TangentSnapModeType.Perpendicular
- `location` — picked location
- `snapEntity` — Optianal argument used if the extent of the drag operation is defined by another object(up to). Support entities are Face, Edge, Vertex and DatumPlane.
- `dragVertexBehavior` — Vertex Drag Behavior Methods: Options are: apex::geometry::DragVertexBehavior.ForceStraightapex::geometry::DragVertexBehavior.KeepCurved

Returns: dragged vertex

### `apex.geometry.edgeCollection(edgeList: [Edge] = []) -> EdgeCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.EdgeCollection().

- `edgeList` — optional list of Edges to add to the collection.

### `apex.geometry.editIncrementalMidSurfaceMethod(target: apex.EntityCollection, method: MidSurfaceIncrementalMethod) -> DllExport None`
modify the incremental midsurface method

- `target` — collection of faces, one face from a face pair
- `method` — Method to use for offset: Options are: MidSurfaceIncrementalMethod.TaperedMidSurfaceIncrementalMethod.LeftMidSurfaceIncrementalMethod.RightMidSurfaceIncrementalMethod.Planar

### `apex.geometry.editPairIncrementalMidSurface(targetPair: apex.Entity, sideA: apex.EntityCollection, sideB: apex.EntityCollection) -> DllExport{str:apex.geometry.FaceCollection}`
create or modify a pair

- `targetPair` — one face from a face pair or unpaird face to create new pair
- `sideA` — updated side A of face pair or side A unpaired faces
- `sideB` — collection when on finds target 2 automatically

Returns: the updated result. The key of the dictionary is a string type and the value is a FaceCollection. The dictionary has the keys "Side 1" and "Side 2". The associated values are FaceCollections contain the Faces associated with each Side.

### `apex.geometry.enterIncrementalMidSurface(: None) -> DllExport bool`
enter Incremental MidSurface operation mode

Returns: True if successfully entered or False if failed

### `apex.geometry.evaluateAngleBetweenCurves(curve1: Curve, curve2: Curve, sharedVertex: Vertex) -> float`
evaluateAngleBetweenCurves

- `curve1` — first curve
- `curve2` — second curve
- `sharedVertex` — a shaired vertex

Returns: angle between edges

### `apex.geometry.evaluateAngleBetweenEdges(edge1: Edge, edge2: Edge, sharedVertex: Vertex) -> float`
evaluateAngleBetweenEdges

- `edge1` — first edge
- `edge2` — second edge
- `sharedVertex` — a shaired vertex

Returns: angle between edges

### `apex.geometry.evaluateAngleBetweenFaces(face1: Face, face2: Face, sharedEdge: Edge, numCheckPoints: int = 2) -> float`
evaluateAngleBetweenFaces

- `face1` — first Face
- `face2` — second Face
- `sharedEdge` — a shaired edge
- `numCheckPoints` — number of checkpoints

Returns: angle between edges

### `apex.geometry.exitIncrementalMidSurface(: None) -> DllExport bool`
exit Incremental MidSurface operation mode

Returns: True if successfully exit or False if failed

### `apex.geometry.extendToSurfaces(target: apex.EntityCollection, searchDist: float, cleanupAutomatically: bool, autoCleanupTol: float = NAN, stitchAfterExtend: bool = True, surfaceFlatteningSensitivity: int = 5, planarSurfaceAlignmentSensitivity: int = 4) -> apex.EntityCollection`
Extend surfaces.

- `target` — collection of sheetbody, general body
- `searchDist` — max extend search distance
- `cleanupAutomatically` — setting to turn on cleanup mode
- `autoCleanupTol` — contoroles if key vertex at curvature changes should be retained.
- `stitchAfterExtend` — when true stitch after done, else do not.
- `surfaceFlatteningSensitivity` — TODO Documentation
- `planarSurfaceAlignmentSensitivity` — TODO Documentation

Returns: Collection of modified bodies

### `apex.geometry.extractPairIncrementalMidSurface(target: apex.EntityCollection, extendTrim: bool, splitOnThickness: bool) -> DllExport apex.EntityCollection`
extract midsurface from identifed face pair

- `target` — collection of faces, one from each pair to extract
- `extendTrim` — true if trim and extend operations are to be done
- `splitOnThickness` — true if create splits where thicknesses change

Returns: Collection of created bodies

### `apex.geometry.faceCollection(faceList: [Face] = []) -> FaceCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.FaceCollection().

- `faceList` — optional list of Faces to add to the collection.

### `apex.geometry.fillerSurface(target: apex.EntityCollection, locations: apex.ILocationCollection = apex.ILocationCollection(), retainReferenceCurveEdges: bool = False) -> apex.Entity`
create fillter surfaces

- `target` — collection of points (vertex or 0d body) or edges
- `locations` — the collection of geometry marker point to filler surface
- `retainReferenceCurveEdges` — The new toggle retainReferenceCurveEdges is False by default. When this is off (False), all edges that are referenced in the filler operation, or that are pre-existing on top of new filler surface edges are removed to reduce extra topology. When this toggle is True, then these edges are all retained so those edges can be reused again. The input edges referenced no longer have to all be in the same Part. Surface edges are referenced, and they are in different Parts, the Part that contains the first edge in the list will get stitched to the new body.

Returns: created entity

### `apex.geometry.findExteriorLoops(target: FaceCollection) -> EdgeLoopCollection`
Finds and returns the exterior EdgeLoops from the input Faces.

- `target` — The set of Faces, as a FaceCollection, that the method will process to find the exterior EdgeLoops.

Returns: exterior EdgeLoopCollection

The input Faces must be (Edge) contiguous and form a manifold region otherwire the method will throw an exception.

### `apex.geometry.findFixSmallSurfaceAndCurveFeatures(target: apex.EntityCollection, enableGapDetection: bool, enableOverhangDetection: bool, enableSmallEdgeDetection: bool, tolerance: float, autoFix: bool) -> apex.geometry.ZResultIdentifyFixSmallFeatures`
identify and optionally repairs small surface/curve features such as gaps, overhangs, and small edges that might cause problems.

- `target` — collection of Geometry objects to be checked for small features. Only Solids, Surfaces and Wires are supported any other Geometry types will be skipped by the method
- `enableGapDetection` — Detects gaps whose width is less than the specified value.
- `enableOverhangDetection` — Detects overhangs whose length is less than the specified value.
- `enableSmallEdgeDetection` — Detects edges whose length is less than the specified value.
- `tolerance` — Tolerance value for geometry cleanup
- `autoFix` — Option to select whether each feature will be automatically fixed when selected.

Returns: ZResultIdentifyFixSmallFeatures

### `apex.geometry.findGeometryFaults(target: apex.EntityCollection) -> apex.geometry.ZResultFindGeometryFaults`
Identify geometry faults in the model.

- `target` — collection of Geometry objects to be checked for Geometry Faults. Only Solids and Surfaces are supported any other Geometry types will be skipped by the method

Returns: ZResultFindGeometryFaults

### `apex.geometry.findInteriorLoops(target: FaceCollection) -> EdgeLoopCollection`
Finds an returns all interior EdgeLoops from the input set of Faces.

- `target` — The set of Faces, as a FaceCollection, that the method will process to find the interior EdgeLoops.

Returns: interior EdgeLoopCollection

The input Faces must be (Edge) contiguous and form a manifold region otherwire the method will throw an exception.

### `apex.geometry.findManifoldRegions(target: EntityCollection) -> [FaceCollection]`
Finds and returns contiguous manifold regions from the input set of Faces and/or Surfaces.

- `target` — A collection of Faces and/or Surfaces from which the contiguous regions will be extracted.

Returns: contiguous manifold regions

The manifold regions are returned as a List of FaceCollections, each FaceCollection represents a contiguous manifold region. Surface or Face they will be silently ignored.

### `apex.geometry.findPairIncrementalMidSurface(target: apex.Entity, thicknessRatio: float = 5.0) -> DllExport{str:{dict}}`
Finds and returns pairs of opposing faces in the input Solid. Multiple "Face Pairs" may be returned and each pair includes the faces for both sides of the pair - "Side 1" and "Side 2". Each Side of a Face Pair may include one or more geometry Faces. Face pairs will be identified and persisted when this function is first called on a Solid. Subsequent calls return the previously calculated face pairs, although these pairs may be modified from the originals using the interactive tools or associated scripting APIs.

- `target` — The Solid geometry body from which the face pairs will be extracted
- `thicknessRatio` — Parameter used to prevent unreasonable pairs from being created. thicknessRatio represents the ratio of the Area of a Face to the square of distance to an opposing Face in the Solid

Returns: Face pairs are returned in a nested dictionary. The primary dictionary uses a string key and has an associated Dictionary value. The primary key string is generated by concatenating the prefix "Pair " with a unique integer, starting at '1'. This rule generates primary keys such as "Pair 1", "Pair 2" etc. The secondary dictionary contains the Faces for each pair. The key is a string type and the value is a FaceCollection. Each secondary dictionary has the keys "Side 1" and "Side 2". The associated values are FaceCollections containing the Faces associated with each Side.

### `apex.geometry.geometryBodyCollection(bodyList: [GeometryBody] = []) -> GeometryBodyCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.GeometryBodyCollection().

- `bodyList` — optional list of Bodys to add to the collection.

### `apex.geometry.geometryFeatureCollection(pGeometryFeatureCollection: GeometryFeatureCollection, featureType: apex.EntityType) -> GeometryFeatureCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.GeometryFeatureCollection().

- `pGeometryFeatureCollection` — optional collection of all GeometryFeatures.
- `featureType` — optional special type of GeometryFeatures.

### `apex.geometry.geometrySimplify(target: apex.EntityCollection, cleanTopology: bool, cleanTopologyTolerance: float, optimizeGeometry: bool, optimizeGeometyTolerance: float) -> apex.geometry.ZResultGeometrySimplify`
simplifies the input geometries

- `target` — the collection of geometries be simplified.
- `cleanTopology` — Enables (True) or Disables (False) topology cleanup during geometry simplification
- `cleanTopologyTolerance` — Defines the the upper bound on deviation between original and repaired geometry. This parameter is REQUIRED if "cleanTopology" is TRUE
- `optimizeGeometry` — Enables (True) or Disables (False) optimization of the underlying geometry representation. Optimization will attempt to replace complex represenattons of geometry (such a Splines and BREPS with) with simpler representations (arcs, cylinders etc,)
- `optimizeGeometyTolerance` — Missing, add it for avoiding warning

Returns: ZResultGeometrySimplify

### `apex.geometry.getBox(pathName: str) -> Box`
Get a Box in a Model.

- `pathName` — of the Box to get including the model name as in 'MyModel/Assembly1/Part1/Box 1'.

Returns: the Box

### `apex.geometry.getBoxes(target: [{str:str}]) -> BoxCollection`
Get a collection of Boxes, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the Boxes of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a BoxCollection of the requested Boxes

### `apex.geometry.getCells(target: [{str:str}]) -> CellCollection`
Get a collection of Cells, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the cells of bodies to retrieve. Valid keys are 'path' and 'ids'.

Returns: a CellCollection of the requested Cells

### `apex.geometry.getCurve(pathName: str) -> Curve`
Get a Curve in a Model.

- `pathName` — of the curve to get including the model name as in 'MyModel/Assembly1/Part1/Curve1'.

Returns: the created curve

### `apex.geometry.getCurves(target: [{str:str}]) -> CurveCollection`
Get a collection of Curves, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the curves of bodies to retrieve. Valid keys are 'path' and 'name'.

Returns: a CurveCollection of the requested Curves

### `apex.geometry.getCylinder(pathName: str) -> Cylinder`
Get a Cylinder in a Model.

- `pathName` — of the Cylinder to get including the model name as in 'MyModel/Assembly1/Part1/Cylinder 1'.

Returns: the Cylinder

### `apex.geometry.getCylinders(target: [{str:str}]) -> CylinderCollection`
Get a collection of Cylinders, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the Boxes of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a CylinderCollection of the requested Cylinders

### `apex.geometry.getEdges(target: [{str:str}]) -> EdgeCollection`
Get a collection of Edges, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the edges of bodies to retrieve. Valid keys are 'path' and 'ids'.

Returns: a EdgeCollection of the requested Edges

### `apex.geometry.getEllipsoid(pathName: str) -> Ellipsoid`
Get a Ellipsoid in a Model.

- `pathName` — of the Ellipsoid to get including the model name as in 'MyModel/Assembly1/Part1/Ellipsoid 1'.

Returns: the Ellipsoid

### `apex.geometry.getEllipsoids(target: [{str:str}]) -> EllipsoidCollection`
Get a collection of Ellipsoids, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the Ellipsoids of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a EllipsoidCollection of the requested Ellipsoids

### `apex.geometry.getFaces(target: [{str:str}]) -> FaceCollection`
Get a collection of Faces, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the faces of bodies to retrieve. Valid keys are 'path' and 'ids'.

Returns: a FaceCollection of the requested Faces

### `apex.geometry.getFacetedCurve(pathName: str) -> FacetedCurve`
Get a Faceted Curve in a Model.

- `pathName` — of the faceted curve to get including the model name as in 'MyModel/Assembly1/Part1/Faceted Curve1'.

Returns: the created facted curve

### `apex.geometry.getFacetedCurves(target: [{str:str}]) -> FacetedCurveCollection`
Get a collection of Faceted Curves, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the faceted curves of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a FacetedCurveCollection of the requested Faceted Curves

### `apex.geometry.getFacetedSolid(pathName: str) -> FacetedSolid`
Get a Faceted Solid in a Model.

- `pathName` — of the faceted solid to get including the model name as in 'MyModel/Assembly1/Part1/Faceted Solid1'.

Returns: the created faceted solid

### `apex.geometry.getFacetedSolids(target: [{str:str}]) -> FacetedSolidCollection`
Get a collection of Faceted Solids, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the faceted solids of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a FacetedSolidCollection of the requested Faceted Solids

### `apex.geometry.getFacetedSurface(pathName: str) -> FacetedSurface`
Get a FacetedSurface in a Model.

- `pathName` — of the faceted surface to get including the model name as in 'MyModel/Assembly1/Part1/Faceted Surface1'.

Returns: the created faceted surface

### `apex.geometry.getFacetedSurfaces(target: [{str:str}]) -> FacetedSurfaceCollection`
Get a collection of Faceted Surfaces, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the facetted surfaces of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a FacetedSurfaceCollection of the requested Faceted Surfaces

### `apex.geometry.getGeometryBodies(target: [{str:str}]) -> GeometryBodyCollection`
Get a collection of GeometryBodies, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the geometry bodies of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a GeometryBodyCollection of the requested GeometryBodies

### `apex.geometry.getGeometryBody(pathName: str) -> GeometryBody`
Get a GeometryBody in a Model.

- `pathName` — of the body to get including the model name as in 'MyModel/Assembly1/Part1/Solid1'.

Returns: the created body

### `apex.geometry.getPoint(pathName: str) -> Point`
Get a Point in a Model.

- `pathName` — of the point to get including the model name as in 'MyModel/Assembly1/Part1/Point1'.

Returns: the created point

### `apex.geometry.getPoints(target: [{str:str}]) -> PointCollection`
Get a collection of Points, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the points of bodies to retrieve. Valid keys are 'path' and 'name'.

Returns: a PointCollection of the requested Points

### `apex.geometry.getSolid(pathName: str) -> Solid`
Get a Solid in a Model.

- `pathName` — of the solid to get including the model name as in 'MyModel/Assembly1/Part1/Solid1'.

Returns: the created solid

### `apex.geometry.getSolids(target: [{str:str}]) -> SolidCollection`
Get a collection of Solids, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the solids of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a SolidCollection of the requested Solids

### `apex.geometry.getSphere(pathName: str) -> Sphere`
Get a Sphere in a Model.

- `pathName` — of the Sphere to get including the model name as in 'MyModel/Assembly1/Part1/Sphere 1'.

Returns: the Sphere

### `apex.geometry.getSpheres(target: [{str:str}]) -> SphereCollection`
Get a collection of Spheres, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the Spheres of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a SphereCollection of the requested Spheres

### `apex.geometry.getSurface(pathName: str) -> Surface`
Get a Surface in a Model.

- `pathName` — of the surface to get including the model name as in 'MyModel/Assembly1/Part1/Surface1'.

Returns: the created surface

### `apex.geometry.getSurfaces(target: [{str:str}]) -> SurfaceCollection`
Get a collection of Surfaces, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the surfaces of parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a SurfaceCollection of the requested Surfaces

### `apex.geometry.getVertices(target: [{str:str}]) -> VertexCollection`
Get a collection of Vertices, specified by target list of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the vertices of bodies to retrieve. Valid keys are 'path' and 'ids'.

Returns: a VertexCollection of the requested Vertices

### `apex.geometry.identifyCustomFeature(target: apex.EntityCollection, featureTemplate: apex.EntityCollection, lentghTolerance: float, angleTolerance: float) -> apex.geometry.ZResultIdentifyCustomFeature`
this method finds all features in the target bodiy list, and returns them in a list of lists.

- `target` — list of surface bodies to search for features in
- `featureTemplate` — collection of contigous edges in a body defining feature template
- `lentghTolerance` — length tolerance for finding feature
- `angleTolerance` — angle tolerance for finding feature

Returns: ZResultIdentifyCustomFeature

### `apex.geometry.identifyFeature(target: apex.EntityCollection) -> apex.geometry.ZResultIdentifyFeature`
Identify features on the input collection of bodies.

- `target` — the apex::EntityCollection of bodies for identifying features on them

Returns: ZResultIdentifyFeature

### `apex.geometry.identifyFixSmallFeatures(target: apex.EntityCollection, enableSmallEdgeCleanup: bool, enableSmallFaceCleanup: bool, enableSliverSurfaceCleanup: bool, enableSpikeSurfaceCleanup: bool, enableSheetBodyCrackCleanup: bool, autoFix: bool, tolerance: float) -> apex.geometry.ZResultIdentifyFixSmallFeatures`
Finds and optionally repairs small geometry artifacts.

- `target` — collection of Solid or Surface Geometry objects to checked. Other Geometry types will be skipped by the method
- `enableSmallEdgeCleanup` — Enables (True) a=or Disables (False) detection and optional removal of short edges
- `enableSmallFaceCleanup` — Detects and removes faces which would fit within a sphere with a radius of the specified value.
- `enableSliverSurfaceCleanup` — Detects and removes surfaces which exceed a pre-set aspect ratio and have a maximum edge to edge distance between two edges of the same face that is less than the specified value.
- `enableSpikeSurfaceCleanup` — Detects and removes surfaces formed by two adjacent edges where the distance between a vertex and the other edge is less than the specified value.
- `enableSheetBodyCrackCleanup` — Detects and removes cracks in sheet bodies with a maximum width less than the specified value.
- `autoFix` — Option to select whether each feature will be automatically fixed when selected.
- `tolerance` — Tolerance value for geometry cleanup

Returns: ZResultIdentifyFixSmallFeatures

### `apex.geometry.intersectBoolean(target: apex.EntityCollection, retainOriginals: bool) -> apex.EntityCollection`
boolean intersect

- `target` — Collection of solids or surfaces to intersect
- `retainOriginals` — Keep all original solid or surface if True

Returns: Collection of modified bodies

### `apex.geometry.mergeBoolean(target: apex.EntityCollection, retainOriginalBodies: bool, mergeSolidsAsCells: bool = False) -> apex.EntityCollection`
boolean merge the entities

- `target` — Collection of solids, surfaces or solid cells
- `retainOriginalBodies` — Keep original entities when True
- `mergeSolidsAsCells` — Merge solid as cells when True

Returns: Collection of modified bodies

### `apex.geometry.mergePairIncrementalMidSurface(target: apex.Entity, mergePairs: apex.EntityCollection) -> DllExport None`
merge pairs

- `target` — face from face pair
- `mergePairs` — collection of faces, one from each pair to merge with target

### `apex.geometry.pointCollection(pointList: [Point] = []) -> PointCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.PointCollection().

- `pointList` — optional list of Points to add to the collection.

### `apex.geometry.pushPull(target: apex.EntityCollection, method: PushPullMethod, behavior: PushPullBehavior, removeInnerLoops: bool, createBooleanUnion: bool, distance: float, direction: [float]) -> apex.EntityCollection`
push/pull surfaces

- `target` — faces to pull, surface or solid.
- `method` — One of: ["normal","fillet","chamfer"]
- `behavior` — one of: ["followShap","extrude","stretch"]
- `removeInnerLoops` — true removes the inner loops of the surfaces. False keeps the inner loops faces
- `createBooleanUnion` — force unite instead of subtract
- `distance` — distance meaning varies depending on method: normal = distance is normal distance fillet = distance is radius chamfer = distance is chamfer depth
- `direction` — missing, add for avoiding warning

Returns: collection of created or modified bodies

### `apex.geometry.pushPullUpto(target: apex.EntityCollection, method: PushPullMethod, behavior: PushPullBehavior, removeInnerLoops: bool, createBooleanUnion: bool, uptoFace: apex.Entity) -> apex.EntityCollection`
push/pull surfaces

- `target` — faces to pull, surface or solid.
- `method` — One of: ["normal","fillet","chamfer"]
- `behavior` — one of: ["followShap","extrude","stretch"]
- `removeInnerLoops` — true removes the inner loops of the surfaces. False keeps the inner loops faces
- `createBooleanUnion` — force unite instead of subtract
- `uptoFace` — The Face or DatumPlane that is used to define the push-pull distance.

Returns: collection of created or modified bodies

### `apex.geometry.removeVertex(targetVertex: apex.EntityCollection, keepAtCurvatureChange: bool) -> apex.EntityCollection`
removes existing vertex from an edge

- `targetVertex` — collection of vertex to remove from body
- `keepAtCurvatureChange` — toggle where key vertex are kept when mulitple vertex picked (box picked vertex)

Returns: collection of newly created edges

### `apex.geometry.solidCollection(solidList: [Solid] = []) -> SolidCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.SolidCollection().

- `solidList` — optional list of Solids to add to the collection.

### `apex.geometry.split(target: apex.EntityCollection, splitter: apex.EntityCollection, splitBehavior: GeometrySplitBehavior = apex.geometry.GeometrySplitBehavior.Partition) -> apex.EntityCollection`
Split Geometry Bodies and Topologies with Surfaces, Faces or DatumPlanes.

- `target` — collection of objects to split. All objects of type Solid, Cell, Surface, Face, Curve or Edge are supported If the collection contains other entity types they will be silently ignored.
- `splitter` — collection of objects that will be used to split the target. All objects of type Surface, Face, and DatumPlane are supported If the collection contains other entity types they will be silently ignored.
- `splitBehavior` — An optional argument that determines whether Solids in target will be split into discrete Solids or partitioned into Cells. splitBehavior is an enumeration of type apex.geometry.GeometrySplitBehavior with a default values of apex.geometry.GeometrySplitBehavior.Partition. The default value will cause the method to partition Solids into multiple Cells within the original Solid. Setting the value apex.geometry.GeometrySplitBehavior.Split will cause the input Solid to be divided into separate discrete Solids. This argument has no effect on target Surfaces, Faces, Curves, Edges or Cells.

Returns: Collection of new and or modified bodies

An argument is provided to control whether Solids are split into discrete Solids or partitioned into multi Cells.

### `apex.geometry.splitCurvesWithCurves(target: apex.EntityCollection, splitter: apex.EntityCollection, useOnlyNearbySplitters: bool = False, stitch: bool = False) -> apex.geometry.ZResultSplitCurvesWithEntities`
Splits one or more target Curves/Edges with one or more splitter Curves/Edges by finding points on the target entities where the splitter entities intersect, or project along the target normal, onto the target.

- `target` — the set of geometry Curves or Edges that the method will target for splitting. If the target includes a mixture of Curves and Edges they must be supplied as an EntityCollection. If the target includes only Curves or Only Edges they may supplied as a CurveCollection or EdgeCollection respectively.
- `splitter` — the collection of geometry Curves and/or Edges that will be used to split the target entities. If the collection of splitter entities includes both Curves and Edges they must be supplied as an EntityCollection. If the collection contains only Curves or only Edges they may be supplied as a CurveCollection or EdgeCollection respectively.
- `useOnlyNearbySplitters` — optional boolean value to control the extent of the splitting objects that will be used to split the target entities. If True only splitting entities that are close to target entities will be considered. For each target entity, the system will determine which of the splitting entities is close to the target and will split the target entity only using the nearby splitting entities. This option is very useful if, for convenience, a large number of target and/or splitting entities have been provided. It results in the target entities only being split by those splitting entities that intersect (within tolerance) the target entities. If False (the default), ALL of the splitting entities will be considered for each target entity. For each target entity the system will attempt to find the projected intersection points of all of the splitter entities onto the target entity and will split the target entity all of the projected intersection points. Use this option if you intend to split the target entities with splitter entities that are remote for the targets.
- `stitch` — optional boolean value to control whether or not the system will attempt to stitch curves together after splitting. If False (the default) the system will perform no stitching after splitting - the same number of curves will be present after splitting as before. If True, the system will group all Curves and/or Edges in the target by Part and then for each Group of Curves/Edges the system will stitch all Curves (including the parent Curves of all Edges) that share vertices (introduced by splitting) into contiguoue Curve bodies. This may result in fewer curves existing after splitting than existed before.

Returns: ZResultSplitCurvesWithEntities result object

An option is provided to control splitting based on whether or not the projected intersection on the target entity is close to the splitter object (a true intersection) or further away (a projected intersection). An option is provided to stitch curves together after splitting.

### `apex.geometry.splitCurvesWithPoints(target: apex.EntityCollection, locations: apex.ILocationCollection = apex.ILocationCollection(), splitter: apex.EntityCollection = None, useOnlyNearbySplitters: bool = False) -> apex.geometry.ZResultSplitCurvesWithEntities`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. Splits one or more target Curves/Edges with one or more splitter Points/Vertices by finding points on the target entities where the splitter entities intersect the target entities.

- `target` — the set of geometry Curves or Edges that the method will target for splitting. If the target includes a mixture of Curves and Edges they must be supplied as an EntityCollection. If the target includes only Curves or Only Edges they may supplied as a CurveCollection or EdgeCollection respectively
- `locations` — The objects will be used to split the target entities
- `splitter` — the collection of geometry Points/Vertices that will be used to split the target entities
- `useOnlyNearbySplitters` — optional boolean value to control the extent of the splitting objects that will be used to split the target entities. If True only splitting entities that are close to target entities will be considered. For each target entity, the system will determine which of the splitting entities is close to the target and will split the target entity only using the nearby splitting entities. This option is very useful if, for convenience, a large number of target and/or splitting entities have been provided. It results in the target entities only being split by those splitting entities that intersect (within tolerance) the target entities. If False (the default), ALL of the splitting entities will be considered for each target entity. For each target entity the system will attempt to find the projected intersection points of all of the splitter entities onto the target entity and will split the target entity all of the projected intersection points. Use this option if you intend to split the target entities with splitter entities that are remote for the targets.

Returns: ZResultSplitCurvesWithEntities result object

An option is provided to control splitting based on whether or not the projected intersection on the target entity is close to the splitter object (a true intersection) or further away (a projected intersection)

### `apex.geometry.splitCurvesWithSurfaces(target: apex.EntityCollection, splitter: apex.EntityCollection, useOnlyNearbySplitters: bool = False) -> apex.geometry.ZResultSplitCurvesWithEntities`
Splits one or more target Curves/Edges with one or more splitter Surfaces/Faces/DatumPlanes by finding points on the target entities where the splitter entities intersect the target entities.

- `target` — the set of geometry Curves or Edges that the method will target for splitting. If the target includes a mixture of Curves and Edges they must be supplied as an EntityCollection. If the target includes only Curves or Only Edges they may supplied as a CurveCollection or EdgeCollection respectively
- `splitter` — the collection of geometry Surfaces, Faces and/or DatumPlanes that will be used to split the target entities. If the collection of splitter entities includes a mixture of Surfaces, Faces and DatumPlanes they must be supplied as an EntityCollection. If the collection contains only Surfaces, only Faces or only DatumPlanes they may be supplied as a SurfaceCollection, a FaceCollection or a construct::DatumPlaneCollection respectively.
- `useOnlyNearbySplitters` — optional boolean value to control the extent of the splitting objects that will be used to split the target entities. If True only splitting entities that are close to target entities will be considered. For each target entity, the system will determine which of the splitting entities is close to the target and will split the target entity only using the nearby splitting entities. This option is very useful if, for convenience, a large number of target and/or splitting entities have been provided. It results in the target entities only being split by those splitting entities that intersect (within tolerance) the target entities. If False (the default), ALL of the splitting entities will be considered for each target entity. For each target entity the system will attempt to find the projected intersection points of all of the splitter entities onto the target entity and will split the target entity all of the projected intersection points. Use this option if you intend to split the target entities with splitter entities that are remote for the targets.

Returns: ZResultSplitCurvesWithEntities result object

An option is provided to control splitting based on whether or not the projected intersection on the target entity is close to the splitter object (a true intersection) or further away (a projected intersection)

### `apex.geometry.splitEntityWithOffsetFaces(target: apex.EntityCollection, splitter: apex.EntityCollection, offset: float = 0.0, splitBehavior: GeometrySplitBehavior = apex.geometry.GeometrySplitBehavior.Partition) -> apex.EntityCollection`
Splits one or more target Solids, Surfaces, Curves, Cells, Faces or Edges using one or more "virtual" Faces defined by offsetting one or more "real" Geometry Faces.

- `target` — collection of Solid, Surface, Curve, Cell, Face or Edge.
- `splitter` — the collection of geometry Faces/Surfaces that will be used to split the target. If splitter includes Surfaces the method will internally expand the Surface to all of its Faces. If splitter contains duplicated Faces (including after expansion of any Surfaces) they will be silently ignored.
- `offset` — The distance by which the "real" splitter Surfaces/Faces will be offset to generate the "virtual" splitter Surfaces/Faces that will be used to perform the split. offset represents a Length quantity and must be provided in the units of Length from the active ScriptUnitSystem. Positive values of offset indicate the offset will be created on the positive normal side of the 'real" splitter Surface/Face. Negative values of offset indicate the offset will be created on the negative normal side.
- `splitBehavior` — An optional argument that determines whether Solids in target will be split into discrete Solids or partitioned into Cells. splitBehavior is an enumeration of type apex.geometry.GeometrySplitBehavior with a default values of apex.geometry.GeometrySplitBehavior.Partition. The default value will cause the method to partition Solids into multiple Cells within the original Solid. Setting the value apex.geometry.GeometrySplitBehavior.Split will cause the input Solid to be divided into separate discrete Solids. This argument has no effect on target Surfaces, Faces, Curves, Edges or Cells.

Returns: Collection of new and or modified bodies

The virtual Faces are created (temporarily) by offsetting real Geometry Faces (Solid or Surface Faces). The real geometry Faces may belong to the object that is being split or to any ohter Solid or Surface.The offset distance is provided as an input.An option is provided to control whether the split will partition the Solid into Cells or cause the target Solid to be divided into separate Solids

### `apex.geometry.splitOn3PointPlane(target: apex.EntityCollection, locations: apex.ILocationCollection, splitBehavior: GeometrySplitBehavior) -> apex.EntityCollection`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. split the body with a defined plane.

- `target` — collection of Solid, Surface, Curve, Cell, Face or Edge.
- `locations` — one two or three locations up to three xyz locations defining plane
- `splitBehavior` — Geometry Split Behavior Methods: Options are: GeometrySplitBehavior.SplitGeometrySplitBehavior.Partition

Returns: Collection of new and or modified bodies

### `apex.geometry.splitOnFeaturePlane(target: apex.EntityCollection, location: apex.ILocation, snapEntity: apex.Entity, splitBehavior: GeometrySplitBehavior) -> apex.EntityCollection`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. boolean split on feature plane.

- `target` — collection of Solid, Surface, Curve, Cell, Face or Edge.
- `location` — location on entity
- `snapEntity` — point, edge or face, entity picked for plane definition
- `splitBehavior` — Geometry Split Behavior Methods: Options are: GeometrySplitBehavior.SplitGeometrySplitBehavior.Partition

Returns: Collection of new and or modified bodies

### `apex.geometry.splitOnSurface(target: apex.EntityCollection, face: apex.EntityCollection, splitBehavior: GeometrySplitBehavior) -> apex.EntityCollection`
split the enitty with a surface "DEPRECATED: THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. It has been superseded by "apex.geometry.split()"

- `target` — collection of Solid, Surface, Curve, Cell, Face or Edge.
- `face` — collection of faces to split on.
- `splitBehavior` — Geometry Split Behavior Methods: Options are: GeometrySplitBehavior.SplitGeometrySplitBehavior.Partition

Returns: Collection of new and or modified bodies

### `apex.geometry.splitSurfacesWithCurves(target: apex.EntityCollection, splitter: apex.EntityCollection, useOnlyNearbySplitters: bool = False, searchDistance: float = NAN) -> apex.geometry.ZResultSplitSurfacesWithEntities`
Splits one or more target Faces with one or more splitter Edges by finding the intersection or projected intersection of the splitter Edges with the target Faces. An option is provided to control splitting based on whether or not the projected intersection on the target entity is close to the splitter object (a true intersection) or further away (a projected intersection)

- `target` — the set of geometry Faces that the method will target for splitting.
- `splitter` — the collection of geometry Edges that will be used to split the target Faces.
- `useOnlyNearbySplitters` — optional boolean value to control the extent of the splitting objects that will be used to split the target entities. If True only the subset of the splitting entities that are close to target entities will be considered. For each target entity, the system will determine which of the splitting entities is close to the target and will split the target entity only using the nearby splitting entities. This option is very useful if, for convenience, a large number of target and/or splitting entities have been provided. It results in the target entities only being split by those splitting entities that intersect (within tolerance) the target entities. If False (Default), ALL of the supplied splitting entities will be considered for each target entity. For each target entity the system will attempt to find the projected intersections of all of the splitter entities onto the target entity and will split the target entity along all of the projected intersections. Use this option if you intend to split the target entities with splitter entities that are remote from the targets.
- `searchDistance` — the search distance value to determine which of the splitting entities is close to the target.Used only when the option useOnlyNearbySplitters is True. The Default value is 1.0e-4m.

Returns: ZResultSplitSurfacesWithEntities

### `apex.geometry.splitSurfacesWithPath(target: apex.EntityCollection, splitter: apex.ILocationCollection, pathtype: apex.geometry.GeometrySplitLineType = apex.geometry.GeometrySplitLineType.Spline) -> apex.geometry.ZResultSplitSurfacesWithEntities`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type List Of apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocationCollection. For the Iberian Lynx release, users may continue to pass List Of Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocationCollection as quickly as possible to avoid future problems. Splits one or more target Surfaces/Faces with a path defined by an ordered series of two or more 3DPoints that lie on the target entities. An optional parameter is provided to control whether the path is interpreted by a spline fitted through the path points or as a polyline consisting of a series of connected straight line segments between the points.

- `target` — the set of geometry Surfaces and/or Faces that the method will target for splitting. If the target includes a mixture of Surfaces and Faces they must be supplied as an EntityCollection. If the target includes only Surfaces or Only Faces they may supplied as a SurfaceCollection or FaceCollection respectively
- `splitter` — The objects will be used to split the target entities
- `pathtype` — An optional enumeration that determines whether the path points will be used to define a spline or a polyline that will be used to split the Surface/Face.

Returns: ZResultSplitSurfacesWithEntities

### `apex.geometry.splitSurfacesWithSurfaces(target: apex.EntityCollection, splitter: apex.EntityCollection, stitch: bool = False) -> apex.geometry.ZResultSplitSurfacesWithEntities`
Splits one or more target Surfaces/Faces with one or more splitter Surfaces/Faces/DatumPlanes by finding the intersection of the splitter Surfaces/faces/DatumPlanes with the target Surfaces/Faces.

- `target` — the set of geometry Surfaces/Faces that the method will target for splitting. If the target includes a mixture of Surfaces and Faces they must be supplied as an EntityCollection. If the target includes only Surfaces or Only Faces they may supplied as a SurfaceCollection or FaceCollection respectively.
- `splitter` — the collection of geometry Surfaces/Faces/DatumPlanes that will be used to split the target Surfaces/Faces. If the splitter includes a mixture of Surfaces, Faces and DatumPlanes they must be supplied as an EntityCollection. If the target includes only Surfaces, Only Faces or Only DatumPlanes they may supplied as a SurfaceCollection, FaceCollection or construct::DatumPlaneCollection respectively.
- `stitch` — optional boolean value to control whether or not the system will attempt to stitch Surfaces/Faces together after splitting. If False (the default) the system will perform no stitching after splitting - the same number of Surfaces will be present after splitting as before. If True, the system will group all Surfaces and/or Faces in the target by Part and then for each Group of Surfaces/Faces the system will stitch all Surfaces (including the parent Surfaces of all Faces) that share Edges (introduced by splitting) into contiguous Surface bodies. This may result in fewer Surfaces existing after splitting than existed before. If splitter are DatumPlanes, stitch parameter will not apply to them.

Returns: ZResultSplitSurfacesWithEntities

### `apex.geometry.splitWithPlane(target: apex.EntityCollection, plane: apex.construct.Plane, splitBehavior: GeometrySplitBehavior) -> apex.EntityCollection`
TODO Documentation.

- `target` — collection of Solid, Surface, Curve, Cell, Face and Edge
- `plane` — the definition of the cutting plane as an apex.construct.Plane object
- `splitBehavior` — Enumeration to control whether the split will cause the Solid to be partitioned into multiple Solids (Split) or a single Solid with multiple Cells (Partition).Options are: GeometrySplitBehavior.SplitGeometrySplitBehavior.Partition

Returns: Collection of new and or modified bodies

### `apex.geometry.stitchCurves(target: apex.EntityCollection) -> apex.geometry.CurveCollection`
Takes as input a list of Curves and stitch them together. It returns Collectoin of created or modified Curves.

- `target` — an input list of Curves to stitch

Returns: Collectoin of created or modified curves

### `apex.geometry.stitchSurfaces(target: apex.EntityCollection, tolerance: float, createSolidIfWatertight: bool, ignoreStitchTolerance: bool, stitchFreeEdgesOnly: bool = True, stitchIntersectingFaces: bool = True) -> apex.geometry.GeometryBodyCollection`
stitch surfaces

- `target` — collection of any type of surface body
- `tolerance` — stitch tolerance
- `createSolidIfWatertight` — if solid is sheetbody that holds water, it will convert to solid
- `ignoreStitchTolerance` — This increases the stitch tolerance to try and "force a stitch"
- `stitchFreeEdgesOnly` — If true (default), the method will attempt to stitch only free Edges from the Surfaces and will ignore interior Surface Edges. If false the method will attempt to stitch all of the Edges in the Surface
- `stitchIntersectingFaces` — If true (default), the method will identify faces that intersect each other and will attempt to generate Edges at each intersection and subsequently stitch these Edges. If false, the method will not attempt to create Edges at Face intersections and will consider only existing Edges from the target Faces

Returns: Collection of stitched surfaces

### `apex.geometry.subtractBoolean(target: apex.EntityCollection, subtractingEntity: apex.EntityCollection, retainOriginalBodies: bool) -> apex.EntityCollection`
boolean subtract subtractingEntity from target

- `target` — collection of solids or surfaces
- `subtractingEntity` — subtracting solid or surface
- `retainOriginalBodies` — Flag to keep subtracting entity. Deleted when False.

Returns: Collection of modified bodies

### `apex.geometry.suppressOnly(target: apex.EntityCollection, maxEdgeAngle: float, maxFaceAngle: float, keepVerticesAtCurvatureChange: bool, cleanupTol: float, forceSuppress: bool = False) -> apex.EntityCollection`
Suppress target if not suppressed.

- `target` — collection Suppress target collection (Edge or Vertex) if not suppressed.
- `maxEdgeAngle` — edge angle for controling which vertex are suppressed in box picking
- `maxFaceAngle` — face angle for controling which edges are suppressed in box picking
- `keepVerticesAtCurvatureChange` — contoroles if key vertex at curvature changes should be retained.
- `cleanupTol` — controls how vertex close together are handled
- `forceSuppress` — controls if ignoring angle setting and keepVerticesAtCurvatureChange

Returns: Collection of suppressed entities

### `apex.geometry.suppressToggle(target: apex.EntityCollection, maxEdgeAngle: float = NAN, maxFaceAngle: float = NAN, keepVerticesAtCurvatureChange: bool = False, cleanupTol: float = NAN, forceSuppress: bool = False) -> [apex.EntityCollection]`
Suppress or unsuppress entities.

- `target` — collection, If edge is suppressed, unsuppress, and if unsuppressed, suppress it.
- `maxEdgeAngle` — edge angle for controling which vertex are suppressed in box picking
- `maxFaceAngle` — face angle for controling which edges are suppressed in box picking
- `keepVerticesAtCurvatureChange` — contoroles if key vertex at curvature changes should be retained.
- `cleanupTol` — controls how vertex close together are handled
- `forceSuppress` — controls if ignoring angle setting and keepVerticesAtCurvatureChange

Returns: tuple of two lists, list of suppressed entities, list of unsuppressed entities

### `apex.geometry.surfaceCollection(surfaceList: [Surface] = []) -> SurfaceCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.geometry.SurfaceCollection().

- `surfaceList` — optional list of Surfaces to add to the collection.

### `apex.geometry.unstitchCurves(target: apex.EntityCollection) -> apex.geometry.CurveCollection`
This function works similar to unstitchSurfaces, but for Curves instead. It takes as input a list of Edges or Curves. For each set of contiguously connected Edges from a single Body, it disconnects them into one new Curve. If a Curve is selected that is non-manifolded or a Generalbody, it converts it into a minimum set of regular Curve Bodies. If a selected Curve is already manifolded, no operation is performed.

- `target` — Collection of curves and or edges to unstitch

Returns: Collection of unstitched curves

### `apex.geometry.unstitchSurfaces(target: apex.EntityCollection) -> apex.geometry.SurfaceCollection`
un-stitch surfaces

- `target` — The collection of faces or a general body

Returns: Collection of unstitched surfaces

### `apex.geometry.unsuppressOnly(target: apex.EntityCollection) -> apex.EntityCollection`
Unsuppress selected edges if they are suppressed.

- `target` — collection unsuppress selected edges collection if they are suppressed

Returns: Collection of unsuppressed entities

## Classes in this module

Full method signatures are in `api/classes/apex.geometry.md`.

`Box`, `BoxCollection`, `Cell`, `CellCollection`, `Curve`, `CurveCollection`, `Cylinder`, `CylinderCollection`, `Edge`, `EdgeCollection`, `EdgeLoop`, `EdgeLoopCollection`, `Ellipsoid`, `EllipsoidCollection`, `Face`, `FaceCollection`, `FacetedCurve`, `FacetedCurveCollection`, `FacetedSolid`, `FacetedSolidCollection`, `FacetedSurface`, `FacetedSurfaceCollection`, `GeometryBody`, `GeometryBodyCollection`, `GeometryFeature`, `GeometryFeatureCollection`, `GeometryTopology`, `GeometryTopologyCollection`, `MeshControlEdge`, `MeshControlEdgeCollection`, `Point`, `PointCollection`, `Solid`, `SolidCollection`, `Sphere`, `SphereCollection`, `Surface`, `SurfaceCollection`, `Vertex`, `VertexCollection`, `ZResultDefeature`, `ZResultDefeatureCustomFeature`, `ZResultEvaluateClosestLocation`, `ZResultEvaluateClosestLocationOnFace`, `ZResultEvaluateCurveParametricCoordinate`, `ZResultEvaluateFaceCurvature`, `ZResultEvaluateFaceTangent`, `ZResultEvaluatePointOnCurve`, `ZResultEvaluatePointOnFace`, `ZResultEvaluatePointOnSurface`, `ZResultEvaluateSurfaceParametricCoordinate`, `ZResultFindGeometryFaults`, `ZResultFindSmallSurfaceFeatures`, `ZResultGeometrySimplify`, `ZResultIdentifyCustomFeature`, `ZResultIdentifyFeature`, `ZResultIdentifyFixSmallFeatures`, `ZResultSolidIdentifyFeature`, `ZResultSplitCurvesWithEntities`, `ZResultSplitSurfacesWithEntities`

