# apex.construct — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.construct.Arc`  (extends `SketchPrimitive`)
Properties: `angle`, `center`, `length`, `name`, `radius`

Methods:

#### `getAngle() -> float`
get the angle of the arc

Returns: the angle of the arc

#### `getCenter() -> Point2D`
get the center of the arc

Returns: the center of the arc

#### `getLength() -> float`
get the length of the arc

Returns: the length of the arc

#### `getName() -> str`
get the name of the arc

Returns: the name of the arc

#### `getRadius() -> float`
get the radius of the arc

Returns: the radius of the arc

- `update(name: str, center: Point2D, radius: float, angle: float) -> bool`

## `apex.construct.Chamfer`  (extends `SketchPrimitive`)
Properties: `end`, `length`, `name`, `start`

Methods:

- `getEnd(: None) -> Point2D`
- `getLength(: None) -> float`
- `getName() -> str`
- `getStart(: None) -> Point2D`
- `update(name: str, start: Point2D, end: Point2D, length: float) -> bool`

## `apex.construct.Circle`  (extends `SketchPrimitive`)
Properties: `center`, `name`, `radius`

Methods:

- `getCenter(: None) -> Point2D`
- `getName() -> str`
- `getRadius(: None) -> float`
- `update(name: str, center: Point2D, radius: float) -> bool`

## `apex.construct.CoordinateSystem`  (extends `Entity`, `IName`, `IDisplayable`, `ILocation`, `IOrientation`)
A scripting class that represents user defined or local coordinate system. The CoordinateSystem class can represent Cartesian, Cylindrical an Spherical coordinate systems types using a "type" attribute. The location of the CoordinateSystem is defined by the "origin" attribute. The orientation of a CoordinateSystem can be defined using one of two methods as indicated by the "orientationMethod" attribute. If the "orientationMethod" is "Euler", the Euler angles are defined using the "orientation" attribute. If the "orientationMethod" is "MultiObject", the objects are defined using the "objectList" attribute.
Properties: `coordinateSystemType`, `id`, `orientation`, `origin`, `xAxis`, `yAxis`, `zAxis`

Methods:

#### `getCoordinateSystemType() -> CoordinateSystemType`
returns the CoordinateSystem type

Returns: a CoordinateSystemType value

#### `getDescription() -> str`
Read-only string representing the description of this object. The description field usually appears the Object Property panel in the interactive UI and in some cases will appear in the Tool property panel of the tool that creates the object.

Returns: this entity description (string)

getDescription() may also be accessed as an Entity property 'description'. For example:

#### `getId() -> int`
returns the id of the coordinate system.

Returns: the id of the coordinate system

#### `getName() -> str`
Read-only string representing the name of this object.

Returns: this entity name (string)

getName() may also be accessed as an Entity property 'name'. For example:

#### `getOrientation() -> apex.Orientation`
returns the orientation of the cooordinate system

Returns: a Orientation object

#### `getOrientationMethod() -> OrientationMethod`
returns the orientation method

Returns: an OrientationMethod value

#### `getOrigin() -> apex.Coordinate`
returns the location of the origin of the Coordinate System

Returns: a ILocation object

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/

#### `update(name: str, description: str, coordType: apex.construct.CoordinateSystemType, origin: apex.ILocation, orientation: apex.IOrientation, id: int) -> None`
create a coordinate system of either Rectangular, Cylindrical or Spherical type by using Euler angle method

- `name` — The name of the coordinate system to be updated.
- `description` — The description of the object. The description field usually appears on the Object Property panel in the interactive UI and in some cases will appear in the Tool property panel of the tool that creates the object.
- `coordType` — The coordinate system type - either Rectangular, Cylindrical or Spherical defines using a CoordinateSystemType enumeration
- `origin` — The location of the origin of the Coordinate System as a Point3D
- `orientation` — The orientation of the CoordinateSystem as an Orientation object. This orientation is always available no matter which OrientationMethod is used to specify the coordinate system (Euler angles can always be determined)
- `id` — update the id of the coordinate system.

Returns: the CoordinateSystem object


## `apex.construct.CoordinateSystemCollection`  (extends `EntityCollection`)
Iterable collection of CoordinateSystems, based on EntityCollection.

Methods:

- `CoordinateSystemCollection() -> None`

## `apex.construct.DatumPlane`  (extends `Entity`, `IDisplayable`, `IPhysical`, `IName`, `IOrientation`)
DatumPlane Class Object Class representing an infinite plane in 3D space.
Properties: `displayLength`, `displayWidth`, `normal`, `origin`

Methods:

- `getDisplayLength() -> float` — Although Planes are infinite, they are visualized using a rectangular planar glygh with finite demensions. displayWidth controls the width of this rectangular glyph.
- `getDisplayWidth() -> float` — Although Planes are infinite, they are visualized using a rectangular planar glygh with finite demensions. displayLength controls the length of this rectangular glyph.
- `getNormal() -> Vector3D` — The normal to the Plane as an apex.construct.Vector3D.
- `getOrigin() -> Coordinate` — origin defines a location in space that Plane passes through.
#### `update(name: str, parent: Entity = 0) -> None`
Update one or more of this DatumPlane properties.

- `name` — of this DatumPlane
- `parent` — of this DatumPlane

Either the name, parent, or both can be updated in one update call.


## `apex.construct.DatumPlaneCollection`  (extends `IPhysicalCollection`)
Iterable collection of DatumPlanes, based on EntityCollection.

Methods:

- `DatumPlaneCollection() -> None` — Construct a new DatumPlaneCollection.
#### `appendList(datumPlaneList: [apex.construct.DatumPlane]) -> None`
Add DatumPlanes from a list to the end of this collection.

- `datumPlaneList` — list of DatumPlanes to add to the collection.

For example:


## `apex.construct.Ellipse`  (extends `SketchPrimitive`)
Properties: `name`, `radiusAxis1`, `radiusAxis2`

Methods:

- `getName() -> str`
- `getRadiusAxis1(: None) -> float`
- `getRadiusAxis2(: None) -> float`
- `update(name: str, center: Point2D, radiusAxis1: float, radiusAxis2: float) -> bool`

## `apex.construct.Fillet`  (extends `SketchPrimitive`)
Properties: `angle`, `center`, `end`, `name`, `radius`, `start`

Methods:

- `getAngle(: None) -> float`
- `getCenter(: None) -> Point2D`
- `getEnd(: None) -> Point2D`
- `getName() -> str`
- `getRadius(: None) -> float`
- `getStart(: None) -> Point2D`
- `update(name: str, center: Point2D, start: Point2D, end: Point2D, radius: float, angle: float) -> bool`

## `apex.construct.MirrorPlane`  (extends `Entity`)
Properties: `normal`, `origin`

Methods:

- `getNormal(: None) -> apex.Coordinate`
- `getOrigin(: None) -> apex.Coordinate`

## `apex.construct.Orientation`
DEPRECATION NOTICE : THIS ENUMERATOR IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.User can use type(object) to get the type directly.
Properties: `alpha`, `beta`, `coordinateSystem`, `gamma`, `GlobalNX`, `GlobalNY`, `GlobalNZ`, `GlobalPX`, `GlobalPY`, `GlobalPZ`, `useCoordinateSystem`, `Vector`, `xAxis`, `yAxis`, `zAxis`

Methods:

- `Orientation() -> None`
- `getAlpha() -> float`
- `getBeta() -> float`
- `getCoordinateSystem() -> apex.construct.CoordinateSystem`
- `getGamma() -> float`
#### `getGlobalNX() -> bool`
gets a boolean value that if True indicates the Orientation is aligned with the global Negative X-Axis

Returns: a boolean value

#### `getGlobalNY() -> bool`
gets a boolean value that if True indicates the Orientation is aligned with the global Negative Y-Axis

Returns: a boolean value

#### `getGlobalNZ() -> bool`
gets a boolean value that if True indicates the Orientation is aligned with the global Negative Z-Axis

Returns: a boolean value

#### `getGlobalPX() -> bool`
gets a boolean value that if True indicates the Orientation is aligned with the global Positive X-Axis

Returns: a boolean value

#### `getGlobalPY() -> bool`
gets a boolean value that if True indicates the Orientation is aligned with the global Positive Y-Axis

Returns: a boolean value

#### `getGlobalPZ() -> bool`
gets a boolean value that if True indicates the Orientation is aligned with the global Positive Z-Axis

Returns: a boolean value

- `getUseCoordinateSystem() -> bool`
- `getVector() -> bool`
- `getXAxis() -> apex.construct.Vector3D`
- `getYAxis() -> apex.construct.Vector3D`
- `getZAxis() -> apex.construct.Vector3D`
- `setAlpha(alpha: float) -> None`
- `setBeta(beta: float) -> None`
- `setCoordinateSystem(coordSystem: apex.construct.CoordinateSystem) -> None`
- `setGamma(gamma: float) -> None`
- `setGlobalNX(bVal: bool) -> None`
- `setGlobalNY(bVal: bool) -> None`
- `setGlobalNZ(bVal: bool) -> None`
- `setGlobalPX(bVal: bool) -> None`
- `setGlobalPY(bVal: bool) -> None`
- `setGlobalPZ(bVal: bool) -> None`
- `setVector(bVal: bool) -> None`
- `setXAxis(vecVal: apex.construct.Vector3D) -> None`
- `setYAxis(vecVal: apex.construct.Vector3D) -> None`
- `setZAxis(vecVal: apex.construct.Vector3D) -> None`
#### `update(alpha: float = NAN, beta: float = NAN, gamma: float = NAN) -> None`
Update this Orientation.

- `alpha` — of this Orientation. Assigning it the None value (alpha = None) to reset it to its original, empty state
- `beta` — of this Orientation. Assigning it the None value (beta = None) to reset it to its original, empty state
- `gamma` — of this Orientation. Assigning it the None value (gamma = None) to reset it to its original, empty state


## `apex.construct.ParametricCoordinate2D`
A convenience class that holds a 2D parametric coordinate. The class exposes two attributes that represent the 2D 'u' and 'v' coordinate values.
Properties: `u`, `v`

Methods:

- `ParametricCoordinate2D() -> None`

## `apex.construct.ParametricCoordinate3D`
A convenience class that holds a 3D parametric coordinate. The class exposes three attributes that represent the 3D 'u', 'v' and 'w' coordinate values.
Properties: `u`, `v`, `w`

Methods:

- `ParametricCoordinate3D() -> None`

## `apex.construct.Plane`  (extends `Entity`)
Properties: `normal`, `origin`

Methods:

- `Plane(origin: apex.construct.Point3D, normal: Vector3D) -> None` — DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems.
- `Plane(origin: ILocation, normal: Vector3D) -> None`
- `getNormal() -> Vector3D`
- `getOrigin() -> Coordinate`
- `update(origin: ILocation, normal: Vector3D) -> bool`

## `apex.construct.Point2D`
object representing a 2D point in space. Used in apex.construct methods.
Properties: `x`, `y`

Methods:

- `Point2D(x: float = NAN, y: float = NAN) -> None`
- `getX(: None) -> float`
- `getY(: None) -> float`
- `setX(x: float) -> None`
- `setY(y: float) -> None`

## `apex.construct.Point3D`
object representing a 3D point in space. Used in geometry and mesh editing, and in apex.Trasformation functions.
Properties: `x`, `y`, `z`

Methods:

- `Point3D(x: float = NAN, y: float = NAN, z: float = NAN) -> None`
- `getX(: None) -> float`
- `getY(: None) -> float`
- `getZ(: None) -> float`
- `setX(x: float) -> None`
- `setY(y: float) -> None`
- `setZ(z: float) -> None`

## `apex.construct.Polyline`  (extends `SketchPrimitive`)
Properties: `length`, `name`, `points`

Methods:

- `getLength(: None) -> float`
- `getName() -> str`
- `getPoints(: None) -> [Point2D]`
- `update(name: str, length: float) -> bool`

## `apex.construct.Profile1D`  (extends `Entity`)
Properties: `description`, `name`

Methods:

#### `getDescription() -> str`
retrieve the description of the profile

Returns: the profile description

#### `getEdgeAnnotation(index: int) -> str`
retrieve the edge annotaion with the specified index

- `index` — the index of the sketch edge

Returns: the edge annotaion

#### `getName() -> str`
retrieve the name of the profile

Returns: the profile name

#### `getVertexAnnotation(index: int) -> str`
retrieve the vertex annotaion with the specified index

- `index` — the index of the sketch vertex

Returns: the vertex annotaion


## `apex.construct.Profile1DCollection`  (extends `EntityCollection`)
Iterable collection of Profile1Ds, based on EntityCollection.

Methods:

- `Profile1DCollection() -> None`

## `apex.construct.Rectangle`  (extends `SketchPrimitive`)
Properties: `height`, `name`, `width`

Methods:

- `getHeight(: None) -> float`
- `getName() -> str`
- `getWidth(: None) -> float`
- `update(name: str, location: Point2D, diagonal: Point2D, orientationPoint: Point2D, heightPoint: Point2D, width: float, height: float) -> bool`

## `apex.construct.Sketch`  (extends `Entity`)
Properties: `name`, `orientation`, `origin`

Methods:

#### `completeSketch(fillSketches: bool) -> apex.EntityCollection`
This controls how sketches are converted to geometry.

- `fillSketches` — missing, add it for avoiding warning

Returns: geometry created from the sketch

#### `createArc3Point(name: str, point1: Point2D, point2: Point2D, point3: Point2D) -> apex.construct.Arc`
adds an Arc to the Sketch by picking three points on circumference, like three point arc, but first two points mark the start and end of the arc.

- `name` — Name of the surface. Default ="" (Future use)
- `point1` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `point2` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `point3` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Arc or none if fails to create.

#### `createArcCenterPoint(name: str, centerPoint: Point2D, point2: Point2D, point3: Point2D, arcDirection: apex.construct.ArcDirection) -> apex.construct.Arc`
adds an Arc to the Sketch by picking center point, then point 2 as radius and start of arc, point 3 as end of arc.

- `name` — Name of the surface. Default ="" (Future use)
- `centerPoint` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `point2` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `point3` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `arcDirection` — direction arc swept from point2 to point3: ArcDirection.Clockwise ArcDirection.CounterClockwise

Returns: the created Arc or none if fails to create.

#### `createChamferEdge(name: str, edge1: apex.construct.SketchPrimitive, edge2: apex.construct.SketchPrimitive, point2: Point2D) -> apex.construct.Chamfer`
adds an Chamfer to the Sketch by selecting a pair of straight edges, then location to define chamfer depth. Returns the chamfer edge created, plus the edge on eithe side of it.

- `name` — Name of the surface. Default ="" (Future use)
- `edge1` — 2d edge in sketch plane
- `edge2` — 2d edge in sketch plane
- `point2` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Chamfer or none if fails to create.

#### `createChamferVertex(name: str, point1: apex.construct.SketchPrimitive, point2: Point2D) -> apex.construct.Chamfer`
adds an Chamfer to the Sketch by selecting a vertex connected to two straight edges, then location to define chamfer depth. Returns the chamfer edge created, plus the edge on eithe side of it.

- `name` — Name of the surface. Default ="" (Future use)
- `point1` — vertex between two straight edges
- `point2` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Chamfer or none if fails to create.

#### `createCircle3Point(name: str, point1: Point2D, point2: Point2D, point3: Point2D) -> apex.construct.Circle`
adds a Circle to the Sketch by picking three points on circumference

- `name` — Name of the surface. Default ="" (Future use)
- `point1` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `point2` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `point3` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Circle or none if fails to create.

#### `createCircleCenterPoint(name: str, centerPoint: Point2D, pointOnCircle: Point2D) -> apex.construct.Circle`
adds a Circle to the Sketch by picking center point and location on radius.

- `name` — Name of the surface. Default ="" (Future use)
- `centerPoint` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `pointOnCircle` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Circle or none if fails to create.

#### `createEllipse3Point(name: str, centerPoint: Point2D, pointAxis1: Point2D, pointAxis2: Point2D) -> apex.construct.Ellipse`
adds a Ellipse to the Sketch by picking point 1 as center point, point 2 as on axis 1 radius and ellipse orientation, third point as axis 2 radius

- `name` — Name of the surface. Default ="" (Future use)
- `centerPoint` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `pointAxis1` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `pointAxis2` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Ellipse or none if fails to create.

#### `createFilletEdge(name: str, edge1: apex.construct.SketchPrimitive, edge2: apex.construct.SketchPrimitive, radiusPoint: Point2D) -> apex.construct.Fillet`
adds an Fillet to the Sketch by selecting a pair of straight edges, then location to define radius. Returns the fillet edge created, plus the edge on eithe side of it.

- `name` — Name of the surface. Default ="" (Future use)
- `edge1` — 2d edge in sketch plane
- `edge2` — 2d edge in sketch plane
- `radiusPoint` — location defining radius

Returns: the created Fillet or none if fails to create.

#### `createFilletVertex(name: str, vertex: apex.construct.SketchPrimitive, radiusPoint: Point2D) -> apex.construct.Fillet`
adds an Fillet to the Sketch by selecting a vertex corner, then location to define radius. Returns the fillet edge created, plus the edge on eithe side of it.

- `name` — Name of the surface. Default ="" (Future use)
- `vertex` — Vertex location of curve
- `radiusPoint` — location defining radius

Returns: the created Fillet or none if fails to create.

#### `createPoint(name: str, location: Point2D) -> apex.construct.SketchPoint`
adds a Point to the Sketch by selecting a location

