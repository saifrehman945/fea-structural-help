# apex.display — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.display.Camera`
Properties: `directionOfProjection`, `distance`, `focalPoint`, `parallelScale`, `position`, `viewUp`

Methods:

#### `dolly(dollyValue: float) -> None`
Moves the camera closer to or away from the focal point.

- `dollyValue` — - a value to change the distance between the camera and the focal point by dividing the camera's distance from the focal point by the given dollyValue. Use a value greater than one to dolly-in toward the focal point, and use a value less than one to dolly-out away from the focal point.

- `getDirectionOfProjection() -> apex.construct.Vector3D` — Gets a direction vector from the camera position to the focal point as a Vector3D.
- `getDistance() -> float` — Gets the distance from this camera to the focal point.
- `getFocalPoint() -> apex.Coordinate` — Gets the focal point of the camera in global Cartesian coordinates. The coordinates of the focal point must be defined using the units of Length the from the active script unit system When focalPoint is returned from a Camera object. it is always returned as an apex.ILocation (which inherits ILocation). When setting the focalPoint on a Camera object any instance of a class the inherits ILocation, including apex.Coordinate, can be used.
- `getParallelScale() -> float` — Gets the scale used to determine what size objects in the scene appear on the screen when parallel projection is enabled. This scale is used to set how model (world) coordinates map to screen coordinates and defines the size of the view in world coordinates. Setting this value to the height of the model (model coordinates) will ensure that the entire model can fit height-wise within the view without being cropped. "parallelScale" works as an "inverse scale" — larger numbers produce smaller images. Setting parallelScale to half the height of the model in the current view will cause the model to require twice as much screen height to be fully displayed (it will appear cropped). Setting parallelScale to twice the height of the model in the current view will cause the model to require half as much screen height to be fully displayed and will occupy only half of the available screen height.
- `getPosition() -> apex.ILocation` — Gets the position of this Camera in global Cartesian coordinates. The coordinates of the Camera position must be defined using the units of Length the from the active script unit system When position is returned from a Camera object. it is always returned as an apex.ILocation (which inherits ILocation). When setting the position on a Camera, any instance of a class the inherits ILocation, including apex.Coordinate, can be used.
- `getViewUp() -> apex.construct.Vector3D` — Gets the view up direction vector for this camera.
#### `pan(horizontal_distance: float = 0.0, vertical_distance: float = 0.0) -> None`
pan the camera along the Camera viewUp and/or horizontal axis. The Camera horizontal axis is perpendicular to both the viewUp and directions of projection axes. Both translation axes pass through the Camera position

- `horizontal_distance` — The distance that the camera will be moved (in model space coordinates) along its horizontal axis positive values will move the camera in the positive direction of the horizontal axis and negative values in the negative direction distance represents a Length value and must be defined using the units of Length from the active script unit system
- `vertical_distance` — The distance that the camera will be moved (in model space coordinates) along its viewUp (vertical) axis Positive values will move the camera in the positive direction of the viewUp axis and negative values in the negative direction distance represents a Length value and must be defined using the units of Length from the active script unit system

#### `pitch(angle: float) -> None`
Rotate this Camera about the camera 'horizontal" axis - an axis passing through the Camera position and perpendicular to both the viewUp and direction of projection axes.

- `angle` — angle defining how far the scene will be rotated

- `reset() -> None` — When parallel projection is enabled (this is the only projection mode currently supported) this method changes the parallel scale, focal point and direction of projection to ensure that all entities in the 3D graphics scene are visible and centered in the view.
#### `roll(angle: float) -> None`
Rotate the camera about the direction of projection axis. The direction of projection axis runs from the camera position to the focal point.

- `angle` — angle defining the amount of camera rotation angle must be defined using the units of Angle from the active script unit system

#### `rotate(azimuth_angle: float = 0.0, elevation_angle: float = 0.0) -> None`
rotate Rotates the camera about the focal point Rotation about two axes passing through the focal point are supported The "Azimuth" axis is parallel to the Camera viewUp axis, passing through the focal point The "Elevation" axis is parallel to the Camera 'horizontal' axis, passing through the focal point. The Camera horizontal axis is perpendicular to both the viewUp and directions of projection axes. This method will change both the position and orientation of the Camera, leaving the focal point, distance and parallel scale unchanged

