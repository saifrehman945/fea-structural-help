# apex.gendes — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.gendes.ClearanceRegion`  (extends `Entity`, `IDisplayable`, `ILocation`, `IName`)
ClearanceRegion Class Object when an existing nominal design CAD model is used to represent retained parts and a Boolean operation is used to remove the volumes of the retained parts from the design space. In this situation it is sometimes required to add a 'clearance region" around the volumes of the retained parts to ensure that the retained parts can be assembled onto the consolidate part. In this case, the clearance region actually reduces the design space.
Properties: `location`, `offsetDistance`

Methods:

- `getLocation() -> apex.Coordinate` — getLocation of ClearanceRegion is not supported yet, it will be supported in feature release.
- `getOffsetDistance() -> float` — returns the offsetDistance of this ClearanceRegion.
- `getTargetFaces() -> apex.geometry.FaceCollection` — returns the targetFaces of this ClearanceRegion.
- `setOffsetDistance(offsetDistance: float) -> None` — set the offsetDistance of this ClearanceRegion.
#### `update(name: str = "", description: str = "", offsetDistance: float = 0.0, targetFaces: apex.EntityCollection = None) -> None`
it's used to modify the created clearance region. Either the name, description, offsetDistance, targetFaces can be updated in one update call.

- `name` — the name of the clearance region.
- `description` — the description of the clearance region.
- `offsetDistance` — it's used to defined how much distance the clearance region is.
- `targetFaces` — it's used to defined which target faces user want to select to applied the clearance region.


## `apex.gendes.ClearanceRegionCollection`  (extends `ILocationCollection`)
An iterable collection of Clearance Region objects, based on EntityCollection.

Methods:

- `ClearanceRegionCollection() -> None` — Construct a new ClearanceRegionCollection.
#### `appendList(clearanceRegionList: [apex.gendes.ClearanceRegion]) -> None`
Add ClearanceRegions from a list to the end of this collection.

- `clearanceRegionList` — list of ClearanceRegions to add to the collection.

For example:


## `apex.gendes.CompoundInterface`  (extends `Entity`, `IDisplayable`, `IPhysical`, `IName`)
Class compound interface represents an compound interface object in generative design model. Many loads and boundary conditions are directly applied on the model regions, this usually leads to unreasonable optimization shapes. Applying them on the interface will ensure these application regions are well preserved during optimization and the design shape is printable. CompoundInterface is created on connected faces, and system will create the compound interface volume on the connected faces according to user input. The connected faces may be extended by the offsetDistance if user specifies the parameter - this will enlarge the scope of compound interface.
Properties: `machiningAllowance`, `nonDesignSpaceThickness`, `offsetDistance`, `target`

Methods:

- `getMachiningAllowance() -> float` — returns the machiningAllowance of this CompoundInterface.
- `getNonDesignSpaceThickness() -> float` — returns the nonDesignSpaceThickness of this CompoundInterface.
- `getOffsetDistance() -> float` — returns the offsetDistance of this CompoundInterface.
- `getTarget() -> apex.EntityCollection` — returns the target of this CompoundInterface.
#### `update(name: str = "####", description: str = "####", nonDesignSpaceThickness: float = NAN, machiningAllowance: float = NAN, offsetDistance: float = NAN, target: apex.EntityCollection = None) -> None`
Updates this interface. One or more properties may be updated in each call to update().

- `name` — Updates the name.
- `description` — Updates the description..
- `nonDesignSpaceThickness` — Updates the nonDesignSpaceThickness.
- `machiningAllowance` — Updates the machiningAllowance.
- `offsetDistance` — Updates the offsetDistance.
- `target` — Updates the target.


## `apex.gendes.CompoundInterfaceCollection`  (extends `ILocationCollection`)
An iterable collection of CompoundInterface objects, based on EntityCollection.

Methods:

- `CompoundInterfaceCollection() -> None` — Construct a new CompoundInterfaceCollection.
#### `appendList(interfaceList: [apex.gendes.CompoundInterface]) -> None`
Add CompoundInterfaces from a list to the end of this collection.

- `interfaceList` — list of CompoundInterfaces to add to the collection.

For example:


## `apex.gendes.DesignSpace`  (extends `Entity`, `IPhysical`, `IName`, `IDisplayable`, `IUserAttributes`)
Class representing a DesignSpace for generative design optimizations. DesignSpaces reference and are generatively dependent upon a single associated geometry Solid. DesignSpaces can be configured to support symmetry about one, two or three orthogonal planes. When configured to support symmetry the referenced Solid represents the "master segment" of the DesignSpace with the full extend of the DesignSpace generated through reflection of the associated Solid about the active DesignSpace symmetry planes.
Properties: `colorRGB`, `designSpaceSolid`, `edgeWeight`, `highlighted`, `location`, `nonDesignRegionAssociated`, `pointSize`, `symmetricXY`, `symmetricXZ`, `symmetricYZ`, `symmetryLocation`, `symmetryOrientation`

Methods:

#### `getDesignSpaceSolid() -> apex.geometry.Solid`
The solid body that defines the design space volume which is internally sent to the generative design solver. It also includes non-design region cells. For symmetric DesignSpaces, the design space solid is the master region solid and the solver will mirror-copy the design space solid about the DesignSpace active symmetry planes to get the complete design space volume.

Returns: the Master Solid.

#### `getFullSpaceSolidWithMA() -> apex.geometry.Solid`
Returns a newly created geometry equal to the original DesignSpace plus all attached MAs. If no MA attached, there will be an error returned.

Returns: the FullSpaceSolidWithMA.

- `getLocation() -> apex.Coordinate` — getLocation of DesignSpace is not supported yet, it will be supported in feature release.
#### `getNonDesignRegionAssociated() -> apex.gendes.NonDesignRegionCollection`
NonDesignRegionCollection associated with the DesignSpace, that cannot be modified or reduced by the generative design solver. The resulting shape generated by the solver will ALWAYS include these regions. It includes all NonDesignRegion objects associated with the DesignSpace.

Returns: the NonDesignRegionCollection associated with the Master Solid.

#### `getSymmetricXY() -> bool`
Boolean property indicating whether the DesignSpace supports symmetry about the XY plane or not. Returns True if the DesignSpaces symmetry across the XY plane, False otherwise.

Returns: the SymmetricXY.

#### `getSymmetricXZ() -> bool`
Boolean property indicating whether the DesignSpace supports symmetry about the XZ plane or not. Returns True if the DesignSpace supports symmetry across the XZ plane, False otherwise.

Returns: the SymmetricXZ.

#### `getSymmetricYZ() -> bool`
Boolean property indicating whether the DesignSpace supports symmetry about the YZ plane or not. Returns True if the DesignSpace supports symmetry across the YZ plane, False otherwise.

Returns: the SymmetricYZ.

#### `getSymmetryLocation() -> apex.ILocation`
The location of the origin of the DesignSpace as an ILocation. If the DesignSpace does not support symmetry, symmetryLocation is None.

Returns: the SymmetryLocation.

#### `getSymmetryOrientation() -> apex.construct.Orientation`
The orientation of the DesignSpace symmetry planes as an Orientation. If the DesignSpace does not support symmetry, symmetryOrientation is None.

Returns: the SymmetryOrientation.

- `getTarget() -> apex.geometry.Cell`
- `setParam(valParam: msc.apex.appfw.CmdParameter) -> None`
#### `update(name: str, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this DesignSpace. One or more properties may be updated in each call to update().

- `name` — Update the name of this DesignSpace.
- `color` — Update color of this DesignSpace.
- `renderStyle` — Update renderStyle of this DesignSpace
- `enableTransparency` — Enable or disable transparency of this DesignSpace.
- `transparencyLevel` — Update transparencyLevel of this DesignSpace.


## `apex.gendes.DesignSpaceCollection`  (extends `ILocationCollection`)
Iterable collection of DesignSpaces, based on EntityCollection.

Methods:

- `DesignSpaceCollection() -> None` — Construct a new DesignSpaceCollection.
#### `appendList(DesignSpaceList: [apex.gendes.DesignSpace]) -> None`
Add DesignSpaces from a list to the end of this collection.

- `DesignSpaceList` — list of DesignSpaces to add to the collection.

For example:


## `apex.gendes.GDConfiguration`  (extends `Entity`, `IName`, `IDisplayable`, `IUserAttributes`)
Class that associates Apex Parts/Bodies with specific Generative Design "roles" and subsequently performs a series of Boolean operations to generate a DesignSpace solid that reflects the role assignments.
Properties: `accessRegions`, `clearanceRegions`, `compoundInterfaces`, `designSpaceFinal`, `designSpaceInitial`, `excludedVolumes`, `nondesignSpaces`, `retainedVolumes`

Methods:

- `applyConfiguration() -> None` — Perform the boolean operations based on the selected entities in the configuration. If it succeeds, then the final design space will be created and added into the updated configuration.
#### `getAccessRegions() -> apex.EntityCollection`
An EntityCollection of parts/solids that are created for the fasteners assembling spaces. They are not the existing parts of the model, but representing the void spaces that occupied by the fasteners or the extra volume used for assembling purpose.

Returns: the AccessRegions.

#### `getClearanceRegions() -> apex.gendes.ClearanceRegionCollection`
The ClearanceRegions specified in the configuration. They will be subtracted from the initial design space.

Returns: the ClearanceRegions.

#### `getCompoundInterfaces() -> apex.gendes.CompoundInterfaceCollection`
The compound interfaces specified in the configuration. They will be boolean with the final design space.

Returns: the Interfaces.

#### `getDesignSpaceFinal() -> DesignSpace`
The final design space derived from the configuration. It's only created after user applies the configuration.

Returns: the DesignSpaceFinal.

#### `getDesignSpaceInitial() -> DesignSpace`
The design space specified as the initialDesignSpace in this configuration. In the first release, system will ignore the symmetry design on the design space, but only references the solid.

Returns: the DesignSpace.

#### `getExcludedVolumes() -> apex.EntityCollection`
An EntityCollection of parts/solids that excluded from the initial design space, while they are not the design target. They will be subtracted from the initial design space to ensure that final resulting shape does not interference with the excludedVolumes.

Returns: the ExcludedVolumes.

#### `getNondesignSpaces() -> apex.EntityCollection`
An EntityCollection containing all parts/solids that represent non-design regions in this GDConfiguration. All solids in this region will be merged as cells with the InitialDesignSpace.

Returns: the NondesignSpaces.

#### `getRetainedVolumes() -> apex.EntityCollection`
An EntityCollection of parts/solids that carry and transfer loads in the generative design optimization, they cannot be modified or reduced by the generative design solver. The resulting shape generated by the solver will ALWAYS exclude these regions.

Returns: the RetainedVolumes.

#### `update(name: str = "#####", description: str = "#####", designSpaceInitial: apex.gendes.DesignSpace = None, nonDesignSpaces: apex.EntityCollection = None, retainedVolumes: apex.EntityCollection = None, excludedVolumes: apex.EntityCollection = None, accessRegions: apex.EntityCollection = None, clearanceRegions: apex.gendes.ClearanceRegionCollection = None, compoundInterfaces: apex.gendes.CompoundInterfaceCollection = None) -> None`
Update this GDConfiguration. One or more properties may be updated in each call to update().

- `name` — The name of the GD Configuration.
- `description` — The description of the GD Configuration.
- `designSpaceInitial` — Update the initialDesignSpace of this GenerativeDesignConfiguration.
- `nonDesignSpaces` — Update the nonDesignRegion of this GenerativeDesignConfiguration.
- `retainedVolumes` — Update the retainedRegion of this GenerativeDesignConfiguration.
- `excludedVolumes` — Update the exclusionVolumes of this GenerativeDesignConfiguration.
- `accessRegions` — Update the accessRegions of this GenerativeDesignConfiguration.
- `clearanceRegions` — Update the clearanceRegions of this GenerativeDesignConfiguration.
- `compoundInterfaces` — Update the compoundInterfaces of this GenerativeDesignConfiguration.


## `apex.gendes.GDConfigurationCollection`  (extends `ILocationCollection`)
Iterable collection of GDConfigurations, based on EntityCollection.

Methods:

- `GDConfigurationCollection() -> None` — Construct a new GDConfigurationCollection.
#### `appendList(GDConfigurationList: [apex.gendes.GDConfiguration]) -> None`
Add GDConfigurations from a list to the end of this collection.

- `GDConfigurationList` — list of GDConfigurations to add to the collection.

For example:


## `apex.gendes.NonDesignRegion`  (extends `Entity`, `IPhysical`, `IName`, `IDisplayable`)
NonDesignRegion.
Properties: `target`

Methods:

- `getLocationInternal() -> apex.LocationInternal`
- `getTarget() -> apex.geometry.Cell`

## `apex.gendes.NonDesignRegionCollection`  (extends `ILocationCollection`)
Iterable collection of NonDesignRegions, based on EntityCollection.

Methods:

- `NonDesignRegionCollection() -> None` — Construct a new NonDesignRegionCollection.
#### `appendList(nonDesignRegionList: [apex.gendes.NonDesignRegion]) -> None`
Add NonDesignRegions from a list to the end of this collection.

- `nonDesignRegionList` — list of NonDesignRegions to add to the collection.

For example:


