# apex.utility — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.utility.PolyData`
A class that supports operations on points and cells. The cells can be linear or quadratic triangles or quadrilaterals. The point and cell data may be composed directly by the class or provided by a suitable external object such as a SurfaceMesh. NOTE : In the current Apex release the point and cell data is ONLY supported through reference to an external SurfaceMesh NOTE : In future releases the types of supported external objects will be expanded to include SolidMesh (tetrahedral) and HexMesh (hexa/penta) mesh types where the free faces of the mesh will be used to define the PolyData. NOTE : In current Apex releases PolyData objects are not persisted although this will likely change in future releases In the current Apex release the primary purpose of the PolyData class is to support the creation of geometry FacetedSurfaces, however future releases will leverage this same data structure for many other purposes including construction and display of user defined shapes and to support mapping of attributes between different meshes. In addition to defining the point locations and cell topologies a PolyData supports the concept of higher level topological organization of the raw points and cells into topological faces, edges and vertices. Topological faces are defined by groups of contiguous 2D cells, edges by groups of contiguous cell edges and vertices as individual points. Methods are provided to organize and introspect the groups of cells, cell edges and points that define the higher level topology. The class internally imposes the rules required to maintain viable topology - cells may be associated with just a single topological face, topological faces must contain only cells that are contiguous, a topological vertex must exits at each end of a topological edge, topological vertices must lie on a topological edge etc. PolyData also supports named Sets that can define arbitrary groups of mixed PolyData primitives. The Sets are not managed by the class as operations are executed and it is the users responsibility to ensure that the contents of the Sets remain synchronized with the underlying primitives.
Properties: `sets`, `topologyEdges`, `topologyEdgeVertices`, `topologyFaceEdges`, `topologyFaces`, `topologyFaceVertices`, `topologyVertices`

Methods:

- `addSet(name: str, contents: apex.utility.PolyDataType, stringDictionary: {int:str}) -> None` — Defines a grouping of PolyData primitives.
- `getSets() -> {str:{int:str}}` — Returns all groupings of PolyData primitives.
- `getTopologyEdgeVertices() -> {int:str}` — Returns a Dictionary containing the topological edges and their associated topological vertices. The Dictionary key is of type integer and represent the ID of the topological edge. The associated value is of type string and holds the ID's of the topological vertices associated with the topological edge.
- `getTopologyEdges() -> {int:str}` — A Dictionary containing all groups of cell edges in the object that represent higher level topological edges.The dictionary key is of type integer and represent the id of the topologyEdge. The dictionary value is of type string and identifies the set of cell edges associated with the toplogical edge identified by the key. Run length encoded ID's enable compact identification of multiple cell edges particullarly when the set of points contains consecutive ID's. The string "1.1, 4.2, 2001-5000.5" fro example identifies...
- `getTopologyFaceEdges() -> {int:str}` — returns a Dictionary containing the topological faces and their associated topological edges. The Dictionary key is of type integer and represent the ID of the topological face. The associated value is of type string and holds the ID's of the topological edges associated with the topological face.
- `getTopologyFaceVertices() -> {int:str}` — Returns a Dictionary containing the topological faces and their associated topological vertices. The Dictionary key is of type integer and represent the ID of the topological face. The associated value is of type string and holds the ID's of the topological vertices associated with the topological face.
- `getTopologyFaces() -> {int:str}` — A Dictionary containing all groups of cells in the object that represent higher level topology faces. The dictionary key is of type integer and represent the id of the topological face. The dictionary value is of type string and identifies the set of 2D cells associated with the topologicalface identified by the key. Run length encoded ID's enable compact identification of multiple cells particularly when the set of points contains consecutive ID's. The string "1, 4, 2001-5000" for example identifies a total of 3,002 cells - cells with ID's 1, 4 and all cells with ID's from 2001 to 5,000 inclusive.
- `getTopologyVertices() -> {int:str}` — A run length encoded string describing the IDs of all points in the object that represent higher level topological vertices Run length encoded ID's enable compact identification of multiple points particularly when the set of points contains consecutive ID's. The string "1, 4, 2001-5000" for example identifies a total of 3,002 points - points with ID's 1, 4 and all points with ID's from 2001 to 5,000 inclusive.
#### `mergeTopologicalFaces(faceIDs: [int], vertexAngle: float) -> [int]`
Merge two or more topology faces into a single topology face. This class internally manages groups of contiguous cells that represent higher level topological faces. The set of topological faces that are available with in the object are exposed via the topological faces atrributes, which returns a Dictionary containing all of the topological faces that exist within the object. The dictionary key is of type integer and represents the ID of the topological face. The dictionary value is of type string and identifies the set of cells that are associated with the named topological face. The two or more topological faces that are be merged are supplied to the method using their ID's. The method return a list of integers representing the ID's of all of the New(new,and any unchanged) topological faces that were created by the method.

