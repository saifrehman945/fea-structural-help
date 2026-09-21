# apex.geometry — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.geometry.Box`  (extends `Solid`)
Class representing a parametric cuboid (box). The Box size is parameterized by the length, height and depth properties. The origin and directions of the length, height and depth directions can be defined using either a location and orientation or an external coordinate system. The origin of the Box is defined to be on a Vertex of the Box and the length, height and depth dimensions are defined along the X, Y and Z axes of the integrated orientation or the external coordinate system.
Properties: `coordinateSystem`, `depth`, `height`, `length`, `origin`

Methods:

#### `getCoordinateSystem() -> apex.construct.CoordinateSystem`
The CoordinateSystem that defines the origin and orientation of the Box. If the Box was created using an integrated Orientation this property return a None type.

Returns: the Box coordinateSystem

#### `getDepth() -> float`
The depth of the Box. depth is defined parallel to the the X-axis of the Box orientation/external CoordinateSystem. depth represents a Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Box depth

#### `getHeight() -> float`
The height of the Box. height is defined parallel to the the X-axis of the Box orientation/external CoordinateSystem. height represents a Length quantity and must be supplied in the units of Length that are active in the ScriptUnitSystem.

Returns: the Box height

#### `getLength() -> float`
The Length of the Box. length is defined parallel to the the X-axis of the Box orientation/external CoordinateSystem. length represents a Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Box length

#### `getOrigin() -> Coordinate`
The origin of the Box as an ILocation. The origin lies at a vertex of the Box. The length, height and dpeth of the Box emanate from the origin.

Returns: the Box origin

- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
#### `setCoordinateSystem(coordinateSystem: apex.construct.CoordinateSystem) -> None`
Set the coordinateSystem of this Box.

- `coordinateSystem` — The CoordinateSystem that defines the origin and orientation of the Box.

#### `setDepth(depth: float) -> None`
Set the depth of this Box.

- `depth` — The depth of the Box. depth is defined parallel to the the X-axis of the Box orientation/external CoordinateSystem. depth represents a Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `setDescription(description: str) -> None`
Set the description of this Box.

- `description` — The description of the Box

#### `setHeight(height: float) -> None`
Set the height of this Box.

- `height` — The height of the Box. height is defined parallel to the the X-axis of the Box orientation/external CoordinateSystem. height represents a Length quantity and must be supplied in the units of Length that are active in the ScriptUnitSystem

#### `setLength(length: float) -> None`
Set the length of this Box.

- `length` — The Length of the Box. length is defined parallel to the the X-axis of the Box orientation/external CoordinateSystem. length represents a Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `setName(name: str) -> None`
Set the name of this Box.

- `name` — The name of the Box

#### `setOrientation(orientation: apex.IOrientation) -> None`
Set the orientation of this Box.

- `orientation` — The orientation of the Box as an IOrientation. The X, Y and Z axes of the Orientation define the direction of the length, height and depth directions

#### `setOrigin(origin: ILocation) -> None`
Set the origin of this Box.

- `origin` — The origin of the Box as an ILocation. The origin lies at a vertex of the Box. The length, height and dpeth of the Box emanate from the origin

#### `update(name: str = "", description: str = "", length: float = 0.0, height: float = 0.0, depth: float = 0.0, origin: apex.ILocation = None, orientation: apex.IOrientation = None, coordinateSystem: apex.construct.CoordinateSystem = None, parent: Entity = 0, color: [int] = [], renderStyle: apex.session.DisplayRenderStyle = apex.session.DisplayRenderStyle.Undefined, enableTransparency: apex.ApexBool = ApexBoolUndefined, transparencyLevel: int = -1, useLocalValue: bool = True) -> None`
Updates one or more modifiable properties of this Box. All modifiable properties of the Box are supported as optional arguments and the method allows multiple properties of the Box to be updated using a single method call. All arguments are optional and the values of all Box properties associated with the omitted arguments are left unchanged.

- `name` — The name of the Box. The name must be unique across all entities composed by the Part that composes this Box
- `description` — A string defining the description of this Box
- `length` — The length of the Box. length is a Length quantity and must be supplied in the Length units of the active ScriptUnitSystem
- `height` — The height of the Box. height is a Length quantity and must be supplied in the Length units of the active ScriptUnitSystem
- `depth` — The depth of the Box. depth is a Length quantity and must be supplied in the Length units of the active ScriptUnitSystem
- `origin` — The origin of the Box. length, depth and height emanate form this origin. origin and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `orientation` — Orientation of the Box. Defines directions of the length, depth and height dimensions orientation and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `coordinateSystem` — The CoordinateSystem that defines the origin an orientation of this Box. If the Box was not originally defined using an external CoordinateSystem, this CoordinateSystem will redefine the orientation and origin of this Box coordinateSystem an origin/orientation must not be included in the same update() method call otherwise the method will throw an exception
- `parent` — of this Box
- `color` — of this Box
- `renderStyle` — of this Box
- `enableTransparency` — of this Box
- `transparencyLevel` — of this Box
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.


## `apex.geometry.BoxCollection`  (extends `SolidCollection`)
Iterable collection of Solids, based on EntityCollection.

Methods:

- `BoxCollection() -> None`

## `apex.geometry.Cell`  (extends `GeometryTopology`)
Cell Class Object. extends GeometryTopology Class Object.
Properties: `centroid`, `edges`, `faces`, `meshControlEdges`, `tessellation`, `vertices`, `volume`

Methods:

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether all locations in this Cell lie within the specified tolerance of the input Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Cell is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Cell is coincident.If this Cell is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Cell is coincident with other objects. Coincidence is defined to exist if all locations on the Cell are fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location in this Cell is not enclosed by the other object this Cell is considered to be not coincident with the object.Note that this Cell does not need to fill the entire space associated with the other object to be coincident - it need only occupy a subset of the space of the other object to be considered coincident. Cell and Solid. All other entity types will be silently ignored. Cell must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices, Points, Edges, Curves, Faces, Surfaces, Cells and Solids that are coincident with this Cell, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Cell. Valid entity types for target include Solid, Cell, Surface, Face, Curve, Edge, Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Cell.

Returns: entities coincident with Cell

When possible the method will return only the "highest topology" objects that are coincident with this Cell. For example, if an entire Solid is coincident with this Cell only the Solid will be returned and its constituent Cells, Faces, Edges and Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Cell the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Cell. Coincidence is defined to exist if all locations on an object are fully enclosed by this Cell. A location is said to be enclosed by the Cell if the shortest distance between it and this Cell is less than the specified tolerance. If any location on the object is not enclosed by this Cell, the object is considered to be not coincident with this Cell.Note that an object does not need to fill the entire space associated with this Cell to be cosidered coincident - it need only occupy a subset of the space of this Cell to be considered coincident.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices, Points, Edges, Curves, Faces, Surfaces, Cells and Solids in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Cell, all locations on the object must lie within this distance of this Cell.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getCentroid() -> apex.Coordinate`
The location of the centroid of the Cell.

Returns: the cell centroid

#### `getEdges() -> apex.geometry.EdgeCollection`
get the edges for this cell.

Returns: the collection of edges

#### `getFaces() -> apex.geometry.FaceCollection`
get the faces for this cell.

Returns: the collection of faces

#### `getLocation() -> Coordinate`
The location of this Cell in 3D cartesian space as an apex.ILocation.

Returns: the Cell location

The location of a geometry Cell is defined to be at the centroid of the Cell

#### `getMeshControlEdges() -> MeshControlEdgeCollection`
A read only meshControlEdgeCollection contain all MeshControlEdge composed by the Faces of this Cell. If no MeshControlEdges are present in the Cell the method will return an empty collection.

Returns: collection of MeshControlEdge

#### `getOrientation() -> apex.Orientation`
the orientation of this Cell as an apex.IOrientation

Returns: the Cell orientation

The orientation of a Cell is aligned with the axes of an orientated bounding box (OOBB) that encloses this Cell

#### `getTessellation() -> apex.display.Tessellation2D`
returns the tessellation for this Cell as a Tesselation2D. The Tesselation2D includes the tessellation for all Faces, Edges and Vertices in this Cell as triangles, lines and points and includes the association between each tessellation and the Face, Edge and Vertex of this Cell that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

#### `getVertices() -> apex.geometry.VertexCollection`
get the vertices for this cell.

Returns: the collection of vertices

#### `getVolume() -> float`
get the volume of this cell.

Returns: the cell volume


## `apex.geometry.CellCollection`  (extends `GeometryTopologyCollection`)
Iterable collection of Cells, based on EntityCollection.

Methods:

- `CellCollection() -> None` — Construct a new CellCollection.
#### `appendList(cellList: [apex.geometry.Cell]) -> None`
Add Cells from a list to the end of this collection.

- `cellList` — list of Cell objects to add to the collection.

For example:


## `apex.geometry.Curve`  (extends `GeometryBody`)
Curve Class Object. extends GeometryBody Class Object.
Properties: `arcCenter`, `centroid`, `exteriorVertices`, `interiorVertices`, `length`, `massCenterNominal`, `massNominal`, `midPoint`, `parametricRange`, `principalInertiaFrameNominal`, `principalInertiaTensorNominal`, `tessellation`

Methods:

#### `evaluateClosestLocation(inputLocation: apex.ILocation) -> ZResultEvaluateClosestLocation`
Given an input location in 3D space, evaluates and returns a result object containing the location on this Curve that is closest to the input location and the vector from the input location to the closest Curve location.

- `inputLocation` — The target location in space for which the point of closest approach on the Curve is required.

Returns: Result object

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether all locations on this Curve lie within the specified tolerance of the input Edges, Curves, Faces, Surfaces, Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Curve is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Curve is coincident.If this Curve is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Curve is coincident with other objects. Coincidence is defined to exist if all locations on the Curve are fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location on this Curve is not enclosed by the other object it is considered to be not coincident with the object.Note that this Curve does not need to fill the entire space associated with the other object to be coincident - it need only occupy a subset of the space of the other object to be considered coincident. Edge, Curve, Face, Surface, Cell and Solid. All other entity types will be silently ignored. Curve must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `evaluateCurveParametricCoordinate(u: float) -> apex.geometry.ZResultEvaluateCurveParametricCoordinate`
This method takes a parametric Curve coordinate (u) as input and returns the equivalent 3D cartesian coordinates as a List of Point3D objects. For simple Curves where all of the Edges in the Curve are represented by a single underlying Curve, this method will return a List containing a single Point3D object based on evaluation of the parametric location (u) on the single underlying Curve. For more complex Curves, where the Edges in the Curve are represented by multiple underlying Curves, current Apex version will throw and exception. This method will be extended in a future Apex release as follows : The method will return one Point3D object per underlying Curve - strictly one point for each underlying Curve for which the input parametric coordinate is valid. Each Point3D location that is returned will have an accompanying ID that identifies the Underlying Curve. This ID cannot be used to access the underlying Curve but is intended to help users understand which coordinates can be reasonably compared - comparing parametric coordinates that are extracted from different underlying Curves should be performed with caution.

- `u` — The value of the parametric "u" coordinate

Returns: Result object

#### `evaluateOrientationCurveParametricCoordinate(u: float) -> apex.Orientation`
This method takes a 1D parametric coordinate (u) as input and returns the default Orientation at that position on the Curve.

- `u` — the 1D parametric coordinate (u) that defines the location on the Curve where the orientation will be evaluated

Returns: Result object

For simple Curves where all of the Edges in the Curve are represented by a single underlying Curve, this method will return the Orientation object based on evaluation of the orientation at the parametric location (u) on the single underlying Curve.For more complex Curves, where the Edges in the Curve are represented by MULTIPLE underlying Curves, current Apex versions will raise an exception.

#### `evaluatePointOnCurve(point: apex.ILocation) -> apex.geometry.ZResultEvaluatePointOnCurve`
This method takes a point in space (as a Point3D object) as input and returns a result object containing the closest point on the Curve as a float value representing the Curve parametric location (u). Apex Curves compose one or more Edges and Edges are bounded by Vertices. Each Edge is actually a region of an underlying Curve defined by one or more trimming vertices where the trimming vertices are the vertices of the Apex Curve. Simple Curves may be represented by single or multiple Edges where all of the Edges are regions of the same underlying Curve. In more complex Curves, the Curves that make up the single Apex Curve may actually be regions of multiple different underlying Curves. The underlying Curves are not visible to the user - the Apex Curve manages the Edges and presents the collection of Edges as a single Apex Curve with multiple contiguous Edges. Apex supports the concept of parametric locations on Curves and Edges. In both cases, the parametric location is actually the parametric location on the underlying Curve. For a point on a single Edge, or for a Curve that has just a single underling Curve, parametric coordinates are relatively straightforward. The range of the parametric coordinate (u) can be determined and the spatial coordinate (x, y, z) can be uniquely calculated for an given parametric location. Note that parametric locations outside of the parametric range of the Curve or Edge do not map to spatial coordinates, and even some parametric coordinates that lie within the parametric coordinate range may not map to real spatial coordinates. It should be noted that the parametric location that is returned by this method is actually the parametric location of the input point on the underlying Curve. In current versions of Apex, this method does not support evaluation of Curves that are supported by multiple underlying Curves and the method will throw an exception in such cases. A future release of Apex will extend this method to support complex Curves as follows: For Apex Curves that are represented by multiple underlying Surfaces, a series of evaluations using this method, each with different input spatial locations, will each return a single parametric location, however those parametric locations may be based on different underlying Curves. If you will be using this method to evaluate relative locations of objects based on the magnitude of a parametric location, you will be required to check that the parametric locations you are comparing are based on the same underlying Curve otherwise you may experience unexpected outcomes. For this reason, the method will return both the ID of the underlying Curve AND the parametric location. The underlying Curve cannot be accessed using the scripting API and the ID that is returned should only be used for comparison with ID's from other underlying Curves.

- `point` — a point in space (as a Point3D object)

Returns: Result object

#### `evaluateTangent(location: apex.ILocation) -> apex.construct.Vector3D`
Evaluates the tangent to this Curve at the input location and returns it as a Vector3D.

- `location` — The point on the Curve at which the tangent will be evaluated.

Returns: the tangent to the Curve at the input location as a Vector3D

ILocation and is expected to lie on, or close to the Curve.

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices, Points, Edges and Curves that are coincident with this Curve, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Curve. Valid entity types for target include Curve, Edge, Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Curve.

Returns: entities coincident with Curve

When possible the method will return only the "highest topology" objects that are coincident with this Curve. For example, if an entire Curve is coincident with this Curve only the Curve will be returned and its constituent Edges and Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Curve the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Curve. Coincidence is defined to exist if all locations on an object are fully enclosed by this Curve. A location is said to be enclosed by the Curve if the shortest distance between it and this Curve is less than the specified tolerance. If any location on the object is not enclosed by this Curve, the object is considered to be not coincident with this Curve.Note that an object does not need to fill the entire space associated with this Curve to be considered coincident - it need only occupy a subset of the space of this Curve to be considered coincident.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices, Points, Edges and Curves in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Curve, all locations on the object must lie within this distance of this Curve.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getArcCenter() -> apex.Coordinate`
return the arcCenter of this Curve. An arcCenter will be calculated for all Curves, even if the Curve is not a true Arc

Returns: the arcCenter of this Curve.

#### `getCentroid() -> apex.Coordinate`
The centroid of this Curve..

Returns: the curve centroid

#### `getExteriorVertices() -> geometry.VertexCollection`
get the exterior verticies on this curve.

Returns: collection of verticies

#### `getInteriorVertices() -> geometry.VertexCollection`
get the interior verticies on this curve.

Returns: collection of verticies

#### `getLength() -> float`
get the length of this curve.

Returns: the curve length

#### `getLocation() -> apex.Coordinate`
The location of this geometry Curve in 3D cartesian space as an apex.ILocation.

Returns: the Curve location

The location of a geometry Curve is defined to be at the midpoint of the Curve. For curves without branches the midpoint is defined to be the location on the curve where the lengths of the curve segments on either side are equal. For curves with branches, the location is defined to be the centroid of the Curve

#### `getMassCenterNominal() -> apex.Coordinate`
get the center of mass on this curve as an apex.Coordinate object.

Returns: the mass center of the Curve

The center of mass is a spatial location and will be returned using the units of Length that is defined in the active scripting unit system.The center of mass is calculated assuming a constant distribution of density throughout the Curve and is therefore independent of the actual density value.

#### `getMassNominal(density: float = 1.0) -> float`
get the nominal mass on this curve.

- `density` — The density of the Curve.

Returns: the mass nominal of the Curve

This method returns a value that represents a Mass quantity and uses the unit of Mass that is defined in the active scripting unit system.The calculation of the mass of a curve requires both a density and a length.The density may be supplied as an input argument and if omitted a value of 1.0 will be used.The length is determined directly from the Curve.

#### `getMidPoint() -> apex.Coordinate`
The location of the midPoint of the Curve.

Returns: the curve midPoint

The midPoint of a Curve is the location on the Curve where, if the Curve was split, both halves would be of equal lenght.

#### `getOrientation() -> apex.Orientation`
the orientation of this Curve as an apex.IOrientation.

Returns: the Curve orientation

The orientation of a Curve is calculated as follows,The x axis of the Orientation is tangent to the Curve at the midpoint of the Curve. The tangent direction follows the direction of increasing Edge parametric value - from low to high u for the Edge that contains the midpoint.The z axis of the Orientation is parallel to the binormal of the Curve at the midpoint of the Curve and follows the Face outward normal

#### `getParametricRange() -> {str:float}`
The range of the parametric space coordinates used by the Curve, Apex Curves compose one or more Edges and Edges are bounded by Vertices. Each Edge is actually a region of an underlying Curve defined by one or more trimming vertices where the trimming vertices are the vertices of the Curve that is being queried. Simple Curves may be represented by single or multiple Edges where all of the Edges are regions of the same underlying Curve. In more complex Curves, the Edges that make up the single Apex Curve may actually be regions of multiple different underlying Curves. The underlying Curves are not visible to the user - the Apex Curve manages the Edges and presents the collection of Edges as a single Apex Curve with multiple Edges. Apex supports the concept of parametric ranges on both Curves and Edges. In both cases the parametric range is actually the parametric range of the underlying trimmed Curve. For a single Edge, or for a Curve that has just a single underling Curve, parametric coordinate ranges are relatively straightforward. The range of the parametric coordinate can be determined from the single, trimmed underlying Curve. For Apex Curves that are defined by multiple underlying Curves, multiple parametric ranges exist and this attribute represents the maximum and minimum parametric coordinates across all of the trimmed underlying Curves - so the individual uStart and uEnd values returned here may occur on different underlying Curves.

Returns: parametric range

#### `getPrincipalInertiaFrameNominal() -> apex.construct.CoordinateSystem`
get the principal inertia frame on this curve as a rectangular CoordinateSystem.

Returns: the principal inertia frame of the Curve

The location and orientation of the principal inertia frame is calculated using an assumption of a constant distribution of density throughout the length of the Curve and is therefore independent of the actual density value.

#### `getPrincipalInertiaTensorNominal(density: float = 1.0) -> {str:float}`
get the nominal principal inertia tensor on this curve as a Dictionary.

- `density` — The density of the Curve.

Returns: the nominal principal inertia tensor of mass of the Curve

The returned Dictionary includes keys of type string and values of type float.The inertia tensor is returned using float values and uses the unit of Moment of Inertia (Mass x Length^2) that is defined in the active scripting unit system.The following keys represents the components of the inertia tensor - "ixx", "ixy", "ixz", "iyx", "iyy", "iyz", "izx", "izy", "izz".The calculation of the principal inertia tensor requires definition of the distribution of mass throughout the Curve and this is calculated based on the supplied "density" argument. A default density of "1.0" is supplied if this argument is omitted.

#### `getTessellation() -> apex.display.Tessellation1D`
returns the tessellation for this Curve as a Tesselation1D. The Tesselation1D includes the tessellation for all Edges and Vertices in this Curve as lines and points and includes the association between each tessellation and the Edge and Vertex of this Surface that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this Curve properties.

- `name` — of this Curve
- `parent` — of this Curve
- `color` — of this Curve
- `renderStyle` — of this Curve
- `enableTransparency` — of this Curve
- `transparencyLevel` — of this Curve

One or more parameters can be updated in one update call.


## `apex.geometry.CurveCollection`  (extends `GeometryBodyCollection`)
Iterable collection of Curves, based on EntityCollection.

Methods:

- `CurveCollection() -> None` — Construct a new CurveCollection.
#### `appendList(curveList: [apex.geometry.Curve]) -> None`
Add Curves from a list to the end of this collection.

- `curveList` — list of Curve objects to add to the collection.

For example:


## `apex.geometry.Cylinder`  (extends `Solid`)
Class representing a parametric solid geometric cylinder. This class can also define a partial cylinder where the shape sweeps around some angle less than 360 degrees. The Cylinder size is parameterized by its length, radius and sweepangle properties. The location can be defined using either a location and orientation or an external coordinate system. The location of the cylinder is defined to be at the center of the bottom circular face. The axis of revolution of the cylinder passes through this location and its orientation is defined by the orientation property. The location and orientation can alternately be defined using an external CoordinateSystem that defines both the location and the orientation of the cylinder where the cylinder origin is coincident with the coordinate system origin and the cylinder axis is coincident with the z-axis of the CoordinateSystem.
Properties: `coordinateSystem`, `length`, `origin`, `radius`, `sweepangle`

Methods:

#### `getCoordinateSystem() -> apex.construct.CoordinateSystem`
A CoordinateSystem that defines the origin and orientation of the Cylinder. If the Cylinder was created using an integrated Orientation this coordinateSystem may not exist and will return a None type.

Returns: the Cylinder coordinateSystem

#### `getLength() -> float`
The Length of the Cylinder. length is defined parallel to the the Z-axis of the Cylinder orientation. length represents a Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Cylinder length

#### `getOrigin() -> Coordinate`
The origin of the Cylinder as an ILocation. The length, radius and axis of the Cylinder emanate from the origin.

Returns: the Cylinder origin

#### `getRadius() -> float`
The radius of the Cylinder. radius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Cylinder radius

- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
#### `getSweepangle() -> float`
The angle used to define partial cylinders. The default value of 360 degrees represents a complete cylinder. Angles less than 360 degrees represent a partial cylinder - for example an angle of 180 degrees represents a semi cylinder, 90 degrees a quarter cylinder etc. sweepangle must be greater than 0 degrees and less than 360 degrees (or equivalent limit when other Angle units are supplied) sweepangle represents an Angle quantity and must be defined in the Angle units of the active script unit system.

Returns: the Cylinder sweepangle

#### `setCoordinateSystem(coordinateSystem: apex.construct.CoordinateSystem) -> None`
Set the coordinateSystem of this Cylinder.

- `coordinateSystem` — A CoordinateSystem that defines the origin and orientation of the Cylinder.

#### `setDescription(description: str) -> None`
Set the description of this Cylinder.

- `description` — The description of the Cylinder

#### `setLength(length: float) -> None`
Set the length of this Cylinder.

- `length` — The Length of the Cylinder. length is defined parallel to the the Z-axis of the Cylinder orientation. length represents a Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `setName(name: str) -> None`
Set the name of this Cylinder.

- `name` — The name of the Cylinder

#### `setOrientation(orientation: apex.IOrientation) -> None`
Set the orientation of this Cylinder.

- `orientation` — The orientation of the Cylinder as an IOrientation. The Orientation defines the direction of the cylinder axis

#### `setOrigin(origin: ILocation) -> None`
Set the origin of this Cylinder.

- `origin` — The origin of the Cylinder as an ILocation. The length, radius and axis of the Cylinder emanate from the origin

#### `setRadius(radius: float) -> None`
Set the radius of this Cylinder.

- `radius` — The radius of the Cylinder. radius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `setSweepangle(sweepangle: float) -> None`
Set the sweepangle of this Cylinder.

- `sweepangle` — The angle used to define partial cylinders. The default value of 360 degrees represents a complete cylinder. Angles less than 360 degrees represent a partial cylinder - for example an angle of 180 degrees represents a semi cylinder, 90 degrees a quarter cylinder etc. sweepangle must be greater than 0 degrees and less than 360 degrees (or equivalent limit when other Angle units are supplied) sweepangle represents an Angle quantity and must be defined in the Angle units of the active script unit system

#### `update(name: str = "", description: str = "", length: float = 0.0, radius: float = 0.0, sweepangle: float = 0.0, origin: apex.ILocation = None, orientation: apex.IOrientation = None, coordinateSystem: apex.construct.CoordinateSystem = None, parent: Entity = 0, color: [int] = [], renderStyle: apex.session.DisplayRenderStyle = apex.session.DisplayRenderStyle.Undefined, enableTransparency: apex.ApexBool = ApexBoolUndefined, transparencyLevel: int = -1, useLocalValue: bool = True) -> None`
Updates the properties of this Cylinder. All modifiable properties of the Cylinder are supported as optional arguments and multiple properties may be updated in a single call. Any properties not included in the argument list are unchanged by this method.

- `name` — The name of this Cylinder
- `description` — The description of this Cylinder
- `length` — The Length of this Cylinder. length is defined parallel to the the Z-axis of the Cylinder orientation. length represents a Length quantity and must be supplied in the units of Length that are active in the script unit system
- `radius` — The radius of this Cylinder. radius represents an Angle quantity and must be supplied in the units of Angle that are active in the script unit system
- `sweepangle` — The angle used to define partial cylinders. The default value of 360 degrees represents a complete cylinder. Angles less than 360 degrees represent a partial cylinder - for example an angle of 180 degrees represents a semi cylinder, 90 degrees a quarter cylinder etc. sweepangle must be greater than 0 degrees and less than 360 degrees (or equivalent limit when other Angle units are supplied)
- `origin` — the origin of this Cylinder as an ILocation. The length, radius and axis of the Cylinder emanate from the origin. origin and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `orientation` — The orientation of this Cylinder as an IOrientation. The Orientation defines the direction of the cylinder axis. orientation and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `coordinateSystem` — The CoordinateSystem that defines the origin and orientation of the Cylinder. If supplied, the location and orientation of the Cylinder will be updated based on the origin and orientation of this CoordinateSystem. coordinateSystem an origin/orientation must not be included in the same update() method call otherwise the method will throw an exception
- `parent` — of this Cylinder
- `color` — of this Cylinder
- `renderStyle` — of this Cylinder
- `enableTransparency` — of this Cylinder
- `transparencyLevel` — of this Cylinder
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.


## `apex.geometry.CylinderCollection`  (extends `SolidCollection`)
Iterable collection of Solids, based on EntityCollection.

Methods:

- `CylinderCollection() -> None`

## `apex.geometry.Edge`  (extends `GeometryTopology`)
Edge Class Object. extends GeometryTopology Class Object.
Properties: `arcCenter`, `centroid`, `connectedCells`, `connectedFaces`, `edgeSeed`, `length`, `midPoint`, `parametricRange`, `span`, `tessellation`, `vertices`, `verticesSuppressed`

Methods:

#### `evaluateClosestLocation(inputLocation: apex.ILocation) -> ZResultEvaluateClosestLocation`
Given an input location in 3D space, evaluates and returns a result object containing the location on this Edge that is closest to the input location and the vector from the input location to the closest Edge location.

- `inputLocation` — The target location in space for which the point of closest approach on the Edge is required.

Returns: Result object

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether all locations on this Edge lie within the specified tolerance of the input Edges, Curves, Faces, Surfaces, Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Edge is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Edge is coincident.If this Edge is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Edge is coincident with other objects. Coincidence is defined to exist if all locations of the Edge are fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location on this Edge is not enclosed by the other object this Edge is considered to be not coincident with the object.Note that this Edge does not need to fill the entire space associated with the other object to be coincident - it need only occupy a subset of the space of the other object to be considered coincident. Edge, Curve, Face, Surface, Cell and Solid. All other entity types will be silently ignored. Edge must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `evaluateEdgeParametricCoordinate(u: float) -> apex.Coordinate`
This method takes a parametric edge coordinate (u) as input and returns the equivalent 3D cartesian coordinates as a apex.Coordinate object.

- `u` — The value of the parametric "u" coordinate

Returns: apex::Coordinate

#### `evaluateEdgeTangent(u: float) -> apex.construct.Vector3D`
Evaluates the tangent to this Edge at the input parametric location and returns it as a Vector3D.

- `u` — The parametric location on the Edge at which the tangent will be evaluated.

Returns: the tangent to the Edge at the input location as a Vector3D

Edge may support only a subset of this parametric range.Use Edge.parametricRange to determine the parametric range that an Edge supports.