- `name` — Name of the surface. Default ="" (Future use)
- `location` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created SketchPoint or none if fails to create.

#### `createPolyline(name: str, points: [Point2D]) -> apex.construct.Polyline`
adds a Polyline to the Sketch by inputting an unlimited list of 2d locations

- `name` — Name of the surface. Default ="" (Future use)
- `points` — list of 2d coordinates in sketch plane coordinate system

Returns: the created Polyline or none if fails to create.

#### `createRectangle2Point(name: str, location: Point2D, diagonal: Point2D) -> apex.construct.Rectangle`
adds a Rectangle to the Sketch by selecting two vertices of the rectangle diagonal

- `name` — Name of the surface. Default ="" (Future use)
- `location` — missing, add it for avoiding warning
- `diagonal` — missing, add it for avoiding warning

Returns: the created Rectangle or none if fails to create.

#### `createRectangle3Point(name: str, location: Point2D, orientationPoint: Point2D, heightPoint: Point2D) -> apex.construct.Rectangle`
adds a Rectangle to the Sketch by selecting two vertex along one edge to define the location and orientation, then a third for length.

- `name` — Name of the surface. Default ="" (Future use)
- `location` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `orientationPoint` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin
- `heightPoint` — a Point2D object defining the X, Y coordinates relative to the sketch plane origin

Returns: the created Rectangle or none if fails to create.

#### `createSpline(name: str, points: [Point2D], asPolyline: bool) -> apex.construct.Spline`
adds a Spline to the Sketch by inputting an unlimited list of 2d locations

- `name` — Name of the surface. Default ="" (Future use)
- `points` — list of 2d coordinates in sketch plane coordinate system
- `asPolyline` — true, then polyline path used, else curved path

Returns: the created Spline or none if fails to create.

#### `getArc(id: int int int) -> apex.construct.Arc`
retrieve the sketch Arc with the specified id

- `id` — the id of the sketch Arc

Returns: the sketch Arc

#### `getChamfer(id: int int int) -> apex.construct.Chamfer`
retrieve the sketch Chamfer with the specified id

- `id` — the id of the sketch Chamfer

Returns: the sketch Chamfer

#### `getCircle(id: int int int) -> apex.construct.Circle`
retrieve the sketch Circle with the specified id

- `id` — the id of the sketch Circle

Returns: the sketch Circle

#### `getEdge(id: int int int = 0U, annotation: str = "#####") -> apex.construct.SketchEdge`
retrieve the sketch edge with the specified id

- `id` — the id of the sketch edge
- `annotation` — the annotation of the edge

Returns: the sketch edge

#### `getEllipse(id: int int int) -> apex.construct.Ellipse`
retrieve the ellipse with the specified id

- `id` — the id of the ellipse

Returns: the ellipse

#### `getFillet(id: int int int) -> apex.construct.Fillet`
retrieve the sketch Fillet with the specified id

- `id` — the id of the sketch Fillet

Returns: the sketch Fillet

#### `getName(: None) -> str`
retrieve the name of the sketch

Returns: the sketch name

#### `getOrientation(: None) -> Vector3D`
retrieve the orientation of the sketch

Returns: the sketch orientation

#### `getOrigin(: None) -> Coordinate`
retrieve the origin of the sketch

Returns: the sketch origin

#### `getPolyline(id: int int int) -> apex.construct.Polyline`
retrieve the sketch Polyline with the specified id

- `id` — the id of the sketch Polyline

Returns: the sketch Polyline

#### `getRectangle(id: int int int) -> apex.construct.Rectangle`
retrieve the sketch Rectangle with the specified id

- `id` — the id of the sketch Rectangle

Returns: the sketch Rectangle

#### `getSketchPoint(id: int int int) -> apex.construct.SketchPoint`
retrieve the sketch Point with the specified id

- `id` — the id of the sketch Point

Returns: the sketch Point

#### `getVertex(id: int int int = 0U, annotation: str = "#####") -> SketchVertex`
retrieve the sketch vertex with the specified id

- `id` — the id of the sketch vertex
- `annotation` — the annotation of the vertex

Returns: the sketch vertex

#### `projectEdge(name: str, curve: Entity) -> apex.EntityCollection`
adds a curve to a sketch projecting any selected 3d edge to the current sketch plane

- `name` — Name of the surface. Default ="" (Future use)
- `curve` — 3D entity (3D curver or face)

Returns: the projected entity or none if fails to project.

#### `projectPoint(name: str, location: apex.ILocation) -> apex.construct.SketchPoint`
adds a point to a sketch projecting any selected vertex or node to the current sketch plane