- `faceIDs` — A List of integers defining the ID's of the Faces that the method will attempt to merge
- `vertexAngle` — An optional angle (default is 40 degrees) that will be used to automatically decide if one children vertex need to be removed when one topology edge is removed during face merge. This argument represents a measure of angle and must be supplied in the angle units defined in the active ScriptUnitSystem.

- `removeSets(names: [str]) -> bool` — Removes a grouping of PolyData primitives.
#### `updateToplogyEdges(edgeIDs: str, vertexAngle: float, addRemoveBehavior: apex.utility.AddRemoveBehavior) -> None`
modifies the contents of the object topologyEdges data structure This class maintains a list of cell edges that will be used to define high level topological edges and this method modifies that list. This method accepts a list of cell edges and udpateBehavior argument and causes the supplied cell edges to be added to or removed from topologyEdges depending on the value provided for updateBehavior. The input cells are identified by ID and must exist within the object, otherwise the method will throw an exeption.

- `edgeIDs` — The set of cell edges to be added to or removed from the topologyEdges set
- `vertexAngle` — An optional angle (default is 40 degrees) that will be used to automatically add topology Vertices based on the angle between adjacent edge normals when a new topology edge is added, or decide if one children vertex need to be removed when one topology edge is removed in the PolyData. This argument represents a measure of angle and must be supplied in the angle units defined in the active ScriptUnitSystem.
- `addRemoveBehavior` — optional argument that defines whether the supplied cell edges will be added to or removed from the topologyEdges set. The default "Add" option will cause all of the supplied cell edges to be added to the topologyEdges set. Any input cell edges that would result in duplicate cell edges in topologyEdges are silently ignored to ensure that topologyEdges contains only unique cell edges. The "Remove" option will cause all of the supplied cell edges to be removed from the topologyEdges set. Any input cell edges that are not already in topologyEdges will be silently ignored The "Toggle" option will cause all of the supplied cell edges that are already in the topologyEdges set to be removed from topologyEdges and all supplied cell edges that are NOT already in topologyEdges to be added.

#### `updateToplogyVertices(pointIDs: str, addRemoveBehavior: apex.utility.AddRemoveBehavior) -> None`
modifies the set of points in the Tessellation that will be identified as Vertex points. This class maintains a list of points that will be used to define vertices and this method modifies that list. This method accepts a list of points and an updateBehavior argument and causes the supplied points to be added to or removed from the internal vertex depending on the value provided for updateBehavior. The input points are identified by ID and must exist within the object, otherwise the method will throw an exception.

- `pointIDs` — The set of points to be added to or removed from the object vertexPoints set
- `addRemoveBehavior` — optional argument that defines how the supplied points will be processed. The default "Add" option will cause all of the supplied points to be added to the vertexPoints list. Any input points that would result in duplicate points in the vertexPoints set are silently ignored to ensure that the set contains only unique points. The "Remove" option will cause all of the supplied points to be removed from the vertexPoints set. Any input points that are not already in the vertexPoints set will be silently ignored The "Toggle" option will cause all of the supplied points that are already in the vertexPoints set to be removed from the set and all supplied points that are NOT already in the vertexPoint set to added to the point set.