#### `evaluateOrientationEdgeParametricCoordinate(u: float) -> apex.Orientation`
This method takes a parametric edge coordinate (u) as input and returns the default orientation at that position as an apex.Orientation.

- `u` — the 1D parametric coordinate (u) that defines the location on this Edge where the orientation will be evaluated

Returns: Result object

#### `evaluatePointOnEdge(point: apex.ILocation) -> float`
evaluatePointOnEdge.

Returns: double

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices, Points, Edges and Curves that are coincident with this Edge, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Edge. Valid entity types for target include Curve, Edge, Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Edge.

Returns: entities coincident with Edge

When possible the method will return only the "highest topology" objects that are coincident with this Edge. For example, if an entire Curve is coincident with this Edge only the Curve will be returned and its constituent Edges and Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Edge the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Edge. Coincidence is defined to exist if all locations on an object are fully enclosed by this Edge. A location is said to be enclosed by the Edge if the shortest distance between it and this Edge is less than the specified tolerance. If any location on the object is not enclosed by this Edge, the object is considered to be not coincident with this Edge.Note that an object does not need to fill the entire space associated with this Edge to be considered coincident - it need only occupy a subset of the space of this Edge to be considered coincident.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices, Points, Edges and Curves in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Edge, all locations on the object must lie within this distance of this Edge.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getArcCenter() -> apex.Coordinate`
return the arcCenter of this Edge. An arcCenter will be calculated for all Edges, even if the Edge is not a true Arc

Returns: the arcCenter of this Edge.

#### `getCentroid() -> apex.Coordinate`
returns the centroid of this Edge as a Coordinate

Returns: the edge centroid location

#### `getConnectedCells() -> apex.geometry.CellCollection`
get the connected cells for this edge. All of the Cells, in the Geometry Body that contains the Edge, that share the Edge.

Returns: the collection of cells

#### `getConnectedFaces() -> apex.geometry.FaceCollection`
get the connected faces for this edge. All of the Faces, in the Geometry Body that contains the Edge, that share the Edge.

Returns: the collection of faces

#### `getEdgeSeed() -> apex.mesh.EdgeSeed`
return the associated EdgeSeed.

Returns: EdgeSeed object

#### `getLength() -> float`
get the length of this edge.

Returns: the edge volume

#### `getLocation() -> apex.Coordinate`
The location of this Edge in 3D cartesian space as an apex.ILocation.

Returns: the Edge location

The location of a geometry Edge is defined to be at the midpoint of the Edge. The midpoint of an Edge is defined to be that point that divides the Edge into two equal length segments

#### `getMidPoint() -> apex.Coordinate`
The location of the midPoint of the Edge.

Returns: the edge midPoint

The midPoint of an Edge is the location on the Edge where, if the Edge was split, both halves would be of equal lenght.

#### `getOrientation() -> apex.Orientation`
the orientation of this Edge as an apex.IOrientation.

Returns: the Edge orientation

The orientation of an Edge is calculated using one of the following methods depending upon the configuration of this Edge.Edge associated with a single FaceThe x axis of the Orientation is tangent to the Edge at the midpoint of the Edge. The tangent direction follows the direction of increasing Edge parametric value - from low to high uThe z axis of the Orientation is perpendicular to the Face at the midpoint of the Edge and follows the Face outward normalThe y axis of the Orientation is perpendicular to both the x and z axes using the right hand ruleEdge associated with multiple FacesThe x axis of the Orientation is tangent to the Edge at the midpoint of the Edge. The tangent direction follows the direction of increasing Edge parametric value - from low to high uThe z axis of the Orientation is perpendicular to the Face at the midpoint of the Edge and follows the Face outward normal

#### `getParametricRange() -> {str:float}`
The range of the parametric space coordinates used by the edge (uStart, uEnd). The coordinate range is returned in a Dictionary with keys "uStart" and "uEnd". The corresponding values are double types.

Returns: void

#### `getSpan() -> apex.attribute.BeamSpan`
returns the BeamSpan associated with this Edge or "None" if their is no associated BeamSpan.

Returns: BeamSpan object

#### `getTessellation() -> apex.display.Tessellation1D`
returns the tessellation for this Edge as a Tesselation1D. The Tesselation1D includes the tessellation for this Edge and its Vertices as lines and points and includes the association between each tessellation and the Edge and Vertex of this Edge that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

#### `getVertices() -> apex.geometry.VertexCollection`
get the vertices for this edge.

Returns: the collection of vertices

#### `getVerticesSuppressed() -> apex.geometry.VertexCollection`
get the suppressed vertices for this edge.

Returns: the collection of suppressed vertices


## `apex.geometry.EdgeCollection`  (extends `GeometryTopologyCollection`)
Iterable collection of Edges, based on EntityCollection.

Methods:

- `EdgeCollection() -> None` — Construct a new EdgeCollection.
#### `appendList(edgeList: [apex.geometry.Edge]) -> None`
Add Edges from a list to the end of this collection.

- `edgeList` — list of Edge objects to add to the collection.

For example:


## `apex.geometry.EdgeLoop`  (extends `Entity`, `IUserHighlightable`)
A Class that describes an unbranched closed loop of geometryEdges.
Properties: `edges`, `edgeSenses`, `length`, `nominalEnclosedArea`, `vertices`

Methods:

- `getEdgeSenses(: None) -> [bool]` — An ordered sequence (List) of Boolean values representing the senses of the Edges in this EdgeLoop. The number and order entries in this List matches the number and order of the Edges in the EdgeLoop.
- `getEdges(: None) -> EdgeCollection` — An ordered sequence of geometry Edges that define the EdgeLoop. The Edges are contiguous, unbranched and form a closed loop.
- `getLength(: None) -> float` — The total length of the Edge Loop determined by summing the length of all of the Edges that make up the EdgeLoop.
- `getNominalEnclosedArea(: None) -> float` — An approximation of the area enclosed by this EdgeLoop.
- `getVertices(: None) -> VertexCollection` — An ordered sequence of unique geometry Vertices extracted from the edges of the EdgeLoop such that the first Edge in the EdgeLoop connects the first and second vertices in this sequence, the second Edge connects vertices 2 and 3 and so on. Since the EdgeLoop is closed, the last Edge connects Vertex n-1 to the first Vertex in this sequence.

## `apex.geometry.EdgeLoopCollection`  (extends `EntityCollection`)
Iterable collection of EdgeLoops, based on EntityCollection.

Methods:

- `EdgeLoopCollection() -> None` — Construct a new EdgeLoopCollection.
#### `appendList(edgeLoopList: [apex.geometry.EdgeLoop]) -> None`
Add EdgeLoops from a list to the end of this collection.

- `edgeLoopList` — list of EdgeLoops to add to the collection.

For example:


## `apex.geometry.Ellipsoid`  (extends `Solid`)
Class representing a parametric solid geometric Ellipsoid. The Ellipsoid size is parameterized by three orthogonal 'radius' properties - xradius, yradius and zradius. The position of the Ellipsoid can be defined using either discrete location and orientation properties or an external coordinate system. The location of the Ellipsoid is defined to be at the center of the Ellipsoid. The orientation of the Ellipsoid is defined by the orientation property. The location and orientation can alternately be defined using an external CoordinateSystem that defines both the location and the orientation.
Properties: `coordinateSystem`, `origin`, `xradius`, `yradius`, `zradius`

Methods:

#### `getCoordinateSystem() -> apex.construct.CoordinateSystem`
A CoordinateSystem that defines the origin and orientation of the Ellipsoid. If the Ellipsoid was created using an integrated Orientation this coordinateSystem will not exist and will return a None type.

Returns: the Ellipsoid coordinateSystem

#### `getOrigin() -> Coordinate`
The origin of the Ellipsoid as an ILocation.

Returns: the Ellipsoid origin

- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
#### `getXradius() -> float`
The 'radius' of the Ellipsoid in the x direction. xradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Ellipsoid xradius

#### `getYradius() -> float`
The 'radius' of the Ellipsoid in the y direction. yradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Ellipsoid yradius

#### `getZradius() -> float`
The 'radius' of the Ellipsoid in the z direction. zradius represents a Length quantity and must be supplied in the units of Length that are active in the script unit system.

Returns: the Ellipsoid zradius

#### `setCoordinateSystem(coordinateSystem: apex.construct.CoordinateSystem) -> None`
Set the coordinateSystem of this Ellipsoid.

- `coordinateSystem` — A CoordinateSystem that defines the origin and orientation of the Ellipsoid.

#### `setDescription(description: str) -> None`
Set the description of this Ellipsoid.

- `description` — The description of the Ellipsoid

#### `setName(name: str) -> None`
Set the name of this Ellipsoid.

- `name` — The name of the Ellipsoid

#### `setOrientation(orientation: apex.IOrientation) -> None`
Set the orientation of this Ellipsoid.

- `orientation` — The orientation of the Ellipsoid as an IOrientation.

#### `setOrigin(origin: ILocation) -> None`
Set the origin of this Ellipsoid.

- `origin` — The origin of the Ellipsoid as an ILocation.

#### `setXradius(xradius: float) -> None`
Set the xradius of this Ellipsoid.

- `xradius` — The 'radius' of the Ellipsoid in the x direction. xradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `setYradius(yradius: float) -> None`
Set the yradius of this Ellipsoid.

- `yradius` — The 'radius' of the Ellipsoid in the y direction. yradius represents an Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `setZradius(zradius: float) -> None`
Set the zradius of this Ellipsoid.

- `zradius` — The 'radius' of the Ellipsoid in the z direction. zradius represents a Length quantity and must be supplied in the units of Length that are active in the script unit system

#### `update(name: str = "", description: str = "", xradius: float = 0.0, yradius: float = 0.0, zradius: float = 0.0, origin: apex.ILocation = None, orientation: apex.IOrientation = None, coordinateSystem: apex.construct.CoordinateSystem = None, parent: Entity = 0, color: [int] = [], renderStyle: apex.session.DisplayRenderStyle = apex.session.DisplayRenderStyle.Undefined, enableTransparency: apex.ApexBool = ApexBoolUndefined, transparencyLevel: int = -1, useLocalValue: bool = True) -> None`
Updates the properties of this Ellipsoid. All modifiable properties of the Ellipsoid are supported as optional arguments and multiple properties may be updated in a single call. Any properties not included in the argument list are unchanged by this method.

- `name` — The name of this Ellipsoid
- `description` — The description of this Ellipsoid
- `xradius` — The 'radius' of this Ellipsoid in the x direction. xradius represents a Length quantity and must be supplied in the units of Length that are active in the script unit system
- `yradius` — The 'radius' of this Ellipsoid in the y direction. yradius represents a Length quantity and must be supplied in the units of Length that are active in the script unit system
- `zradius` — The 'radius' of this Ellipsoid in the z direction. zradius represents a Length quantity and must be supplied in the units of Length that are active in the script unit system
- `origin` — the origin of this Ellipsoid as an ILocation. origin and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `orientation` — The orientation of this Ellipsoid as an IOrientation. orientation and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `coordinateSystem` — The CoordinateSystem that defines the origin and orientation of this Ellipsoid. If supplied, the location and orientation of this Ellipsoid will be updated based on the origin and orientation of this CoordinateSystem coordinateSystem an origin/orientation must not be included in the same update() method call otherwise the method will throw an exception
- `parent` — of this Ellipsoid
- `color` — of this Ellipsoid
- `renderStyle` — of this Ellipsoid
- `enableTransparency` — of this Ellipsoid
- `transparencyLevel` — of this Ellipsoid
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.


## `apex.geometry.EllipsoidCollection`  (extends `SolidCollection`)
Iterable collection of Solids, based on EntityCollection.

Methods:

- `EllipsoidCollection() -> None`

## `apex.geometry.Face`  (extends `GeometryTopology`)
Face Class Object. extends GeometryTopology Class Object.
Properties: `area`, `centroid`, `connectedCells`, `cylindricalAxis`, `cylindricalAxisEndPoint`, `cylindricalAxisMidPoint`, `cylindricalAxisStartPoint`, `edges`, `edgesSuppressed`, `exteriorEdgeLoops`, `interiorEdgeLoops`, `meshControlEdges`, `parametricRange`, `tessellation`, `vertices`, `verticesSuppressed`

Methods:

#### `evaluateClosestLocation(inputLocation: apex.ILocation) -> ZResultEvaluateClosestLocation`
Given an input location in 3D space, evaluates and returns a result object containing the location on this Face that is closest to the input location and the vector from the input location to the closest Face location.

- `inputLocation` — The target location in space for which the point of closest approach on the Face is required.

Returns: Result object

#### `evaluateClosestLocationOnFace(point: apex.ILocation) -> apex.geometry.ZResultEvaluateClosestLocationOnFace`
DEPRECATED: "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE " This method has been superseded by the equivalent "apex.geometry.face.evaluateClosestLocation()" method.

- `point` — The point in space that is being evaluated to find the closest location on the face.

Returns: Result object

This method takes a point in space (as a apex::ILocation* object) as input and returns the location on the Face (as parametric face coordinates(u, v)) that is closest to the input point, the distance between the input point and the closest face location and the vector from the input point to the closest face location.

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether all locations on this Face lie within the specified tolerance of the input Faces, Surfaces, Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Face is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Face is coincident.If this Face is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Face is coincident with other objects. Coincidence is defined to exist if all locations on the Face is fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location on this Face is not enclosed by the other object this Face is considered to be not coincident with the object.Note that this Face does not need to fill the entire space associated with the other object to be coincident - it need only occupy a subset of the space of the other object to be considered coincident. Face, Surface, Cell and Solid. All other entity types will be silently ignored. Face must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `evaluateFaceCurvatureUV(u: float, v: float) -> apex.geometry.ZResultEvaluateFaceCurvature`
This method takes a parametric face coordinate (u, v) as input and returns normal, principal1, principal2 and curvature1, curvature2 to the surface at that location as apex.construct.Vector3D objects in a ResultObject.

- `u` — The value of the parametric "u" coordinate
- `v` — The value of the parametric "v" coordinate

Returns: Result object

#### `evaluateFaceParametricCoordinate(u: float, v: float) -> apex.Coordinate`
evaluateFaceParametricCoordinate.

- `u` — The value of the parametric "u" coordinate
- `v` — The value of the parametric "v" coordinate

Returns: apex::Coordinate

#### `evaluateFaceTangentUV(u: float, v: float) -> apex.geometry.ZResultEvaluateFaceTangent`
This method takes a parametric face coordinate (u, v) as input and returns two tangents to the surface at that location as apex.construct.Vector3D objects in a ResultObject. The returned Face tangents are calculated in the parametric U and V directions.

- `u` — The value of the parametric "u" coordinate
- `v` — The value of the parametric "v" coordinate

Returns: Result object

#### `evaluateNormal(u: float, v: float) -> apex.construct.Vector3D`
This method takes a parametric face coordinate (u, v) as input and returns the normal to the face at that location as a apex.construct.Vector3D object.

- `u` — The value of the parametric "u" coordinate
- `v` — The value of the parametric "v" coordinate

Returns: normal Vector

#### `evaluateOrientationFaceParametricCoordinate(u: float, v: float) -> apex.Orientation`
This method takes a parametric face coordinate (u,v) as input and returns a default Orientation at that position as an apex.Orientation.

- `u` — the 'u' component of the 2D parametric coordinate (u, v) that defines the location on this Face where the orientation will be evaluated
- `v` — the 'v' component of the 2D parametric coordinate (u, v) that defines the location on this Face where the orientation will be evaluated

Returns: Result object

#### `evaluatePointOnFace(point: apex.ILocation) -> apex.geometry.ZResultEvaluatePointOnFace`
This method takes a point in space (as a apex.ILocation* object)as input and returns the equivalent position as parametric coordinates on the face..

Returns: Result object

#### `evaluateTangentInDirection(u: float, v: float, direction: apex.construct.Vector3D) -> apex.construct.Vector3D`
This method takes a parametric face coordinate (u, v) and a direction vector as input and returns the tangent to the surface at the input location as apex.construct.Vector3D objects in a ResultObject.The tangent is calculated in the direction of the projection of the input direction vector onto the Face.

- `u` — The value of the parametric "u" coordinate
- `v` — The value of the parametric "v" coordinate
- `direction` — the direction vector

Returns: tangent vector

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices, Points, Edges, Curves, Faces and Surfaces that are coincident with this Face, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Face. Valid entity types for target include Surface, Face, Curve, Edge, Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Face.

Returns: entities coincident with Face

When possible the method will return only the "highest topology" objects that are coincident with this Face. For example, if an entire Surface is coincident with this Face only the Surface will be returned and its constituent Faces, Edges and Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Face the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Face. Coincidence is defined to exist if all locations on an object are fully enclosed by this Face. A location is said to be enclosed by the Face if the shortest distance between it and this Face is less than the specified tolerance. If any location on the object is not enclosed by this Face, the object is considered to be not coincident with this Face.Note that an object does not need to fill the entire space associated with this Face to be considered coincident - it need only occupy a subset of the space of this Face to be considered coincident.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices, Points, Edges, Curves, Faces and Surfaces in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Face, all locations on the object must lie within this distance of this Face.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getArea() -> float`
get the area of this face.

Returns: the face area

#### `getCentroid() -> apex.Coordinate`
The location of the centroid of the Face.

Returns: the face centroid location

#### `getConnectedCells() -> CellCollection`
get the connected Cells on this face.

Returns: collection of cells

#### `getCylindricalAxis() -> apex.construct.Vector3D`
return the cylindrical axis of this Face. An cylindricalAxis will be calculated for all Faces, even if the Face is not a true cylinder or partial cylinder

Returns: the axis direction of this Face

#### `getCylindricalAxisEndPoint() -> apex.Coordinate`
return the end point of the cylindrical axis of this Face. An cylindricalAxisEndPoint will be calculated for all Faces, even if the Face is not a true cylinder or partial cylinder

Returns: the end point of the cylindrical axis of this Face

#### `getCylindricalAxisMidPoint() -> apex.Coordinate`
return the mid point of the cylindrical axis of this Face. An cylindricalAxisMidPoint will be calculated for all Faces, even if the Face is not a true cylinder or partial cylinder

Returns: the mid point of the cylindrical axis of this Face

#### `getCylindricalAxisStartPoint() -> apex.Coordinate`
return the start point of the cylindrical axis of this Face. An cylindricalAxisStartPoint will be calculated for all Faces, even if the Face is not a true cylinder or partial cylinder

Returns: the start point of the cylindrical axis of this Face

#### `getEdges() -> EdgeCollection`
get the edges on this face.

Returns: collection of edges

#### `getEdgesSuppressed() -> EdgeCollection`
get the suppressed edges on this face.

Returns: collection of suppressed edges

#### `getExteriorEdgeLoops() -> EdgeLoopCollection`
Returns the bounding EdgeLoops for this Face.

Returns: exterior EdgeLoopCollection

The EdgeLoop comprises the sequence of Edges that bound this Face

#### `getInteriorEdgeLoops() -> EdgeLoopCollection`
Returns all interior EdgeLoops that may exist for this Face.

Returns: interior EdgeLoopCollection

#### `getLocation() -> apex.Coordinate`
The location of this Face in 3D cartesian space as an apex.ILocation.

Returns: the Face location

The location of a geometry Face is defined to be at the centroid of the Face.

#### `getMeshControlEdges() -> MeshControlEdgeCollection`
A read only meshControlEdgeCollection contain all MeshControlEdge composed by the Faces of this Cell. If no MeshControlEdges are present in the Cell the method will return an empty collection.

Returns: collection of MeshControlEdge

#### `getOrientation() -> apex.Orientation`
the orientation of this Face as an apex.IOrientation.

Returns: the Face orientation

The orientation of this Face is calculated as follows.The x axis of the Face orientation is parallel to the positive u direction of the Face at the Face centroidThe z axis of the Face orientation is perpendicular to the Face at the Face centroid and aligned with the Face outward normal at that locationThe y axis of the Face orientation is perpendicular to the x and z axes following the right hand rule

#### `getParametricRange() -> {str:float}`
getParametricRange.

Returns: void

#### `getTessellation() -> apex.display.Tessellation2D`
returns the tessellation for this Face as a Tesselation2D. The Tesselation2D includes the tessellation for this Face and its Edges and Vertices as triangles, lines and points and includes the association between each tessellation and the Face, Edge and Vertex of this Face that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

#### `getVertices() -> VertexCollection`
get the verticies on this face.

Returns: collection of verticies

#### `getVerticesSuppressed() -> VertexCollection`
get the suppressed verticies on this face.

Returns: collection of suppressed verticies

- `isMidsurface() -> bool` — Boolean value indicating whether this Face is part of an automatically extracted mid-surface.
#### `update(midsurfaceTopFaces: apex.geometry.FaceCollection = None, midsurfaceBottomFaces: apex.geometry.FaceCollection = None) -> None`
Updates one or more properties of this Face. This method allows multiple properties of the Face to be updated using a single method call. All arguments are optional and the values of all properties associated with the omitted arguments are left unchanged.

- `midsurfaceTopFaces` — a collection of Faces that represent the 'Top' boundary of the region for which this Face represents the mid-surface. The collection will be empty if the Face does not represent a mid-surface
- `midsurfaceBottomFaces` — a collection of Faces that represent the 'Bottom' boundary of the region for which this Face represents the mid-surface. The collection will be empty if the Face does not represent a mid-surface


## `apex.geometry.FaceCollection`  (extends `GeometryTopologyCollection`)
Iterable collection of Faces, based on EntityCollection.

Methods:

- `FaceCollection() -> None` — Construct a new FaceCollection.
#### `appendList(faceList: [apex.geometry.Face]) -> None`
Add Faces from a list to the end of this collection.

- `faceList` — list of Face objects to add to the collection.

For example:


## `apex.geometry.FacetedCurve`  (extends `Curve`)
FacetedCurve Class Object. extends Curve Class Object.

## `apex.geometry.FacetedCurveCollection`  (extends `CurveCollection`)
Iterable collection of Curves, based on EntityCollection.

Methods:

- `FacetedCurveCollection() -> None`

## `apex.geometry.FacetedSolid`  (extends `Solid`)
FacetedSolid Class Object. extends Solid Class Object.

## `apex.geometry.FacetedSolidCollection`  (extends `SolidCollection`)
Iterable collection of Solids, based on EntityCollection.

Methods:

- `FacetedSolidCollection() -> None`

## `apex.geometry.FacetedSurface`  (extends `Surface`)
FacetedSurface Class Object. extends Surface Class Object.

## `apex.geometry.FacetedSurfaceCollection`  (extends `SurfaceCollection`)
Iterable collection of Surfaces, based on EntityCollection.

Methods:

- `FacetedSurfaceCollection() -> None`

## `apex.geometry.GeometryBody`  (extends `Entity`, `IDisplayable`, `IUserAttributes`, `IName`, `IPhysical`, `IOrientation`, `IActivatable`)
Properties: `cells`, `constraints`, `edges`, `edgesSuppressed`, `elements`, `exteriorNodes`, `faces`, `initialConditions`, `interiorNodes`, `loads`, `meshes`, `nodes`, `parent`, `referencedBy`, `referenceSystem`, `vertices`, `verticesSuppressed`

Methods:

#### `assignMaterial(pMat: apex.attribute.Material) -> bool`
assign a material to this GeometryBody.

Returns: status of true or false (bool)

#### `assignShellSection(pSection: apex.attribute.ShellSection) -> bool`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.attribute.createFieldThicknessOffsetConstant. assign a shell section to this GeometryBody.

Returns: status of true or false (bool)

#### `exportGeometry(filename: str, cadFormat: apex.geometry.CADFormat, unitSystem: str = "m", stlMergeCells: bool = True, exportVirtualFaces: bool = False, exportVirtualFaceMethod: apex.VirtualFaceExportMethod = apex.VirtualFaceExportMethod.NurbsOnly, exportBodyPositionInLocal: bool = False) -> None`
Export Geometry from this GeometryBody to a file using the supplied CAD format.

- `filename` — Fully qualified name of the file to which the geometry objects will be exported.
- `cadFormat` — defines the format of the CAD file that will be exported using an apex.geometry.CADFormat enumeration.
- `unitSystem` — A string to identify the units to be used during export. Unit support is dependent on the CADFormat of the exported file and not all formats support units. Of the CAD formats currently supported by Apex, only the IGES format supports user defined export units. The table below shows each of the supported unit systems and associated unitSystem values for IGES export CAD Format - Length unit - unitSystem value IGES Kilometer km Meter m Centimeter cm Millimeter mm Micrometer um Mile mile Foot ft Inch in Milliinch mi Microinch ui If the IGES format is selected, unitSystem must be provided. If a value other than one in the above table is supplied, the method will throw an exception
- `stlMergeCells` — optional Boolean argument (default = True) that controls how multi-cellular solids will be represented in STL files. This argument is only relevant when the cadFormat type is an STL type and is silently ignored for all other formats. When True (Default), all cells in a multi-cellular solid will be merged into a single cell during export by removing all internal Faces. The GeometryBody is unaffected by this operation. When False, all cells in multi-cellular solids will be present in the exported STL file.
- `exportVirtualFaces` — Optional Argument, Default = False, where each virtual faces will be exported as a single face. This only applies to CAD Format Parasolid. The purpose is to export geometry topology that is consistent with native Apex to maintaining associatively with mesh, loads, BCs and other attributes. An attempt will be made to export the virtual faces as NURBS, by replacing the each virtual face with a single NURBS face. If this fails, then a facet body face will be used instead.
- `exportVirtualFaceMethod` — This applies to exportGeometry API only. It controls what is permitted for converting virtual topology to exportable faces with the same topology. This is ignored if exportVirtualFaces is False. If set to NurbsAndFaceted, then the system will try to convert to NURBS, and if that fails, it will then convert the face into a faceted face. If set to NurbsOnly (Default), then it will try to convert each virtual face to NURBS only.
- `exportBodyPositionInLocal` — Optional Boolean argument to export the geometry body in local position based the reference system of the body and parent part. By default, it is false. The system will export the geometry body position in global.

#### `getCell(id: int int int) -> apex.geometry.Cell`
get the cell for the specified id

- `id` — the id of cell

Returns: the cell

#### `getCells(ids: str = "") -> apex.geometry.CellCollection`
get the cells for the specified ids.

- `ids` — the ids of cells. If ids is empty, return all cells under the body

Returns: the collection of cells

- `getConstraints() -> apex.EntityCollection` — Returns a collection of all Constraints that are applied to this GeometryBody. The Constraints may be applied directly to the GeometryBody or to its Face, Edge, Vertex, or MeshBody. If no Constraints are associated with the GeometryBody the method will return an empty EntityCollection.
#### `getEdge(id: int int int) -> apex.geometry.Edge`
get the edge for the specified id

- `id` — the id of edge

Returns: the edge

#### `getEdges(ids: str = "") -> apex.geometry.EdgeCollection`
get the edges for the specified ids.

- `ids` — the ids of edges. If ids is empty, return all edges under the body

Returns: the collection of edges

#### `getEdgesSuppressed(ids: str = "") -> apex.geometry.EdgeCollection`
get the suppressed edges for the specified ids.

- `ids` — the ids of suppressed edges. If ids is empty, return all suppressed edges under the body

Returns: the collection of suppressed edges

#### `getElements() -> apex.mesh.ElementCollection`
get the elements on this geometry body.

Returns: collection of elements

#### `getExteriorNodes() -> apex.mesh.NodeCollection`
get the exterior nodes on this geometry body.

Returns: collection of nodes

#### `getFace(id: int int int) -> apex.geometry.Face`
get the face for the specified id

- `id` — the id of face

Returns: the face

#### `getFaces(ids: str = "") -> apex.geometry.FaceCollection`
get the faces for the specified ids.

- `ids` — the ids of faces. If ids is empty, return all faces under the body

Returns: the collection of faces

- `getInitialConditions() -> apex.EntityCollection` — Returns a collection of all InitialConditions that are applied to this GeometryBody. The InitialConditions may be applied directly to the GeometryBody or to its Face, Edge, Vertex, or MeshBody. If no InitialConditions are associated with the GeometryBody the method will return an empty EntityCollection.
#### `getInteriorNodes() -> apex.mesh.NodeCollection`
get the interior nodes on this geometry body.

Returns: collection of nodes

- `getLoads() -> apex.EntityCollection` — Returns a collection of all Loads that are applied to this GeometryBody. The Loads may be applied directly to the GeometryBody or to its Face, Edge, Vertex, or MeshBody. If no Loads are associated with the GeometryBody the method will return an empty EntityCollection.
#### `getMeshes() -> apex.mesh.MeshBodyCollection`
get the meshes on this geometry body.

Returns: collection of meshes

#### `getNodes() -> apex.mesh.NodeCollection`
get the nodes on this geometry body.

Returns: collection of nodes

- `getParent() -> Part` — Get the parent Part for this GeometryBody.
- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
- `getReferencedBy() -> apex.EntityCollection` — returns a collection of all entities that directly Reference this GeometryBody (Point, Curve, Surface, Solid)
#### `getVertex(id: int int int) -> apex.geometry.Vertex`
get the vertex for the specified id

- `id` — the id of vertex

Returns: the vertex

#### `getVertices(ids: str = "") -> apex.geometry.VertexCollection`
get the vertices for the specified ids.

- `ids` — the ids of vertices. If ids is empty, return all vertices under the body

Returns: the collection of vertices

#### `getVerticesSuppressed(ids: str = "") -> apex.geometry.VertexCollection`
get the suppressed vertices for the specified ids.

- `ids` — the ids of suppressed vertices. If ids is empty, return all suppressed vertices under the body

Returns: the collection of suppressed vertices

#### `setParent(parent: Part) -> None`
Set a Part to be the new parent for this GeometryBody.

- `parent` — to be assigned the new parent of this GeometryBody

- `setReferenceSystem(refSysPair: ( apex.ILocation,apex.IOrientation )) -> None`
#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this GeometryBody properties.

- `name` — of this GeometryBody
- `parent` — of this GeometryBody
- `color` — of this GeometryBody
- `renderStyle` — of this GeometryBody
- `enableTransparency` — of this GeometryBody
- `transparencyLevel` — of this GeometryBody

Either the name, parent, or both can be updated in one update call.


## `apex.geometry.GeometryBodyCollection`  (extends `IPhysicalCollection`)

Methods:

- `GeometryBodyCollection() -> None` — Construct a new GeometryBodyCollection.
#### `appendList(geometryBodyList: [apex.geometry.GeometryBody]) -> None`
Add GeometryBodies from a list to the end of this collection.

- `geometryBodyList` — list of GeometryBodies to add to the collection.

For example:


## `apex.geometry.GeometryFeature`  (extends `Entity`)
Class representing an Apex geometry feature such as a 3D Hole, Fillet, Chamfer etc.
Properties: `featureDimension`, `featureType`, `topology`

Methods:

- `getFeatureDimension(: None) -> float` — Gets the leading dimension of this GeometryFeature The meaning of this property is dependent on the feature type as follows Hole2D - diameter of the hole Fillet2D - radius of the fillet Chamfer2D - width of the chamfer Hole3D - diameter of the Hole Fillet3D - radius of the Fillet Chamfer3D - width of the Chamfer featureDimension represents a Length quantity and must be interpreted in the units of Length from the active script unit system.
- `getFeatureType() -> apex.geometry.GeometryFeatureType` — Gets the type of this GeometryFeature as an apex.geometry.GeometryFeatureType.
- `getTopology() -> apex.geometry.GeometryTopologyCollection` — Gets collection of geometry topologies (Faces, Edges) that represent this feature.

## `apex.geometry.GeometryFeatureCollection`  (extends `EntityCollection`)
Iterable collection of GeometryFeatures, based on EntityCollection.

Methods:

- `GeometryFeatureCollection() -> None` — Construct a new GeometryFeatureCollection.
#### `appendList(geometryFeatureList: [apex.geometry.GeometryFeature]) -> None`
Add GeometryFeatures from a list to the end of this collection.

- `geometryFeatureList` — list of GeometryFeatures to add to the collection.

For example:


## `apex.geometry.GeometryTopology`  (extends `Entity`, `IIdentifier`, `IPhysical`, `IUserAttributes`, `IOrientation`)
GeometryTopology class exposes Topology 'get' methods.
Properties: `body`, `constraints`, `elements`, `exteriorNodes`, `initialConditions`, `interiorNodes`, `loads`, `nodes`, `referencedBy`

Methods:

- `asEntity() -> apex.Entity`
#### `getBody() -> GeometryBody`
Returns the Geometry Body that contains the topology.

Returns: Geometry Body that contains the topology

- `getConstraints() -> apex.EntityCollection` — Returns a collection of all Constraints that are applied to this GeometryTopology. If no Constraints are associated with the GeometryTopology the method will return an empty EntityCollection.
#### `getElements() -> apex.mesh.ElementCollection`
get the elements on this object.

Returns: collection of elements

#### `getExteriorNodes() -> apex.mesh.NodeCollection`
get the exterior nodes on this object.

Returns: collection of nodes

- `getInitialConditions() -> apex.EntityCollection` — Returns a collection of all InitialConditions that are applied to this GeometryTopology. If no InitialConditions are associated with the GeometryBody the method will return an empty EntityCollection.
#### `getInteriorNodes() -> apex.mesh.NodeCollection`
get the interior nodes on this object.

Returns: collection of nodes

- `getLoads() -> apex.EntityCollection` — Returns a collection of all Loads that are applied to this GeometryBody. The Loads may be applied directly to the GeometryBody or to its Face, Edge, Vertex, or MeshBody. If no Loads are associated with the GeometryBody the method will return an empty EntityCollection.
#### `getNodes() -> apex.mesh.NodeCollection`
get the nodes on this object.

Returns: collection of nodes

- `getReferencedBy() -> apex.EntityCollection` — returns a collection of all entities that directly Reference this geometry Topology (Vertex, Edge, Face, Cell)

## `apex.geometry.GeometryTopologyCollection`  (extends `IPhysicalCollection`)
Iterable collection of GeometryTopologies, based on EntityCollection.

Methods:

- `GeometryTopologyCollection() -> None` — Construct a new GeometryTopologyCollection.
#### `appendList(geometryTopologyList: [apex.geometry.GeometryTopology]) -> None`
Add GeometryTopology Entities from a list to the end of this collection.

- `geometryTopologyList` — list of GeometryTopology objects to add to the collection.

For example:


## `apex.geometry.MeshControlEdge`  (extends `Entity`, `IIdentifier`, `IDisplayable`, `IPhysical`)
Properties: `length`, `midPoint`, `parent`

Methods:

- `getLength() -> float` — The length of the MeshControlEdge.
- `getMidPoint() -> apex.Coordinate` — The location of the midPoint of MeshControlEdge, returned as a Coordinate.
- `getParent() -> Face` — The parent Face of this MeshControlEdge.

## `apex.geometry.MeshControlEdgeCollection`  (extends `IPhysicalCollection`)
Iterable collection of Mesh Control Edges, based on EntityCollection.

Methods:

- `MeshControlEdgeCollection() -> None` — Construct a new MeshControlEdgeCollection.
#### `appendList(meshControlEdgeList: [apex.geometry.MeshControlEdge]) -> None`
Add MeshControlEdges from a list to the end of this collection.

- `meshControlEdgeList` — list of MeshControlEdge to add to the collection.

For example:


## `apex.geometry.Point`  (extends `GeometryBody`)
Point Class Object. extends GeometryBody Class Object.
Properties: `centroid`, `tessellation`

Methods:

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether the location of all Vertices in this Point lie within the specified tolerance of the input Vertices, Points, Edges, Curves, Faces, Surfaces, Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Point is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Point is coincident.If this Point is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Point is coincident with other objects. Coincidence is defined to exist if the location of the Point is fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location of this Point is not enclosed by the other object this Point is considered to be not coincident with the object. Vertex, Point, Edge, Curve, Face, Surface, Cell and Solid. All other entity types will be silently ignored. Point must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices and Points that are coincident with this Point, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Point. Valid entity types for target include Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Point.

Returns: entities coincident with Point

When possible the method will return only the "highest topology" objects that are coincident with this Point. For example, if an entire Point is coincident with this Point only the Point will be returned and its constituent Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Point the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Point. Coincidence is defined to exist if the distance between the object and this Point is less than or equal to the supplied tolerance.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices and Points in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Point, all locations on the object must lie within this distance of this Point.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getAssociatedSeedPoint() -> apex.mesh.SeedPoint`
return the associated Seed Point.

Returns: SeedPoint object

#### `getCentroid() -> apex.Coordinate`
returns the centroid of this Point Body as a Coordinate

Returns: the point centroid

#### `getLocation() -> apex.Coordinate`
The location of this geometry Point in 3D cartesian space as an apex.ILocation.

Returns: the Point location

Note that Apex Point objects may compose one OR MORE vertices - they are not always simple single vertex points.The location of a geometry Point is defined to be at the centroid of the Point - the average location of all of the vertices in the Point. For simple Points composing a single vertex, this location is equal to the coordinates of the Point/vertex

#### `getOrientation() -> apex.Orientation`
the orientation of this Point as an apex.IOrientation

Returns: the Point orientation

The orientation of a Point body is aligned with the axes of an orientated bounding box (OOBB) that encloses this Point Body

#### `getTessellation() -> apex.display.Tessellation0D`
returns the tessellation for this Point as a Tesselation0D. The Tesselation0D includes the tessellation for all Vertices in this Point as points and includes the association between each tessellation and the Vertex of this Point that it represents. Point tessellation is not impacted by the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation.

Returns: Tessellation

#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this Point properties.

- `name` — of this Point
- `parent` — of this Point
- `color` — of this Point
- `renderStyle` — of this Point
- `enableTransparency` — of this Point
- `transparencyLevel` — of this Point

One or more parameters can be updated in one update call.


## `apex.geometry.PointCollection`  (extends `GeometryBodyCollection`)
Iterable collection of Points, based on EntityCollection.

Methods:

- `PointCollection() -> None` — Construct a new PointCollection.
#### `appendList(pointList: [apex.geometry.Point]) -> None`
Add Points from a list to the end of this collection.

- `pointList` — list of Point objects to add to the collection.

For example:


## `apex.geometry.Solid`  (extends `GeometryBody`)
Solid Class Object. extends GeometryBody Class Object.
Properties: `cells`, `centroid`, `exteriorEdges`, `exteriorFaces`, `exteriorVertices`, `interiorEdges`, `interiorFaces`, `interiorVertices`, `massCenterNominal`, `massNominal`, `meshControlEdges`, `principalInertiaFrameNominal`, `principalInertiaTensorNominal`, `tessellationExterior`, `tessellationInterior`, `volume`

Methods:

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether all locations on this Solid lie within the specified tolerance of the input Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Solid is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Solid is coincident.If this Solid is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Solid is coincident with other objects. Coincidence is defined to exist if all locations on the Solid are fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location on this Solid is not enclosed by the other object it is considered to be not coincident with the object.Note that this Solid does not need to fill the entire space associated with the other object to be coincident - it need only occupy a subset of the space of the other object to be considered coincident. Cell and Solid. All other entity types will be silently ignored. Solid must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices, Points, Edges, Curves, Faces, Surfaces, Cells and Solids that are coincident with this Solid, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Solid. Valid entity types for target include Solid, Cell, Surface, Face, Curve, Edge, Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Solid.

Returns: entities coincident with Solid

When possible the method will return only the "highest topology" objects that are coincident with this Solid. For example, if an entire Solid is coincident with this Solid only the Solid will be returned and its constituent Cells, Faces, Edges and Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Solid the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Solid. Coincidence is defined to exist if all locations on an object are fully enclosed by this Solid. A location is said to be enclosed by the Solid if the shortest distance between it and this Solid is less than the specified tolerance. If any location on the object is not enclosed by this Solid, the object is considered to be not coincident with this Solid.Note that an object does not need to fill the entire space associated with this Solid to be considered coincident - it need only occupy a subset of the space of this Solid to be considered coincident.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices, Points, Edges, Curves, Faces, Surfaces, Cells and Solids in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Solid, all locations on the object must lie within this distance of this Solid.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getCells(ids: str = "") -> apex.geometry.CellCollection`
get the cells for the specified ids.

- `ids` — the ids of cells. If ids is empty, return all cells under the body

Returns: the collection of cells

#### `getCentroid() -> apex.Coordinate`
The location of the centroid of the Solid.

Returns: the solid centroid location

#### `getExteriorEdges() -> EdgeCollection`
get the exterior Edges on this solid.

Returns: collection of Edges

#### `getExteriorFaces() -> FaceCollection`
get the exterior Faces on this solid.

Returns: collection of Faces

#### `getExteriorVertices() -> VertexCollection`
get the exterior Vertices on this solid.

Returns: collection of Vertices

#### `getInteriorEdges() -> EdgeCollection`
get the interior Edges on this solid.

Returns: collection of Edges

#### `getInteriorFaces() -> FaceCollection`
get the interior Faces on this solid.

Returns: collection of Faces

#### `getInteriorVertices() -> VertexCollection`
get the interior Vertices on this solid.

Returns: collection of Vertices

#### `getLocation() -> apex.Coordinate`
The location of this geometry Solid in 3D cartesian space as an apex.ILocation.

Returns: the Solid location

The location of a geometry Solid is defined to be at the centroid of the solid

#### `getMassCenterNominal() -> apex.Coordinate`
get the center of mass on this solid as an apex.Coordinate object.

Returns: the mass center of the Solid

The center of mass is a spatial location and will be returned using the units of Length that is defined in the active scripting unit system.The center of mass is calculated assuming a constant distribution of density throughout the Solid and is therefore independent of the actual density value.

#### `getMassNominal(density: float = 1.0) -> float`
get the nominal mass on this solid.

- `density` — The density of the Solid.

Returns: the mass nominal of the Solid

This method returns a value that represents a Mass quantity and uses the unit of Mass that is defined in the active scripting unit system.The calculation of the mass of a solid requires both a density and a volume.The density may be supplied as an input argument and if omitted a value of 1.0 will be used.The volume is determined directly from the Solid.

#### `getMeshControlEdges() -> MeshControlEdgeCollection`
A read only meshControlEdgeCollection contain all MeshControlEdge composed by the Faces of this solid. If no MeshControlEdges are present in the Solid the method will return an empty collection.

Returns: collection of MeshControlEdge

#### `getOrientation() -> apex.Orientation`
the orientation of this Solid as an apex.IOrientation.

Returns: the Solid orientation

The orientation of a Solid is aligned with the axes of an orientated bounding box (OOBB) that encloses the Solid

#### `getPrincipalInertiaFrameNominal() -> apex.construct.CoordinateSystem`
get the principal inertia frame on this solid as a rectangular CoordinateSystem.

Returns: the principal inertia frame of the Solid

The location and orientation of the principal inertia frame is calculated using an assumption of a constant distribution of density throughout the volume of the Solid and is therefore independent of the actual density value.

#### `getPrincipalInertiaTensorNominal(density: float = 1.0) -> {str:float}`
get the nominal principal inertia tensor on this solid as a Dictionary.

- `density` — The density of the Solid.

Returns: the nominal principal inertia tensor of mass of the Solid

The returned Dictionary includes keys of type string and values of type float.The inertia tensor is returned using float values and uses the unit of Moment of Inertia (Mass x Length^2) that is defined in the active scripting unit system.The following keys represents the components of the inertia tensor - "ixx", "ixy", "ixz", "iyx", "iyy", "iyz", "izx", "izy", "izz".The calculation of the principal inertia tensor requires definition of the distribution of mass throughout the Solid and this is calculated based on the supplied "density" argument. A default density of "1.0" is supplied if this argument is omitted.

#### `getTessellationExterior() -> apex.display.Tessellation2D`
returns the exterior tessellation for this Solid as a Tesselation2D. The Tesselation2D includes the tessellation for all exterior Faces, Edges and Vertices in this Solid as triangles, lines and points and includes the association between each tessellation and the Face, Edge and Vertex of this Solid that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

#### `getTessellationInterior() -> apex.display.Tessellation2D`
returns the interior tessellation for this Solid as a Tesselation2D. The Tesselation2D includes the tessellation for all interior Faces, Edges and Vertices in this Solid as triangles, lines and points and includes the association between each tessellation and the Face, Edge and Vertex of this Solid that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

#### `getVolume() -> float`
get the volume of this solid.

Returns: the solid volume

- `identifyFeature() -> apex.geometry.ZResultSolidIdentifyFeature`
#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this Solid properties.

- `name` — of this Solid
- `parent` — of this Solid
- `color` — of this Solid
- `renderStyle` — of this Solid
- `enableTransparency` — of this Solid
- `transparencyLevel` — of this Solid

One or more parameters can be updated in one update call.


## `apex.geometry.SolidCollection`  (extends `GeometryBodyCollection`)
Iterable collection of Solids, based on EntityCollection.

Methods:

- `SolidCollection() -> None` — Construct a new SolidCollection.
#### `appendList(solidList: [apex.geometry.Solid]) -> None`
Add Solids from a list to the end of this collection.

- `solidList` — list of Solid objects to add to the collection.

For example:


## `apex.geometry.Sphere`  (extends `Solid`)
Class representing a parametric sphere. The Sphere size is parameterized by a single radius property. The origin and directions of the sphere axes can be defined using either a location and orientation or an external coordinate system. The origin of the Sphere is defined to be at the sphere center.
Properties: `coordinateSystem`, `origin`, `radius`

Methods:

#### `getCoordinateSystem() -> apex.construct.CoordinateSystem`
A CoordinateSystem that defines the origin and orientation of the Sphere. If the Sphere was created using an integrated Orientation this coordinateSystem will not exist and will return a None type.

Returns: the Sphere coordinateSystem

#### `getOrigin() -> ILocation`
the origin of the Sphere as an ILocation.

Returns: the Sphere origin

#### `getRadius() -> float`
The radius of the Sphere. radius represents an Length quantity and must be supplied in the units of Angle that are active in the script unit system.

Returns: the Sphere length

- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
#### `setCoordinateSystem(coordinateSystem: apex.construct.CoordinateSystem) -> None`
Set the coordinateSystem of this Sphere.

- `coordinateSystem` — A CoordinateSystem that defines the origin and orientation of the Sphere.

#### `setDescription(description: str) -> None`
Set the description of this Sphere.

- `description` — The description of the Sphere

#### `setName(name: str) -> None`
Set the name of this Sphere.

- `name` — The name of the Sphere

#### `setOrientation(orientation: apex.IOrientation) -> None`
Set the orientation of this Sphere.

- `orientation` — The orientation of the Sphere as an IOrientation.

#### `setOrigin(origin: ILocation) -> None`
Set the origin of this Sphere.

- `origin` — the origin of the Sphere as an ILocation.

#### `setRadius(radius: float) -> None`
Set the radius of this Sphere.

- `radius` — The radius of the Sphere. radius represents an Length quantity and must be supplied in the units of Angle that are active in the script unit system

#### `update(name: str = "", description: str = "", radius: float = 0.0, origin: apex.ILocation = None, orientation: apex.IOrientation = None, coordinateSystem: apex.construct.CoordinateSystem = None, parent: Entity = 0, color: [int] = [], renderStyle: apex.session.DisplayRenderStyle = apex.session.DisplayRenderStyle.Undefined, enableTransparency: apex.ApexBool = ApexBoolUndefined, transparencyLevel: int = -1, useLocalValue: bool = True) -> None`
Updates the properties of this Sphere. All modifiable properties of the Sphere are supported as optional arguments and multiple properties may be updated in a single call. Any properties not included in the argument list are unchanged by this method.

- `name` — The name of this Sphere
- `description` — The description of this Sphere
- `radius` — The radius of this Sphere. radius represents an Angle quantity and must be supplied in the units of Angle that are active in the script unit system
- `origin` — The origin of this Sphere as an ILocation. origin and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `orientation` — The orientation of this Sphere as an IOrientation. orientation and coordinateSystem must not be included in the same update() method call otherwise the method will throw an exception
- `coordinateSystem` — The CoordinateSystem that defines the origin and orientation of the Cylinder. If supplied, the location and orientation of the Cylinder will be updated based on the origin and orientation of this CoordinateSystem coordinateSystem an origin/orientation must not be included in the same update() method call otherwise the method will throw an exception
- `parent` — of this Sphere
- `color` — of this Sphere
- `renderStyle` — of this Sphere
- `enableTransparency` — of this Sphere
- `transparencyLevel` — of this Sphere
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.


## `apex.geometry.SphereCollection`  (extends `SolidCollection`)
Iterable collection of Solids, based on EntityCollection.

Methods:

- `SphereCollection() -> None`

## `apex.geometry.Surface`  (extends `GeometryBody`)
Surface Class Object. extends GeometryBody Class Object.
Properties: `area`, `centroid`, `cylindricalAxis`, `cylindricalAxisEndPoint`, `cylindricalAxisMidPoint`, `cylindricalAxisStartPoint`, `exteriorEdgeLoops`, `exteriorEdges`, `exteriorVertices`, `interiorEdgeLoops`, `interiorEdges`, `interiorVertices`, `isManifold`, `manifoldRegions`, `massCenterNominal`, `massNominal`, `meshControlEdges`, `parametricRange`, `principalInertiaFrameNominal`, `principalInertiaTensorNominal`, `tessellation`

Methods:

#### `evaluateClosestLocation(inputLocation: apex.ILocation) -> ZResultEvaluateClosestLocation`
Given an input location in 3D space, evaluates and returns a result object containing the location on this Surface that is closest to the input location and the vector from the input location to the closest Surface location.

- `inputLocation` — The target location in space for which the point of closest approach on the Surface is required.

Returns: Result object

#### `evaluateClosestLocationOnSurface(point: apex.ILocation) -> apex.Coordinate`
DEPRECATED: "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE " This method has been superseded by the equivalent "apex.geometry.surface.evaluateClosestLocation()" method.

- `point` — to find location

Returns: location point

evaluateClosestLocationOnSurface

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether all locations on this Surface lie within the specified tolerance of the input Faces, Surfaces, Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Surface is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Surface is coincident.If this Surface is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Surface is coincident with other objects. Coincidence is defined to exist if all locations on the Face is fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If any location on this Surface is not enclosed by the other object it is considered to be not coincident with the object.Note that this Surface does not need to fill the entire space associated with the other object to be coincident - it need only occupy a subset of the space of the other object to be considered coincident. Face, Surface, Cell and Solid. All other entity types will be silently ignored. Surface must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `evaluateOrientationSurfaceParametricCoordinate(u: float, v: float) -> apex.Orientation`
This method takes a 2D parametric coordinate (u, v) as input and returns the default Orientation at that position on the Surface.

- `u` — the 'u' component of the 2D parametric coordinate (u, v) that defines the location on the Surface where the orientation will be evaluated
- `v` — the 'v' component of the 2D parametric coordinate (u, v) that defines the location on the Surface where the orientation will be evaluated

Returns: Result object

For simple Surfaces, where all of the Faces in the Surface are represented by a single underlying Surface, this method will return the orientation at the parametric location (u) on the single underlying Surface.For more complex Surfaces, where the Faces in the Surfaces are represented by MULTIPLE underlying Surfaces, Apex will raise an exception.

#### `evaluatePointOnSurface(point: apex.ILocation) -> apex.geometry.ZResultEvaluatePointOnSurface`
This method takes a point in space (as a Point3D object) as input and returns a result object containing the closest point on the Surface as a ParametricCoordinate2D. Apex Surfaces compose one or more Faces and Faces are bounded by Edges. Each Face is actually a region of an underlying Surface defined by one or more trimming loops where the trimming loops are the Edges of the Face. Simple Surfaces may be represented by single or multiple Faces where all of the Faces are regions of the same underlying Surface. In more complex Surfaces, the Faces that make up the single Apex Surface may actually be regions of multiple different underlying Surfaces. The underlying Surfaces are not visible to the user - the Apex Surface manages the Faces and presents the collection of faces as a single Apex Surface with multiple Faces. Apex supports the concept of parametric locations on Surfaces and Faces. In both cases, the parametric location is actually the parametric location on the underlying Surface. For a single Face, or for a Surface that has just a single underling Surface, parametric coordinates are relatively straightforward. The range of each parametric coordinate (u, v) can be determined and the spatial coordinate (x, y, z) can be uniquely calculated for an given parametric location. Note that parametric locations outside of the parametric range of the Surface or Face do not map to spatial coordinates, and even some parametric coordinates that lie within the parametric coordinate range may not map to real spatial coordinates - consider example a Face or Surface with a hole, or that is irregular in shape. AND the ID of the underlying Surface. See the below text for further explanation of the underlying Surface. It should be noted that the parametric location that is returned by this method is actually the parametric location of the input point on the underlying Surface. In current versions of Apex, this method only supports simple Apex Surfaces (as defined above) and the method will throw an exception if the Apex Surface is complex. A future release of Apex will extend this method to support complex Surfaces as follows: For Apex Surfaces that are represented by multiple underlying Surfaces, a series of evaluations using this method, each with different input spatial locations, will each return a single parametric location, however those parametric locations may be based on different underlying Surfaces. If you will be using this method to evaluate relative locations of objects based on the magnitude of a parametric location, you will be advised to check that the parametric locations you are comparing are based on the same underlying Surface, otherwise you may experience unexpected outcomes. For this reason, in a future Apex version, the method will return both the ID of the underlying Surface AND the parametric location. The underlying Surface cannot be accessed using the scripting API and the ID that is returned should only be used for comparison with ID's from other underlying Surfaces.

- `point` — a point in space (as a Point3D object)

Returns: Result object

#### `evaluateSurfaceNormal(location: apex.ILocation) -> apex.construct.Vector3D`
evaluateSurfaceNormal

- `location` — to find normal

Returns: normal vector

#### `evaluateSurfaceParametricCoordinate(u: float, v: float) -> apex.geometry.ZResultEvaluateSurfaceParametricCoordinate`
This method takes a parametric Surface coordinate (u, v) as input and returns the equivalent 3D cartesian coordinates as a List of Point3D objects. For simple Surfaces where all of the Faces in the Surface are represented by a single underlying Surface, this method will return a List containing a single Point3D object based on evaluation of the parametric location (u, v) on the single underlying Surface. For more complex Surfaces, where the Faces in the Surface are represented by multiple underlying Surfaces, Apex will currently throw an exception. Future releases of Apex will extend this method as follows: The method will return one Point3D object per underlying Surface - strictly one point for each underlying Surface for which the input parametric coordinate is valid. Each Point3D location that is returned will have an accompanying "underlying surface ID" that represents the ID of the Underlying Surface. This ID will not be used to access the underlying Surface but will be intended to help users understand which coordinates can be reasonably compared - comparing parametric coordinates that are extracted from different underlying surfaces should be performed with caution.

- `u` — The value of the parametric "u" coordinate
- `v` — The value of the parametric "v" coordinate

Returns: Result object

#### `evaluateTangentInDirection(location: apex.ILocation, direction: apex.construct.Vector3D) -> apex.construct.Vector3D`
evaluateTangentInDirection

- `location` — to find tangent
- `direction` — to find tangent

Returns: tangent vector

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices, Points, Edges, Curves, Faces and Surfaces that are coincident with this Surface, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Surface. Valid entity types for target include Surface, Face, Curve, Edge, Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Surface.

Returns: entities coincident with Surface

If no entities are coincident with this Surface the method will return an empty EntityCollection.When possible the method will return only the "highest topology" objects that are coincident with this Surface. For example, if an entire Surface is coincident with this Surface only the Surface will be returned and its constituent Faces, Edges and Vertices will be omitted, even though they are coincident by definition.This method is designed to find all objects that are coincident with this Surface. Coincidence is defined to exist if all locations on an object are fully enclosed by this Surface. A location is said to be enclosed by the Surface if the shortest distance between it and this Surface is less than the specified tolerance. If any location on the object is not enclosed by this Surface, the object is considered to be not coincident with this Surface.Note that an object does not need to fill the entire space associated with this Surface to be considered coincident - it need only occupy a subset of the space of this Surface to be considered coincident.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices, Points, Edges, Curves, Faces and Surfaces in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Surface, all locations on the object must lie within this distance of this Surface.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `findFaceAtPoint(pointOnSurface: apex.ILocation) -> Face`
findFaceAtPoint

- `pointOnSurface` — to find face

Returns: Face

#### `getArea() -> float`
get the area of this surface.

Returns: the surface area

#### `getCentroid() -> apex.Coordinate`
The location of the centroid of the Surface.

Returns: the surface centroid location

#### `getCylindricalAxis() -> apex.construct.Vector3D`
return the cylindrical axis of this Surface. An cylindricalAxis will be calculated for all Surface, even if the Surface is not a true cylinder or partial cylinder

Returns: the axis direction of this Surface

#### `getCylindricalAxisEndPoint() -> apex.Coordinate`
return the end point of the cylindrical axis of this Surface. A cylindricalAxisEndPoint will be calculated for all Surfaces, even if the Surface is not a true cylinder or partial cylinder

Returns: the end point of the cylindrical axis of this Surface

#### `getCylindricalAxisMidPoint() -> apex.Coordinate`
return the mid point of the cylindrical axis of this Surface. A cylindricalAxisMidPoint will be calculated for all Surfaces, even if the Surface is not a true cylinder or partial cylinder

Returns: the mid point of the cylindrical axis of this Surface

#### `getCylindricalAxisStartPoint() -> apex.Coordinate`
return the start point of the cylindrical axis of this Surface. A cylindricalAxisStartPoint will be calculated for all Surfaces, even if the Surface is not a true cylinder or partial cylinder

Returns: the start point of the cylindrical axis of this Surface

#### `getExteriorEdgeLoops() -> EdgeLoopCollection`
Returns the bounding EdgeLoops of this Surface.

Returns: exterior EdgeLoopCollection

If the Surface is non-manifold this method will throw an exception - check if the Surface is manifold before calling this method.

#### `getExteriorEdges() -> EdgeCollection`
get the exterior Edges on this surface.

Returns: collection of Edges

- `getExteriorIds(ids: SCA.SCAInt32Sequence) -> None`
#### `getExteriorVertices() -> VertexCollection`
get the exterior Vertices on this surface.

Returns: collection of Vertices

#### `getInteriorEdgeLoops() -> EdgeLoopCollection`
Returns all interior EdgeLoops that may exist for this Surface.

Returns: interior EdgeLoopCollection

#### `getInteriorEdges() -> EdgeCollection`
get the interior Edges on this surface.

Returns: collection of Edges

- `getInteriorIds(ids: SCA.SCAInt32Sequence) -> None`
#### `getInteriorVertices() -> VertexCollection`
get the interior Vertices on this surface.

Returns: collection of Vertices

#### `getIsManifold() -> bool`
A Boolean value that indicates whether this Surface is manifold or not.

Returns: if is manifold

#### `getLocation() -> apex.Coordinate`
The location of this Surface in 3D cartesian space as an apex.ILocation.

Returns: the Surface location

The location of a geometry Surface is defined to be at the centroid of the Surface.

#### `getManifoldRegions() -> [FaceCollection]`
Returns a List of FaceCollections.

Returns: contiguous manifold regions

Each FaceCollection in the List contains a set of one or more cotiguous Faces. Each set of Faces represents one manifold region from the Surface.

#### `getMassCenterNominal() -> apex.Coordinate`
get the center of mass on this surface as an apex.Coordinate object.

Returns: the mass center of the Surface

The center of mass is a spatial location and will be returned using the units of Length that is defined in the active scripting unit system.The center of mass is calculated assuming a constant distribution of density throughout the Surface and is therefore independent of the actual density value.

#### `getMassNominal(density: float = 1.0) -> float`
get the nominal mass on this surface.

- `density` — The density of the Surface.

Returns: the mass nominal of the Surface

This method returns a value that represents a Mass quantity and uses the unit of Mass that is defined in the active scripting unit system.The calculation of the mass of a surface requires both a density and an area.The density may be supplied as an input argument and if omitted a value of 1.0 will be used.The area is determined directly from the Surface.

#### `getMeshControlEdges() -> MeshControlEdgeCollection`
A read only meshControlEdgeCollection contain all MeshControlEdge composed by the Faces of this surface. If no MeshControlEdges are present in the Surface the method will return an empty collection.

Returns: collection of MeshControlEdge

#### `getOrientation() -> apex.Orientation`
the orientation of this Surface as an apex.IOrientation.

Returns: the Surface orientation

The orientation of a Surface is calculated as follows,The x axis of the Surface orientation is parallel to the positive u direction of the Surface at the Surface centroidThe z axis of the Surafce orientation is perpendicular to the Surface at the Surface centroid and aligned with the Surface outward normal at that locationThe y axis of the Surface orientation is perpendicular to the x and z axes following the right hand rule

#### `getParametricRange() -> {str:float}`
The range of the parametric space coordinates used by the Surface, Apex Surfaces compose one or more Faces bounded by Edges. Each Face is actually a region of an underlying Surface defined by one or more trimming loops where the trimming loops are the Edges of the Face. Simple Surfaces may be represented by single or multiple Faces where all of the Faces are regions of the same underlying Surface. In more complex Surfaces, the Faces that make up the single Apex Surface may actually be regions of multiple different underlying Surfaces. The underlying Surfaces are not visible to the user - the Apex Surface manages the Faces and presents the collection of faces as a single Apex Surface with multiple Faces. Apex supports the concept of parametric locations on Surfaces and Faces. In both cases the parametric location is actually the parametric location of the underlying Surface. For a single Face, or for a Surface that has just a single underling Surface, parametric coordinate ranges are relatively straightforward. The range of each parametric coordinate (u, v) can be determined from the single, trimmed underlying Surface. For Apex Surfaces that are defined by multiple underlying Surfaces, multiple parametric ranges exist and this attribute represents the maximum and minimum parametric coordinates across all of the trimmed underlying Surfaces - so the individual uStart, uEnd,, vStart and vEnd values returned here may occur on different underlying Surfaces.

Returns: parametric range

#### `getPrincipalInertiaFrameNominal() -> apex.construct.CoordinateSystem`
get the principal inertia frame on this surface as a rectangular CoordinateSystem.

Returns: the principal inertia frame of the Surface

The location and orientation of the principal inertia frame is calculated using an assumption of a constant distribution of density throughout the area of the Surface and is therefore independent of the actual density value.

#### `getPrincipalInertiaTensorNominal(density: float = 1.0) -> {str:float}`
get the nominal principal inertia tensor on this surface as a Dictionary.

- `density` — The density of the Surface.

Returns: the nominal principal inertia tensor of mass of the Surface

The returned Dictionary includes keys of type string and values of type float.The inertia tensor is returned using float values and uses the unit of Moment of Inertia (Mass x Length^2) that is defined in the active scripting unit system.The following keys represents the components of the inertia tensor - "ixx", "ixy", "ixz", "iyx", "iyy", "iyz", "izx", "izy", "izz".The calculation of the principal inertia tensor requires definition of the distribution of mass throughout the Surface and this is calculated based on the supplied "density" argument. A default density of "1.0" is supplied if this argument is omitted.

#### `getTessellation() -> apex.display.Tessellation2D`
returns the tessellation for this Surface as a Tesselation2D. The Tesselation2D includes the tessellation for all Faces, Edges and Vertices in this Surface as triangles, lines and points and includes the association between each tessellation and the Face, Edge and Vertex of this Surface that it represents. The tessellation does not include suppressed Edges or Vertices. The tessellation is extracted from the displayed geometry and is based on the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation

Returns: Tessellation

- `getType() -> str`
- `identifyFeature(: None) -> [apex.geometry.GeometryFeature]`
#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this Surface properties.

- `name` — of this Surface
- `parent` — of this Surface
- `color` — of this Surface
- `renderStyle` — of this Surface
- `enableTransparency` — of this Surface
- `transparencyLevel` — of this Surface

One or more parameters can be updated in one update call.


## `apex.geometry.SurfaceCollection`  (extends `GeometryBodyCollection`)
Iterable collection of Surfaces, based on EntityCollection.

Methods:

- `SurfaceCollection() -> None` — Construct a new SurfaceCollection.
#### `appendList(surfaceList: [apex.geometry.Surface]) -> None`
Add Surfaces from a list to the end of this collection.

- `surfaceList` — list of Surface objects to add to the collection.

For example:


## `apex.geometry.Vertex`  (extends `GeometryTopology`)
Vertex Class Object. extends GeometryTopology Class Object.
Properties: `axisAlignedBoundingBox`, `connectedCells`, `connectedEdges`, `connectedFaces`, `tessellation`

Methods:

#### `evaluateCoincidence(target: EntityCollection, tolerance: float = 0.001) -> EntityCollection`
Evaluates whether this Vertex within the specified tolerance of the input Vertices, Points, Edges, Curves, Faces, Surfaces, Cells or Solids.

- `target` — The entities that will be evaluated for coincidence as an EntityCollection.
- `tolerance` — The tolerance that will be used to determine if the Vertex is coincident with the input entities.

Returns: coincident entities

Returns an EntityCollection containing the subset of the input entities with which this Vertex is coincident.If this Vertex is not coincident with any of the input entities the method will return an empty EntityCollection.This method is designed to determine if this Vertex is coincident with other objects. Coincidence is defined to exist if the location of the Vertex is fully enclosed by the other object. A location is said to be enclosed by the other object if the shortest distance between it and the other object is less than the specified tolerance. If the location of this Vertex is not enclosed by the other object this Vertex is considered to be not coincident with the object. Vertex, Point, Edge, Curve, Face, Surface, Cell and Solid. All other entity types will be silently ignored. Vertex must lie within this distance of the input entity.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `findCoincidentObjects(target: EntityCollection = EntityCollection(), tolerance: float = 0.001) -> EntityCollection`
Finds all Vertices and Points that are coincident with this Vertex, within the supplied tolerance, and returns them in an EntityCollection.

- `target` — An optional collection of entities that will be checked for coincidence with this Vertex. Valid entity types for target include Point and Vertex - all other entity types will be silently ignored.
- `tolerance` — The tolerance that will be used to determine if an object is coincident with this Vertex.

Returns: entities coincident with Vertex

When possible the method will return only the "highest topology" objects that are coincident with this Vertex. For example, if an entire Point is coincident with this Vertex only the Point will be returned and its constituent Vertices will be omitted, even though they are coincident by definition.If no entities are coincident with this Vertex the method will return an empty EntityCollection.This method is designed to find all objects that are coincident with this Vertex. Coincidence is defined to exist if the distance between the object and this vertex is less than or equal to the supplied tolerance.Note - although this method has been implemented to be highly performant, the performance is dependent on the number of Vertices and Points in the Model and for large models the computational cost and elapsed time may be significant.To improve performance use the optional target argument to supply an explicit collection of objects to check. Performance of this method is proportional to the number of objects that will be checked for coincidence so when possible it is recommended to provide this collection. Vertex, all locations on the object must lie within this distance of this Vertex.tolerance is a length quantity and must be defined using the units of Length defined by the active ScriptUnitSystem.

#### `getConnectedCells() -> apex.geometry.CellCollection`
get the connected Cells on this vertex.

Returns: collection of Cells

#### `getConnectedEdges() -> apex.geometry.EdgeCollection`
get the connected Edge on this vertex.

Returns: collection of edges

#### `getConnectedFaces() -> apex.geometry.FaceCollection`
get the connected Faces on this vertex.

Returns: collection of Faces

#### `getLocation() -> apex.Coordinate`
The the location of the Vertex in global cartesian space as an apex.ILocation.

Returns: the Vertex location

#### `getOrientation() -> apex.Orientation`
the orientation of this Vertex as an apex.IOrientation

Returns: the Vertex orientation

The orientation of a Vertex is calculated using one of the following methods depending upon the configuration of this VertexVertex associated with a Single Edge of a CurveThe Orientation x axis is Tangent to the Edge at the Vertex location. The positive edge tangent runs in the direction of increasing parametric value - from low to high uThe Orientation z axis is defined using the Binormal of the Edge at the Vertex which is guaranteed to be perpendicular to the x axis.The Orientation y axis is perpendicular to the above two axes using the right hand ruleVertex associated with multiple Curve EdgesThe Orientation x axis is tangent to the longest Edge connected to the Vertex at the Vertex location. The positive edge tangent runs in the direction of increasing parametric value - from low to high uThe Orientation z axis is defined using the Binormal of the longest Edge at the Vertex which is perpendicular to be perpendicular to the x axisThe Orientation y axis is perpendicular to the above two axes using the right hand ruleVertex associated with a single FaceThe Orientation x axis is tangent to the longest Edge of the Facet the Vertex (Option 1: Use the longest Edge, from low to high parametric direction; Option 2: User Gesture to define which Edge to use), andThe Orientation z axis is perpendicular to the Face at the Vertex. The positive perpendicular runs in the direction of the Face outward normal at the Vertex locationVertex associated with multiple FacesThe Orientation x axis is tangent to the longest Edge to which it is connected. The positive edge tangent runs in the direction of increasing parametric value - from low to high uThe Orientation z axis is perpendicular to the largest Face to which it is connected. The positive perpendicular runs in the direction of the Face outward normal at the Vertex locationThe Orientation y axis is perpendicular to the above two axes using the right hand rule

#### `getTessellation() -> apex.display.Tessellation0D`
returns the tessellation for this Vertex as a Tesselation0D. The Tesselation0D includes the tessellation for this Vertex as a point. Point tessellation is not impacted by the geometry tessellation tolerances and settings in Application Settings/Tolerances/Tessellation.

Returns: Tessellation


## `apex.geometry.VertexCollection`  (extends `GeometryTopologyCollection`)
Iterable collection of Vertexs, based on EntityCollection.

Methods:

- `VertexCollection() -> None` — Construct a new VertexCollection.
#### `appendList(vertexList: [apex.geometry.Vertex]) -> None`
Add Verticies from a list to the end of this collection.

- `vertexList` — list of Vertex objects to add to the collection.

For example:


## `apex.geometry.ZResultDefeature`
Properties: `modifiedGeometryBodies`, `notRemovedFeatures`, `numFeaturesRemoved`, `seedPointIds`

Methods:

#### `getModifiedGeometryBodies(: None) -> [apex.geometry.GeometryBody]`
getModifiedGeometryBodies return the list of modified bodies

Returns: the list of modified bodies

#### `getNotRemovedFeatures(: None) -> GeometryFeatureListType`
getNotRemovedFeatures return the list of features not removed

Returns: the list of not removed features.

#### `getNumFeaturesRemoved(: None) -> int`
getNumFeaturesRemoved return the number of removed features

Returns: the number of removed features

#### `getSeedPointIds(: None) -> SCA.SCAInt32Sequence`
getSeedPointIds return the list of seed point Id

Returns: the list of seed point Id

#### `getSeedPoints(seedPointIds: SCA.SCAInt32Sequence) -> apex.mesh.SeedPointCollection`
getSeedPoints return the list of seed point

Returns: the list of seed point


## `apex.geometry.ZResultDefeatureCustomFeature`
Properties: `edgesOfFeatures`, `numberOfFeaturesFound`

Methods:

#### `getEdgesOfFeatures(: None) -> [EdgeListType]`
return list of edge lists. Each list are the edges of the feature. Each list will be the same length of edges

Returns: list of edge lists

#### `getNumberOfFeaturesFound(: None) -> int`
return the number of features found.

Returns: the number of features found


## `apex.geometry.ZResultEvaluateClosestLocation`
This ResultObject contains,.
Properties: `closestLocation`, `vector`

Methods:

- `getClosestLocation(: None) -> apex.ILocation` — The location that lies directly on the target object that is closest to the input location.
- `getVector(: None) -> apex.construct.Vector3D` — The vector in global Cartesian space that runs between the input location and the point on the target entity that is closest to that input location.

## `apex.geometry.ZResultEvaluateClosestLocationOnFace`
Instances of this class are returned by the evaluateClosestLocationOnFace () method of the Face class.
Properties: `distance`, `u`, `v`, `vector`

Methods:

- `ZResultEvaluateClosestLocationOnFace() -> None`
- `getDistance(: None) -> float` — The distance between the input Point and the location on the Face that is closest to it.
- `getU(: None) -> float` — The distance between the input Point and the location on the Face that is closest to it.
- `getV(: None) -> float` — The distance between the input Point and the location on the Face that is closest to it.
- `getVector(: None) -> apex.construct.Vector3D` — A vector, in global Cartesian space, that defines the location of the closest point on the Face relative to the input Point.

## `apex.geometry.ZResultEvaluateCurveParametricCoordinate`
Result object for the Curve.evaluateCurveParametricCoordinate() method. Simple Apex Curves may have one or more Edges and be supported by a single underlying Curve. In this case, the single underlying Curve will be used to evaluate the input parametric coordinate and a single location in 3D space will be returned as a Point3D in the 'points' property of this result object. For more complex Apex Curves, multiple underlying Curves may exist and in current releases of Apex this will cause the method to throw an exception. In a future Apex release, the parametric coordinate will be evaluated using each underlying Curve and one location in 3D space will be returned for each underlying Curve. If the input parametric coordinate is outside of the parametric range of any underlying Curve, no 3D space location will be calculated. This result object provides access to a List of locations that evaluate from the input parametric coordinates and a corresponding List of Curve ID's representing the ID of the underlying Curve from which the corresponding location was evaluated. Underlying Curves are not accessible to Apex and the Curve ID is intended to be used only to compare with other Curve ID's within the same Apex Curve.
Properties: `points`

Methods:

- `getPoints() -> apex.ILocationCollection` — The location(s) in 3D Space of the input Curve parametric coordinates as a List of apex.construct.Point3D. For simple Curves with a single underlying Curve the List will contain a single Point3D corresponding to the input parametric coordinates. For more complex Curves that have multiple underlying Curves, the parametric coordinate is evaluated on each underlying Curve and, if the parametric coordinate exists on the underlying Curve, a Point3D will be returned. The IDs of the underlying Curves that were used to generate these Point3D's are available in the "curveIDs" List.

## `apex.geometry.ZResultEvaluateFaceCurvature`
Instances of this class are returned by the evaluateFaceCurvatureUV () method of the Face class.
Properties: `curvature1`, `curvature2`, `normal`, `principal1`, `principal2`

Methods:

- `ZResultEvaluateFaceCurvature() -> None`
- `getCurvature1(: None) -> float` — Curvature in the principal 1 direction at point UV.
- `getCurvature2(: None) -> float` — Curvature in the principal 2 direction at point UV.
- `getNormal(: None) -> apex.construct.Vector3D` — A unit vector that defines normal at point UV.
- `getPrincipal1(: None) -> apex.construct.Vector3D` — A unit vector that defines principal 1 direction of curvature at point UV.
- `getPrincipal2(: None) -> apex.construct.Vector3D` — A unit vector that defines principal 2 direction of curvature at point UV.

## `apex.geometry.ZResultEvaluateFaceTangent`
Instances of this class are returned by the evaluateFaceTangentUV () method of the Face class.
Properties: `uTangent`, `vTangent`

Methods:

- `ZResultEvaluateFaceTangent() -> None`
- `getuTangent(: None) -> apex.construct.Vector3D` — A vector that defines the tangent to the Face at the input location in a direction parallel to the local Face parametric U direction.
- `getvTangent(: None) -> apex.construct.Vector3D` — A vector that defines the tangent to the Face at the input location in a direction parallel to the local Face parametric V direction.

## `apex.geometry.ZResultEvaluatePointOnCurve`
A result object that holds the Curve parametric coordinate associated with the input location. For simple Curve with a single underlying Curve the input location will be evaluated against the single underlying Curve and the parametric coordinates of the location on that Curve will be returned. No matter what valid location is provided, the parametric coordinates will always be evaluated using the same single underlying Curve For more complex Curves that have multiple underlying Curves, the same basic approach defined for simple Curves is used, but in this case, the parametric coordinates that are returned may be based on different underlying Curves depending on the actual input location. Comparing parametric coordinates for purposes of sorting etc. is only valid if the parametric coordinates derive form the same underlying Curve. In a future release of Apex, this result object will provide access to both the parametric Curve coordinate associated with the input point AND the ID of the underlying Curve from which it is derived. The underlying Curves will not be accessible to users and the provided ID is designed only to be used for comparison with other underlying Curve ID's from the same Apex Curve In the current release of Apex this method will throw an exception if the Apex Curve relies on more than a single underlying Curve.
Properties: `parametricCoordinates`

Methods:

- `getParametricCoordinates() -> [float]` — The parametric coordinates of input point as a floating point value representing the parametric location on the Curve. Note that this coordinate is extracted from underlying Curves of the Apex Curve that is being evaluated. If the Apex Curve is composed of multiple underlying Curves a location on the Apex Curve will map to just one of them and different Apex Curve locations may map to different underlying Curves. A future release of Apex will return the ID of the underlying Curve in this result object alongside the parametric coordinate - this will enable users to validate whether two parametric coordinates returned from different Apex Curve locations are derived from the same underlying Curve or not and use this information to determine whether comparison is meaningful.

## `apex.geometry.ZResultEvaluatePointOnFace`
Instances of this class are returned by the evaluatePointOnFace () method of the Face class.
Properties: `u`, `v`

Methods:

- `ZResultEvaluatePointOnFace() -> None`
- `getU(: None) -> float` — The distance between the input Point and the location on the Face that is closest to it.
- `getV(: None) -> float` — The distance between the input Point and the location on the Face that is closest to it.

## `apex.geometry.ZResultEvaluatePointOnSurface`
A result object that holds the Surface parametric coordinate associated with the input location. For simple Surfaces with a single underlying Surface the input location will be evaluated against the single underlying Surface and the parametric coordinates of the location on that Surface will be returned. No matter what valid location is provided, the parametric coordinates will always be evaluated using the same single underlying Surface For more complex Surfaces that have multiple underlying Surfaces, the same basic approach defined for simple Surfaces is used, but in this case, the parametric coordinates that are returned may be based on different underlying Surfaces depending on the actual input location. Comparing parametric coordinates for purposes of sorting etc. is only valid if the parametric coordinates derive form the same underlying Surface. In a future release of Apex, this result object will provide access to both the parametric surface coordinate associated with the input point AND the ID of the underlying Surface from which it is derived. The underlying Surfaces will not be accessible to users and the provided ID is designed only to be used for comparison with other underlying Surface ID's from the same Apex Surface In the current release of Apex this method will throw an exception if the Apex Surface relies on more than a single underlying Surface.
Properties: `parametricCoordinates`

Methods:

- `getParametricCoordinates() -> [apex.construct.ParametricCoordinate2D]` — The parametric coordinates of input point as an apex.construct.ParametricCoordinate2D. Note that this coordinate is extracted from underlying Surfaces of the Apex Surface that is being evaluated. If the Apex Surface is composed of multiple underlying Surfaces a location on the Apex Surface will map to just one of them and different Apex Surface locations may map to different underlying Surfaces. A future release of Apex will return the ID of the underlying surface in this result object alongside the parametric coordinate - this will enable users to validate whether two parametric coordinates returned from different Apex Surface locations are derived from the same underlying Surface or not and use this information to determine whether comparison is meaningful.

## `apex.geometry.ZResultEvaluateSurfaceParametricCoordinate`
Result object for the Surface.evaluateSurfaceParametricCoordinate() method. Simple Apex Surfaces may have one or more Faces and be supported by a single underlying Surface. In this case, the single underlying Surface will be used to evaluate the input parametric coordinate and a single location in 3D space will be returned as a single Point3D object in the "points" List For more complex Apex Surfaces, multiple underlying Surfaces may exist and in this case current Apex releases will throw an exception. A future release of Apex will support evaluation of surface parametric coordinates on complex Surfaces by evaluating the input parametric coordinate using each underlying Surface and returning one location in 3D space for each underlying Surface. (If the input parametric coordinate is outside of the parametric range of any underlying Surface, no 3D space location will be calculated.) In a future Apex release this result object provide access not only to the single Point3D associated with a valid Surface parametric coordinate, but to a List of locations that evaluate from the input parametric coordinates and a corresponding List of Surface ID's representing the ID of the underlying Surface from which the corresponding location was evaluated. Underlying Surfaces will not be accessible to Apex and the Surface ID is intended to be used only to compare with other Surface ID's within the same Apex Surface.
Properties: `points`

Methods:

- `getPoints() -> apex.ILocationCollection` — The location(s) in 3D Space of the input Surface parametric coordinate as a List of apex.construct.Point3D. For simple Surfaces with a single underlying Surface the List will contain a single Point3D corresponding to the input parametric coordinates. A future release of Apex will support complex Surfaces that have multiple underlying Surfaces, the parametric coordinate will be evaluated on each underlying Surfaces and, if the parametric coordinate exists on the underlying Surface, a Point3D will be returned. The IDs of the underlying Surfaces that were used to generate these Point3D's will be available in this result object.

## `apex.geometry.ZResultFindGeometryFaults`
Properties: `faults`, `faultTypes`, `numGeometryFaults`

Methods:

#### `getFaultTypes(: None) -> [apex.geometry.GeometryFaultType]`
return a list of fault types of the faults matching Faults[0]

Returns: a list of fault types of the faults matching Faults[0]

#### `getFaults(: None) -> [EntityListType]`
return Tuples containing Topology, GeometryBody and Parts of faults that were found.

Returns: Tuples containing Topology, GeometryBody and Parts of faults that were found.

#### `getNumGeometryFaults(: None) -> int`
return Total number of geometry faults found

Returns: Total number of geometry faults found


## `apex.geometry.ZResultFindSmallSurfaceFeatures`
Properties: `numSmallFeaturesIdentified`, `smallFeatures`

Methods:

#### `getNumSmallFeaturesIdentified(: None) -> int`
return Total number of small features identified

Returns: Total number of small features identified

#### `getSmallFeatures(: None) -> [EntityListType]`
return Dictionaries containing Topology, GeometryBody and Parts of the small features that were found.

Returns: List of Dictionaries containing information about the small features that were found.


## `apex.geometry.ZResultGeometrySimplify`
Properties: `notSimplifiedGeometries`, `simplifiedGeometries`

Methods:

#### `getNotSimplifiedGeometries(: None) -> EntityListType`
return the list of Not Simplified Geometries

Returns: the list of Not Simplified Geometries.

#### `getSimplifiedGeometries(: None) -> EntityListType`
return the list of Simplified Geometries

Returns: the list of Simplified Geometries


## `apex.geometry.ZResultIdentifyCustomFeature`
Properties: `edgesOfFeatures`, `numberOfFeaturesFound`

Methods:

#### `getEdgesOfFeatures(: None) -> [EdgeCollection]`
return list of edge lists. Each list are the edges of the feature. Each list will be the same length of edges

Returns: list of edge lists

#### `getNumberOfFeaturesFound(: None) -> int`
return the number of features found.

Returns: the number of features found


## `apex.geometry.ZResultIdentifyFeature`
Properties: `featureDimensions`, `featuresIdentified`

Methods:

#### `getFeatureDimensions(: None) -> [float]`
return a list of the featureDimensions

Returns: list of the featureDimensions

#### `getFeaturesIdentified(: None) -> apex.geometry.GeometryFeatureCollection`
return the list of features identified

Returns: collection of features identified


## `apex.geometry.ZResultIdentifyFixSmallFeatures`
Properties: `numFeaturesFixed`, `numFeaturesIdentified`, `smallFeatures`

Methods:

#### `getNumFeaturesFixed(: None) -> int`
return Total number of small features that were changed by AutoFix.This will be 0 if AutoFix is FALSE

Returns: Total number of small features that were changed by AutoFix.This will be 0 if AutoFix is FALSE

#### `getNumFeaturesIdentified(: None) -> int`
return Total number of small features identified

Returns: Total number of small features identified

#### `getSmallFeatures(: None) -> [EntityListType]`
return Dictionaries containing information about the small features that were found.Features that were succesfully fixed are not included in this list Each Ditionary contains

Returns: List of Dictionaries containing information about the small features that were found.


## `apex.geometry.ZResultSolidIdentifyFeature`
Properties: `featuresIdentified`

Methods:

#### `getFeaturesIdentified(: None) -> [GeometryFeatureDictionaryType]`
return the features identified

Returns: the features identified


## `apex.geometry.ZResultSplitCurvesWithEntities`
a ResultObject containing a collection all of the new Edges that were created by the split method
Properties: `newEdges`

Methods:

#### `getNewEdges(: None) -> apex.geometry.EdgeCollection`
return an EdgeCollection containing all of the new Edges that were introduced by the split operation.

Returns: the new edges

When an Edge is split, the original edge is replaced by two (or more) new Edges. When a Curve is split, the Edge within the Curve where the split occurs will be replaced by two new Edges. The new Edges that are created by the split will be returned in this collection. The new edges may be accessed using the result attribute newEdges.


## `apex.geometry.ZResultSplitSurfacesWithEntities`
a ResultObject containing a collection of all of the new Faces that were created by the split method
Properties: `newFaces`

Methods:

#### `getNewFaces(: None) -> apex.geometry.FaceCollection`
return a FaceCollection containing all of the new Faces that were introduced by the split operation. When a Face is split, the original Face is replaced by two (or more) new Faces. The new Faces that are created by the split will be returned in this collection.

Returns: the new faces

The new faces may be accessed using the result attribute newFaces.


