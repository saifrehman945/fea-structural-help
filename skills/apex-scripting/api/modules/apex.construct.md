# apex.construct

(apex.construct module) Geometry Construction functions (create Sketch object using Part createSketch() method)

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.construct.ArcDirection`: `Clockwise`, `CounterClockwise`

`apex.construct.ConstructionMarkerType`: `ArcCenter`, `Centroid`, `CylindricalAxisStartPoint`, `CylindricalAxisMidPoint`, `CylindricalAxisEndPoint`, `StartPoint`, `EndPoint`, `MidPoint`, `FaceCenter`
  - Identifying the type of construction marker to evaluate from the target entities

`apex.construct.CoordinateSystemAxis`: `X_Axis`, `Y_Axis`, `Z_Axis`

`apex.construct.CoordinateSystemType`: `Cartesian`, `Cylindrical`, `Spherical`
  - Possible CoordinateSystemType Options in Apex

`apex.construct.GlobalPlane`: `XY`, `YZ`, `ZX`

`apex.construct.OrientationMethod`: `Euler`, `MultiObject`
  - Of the different orientation methods supported in Apex. Orientations can be embedded within objects such as Connectors and PointMasses and each of these Orientations can be defined using one of the orientation methods enumerated here. Coordinate system orientations can also be defined using one of these methods

## Module functions

### `apex.construct.createCoordinateSystemByEulerMethod(name: str, description: str, coordType: apex.construct.CoordinateSystemType, origin: apex.ILocation, orientation: Orientation) -> apex.construct.CoordinateSystem`
create a coordinate system of either Rectangular, Cylindrical or Spherical type by using Euler angle method

- `name` — The name of the coordinate system to be created.
- `description` — The description of the object. The description field usually appears on the Object Property panel in the interactive UI and in some cases will appear in the Tool property panel of the tool that creates the object.
- `coordType` — The coordinate system type - either Rectangular, Cylindrical or Spherical defines using a CoordinateSystemType enumeration
- `origin` — The location of the origin of the Coordinate System as a Point3D
- `orientation` — The orientation of the CoordinateSystem as an Orientation object. This orientation is always available no matter which OrientationMethod is used to specify the coordinate system (Euler angles can always be determined)

Returns: the CoordinateSystem object

THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use the alternative apex.construct.createCoordinateSystemByLocationOrientation instead

### `apex.construct.createCoordinateSystemByLocationOrientation(name: str, description: str, coordType: apex.construct.CoordinateSystemType, origin: apex.ILocation, orientation: apex.IOrientation, id: int) -> apex.construct.CoordinateSystem`
create a coordinate system of either Rectangular, Cylindrical or Spherical type using a location and orientation

- `name` — An optional name for the coordinate system being created. If omitted the system will assign a default name If provided, the name must be unique within the scope of the current project
- `description` — An optional description for the CoordinateSystem that is being created
- `coordType` — An optional enumeration to define which type of coordinate system will be created - either Rectangular, Cylindrical or Spherical. If omitted, the coordinate system type defaults to Rectangular
- `origin` — The origin of the Coordinate System as an ILocation. Any Apex entity type that implements ILocation can be supplied, including apex.Coordinate
- `orientation` — The orientation of the CoordinateSystem as an IOrientatio. Any Apex type that implements IOrientation (including Orientation) can be supplied. If omitted, the orientation will be aligned with the Apex global orientation
- `id` — Optional - the id of the coordinate system. If omitted, system will assign the smallest coordinate system id to it.

Returns: the CoordinateSystem object

### `apex.construct.createLocationByCoordinates(x: float, y: float, z: float) -> apex.Coordinate`
Create a new Location.

- `x` — x-coordinate.
- `y` — coordinate.
- `z` — of the new Location.

Returns: the created Location

### `apex.construct.createLocationByEntity(entity: apex.Entity) -> apex.Coordinate`
Create a new Location.

- `entity` — a model object (node or vertex).

### `apex.construct.createOptionOrientation() -> Orientation`
Create a new Orientation with default options.

Returns: the created Orientation

### `apex.construct.createOrientation(alpha: float, beta: float, gamma: float) -> Orientation`
Create a new Orientation.

- `alpha` — of the new Orientation.
- `beta` — of the new Orientation.
- `gamma` — of the new Orientation.

Returns: the created Orientation

### `apex.construct.createOrientationByCoordinateSystem(coordinateSystem: apex.construct.CoordinateSystem) -> Orientation`
Create a new Orientation in terms of a coordinate system.

- `coordinateSystem` — The coordinate system defines the orientation.

Returns: the created Orientation

### `apex.construct.createSketchForProfile1D(name: str) -> apex.construct.SketchProfile1D`
Create and initialize the sketch for Profile1D.

- `name` — Name of the sketch.

Returns: the created SketchProfile1D

### `apex.construct.datum3PointPlane(locations: apex.ILocationCollection) -> apex.construct.DatumPlane`
datum3PointPlane creates a datum plane from three points using two or three locations in the form of an iphysicalCollection. If three points are supplied, the planes origin will be the first point. The plane orientation will be calculated from the three point plane of the three inputs ILocations. If only two locations are specified, then the plane origin will be the first point, and oriented perpendicular to the vector between location 1 and location 2.

- `locations` — is an iphysicalCollection of from two or three ILocations. If only one location is provided, then we assume the second location is in the global X direction from Location 1. no locations are given, the origin of 0,0,0 will be used, with the orientation of 1,0,0.

Returns: the DatumPlane object

### `apex.construct.datumFromCoordinateSystem(coord: apex.construct.CoordinateSystem, axis: apex.construct.CoordinateSystemAxis = apex.construct.CoordinateSystemAxis.Z_Axis) -> apex.construct.DatumPlane`
A datum plane is created from a coordinate system by using datumFromCoordinateSystem. The input is a CoordinateSystem object, and a specified axis. The global model coordinate frame is the default location, with the z axis as the default orientation.

- `coord` — is an Apex CoordinateSystem. If not specified, the global coordinate system is assumed.
- `axis` — is a coordinate systems axis (apex.construct.DatumNormalAxis.X, apex.construct.DatumNormalAxis.Y, apex.construct.DatumNormalAxis.Z). Default is "Z" axis.

Returns: the DatumPlane object

### `apex.construct.datumFromPlane(plane: apex.construct.Plane) -> apex.construct.DatumPlane`
datumFromPlane takes as input a an Apex Plane class, and creates a datumPlane at the planes location and orientation.

- `plane` — the input is an Apex Plane Object. The plan datum plane will be constructed at the Plane objects ILocation, and oriented perpendicular to the Vector3D.

Returns: the DatumPlane object

### `apex.construct.datumFromPointOnGeometry(location: apex.ILocation, snapEntity: apex.Entity) -> apex.construct.DatumPlane`
datumFromPointOnGeometry is used to define a datumPlane by specifying the location on an Edge or Face. The two arguments represent the pick location and the geometry Edge or Face that was selected. The location does not have to be directly on the geometry, since the closest approach on the geometry to the location will be used.

- `location` — is an Apex ILocation. This represents the location on the snapEntity geometry where the new Datum Plane's normal location and orientation will be extracted. If the location is not on the geometry, the closest approach will be used instead.
- `snapEntity` — is a Face or an Edge used to define the Datum Plane location and orientation. The location of the plane will be the closest approach to the location argument on the targeted geometry. The orientation will be perpendicular to the surface normal, or edge tangent, depending on the geometry type.

Returns: the DatumPlane object

### `apex.construct.editSketchForProfile1D(name: str) -> apex.construct.SketchProfile1D`
Edit the sketch for Profile1D.

- `name` — Name of the sketch.

Returns: the created SketchProfile1D

### `apex.construct.evaluateConstructionMarkerOrientation(target: Entity, constructionMarkerType: apex.construct.ConstructionMarkerType) -> apex.Orientation`
evaluates the default orientation of a construction marker from the input target entities and construction marker type.

- `target` — collection of entities from which the construction marker and subsequently the default construction marker orientation will be derived. Currently, this collection may include any geometry or geometry topology entities. Entities of any other types will be silently ignored
- `constructionMarkerType` — enumeration identifying the type of construction marker to evaluate from the target entities

Returns: the evaluate orientation

The method first calculates the location of the requested construction marker based on the input target entities and then evaluates a default orientation for that marker.The logic used in this algorithm is complex however the intention is to provide an orientation that is naturally aligned with the input target.

### `apex.construct.getAxisEndPointLocationFromGroup(group: apex.Group) -> apex.Coordinate`
returns the end point of the cylindrical axis of this Group if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Group contains a single cylindrical Face or circular arc this method will return the end point of the axis of that Face or Edge as a Coordinate. If the Group references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be determined, its end point will be returned as a Coordinate. If a cylindrical axis cannot be determined, the method will return a None type.

- `group` — The specified Group which the cylindracal axis is based on.

### `apex.construct.getAxisEndPointLocationFromRegion(region: apex.Region) -> apex.Coordinate`
returns the end point of the cylindrical axis of this Region if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Region contains a single cylindrical Face or circular arc this method will return the end point of the axis of that Face or Edge as a Coordinate. If the Region references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be determined, its end point will be returned as a Coordinate. If a cylindrical axis cannot be determined, the method will return a None type.

- `region` — The specified Region which the cylindracal axis is based on.

### `apex.construct.getAxisMidPointLocationFromGroup(group: apex.Group) -> apex.Coordinate`
returns the mid point of the cylindrical axis of this Group if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Group contains a single cylindrical Face or circular arc this method will return the mid point of the axis of that Face or Edge as a Coordinate. If the Group references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be identified, its mid point will be returned as a Coordinate. If a cylindrical axis cannot be determined, the method will return a None type.

- `group` — The specified Group which the cylindracal axis is based on.

### `apex.construct.getAxisMidPointLocationFromRegion(region: apex.Region) -> apex.Coordinate`
returns the mid point of the cylindrical axis of this Region if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Region contains a single cylindrical Face or circular arc this method will return the mid point of the axis of that Face or Edge as a Coordinate. If the Region references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be identified, its mid point will be returned as a Coordinate. If a cylindrical axis cannot be determined, the method will return a None type.

- `region` — The specified Region which the cylindracal axis is based on.

### `apex.construct.getAxisStartPointLocationFromGroup(group: apex.Group) -> apex.Coordinate`
returns the start point of the cylindrical axis of this Group if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Group contains a single cylindrical Face or circular arc this method will return the start point of the axis of that Face or Edge as a Coordinate. If the Group references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be determined, its start point will be returned as a Coordinate. If a cylindrical axis cannot be determined, the method will return a None type.

- `group` — The specified Group which the cylindracal axis is based on.

### `apex.construct.getAxisStartPointLocationFromRegion(region: apex.Region) -> apex.Coordinate`
returns the start point of the cylindrical axis of this Region if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Region contains a single cylindrical Face or circular arc this method will return the start point of the axis of that Face or Edge as a Coordinate. If the Region references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be determined, its start point will be returned as a Coordinate. If a cylindrical axis cannot be determined, the method will return a None type.

- `region` — The specified Region which the cylindracal axis is based on.

### `apex.construct.getCylindricalAxisFromGroup(group: apex.Group) -> apex.construct.Vector3D`
returns the cylindrical axis of this Group if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Group contains a single cylindrical Face or circular arc this method will return the cylindrical axis of that Face or Edge as a Vector3D. If the Group references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be identified, it will be returned as a Vector3D. If a cylindrical axis cannot be determined, the method will return a None type.

- `group` — The specified Group which the cylindracal axis is based on.

### `apex.construct.getCylindricalAxisFromRegion(region: apex.Region) -> apex.construct.Vector3D`
returns the cylindrical axis of this Region if one can be determined. A cylindrical axis (and its start, end and mid points), is only guaranteed for geometry Faces based on analytic cylinders or circular arcs, however in many cases it is possible to determine an approximate cylindrical axis (and associated axis points) from a collection of Faces or Edges. If the input Region contains a single cylindrical Face or circular arc this method will return the cylindrical axis of that Face or Edge as a Vector3D. If the Region references any other type of Entity or collection of Entities this method will attempt to calculate an approximate cylindrical axis from those entities and, if an axis can be identified, it will be returned as a Vector3D. If a cylindrical axis cannot be determined, the method will return a None type.

- `region` — The specified Region which the cylindracal axis is based on.

## Classes in this module

Full method signatures are in `api/classes/apex.construct.md`.

`Arc`, `Chamfer`, `Circle`, `CoordinateSystem`, `CoordinateSystemCollection`, `DatumPlane`, `DatumPlaneCollection`, `Ellipse`, `Fillet`, `MirrorPlane`, `Orientation`, `ParametricCoordinate2D`, `ParametricCoordinate3D`, `Plane`, `Point2D`, `Point3D`, `Polyline`, `Profile1D`, `Profile1DCollection`, `Rectangle`, `Sketch`, `SketchEdge`, `SketchPoint`, `SketchPrimitive`, `SketchProfile1D`, `SketchVertex`, `Spline`, `Vector3D`

