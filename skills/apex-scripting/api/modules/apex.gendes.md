# apex.gendes

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.gendes.BoundingBoxOffsetType`: `Fixed`, `Proportional`
  - Optional enumeration argument that controls how the base bounding box size is adjusted. The base bounding box is calculated such that it minimally encloses the target Parts/Bodies. This implies that the target will 'touch' each face of the bounding box in at least one location. In order to allow for some clearance between the bounding box and the target entities the method supports specification of an offset. This offset will be added to the base bounding box shape to provide some clearance between the target and the box. The offset may be specified to be a fixed offset (each face of the base bounding box will be offset by the same fixed distance on all size faces) or to be a proportional offset where the offset on pairs of opposite faces is determined y the distance between these faces multiple id by a scale factor The default value of apex.BoundingBoxOffsetType.Fixed will cause the provided offset value to be used asa fixed offset on all six faces. The optional apex.BoundingBoxOffsetType.Proportional value will cause the provided offset value to be used as a proportional offset

`apex.gendes.BoundingBoxType`: `ObjectAligned`, `Global`
  - To determine whether the DesignSpace will be created based on a globally or object oriented bounding box around the target Parts/Bodies. The default apex.BoundingBoxType.ObjectAligned will cause the minimum possible volume DesignSpace to be created by allowing the orientation of the bounding box to be oriented to any direction. The optional apex.BoundingBoxType.Global will cause the minimum possible volume DesignSpace to be created while retaining the orientation of the bounding box to be remain aligned with the global rectangular axes

`apex.gendes.TargetSolidBehavior`: `KeepCurrent`, `Reparent`, `Copy`
  - Argument to define the target solid behavior. Default behavior is "KeepCurrent", this will use the target solid as the design space solid and create design space in the current part. Setting this value to "Reparent" will force system to reuse the target solid as the design space solid and reparent it in "Design Part", with material, Loads and Boundary Condition retained on the design space solid. Setting this value to "Copy" will copy the target solid as design space solid in "Design Part", while the material, Loads and Boundary Condition are not retained on the design space solid

## Module functions

### `apex.gendes.createAccessRegionExtrudeCrossSection(target: apex.EntityCollection, origin: apex.ILocation, extrudeVector: apex.construct.Vector3D, extrusionDistance: float = 10, startOffsetDistance: float = 0, scalingFactor: float = 1, flipDirection: bool = False, removeInteriorClosedLoops: bool = True) -> apex.geometry.SolidCollection`
Create solids of access region by extruding a cross section profile extracted on a plane.

- `target` — EntityCollection of solids, surfaces, cells and faces.
- `origin` — The origin of the cross section plane.
- `extrudeVector` — This vector is used to define the cutting plane orientation as well as the extrude direction. The cutting plane location is determined by the origin and the extrudeVector, while the extrudeVector is always the normal vector of the plane.
- `extrusionDistance` — The total extrude distance.
- `startOffsetDistance` — The initial offset, or starting bound distance.
- `scalingFactor` — An optional scaling factor that will be applied to the extruded solid. This is intended to support creation of an Access Region that is slightly larger than the selected entities, default value is 1.00 (no scale). Valid values larger than 1.00 will scale up the solid, while values smaller than 1.00 will scale down the solid. Note that this scaling does not change the dimension along the extruding vector.
- `flipDirection` — Flip the extrude direction. It's omitted by default(False) and system extrudes along the normal direction of the cross section plane. If True, system will extrude along the reversed direction.
- `removeInteriorClosedLoops` — Remove the interior edges that are enclosed inside the cross section. It's omitted by default (True).

### `apex.gendes.createAccessRegionFollowNormal(target: apex.EntityCollection, extrudeVector: apex.construct.Vector3D, extrusionDistance: float = 10, startOffsetDistance: float = 0, scalingFactor: float = 1, flipDirection: bool = False) -> apex.geometry.Solid`
Create solid of access region by extruding the surfaces/faces following a normal direction by default.

- `target` — A collection of surfaces, faces.
- `extrudeVector` — The extruding vector of the selected entities. It's empty by default and system will calculate a default normal vector. If there are planar faces in the selected entities, then system will use the normal vector of the largest face as the default vector. If all selected entities are non-planar faces, then system will evaluate the boundary edges and use the normal vector of the plane defined by co-planar boundary edges. If both of the two methods fail, system will calculate a local minimum bounding box for all the selected entities, and then use the local axis of the bounding box, in which the bounding box dimension is the smallest, as the default extrude vector.
- `extrusionDistance` — The total extrude distance.
- `startOffsetDistance` — The initial offset, or starting bound distance.
- `scalingFactor` — An optional scaling factor that will be applied to the extruded solid. This is intended to support creation of an Access Region that is slightly larger than the selected entities, default value is 1.00 (no scale). Valid values larger than 1.00 will scale up the solid, while values smaller than 1.00 will scale down the solid. Unlike createAccessRegionExtrudeCrossSection, this scaling factor changes the dimensions uniformly.
- `flipDirection` — Flip the extrude direction. Default is omitted (False) and system extrudes the selected entities along the extrudeVector. If True, system will extrude along the reverse direction.

### `apex.gendes.createClearanceRegion(offsetDistance: float, targetFaces: apex.EntityCollection, name: str = "", description: str = "") -> apex.gendes.ClearanceRegion`
this function used to create a clearance region object.

- `offsetDistance` — it's used to defined how much distance the clearance region is.
- `targetFaces` — it's used to defined which target faces user want to select to applied the clearance region.
- `name` — the name of the clearance region object.
- `description` — the description of a clearance region object.

### `apex.gendes.createCompoundInterface(nonDesignSpaceThickness: float, machiningAllowance: float, offsetDistance: float, target: apex.EntityCollection, name: str = "", description: str = "", overWrite: bool = True) -> apex.gendes.CompoundInterfaceCollection`
Create one or several compoundInterfaces by defining the interface thickness, machining allowance and offset distance. This method returns an CompoundInterfaceCollection, the number of compound interfaces is dependent on the target. System will smartly create the correct number of compound interfaces by judging the faces connectivity and considering the associated loads and boundary conditions. In general, all connected faces will be created with one compound interface, and if the connected faces are associated with several loads and boundary conditions, then system groups the connected faces by each load and boundary condition: each interface is created to cover the application region of each load and boundary condition. For example:

- `nonDesignSpaceThickness` — The Non-Design Space Thickness of the compound interface.
- `machiningAllowance` — The machining allowance of the compound interface.
- `offsetDistance` — An optional offset distance for the selected faces in the compound interface. If provided, system will offsets the selected faces to get the side faces, and then merge the selected faces with the side faces. The merge face will be used as the actual compound interface surface. If omitted, the selected faces will be used as the compound interface surface.
- `target` — The selected target for the compound interface. Currently Apex only supports face in the target.
- `name` — An optional name for the interface that will be created. If omitted, the system will assign a default name formed by concatenating the prefix “Interface” with the smallest possible integer required to ensure name uniqueness within the current Model. For example “Interface 3”.
- `description` — An optional description for the interface that will be created. If omitted the description will be left blank.
- `overWrite` — The optional boolean argument to control whether overwrite existing interfaces or not. If omitted, the default value is True. If True the method will overwrite the existing interfaces on same faces. If False the method will NOT overwrite the existing interfaces on the same faces, but only create new interfaces.

If the target only contains one face or a group of connected faces, or a group of connected faces associated with one load, then this method creates one compound interface.If the target contains several groups of connected faces without any load or boundary condition, then this method creates several compound interfaces: each compound interface covers one group of connected faces.If the target contains one group of connected faces, while these connected faces are associated with several loads and boundary conditions, then this method creates several compound interfaces: each compound interface covers the connected application region of one load and boundary condition. Note that if the connected application regions of all loads and boundary conditions are exactly the same, then only one compound interface is created.If the target contains several groups of connected faces associated with several loads and boundary conditions, then for each group of connected faces, system performs step 3 until all faces are covered by compound interfaces.

### `apex.gendes.createCompoundInterfacesByLoadsConstraints(nonDesignSpaceThickness: float, machiningAllowance: float, offsetDistance: float, target: apex.EntityCollection = None, name: str = "", description: str = "", overWrite: bool = True) -> apex.gendes.CompoundInterfaceCollection`
Create compound interfaces on the faces applied with loads and constraints in the design target. This method returns a CompoundInterfaceCollection, the number of compound interfaces is dependent on the target. System will smartly create the correct number of interfaces by judging the faces connectivity and considering the associated loads and constraints. If target is omitted, system will automatically create compound interfaces on the all faces applied with loads and constraints in the design target so that each compound interface covers the application region of one load or constraint. Each group of connected faces applied with one load or constraint will be created with one compound interface. For example, if one force is applied with two disconnected faces, then two compound interfaces are created on the two faces. But if one force is applied on two connected faces, then only one compound interface is created on the two faces.

- `nonDesignSpaceThickness` — The non-design space thickness of compound the interface.
- `machiningAllowance` — The machining allowance thickness of the compound interface.
- `offsetDistance` — An optional offset distance for the selected faces in the compound interface. If provided, system will offsets the selected faces to get the side faces, and then merge the selected faces with the side faces. The merge face will be used as the actual interface surface. If omitted, the selected faces will be used as the interface surface.
- `target` — An optional target that will be created with compound interfaces. When this argument is omitted, system will automatically search all faces applied with loads and constraints in the design target and create compound interface on each group of faces applied with one load or constraint. When this argument is provided, the target must be the faces applied with loads and boundary conditions in the design target.
- `name` — An optional name for the compound interface that will be created. If omitted, the system will assign a default name formed by concatenating the prefix “Interface” with the smallest possible integer required to ensure name uniqueness within the current Model. For example “Interface 3”.
- `description` — An optional description for the compound interface that will be created. If omitted the description will be left blank.
- `overWrite` — The optional boolean argument to control whether overwrite existing interfaces or not. If omitted, the default value is True. If True the method will overwrite the existing interfaces on same faces. If False the method will NOT overwrite the existing interfaces on the same faces, but only create new interfaces.

### `apex.gendes.createDesignSpaceFromParts(target: apex.EntityCollection, boundingBoxType: apex.gendes.BoundingBoxType = apex.gendes.BoundingBoxType.ObjectAligned, boundingBoxOffsetType: apex.gendes.BoundingBoxOffsetType = apex.gendes.BoundingBoxOffsetType.Fixed, offset: float = 0.0, symmetric: bool = False, symmetryLocation: apex.ILocation = None, symmetryOrientation: apex.construct.Orientation = None, symmetricXY: bool = False, symmetricYZ: bool = False, symmetricXZ: bool = False, name: str = "DesignSpace", description: str = "") -> apex.gendes.DesignSpace`
Creates and returns a DesignSpace object from a collection of Parts or geometry bodies. The DesignSpace will have a cuboid shape, sized to completely enclose the input Parts / Bodies using a bounding box algorithm. Input arguments control whether the bounding box will be oriented with the global rectangular coordinate system or with the target Parts / bodies(object oriented). The bounding box may also be scaled to ensure some clearance between the boundary faces and the target Parts / Bodies. The DesignSpace and its associated geometry Solid will be created in a new Part. A symmetric DesignSpace may be requested using optional arguments.

- `target` — A collection of Parts and/or geometry Solids that will be used to determine the size, position and orientation of the DesignSpace. Any Parts in target will be internally expanded to the collection of geometry Bodies composed by each Part and combined with any geometry solids. Any duplicate geometry bodies from the resulting collection will be silently ignored and the DesignSpace will entirely enclose all of the remaining geometry Bodies.
- `boundingBoxType` — enumeration to determine whether the DesignSpace will be created based on a globally or object oriented bounding box around the target Parts/Bodies. The default apex.BoundingBoxType.ObjectAligned will cause the minimum possible volume DesignSpace to be created by allowing the orientation of the bounding box to be oriented to any direction. The optional apex.BoundingBoxType.Global will cause the minimum possible volume DesignSpace to be created while retaining the orientation of the bounding box to be remain aligned with the global rectangular axes.
- `boundingBoxOffsetType` — optional enumeration argument that controls how the base bounding box size is adjusted. The base bounding box is calculated such that it minimally encloses the target Parts/Bodies. This implies that the target will 'touch' each face of the bounding box in at least one location. In order to allow for some clearance between the bounding box and the target entities the method supports specification of an offset. This offset will be added to the base bounding box shape to provide some clearance between the target and the box. The offset may be specified to be a fixed offset (each face of the base bounding box will be offset by the same fixed distance on all size faces) or to be a proportional offset where the offset on pairs of opposite faces is determined y the distance between these faces multiple id by a scale factor. The default value of apex.BoundingBoxOffsetType.Fixed will cause the provided offset value to be used asa fixed offset on all six faces The optional apex.BoundingBoxOffsetType.Proportional value will cause the provided offset value to be used as a proportional offset
- `offset` — An optional float value specifying the amount of offset that will be added to the base bounding box. See the documentation for the boundingBoxOffsetType argument for a description of the base bounding box. If boundingBoxOffsetType is "Fixed" this value represents the distance by which each of the six faces of the base bounding box will be offset during creation of this DesignSpace. In this case, offset represent a unit of Length and must be provided in the units of Length in the active script unit system. If boundingBoxOffsetType is "Proportional" this value represents a factor that will be used in conjunction with the distance between pairs of opposing faces of the base bounding box to determine a different offset for each each of the three opposing pairs of base bounding box faces.
- `symmetric` — An optional boolean argument to specify whether a symmetric DesignSpace will be created. The default value of "False" will create a DesignSpace that does not support symmetry. Setting the value to "True" will create a DesignSpace that will support symmetry. The actual symmetry supported is dependent other input arguments.
- `symmetryLocation` — Optional argument that defines the origin of the DesignSpace symmetry planes. This argument is REQUIRED if symmetric is True. symmetryLocation represents Length quantities and must be defined using units of Length from the active script unit system.
- `symmetryOrientation` — optional argument defining the orientation of the symmetry planes using an Orientation object. This argument is REQUIRED if the symmetric argument is True.
- `symmetricXY` — optional Boolean argument (default = False) specifying whether the DesignSpace will be symmetric across the XY plane defined by the symmetryLocation and symmetryOrientation arguments. Set to True to specify DesignSpaces symmetry across the XY plane.
- `symmetricYZ` — optional Boolean argument (default = False) specifying whether the DesignSpace will be symmetric across the YZ plane defined by the symmetryLocation and symmetryOrientation arguments. Set to True to specify DesignSpace symmetry across the YZ plane.
- `symmetricXZ` — optional Boolean argument (default = False) specifying whether the DesignSpace will be symmetric across the XZ plane defined by the symmetryLocation and symmetryOrientation arguments. Set to True to specify DesignSpace symmetry across the XZ plane.
- `name` — An optional name for this DesignSpace. If omitted, the system will provide a default name using the prefix "Design Space " followed by a unique integer to ensure name uniqueness within the Model.
- `description` — An optional description for the DesignSpace. If omitted, the description will be left blank.

Returns: created DesignSpace.

### `apex.gendes.createDesignSpaceFromSolid(target: apex.geometry.Solid, scalingFactor: float = 1.0, symmetric: bool = False, symmetryLocation: apex.ILocation = None, symmetryOrientation: apex.construct.Orientation = None, symmetricXY: bool = False, symmetricYZ: bool = False, symmetricXZ: bool = False, name: str = "DesignSpace", description: str = "", targetSolidBehavior: apex.gendes.TargetSolidBehavior = apex.gendes.TargetSolidBehavior.KeepCurrent) -> apex.gendes.DesignSpace`
Creates and returns a DesignSpace object from a single geometry Solid that represents the full volume of the DesignSpace. The DesignSpace can optionally be scaled relative to the input Solid. The DesignSpace and the associated geometry Solid will be created in a new Part. A symmetric DesignSpace may be requested using optional arguments. If symmetry is created, a segment of the input Solid will be extracted and used as the master segment of the symmetric DesignSpace.

- `target` — The single geometry Solid that defines the shape of the DesignSpace. If a symmetric DesignSpace is requested, a portion of this input Solid will be used to define the master segment of the DesignSpace with the remaining volume generated through reflection(s) about the active symmetry plane(s).
- `scalingFactor` — An optional scaling factor that will be applied to the target Solid for creation of the DesignSpace. This is intended to support creation of a DesignSpace that is slightly larger than the target Solid to provide clearance, although specification of a negative offset can also be used to reduce the size of the DesignSpace relative to the target Solid. Note that in "CreateDesignSpaceFromSolid", this parameter only makes sense when symmetric is False.
- `symmetric` — An optional boolean argument to specify whether a symmetric DesignSpace will be created. The default value of "False" will create a DesignSpace that does not support symmetry. Setting the value to "True" will create a DesignSpace that will support symmetry. The actual symmetry supported is dependent other input arguments.
- `symmetryLocation` — Optional argument that defines the origin of the DesignSpace symmetry planes. This argument is REQUIRED if symmetric is True. symmetryLocation represents Length quantities and must be defined using units of Length from the active script unit system.
- `symmetryOrientation` — optional argument defining the orientation of the symmetry planes using an Orientation object. This argument is REQUIRED if the symmetric argument is True.
- `symmetricXY` — optional Boolean argument (default = False) specifying whether the DesignSpace will be symmetric across the XY plane defined by the symmetryLocation and symmetryOrientation arguments. Set to True to specify DesignSpaces symmetry across the XY plane.
- `symmetricYZ` — optional Boolean argument (default = False) specifying whether the DesignSpace will be symmetric across the YZ plane defined by the symmetryLocation and symmetryOrientation arguments. Set to True to specify DesignSpace symmetry across the YZ plane.
- `symmetricXZ` — optional Boolean argument (default = False) specifying whether the DesignSpace will be symmetric across the XZ plane defined by the symmetryLocation and symmetryOrientation arguments. Set to True to specify DesignSpace symmetry across the XZ plane.
- `name` — An optional name for this DesignSpace. If omitted, the system will provide a default name using the prefix "Design Space " followed by a unique integer to ensure name uniqueness within the Model.
- `description` — An optional description for the DesignSpace. If omitted, the description will be left blank.
- `targetSolidBehavior` — Enum argument to define the target solid behavior. Default behavior is "KeepCurrent", this will use the target solid as the design space solid and create design space in the current part. Setting this value to "Reparent" will force system to reuse the target solid as the design space solid and reparent it in "Design Part", with material, Loads and Boundary Condition retained on the design space solid. Setting this value to "Copy" will copy the target solid as design space solid in "Design Part", while the material, Loads and Boundary Condition are not retained on the design space solid.

Returns: created DesignSpace.

### `apex.gendes.createGDconfiguration(name: str = "#####", description: str = "", designSpaceInitial: apex.gendes.DesignSpace = None, nonDesignSpaces: apex.EntityCollection = None, retainedVolumes: apex.EntityCollection = None, excludedVolumes: apex.EntityCollection = None, accessRegions: apex.EntityCollection = None, clearanceRegions: apex.gendes.ClearanceRegionCollection = None, compoundInterfaces: apex.gendes.CompoundInterfaceCollection = None) -> apex.gendes.GDConfiguration`
Create a generative design configuration by assigning different "roles" to Apex Parts/Bodies. Note that at this time, the final design space is not created until the configuration is applied.

- `name` — The name of the GD Configuration.
- `description` — The description of the GD Configuration.
- `designSpaceInitial` — The design space that is used as the initial design, it will be subtracted and merged by other regions and volumes to create the final design space.
- `nonDesignSpaces` — The parts/solids/cells that will be used as nonDesignSpaces in the final design space.
- `retainedVolumes` — The parts/solids that will be used to carry and transfer loads to final design space.
- `excludedVolumes` — The parts/solids that will be subtracted from the initial design space.
- `accessRegions` — The parts/solids that will be subtracted from the initial design space.
- `clearanceRegions` — The clearance regions assigned in the configuration.
- `compoundInterfaces` — The compoundInterfaces assigned in the configuration.

Returns: created GDconfiguration.

### `apex.gendes.createNonDesignRegionDirectMethod(target: apex.geometry.CellCollection, name: str = "", description: str = "") -> apex.gendes.NonDesignRegion`
Creates and returns a non design region for use in generative design simulations. The extent of the non-design region is based on the input geometry Cells.

- `target` — one or more Cells as that define the non design region.
- `name` — an optional name for the NonDesignRegion. If omitted, Apex will provide a default unique name. If provided, the name must be unique within the scope of the Part that composes the NonDesignRegion.
- `description` — optional description for the NonDesignRegion.

### `apex.gendes.createNonDesignRegionOffsetMethod(target: apex.EntityCollection, targetFaces: apex.geometry.FaceCollection, offsetDistance: float = NAN, name: str = "", description: str = "") -> apex.gendes.NonDesignRegion`
Creates and returns a non design region for use in generative design simulations. The extent of the non-design region is based on the geometry Cell offsetting from faces.

- `target` — A collection of solids or cells to be split for non-design regions.
- `targetFaces` — the collection of geometry Faces/Surfaces that will be used to offset and split the target solid to apply non-design regions.
- `offsetDistance` — The distance by which the target Surfaces/Faces will be offset to generate the "virtual" Surfaces/Faces that will be used to perform the split for non-design region.
- `name` — an optional name for the NonDesignRegion. If omitted, Apex will provide a default unique name. If provided, the name must be unique within the scope of the Part that composes the NonDesignRegion.
- `description` — optional description for the NonDesignRegion.

### `apex.gendes.get(target: [{str:str}]) -> apex.EntityCollection`
Get a collection of Entities, specified by target list of key:value string dictionaries.

- `target` — list of dictionaries (string:string) specifying the Entities to retrieve. Each dictionary can identify one or more objects of a single apex type. Multiple dictionaries can be added to the list to enable retrieval of collections of different object types from this method. Each Dictionary contains either two or three keys from the following list of supported keys: string - "type" string - "path" [string] - "names" string - "ids" string - "indices"

Returns: an EntityCollection of the requested Entities

Retrieve a collection of Entities, specified by a target List of key:value Dictionaries. This method can retrieve combinations of objects of any Apex type that inherits from apex.Entity apex.EntityType string eliteral - for example "Part", "Surface", "Element" etc.path key The path key is required and is a string type. The associated value is also a string type that uniquely identifies a named Apex object (any objects that implements the IName interface) using the pathName of that object. If used without any other key, will return the named object identified by the path valueExample: EntityCollection containing the single "Solid 1" objectnames key An optional key of type string. The associated value is of type [string] - List of strings. Each string in the List represents the name of a named objects that is contained by the object identified by "path". The objects defined by "names" must exist within object defined by pathExample: apex.gendes.CompoundInterfaceCollection containing the two Interfaces - "CompoundInterface 3" and "CompoundInterface 5"Identifying multiple sub-entities The ids and indices key are used to identify objects that support ID's and Indices instead of names - these entity types are referred to as sub-entities. Nodes and Elements are sub-entities of MeshBodies. Cells, Faces, Edges and Vertices are sub-entities of GeometryBodies.Example: The pattern for IDs is exactly the same (use the "ids" key instead of the "indices' key). Queries based on Indices are usually much faster than Ids, and are preferred if you don't care about the IDs. Both the ids and indices values are strings and can be run length encoded for compactness. "ids":"1-5000, 5002-5005, 5009, 50013, 60000-1000000"

### `apex.gendes.getClearanceRegion(pathName: str = "") -> apex.gendes.ClearanceRegion`
get an existing clearance region object.

- `pathName` — the path name of the clearance region object.

### `apex.gendes.getCompoundInterface(pathName: str = "") -> apex.gendes.CompoundInterface`
get an existing compound interface object.

- `pathName` — the path name of the interface object

### `apex.gendes.getDesignSpace(pathName: str) -> apex.gendes.DesignSpace`
Get a DesignSpace in a model.

- `pathName` — PathName of the DesignSpace to get including the model name as in 'MyModel/Design Part/DesignSpace 1'.

Returns: created DesignSpace

### `apex.gendes.getGDConfiguration(pathName: str) -> apex.gendes.GDConfiguration`
Get a GDConfiguration by name.

- `pathName` — PathName of the GDConfiguration to get including the model name as in 'MyModel/Design Part/GDConfiguration 1'.

Returns: created GDConfiguration

### `apex.gendes.getNonDesignRegion(pathName: str) -> apex.gendes.NonDesignRegion`
get an existing NonDesignRegion

- `pathName` — of the new NonDesignRegion.

### `apex.gendes.setDesignTarget(pathName: str) -> None`
Set the design target in the Optimization. Note that in 2021 release, only part can be set as design target. In later release, we will support AssemblyRep as the design target.Get a DesignSpace in a model. For example: ~~~~~~~~~~~~~{.py} apex.gendes.setDesignTarget(pathName=r'MyModel/Assembly1/Part1') ~~~~~~~~~~~~~.

- `pathName` — The full path name of the object which is set as design target. For example, 'MyModel/Assembly 1/ Part 1' is the valid path name of a part.

## Classes in this module

Full method signatures are in `api/classes/apex.gendes.md`.

`ClearanceRegion`, `ClearanceRegionCollection`, `CompoundInterface`, `CompoundInterfaceCollection`, `DesignSpace`, `DesignSpaceCollection`, `GDConfiguration`, `GDConfigurationCollection`, `NonDesignRegion`, `NonDesignRegionCollection`