- `azimuth_angle` — angle by which the camera will be rotated about the azimuth at the focal point. angle represents an Angle quantity and must be defined using the unit of Angle from the active Script unit system
- `elevation_angle` — angle by which the camera will be rotated about the elevation axis at the focal point. angle represents an Angle quantity and must be defined using the unit of Angle from the active Script unit system

#### `setDirectionOfProjection(projection: apex.construct.Vector3D) -> None`
Sets a direction vector from the camera position to the focal point as a Vector3D.

- `projection` — Optional argument to define the direction of the Camera.

#### `setDistance(distance: float) -> None`
Sets the distance from this camera to the focal point.

- `distance` — - set camera distance which is a length between focal point to camera position.

#### `setFocalPoint(focalPoint: apex.ILocation) -> None`
Sets the position of this Camera in global Cartesian coordinates. The coordinates of the Camera position must be defined using the units of Length the from the active script unit system When position is returned from a Camera object. When setting the position on a Camera, any instance of a class the inherits ILocation, including apex.Coordinate, can be used.

- `focalPoint` — - set the focal point.

#### `setParallelScale(parallelScale: float) -> None`
Sets the scale used to determine what size objects in the scene appear on the screen when parallel projection is enabled. This scale is used to set how model (world) coordinates map to screen coordinates and defines the size of the view in world coordinates. Setting this value to the height of the model (model coordinates) will ensure that the entire model can fit height-wise within the view without being cropped. "parallelScale" works as an "inverse scale" — larger numbers produce smaller images. Setting parallelScale to half the height of the model in the current view will cause the model to require twice as much screen height to be fully displayed (it will appear cropped). Setting parallelScale to twice the height of the model in the current view will cause the model to require half as much screen height to be fully displayed and will occupy only half of the available screen height.

- `parallelScale` — - set the real scale.

#### `setPosition(position: apex.ILocation) -> None`
Sets the position of this Camera in global Cartesian coordinates. The coordinates of the Camera position must be defined using the units of Length the from the active script unit system When position is returned from a Camera object. When setting the position on a Camera, any instance of a class the inherits ILocation, including apex.Coordinate, can be used.

- `position` — - set the camera position.

#### `setViewUp(viewUp: apex.construct.Vector3D) -> None`
Sets the view up direction vector for this camera.

- `viewUp` — - set the camera View Up.

#### `viewFromX(reverse: bool = False, viewUp: [float] = [0.0, 1.0, 0.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector parallel to the global X axis. By default the camera will be pointing in a direction from +X to -X. Optional arguments are provided to, reverse the view direction (from -X to +X) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False (default) causes the camera to point from +X to -X Setting to True (default) causes the camera to point from -X to +X
- `viewUp` — optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global +Y axis If the input vector is not perpendicular to the global X axis it will be orthogonalised by projecting onto the YZ plane. If the input vector is parallel to the global X axis it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport. If True (default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `viewFromY(reverse: bool = False, viewUp: [float] = [0.0, 0.0, 1.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector parallel to the global Y axis. By default the camera will be pointing in a direction from +Y to -Y. Optional arguments are provided to, reverse the view direction (from -Y to +Y) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False (default) causes the camera to point from +Y to -Y Setting to True (default) causes the camera to point from -Y to +Y
- `viewUp` — optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global +Z axis If the input vector is not perpendicular to the global Y axis it will be orthogonalised by projecting onto the XZ plane. If the input vector is parallel to the global Y axis it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport. If True (default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `viewFromZ(reverse: bool = False, viewUp: [float] = [0.0, 1.0, 0.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector parallel to the global Z axis. By default the camera will be pointing in a direction from +Z to -Z. Optional arguments are provided to, reverse the view direction (from -Z to +Z) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False (default) causes the camera to point from +Z to -Z Setting to True (default) causes the camera to point from -Z to +Z
- `viewUp` — optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global +Y axis If the input vector is not perpendicular to the global Z axis it will be orthogonalised by projecting onto the XY plane. If the input vector is parallel to the global Z axis it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport. If True (default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `viewIsometric_1(reverse: bool = False, viewUp: [float] = [0.0, 1.0, 0.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector from octant (+++) to octant () Optional arguments are provided to, reverse the view direction (from octant () to octant (+++)) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False (default) causes the camera to point from octant (+++) to octant () Setting to True (default) causes the camera to point from octant () to octant (+++)
- `viewUp` — optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global +Y axis If the input vector is not perpendicular to the view direction axis it will be orthogonalized by projecting onto the XZ plane. If the input vector is parallel to the global direction of projection it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport. If True (default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `viewIsometric_2(reverse: bool = False, viewUp: [float] = [0.0, 1.0, 0.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector from octant(-++) to octant(+) Optional arguments are provided to, reverse the view direction(from octant(+) to octant(-++)) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False(default) causes the camera to point from octant(-++) to octant(+) Setting to True(default) causes the camera to point from octant(+) to octant(-++)
- `viewUp` — optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global + Y axis If the input vector is not perpendicular to the view direction axis it will be orthogonalized by projecting onto the XZ plane.If the input vector is parallel to the global direction of projection it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport.If True(default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `viewIsometric_3(reverse: bool = False, viewUp: [float] = [0.0, 1.0, 0.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector from octant(+-+) to octant(-+-) Optional arguments are provided to, reverse the view direction(from octant(-+-) to octant(+-+)) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False(default) causes the camera to point from octant(+-+) to octant(-+-) Setting to True(default) causes the camera to point from octant(-+-) to octant(+-+)
- `viewUp` — Optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global + Y axis If the input vector is not perpendicular to the view direction axis it will be orthogonalized by projecting onto a plane perpendicular to the direction of projection If the input vector is parallel to the global direction of projection it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport.If True(default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `viewIsometric_4(reverse: bool = False, viewUp: [float] = [0.0, 1.0, 0.0], reset: bool = True) -> None`
Repositions the Camera such that it is looking along a vector from octant( + ) to octant(+) Optional arguments are provided to, reverse the view direction(from octant(+) to octant( + )) control the camera viewUp direction automatically fit the entire model to the viewport - this is the default behavior.

- `reverse` — Optional argument to reverse the view direction Setting to False(default) causes the camera to point from octant( + ) to octant(+) Setting to True(default) causes the camera to point from octant(+) to octant( + )
- `viewUp` — optional argument to define the direction of the Camera viewUp vector By default, the Camera viewUp axis will be set parallel to the global + Y axis If the input vector is not perpendicular to the view direction axis it will be orthogonalized by projecting onto the XZ plane.If the input vector is parallel to the global direction of projection it will be ignored and the default viewUp vector used
- `reset` — optional argument to control whether the view will be fitted to the viewport.If True(default) the Camera properties will be adjusted to ensure that the model fills and is centered on the viewport Setting reset to False will rotate the camera such that is is aligned with the view direction but will not change the position of the Camera or its parallel scale

#### `yaw(angle: float) -> None`
Rotate this Camera about an axis passing through the Camera position and parallel to the Camera viewUp vector. This method rotates all Camera axes and the focal point.

- `angle` — - angle defining how far the scene will be rotated

#### `zoom(factor: float) -> None`
When parallel projection is enabled (this is the only projection mode currently supported) this method changes the parallel scale by the specified factor. Since parallel scale is an inverse scale, a value greater than 1.0 zooms in and a value less than 1.0 zooms out.

- `factor` — parallel scale factor. A value greater than 1.0 zooms in, a value less than 1.0 zooms out.


## `apex.display.CutView`
A CutView defines a set of parameters which are used in the Cut view.
Properties: `bSlideMode`, `location`, `orientation`

Methods:

- `getCutViewLocation() -> apex.Coordinate` — Gets a location from the cut view as a apex.ILocation.
- `getCutViewOrientation() -> apex.IOrientation` — Gets a orientation from the cut view as a apex.Orientation.
- `getCutViewSlideMode() -> bool` — Gets a slide mode from cut view.
- `reverse() -> None` — Call this method will result to the reversed cut view, the attribute of "orientation" is changed to point to the opposite direction.
#### `setCutViewLocation(location: apex.ILocation) -> None`
Sets a location to the cut view as a apex.ILocation.

- `location` — Optional argument to define the location of the cut view.

#### `setCutViewOrientation(orientation: apex.IOrientation) -> None`
Sets a orientation to the cut view as a apex.Orientation.

- `orientation` — Optional argument to define the orientation of the cut view.

#### `setCutViewSlideMode(bSlideMode: bool) -> None`
Sets a slide mode to cut view.

- `bSlideMode` — - specify the cut view type, either clip or slide.

#### `update(location: apex.ILocation, orientation: apex.IOrientation, bSlideMode: bool) -> None`
Boolean argument controls to show the UTM and cut tool or hide them.

- `location` — - set the focal point.
- `orientation` — - set the focal point.
- `bSlideMode` — - specify the cut view type, either clip or slide.


## `apex.display.GraphicsText`
Text object on the graphics view at a specified location. The graphics text will rotate and translate with the model but will remain front facing. Create using apex::display::displayText() method.
Properties: `fontColor`, `fontFamily`, `fontSize`, `fontStyle`, `location`, `text`, `underlineStyle`

Methods:

- `createText() -> bool`
- `setText(strtext: str) -> None` — Update text Location of this GraphicsText object.

## `apex.display.Tessellation`  (extends `Entity`)
Base class for Tessellation0D, Tessellation1D and Tessellation2D.
Properties: `points`

Methods:

#### `getPoints() -> [float]`
An array of floats holding all of the tessellation point coordinates. The array contains the coordinates of all points that define the tessellation as a continuous array of x, y, z coordinates. The array is a one dimensional array where the coordinates are stored as a contiguous sequence of float values [x1, y1, z1, x2, y2, z2,...] The triangle, line and point topologies defined in the Tessellation0D, Tessellation1D and Tessellation2D classes are defined using 'indices' into this array (strictly indices into the triplets of x, y, z values) The coordinate values in this array represent quantities of Length and are specified in the units of Length from the active script unit system.

Returns: array of points


## `apex.display.Tessellation0D`  (extends `Tessellation`)
class describing the tessellation of a 0D body - usually a geometry Point or Vertex. Note - a geometry PointBody object may compose one or more Vertices. The 0D region is assumed to be made up of one or more Vertices where the Vertices are represented as polyvertices. The topology of each vertex is defined using indices into the 'points' array from this class.Since the points array is a 1D array, the indices of the points are actually the indices of triplets of coordinates in the points array.
Properties: `vertices`

Methods:

#### `getVertices() -> {str:[int]}`
returns a Dictionary containing the tessellations of all Vertices in this Tessellation. The dictionary contains a maximum of three and a minimum of two items, Point/Vertex IDs (optional) Number of points per vertex Indices of the point coordinates in the Tessellation.points array. The optional Point/Vertex ID item has a string key "ids" with an associated integer array value. Each integer item in this array represents the ID of a Point/Vertex in the Tessellation. The required number of points per Vertex item has a string key "num_cells" with an associated integer array value. Each integer item in this array represents the number of points required to define each polyvertex that represents a Point The number of items in each of these two arrays is equal to the number of Vertices in the Tessellation and the data is ordered consistently by Vertex across each array. The coordinate item has string key "point_indices" with an associated integer array value. Each integer item in this array represents the index of a point in the Tessellation/points array. Example: Given the topology shown below comprising a single region with two Faces, nine Edges and eight Vertices, vertices["ids"] contains the ids for all eight vertices - [V1, V2, V3,.....V8] where Vn represents the ID for Vertex n vertices["num_cells"] contains the number of vertices used to define the polyvertex for each Point [V1NumPoints, V2NumPoints, V3NumPoints.....V9NumPoints] where VnNumPoints = the number of points required to define the polyvertex representing Vertex n vertices["point_indices"] contains the indices of the coordinates for all eight vertices [V1I, V2I, V3I.....V8I] where VnI = the index of the point coordinates for Vertex n

Returns: a Dictionary of verteices


## `apex.display.Tessellation1D`  (extends `Tessellation0D`)
class representing the tessellation of a 1D region - commonly a geometry Line or Edge. The 1D region is assumed to be made up of one or more Edges and Vertices where the Edges are represented as polylines and the Vertices as points. The topology of each line and point is defined using indices into the 'points' array from this class.Since the points array is a 1D array, the indices of the lines and points is actually the index of triplets of coordinates in the points array.
Properties: `edges`

Methods:

#### `getEdges() -> {str:[int]}`
returns a Dictionary containing the tessellations of all Edges in this region. Each Edge in the region has an optional ID and is represented by a polyline. Each polyline may have a different number of segments. The dictionary contains a maximum of three and a minimum of two items, Edge IDs (optional) Number of points per Edge (equals the number of polyline segments plus 1) Indices of the Edge point coordinates in the Tessellation.points array. The optional Edge ID item has a string key "ids" with an associated integer array value. Each integer item in this array represents the ID of an Edge in the Tessellation. The required number of points per Edge item has a string key "num_poly_points" with an associated integer array value. Each integer item in this array represents the number of points required to define each polyline that represents an Edge The number of items in each of these two arrays is equal to the number of Edges in the Tessellation and the data is ordered consistently by Edge across each array. The coordinate item has string key "point_indices" with an associated integer array value. Each integer item in this array represents the index of a point in the Tessellation/points array. Example: Given the topology shown below comprising a single region with two Faces, nine Edges and eight Vertices, edges["ids"] contains the ids for all nine edges - [E1, E2, E3,.....E9] where En represents the ID for Edge n edges["num_poly_points"] contains the number of points used to define the polylines for each Edge [E1NumPoints, E2NumPoints, E3NumPoints.....E9NumPoints] where EnNumPoints = the number of points required to define the polyline representing Edge n edges["point_indices"] contains the indices of the points that define the polylines for each Edge in this Tessellation. This array will contain sum(edges["num_poly_points"]) entries

Returns: a Dictionary of edges


## `apex.display.Tessellation2D`  (extends `Tessellation1D`)
class describing the tessellation of a 2D region - usually a geometry Surface or Face. The 2D region is assumed to be made up of one or more Faces, Edges and Vertices where the Faces are represented as triangles, the Edges as lines and the Vertices as points. The topology of each triangle, line and point is defined using indices into the 'points' array from this class.Since the points array is a 1D array, the indices of the triangles, lines and points is actually the index of triplets of coordinates in the points array.
Properties: `faces`

Methods:

#### `getFaces() -> {str:[int]}`
returns a Dictionary containing the tessellations of all Faces in this region. Each Face in the region has an optional ID and is represented by series of triangles. The dictionary contains a maximum of three and a minimum of two items, Face IDs (optional) Number of triangles per Face Indices of the triangle point coordinates in the Tessellation.points array. The optional Face ID item has a string key "ids" with an associated integer array value. Each integer item in this array represents the ID of a Face in the Tessellation. The number of triangles per Face item has a string key "num_cells" with an associated integer array value. Each integer item in this array represents the number of triangles used to define each Face The number of items in each of these two arrays is equal to the number of Faces in the Tessellation and the data is sequenced consistently by Face across each array. The coordinate item has string key "point_indices" with an associated integer array value. Each integer item in this array represents the index of a point in the Tessellation.points array. Example: a Given the topology shown below comprising a single region with two Faces, nine Edges and eight Vertices, faces["ids"] contains the ids for both Faces - [F1, F2] where Fn represents the ID for Face n faces["num_cells"] contains the number of triangles used to define each Face [F1NumTRias, F2NumTRias]where FnNumTrias = the number of triangles required to define the Face "n" faces["point_indices"] contains the indices of the points that define the triangles for each Face in this Tessellation. This array will contain sum(edges["num_cells"] * 3) entries Each Face tessellation is represented in a key, value pair where, 1. key is an integer type and identifies the Face index. The Face index uniquely identifies the Face within this 2D region 2. value is an array of ints defining the connectivity of the Face tessellation. The Face tessellation consists entirely of triangles, each defined by three indices into the points array for this 2D region. The array is a 1D array where the indices of each triangle are defined one after the other [T1V1, T1V2, T1V3, T2V1, T2V2, T2V3, ....] where Tn represents the triangle index in this array and Vn represents the triangle Vertex index. This array will contain three times as many entire as there are triangle in this tessellation

Returns: a Dictionary of edges