## `apex.utility.ProximitySearch`
The ProximitySearch class is provided to support very fast determination of the objects (or objects) that are closest to a given target location (or object) or that lie within an axis aligned box in global 3D space. To use this class, insert all of the objects that you need to consider in the proximity calculation - performance is proportional to the number of objects that are inserted so for best performance, limit the number of objects that you add. Several methods are provided to add individual objects or lists/collections of objects. Only object that support the ILocation interface can be added to a ProximitySearch object. When the object is populated with all candidate objects, use the 'findXXX()' methods to determine which of the candidate objects is closest to the target location or lie within the bounding box.
Properties: `candidates`

Methods:

- `ProximitySearch() -> None` — Construct a new ProximitySearch.
#### `clearCandidates() -> bool`
This method clears all candidate objects from the ProximitySearch object.

Returns: true if successful

#### `findNearestObject(location: apex.ILocation) -> apex.utility.ZResultfindNearestObject`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems.

- `location` — Specifies the location want to find the entity

Returns: true if successful

This method takes a target location in 3D space as an argument and returns a result object that includes the candidate object within the ProximitySearch object that is closest to the target location. All proximity calculations use the "location" attribute of the candidate objects as their basis so for 1D, 2D and 3D objects, some portions of the object may lie closer to or further away from the target location than the single distance value indicates. For example, for an edge or manifold curve, the distance is between the target location and the mid point of the edge or manifold curve. For a solid, the distance is between the target location and the centroid of the solid..

#### `findNearestObjects(location: apex.ILocation, numObjects: int = 1) -> apex.utility.ZResultfindNearbyObjects`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems.

- `location` — Specifies the location want to find the entity
- `numObjects` — Specifies the number of objects to find.

Returns: ZResultfindNearbyObjects result class if successful

This method takes a target location in 3D space and the number of nearest objects to find as arguments and returns a result object that includes the candidate object within the ProximitySearch object that is closest to the target location. All proximity calculations use the "location" attribute of the candidate objects as their basis so for 1D, 2D and 3D objects, some portions of the object may lie closer to or further away from the target location than the single distance values indicates. For example, for an edge or manifold curve, the distance is between the target location and the mid point of the edge or manifold curve. For a solid, the distance is between the target location and the centroid of the solid.

#### `findObjectsAABoundingBox(corner1: apex.ILocation, corner2: apex.ILocation) -> IPhysicalCollection`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. This method takes the corners of a bounding box in global 3D space as input and returns all candidate objects referenced by the ProximitySearch object that lie within this bounding box as a Collection of PhysicalObjects.

- `corner1` — An object that defines the location of one corner of the axis aligned bounding box.
- `corner2` — An object that defines the location of one corner of the axis aligned bounding box.

Returns: ILocationCollection of objects within the box

All objects that lie within or on the faces of the bounding box are returned.

#### `findObjectsWithinDistance(location: apex.ILocation, distance: float) -> apex.utility.ZResultfindNearbyObjects`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. This method takes a target location in 3D space and a distance as input and returns all objects in the candidate set that are closer to (or the same distance from) the target location than the specified distance. All proximity calculations use the "location" attribute of the candidate objects as their basis so for 1D, 2D and 3D objects, some portions of the object may lie closer to or further away from the target location than the single distance values indicates. All candidate objects that lie within this distance (including exactly matching this distance) of the target location will be returned. Candidate objects further away from the target than this distance will be omitted.

- `location` — Specifies the location want to find the entity
- `distance` — The distance that will be used to determine if a candidate object is close enough to the target to qualify as "within distance".

Returns: ZResultfindNearbyObjects result class if successful

#### `getCandidates() -> IPhysicalCollection`
This method returns collection of all of the candidate entities that have been added to the ProximitySearch object..

Returns: ILocationCollection of the candidate entities that have been added to the ProximitySearch object