- `name` — Name.
- `location` — location of vertex or node

Returns: the SketchPoint or none if fails to project.

#### `splitCurveByCurve(edge1: apex.construct.SketchPrimitive, edge2: apex.construct.SketchPrimitive) -> apex.construct.SketchPrimitive`
splits a pair of curves where they cross

- `edge1` — 2d edge in sketch plane
- `edge2` — 2d edge in sketch plane

Returns: the split Curve or none if fails to split.

#### `splitCurveByPoint(edge1: apex.construct.SketchPrimitive, point: Point2D) -> apex.construct.SketchPrimitive`
splits a pair of curves at a location on the curve

- `edge1` — 2d edge in sketch plane
- `point` — a point

Returns: the split Curve or none if fails to split.

#### `trimCurve(edge1: apex.construct.SketchPrimitive, point: Point2D) -> None`
Deletes curve or curve segment terminated by crossing curves.

- `edge1` — 2d edge in sketch plane
- `point` — indicates which portion of the curve to trim


## `apex.construct.SketchEdge`  (extends `SketchPrimitive`)
Properties: `end`, `length`, `name`, `start`

Methods:

#### `getEnd(: None) -> apex.construct.SketchVertex`
get end point of the edge

Returns: the end point

#### `getLength(: None) -> float`
get the length of the edge

Returns: the length of the edge

- `getName() -> str`
#### `getStart(: None) -> apex.construct.SketchVertex`
get start point of the edge

Returns: the start point

#### `update(length: float, startPoint: Point2D, endPoint: Point2D, annotation: str) -> bool`
Update the lenght, the start point, the end point or the annotation of an edge.

- `length` — the length of a straight line. not for curved edge
- `startPoint` — the start point of the edge
- `endPoint` — the end point of the edge
- `annotation` — the annotation of the edge

Returns: true if succeeds or false if fails


## `apex.construct.SketchPoint`  (extends `SketchPrimitive`)
Properties: `location`, `name`

Methods:

- `getLocation(: None) -> Point2D`
- `getName() -> str`
- `update(name: str, location: Point2D) -> bool`

## `apex.construct.SketchPrimitive`  (extends `Entity`)
Properties: `name`

Methods:

- `getName() -> str`

## `apex.construct.SketchProfile1D`  (extends `Sketch`)

Methods:

#### `deleteProfile(name: str) -> None`
delete the profile

- `name` — Name of the profile.

- `exit() -> None` — exit the sketch profile
#### `openProfile(name: str) -> Profile1D`
open the profile

- `name` — Name of the profile.

Returns: the profile object

#### `saveAsProfile(name: str, description: str = "") -> Profile1D`
save as the profile

- `name` — Name of the profile.
- `description` — Description of the profile.

Returns: the profile object

#### `saveProfile() -> Profile1D`
save the profile

Returns: the profile object


## `apex.construct.SketchVertex`  (extends `SketchPrimitive`)
Properties: `location`, `name`

Methods:

#### `getLocation(: None) -> Point2D`
get the location of the vertex

Returns: the location of the vertex

- `getName() -> str`
#### `update(location: Point2D, annotation: str) -> bool`
Update the location (X or Y or both) or the annotation of the sketch vertex.

- `location` — the coordinates of the vertex
- `annotation` — the annotation of the vertex

Returns: true if succeeds or false if fails


## `apex.construct.Spline`  (extends `SketchPrimitive`)
Properties: `end`, `length`, `name`, `points`, `start`

Methods:

#### `getEnd(: None) -> apex.construct.SketchVertex`
get end point of the spline

Returns: the end point

- `getLength(: None) -> float`
- `getName() -> str`
- `getPoints(: None) -> [Point2D]`
#### `getStart(: None) -> apex.construct.SketchVertex`
get start point of the spline

Returns: the start point

- `update(name: str) -> bool`

## `apex.construct.Vector3D`
object representing a 3D Vector in space.
Properties: `length`, `x`, `y`, `z`

Methods:

- `Vector3D(x: float = NAN, y: float = NAN, z: float = NAN) -> None`
#### `getLength() -> float`
get the length of this vector.

Returns: the vector length

This value represents a Length quantity and will be returned in the units of Length that are defined in the active ScriptUnitSystem.

- `getX() -> float`
- `getY() -> float`
- `getZ() -> float`
- `setX(x: float) -> None`
- `setY(y: float) -> None`
- `setZ(z: float) -> None`