#### `insert(locationObject: apex.ILocation) -> bool`
This method adds an object to the ProximitySearch object.

- `locationObject` — The locationObject must support the ILocation interface. After an object is inserted it will be included in all future requests to find nearest neighbors.

Returns: true if successful

The object that is being added must support the ILocation interface - if it does NOT support this Interface it will not be added and the method will return False. The class internally removes duplicate candidate objects prior to any request for finding nearest neighbors.

#### `insertCollection(candidates: apex.ILocationCollection) -> bool`
This method adds a Collection of objects to the ProximitySearch object.

- `candidates` — A collection of PhysicalObjects that will be added to any existing candidate objects contained by the ProximitySearch object.

Returns: true if successful

All objects in the Colection must support the ILocation interface - objects that do NOT support this Interface will not be added and the method will return False (although all objects in the List that DO support the ILocation interface will be added) The class internally removes duplicate candidate objects prior to any request for finding nearest neighbors.

#### `insertList(candidates: [apex.ILocation]) -> bool`
This method adds a List of objects to the ProximitySearch object.

- `candidates` — A List of PhysicalObjects that will be added to any existing candidate objects contained by the ProximitySearch object.

Returns: true if successful

All objects in the List must support the ILocation interface - objects that do NOT support this Interface will not be added and the method will return False (although all objects in the List that DO support the ILocation interface will be added) The class internally removes duplicate candidate objects prior to any request for finding nearest neighbors.


## `apex.utility.ZResultfindNearbyObjects`
Instances of this class are returned by the findObjectsWithinDistance() method of the ProximitySearch class.
Properties: `distances`, `objects`, `vectors`

Methods:

- `foundObjects(: None) -> apex.IPhysicalCollection` — The objects from the ProximitySearch candidates that are closest to or within a specified distance of the target location. When returned from the getNearestObjects(numObjects = n) method, foundObjects contains the n nearest objects to the location. If there are less then n objects in the candidate object set foundObjects may contain less than n objects When returned from the getObjectsWithinDistance(distance = d) method, foundObjects contains all objects in the candidate objects set that lie within the specified distance d of the location. If no objects lie within this distance, foundObjects will be empty. this object.
- `getDistances(: None) -> [float]` — This method returns a List of distances, as floats, between the target location and the found objects. These distance are based on the location attribute of the candidate objects - for 1D, 2D or 3D candidates some portions of the candidate objects may lie closer to or further away than this distance This List contains the same number of items as the foundObjects Collection and the distances are ordered with the shortest distance first and in increasing order. The order of the objects in foundObjects matches the ordering in this List.
- `getVectors(: None) -> [apex.construct.Vector3D]` — This method returns a list of Vector3D objects that defines the vector between the target location and the location of the nearest object. a list of Vector3Ds that defines the global x, y, z vector between the location and the foundObjects. These vectors are based on the location attribute of the foundObjects - for 1D, 2D or 3D objects some portions of the foundObjects may lie closer to or further away than the distance defined by this vector. This list contains the same number of items as the foundObjects Collection and the vectors are ordered with the shortest distance first and in increasing order. The order of the objects in foundObjects matches the ordering in this list.
- `~ZResultfindNearbyObjects() -> None`

## `apex.utility.ZResultfindNearestObject`
Instances of this class are returned by the findNearestObject() and findObjectsWithinDistance() methods of the ProximitySearch class.
Properties: `distance`, `nearestObject`, `vector`

Methods:

- `getDistance(: None) -> float` — This method returns the distance between the target location and the nearest neighbor. This distance is base on the location attribute of the candidate object - for 1D, 2D or 3D candidates some portions of the candidate objects may lie closer to or further away than this distance.
- `getNearestObject(: None) -> apex.Entity` — This method returns the object from the ProximitySearch candidates that is closest to the target location.
- `getVector(: None) -> apex.construct.Vector3D` — This method returns a apex.construct.Vector3D object that defines the vector between the target location and the location of the nearest object.

