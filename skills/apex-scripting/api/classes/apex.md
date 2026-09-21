# apex — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.Assembly`  (extends `Entity`, `IPhysical`, `IDisplayable`, `IUserAttributes`, `IName`, `IActivatable`)
model object that can contain Parts and other Assemblies. Create using Model or Assembly createAssembly() method.
Properties: `assemblies`, `assemblyReps`, `axisAlignedBoundingBox`, `datumPlanes`, `displayableEntities`, `elements`, `exclusiveRegions`, `interfacePoints`, `model`, `namedEntities`, `nodes`, `parent`, `partialRegions`, `parts`, `physicalEntities`

Methods:

#### `applyColorToChildren(color: [int]) -> None`
applies the color of this Assembly to all its children.

- `color` — 3 vector(list) specifying the Red, Green, and Blue component of the color. Each value should be in the range 0-255.

This method provides the ability to set the parent container's setting to all children settings. This method actually changes the childrens' settings, not just their display in 3D Graphics.

#### `applyRenderStyleToChildren(renderStyle: apex.session.DisplayRenderStyle) -> None`
applies the Render Style of this Assembly to all its children.

- `renderStyle` — is the enumeration for the render style.

This method provides the ability to set the parent container's setting to all children settings. This method actually changes the childrens' settings, not just their display in 3D Graphics.

#### `applyTransparencyToChildren(enableTransparency: bool, transparencyLevel: int) -> None`
applies the Transparency setting of this Assembly to all its children.

- `enableTransparency` — Boolean to enable setting transparency. Default: False
- `transparencyLevel` — The Transparency Level. This is an integer representing the transparency value from 0 (No Transparency) to 100 (Completely Transparent). Any value specified less than 0 will be treated as 0. Any value greater than 100 will be treated as 100. This value is required if enableTransparency is set to True.

This method provides the ability to set the parent container's setting to all children settings. This method actually changes the childrens' settings, not just their display in 3D Graphics.

#### `asEntity() -> Entity`
return the (base) Entity Object of this Assembly.

Returns: this assembly Entity object

#### `createAssembly(name: str = "") -> Assembly`
Create a new Assembly that is child of this Assembly.

- `name` — of the new assembly. default = "" (auto-named)

Returns: the created Assembly

#### `createAssemblyRep(name: str, description: str = "") -> apex.AssemblyRep`
Create an Assembly Rep from this Assembly.

- `name` — of the Assembly Rep.
- `description` — of Assembly Rep.

Returns: the newly created Assembly Rep object

#### `createPart(name: str = "") -> Part`
Create a new Part that is child of this Assembly.

- `name` — of the new part. default = "" (auto-named)

Returns: the created Part

#### `deleteAssemblyRep(assemblyRep: apex.AssemblyRep) -> None`
Deletes an Assembly Rep from an Assembly. If the target AssemblyRep does not exist in this Assembly the method will ignore the input.

- `assemblyRep` — objet to be deleted.

- `delete_RENAMED_AFTER_SWIG() -> None` — Delete this Assembly.
#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports the contents of the Assembly to a Nastran file. All objects in the Assembly that can be mapped to Nastran keywords will be exported. Only bulk data entries are exported when this method is called from the Assembly class - to export Case (and other Nastran file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single flat file. The default value of "False" causes a single file to be written containing all of the finite element entities within the Assembly to be written.
- `renumberMethod` — An enumeration to control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Assembly Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "apex.attributes.ExportRenumberMethod.internal" causes the renumbering operation to carried out and persisted in the Apex Model. "apex.attributes.ExportRenumberMethod.export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

#### `exportGeometry(filename: str, cadFormat: apex.geometry.CADFormat, unitSystem: str = "m", stlMergeCells: bool = True, exportVirtualFaces: bool = False, exportVirtualFaceMethod: apex.VirtualFaceExportMethod = apex.VirtualFaceExportMethod.NurbsOnly, exportBodyPositionInLocal: bool = False) -> None`
Export Geometry from this assembly to a file using the supplied CAD format.

- `filename` — Fully qualified name of the file to which the geometry objects will be exported.
- `cadFormat` — defines the format of the CAD file that will be exported using an apex.geometry.CADFormat enumeration.
- `unitSystem` — A string to identify the units to be used during export. Unit support is dependent on the CADFormat of the exported file and not all formats support units. Of the CAD formats currently supported by Apex, only the IGES format supports user defined export units. The table below shows each of the supported unit systems and associated unitSystem values for IGES export CAD Format - Length unit - unitSystem value IGES Kilometer km Meter m Centimeter cm Millimeter mm Micrometer um Mile mile Foot ft Inch in Milliinch mi Microinch ui If the IGES format is selected, unitSystem must be provided. If a value other than one in the above table is supplied, the method will throw an exception
- `stlMergeCells` — optional Boolean argument (default = True) that controls how multi-cellular solids will be represented in STL files. This argument is only relevant when the cadFormat type is an STL type and is silently ignored for all other formats. When True (Default), all cells in a multi-cellular solid will be merged into a single cell during export by removing all internal Faces. The GeometryBody is unaffected by this operation. When False, all cells in multi-cellular solids will be present in the exported STL file.
- `exportVirtualFaces` — Optional Argument, Default = False, where each virtual faces will be exported as a single face. This only applies to CAD Format Parasolid. The purpose is to export geometry topology that is consistent with native Apex to maintaining associatively with mesh, loads, BCs and other attributes. An attempt will be made to export the virtual faces as NURBS, by replacing the each virtual face with a single NURBS face. If this fails, then a facet body face will be used instead.
- `exportVirtualFaceMethod` — This applies to exportGeometry API only. It controls what is permitted for converting virtual topology to exportable faces with the same topology. This is ignored if exportVirtualFaces is False. If set to NurbsAndFaceted, then the system will try to convert to NURBS, and if that fails, it will then convert the face into a faceted face. If set to NurbsOnly (Default), then it will try to convert each virtual face to NURBS only.
- `exportBodyPositionInLocal` — Optional Boolean argument to export the geometry body in local position based the reference system of the body and parent part. By default, it is false. The system will export the geometry body position in global.

#### `exportMarc(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False) -> None`
Exports the contents of the Assembly to a Marc file. All objects in the Assembly that can be mapped to Marc keywords will be exported. Only bulk data entries are exported when this method is called from the Assembly class - to export Case (and other Marc file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single flat file. The default value of "False" causes a single file to be written containing all of the finite element entities within the Assembly to be written.
- `renumberMethod` — An enumeration to control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Assembly Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "apex.attributes.ExportRenumberMethod.internal" causes the renumbering operation to carried out and persisted in the Apex Model. "apex.attributes.ExportRenumberMethod.export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.

#### `getAssemblies(recursive: bool = False) -> apex.AssemblyCollection`
Get all Assemblies in this Assembly.

Returns: Iterable collection of all the Assemblies in this Assembly

getAssemblies() may also be accessed as an Assembly object property 'assemblies'. For example:

#### `getAssembly(name: str) -> Assembly`
Get an Assembly in this Assembly.

- `name` — of the assembly to get..

Returns: the Assembly

#### `getAssemblyRep(name: str) -> apex.AssemblyRep`
get an Assembly Rep by name

- `name` — of Assembly Rep objet.

#### `getAssemblyReps() -> apex.AssemblyRepCollection`
get all Assembly Reps from this Assembly.

Returns: all the named Assembly Reps of this Assembly.

#### `getDatumPlane(name: str) -> apex.construct.DatumPlane`
Retrieves a DatumPlane that is a direct child of this Assembly using the supplied name.

- `name` — The name of the DatumPlane to retrieve.

Returns: the DatumPlane

#### `getDatumPlanes(recursive: bool = False) -> apex.construct.DatumPlaneCollection`
Retrieves all DatumPlanes directly composed by this Assembly and returns them in a DatumPlaneCollection.

- `recursive` — Optional Boolean argument (Default = False) that determines whether only DatumPlanes composed directly by this Assembly will be returned or if the assembly will searched recursively and all DatumPlanes in the Assembly hierarchy will be returned.

Returns: the DatumPlaneCollection

An optional "recursive" argument enables the method to return all DatumPlanes composed by Parts or (Sub)Assemblies within this Assembly hierarchy. Assembly hierarchy.

#### `getDisplayableEntities() -> apex.EntityCollection`
returns a collection of all entities in this Assembly that implement IDisplayable as an EntityCollection.

Returns: this Entity objects

The Assembly hierarchy is traversed recursively and all entities in the hierarchy that implement IDisplayable are returned.

#### `getElements() -> apex.mesh.ElementCollection`
Get all elements in this Assembly.

Returns: Iterable collection of all the elements in this part

#### `getExclusiveRegions() -> apex.RegionCollection`
returns a RegionCollection of all Regions that exclusively reference ONLY Entities composed by Parts within this Assembly hierarchy. To return Regions that reference at least one Entity that is composed by a Part within this Assembly hierarchy use the partialRegions property instead.

Returns: a RegionCollection of all Regions that exclusively reference ONLY Entities composed by Parts within this Assembly hierarchy.

#### `getInterfacePoints() -> apex.attribute.InterfacePointCollection`
returns a read only collection of all InterfacePoints composed by this Assembly

Returns: a reference to the apex.attribute.InterfacePointCollection object

#### `getModel() -> Model`
Return the parent Model of this Assembly.

Returns: parent Model of this Assembly

#### `getNamedEntities() -> apex.EntityCollection`
returns a collection of all entities in this Assembly that implement IName as an EntityCollection.

Returns: this Entity objects

The Assembly hierarchy is traversed recursively and all entities in the hierarchy that implement IName are returned.

#### `getNodes() -> apex.mesh.NodeCollection`
Get all nodes in this Assembly.

Returns: Iterable collection of all the nodes in this part

#### `getParent() -> Assembly`
Get the parent Assembly for this Assembly.

Returns: The parent Assembly

getParent() may also be accessed as an Assembly object property 'parent'. For example:

#### `getPart(name: str) -> Part`
Get a Part in this Assembly.

- `name` — of the part to get..

Returns: the Part

#### `getPartialRegions() -> apex.RegionCollection`
returns a RegionCollection of all Regions that reference at least one Entity that is composed by a Part within this Assembly hierarchy. To return Regions that exclusively reference ONLY Entities composed by Parts within this Assembly hierarchy use the exclusiveRegions property instead.

Returns: a RegionCollection of all Regions that reference at least one Entity that is composed by a Part within this Assembly hierarchy.

#### `getParts(recursive: bool = False) -> apex.PartCollection`
Get all Parts in this Assembly.

Returns: Iterable collection of all the Parts in this Assembly

getParts() may also be accessed as an Assembly object property 'parts'. For example:

#### `getPhysicalEntities() -> apex.EntityCollection`
returns a collection of all entities in this Assembly that implement IName as an EntityCollection.

Returns: this Entity objects

The Assembly hierarchy is traversed recursively and all entities in the hierarchy that implement ILocation are returned.

#### `importGeometryAsParts(geometryFileNames: [str], importSolids: bool = True, importSurfaces: bool = True, importCurves: bool = True, importPoints: bool = True, importGeneralBodies: bool = True, importDatumPlanes: bool = False, importHiddenGeometry: bool = False, cleanOnImport: bool = True, removeRedundantTopoOnImport: bool = True, loadCompleteTopology: bool = True, sewOnImport: bool = False, importReviewMode3dxmlCleanOnImport: bool = True, importReviewMode3dxmlSplitOnFeatureVertexAngle: bool = True, importReviewMode3dxmlFeatureAngle: float = 40.0, importReviewMode3dxmlVertexAngle: float = 40.0, importReviewMode3dxmlDetectMachinedFaces: bool = False, importPublications: bool = False, importAttributes: bool = False) -> {str:apex.EntityCollection}`
Imports a target CAD model from the input CAD files into the target assembly. All parts of input CAD files will be imported to the target assembly by flattening the model structure. The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of geometry file. The apex.EntityCollection contains parts imported to the target assembly from geometry files.

- `geometryFileNames` — A List of the path qualified file geometry file names.
- `importSolids` — Optional boolean argument to control whether Solid geometry types will be Imported or ignored. The default value of "True" will cause all Solid geometry to be imported. Setting to False will cause Solid geometry to be ignored (Not imported).
- `importSurfaces` — Optional boolean argument to control whether Surface geometry types will be Imported or ignored. The default value of "True" will cause all Surface geometry to be imported. Setting to False will cause Surface geometry to be ignored (Not imported).
- `importCurves` — Optional boolean argument to control whether Curve geometry types will be Imported or ignored. The default value of "True" will cause all Curve geometry to be imported. Setting to False will cause Curve geometry to be ignored (Not imported).
- `importPoints` — Optional boolean argument to control whether Point geometry types will be Imported or ignored. The default value of "True" will cause all Point geometry to be imported. Setting to False will cause Point geometry to be ignored (Not imported).
- `importGeneralBodies` — Optional boolean argument to control whether GeneralBody (Non-manifold Surfaces) geometry types will be Imported or ignored. The default value of "True" will cause all GeneralBody geometry to be imported. Setting to False will cause GeneralBody geometry to be ignored (Not imported).
- `importDatumPlanes` — Optional boolean argument to control whether Datum Planes will be Imported or ignored. The value of "True" will cause all Datum Planes to be imported. Setting to False will cause Datum Planes to be ignored (Not imported).
- `importHiddenGeometry` — Optional boolean argument to control whether geometry that is marked as hidden in geometry file will be Imported or ignored. The default value of "True" will cause all geometry to be imported visible or hidden. Setting to False will cause any geometry that is marked as hidden in the geometry file to be ignored (Not imported).
- `cleanOnImport` — Optional boolean argument to control whether the imported geometry will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is".
- `removeRedundantTopoOnImport` — Optional boolean argument to control whether the imported geometry will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is".
- `loadCompleteTopology` — Optionally "load complete topology" geometry as part of the import operation. Default = True.
- `sewOnImport` — Optionally "Sew" geometry edges as part of the import operation. Default = False.
- `importReviewMode3dxmlCleanOnImport` — Optional boolean argument to control whether the imported review mode 3dxml file will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is".
- `importReviewMode3dxmlSplitOnFeatureVertexAngle` — optional argument used to control the creation of faceted geometry bodies by taking account the feature and vertex angle, the default is True. If it is set as false, then the arguments of "importReviewMode3dxmlFeatureAngle" and "importReviewMode3dxmlVertexAngle" will be ignored.
- `importReviewMode3dxmlFeatureAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry edges will be created between any faces of the 3dxml data that have subtended angles greater than this value. featureAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `importReviewMode3dxmlVertexAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry vertices will be created between any edges of the 3dxml data that have subtended angles greater than this value. vertexAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `importReviewMode3dxmlDetectMachinedFaces` — This is an optional argument. When on, this triggers an algorithm to search for possible machined faces. When found, these will be split into separate faces. The types of faces that can be found are planar, cylinder, and torus faces. Depending on the smoothness and accuracy of the input tessellation, these will be detected and partitioned into separate faces. The intended use case is a model with mostly organic faces that as some analytical faces machined into it. For models that come primarily from analytical faces, such as STL from CAD or STL from FEM meshes that were applied to CAD, it is better to import as Mesh, then use the facet body tool in Apex to convert to facet bodies and optionally NURBS. It will be ignored if the argument "importReviewMode3dxmlSplitOnFeatureVertexAngle" is set as True.
- `importPublications` — Optionally import the Publications from Catia V5 and 3D Experience files. Default = False.
- `importAttributes` — Optional boolean argument that defines whether the attributes of the target CAD files will be imported into Apex. If False (Default), the attributes in the CAD files will be ignored during import. If True, the method will import the attributes in the CAD files and convert them as Apex User Attributes after import. In 2021.2 release, Apex supports the following attributes: Parasolid System Attributes: body_density and colour,Parasolid Attributes, Catia V5 Properties and 3D Experience Properties.

Returns: The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of geometry file. The apex.EntityCollection contains parts imported to the target assembly from geometry files.

#### `importSTLAsParts(stlFileNames: [str], importBodyType: apex.geometry.STLImportBodyType = apex.geometry.STLImportBodyType.Mesh, featureAngle: float = 40.0, vertexAngle: float = 40.0, detectMachinedFaces: bool = False, splitOnAngle: bool = True, unitSystem: str = "m", cleanOnImport: bool = True) -> {str:apex.EntityCollection}`
Imports one or more STL files into this model and creates either mesh or geometry bodies depending on the supplied input values. All parts created from STL files will be imported into the target assembly. One mesh or geometry body will be created from each set of contiguous faces/lines in each STL file. If a set of contiguous faces in the STL file represents a watertight set and the the system will create an importBodyType is Facet, the system will create a facetted Solid body, otherwise the system will create a facetted Surface. The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of STL file. The apex.EntityCollection contains parts imported to the target assembly from STL files.

- `stlFileNames` — List of fully qualified path names of the STL files to be imported.
- `importBodyType` — An enumeration defining the type of Apex body that will be created from the STL data. STL data can be used to create either mesh or facetted geometry bodies based on the value of this argument. The default value of apex.geometry.STLImportBodyType.Mesh will cause the creation of MeshBodies from the STL data. Setting the value of this argument to apex.geometry.STLImportBodyType.Faceted will cause the system to create faceted geometry bodies.
- `featureAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry edges will be created between any faces of the STL data that have subtended angles greater than this value. This argument will be silently ignored if importBodyType is set to Mesh. featureAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `vertexAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry vertices will be created between any edges of the STL data that have subtended angles greater than this value. This argument will be silently ignored if importBodyType is set to Mesh. vertexAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `detectMachinedFaces` — This is an optional argument. When on, this triggers an algorithm to search for possible machined faces. When found, these will be split into separate faces. The types of faces that can be found are planar, cylinder, and torus faces. Depending on the smoothness and accuracy of the input tessellation, these will be detected and partitioned into separate faces. This only applies to STL imported as facet body. If imported as mesh this is ignored. The intended use case is a model with mostly organic faces that as some analytical faces machined into it. For models that come primarily from analytical faces, such as STL from CAD or STL from FEM meshes that were applied to CAD, it is better to import as Mesh, then use the facet body tool in Apex to convert to facet bodies and optionally NURBS.
- `splitOnAngle` — Optional argument used to control the creation of faceted geometry bodies. Default = True. Topological geometry edges and vertices will be created according to featureAngle and vertexAngle value. This argument will be silently ignored if importBodyType is set to Mesh.
- `unitSystem` — A string to identify the units to be used during import STL. unitSystem value can be m, cm, mm, ft or in.
- `cleanOnImport` — Optionally "Clean" geometry as part of the import operation. Default = True.

Returns: The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of STL file. The apex.EntityCollection contains parts imported to the target assembly from STL files.

#### `setParent(parent: Assembly) -> None`
Set an Assembly to be the new parent for this Assembly.

- `parent` — to be assigned the new parent of this Assembly

- `unsetColor() -> None` — unapplies the color of this Assembly to all its children.
- `unsetRender() -> None` — unapplies the renderStyle of this Assembly to all its children.
#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this Assembly properties.

- `name` — of this Assembly
- `parent` — of this Assembly
- `color` — of this Assembly
- `renderStyle` — of this Assembly
- `enableTransparency` — of this Assembly
- `transparencyLevel` — of this Assembly

One or more parameters can be updated in one update call.


## `apex.AssemblyCollection`  (extends `IPhysicalCollection`)
Iterable collection of Assemblies, based on IPhysicalCollection.

Methods:

- `AssemblyCollection() -> None` — Construct a new AssemblyCollection.
#### `appendList(assemblyList: [Assembly]) -> None`
Add Assemblies from a list to the end of this collection.

- `assemblyList` — list of Assemblies to add to the collection.

For example:


## `apex.AssemblyRep`  (extends `ModelRep`, `IName`)
Assembly representation objects.
Properties: `exclusiveGroups`, `exclusiveRegions`, `partialGroups`, `partialRegions`, `parts`, `targets`

Methods:

#### `add(target: apex.Entity = None, targets: apex.EntityCollection = None) -> None`
adds Assembly/ AssemblyRep/ Part/ apex.attribute.MeshDependentTie/ apex.attribute.DiscreteTie to an AssemblyRep

- `target` — a single target to be added to the current AssembyRep.
- `targets` — collection targets to be added to the current AssemblyRep.

#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports the contents of the AssemblyRep to a Nastran file. All objects in the AssemblyRep that can be mapped to Nastran keywords will be exported. Only bulk data entries are exported when this method is called from the Assembly class - to export Case (and other Nastran file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single flat file. The default value of "False" causes a single file to be written containing all of the finite element entities within the Assembly to be written.
- `renumberMethod` — An enumeration to control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Assembly Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "apex.attributes.ExportRenumberMethod.internal" causes the renumbering operation to carried out and persisted in the Apex Model. "apex.attributes.ExportRenumberMethod.export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

#### `exportMarc(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, inputType: apex.attribute.MarcInputType = apex.attribute.MarcInputType.Dat, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, apexEngineeringAbstractions: bool = False) -> None`
Exports the contents of the AssemblyRep to a Marc file. All objects in the AssemblyRep that can be mapped to Nastran keywords will be exported. Only bulk data entries are exported when this method is called from the Assembly class - to export Case (and other Nastran file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf"
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field)
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hiearchical include files that mirrors the Assmbly/Part product structure, or as a singel Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the xport) to be written
- `inputType` — An enumeration to define which Marc input file format will be requested in the exported file. The default is DAT input file
- `renumberMethod` — Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Marc file and has no impact on the ID's within Apex.
- `apexEngineeringAbstractions` — A Boolean quantity to control whether the exported data contains Apex Engineering Abstractions.

#### `getExclusiveGroups() -> apex.GroupCollection`
returns a GroupCollection of all Groups that exclusively reference ONLY Entities composed by PartReps within this AssemblyRep hierarchy. To return Groups that reference at least one Entity that is composed by a PartRep within this AssemblyRep hierarchy use the partialGroups property instead.

Returns: a GroupCollection of all Groups that exclusively reference ONLY Entities composed by PartReps within this AssemblyRep hierarchy.

#### `getExclusiveRegions() -> apex.RegionCollection`
returns a RegionCollection of all Regions that exclusively reference ONLY Entities composed by PartReps within this AssemblyRep hierarchy. To return Regions that reference at least one Entity that is composed by a PartRep within this AssemblyRep hierarchy use the partialRegions property instead.

Returns: a RegionCollection of all Regions that exclusively reference ONLY Entities composed by PartReps within this AssemblyRep hierarchy.

#### `getPartialGroups() -> apex.GroupCollection`
returns a GroupCollection of all Groups that reference at least one Entity that is composed by a PartRep within this AssemblyRep hierarchy. To return Groups that exclusively reference ONLY Entities composed by PartReps within this AssemblyRep hierarchy use the exclusiveGroups property instead.

Returns: a GroupCollection of all Groups that reference at least one Entity that is composed by a PartRep within this AssemblyRep hierarchy.

#### `getPartialRegions() -> apex.RegionCollection`
returns a RegionCollection of all Regions that reference at least one Entity that is composed by a PartRep within this AssemblyRep hierarchy. To return Regions that exclusively reference ONLY Entities composed by PartReps within this AssemblyRep hierarchy use the exclusiveRegions property instead.

Returns: a RegionCollection of all Regions that reference at least one Entity that is composed by a PartRep within this AssemblyRep hierarchy.

- `getParts() -> apex.PartCollection` — get Parts in AssemblyRep.
- `getTargets() -> apex.EntityCollection` — get targets, Assembly/ AssemblyRep/ Part/ apex.attribute.MeshDependentTie/ apex.attribute.DiscreteTie from an AssemblyRep
#### `remove(target: apex.Entity = None, targets: apex.EntityCollection = None) -> None`
remove Assembly/ AssemblyRep/ Part/ apex.attribute.MeshDependentTie/ apex.attribute.DiscreteTie from an AssemblyRep

- `target` — a single target to be removed to the current AssembyRep.
- `targets` — collection targets to be removed to the current AssemblyRep.

#### `update(name: str = "#####", description: str = "#####", targets: apex.EntityCollection = None) -> None`
Update this AssemblyRep.

- `name` — of this AssemblyRep
- `description` — of this AssemblyRep
- `targets` — of this AssemblyRep

One or more properties may be updated in each call to update().


## `apex.AssemblyRepCollection`  (extends `EntityCollection`)

Methods:

- `AssemblyRepCollection() -> None` — Construct a new AssemblyRepCollection.

## `apex.AxisAlignedBoundingBox`
object representing a the bounding box of a 3D object in space.
Properties: `point1`, `point2`

Methods:

- `AxisAlignedBoundingBox(point1: apex.construct.Point3D, point2: apex.construct.Point3D) -> None` — DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems.
- `AxisAlignedBoundingBox(point1: ILocation, point2: ILocation) -> None`
- `AxisAlignedBoundingBox() -> None`
- `getPoint1(: None) -> ILocation`
- `getPoint2(: None) -> ILocation`
- `update(point1: ILocation, point2: ILocation) -> bool`

## `apex.ColorRGB`
A convenience class that holds a Color defined by 3 integer values(RGB). The class exposes three attributes that represent the 'r', 'g', 'b' values.
Properties: `b`, `g`, `integer`, `r`, `RGBstr`

Methods:

- `ColorRGB() -> None`
- `ColorRGB(rval: int, gval: int, bval: int) -> None`
- `ColorRGB(ival: int) -> None`
- `operator==(color: ColorRGB) -> bool`
#### `update(rval: int, gval: int, bval: int) -> None`
update the color value

- `rval` — the red value
- `gval` — the green value
- `bval` — the blue value

update the color values

#### `updateInteger(ival: int) -> None`
update the color value

- `ival` — the integer value

update the color values


## `apex.Coordinate`  (extends `Entity`, `IPhysical`)
3D Coordinate object with optional associated Entity.
Properties: `associatedEntity`, `x`, `y`, `z`

Methods:

#### `Coordinate() -> None`
Create a new 3d Coordinate with x, y, z = 0.

Returns: the created Coordinate (with no associated Entity)

#### `Coordinate(physicalEntity: apex.ILocation) -> None`
Create a new 3d Coordinate with location initialized from an ILocation Entity.

- `physicalEntity` — Entity to associate Coordinate with.

Returns: the created Coordinate (will inherit x,y,z location from Entity)

The Coordinate will inherit the x,y,z location from the specified ILocation Entity. The specified ILocation Entity can be obtained from the Coordiate using the getAssociatedEntity() method.

#### `Coordinate(x: float, y: float, z: float) -> None`
Create a new 3d Coordinate specifying each of x, y, z.

- `x` — location
- `y` — location
- `z` — location

Returns: the created Coordinate (with no associated Entity)

- `getAssociatedEntity() -> apex.Entity` — Return the Entity associated with this Coordinate (may be None).
- `setAssociatedEntity(entity: apex.Entity) -> None` — Set the Entity associated with this Coordinate (may be None).
- `setX(x: float) -> None` — sets the x value of this Coordinate.
- `setY(y: float) -> None` — sets the y value of this Coordinate.
- `setZ(z: float) -> None` — sets the z value of this Coordinate.

## `apex.DataTable2Col`
object representing 2 columns of float data. Used in apex.environment module.
Properties: `column1`, `column2`

Methods:

- `getColumn1() -> [float]`
- `getColumn2() -> [float]`
- `update(column1: [float] = [], column2: [float] = []) -> None`

## `apex.DataTable3Col`  (extends `DataTable2Col`)
object representing 3 columns of float data. Used in apex.environment module.
Properties: `column3`

Methods:

- `getColumn3() -> [float]`
- `update(column1: [float], column2: [float], column3: [float]) -> None`

## `apex.DesignVariable`  (extends `Entity`, `IName`)
Properties: `allowDesignStudyToIgnoreList`, `allowOptimizationToIgnoreRange`, `description`, `discreteValueIncludeMax`, `discreteValueIncludeMin`, `discreteValueList`, `discreteValueMethod`, `discreteValueNumber`, `discreteValueRange`, `enableOptimizationParams`, `id`, `maxValue`, `minValue`, `moveLimit`, `name`, `negativeDelta`, `negativePercentage`, `positiveDelta`, `positivePercentage`, `rangeType`, `specifyAllowableDiscreteValues`, `type`, `unit`, `value`

Methods:

#### `getAllowDesignStudyToIgnoreList() -> bool`
Gets option to allow design study to ignore list or not, for Real or Integer type.

Returns: option to allow design study to ignore list or not, for Real or Integer type.

#### `getAllowOptimizationToIgnoreRange() -> bool`
Gets option to allow optimization to ignore range or not for Real or Integer type.

Returns: option to allow optimization to ignore range or not for Real or Integer type.

#### `getDescription() -> str`
Gets description of the design variable.

Returns: description of the design variable.

#### `getDesignVariableType() -> apex.DesignVariableType`
Gets one of types: Real, Integer, String, Expression or Object.

Returns: one of types: Real, Integer, String, Expression or Object.

#### `getDiscreteValueIncludeMax() -> bool`
Gets option to include max value in the discrete values list or not, for Real type.

Returns: option to include max value in the discrete values list or not, for Real type.

#### `getDiscreteValueIncludeMin() -> bool`
Gets option to include min value in the discrete values list or not, for Real type.

Returns: option to include min value in the discrete values list or not, for Real type.

#### `getDiscreteValueList() -> [float]`
Gets list of discrete values, for Real or Integer type. It will take effect only when ""EnterValues"" method is selected.

Returns: list of discrete values, for Real or Integer type. It will take effect only when ""EnterValues"" method is selected.

#### `getDiscreteValueMethod() -> apex.DiscreteValueMethod`
Gets discrete values method for design variable, either "Generate" or "EnterValues" for Real type, or "EnterValues" for Integer type.

Returns: discrete values method for design variable, either "Generate" or "EnterValues" for Real type, or "EnterValues" for Integer type.

#### `getDiscreteValueNumber() -> int`
Gets number of discrete values for Real type.

Returns: number of discrete values for Real type.

#### `getDiscreteValueRange() -> apex.DiscreteValueRange`
Gets discrete value range, either "Equal spaced" or "MinStdMax", for Real type.

Returns: discrete value range, either "Equal spaced" or "MinStdMax", for Real type.

#### `getEnableOptimizationParams() -> bool`
Gets option to enable optimization parameters for Real or Integer type.

Returns: option to enable optimization parameters for Real or Integer type.

#### `getId() -> int`
Gets id of design variable for Real type.

Returns: id of design variable for Real type.

#### `getMaxValue() -> float`
Gets maximum value of design variable for Real or Integer type.

Returns: maximum value of design variable for Real or Integer type.

#### `getMinValue() -> float`
Gets minimum value of design variable for Real or Integer type.

Returns: minimum value of design variable for Real or Integer type.

#### `getMoveLimit() -> float`
Gets the move limit of design variable for Real or Integer type.

Returns: the move limit of design variable for Real or Integer type.

#### `getName() -> str`
Gets name of design variable.

Returns: name of design variable.

#### `getNegativeDelta() -> float`
Gets negative delta for value of design variable for Real or Integer type.

Returns: negative delta for value of design variable for Real or Integer type.

#### `getNegativePercentage() -> float`
Gets negative percentage for value of design variable for Real or Integer type.

Returns: negative percentage for value of design variable for Real or Integer type.

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/

#### `getPositiveDelta() -> float`
Gets positive delta for value of design variable for Real or Integer type.

Returns: positive delta for value of design variable for Real or Integer type.

#### `getPositivePercentage() -> float`
Gets positive percentage for value of design variable for Real or Integer type.

Returns: positive percentage for value of design variable for Real or Integer type.

#### `getRangeType() -> apex.DesignVariableRangeType`
Gets one of 3 range types for Real or Integer type.

Returns: one of 3 range types for Real or Integer type.

#### `getSpecifyAllowableDiscreteValues() -> bool`
Gets boolean value to indicate specifying allowable discrete values or not for Real or Integer type.

Returns: boolean value to indicate specifying allowable discrete values or not for Real or Integer type.

#### `getUnit() -> apex.DesignVariableUnit`
Gets unit of design variable for Real type.

Returns: unit of design variable for Real type.

#### `getValue() -> object`
Gets value for design variable.

Returns: value for design variable.

#### `setAllowDesignStudyToIgnoreList(allowDesignStudyToIgnoreList: bool) -> None`
Sets option to allow design study to ignore list or not, for Real or Integer type.

- `allowDesignStudyToIgnoreList` — option to allow design study to ignore list or not, for Real or Integer type.

#### `setAllowOptimizationToIgnoreRange(allowOptimizationToIgnoreRange: bool) -> None`
Sets option to allow optimization to ignore range or not for Real or Integer type.

- `allowOptimizationToIgnoreRange` — option to allow optimization to ignore range or not for Real or Integer type.

#### `setDescription(description: str) -> None`
Sets description of the design variable.

- `description` — description of design variable.

#### `setDesignVariableType(type: apex.DesignVariableType) -> None`
Sets one of types: Real, Integer, String, Expression or Object.

- `type` — one of types: Real, Integer, String, Expression or Object.

#### `setDiscreteValueIncludeMax(discreteValueIncludeMax: bool) -> None`
Sets option to include max value in the discrete values list or not, for Real type.

- `discreteValueIncludeMax` — option to include max value in the discrete values list or not, for Real type.

#### `setDiscreteValueIncludeMin(discreteValueIncludeMin: bool) -> None`
Sets option to include min value in the discrete values list or not, for Real type.

- `discreteValueIncludeMin` — option to include min value in the discrete values list or not, for Real type.

#### `setDiscreteValueList(discreteValueList: [float]) -> None`
Sets list of discrete values, for Real or Integer type. It will take effect only when ""EnterValues"" method is selected.

- `discreteValueList` — list of discrete values, for Real or Integer type. It will take effect only when ""EnterValues"" method is selected.

#### `setDiscreteValueMethod(discreteValueMethod: apex.DiscreteValueMethod) -> None`
Sets discrete values method for design variable, either "Generate" or "EnterValues" for Real type, or "EnterValues" for Integer type.

- `discreteValueMethod` — discrete values method for design variable, either "Generate" or "EnterValues" for Real type, or "EnterValues" for Integer type.

#### `setDiscreteValueNumber(discreteValueNumber: int) -> None`
Sets number of discrete values for Real type.

- `discreteValueNumber` — number of discrete values for Real type.

#### `setDiscreteValueRange(discreteValueRange: apex.DiscreteValueRange) -> None`
Sets discrete value range, either "Equal spaced" or "MinStdMax", for Real type.

- `discreteValueRange` — discrete value range, either "Equal spaced" or "MinStdMax", for Real type.

#### `setEnableOptimizationParams(enableOptimizationParams: bool) -> None`
Sets option to enable optimization parameters for Real or Integer type.

- `enableOptimizationParams` — option to enable optimization parameters for Real or Integer type.

#### `setId(id: int) -> None`
Sets id of design variable for Real type.

- `id` — id of design variable for Real type.

#### `setMaxValue(maxValue: float) -> None`
Sets maximum value of design variable for Real or Integer type.

- `maxValue` — maximum value of design variable for Real or Integer type.

#### `setMinValue(minValue: float) -> None`
Sets minimum value of design variable for Real or Integer type.

- `minValue` — minimum value of design variable for Real or Integer type.

#### `setMoveLimit(moveLimit: float) -> None`
Sets the move limit of design variable for Real or Integer type.

- `moveLimit` — the move limit of design variable for Real or Integer type.

- `setName(name: str) -> None` — Sets name of design variable.
#### `setNegativeDelta(negativeDelta: float) -> None`
Sets negative delta for value of design variable for Real or Integer type.

- `negativeDelta` — negative delta for value of design variable for Real or Integer type.

#### `setNegativePercentage(negativePercentage: float) -> None`
Sets negative percentage for value of design variable for Real or Integer type.

- `negativePercentage` — negative percentage for value of design variable for Real or Integer type.

#### `setPositiveDelta(positiveDelta: float) -> None`
Sets positive delta for value of design variable for Real or Integer type.

- `positiveDelta` — positive delta for value of design variable for Real or Integer type.

#### `setPositivePercentage(positivePercentage: float) -> None`
Sets positive percentage for value of design variable for Real or Integer type.

- `positivePercentage` — positive percentage for value of design variable for Real or Integer type.

#### `setRangeType(rangeType: apex.DesignVariableRangeType) -> None`
Sets one of 3 range types for Real or Integer type.

- `rangeType` — one of 3 range types for Real or Integer type.

#### `setSpecifyAllowableDiscreteValues(specifyAllowableDiscreteValues: bool) -> None`
Sets boolean value to indicate specifying allowable discrete values or not for Real or Integer type.

- `specifyAllowableDiscreteValues` — boolean value to indicate specifying allowable discrete values or not for Real or Integer type.

#### `setUnit(unit: apex.DesignVariableUnit) -> None`
Sets unit of design variable for Real type.

- `unit` — unit of design variable for Real type.

#### `setValue(value: object) -> None`
Sets value for design variable.

- `value` — for design variable.

#### `update(name: str, id: int, description: str, type: apex.DesignVariableRangeType, unit: str, value: object, rangeType: apex.DesignVariableRangeType, minValue: float, maxValue: float, negativePercentage: float, positivePercentage: float, negativeDelta: float, positiveDelta: float, enableOptimizationParams: ApexBool, moveLimit: float, allowOptimizationToIgnoreRange: ApexBool, specifyAllowableDiscreteValues: ApexBool, discreteValueMethod: apex.DiscreteValueMethod, discreteValueRange: apex.DiscreteValueRange, discreteValueNumber: int, discreteValueIncludeMax: ApexBool, discreteValueIncludeMin: ApexBool, discreteValueList: [float], allowDesignStudyToIgnoreList: ApexBool) -> None`
update the attributes of design variable. Any arg not needed can be omitted (defaults will be used)

- `name` — name of design variable.
- `id` — id of design variable for Real type.
- `description` — update the description.
- `type` — type of design variable.
- `unit` — unit of design variable for Real type.
- `value` — Optional argument for Real type, it is set as 0.0 if omit. Optional argument for Integer type, it is set as 10 if omit. For String type, one string must be provided. For Expression type, one expression must be provided. For Object type, one Apex.Entity object must be provided.
- `rangeType` — one of 3 types for defining the range of design variable for Real or Integer type.
- `minValue` — minimum value of design variable for Real or Integer type.
- `maxValue` — maximum value of design variable for Real or Integer type.
- `negativePercentage` — negative percentage of design variable for Real or Integer type.
- `positivePercentage` — positive percentage of design variable for Real or Integer type.
- `negativeDelta` — negative delta of design variable for Real or Integer type.
- `positiveDelta` — positive delta for design variable for Real or Integer type.
- `enableOptimizationParams` — option to enable optimization to ignore range for Real or Integer type.
- `moveLimit` — move limit of design variable for Real or Integer type.
- `allowOptimizationToIgnoreRange` — option to allow optimization to ignore range for Real or Integer type.
- `specifyAllowableDiscreteValues` — update the boolean value for the option of specifyAllowableDiscreteValues, which is for Real or Integer type.
- `discreteValueMethod` — one of two methods to create discrete values: "Generate" or "EnterValues" for Real or Integer type.
- `discreteValueRange` — one of two types for the range: "EquallySpaced" or "MinStdMax" for Real type.
- `discreteValueNumber` — number of discrete values for Real type.
- `discreteValueIncludeMax` — control if maximum value is included in the list of discrete values for Real type.
- `discreteValueIncludeMin` — control if minimum value is included in the list of discrete values for Real type.
- `discreteValueList` — list of discrete values if "EnterValues" method is selected.
- `allowDesignStudyToIgnoreList` — option to allow design study to ignore list for Real or Integer type.


## `apex.DesignVariableCollection`  (extends `EntityCollection`)
Iterable collection of DesignVariables, based on EntityCollection.

Methods:

- `DesignVariableCollection() -> None` — Construct a new UserAttributeCollection.

## `apex.Entity`
Base scripting class that supports type operations. Most other scripting Classes inherit from Entity.
Properties: `entityType`

Methods:

- `asAssembly() -> Assembly`
- `asBody() -> apex.geometry.GeometryBody`
- `asBox() -> apex.geometry.Box`
- `asBucklingStep() -> apex.studies.BucklingStep`
- `asCell() -> apex.geometry.Cell`
- `asCoordinate() -> apex.Coordinate`
- `asCoordinateSystem() -> apex.construct.CoordinateSystem`
- `asCurve() -> apex.geometry.Curve`
- `asCurveMesh() -> apex.mesh.CurveMesh`
- `asCylinder() -> apex.geometry.Cylinder`
- `asCylindricalJoint() -> apex.attribute.CylindricalJoint`
- `asDatumPlane() -> apex.construct.DatumPlane`
- `asEdge() -> apex.geometry.Edge`
- `asEdgeLoop() -> apex.geometry.EdgeLoop`
- `asEdgeSeed() -> apex.mesh.EdgeSeed`
- `asElement() -> apex.mesh.Element`
- `asElementEdge() -> apex.mesh.ElementFace`
- `asElementFace() -> apex.mesh.ElementFace`
- `asElementIdSet() -> apex.mesh.ElementIdSet`
- `asEllipsoid() -> apex.geometry.Ellipsoid`
- `asEvent() -> apex.studies.Event`
- `asFace() -> apex.geometry.Face`
- `asFacetedCurve() -> apex.geometry.FacetedCurve`
- `asFacetedSolid() -> apex.geometry.FacetedSolid`
- `asFacetedSurface() -> apex.geometry.FacetedSurface`
- `asGeometryFeature() -> apex.geometry.GeometryFeature`
- `asGeometryTopology() -> apex.geometry.GeometryTopology`
- `asHexMesh() -> apex.mesh.HexMesh`
- `asIDisplayable() -> apex.IDisplayable`
- `asILocation() -> ILocation`
- `asIOrientation() -> IOrientation`
- `asIPhysical() -> IPhysical`
- `asInitialTemperature() -> apex.environment.InitialTemperature`
- `asLoadCase() -> apex.studies.Event`
- `asMaterialCoverageRegion() -> apex.attribute.MaterialCoverageRegion`
- `asMesh() -> apex.mesh.MeshBody`
- `asMeshControlEdge() -> apex.geometry.MeshControlEdge`
- `asMeshDependentTie() -> apex.attribute.MeshDependentTie`
- `asMeshlessGenerativeDesignStep() -> apex.studies.MeshlessGenerativeDesignStep`
- `asModalFrequencyStep() -> apex.studies.ModalFrequencyStep`
- `asModel() -> Model`
- `asModesStep() -> apex.studies.ModesStep`
- `asNode() -> apex.mesh.Node`
- `asNodeIdSet() -> apex.mesh.NodeIdSet`
- `asPart() -> Part`
- `asPartRep() -> PartRep`
- `asPlanarJoint() -> apex.attribute.PlanarJoint`
- `asPoint() -> apex.geometry.Point`
- `asPointMesh() -> apex.mesh.PointMesh`
- `asPrismaticJoint() -> apex.attribute.PrismaticJoint`
- `asRemotePointEntity() -> apex.attribute.RemotePointEntity`
- `asRevoluteJoint() -> apex.attribute.RevoluteJoint`
- `asShellBehavior() -> apex.attribute.ShellBehavior`
- `asSolid() -> apex.geometry.Solid`
- `asSolidMesh() -> apex.mesh.SolidMesh`
- `asSphere() -> apex.geometry.Sphere`
- `asSphericalJoint() -> apex.attribute.SphericalJoint`
- `asStaticStep() -> apex.studies.StaticStep`
- `asStep() -> apex.studies.Step`
- `asSubMesh() -> apex.mesh.SubMesh`
- `asSubMesh1D() -> apex.mesh.SubMesh1D`
- `asSubMesh2D() -> apex.mesh.SubMesh2D`
- `asSubMesh3D() -> apex.mesh.SubMesh3D`
- `asSurface() -> apex.geometry.Surface`
- `asSurfaceMesh() -> apex.mesh.SurfaceMesh`
- `asUserAttribute() -> UserAttribute`
- `asVertex() -> apex.geometry.Vertex`
#### `getEntityType() -> apex.EntityType`
DEPRECATED: THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.

Returns: this apex::EntityType

return the type of this object.Use this method instead of the built-in Python "type()" method for Apex objects

- `~Entity() -> None`

## `apex.EntityCollection`
Iterable collection of Entities.
Properties: `collectionType`

Methods:

- `EntityCollection() -> None` — Construct a new EntityCollection.
- `append(entity: apex.Entity) -> None` — Add a new Entity to the end of this collection.
#### `appendList(entityList: [Entity]) -> None`
Add the entities from a list to the end of this collection.

- `entityList` — list of Entities to add to the collection.

For example:

- `clear() -> None` — clear this collection.
- `extend(collection: apex.EntityCollection) -> None` — Add a new EntityCollection to the end of this collection.
- `fromList(entityList: [apex.Entity]) -> None` — This method inserts a List of Entities to the collection. It will not return a new collection.
#### `getCollectionType() -> apex.CollectionType`
return the type of this Collection. DEPRECATED: THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. User can use type(object) to get the type directly. getCollectionType() may also be accessed as an object property 'collectionType'. For example:

Returns: this apex::CollectionType

- `hide() -> None` — Hide the Entities in this collection.
#### `index(entity: apex.Entity = None, start: int = 0, end: int = -1) -> int`
This method is to get the entity index.

- `entity` — The entity whose index we're trying to find.
- `start` — A optional argument, start searching from this index. If omitted, start searching at the beginning of the list.
- `end` — A optional argument, search the entity up to thsi index. If omitted, search every element from start to the end of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

#### `insert(index: int, entity: apex.Entity) -> None`
This method is to insert an entity into the collection.

- `index` — The index in the Collection after which the object will be inserted. The inserted index will be inserted immediately AFTER the supplied index.
- `entity` — the entity to be inserted

- `len() -> int` — return the length of this collection.
#### `remove(entity: apex.Entity) -> None`
This method is to remove an entity from the collection.

- `entity` — the entity to be remove from the collection.

- `show() -> None` — Show the Entities in this collection.
- `showOnly() -> None` — Show Only the Entities in this collection.
- `toList() -> [apex.Entity]` — This method returns the members of the Entity Collection as a Python List.
- `unsetVisibility() -> None` — Set the Entities' visibility to "UnSet" status in this collection.

## `apex.Group`  (extends `Entity`, `IPhysical`, `IUserAttributes`, `IName`, `IOrientation`, `IDisplayable`)
Class used to persist collections of ILocation objects, including Mesh and Geometry sub-entities, with non-volatile names and pathNames. Groups support two critical behaviors, 1. Non-volatile names/pathNames for collections of mesh and geometry sub-entities. Neither Mesh nor Geometry sub-entities provided non-volatile names or IDs. 2. Generative update of the their contents.
Properties: `centroid`, `target`

Methods:

#### `addEntities(entities: apex.ILocationCollection) -> None`
Add entities to this Group. Entities in the input that are not supported by Group will be silently ignored. Entities in the input that are already referenced by this Group will be silently ignored.

- `entities` — The collection of ILocation entities that will comprise the Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `addEntity(entity: apex.ILocation) -> None`
Add entity to this Group. If the input Entity type is not supported by Group, it will be silently ignored If the input Entity type is already referenced by this Group, it will be silently ignored.

- `entity` — The Entity to add to this Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `getCentroid() -> apex.Coordinate`
returns the centroid of this Group as a Coordinate. If the Group references a single entity, the centroid of this Group is derived directly from the centroid of that single object. If the single object is a type that does not support a centroid propertythis property will return a None type. If the Group references multiple entities, the centroid of this Group is derived directly from the centroid of the oriented bounding box that encloses the referenced entities.

Returns: returns the centroid of this Group as a Coordinate.

- `getTarget() -> apex.ILocationCollection` — A collection of ILocation objects that represent this Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element.
#### `removeEntities(entities: apex.ILocationCollection) -> None`
Removes entities from this Group. Entities in the input that are not supported by Group will be silently ignored Entities in the input that are not referenced by this Group will be silently ignored.

- `entities` — The collection of ILocation objects to remove from this Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `removeEntity(entity: apex.ILocation) -> None`
Removes an entity from this Group. If the input Entity type is not supported by Group, it will be silently ignored If the input Entity type is not already referenced by this Group, it will be silently ignored.

- `entity` — The Entity to add to this Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `update(name: str, description: str, entities: apex.ILocationCollection) -> None`
Update this group.

- `name` — An optional name for this Group. If provided, the name must be unique within the scope of model that composes this Group. If a non-unique name is provided, the system will silently rename the Group to ensure such name uniqueness. If provided name is "Group", the system will provide a default name using the prefix "Group " and concatenating the lowest integer value required to ensure name uniqueness. For example "Group 23". If omitted or provided name is "", the system will not change the name of this Group.
- `description` — An optional description for the Group. If omitted, the system will not change the description of this Group.
- `entities` — The collection of ILocation entities that will comprise the Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh) 4. Node 5. Element Duplicate entities will be silently ignored Entities of unsupported type will be silently ignored. If omitted, the system will not change the entities of this Group.


## `apex.GroupCollection`  (extends `EntityCollection`)

Methods:

- `GroupCollection() -> None` — Construct a new GroupCollection.
- `hide() -> None` — Hide the Entities in this collection.
- `show() -> None` — Show the Entities in this collection.
- `showOnly() -> None` — Show Only the Entities in this collection.

## `apex.IActivatable`
Properties: `isActive`

Methods:

#### `activate() -> bool`
Activates the Entity. If the entity is already Active the method will return without changing the entity.

Returns: true if the entity is activated

#### `deactivate() -> bool`
Deactivates the Entity. If the entity is already Inactive the method will return without changing the entity.

Returns: true if the entity is deactivated

#### `getIsActive() -> bool`
Returns True of this Entity is Active, False if it is Inactive.

Returns: true if the entity is active


## `apex.IDisplayable`
Base Interface class of other scripting objects (supports object visibility). IDisplayable is not exposed as a scripting object, but scripting objects inheriting IDisplayable may access it's methods.
Properties: `color`, `displayRenderStyle`, `displayTransparency`, `visibility`

Methods:

- `applyVisibilityToChildren(visibility: apex.session.Visibility) -> None` — change the container Entity visibility and apply the new value to its children.
- `getColor() -> [int]` — gets the color of this Entity.
- `getDisplayRenderStyle() -> apex.session.DisplayRenderStyle` — gets the render style of this Entity.
- `getDisplayTransparency() -> int` — gets the transparency of this Entity.
- `getVisibility() -> apex.session.Visibility` — gets the visibility of this Entity.
- `hide() -> None` — Hide this Entity.
- `show() -> None` — Show this Entity.
- `showOnly() -> None` — Show Only this Entity.
- `unsetColor() -> None` — unapplies the color of this entity to all its children.
- `unsetRender() -> None` — unapplies the renderStyle of this entity to all its children.
- `unsetTransparency() -> None` — unapplies the Transparency of this entity to all its children.
- `unsetVisibility() -> None` — unset the visibility of this entity and all its children need to be displaied as their original visibility.

## `apex.IIdentifier`
pure virtual Base scripting Interface object supporting Identifier (index and Id) methods.
Properties: `id`, `index`

Methods:

#### `getId() -> str`
return the Id of this Entity.

Returns: this entity id (string)

getId() may also be accessed as an Entity property 'id'. For example:

#### `getIndex() -> int`
return the index of this Entity.

Returns: this entity index (integer)

getIndex() may also be accessed as an Entity property 'index'. For example:


## `apex.ILocation`
Properties: `location`, `locationCartesian`, `locationCartesianLocal`, `locationCylindrical`, `locationCylindricalLocal`, `locationSpherical`, `locationSphericalLocal`, `x`, `xLocal`, `y`, `yLocal`, `z`, `zLocal`

Methods:

- `getLocation() -> Coordinate` — Gets The location of the object. All classes that implement ILocation define a single spatial reference location for that object. For 0D objects the location is unambiguous. For 1D, 2D and 3D object types the location is based on an object type specific rule.
#### `getLocationCartesian() -> [float]`
Gets Returns the location of the object as List of three floats, representing the x, y and z coordinates of the location in the global cartesian coordinate system. Each of the values in the list represents a Length value and is returned in the units of Length from the active script unit system.

Returns: the location of the object as List of three floats

#### `getLocationCartesianLocal() -> [float]`
Gets Returns the location of the object as List of three floats, representing the x, y and z coordinates of the location in the local Cartesian coordinate system. Each of the values in the list represents a Length value and is returned in the units of Length from the active script unit system.

Returns: the local location of the object as List of three floats

#### `getLocationCylindrical() -> [float]`
Gets Returns the location of the object as List of three floats, representing the r, theta and z coordinates of the location in the global cylindrical coordinate system. r and z represent a Length quantity and are returned in the units of Length from the active script unit system. theta represents an Angle quantity and is returned in the units of Angle from the active script unit system.

Returns: the location of the object as List of three floats

#### `getLocationCylindricalLocal() -> [float]`
Gets Returns the location of the object as List of three floats, representing the r, theta and z coordinates of the location in the local cylindrical coordinate system. r and z represent a Length quantity and are returned in the units of Length from the active script unit system. theta represents an Angle quantity and is returned in the units of Angle from the active script unit system.

Returns: the local location of the object as List of three floats

#### `getLocationSpherical() -> [float]`
Returns the location of the object as List of three floats, representing the r, theta and phi coordinates of the location in the global spherical coordinate system. r represents a Length quantity and is returned in the units of Length from the active script unit system. theta and phi represent an Angle quantities and are returned in the units of Angle from the active script unit system.

Returns: the location of the object as List of three floats

#### `getLocationSphericalLocal() -> [float]`
Gets Returns the location of the object as List of three floats, representing the r, theta and phi coordinates of the location in the local spherical coordinate system. r represents a Length quantity and is returned in the units of Length from the active script unit system. theta and phi represent an Angle quantities and are returned in the units of Angle from the active script unit system.

Returns: the local location of the object as List of three floats

- `getX() -> float` — Gets The x coordinate of the object location in a global cartesian system. x represents a position quantity and will be returned in the units of Length form the active script unit system.
- `getXLocal() -> float` — Gets The x coordinate of the object location in a local Cartesian system. x represents a position quantity and will be returned in the units of Length form the active script unit system.
- `getY() -> float` — Gets The y coordinate of the object location in a global Cartesian system. y represents a position quantity and will be returned in the units of Length form the active script unit system.
- `getYLocal() -> float` — Gets The y coordinate of the object location in a local Cartesian system. y represents a position quantity and will be returned in the units of Length form the active script unit system.
- `getZ() -> float` — Gets The z coordinate of the object location in a global Cartesian/cylindrical system. z represents a position quantity and will be returned in the units of Length form the active script unit system.
- `getZLocal() -> float` — Gets The z coordinate of the object location in a local Cartesian/Cylindrical system. z represents a position quantity and will be returned in the units of Length form the active script unit system.

## `apex.ILocationCollection`
Iterable collection of Entities that implement ILocation. based on EntityCollection.

Methods:

- `ILocationCollection() -> None` — Construct a new ILocationCollection.
#### `appendList(ilocationList: [apex.ILocation]) -> None`
Add entities that implement ILocation interface from a list to the end of this collection.

- `ilocationList` — list of ILocation entities to add to the collection.

For example:


## `apex.IName`  (extends `IPath`)
pure virtual Base scripting Interface object supporting name/description methods.
Properties: `description`, `name`, `pathName`

Methods:

#### `getDescription() -> str`
Read-only string representing the description of this object. The description field usually appears the Object Property panel in the interactive UI and in some cases will appear in the Tool property panel of the tool that creates the object.

Returns: this entity description (string)

getDescription() may also be accessed as an Entity property 'description'. For example:

#### `getName() -> str`
Read-only string representing the name of this object.

Returns: this entity name (string)

getName() may also be accessed as an Entity property 'name'. For example:

- `getPathName() -> str` — Read-only string representing the pathName (combination of entity path and name) of this object.

## `apex.IOrientation`
Properties: `alpha`, `alphaLocal`, `beta`, `betaLocal`, `euler121`, `euler121Local`, `euler123`, `euler123Local`, `euler131`, `euler131Local`, `euler132`, `euler132Local`, `euler212`, `euler212Local`, `euler213`, `euler213Local`, `euler231`, `euler231Local`, `euler232`, `euler232Local`, `euler313`, `euler313Local`, `euler323`, `euler323Local`, `gamma`, `gammaLocal`, `orientation`, `xAxis`, `xAxisLocal`, `yAxis`, `yAxisLocal`, `zAxis`, `zAxisLocal`

Methods:

- `getAlpha() -> float` — Gets a float value representing the first Euler rotation angle based on the Euler 313 rotation convention. It is based on global reference coordinate system of the object. alpha represents an Angle value and is returned in the Angle units of the active script unit system.
- `getAlphaLocal() -> float` — Gets a float value representing the first Euler rotation angle based on the Euler 313 rotation convention in local coordinate system. alpha represents an Angle value and is returned in the Angle units of the active script unit system.
- `getBeta() -> float` — Gets a float value representing the second Euler rotation angle based on the Euler 313 rotation convention. It is based on global reference coordinate system of the object. beta represents an Angle value and is returned in the Angle units of the active script unit system.
- `getBetaLocal() -> float` — Gets a float value representing the second Euler rotation angle based on the Euler 313 rotation convention in local coordinate system. beta represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler121() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 121 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler121Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 121 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler123() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 123 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler123Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 123 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler131() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 131 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler131Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 131 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler132() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 132 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler132Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 132 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler212() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 212 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler212Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 212 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler213() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 213 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler213Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 213 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler231() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 231 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler231Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 231 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler232() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 232 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler232Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 232 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler313() -> [float]` — Returns the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 313 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler313Local() -> [float]` — Gets the orientation of the object as a List of three floats, each representing the rotation of the orientation using the Euler 313 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler323() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 323 rotation convention. It is based on global reference coordinate system of the object. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getEuler323Local() -> [float]` — Gets the orientation of the object as List of three floats, each representing the rotation of the orientation using the Euler 323 rotation convention in local coordinate system. Each of the values in the list represents an Angle value and is returned in the Angle units of the active script unit system.
- `getGamma() -> float` — Gets a float value representing the third Euler rotation angle based on the Euler 313 rotation convention. It is based on global reference coordinate system of the object. gamma represents an Angle value and is returned in the Angle units of the active script unit system.
- `getGammaLocal() -> float` — Gets a float value representing the third Euler rotation angle based on the Euler 313 rotation convention in local coordinate system. gamma represents an Angle value and is returned in the Angle units of the active script unit system.
- `getOrientation() -> apex.Orientation` — Gets the orientation of the object as an apex.Orientation. All classes that implement IOrientation define a single orientation for that object. The rules used to determine the orientation vary with object types and are defined within the documented for each class. Returns the orientation of the object as an Orientation based on the 313 rotation convention.
- `getXAxis() -> apex.construct.Vector3D` — Gets the direction of the x axis of the Orientation of this object as a Vector3D. It is based on global reference coordinate system of the object.
- `getXAxisLocal() -> apex.construct.Vector3D` — Gets the direction of the x axis of the Orientation of this object as a Vector3D in local coordinate system.
- `getYAxis() -> apex.construct.Vector3D` — Gets the direction of the y axis of the Orientation of this object as a Vector3D. It is based on global reference coordinate system of the object.
- `getYAxisLocal() -> apex.construct.Vector3D` — Gets the direction of the y axis of the Orientation of this object as a Vector3D in local coordinate system.
- `getZAxis() -> apex.construct.Vector3D` — Gets the direction of the z axis of the Orientation of this object as a Vector3D. It is based on global reference coordinate system of the object.
- `getZAxisLocal() -> apex.construct.Vector3D` — Gets the direction of the z axis of the Orientation of this object as a Vector3D in local coordinate system.

## `apex.IOrientationCollection`
Iterable collection of Objects that implement IOrientation.

Methods:

- `IOrientationCollection() -> None` — Construct a new IOrientationCollection.
#### `appendList(iorientationList: [apex.IOrientation]) -> None`
Add entities that implement IOrientation interface from a list to the end of this collection.

- `iorientationList` — list of IOrientation entities to add to the collection.

For example:


## `apex.IPath`
pure virtual Base scripting Interface object supporting path methods.
Properties: `path`

Methods:

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/


## `apex.IPhysical`  (extends `ILocation`, `IUserHighlightable`)
Properties: `axisAlignedBoundingBox`

Methods:

- `getAxisAlignedBoundingBox() -> apex.AxisAlignedBoundingBox` — Returns the axis aligned bounding box around the object in space.

## `apex.IPhysicalCollection`  (extends `ILocationCollection`, `IUserHighlightable`)
Iterable collection of Entities that implement IPhysical. based on EntityCollection.
Properties: `averageCentroid`, `centroid`

Methods:

- `IPhysicalCollection() -> None` — Construct a new IPhysicalCollection.
#### `appendList(iphysicalList: [apex.IPhysical]) -> None`
Add entities that implement IPhysical interface from a list to the end of this collection.

- `iphysicalList` — list of IPhysical entities to add to the collection.

For example:

- `clearHighlight() -> None` — Removes highlighting from the object. The method has no effect if the object is not already highlighted.
#### `getAverageCentroid() -> apex.Coordinate`
The average location of the centroids of all of the Geometry and Topology entities in this IPhysicalCollection. Support for inclusion of other IPhysical types will be added a future release.

Returns: The average location of the centroids of All of the IPhysical entities in this IPhysicalCollection.

#### `getCentroid() -> apex.Coordinate`
The location of the centroid of all of the geomety/topology entities in this IPhysicalCollection. Support for inclusion of other IPhysical types will be added a future release. The centroid is defined to be the average of the locations of all geometry/topology Solids, SUrfaces, Cuirves, Points, Cells, Faces, Edges and Vertices. An alternate averageCentroid property defines a location calculated by averaging the centroids of each IPhysical the IPhysicalCollection contains.

Returns: The location of the centroid of All of the IPhysical entities in this IPhysicalCollection.

- `highlight(colorRGB: apex.ColorRGB, lineWidth: int, pointSize: int) -> None` — Highlights the object using the highlight parameters in the argument list.
- `highlightColorRGB() -> apex.ColorRGB` — The highlight color assigned to the object as a ColorRGB object that support 8 bit RGB color definitions.
- `highlightEdgeWeight() -> int` — The edge weight assigned to the object.
- `highlightPointSize() -> int` — The highlight point size assigned to the object.
- `isHighlighted() -> bool` — Boolean indicating whether the object is highlighted or not.

## `apex.IUserAttributes`
scripting Interface supporting methods for setting/getting attribute on Entities

Methods:

#### `addUserAttribute(userAttributeName: str, floatValue: float, boolValue: apex.ApexBool, stringValue: str, intValue: int) -> None`
add a UserAttribute object to this Entity.

- `userAttributeName` — The name of the UserAttribute that will be added to this object. The name can be used as a key to identify and differentiate between multiple UserAtrributes associated to an object.
- `floatValue` — An optional floating point value that will be stored within the UserAttribute
- `boolValue` — An optional Boolean value that will be stored within the UserAttribute
- `stringValue` — An optional string value that will be stored within the UserAttribute
- `intValue` — An optional integer value that will be stored within the UserAttribute For example:

Adds a UserAttribute to the object. The argument list MUST contain a 'userAttributeName' plus one optional value. The type of the UserAttribute is determined by the type of the value that is supplied - inValue, floatValue, strValue, boolValue. Only one value argument may be supplied.

#### `getUserAttributes(userAttributeNames: [str] = []) -> apex.UserAttributeCollection`
get a UserAttribute from this Entity.

- `userAttributeNames` — An optional List of strings representing the names of UserAttributes. If omitted, the method will return ALL of the UserAttributes associated with the object. If supplied, only User Attributes associated wit the objects that have names that match any of the names in the input List will be returned.

Recovers all user attribute associated with the objects and returns them as a UserAtrtibuteCollection. If no arguments are supplied the method will return all of the User Attributes associated with the object. If the optional 'userAttributeNames' argument ( a List of strings) is supplied, the method will return all UserAttributes associated wit the object whose name is included in the List. The input List of names may include names for which no UserAttribute exists in the model - these are simply ignored.

#### `removeUserAttributes(userAttributeNames: [str] = []) -> apex.UserAttributeCollection`
delete a UserAttribute from this Entity.

- `userAttributeNames` — An List of strings representing the names of UserAttributesthat should be removed. All user defined attribute that have attributeNames that match the supplied name will be removed. If attributeName is omitted, all user defined attribute will be removed

Removes user defined attribute from the object. If no arguments are supplied, all user defined attribute associated with the object will be removed If the name argument is supplied, all users defined attribute associated with the object that use the name will be removed from the object The method returns all of the UserAttributes that were removed from the object as a UserAttributeCollection


## `apex.IUserHighlightable`
Base for other scripting objects that support highlighting. IUserHighlightable is not exposed as a scripting object, but other scripting objects that inherit IUserHighlightable must implement it's methods. Most scripting objects that can be displayed in a graphics view support IUserHighlightable.
Properties: `colorRGB`, `edgeWeight`, `highlighted`, `pointSize`

Methods:

- `clearHighlight() -> None` — Removes highlighting from the object. The method has no effect if the object is not already highlighted.
- `highlight(colorRGB: apex.ColorRGB = apex.ColorRGB(), lineWidth: int = 2, pointSize: int = 3) -> None` — Highlights the object using the highlight parameters in the argument list.
- `highlightColorRGB() -> apex.ColorRGB` — The highlight color assigned to the object as a ColorRGB object that support 8 bit RGB color definitions.
- `highlightEdgeWeight() -> int` — The edge weight assigned to the object.
- `highlightPointSize() -> int` — The highlight point size assigned to the object.
- `isHighlighted() -> bool` — Boolean indicating whether the object is highlighted or not.

## `apex.LocationInternal`  (extends `IsConstructed`)
apex.Location Class representing a location in 3D space. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with apex.Coordinate, which implements ILocation, which provides .x, .y, .z directly. All methods have already been updated to accept IPhysical.

Methods:

- `LocationInternal() -> None`
- `getByCoord() -> bool`
- `getEntity() -> apex.Entity`
#### `getX() -> float`
get float x Value of the X coordinate of the location in 3D space in the Apex global coordinate system. Coordinate values represent Length quantities and will be returned in the units of Length of the current ScriptUnitSystem.

Returns: float x Value of the X coordinate of the location in 3D space in the Apex global coordinate system.

#### `getY() -> float`
get float y Value of the X coordinate of the location in 3D space in the Apex global coordinate system. Coordinate values represent Length quantities and will be returned in the units of Length of the current ScriptUnitSystem.

Returns: float y Value of the X coordinate of the location in 3D space in the Apex global coordinate system.

#### `getZ() -> float`
get float z Value of the X coordinate of the location in 3D space in the Apex global coordinate system. Coordinate values represent Length quantities and will be returned in the units of Length of the current ScriptUnitSystem.

Returns: float z Value of the X coordinate of the location in 3D space in the Apex global coordinate system.

- `setByCoord(byCoord: bool) -> None`
- `setEntity(entity: apex.Entity) -> None`
- `setX(x: float) -> None`
- `setY(y: float) -> None`
- `setZ(z: float) -> None`

## `apex.Model`  (extends `Assembly`)
(database) object that can contain Assemblies, Parts, Geometry and FEM data, and be saved to the computer filesystem. Created with the apex.createModel() method.
Properties: `assemblies`, `currentPart`, `displayableEntities`, `groups`, `modelAssociations`, `namedEntities`, `parts`, `physicalEntities`, `regions`

Methods:

#### `close() -> Model`
Closes the current Model and creates a new one. The new Model is provied with a default name and is created in the default location.

Returns: the created Model

#### `createAssembly(name: str = "", parentPath: str = "") -> Assembly`
Create a new Assembly in this Model.

- `name` — of the new assembly. default = "" (auto-named)
- `parentPath` — of the new assembly. default = "" (top level assembly)

Returns: the created Assembly

- `createMirrorPlane(normal: apex.ILocation, origin: apex.ILocation) -> apex.construct.MirrorPlane`
#### `createModelAssociation(name: str, description: str, primaryAssembly: apex.Assembly, secondaryAssembly: apex.Assembly) -> ModelAssociation`
Creates and returns a ModelAssociation. ModelAssociations enable associations to be defined between two top level Assemblies in a Model. One of the Assemblies is defined to be the "Primary" Assembly and the other to be the "Secondary" Assembly and individual Each Part in the primary Assembly can be associated with one or more Parts or Assemblies in the secondary Assembly. Parts/Assemblies in the secondary Assembly can only be associated to one Part in the primary Assembly. ModelAssociations are used to connect two different representations of the same model. Current Apex releases use ModelAssociations to enable, 1.animation of CAD or finite element models based on the results of an Adams/Car multi-body dynamics simulation. In his case, the multibody dynamics model (results) are generated by importing an Adams/Car model (and results). The multi-body dynamics model is added to a ModelAssociation as the primary assembly and a second Assembly containing CAD or finite element entities is included as the secondary Assembly. Individual Parts form the multiboidy model (primary assembly) are then associated with one or more Parts/Assemblies from the CAD/finite element model.

- `name` — An optional name for this ModelAssociation. If omitted the system will assign a unique name based on the prefix "Model Association " and appending an integer to ensure name uniqueness for all ModelAssociations within the scope of the top level Apex Model.
- `description` — An optional description for this ModelAssociation
- `primaryAssembly` — The primary Assembly for this ModelAssociation. Each Part in this Assembly may subsequently be associated with one or more Parts and/or Assemblies in the secondary Assembly.
- `secondaryAssembly` — The secondary Assembly for this ModelAssociation. Parts and or Assemblies from this Assembly may subsequently be associated with a single Part from the primary Assembly.

Returns: the ModelAssociation

#### `createModelSet3Nastran(id: int, name: str, set_type: str, set_ids: [int]) -> apex.ModelSet3Nastran`
Creates and returns a ModelSet3Nastran The ModelSet3Nastran may optionally be initialized with an id, set type and list of ids.

- `id` — an id for this ModelSet3Nastran If omitted, Apex will assign an ID that is unique within this Model. If provided, the ID must be unique within this Model. If a non_unique ID is provided Apex will automatically and silently replace it with a unique ID
- `name` — an name for this ModelSet3Nastran
- `set_type` — the type of this ModelSet3Nastran as a string This argument may be assigned any one of the following values "GRID" - The IDs represent the IDs of finite element Grids (Nodes) "ELEM" - The IDs represent the IDs of finite element Elements "POINT" - The IDs represent the IDs of finite element Points "PROP" - The IDs represent the IDs of element properties "RBEin" - The IDs represent the IDs of rigid elements (to be INCLUIDED in MPC selections) "RBEex" - The IDs represent the IDs of rigid elements (to be EXCLUDED from MPC selections)
- `set_ids` — an optional iterable of integer values defining the IDs of the entities that this ModelSet3Nastran references

#### `createPart(name: str = "", parentPath: str = "") -> Part`
Create a new Part in this Model.

- `name` — of the new part. default = "" (auto-named)
- `parentPath` — of the new part. default = "" (top level part)

Returns: the created Part

#### `deleteModelAssociation(modelAssociation: ModelAssociation) -> None`
Deletes the input ModelAssociation from this Model. If the input ModelAssociation does not exist in this Model it will be silently ignored.

- `modelAssociation` — The modelAssociation object to be deleted.

#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports the Model in Nastran bulk data file format. All objects in the Model that can be mapped to Nastran keywords will be exported. Only the bulk data entries are exported when this method is called from the Model class, although a small subset of case control keywords are also exported to enable import of mesh independent ties into the other applications. To export case control entries, use the equivalent exportFEModel() method on the Scenario object.

- `filename` — Fully qualified name of the file to which the finite element objects will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files. The valid unit system names are "m-kg-s-N"; // Standard SI units (meter-kilogram-second) "cm-kg-s-cN"; // SI units with length in centimeters "cm-kg-ms-dakN"; // SI units with length in centimeters and time in milliseconds "cm-kg-us-daGN"; // SI units with length in centimeters and time in microseconds "mm-kg-ms-kN"; // SI units with length in millimeters and time in milliseconds "cm-g-s-dyn"; // Standard centimeter-gram-second (CGS) units "cm-g-us-daMN"; // CGS units with time in microseconds "mm-g-s-uN"; // CGS units with length in millimeters "mm-g-ms-N"; // CGS units with length in millimeters and time in milliseconds "mm-t-s-N"; // SI units with length in millimeters and mass in metric tons "in-slinch-s-lbf"; // English engineering units with mass in slinches (1 slinch = 12 slugs) "ft-slug-s-lbf"; // English engineering units with mass in slugs (1 slug = 32.174 pounds) "mm-khyl-s-kgf"; // Kilogram-force units with mass in kilohyls and length in millimeters "mm-kg-s-mN"; // SI units with length in millimeters "cm-g-ms-daN"; // CGS units with time in milliseconds "ft-lb-s-lbf"; // Standard English engineering units (foot-pound-second)
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single flat file. The default value of "False" causes a single file to be written containing all of the finite element entities within the Assembly to be written.
- `renumberMethod` — An enumeration to control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Model Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — A Boolean quantity to control whether the exported data contains Apex Engineering Abstractions.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

#### `exportGeometry(filename: str, cadFormat: apex.geometry.CADFormat, unitSystem: str = "m", stlMergeCells: bool = True, exportVirtualFaces: bool = False, exportVirtualFaceMethod: apex.VirtualFaceExportMethod = apex.VirtualFaceExportMethod.NurbsOnly, exportGeometryOrganization: apex.GeometryExportOrganization = apex.GeometryExportOrganization.Multiple, exportBodyPositionInLocal: bool = False) -> None`
Export Geometry file from this model to a file using the supplied CAD format.

- `filename` — Fully qualified name of the file to which the geometry objects will be exported.
- `cadFormat` — defines the format of the CAD file that will be exported using an apex.geometry.CADFormat enumeration.
- `unitSystem` — A string to identify the units to be used during export. Unit support is dependent on the CADFormat of the exported file and not all formats support units.Of the CAD formats currently supported by Apex, only the IGES/STL format supports user defined export units. The support Length unit: m, cm, mm, ft, in If the IGES/STL format is selected, unitSystem will be available. If it is undefined, use the default unitSystem = m. If a value other than one in the above unit is supplied, the method will throw an exception
- `stlMergeCells` — optional Boolean argument (default = True) that controls how multi-cellular solids will be represented in STL files. This argument is only relevant when the cadFormat type is an STL type and is silently ignored for all other formats. When True (Default), all cells in a multi-cellular solid will be merged into a single cell during export by removing all internal Faces. The GeometryBody is unaffected by this operation. When False, all cells in multi-cellular solids will be present in the exported STL file.
- `exportVirtualFaces` — Optional Argument, Default = False, where each virtual faces will be exported as a single face. This only applies to CAD Format Parasolid. The purpose is to export geometry topology that is consistent with native Apex to maintaining associatively with mesh, loads, BCs and other attributes. An attempt will be made to export the virtual faces as NURBS, by replacing the each virtual face with a single NURBS face. If this fails, then a facet body face will be used instead.
- `exportVirtualFaceMethod` — This applies to exportGeometry API only. It controls what is permitted for converting virtual topology to exportable faces with the same topology. This is ignored if exportVirtualFaces is False. If set to NurbsAndFaceted, then the system will try to convert to NURBS, and if that fails, it will then convert the face into a faceted face. If set to NurbsOnly (Default), then it will try to convert each virtual face to NURBS only.
- `exportGeometryOrganization` — Optional argument which specifies whether the model with multiple top level parts is exported as multiple files or single file.
- `exportBodyPositionInLocal` — Optional Boolean argument to export the geometry body in local position based the reference system of the body and parent part. By default, it is false. The system will export the geometry body position in global.

#### `exportMarc(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False) -> None`
Exports the contents of the Model to a Marc file. All objects in the Model that can be mapped to Marc keywords will be exported. If the Model contains multiple top level Parts or Assemblies the method will throw an exception. Use the equivalent method on each top Level Part or Asssembly instead or re-organize your model into a singel top level Assembly. The method arguments provide control over export options. Only bulk data entries are exported when this method is called from the Model class - to export Case (and other Marc file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — Fully qualified name of the file to which the finite element objects will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files. The valid unit system names are "m-kg-s-N"; // Standard SI units (meter-kilogram-second) "cm-kg-s-cN"; // SI units with length in centimeters "cm-kg-ms-dakN"; // SI units with length in centimeters and time in milliseconds "cm-kg-us-daGN"; // SI units with length in centimeters and time in microseconds "mm-kg-ms-kN"; // SI units with length in millimeters and time in milliseconds "cm-g-s-dyn"; // Standard centimeter-gram-second (CGS) units "cm-g-us-daMN"; // CGS units with time in microseconds "mm-g-s-uN"; // CGS units with length in millimeters "mm-g-ms-N"; // CGS units with length in millimeters and time in milliseconds "mm-t-s-N"; // SI units with length in millimeters and mass in metric tons "in-slinch-s-lbf"; // English engineering units with mass in slinches (1 slinch = 12 slugs) "ft-slug-s-lbf"; // English engineering units with mass in slugs (1 slug = 32.174 pounds) "mm-khyl-s-kgf"; // Kilogram-force units with mass in kilohyls and length in millimeters "mm-kg-s-mN"; // SI units with length in millimeters "cm-g-ms-daN"; // CGS units with time in milliseconds "ft-lb-s-lbf"; // Standard English engineering units (foot-pound-second)
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single flat file. The default value of "False" causes a single file to be written containing all of the finite element entities within the Assembly to be written.
- `renumberMethod` — An enumeration to control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Model Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — A Boolean quantity to control whether the exported data contains Apex Engineering Abstractions.

#### `getAssemblies(recursive: bool = False) -> apex.AssemblyCollection`
Get all Assemblies in this Model.

Returns: Iterable collection of all the Assemblies in this Model

getAssemblies() may also be accessed as a Model object property 'assemblies'. For example:

#### `getAssembly(pathName: str) -> Assembly`
Get an Assembly in this Model.

- `pathName` — of the assembly to get. Must use full name as in 'Assembly 1/Assembly 2'.

Returns: the found Assembly

#### `getBeamSpan(pathName: str) -> attribute.BeamSpan`
Retrieve a BeamSpan from this Model using the BeamSpan pathName "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE" This method has been superseded by the equivalent "apex.getBeamSpan()" function in the apex module. The new function takes the absolute pathName provided by the IName interface implementation as the object identifier making it more convenient to use than this method which requires a pathName relative to the "Model" object".

- `pathName` — pathName of the BeamSpan to retrieve

Returns: a reference to the BeamSpan object

#### `getBox(pathName: str) -> apex.geometry.Box`
Get a Box in this Model.

- `pathName` — of the Box to get. Must use full name as in 'Assembly 1/Part 1/Box 1'.

Returns: the Box

#### `getCoordinateSystem(name: str) -> apex.construct.CoordinateSystem`
Get a CoordinateSystem in a Model.

- `name` — of the CoordinateSystem to get.

Returns: the CoordinateSystem object

#### `getCoordinateSystemById(id: int) -> apex.construct.CoordinateSystem`
Get a CoordinateSystem in a Model.

- `id` — of the CoordinateSystem to get.

Returns: the CoordinateSystem object

#### `getCoordinateSystems(target: [{str:str}]) -> apex.construct.CoordinateSystemCollection`
Get CoordinateSystem objects in a Model.

- `target` — of dictionaries (string:string) specifying the coordinate systems to retrieve. Valid keys are 'path' and 'name'.

Returns: the collection of coordinate system objects

#### `getCurrentPart() -> Part`
Return the 'current' Part in this Model.

Returns: the current Part

#### `getCurve(pathName: str) -> apex.geometry.Curve`
Get a Curve in this Model.

- `pathName` — of the curve to get. Must use full name as in 'Assembly 1/Part 1/Solid 1'.

Returns: the Curve

#### `getCurveMesh(pathName: str) -> apex.mesh.CurveMesh`
Get a CurveMesh in this Model. "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE" This method has been superseded by the equivalent "apex.getCurveMesh()" function in the apex module. The new function takes the absolute pathName provided by the IName interface implementation as the object identifier making it more convenient to use than this method which requires a pathName relative to the "Model" object".

- `pathName` — of the CurveMesh to get.

Returns: the CurveMesh

#### `getCylinder(pathName: str) -> apex.geometry.Cylinder`
Get a Cylinder in a Model.

- `pathName` — of the Cylinder to get including the model name as in 'MyModel/Assembly1/Part1/Cylinder 1'.

Returns: the Cylinder

#### `getDatumPlanes(recursive: bool = False) -> apex.construct.DatumPlaneCollection`
Retrieves all DatumPlanes directly composed by the Model and return them in a DatumPlaneCollection.

- `recursive` — Optional Boolean argument (Default = False) that determines whether only DatumPlanes composed directly by this Model will be returned or if the Model will searched recursively and all DatumPlanes in the Model hierarchy will be returned.

Returns: the collection of datum plane objects

An optional "recursive" argument enables the method to return all DatumPlanes composed by Parts or Assemblies within this Model hierarchy.NOTE : DatumPlanes are composed only by Assemblies or Parts in Apex, so this method will always return an empty colllection if "recursive = False". This method is intended to be used with "recursive = True" which will cause all datum planes in the model to be returned. Model hierarchy.

#### `getDesignVariable(pathName: str) -> apex.DesignVariable`
Retrieves a design variable by using the input pathName.

- `pathName` — path name of the design variable.

Returns: the design variable

#### `getDesignVariables() -> apex.DesignVariableCollection`
return all design variables in the model.

Returns: a DesignVariableCollection of all design variables in the model.

#### `getDisplayableEntities() -> apex.EntityCollection`
returns a collection of all entities in the Model that implement IDisplayable as an EntityCollection.

Returns: this Entity objects

The Model hierarchy is traversed recursively and all entities in the hierarchy that implement IDisplayable are returned.

#### `getElements(elementsOfPartVec: [{str:str}] = []) -> apex.mesh.ElementCollection`
Get a ElementCollection in multi Part.

- `elementsOfPartVec` — vectors of the element in one part.

Returns: the ElementCollection

#### `getEllipsoid(pathName: str) -> apex.geometry.Ellipsoid`
Get a Ellipsoid in a Model.

- `pathName` — of the Ellipsoid to get including the model name as in 'MyModel/Assembly1/Part1/Ellipsoid 1'.

Returns: the Ellipsoid

#### `getEntities(pathNames: [str]) -> apex.EntityCollection`
Get a collection of named Entities in this Model.

- `pathNames` — list of the entities to get. Must use full names as in 'Assembly 1/Assembly 2'.

Returns: Iterable collection of the Entities in this Model

#### `getFacetedCurve(pathName: str) -> apex.geometry.FacetedCurve`
Get a Faceted Curve in this Model.

- `pathName` — of the faceted curve to get. Must use full name as in 'Assembly 1/Part 1/Faceted Curve 1'.

Returns: the FacetedCurve

#### `getFacetedSolid(pathName: str) -> apex.geometry.FacetedSolid`
Get a Faceted Solid in this Model.

- `pathName` — of the faceted solid to get. Must use full name as in 'Assembly 1/Part 1/Faceted Solid 1'.

Returns: the FacetedSolid

#### `getFacetedSurface(pathName: str) -> apex.geometry.FacetedSurface`
Get a Faceted Surface in this Model.

- `pathName` — of the faceted surface to get. Must use full name as in 'Assembly 1/Part 1/Faceted Surface 1'.

Returns: the FacetedSurface

#### `getGeometryBody(pathName: str) -> apex.geometry.GeometryBody`
Get a GeometryBody in this Model.

- `pathName` — of the body to get. Must use full name as in 'Assembly 1/Part 1/Solid 1'.

Returns: the GeometryBody

#### `getGroup(name: str) -> apex.Group`
Return a named Group identified from this Model. If a Group with this name does not exist in this Model, the method will raise an exception.

- `name` — The name of the Group to return. If a Group with this name does not exist within this Model the method will raise an Exception.

Returns: Return a named Group identified from this Model.

#### `getGroups() -> apex.GroupCollection`
get all Groups from this Model.

Returns: all the named Groups of this Model.

#### `getHexMesh(pathName: str) -> apex.mesh.HexMesh`
Get a HexMesh in this Model. "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE" This method has been superseded by the equivalent "apex.getHexMesh()" function in the apex module. The new function takes the absolute pathName provided by the IName interface implementation as the object identifier making it more convenient to use than this method which requires a pathName relative to the "Model" object".

- `pathName` — of the HexMesh to get.

Returns: the HexMesh

#### `getInterfacePoints() -> apex.attribute.InterfacePointCollection`
Retrieves all of the apex.attribute.InterfacePoints InterfacePoints in this Model and returns them as an InterfacePointCollection. If no InterfacePoint exists in the Model the returned collection will be empty. If the optional 'recursive' argument is set to True, all InterfacePoints within the scope of the Model will be returned from the hierarchy of Assemblies and Parts composed by the Model. If the argument is omitted or set to False, only the InterfacePoints that are directly composed by the Model will be returned.

Returns: a reference to the apex.attribute.InterfacePointCollection object

#### `getMaterialCoverageRegions() -> apex.attribute.MaterialCoverageRegionCollection`
Retrieves all MaterialCoverageRegions directly composed by the Model and returns them in a MaterialCoverageRegionCollection.

Returns: the MaterialCoverageRegionCollection

#### `getMesh(pathName: str) -> apex.mesh.MeshBody`
Get a MeshBody in this Model. "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE" This method has been superseded by the equivalent "apex.getMesh()" function in the apex module. The new function takes the absolute pathName provided by the IName interface implementation as the object identifier making it more convenient to use than this method which requires a pathName relative to the "Model" object".

- `pathName` — of the MeshBody to get.

Returns: the MeshBody

#### `getModelAssociation(name: str, primaryAssembly: apex.Assembly) -> ModelAssociation`
Get a ModelAssociation.

- `name` — An optional name for this ModelAssociation. If omitted the system will assign a unique name based on the prefix "Model Association " and appending an integer to ensure name uniqueness for all ModelAssociations within the scope of the top level Apex Model.
- `primaryAssembly` — The primary Assembly for this ModelAssociation. Each Part in this Assembly may subsequently be associated with one or more Parts and/or Assemblies in the secondary Assembly.

Returns: the ModelAssociation

#### `getModelAssociations() -> apex.ModelAssociationCollection`
get modelAssociation collection from model.

Returns: a collection of all ModelAssociations associated with this Model

#### `getModelSetNastran(id: int) -> apex.ModelSetNastran`
gets a ModelSetNastran from this Model using the ID provided in the argument The ModelSetNastran is returned as an instance of the actual type of the Set and not as the base class ModelSetNastran type

- `id` — The ID of the ModelSetNastran to retrieve. If a ModelSetNastran with this ID does not exist in this Model the method will raise an exception

#### `getNamedEntities() -> apex.EntityCollection`
returns a collection of all entities in this Model that implement IName as an EntityCollection.

Returns: this Entity objects

The Model hierarchy is traversed recursively and all entities in the hierarchy that implement IName are returned.

#### `getNodes(nodesOfPartVec: [{str:str}] = []) -> apex.mesh.NodeCollection`
Get a NodeCollection in multi Part.

- `nodesOfPartVec` — vectors of the node in one part.

Returns: the NodeCollection

#### `getPart(pathName: str) -> Part`
Get a Part in this Model.

- `pathName` — of the part to get. Must use full name as in 'Assembly 1/Part 1'.

Returns: the created Part

#### `getParts(recursive: bool = False) -> apex.PartCollection`
Get all Parts in this Model.

Returns: Iterable collection of all the Parts in this Model

getParts() may also be accessed as a Model object property 'parts'. For example:

#### `getPhysicalEntities() -> apex.EntityCollection`
returns a collection of all entities in the Model that implement ILocation as an EntityCollection.

Returns: this Entity objects

The Model hierarchy is traversed recursively and all entities in the hierarchy that implement ILocation are returned.

#### `getPoint(pathName: str) -> apex.geometry.Point`
Get a Point in this Model.

- `pathName` — of the point to get. Must use full name as in 'Assembly 1/Part 1/Solid 1'.

Returns: the Point

#### `getRegion(name: str) -> apex.Region`
Return a named Region identified from this Model. If a Region with this name does not exist in this Model, the method will raise an exception.

- `name` — The name of the Region to return. If a Region with this name does not exist within this Model the method will raise an Exception.

Returns: Return a named Region identified from this Model.

#### `getRegions() -> apex.RegionCollection`
get all Regions from this Model.

Returns: all the named Regions of this Model.

#### `getSolid(pathName: str) -> apex.geometry.Solid`
Get a Solid in this Model.

- `pathName` — of the solid to get. Must use full name as in 'Assembly 1/Part 1/Solid 1'.

Returns: the Solid

#### `getSolidMesh(pathName: str) -> apex.mesh.SolidMesh`
Get a SolidMesh in this Model. "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE" This method has been superseded by the equivalent "apex.getSolidMesh()" function in the apex module. The new function takes the absolute pathName provided by the IName interface implementation as the object identifier making it more convenient to use than this method which requires a pathName relative to the "Model" object".

- `pathName` — of the SolidMesh to get.

Returns: the SolidMesh

#### `getSphere(pathName: str) -> apex.geometry.Sphere`
Get a Sphere in a Model.

- `pathName` — of the Sphere to get including the model name as in 'MyModel/Assembly1/Part1/Sphere 1'.

Returns: the Sphere

#### `getSurface(pathName: str) -> apex.geometry.Surface`
Get a Surface in this Model.

- `pathName` — of the surface to get. Must use full name as in 'Assembly 1/Part 1/Solid 1'.

Returns: the Surface

#### `getSurfaceMesh(pathName: str) -> apex.mesh.SurfaceMesh`
Get a SurfaceMesh in this Model. "THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE NEXT APEX RELEASE" This method has been superseded by the equivalent "apex.getSurfaceMesh()" function in the apex module. The new function takes the absolute pathName provided by the IName interface implementation as the object identifier making it more convenient to use than this method which requires a pathName relative to the "Model" object".

- `pathName` — of the SurfaceMesh to get.

Returns: the SurfaceMesh

#### `importApexModel(databaseFileNames: [str]) -> apex.EntityCollection`
Imports a target Apex database model from the input database files and returns the EntityCollection of Top Level of Part/Assembly.

- `databaseFileNames` — A List of the path qualified file database file names. In current release, supports single database path only. If defines multiple database paths, returns exception.

#### `importFEModel(feModelFileName: str, feResultsFileName: str, modelType: apex.mesh.FEModelFormat, unitSystemName: str, organizeBy: apex.mesh.FEModelImportOrganizationOptions = apex.mesh.FEModelImportOrganizationOptions.ByContiguousMesh, skip: [str] = [], modelResultsImportOptions: apex.ModelResultsImportOptions = apex.ModelResultsImportOptions.Undefined, idConflictResolutionMethod: apex.attribute.IdConflictResolutionMethod = apex.attribute.IdConflictResolutionMethod.AutomaticOffset, detectFlexibleLink: bool = True, set3ToGroup: bool = True, preserveIncludeFileStructure: bool = False) -> apex.Entity`
Imports a finite element models, and optionally results data, into this Apex Model and returns (as an Entity) the top level Part, Assembly or Scenario that is created. Currently, import is restricted to Nastran models and HDF5 formatted result files.

- `feModelFileName` — The fully qualified name of the FE model/results file that is being imported. This file must be a Nastran input file or a Nastran HDF5 file. Nastran provides an option to export model and results data to HDF5 files with options to have the model and results written to the same .h5 file or to different .h5 files. The .h5 file provided here must contain model data - providing a .h5 file that contains only results data is considered an error and the method will raise an exception.
- `feResultsFileName` — The fully qualified name of the FE results file containing the results data that is being read. This file must be a Nastran HDF5 result file. Nastran provides an option to export both model and results data to HDF5 files with options to have the model and results written to the same .h5 file or to different .h5 files. The .h5 file provided here must contain results data (either model plus results or results only) providing an .h5 file that contains only model data is considered an error and the method will raise an exception. If omitted AND modelResult is set to "Results" or 'Both", the file name provided for feModelFileName will used.
- `modelType` — Optional enumeration of the file format of the FE Model that is being imported. Currently only the Nastran file format is supported using apex.mesh.FEModelFormat.NastranBulk. Future release may add support for .op2, Abaqus, LS-Dyna etc.
- `unitSystemName` — The name of the Apex unit system that contains the units in which the imported file is be assumed to be. For example 'mm-kg-s-N'.
- `organizeBy` — Optional enumeration (default = apex.mesh.FEModelImportOrganizationOptions.ByContiguousMesh) to select the approach for organizing the model after import.
- `skip` — Optional List of Nastran keywords that will be skipped during import. Default is to read ALL keywords.
- `modelResultsImportOptions` — Optional enumeration argument used to control whether model data, results data or both model and results data will be imported. Use apex.ModelResultsImportOptions.Undefined (Default) to let "feResultsFileName" determine whether to import results or not. apex.ModelResultsImportOptions.Both will cause both model and results data to be imported. use "apex.ModelResultsImportOptions.Model" or "apex.ModelResultsImportOptions.Results" to import only Model or only Results Data.
- `idConflictResolutionMethod` — Optional enumeration argument (default = apex.attributes.IdConflictResolutionMethod.AutomaticOffset) to control how duplicate FE ID's are handled during import of an FE model into an existing Apex Model. The default apex.attributes.IdConflictResolutionMethod.AutomaticOffset will cause the ID's of any FE entities (Nodes, Elements, Materials, Properties, Loads, Constraints etc.) to be offset automatically during import if entities with the same ID's already exist. Setting this value apex.attributes.IdConflictResolutionMethod.AllowDuplicates will preserve the ID's of the imported FE entities even if existing entities are using the same IDs.
- `detectFlexibleLink` — Optional boolean argument (default = True) that will cause any CBAR elements reference PBAR or PBARL entries that define circular cross sections to be imported to 1D Flexible connectors.
- `set3ToGroup` — Optional boolean argument (default = True) determines whether the sets defined by SET3 cards will be imported as groups in Apex.
- `preserveIncludeFileStructure` — Optional boolean argument (default = False) If true, the BDF include file structure is preserved in the imported model.

Returns: the top level Part, Assembly or Scenario that is created.

#### `importGendesResults(resultFolder: str, studyName: str, scenarioName: str, designPart: str = "") -> apex.Entity`
Imports a Generative Design result file into this Apex Study and returns (as an Entity) the scenario that is created for the import results.

- `resultFolder` — The fully qualified name of the Generative design result folder that is being imported.
- `studyName` — The fully qualified name of the study to be created for the import results.
- `scenarioName` — The fully qualified name of the scenario to be created for the import results.
- `designPart` — The name of the design part used to generated the result within Generative design application. By default, the argument is undefined, and the design part will not be present in post process. When the argument is defined, the design part will be present in post.

Returns: the scenario that is created for the import results.

#### `importGeometry(geometryFileNames: [str], importSolids: bool = True, importSurfaces: bool = True, importCurves: bool = True, importPoints: bool = True, importGeneralBodies: bool = True, importHiddenGeometry: bool = True, importCoordinate: bool = False, importDatumPlane: bool = False, cleanOnImport: bool = True, removeRedundantTopoOnimport: bool = True, loadCompleteTopology: bool = True, sewOnImport: bool = False, skipUnmodified: bool = False, importFilter: {str:bool} = {}, preview: bool = False, importReviewMode3dxmlCleanOnImport: bool = True, importReviewMode3dxmlSplitOnFeatureVertexAngle: bool = True, importReviewMode3dxmlFeatureAngle: float = 40.0, importReviewMode3dxmlVertexAngle: float = 40.0, importReviewMode3dxmlDetectMachinedFaces: bool = False, importAttributes: bool = False, importPublications: bool = False) -> {str:apex.Entity}`
Imports a target CAD model from the input CAD files and returns a Dictionary representing the Part / Assembly structure of that CAD model. If preview option is set as "False" by default, import geometry will return dictionary{ str: apex.entity }.The returned dictionary has keys of type string and values of type apex.entity.Each key represents the fully qualified path name of an Assembly or Part in the target CAD model.The apex.entity indicates the entity shown in Apex either from the top level Part or Assembly of the target CAD model. If neither of the "skipUnmodified" or "importFilter" arguments are supplied, all Parts and Assemblies in the target CAD model will be imported - and the Boolean values in the dictionary will be "True" for all Parts and Assemblies. If the "skipUnmodified" argument is "True", Apex will attempt to determine if the target CAD model has previously been imported into this Apex Model, and if it has, will attempt to determine which Parts / Assemblies in the target CAD Model have been modified or added since the last import.Any Parts or Assemblies that are determined to be unchanged since the last import will be skipped during import. The optional "importFilter" argument is a Dictionary with string type keys and Boolean values and has the same form as the dictionary returned by this method.When supplied as an input to this method the Boolean values associated with each Part / Assembly determines whether the Part / Assembly will be imported or ignored.True values will cause the Part / Assembly to be imported and False values will cause it to be ignored. If the optional "preview" argument is True, this method will not complete the import of the CAD model.Please use importGeometryPreview() to get the result of preview.

- `geometryFileNames` — A List of the path qualified file geometry file names
- `importSolids` — Optional boolean argument to control whether Solid geometry types will be Imported or ignored. The default value of "True" will cause all Solid geometry to be imported. Setting to False will cause Solid geometry to be ignored (Not imported)
- `importSurfaces` — Optional boolean argument to control whether Surface geometry types will be Imported or ignored. The default value of "True" will cause all Surface geometry to be imported. Setting to False will cause Surface geometry to be ignored (Not imported)
- `importCurves` — flag. Optional boolean argument to control whether Curve geometry types will be Imported or ignored. The default value of "True" will cause all Curve geometry to be imported. Setting to False will cause Curve geometry to be ignored (Not imported)
- `importPoints` — Optional boolean argument to control whether Point geometry types will be Imported or ignored. The default value of "True" will cause all Point geometry to be imported. Setting to False will cause Point geometry to be ignored (Not imported)
- `importGeneralBodies` — Optional boolean argument to control whether GeneralBody (Non-manifold Surfaces) geometry types will be Imported or ignored. The default value of "True" will cause all GeneralBody geometry to be imported. Setting to False will cause GeneralBody geometry to be ignored (Not imported)
- `importHiddenGeometry` — Optional boolean argument to control whether geometry that is marked as hidden in geometry file will be Imported or ignored. The default value of "True" will cause all geometry to be imported visible or hidden. Setting to False will cause any geometry that is marked as hidden in the geometry file to be ignored (Not imported)
- `importCoordinate` — Optional boolean argument to control whether Coordinate Systems will be Imported or ignored. The default value of "True" will cause all Coordinate Systems to be imported. Setting to False will cause Coordinate Systems to be ignored (Not imported)
- `importDatumPlane` — Optional boolean argument to control whether Datum Planes will be Imported or ignored. The default value of "True" will cause all Datum Planes to be imported. Setting to False will cause Datum Planes to be ignored (Not imported)
- `cleanOnImport` — Optional boolean argument to control whether the imported geometry will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is"
- `removeRedundantTopoOnimport` — Optionally remove redundant faces during import. Redundant faces are faces that share the same underlying geometry and do no impact the topology of neighboring faces. Default = True
- `loadCompleteTopology` — Optionally "load complete topology" geometry as part of the import operation. Default = True
- `sewOnImport` — Optionally "Sew" geometry edges as part of the import operation. Default = False
- `skipUnmodified` — Optional Boolean argument (default = False) that determines whether the system will import all of the Parts and/or Assemblies in the target set of files in geometryFilenames or only the subset that has changed since the last import. If set to True, Apex will examine (recursively) every Part and Assembly in the target set of Geometry files to import and will import only those Parts and Assemblies that it can determine have changed since the last import. To determine which Parts or Assemblies Apex believes have changed or added WITHOUT importing the CAD model, set this argument to True and also se the "preview" argument to True - this will cause the method to return the Dictionary and for each Part/Assembly a Boolean value that indicates whether the Part?assembly would have been imported (if "preview" was omitted or set to False). A True value associated to a Part/Assembly indicates that Apex has determined that the Part/Assembly has changed since the last import and will be re-imported.
- `importFilter` — Optional import filter to control which Parts and Assemblies in the input Assembly will be imported. importFilter is a Dictionary with string keys and Boolean values. Each key contains the fully qualified path name of the Part/Assembly in the imported CAD model and the associated Boolean value indicates whether the associated Part/Assembly should be imported or ignored. Parts/Assemblies with True values will be imported while False values will cause the associated Part/Assembly to be ignored and not imported. If a parent item in the tree (Assembly, sub-Assembly) is ignored (False) then all of its children will be silently ignored, even if they are marked as "True" Although it is possible to construct importFilter manually, it is recommended to execute this method with the "preview" argument set to True and this value set to False. This will cause the method to interrogate the target CAD model and return the Dictionary containing the Part/Assembly structure only. You can then be sure that the dictionary matches the structure in the CAD model. Users can then modify the Boolean values and execute the method again, using the modified dictionary for this argument.
- `preview` — Optional argument that defines whether the content of the target CAD files will be completely imported into Apex or if the method will simply interrogate the structure of the CAD model and return the model structure only. If False (Default) the model contained in the target geometryFileNames will be imported directly to Apex according to the values of the other arguments. If True, this method will not complete the import of the CAD model. Please use importGeometryPreview() to get the result of preview.
- `importReviewMode3dxmlCleanOnImport` — Optional boolean argument to control whether the imported review mode 3dxml file will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is".
- `importReviewMode3dxmlSplitOnFeatureVertexAngle` — Optional argument used to control the creation of faceted geometry bodies by taking account the feature and vertex angle, the default is True. If it is set as false, then the arguments of "importReviewMode3dxmlFeatureAngle" and "importReviewMode3dxmlVertexAngle" will be ignored.
- `importReviewMode3dxmlFeatureAngle` — 0ptional argument used to control the creation of faceted geometry bodies. Topological geometry edges will be created between any faces of the 3dxml data that have subtended angles greater than this value. featureAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system
- `importReviewMode3dxmlVertexAngle` — Optional argument used to control the creation of faceted geometry bodies. Topological geometry vertices will be created between any edges of the 3dxml data that have subtended angles greater than this value. vertexAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system
- `importReviewMode3dxmlDetectMachinedFaces` — This is an optional argument. When on, this triggers an algorithm to search for possible machined faces. When found, these will be split into separate faces. The types of faces that can be found are planar, cylinder, and torus faces. Depending on the smoothness and accuracy of the input tessellation, these will be detected and partitioned into separate faces. The intended use case is a model with mostly organic faces that as some analytical faces machined into it. For models that come primarily from analytical faces, such as STL from CAD or STL from FEM meshes that were applied to CAD, it is better to import as Mesh, then use the facet body tool in Apex to convert to facet bodies and optionally NURBS. It will be ignored if the argument "importReviewMode3dxmlSplitOnFeatureVertexAngle" is set as True.
- `importAttributes` — Optional boolean argument that defines whether the attributes of the target CAD files will be imported into Apex. If False (Default) the attributes in the CAD files will be ignored. If True, the method will import the attributes in the CAD files and convert them as Apex User Attributes after import. In 2021.2 release, Apex supports the following attributes: Parasolid System Attributes: body_density and colour. Catia V5 Properties. 3D Experience Properties.
- `importPublications` — Optionally import the Publications from Catia V5 and 3D Experience files. Default = False.

#### `importGeometryPreview(geometryFileNames: [str]) -> {str:bool}`
Previews a target CAD model from the input CAD files and returns a Dictionary representing the Part/Assembly structure of that CAD model. The supported CAD file formats are: CATIA V5 Solidworks Inventor Pro/E.

- `geometryFileNames` — A List of the path qualified file geometry file names.

#### `importMarc(filename: str, unitSystem: str, importHierarchicalFiles: bool = False, renumberMethod: apex.attribute.ImportRenumberMethod = apex.attribute.ImportRenumberMethod.Internal, importAbstractions: bool = False) -> apex.Entity`
Imports the contents of the Model to a Marc file. All objects in the Model that can be mapped to Marc keywords will be imported. If the Model contains multiple top level Parts or Assemblies the method will throw an exception. Use the equivalent method on each top Level Part or Asssembly instead or re-organize your model into a singel top level Assembly. The method arguments provide control over import options. Only bulk data entries are imported when this method is called from the Model class - to import Case (and other Marc file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over import options.

- `filename` — Fully qualified name of the file to which the finite element objects will be imported.
- `unitSystem` — The name of a consistent unit system to use when importing Marc files. The valid unit system names are "m-kg-s-N"; // Standard SI units (meter-kilogram-second) "cm-kg-s-cN"; // SI units with length in centimeters "cm-kg-ms-dakN"; // SI units with length in centimeters and time in milliseconds "cm-kg-us-daGN"; // SI units with length in centimeters and time in microseconds "mm-kg-ms-kN"; // SI units with length in millimeters and time in milliseconds "cm-g-s-dyn"; // Standard centimeter-gram-second (CGS) units "cm-g-us-daMN"; // CGS units with time in microseconds "mm-g-s-uN"; // CGS units with length in millimeters "mm-g-ms-N"; // CGS units with length in millimeters and time in milliseconds "mm-t-s-N"; // SI units with length in millimeters and mass in metric tons "in-slinch-s-lbf"; // English engineering units with mass in slinches (1 slinch = 12 slugs) "ft-slug-s-lbf"; // English engineering units with mass in slugs (1 slug = 32.174 pounds) "mm-khyl-s-kgf"; // Kilogram-force units with mass in kilohyls and length in millimeters "mm-kg-s-mN"; // SI units with length in millimeters "cm-g-ms-daN"; // CGS units with time in milliseconds "ft-lb-s-lbf"; // Standard English engineering units (foot-pound-second)
- `importHierarchicalFiles` — A Boolean quantity to control whether the imported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single flat file. The default value of "False" causes a single file to be written containing all of the finite element entities within the Assembly to be written.
- `renumberMethod` — An enumeration to control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the imported Model Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Marc jobs require these ID's to be unique within the scope of the Marc run. This enumeration is used to control how Apex resolves duplicate ID's when models are being imported as Marc files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "import" causes the renumbering operation to be applied ONLY to the imported Marc file and has no impact on the ID's within Apex.
- `importAbstractions` — A Boolean quantity to control whether the imported data contains Apex Engineering Abstractions.

#### `importModelAssociation(associationFilename: str) -> ModelAssociationCollection`
import ModelAssociation from file.

- `associationFilename` — The name of the file that the ModelAssociation data will be imported from.

Returns: the ModelAssociationCollection The list of ModelAssociation

#### `importRegisteredAdamsCarAssembly(databaseAlias: str = "", assemblyName: str = "") -> Assembly`
Imports an Adams/Car assembly from an Adams/Car database when the database has previously been registered in the Adams/Car config file. To import Databases that have not yet been registered with the Adams/Car config file, use importUnregisteredAdamsCarAssembly.

- `databaseAlias` — The alias for the Adams/Car database that contains the target Adams/Car Assembly. If the alias does not exist in the Adams/Car config file the method will raise an exception.
- `assemblyName` — The name of the assembly to import, including the file extension. This assembly must exist in the database referenced by databaseAlias or the method will raise an Exception. The assembly name must be provided with an extension or the method will raise an Exception.

Returns: the top Assembly of imported model

#### `importSTL(stlFileNames: [str], importBodyType: apex.geometry.STLImportBodyType = apex.geometry.STLImportBodyType.Mesh, featureAngle: float = 40.0, vertexAngle: float = 40.0, splitOnAngle: bool = True, detectMachinedFace: bool = False, unitSystem: str = "m", cleanOnImport: bool = True) -> {str:apex.Entity}`
Imports one or more STL files into this model and creates either mesh or geometry bodies depending on the supplied input values. Each STL file will be imported into a new Part that is a top level child of this Model. One mesh or geometry body will be created from each set of contiguous faces/lines in each STL file. If a set of contiguous faces in the STL file represents a watertight set and the the system will create an importBodyType is Facet, the system will create a facetted Solid body, otherwise the system will create a facetted Surface Import STL will return dictionary {str: apex.entity}.The returned dictionary has keys of type string and values of type apex.entity. Each key represents the fully qualified path name of an Part in the target CAD model. The apex.entity indicates the part of the target CAD model.

- `stlFileNames` — List of fully qualified path names of the STL files to be imported.
- `importBodyType` — An enumeration defining the type of Apex body that will be created from the STL data. STL data can be used to create either mesh or facetted geometry bodies based on the value of this argument. The default value of apex.geometry.STLImportBodyType.Mesh will cause the creation of MeshBodies from the STL data. Setting the value of this argument to apex.geometry.STLImportBodyType.Faceted will cause the system to create faceted geometry bodies.
- `featureAngle` — Optional argument used to control the creation of faceted geometry bodies. Topological geometry edges will be created between any faces of the STL data that have subtended angles greater than this value. This argument will be silently ignored if importBodyType is set to Mesh. featureAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system
- `vertexAngle` — Optional argument used to control the creation of faceted geometry bodies. Topological geometry vertices will be created between any edges of the STL data that have subtended angles greater than this value. This argument will be silently ignored if importBodyType is set to Mesh. vertexAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `splitOnAngle` — Optional argument used to control the creation of faceted geometry bodies. Default = True. Topological geometry edges and vertices will be created according to featureAngle and vertexAngle value. This argument will be silently ignored if importBodyType is set to Mesh.
- `detectMachinedFace` — This is an optional argument. When on, this triggers an algorithm to search for possible machined faces. When found, these will be split into separet faces. The types of faces that can be found are planar, cylinder, and torus faces. Depending on the smoothness and accuracy of the input tessellation, these will be detected and partitioned into separate faces. This only applies to STL imported as facet body. If imported as mesh this is ignored. The intended use case is a model with mostly organic faces that as some analytical faces machined into it. For models that come primarily from analytical faces, such as STL from CAD or STL from FEM meshes that were applied to CAD, it is better to import as Mesh, then use the facet body tool in Apex to convert to facet bodies and optionally NURBS.
- `unitSystem` — A string to identify the units to be used during import STL. unitSystem value can be m, cm, mm, ft or in.
- `cleanOnImport` — Optionally "Clean" geometry as part of the import opertation . Default = True

#### `importUnregisteredAdamsCarAssembly(databaseAlias: str, assemblyName: str, databasePathname: str) -> Assembly`
Imports and registers and Adams/Car assembly from an Adams/Car database when the database has NOT previously been registered in the Adams/Car config file. To import Databases that have already been registered with the Adams/Car config file, use importRegisteredAdamsCarAssembly instead.

- `databaseAlias` — The alias for the Adams/Car database that contains the target Adams/Car Assembly. If the alias does not exist in the Adams/Car config file or the alias is associated with a database that is not present at the location defined in the config file this method will raise an exception.
- `assemblyName` — The name of the assembly to import. This assembly must exist in the database referenced by databaseAlias or the method will raise an Exception.
- `databasePathname` — The fully qualified pathname of the Adams/Car database.

Returns: the top Assembly of imported model

- `isCurrent() -> bool` — Returns bool representing whether the model is current and can be operated on.
- `save() -> None` — Save all changes to the Model since the last Save.
#### `saveAs(name: str, path: str) -> Model`
Save the model to a new DB.

- `name` — of the new model.
- `path` — to the new model.

Returns: the newly created Model

#### `setCurrentPart(pathName: str) -> Part`
Set the 'current' Part in this Model.

Returns: the current Part


## `apex.ModelAssociation`  (extends `Entity`, `IName`)
Class defining the association between two Models.
Properties: `interfaceLoadAssociations`, `partAssociations`, `primaryAssembly`, `secondaryAssembly`

Methods:

- `ModelAssociation() -> None`
#### `associateLoadTransferPoints(primaryAssemblyLoadTransferPoint: apex.attribute.InterfacePoint, secondaryAssemblyLoadTransferPoint: apex.attribute.NodeTie) -> None`
Associates an InterfacePoints in the primary Assembly with a NodeTies in the secondary Assembly.

- `primaryAssemblyLoadTransferPoint` — An InterfacePoint in the primary Assembly.
- `secondaryAssemblyLoadTransferPoint` — A NodeTie in the secondary Assembly.

#### `associatePartsAutomatic(scope: apex.ModelAssociationScope, parts: apex.PartCollection = None, mappingTolerance: float = 5, onlyMapUnmappedParts: bool = True, hideAfterMapping: bool = True) -> bool`
Automatically associates Parts and/or Assemblies from the secondary assembly to a Parts in the primary assembly using a proximity tolerance algorithm.

- `scope` — An optional Enumeration that controls the scope of the model that will be considered for automatic association between the primary and secondary assemblies of this ModelAssociations. Supported options are "All" (Default) "Visible" and "Selected"
- `parts` — Optional collection of Parts from the secondary Assembly that will be considered for automatic association to Parts in the primary Assembly. This argument must be defined if the scope argument is set to "Selected", otherwise it is silently ignored.
- `mappingTolerance` — Optional tolerance (Default = 5mm) used to determine whether Parts in the secondary Assembly will be associated to Parts in the primary Assembly.
- `onlyMapUnmappedParts` — Optional Boolean argument (default = True) that controls whether Parts and Assemblies that have already been mapped will be skipped by this method or whether they will be re-mapped.
- `hideAfterMapping` — Optional Boolean argument that controls whether Parts mapped by this method will be hidden from the viewports after mapping (True) or left visible (False).

#### `associatePartsManual(primaryPart: apex.Part, secondaryPartsAssemblies: apex.EntityCollection, hideAfterMapping: bool = True) -> bool`
Manually associates Parts and/or Assemblies from the secondary Assembly with a Part in the primary Assembly. Any Parts in the secondary assembly that have already been associated with a Part in the primary assembly (within the scope of this ModelAssociation) will be removed form the previous association before being added to the association created by this method.

- `primaryPart` — The Part in the primary Assembly to which the input Parts and/or Assemblies from the secondary Assembly will be mapped.
- `secondaryPartsAssemblies` — One or more Parts and/or Assemblies in the secondary assembly that are intended to be mapped to the primaryPart. Any Parts/Assemblies in this collection that are within tolerance of the primary Part will be associated to the primary Part (unless they are already associated to another Part AND onlyMapUnmappedParts is True).
- `hideAfterMapping` — Optional Boolean argument that controls whether Parts mapped by this method will be hidden from the viewports after mapping (True) or left visible (False).

#### `exportAssociationData(fileName: str) -> bool`
Exports the model association data from this ModelAssociation to an external file in .txt format.

- `fileName` — The name of the file that the ModelAssociation data will be exported to.

#### `getDescription() -> str`
Read-only string representing the description of this object. The description field usually appears the Object Property panel in the interactive UI and in some cases will appear in the Tool property panel of the tool that creates the object.

Returns: this entity description (string)

getDescription() may also be accessed as an Entity property 'description'. For example:

#### `getInterfaceLoadAssociations() -> {str:apex.attribute.NodeTie}`
a dictionary defining the association between InterfacePoints in the primary Assembly and NodeTies in the secondary Assembly.

Returns: a dictionary defining the association between Parts in the primary Assembly and Parts/Assemblies in the secondary Assembly. The dictionary key is a string type where the string represents the pathName of the InterfacePoint in the primary Assembly The dictionary value is an Entity representing the NodeTie in the secondary Assembly where the load from the primary Assembly will be applied on the secondary Assembly.

#### `getName() -> str`
Read-only string representing the name of this object.

Returns: this entity name (string)

getName() may also be accessed as an Entity property 'name'. For example:

#### `getPartAssociations() -> {str:apex.EntityCollection}`
get part associations.

Returns: a dictionary defining the association between Parts in the primary Assembly and Parts/Assemblies in the secondary Assembly. The dictionary key is string type where the string represents the pathName of the Part in the primary Assembly The dictionary value is an EntityCollection holding the Parts/Assemblies that are associated with the Part identified by the key

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/

#### `getPrimaryAssembly() -> apex.Assembly`
get primary assembly.

Returns: the primary assembly of this ModelAssociation

#### `getSecondaryAssembly() -> apex.Assembly`
get secondary assembly.

Returns: the secondary assembly of this ModelAssociation

#### `removeLoadTransferPointAssociation(loadTransferPointAssociation: str) -> None`
Removes an existing load transfer point association from this ModelAssociation. The association to be removed is identified using the pathName of the InterfacePoint from the secondary Assembly.

- `loadTransferPointAssociation` — The pathName of the InterfacePoint from which to remove all secondary NodeTie associations. If an association referencing this InterfacePoint does not exist within this ModelAssociation the method will return silently.

#### `removePartAssociation(partAssociation: str) -> bool`
Removes an existing Part Association from this ModelAssociation.

- `partAssociation` — The pathName of the primary Part from which to remove all secondary Part/Assembly associations. If an association referencing this Part does not exist within this ModelAssociation the method will return silently.

#### `update(name: str = "", description: str = "#####", primaryAssembly: apex.Assembly = None, secondaryAssembly: apex.Assembly = None) -> ModelAssociation`
Update this model association. One or more properties may be updated in each call to update().

- `name` — An optional name for this ModelAssociation. If omitted the system will assign a unique name based on the prefix "Model Association " and appending an integer to ensure name uniqueness for all ModelAssociations within the scope of the top level Apex Model.
- `description` — An optional description for this ModelAssociation.
- `primaryAssembly` — The primary Assembly for this ModelAssociation. Each Part in this Assembly may subsequently be associated with one or more Parts and/or Assemblies in the secondary Assembly.
- `secondaryAssembly` — The secondary Assembly for this ModelAssociation. Parts and or Assemblies from this Assembly may subsequently be associated with a single Part from the primary Assembly.

Returns: the ModelAssociation


## `apex.ModelAssociationCollection`  (extends `EntityCollection`)

Methods:

- `ModelAssociationCollection() -> None` — Construct a new ModelAssociationCollection.

## `apex.ModelRep`  (extends `Entity`)
A ScenarioModelRep that represents an Assembely rep or part rep that is associated with a Scenario.

Methods:

- `asAssemblyRep() -> apex.AssemblyRep`
- `asPartRep() -> apex.Part`

## `apex.ModelSet3Nastran`  (extends `ModelSetNastran`)
Class representing a Nastran SET3 bulk data entry. SET3 defines a list of Grid, Element, Point, Property, RBE (inclusive/exclusive options) or Module IDs.
Properties: `set_ids`, `set_type`

Methods:

- `getSetIds() -> [int]` — Gets a property defining the IDs of the entity types specified by the set_type property This property may be assigned an iterable (List, Array etc) of ints.
- `getSetType() -> str` — Gets a property used to define the type of entity that the IDs defined in this ModelSet3Nastran represnt This property may be assigned any one of the following values, "GRID" - The IDs represent the IDs of finite element Grids (Nodes) "ELEM" - The IDs represent the IDs of finite element Elements "POINT" - The IDs represent the IDs of finite element Points "PROP" - The IDs represent the IDs of element properties "RBEin" - The IDs represent the IDs of rigid elements (to be INCLUIDED in MPC selections) "RBEex" - The IDs represent the IDs of rigid elements (to be EXCLUDED from MPC selections)
- `setSetIds(set_ids: [int]) -> None` — Sets a property defining the IDs of the entity types specified by the set_type property This property may be assigned an iterable (List, Array etc) of ints.
- `setSetType(set_type: str) -> None` — Sets a property used to define the type of entity that the IDs defined in this ModelSet3Nastran represnt This property may be assigned any one of the following values, "GRID" - The IDs represent the IDs of finite element Grids (Nodes) "ELEM" - The IDs represent the IDs of finite element Elements "POINT" - The IDs represent the IDs of finite element Points "PROP" - The IDs represent the IDs of element properties "RBEin" - The IDs represent the IDs of rigid elements (to be INCLUIDED in MPC selections) "RBEex" - The IDs represent the IDs of rigid elements (to be EXCLUDED from MPC selections)

## `apex.ModelSetNastran`  (extends `Entity`)
Base class for a series of specializations representing Nastran bulk data SET1, SET2, SET3 and SET4 entries.
Properties: `id`, `name`

Methods:

- `clone() -> ModelSetNastran` — Creates a copy of this ModelSetNastran. The copy will be created by default in the same model set as the original, however if the optional "model_set" argument is provided, the copy will be created in the ModelSetNastran that it references All properties of the original ModelSetNastran will be copied with the exception of the id which will be replaced by a new unique ID.
- `getId() -> int` — Gets the ID of this SET.
- `getName() -> str` — Gets the name of this SET.
- `setId(id: int) -> None` — Sets the ID of this SET.
- `setName(name: str) -> None` — Sets the name of this SET.

## `apex.Orientation`  (extends `IsConstructed`, `IOrientation`)

Methods:

#### `Orientation(alpha: float = 0.0, beta: float = 0.0, gamma: float = 0.0) -> None`
Orientation constructor.Optional arguments enable the Orientation to be constructed relative to the global Carteaisn coordinate system using Euler angles based on the Euler 313 rotation convention.A default value of 0.0 will be used for any omitted arguments.If all arguments are omitted the Orientation will be created aligned with the global Cartesian system.

- `alpha` — an optional float value representing the first Euler rotation angle(default = 0.0) based on the Euler 313 rotation convention and relative to the global Cartesian system.alpha represents an Angle value and must be supplied in the Angle units of the active script unit system
- `beta` — an optional float value representing the second Euler rotation angle(default = 0.0) based on the Euler 313 rotation convention and relative to the global Cartesian system.beta represents an Angle value and must be supplied in the Angle units of the active script unit system
- `gamma` — an optional float value representing the third Euler rotation angle(default = 0.0) based on the Euler 313 rotation convention and relative to the global Cartesian system.gamma represents an Angle value and must be supplied in the Angle units of the active script unit system

#### `Orientation(xAxis: apex.construct.Vector3D = Internally determined, yAxis: apex.construct.Vector3D = Internally determined, zAxis: apex.construct.Vector3D = Internally determined) -> None`
Orientation constructor. Optional arguments enable the Orientation to be constructed with its initial orientation defined by axis vectors.Each axis vector is assumed to be supplied in the global Cartesian system. If no axis vectors are provided the Orientation will be aligned with the global Cartesian system If only one axis vector is provided the Orientation axis associated with that vector is guaranteed to be aligned with the input vector the directions of the other two Orientation axes are only guaranteed to be perpendicular to each otherand to the first axis if multiple axis vectors are providedand are not mutually perpendicular the Orientation will be created as follows, the Orientation axis associated with the first input axis is guaranteed to be aligned with the input axis the Orientation axis associated with the second input axis will be orthogonal to the firstand is guaranteed to be in the plane defined by the first Orientation axisand the second input axis.The second Orientation axis therefore may not be the same as second input axis if the second input axis is not orthogonal to the first The Orientation axis associated with the third input axis will be crated orthogonal to the first two Orientation axes.

- `xAxis` — an optional float value representing the first Euler rotation angle (default = 0.0) based on the Euler 313 rotation convention and relative to the global Cartesian system. alpha represents an Angle value and must be supplied in the Angle units of the active script unit system
- `yAxis` — an optional float value representing the second Euler rotation angle (default = 0.0) based on the Euler 313 rotation convention and relative to the global Cartesian system. beta represents an Angle value and must be supplied in the Angle units of the active script unit system
- `zAxis` — an optional float value representing the third Euler rotation angle (default = 0.0) based on the Euler 313 rotation convention and relative to the global Cartesian system. gamma represents an Angle value and must be supplied in the Angle units of the active script unit system

- `getAlpha() -> float` — Float value representing the first Euler rotation angle based on the Euler 313 rotation convention. alpha represents an Angle value and is returned in the Angle units of the active script unit system.
- `getBeta() -> float` — Float value representing the second Euler rotation angle based on the Euler 313 rotation convention. beta represents an Angle value and is returned in the Angle units of the active script unit system.
- `getGamma() -> float` — Float value representing the third Euler rotation angle based on the Euler 313 rotation convention. beta represents an Angle value and is returned in the Angle units of the active script unit system.
- `getXAxis() -> apex.construct.Vector3D` — The direction of the x axis of this Orientation as a Vector3D.
- `getYAxis() -> apex.construct.Vector3D` — The direction of the y axis of this Orientation as a Vector3D.
- `getZAxis() -> apex.construct.Vector3D` — The direction of the z axis of this Orientation as a Vector3D.

## `apex.Part`  (extends `Entity`, `IPhysical`, `IDisplayable`, `IUserAttributes`, `IName`, `IActivatable`)
model object that can contain Geometry and FEM data (and have Material and Shell data assigned). Create using Model or Assembly createPart() method.
Properties: `activeRep`, `axisAlignedBoundingBox`, `beamSpans`, `curves`, `datumPlanes`, `displayableEntities`, `elements`, `entities`, `exclusiveGroups`, `exclusiveRegions`, `facetedCurves`, `facetedSolids`, `facetedSurfaces`, `geometryBodies`, `interfacePoints`, `meshes`, `namedEntities`, `nodes`, `parent`, `partialGroups`, `partialRegions`, `partProperties`, `partReps`, `physicalEntities`, `points`, `referencedBy`, `referenceSystem`, `solids`, `surfaces`

Methods:

#### `applyColorToChildren(color: [int]) -> None`
applies the color of this Part to all its children.

- `color` — 3 vector(list) specifying the Red, Green, and Blue component of the color. Each value should be in the range 0-255.

This method provides the ability to set the parent container's setting to all children settings. This method actually changes the childrens' settings, not just their display in 3D Graphics.

#### `applyRenderStyleToChildren(renderStyle: apex.session.DisplayRenderStyle) -> None`
applies the Render Style of this Part to all its children.

- `renderStyle` — is the enumeration for the render style.

This method provides the ability to set the parent container's setting to all children settings. This method actually changes the childrens' settings, not just their display in 3D Graphics.

#### `applyTransparencyToChildren(enableTransparency: bool, transparencyLevel: int) -> None`
applies the Transparency setting of this Part to all its children.

- `enableTransparency` — Boolean to enable setting transparency. Default: False
- `transparencyLevel` — The Transparency Level. This is an integer representing the transparency value from 0 (No Transparency) to 100 (Completely Transparent). Any value specified less than 0 will be treated as 0. Any value greater than 100 will be treated as 100. This value is required if enableTransparency is set to True.

This method provides the ability to set the parent container's setting to all children settings. This method actually changes the childrens' settings, not just their display in 3D Graphics.

#### `asEntity() -> Entity`
return the (base) Entity Object of this Part.

Returns: this part Entity object

#### `assignMaterial(pMat: apex.attribute.Material) -> bool`
assign a material to this Part.

Returns: status of true or false (bool)

#### `assignShellSection(pSection: apex.attribute.ShellSection) -> bool`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.attribute.createFieldThicknessOffsetConstant. assign a shell section to this Part.

Returns: status of true or false (bool)

#### `createImportedPartRepFlex(modalNeutralFileName: str) -> apex.PartRep`
create a Imported PartRep in this Part.

- `modalNeutralFileName` — the path qualified file name of MNF file.

Returns: the PartRep

#### `createMeshBody(meshType: apex.mesh.MeshTopology, name: str, description: str, csys: apex.construct.CoordinateSystem, nodeCoordinates: [float], elements: {str:[int]}) -> apex.mesh.MeshBody`
Creates and returns a MeshBody in this Part. The method can create all types of meshBodies supported by Apex - PointMesh, CurveMesh, SurfaceMesh, SolidMesh, HexMesh - using the meshType argument. Nodes and Elements can optionally be created during construction of the MeshBody or added to the MeshBody later.

- `meshType` — Defines the type of mesh that will be created using a MeshType enum.
- `name` — An optional name for the mesh. If omitted, the system will define a default mesh name.
- `description` — An optional description for the MeshBody. If omitted, the Description will be left blank.
- `csys` — An optional CoordinateSystem for the Node coordinates.The CoordinateSystem must be Rectangular, Cylindrical or Spherical.If omitted, the coordinate values are assumed to be in the global coordinate system.If supplied, the coordinate values represents coordinates in this CoordinateSystem.NOTE : If a CoordinateSystem is supplied the coordinate values will be transformed from this coordinate system to global. A future release will extend the Node object to support a definition coordinate system thereby allowing the original coordinates to be retained.
- `nodeCoordinates` — A List of floats defining the coordinates of the nodes.The array contains repeated sequences of x, y and z coordinates, one sequence for each node.The number of array entries must be a multiple of 3.The coordinates represent locations in space and have units of Length therefore the values must be defined in the units of Length of the current ScriptUnitsSystem.Node ID's will be assigned by the system.
- `elements` — The elements that will be created and added to the meshBody during construction. If omitted, no elements will be created during MeshBody construction and elements may be added later using methods provided on the MeshBody. elements is a Dictionary with a key type of apex.mesh.ElementTopology and an associated List[Int] value type. Multiple element types may be added to the MeshBody during construction by including multiple key, value pairs in the Dictionary - one for each ElementType. The value associated with each key is List of integers representing the element Node indices. The Node indices are indices into the provided nodeCoordinates List. When elements are defined during meshBody creation, the nodes that they reference must also be defined during creation. The indices are used to define the topology of the element. Multiple elements of the same type are defined within a single dictionary value by providing sequences of element indices. The length of each sequence is dependent on the element type and the total number of indices in the string must be a multiple of the required number of Nodes for the specific element type. Consider for example a linear triangular shell element. The key for this element type will be apex.mesh.ElementType.Tria. Each element has three nodes, therefore the length of the integer sequence in the corresponding Dictionary value will be three and the total number of entries in the value List must be a factor of three. Consider a MeshBody containing three linear triangular shell elements as follows, Tria 1 is defined by Node indices 1, 2, 3 Tria 2 is defined by Node indices 1, 3, 4 Tria 3 is defined by Node indices 4, 3, 5 In this case the value List would be defined as element_node_ids = [1, 2, 3, 1, 3, 4, 4, 3, 5]

Returns: the MeshBody

- `createNativePartRepFlex(name: str, description: str = "", numberModes: int = 6, maximumFrequency: float = NAN, generateGridPointStresses: bool = True, generateGridPointStrains: bool = True) -> apex.PartRep`
#### `createSketchOnDatumPlane(name: str, datumPlane: apex.construct.DatumPlane, alignSketchViewWithViewport: bool) -> apex.construct.Sketch`
Create and initialize a sketch on the input DatumPlane.

- `name` — The name of the sketch. If omitted the Sketch name will be undefined.
- `datumPlane` — The DatumPlane that defines the plane of the Sketch.
- `alignSketchViewWithViewport` — An optional boolean argument (Default = True) that determines whether or not the Sketch Grid will be automatically aligned with the viewport normal during Sketch creation.

Returns: the created Sketch

#### `createSketchOnGlobalPlane(name: str, plane: apex.construct.GlobalPlane, alignSketchViewWithViewport: bool) -> apex.construct.Sketch`
Create and initialize the sketch given a flat face.

- `name` — Name of the sketch. Default ="" (Future use)
- `plane` — valid planes GlobalPlane.XYGlobalPlane.YZGlobalPlane.XZ
- `alignSketchViewWithViewport` — Orients sketch with screen plane

Returns: the created Sketch

#### `createSketchOnSurface(name: str, face: Entity, reverseNormal: bool, alignSketchViewWithViewport: bool, location: apex.ILocation = None) -> apex.construct.Sketch`
Create and initialize the sketch given a face.

- `name` — Name of the sketch. Default ="" (Future use)
- `face` — face to align sketch
- `reverseNormal` — true the sketch plane normal is in the opposite direction of the face normal.
- `alignSketchViewWithViewport` — Orients sketch with screen plane
- `location` — location on face

Returns: the created Sketch

- `delete_RENAMED_AFTER_SWIG() -> None` — Delete this Part.
#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports this Part to a Nastran file. All objects composed or referenced by the Part that can be mapped to Nastran keywords will be exported. Method arguments provide control over export options. Primarily bulk data entries are exported when this method is called from the Part class, although some case control keywords may also be exported to enable import of mesh independent ties into the other applications. To export case control entries, use the equivalent exportFEModel() method on the Scenario object.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

#### `exportGeometry(filename: str, cadFormat: apex.geometry.CADFormat, unitSystem: str = "m", stlMergeCells: bool = True, exportVirtualFaces: bool = False, exportVirtualFaceMethod: apex.VirtualFaceExportMethod = apex.VirtualFaceExportMethod.NurbsOnly, exportBodyPositionInLocal: bool = False) -> None`
Export Geometry from this Part to a file using the supplied CAD format.

- `filename` — Fully qualified name of the file to which the geometry objects will be exported.
- `cadFormat` — defines the format of the CAD file that will be exported using an apex.geometry.CADFormat enumeration.
- `unitSystem` — A string to identify the units to be used during export. Unit support is dependent on the CADFormat of the exported file and not all formats support units.Of the CAD formats currently supported by Apex, only the IGES/STL format supports user defined export units. The support Length unit: m, cm, mm, ft, in If the IGES/STL format is selected, unitSystem will be available. If it is undefined, use the default unitSystem = m. If a value other than one in the above unit is supplied, the method will throw an exception
- `stlMergeCells` — optional Boolean argument (default = True) that controls how multi-cellular solids will be represented in STL files. This argument is only relevant when the cadFormat type is an STL type and is silently ignored for all other formats. When True (Default), all cells in a multi-cellular solid will be merged into a single cell during export by removing all internal Faces. The GeometryBody is unaffected by this operation. When False, all cells in multi-cellular solids will be present in the exported STL file.
- `exportVirtualFaces` — Optional Argument, Default = False, where each virtual faces will be exported as a single face. This only applies to CAD Format Parasolid. The purpose is to export geometry topology that is consistent with native Apex to maintaining associatively with mesh, loads, BCs and other attributes. An attempt will be made to export the virtual faces as NURBS, by replacing the each virtual face with a single NURBS face. If this fails, then a facet body face will be used instead.
- `exportVirtualFaceMethod` — This applies to exportGeometry API only. It controls what is permitted for converting virtual topology to exportable faces with the same topology. This is ignored if exportVirtualFaces is False. If set to NurbsAndFaceted, then the system will try to convert to NURBS, and if that fails, it will then convert the face into a faceted face. If set to NurbsOnly (Default), then it will try to convert each virtual face to NURBS only.
- `exportBodyPositionInLocal` — Optional Boolean argument to export the geometry body in local position based the reference system of the body and parent part. By default, it is false. The system will export the geometry body position in global.

#### `exportMarc(filename: str, unitSystem: str, exportWideFormat: bool = False, exportAbstractions: bool = False) -> None`
Exports the contents of the Part to a Marc file. All objects in the Part that can be mapped to Marc keywords will be exported. Only bulk data entries are exported when this method is called from the Part class - to export Case (and other Marc file sections) use the equivalent method on the Scenario class instead. The method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.

#### `getActivePartRep() -> apex.PartRep`
returns the active partRep.

Returns: the active partRep

#### `getBeamSpan(name: str) -> apex.attribute.BeamSpan`
Get a BeamSpan in this Part.

- `name` — of the BeamSpan to get.

Returns: the BeamSpan

#### `getBeamSpans() -> apex.attribute.BeamSpanCollection`
Returns read only collection of all BeamSpans contained by the Part.

Returns: Read only collection of all BeamSpans contained by the Part

#### `getBox(name: str) -> apex.geometry.Box`
Get a Box in this Part.

- `name` — of the Box to get.

Returns: the Box

#### `getBoxes() -> apex.geometry.BoxCollection`
Get all Boxes in this Part.

Returns: Iterable collection of all the Boxes in this part

getBoxes() may also be accessed as a Part object property 'boxes'. For example:

#### `getCurve(name: str) -> apex.geometry.Curve`
Get a Curve in this Part.

- `name` — of the Curve to get.

Returns: the Curve

#### `getCurves() -> apex.geometry.CurveCollection`
Get all Curves in this Part.

Returns: Iterable collection of all the Curves in this part

getCurves() may also be accessed as a Part object property 'curves'. For example:

#### `getCylinder(name: str) -> apex.geometry.Cylinder`
Get a Cylinder in this Part.

- `name` — of the Cylinder to get.

Returns: the Cylinder

#### `getCylinders() -> apex.geometry.CylinderCollection`
Get all Cylinders in this Part.

Returns: Iterable collection of all the Cylinders in this part

getCylinders() may also be accessed as a Part object property 'cylinders'. For example:

#### `getDatumPlane(name: str) -> apex.construct.DatumPlane`
Retrieves a named DatumPlane from this Part.

- `name` — The name of the DatumPlane to retrieve.

Returns: the DatumPlane

#### `getDatumPlanes() -> apex.construct.DatumPlaneCollection`
Returns all DatumPlanes directly composed by this Part.

Returns: the DatumPlaneCollection

#### `getDisplayableEntities() -> apex.EntityCollection`
returns a collection of all entities in this Part that implement IDisplayable as an EntityCollection.

Returns: this Entity objects

#### `getElements(target: apex.Entity) -> apex.mesh.ElementCollection`
get the elements on this Entity (GeometryBody/GeometryTopology).

Returns: collection of elements

#### `getEllipsoid(name: str) -> apex.geometry.Ellipsoid`
Get a Ellipsoid in this Part.

- `name` — of the Ellipsoid to get.

Returns: the Ellipsoid

#### `getEllipsoids() -> apex.geometry.EllipsoidCollection`
Get all Ellipsoids in this Part.

Returns: Iterable collection of all the Ellipsoids in this part

getEllipsoids() may also be accessed as a Part object property 'ellipsoids'. For example:

#### `getEntities() -> apex.EntityCollection`
Get all Entities in this Part.

Returns: Iterable collection of all the Entities in this part

getEntities() may also be accessed as a Part object property 'entities'. For example:

#### `getExclusiveGroups(recursive: bool = True) -> apex.GroupCollection`
returns a GroupCollection of all Groups that exclusively reference ONLY Entities composed by this Part. To return Groups that reference at least one entity that is composed by this Part use the partialGroups property.

- `recursive` — boolean flag specifying whether child objects of the entity will be included (default = True).

Returns: a GroupCollection of all Groups that exclusively reference ONLY Entities composed by this Part.

#### `getExclusiveRegions(recursive: bool = True) -> apex.RegionCollection`
returns a RegionCollection of all Regions that exclusively reference ONLY Entities composed by this Part. To return Regions that reference at least one entity that is composed by this Part use the partialRegions property.

- `recursive` — boolean flag specifying whether child objects of the entity will be included (default = True).

Returns: a RegionCollection of all Regions that exclusively reference ONLY Entities composed by this Part.

#### `getFacetedCurve(name: str) -> apex.geometry.FacetedCurve`
Get a Faceted Curve in this Part.

- `name` — of the Faceted Curve to get.

Returns: the FacetedCurve

#### `getFacetedCurves() -> apex.geometry.FacetedCurveCollection`
Get all Faceted Curves in this Part.

Returns: Iterable collection of all the Faceted Curves in this part

getFacetedCurves() may also be accessed as a Part object property 'facetedCurves'. For example:

#### `getFacetedSolid(name: str) -> apex.geometry.FacetedSolid`
Get a Faceted Solid in this Part.

- `name` — of the Faceted Solid to get.

Returns: the FacetedSolid

#### `getFacetedSolids() -> apex.geometry.FacetedSolidCollection`
Get all Faceted Solids in this Part.

Returns: Iterable collection of all the Faceted Solids in this part

getFacetedSolids() may also be accessed as a Part object property 'facetedSolids'. For example:

#### `getFacetedSurface(name: str) -> apex.geometry.FacetedSurface`
Get a Faceted Surface in this Part.

- `name` — of the Faceted Surface to get.

Returns: the FacetedSurface

#### `getFacetedSurfaces() -> apex.geometry.FacetedSurfaceCollection`
Get all Faceted Surfaces in this Part.

Returns: Iterable collection of all the Faceted Surfaces in this part

getFacetedSurfaces() may also be accessed as a Part object property 'facetedSurfaces'. For example:

#### `getGeometryBodies() -> apex.geometry.GeometryBodyCollection`
Get all Bodies in this Part.

Returns: Iterable collection of all the Bodies in this part

getGeometryBodies() may also be accessed as a Part object property 'geometryBodies'. For example:

#### `getGeometryBody(name: str) -> apex.geometry.GeometryBody`
Get a GeometryBody in this Part.

- `name` — of the body to get.

Returns: the GeometryBody

#### `getInterfacePoints() -> apex.attribute.InterfacePointCollection`
returns a read only collection of all InterfacePoints composed by this Part

Returns: a reference to the apex.attribute.InterfacePointCollection object

#### `getMesh(name: str) -> apex.mesh.MeshBody`
Get a MeshBody in this Part.

- `name` — of the MeshBody to get.

Returns: the MeshBody

#### `getMeshes() -> apex.mesh.MeshBodyCollection`
Get all MesheBodies in this Part.

Returns: Iterable collection of all the meshes in this part

#### `getNamedEntities() -> apex.EntityCollection`
returns a collection of all entities in this Part that implement IName as an EntityCollection.

Returns: this Entity objects

#### `getNodes(target: apex.Entity) -> apex.mesh.NodeCollection`
get the nodes on this Entity (GeometryBody/GeometryTopology).

Returns: collection of nodes

#### `getParent() -> Assembly`
Get the parent Assembly for this Part.

Returns: The parent Assembly

getParent() may also be accessed as a Part object property 'parent'. For example:

#### `getPartProperties() -> apex.PartPropertyCollection`
returns all entities in this PartProperty collection.

Returns: this Entity objects

#### `getPartRep(name: str) -> apex.PartRep`
returns the specific partRep.

Returns: the partRep

#### `getPartReps() -> apex.PartRepCollection`
returns all entities in this PartRep collection.

Returns: this Entity objects

#### `getPartialGroups() -> apex.GroupCollection`
returns a GroupCollection of all Groups that reference at least one Entity that is composed by this Part. To return Groups that exclusively reference ONLY Entities composed by this Part use the exclusiveGroups property instead.

Returns: a GroupCollection of all Groups that reference at least one Entity that is composed by this Part.

#### `getPartialRegions() -> apex.RegionCollection`
returns a RegionCollection of all Regions that reference at least one Entity that is composed by this Part. To return Regions that exclusively reference ONLY Entities composed by this Part use the exclusiveRegions property instead.

Returns: a RegionCollection of all Regions that reference at least one Entity that is composed by this Part.

#### `getPhysicalEntities() -> apex.EntityCollection`
returns a collection of all entities in this Part that implement ILocation as an EntityCollection.

Returns: this Entity objects

#### `getPoint(name: str) -> apex.geometry.Point`
Get a Point in this Part.

- `name` — of the point to get.

Returns: the Point

#### `getPoints() -> apex.geometry.PointCollection`
Get all Points in this Part.

Returns: Iterable collection of all the Points in this part

getPoints() may also be accessed as a Part object property 'points'. For example:

- `getReferenceSystem() -> ( apex.ILocation,apex.IOrientation )` — Gets A tuple to represent location and orientation to be used for reference system.
- `getReferencedBy() -> apex.EntityCollection` — returns a collection of all entities that directly Reference this Part
#### `getSolid(name: str) -> apex.geometry.Solid`
Get a Solid in this Part.

- `name` — of the Solid to get.

Returns: the Solid

#### `getSolids() -> apex.geometry.SolidCollection`
Get all Solids in this Part.

Returns: Iterable collection of all the Solids in this part

getSolids() may also be accessed as a Part object property 'solids'. For example:

#### `getSphere(name: str) -> apex.geometry.Sphere`
Get a Sphere in this Part.

- `name` — of the Sphere to get.

Returns: the Sphere

#### `getSpheres() -> apex.geometry.SphereCollection`
Get all Spheres in this Part.

Returns: Iterable collection of all the Spheres in this part

getSpheres() may also be accessed as a Part object property 'spheres'. For example:

#### `getSurface(name: str) -> apex.geometry.Surface`
Get a Surface in this Part.

- `name` — of the Surface to get.

Returns: the Surface

#### `getSurfaces() -> apex.geometry.SurfaceCollection`
Get all Surfaces in this Part.

Returns: Iterable collection of all the Surfaces in this part

getSurfaces() may also be accessed as a Part object property 'surfaces'. For example:

#### `importGeometry(geometryFileNames: [str], importSolids: bool = True, importSurfaces: bool = True, importCurves: bool = True, importPoints: bool = True, importGeneralBodies: bool = True, importDatumPlanes: bool = False, importHiddenGeometry: bool = False, cleanOnImport: bool = True, removeRedundantTopoOnImport: bool = True, loadCompleteTopology: bool = True, sewOnImport: bool = False, importReviewMode3dxmlCleanOnImport: bool = True, importReviewMode3dxmlSplitOnFeatureVertexAngle: bool = True, importReviewMode3dxmlFeatureAngle: float = 40.0, importReviewMode3dxmlVertexAngle: float = 40.0, importReviewMode3dxmlDetectMachinedFaces: bool = False, importPublications: bool = False, importAttributes: bool = False) -> {str:apex.EntityCollection}`
Imports a target CAD model from the input CAD files into target parts. All bodies from part/assembly of input CAD files will be imported to the single target part. The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of geometry file. The apex.EntityCollection contains geometry bodies/datum planes imported to the target part from geometry files.

- `geometryFileNames` — A List of the path qualified file geometry file names.
- `importSolids` — Optional boolean argument to control whether Solid geometry types will be Imported or ignored. The default value of "True" will cause all Solid geometry to be imported. Setting to False will cause Solid geometry to be ignored (Not imported).
- `importSurfaces` — Optional boolean argument to control whether Surface geometry types will be Imported or ignored. The default value of "True" will cause all Surface geometry to be imported. Setting to False will cause Surface geometry to be ignored (Not imported).
- `importCurves` — Optional boolean argument to control whether Curve geometry types will be Imported or ignored. The default value of "True" will cause all Curve geometry to be imported. Setting to False will cause Curve geometry to be ignored (Not imported).
- `importPoints` — Optional boolean argument to control whether Point geometry types will be Imported or ignored. The default value of "True" will cause all Point geometry to be imported. Setting to False will cause Point geometry to be ignored (Not imported).
- `importGeneralBodies` — Optional boolean argument to control whether GeneralBody (Non-manifold Surfaces) geometry types will be Imported or ignored. The default value of "True" will cause all GeneralBody geometry to be imported. Setting to False will cause GeneralBody geometry to be ignored (Not imported).
- `importDatumPlanes` — Optional boolean argument to control whether Datum Planes will be Imported or ignored. The value of "True" will cause all Datum Planes to be imported. Setting to False will cause Datum Planes to be ignored (Not imported).
- `importHiddenGeometry` — Optional boolean argument to control whether geometry that is marked as hidden in geometry file will be Imported or ignored. The default value of "True" will cause all geometry to be imported visible or hidden. Setting to False will cause any geometry that is marked as hidden in the geometry file to be ignored (Not imported).
- `cleanOnImport` — Optional boolean argument to control whether the imported geometry will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is".
- `removeRedundantTopoOnImport` — Optionally remove redundant faces during import. Redundant faces are faces that share the same underlying geometry and do no impact the topology of neighboring faces. Default = True.
- `loadCompleteTopology` — Optionally "load complete topology" geometry as part of the import operation. Default = True.
- `sewOnImport` — Optionally "Sew" geometry edges as part of the import operation. Default = False.
- `importReviewMode3dxmlCleanOnImport` — Optional boolean argument to control whether the imported review mode 3dxml file will be "cleaned" on import. The default value of "True" will cause geometry cleaning to be performed during import, setting to False will import the geometry "as-is".
- `importReviewMode3dxmlSplitOnFeatureVertexAngle` — optional argument used to control the creation of faceted geometry bodies by taking account the feature and vertex angle, the default is True. If it is set as false, then the arguments of "importReviewMode3dxmlFeatureAngle" and "importReviewMode3dxmlVertexAngle" will be ignored.
- `importReviewMode3dxmlFeatureAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry edges will be created between any faces of the 3dxml data that have subtended angles greater than this value.featureAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `importReviewMode3dxmlVertexAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry vertices will be created between any edges of the 3dxml data that have subtended angles greater than this value. vertexAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `importReviewMode3dxmlDetectMachinedFaces` — This is an optional argument. When on, this triggers an algorithm to search for possible machined faces. When found, these will be split into separate faces. The types of faces that can be found are planar, cylinder, and torus faces. Depending on the smoothness and accuracy of the input tessellation, these will be detected and partitioned into separate faces. The intended use case is a model with mostly organic faces that as some analytical faces machined into it. For models that come primarily from analytical faces, such as STL from CAD or STL from FEM meshes that were applied to CAD, it is better to import as Mesh, then use the facet body tool in Apex to convert to facet bodies and optionally NURBS. It will be ignored if the argument "importReviewMode3dxmlSplitOnFeatureVertexAngle" is set as True.
- `importPublications` — Optionally import the Publications from Catia V5 and 3D Experience files. Default = False.
- `importAttributes` — Optional boolean argument that defines whether the attributes of the target CAD files will be imported into Apex. If False (Default), the attributes in the CAD files will be ignored during import. If True, the method will import the attributes in the CAD files and convert them as Apex User Attributes after import. In 2021.2 release, Apex supports the following attributes: Parasolid System Attributes: body_density and colour,Parasolid Attributes, Catia V5 Properties and 3D Experience Properties.

Returns: The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of geometry file. The apex.EntityCollection contains geometry bodies/datum planes imported to the target part from geometry files.

#### `importSTL(stlFileNames: [str], importBodyType: apex.geometry.STLImportBodyType = apex.geometry.STLImportBodyType.Mesh, featureAngle: float = 40.0, vertexAngle: float = 40.0, detectMachinedFaces: bool = False, splitOnAngle: bool = True, unitSystem: str = "m", cleanOnImport: bool = True) -> {str:apex.EntityCollection}`
Imports one or more STL files into this model and creates either mesh or geometry bodies depending on the supplied input values. All bodies created from STL files will be imported into the target Part. One mesh or geometry body will be created from each set of contiguous faces/lines in each STL file. If a set of contiguous faces in the STL file represents a watertight set and the the system will create an importBodyType is Facet, the system will create a facetted Solid body, otherwise the system will create a facetted Surface. The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of STL file. The apex.EntityCollection contains geometry bodies or mesh bodies imported to the target part from STL files.

- `stlFileNames` — List of fully qualified path names of the STL files to be imported.
- `importBodyType` — An enumeration defining the type of Apex body that will be created from the STL data. STL data can be used to create either mesh or facetted geometry bodies based on the value of this argument. The default value of apex.geometry.STLImportBodyType.Mesh will cause the creation of MeshBodies from the STL data. Setting the value of this argument to apex.geometry.STLImportBodyType. Faceted will cause the system to create faceted geometry bodies.
- `featureAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry edges will be created between any faces of the STL data that have subtended angles greater than this value. This argument will be silently ignored if importBodyType is set to Mesh. featureAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `vertexAngle` — optional argument used to control the creation of faceted geometry bodies. Topological geometry vertices will be created between any edges of the STL data that have subtended angles greater than this value. This argument will be silently ignored if importBodyType is set to Mesh. vertexAngle is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `detectMachinedFaces` — This is an optional argument. When on, this triggers an algorithm to search for possible machined faces. When found, these will be split into separet faces. The types of faces that can be found are planar, cylinder, and torus faces. Depending on the smoothness and accuracy of the input tessellation, these will be detected and partitioned into separate faces. This only applies to STL imported as facet body. If imported as mesh this is ignored. The intended use case is a model with mostly organic faces that as some analytical faces machined into it. For models that come primarily from analytical faces, such as STL from CAD or STL from FEM meshes that were applied to CAD, it is better to import as Mesh, then use the facet body tool in Apex to convert to facet bodies and optionally NURBS.
- `splitOnAngle` — Optional argument used to control the creation of faceted geometry bodies. Default = True. Topological geometry edges and vertices will be created according to featureAngle and vertexAngle value. This argument will be silently ignored if importBodyType is set to Mesh.
- `unitSystem` — A string to identify the units to be used during import STL. unitSystem value can be m, cm, mm, ft or in.
- `cleanOnImport` — Optionally "Clean" geometry as part of the import operation. Default = True.

Returns: The returned dictionary has keys of type string and values of type apex.EntityCollection. Each key represents the fully qualified path name of STL file. The apex.EntityCollection contains geometry bodies or mesh bodies imported to the target part from STL files.

#### `setParent(parent: Assembly) -> None`
Set an Assembly to be the new parent for this Part.

- `parent` — to be assigned the new parent of this Part

- `setReferenceSystem(refSysPair: ( apex.ILocation,apex.IOrientation )) -> None`
- `unsetColor() -> None` — unapplies the color of this Part to all its children.
- `unsetRender() -> None` — unapplies the renderStyle of this Part to all its children.
#### `update(name: str, parent: Entity, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update one or more of this Part properties.

- `name` — of this Part
- `parent` — Assembly of this Part
- `color` — of this Part
- `renderStyle` — of this Part
- `enableTransparency` — of this Part
- `transparencyLevel` — of this Part

One or more parameters can be updated in one update call.


## `apex.PartCollection`  (extends `IPhysicalCollection`)
Iterable collection of Parts, based on IPhysicalCollection.

Methods:

- `PartCollection() -> None` — Construct a new PartCollection.
#### `appendList(partList: [Part]) -> None`
Add Parts from a list to the end of this collection.

- `partList` — list of Parts to add to the collection.

For example:


## `apex.PartProperty`  (extends `Entity`)
class represents rep property of a part rep.

## `apex.PartPropertyCollection`  (extends `EntityCollection`)
Iterable collection of PartReps, based on EntityCollection.

Methods:

- `PartPropertyCollection() -> None` — Construct a new PartPropertyCollection.
- `PartPropertyCollection(collectionType: apex.CollectionType) -> None`
#### `appendList(partreplist: [PartProperty]) -> None`
Add reps from a list to the end of this collection.

- `partreplist` — list to add to the collection.

For example:


## `apex.PartPropertyRigid`  (extends `PartProperty`)
a class represents rigid part rep property.
Properties: `calculateProperties`, `cm`, `im`, `ixx`, `ixy`, `iyy`, `iyz`, `izx`, `izz`, `mass`

Methods:

- `getCM() -> apex.attribute.InterfacePoint` — The Interface Point located at the Center of Mass for the Rigid Part Representation.
- `getCalculateProperties() -> bool` — Returns Boolean of how the mass and inertia of the Rigid Part Representation is calculated. If calculateProperties is True, the mass is automatically calculated based on the volume of the solid geometry in the part and the material assigned to the geometry. If calculateProperties is False, the mass is based on custom entered values.
- `getIM() -> apex.attribute.InterfacePoint` — The Interface Point located at the Inertia Reference for the Rigid Part Representation.
- `getIxx() -> float` — The Ixx mass-inertial tensor component expressed in the im reference frame.
- `getIxy() -> float` — The Ixy mass-inertial tensor component expressed in the im reference frame.
- `getIyy() -> float` — The Iyy mass-inertial tensor component expressed in the im reference frame.
- `getIyz() -> float` — The Iyz mass-inertial tensor component expressed in the im reference frame.
- `getIzx() -> float` — The Izx mass-inertial tensor component expressed in the im reference frame.
- `getIzz() -> float` — The Izz mass-inertial tensor component expressed in the im reference frame.
- `getMass() -> float` — Mass of the Rigid Part Representation.
#### `update(mass: float, ixx: float, iyy: float, izz: float, ixy: float, iyz: float, izx: float, calculateProperties: bool, cm: apex.attribute.InterfacePoint, im: apex.attribute.InterfacePoint) -> None`
One or more properties may be updated in each call to update().

- `mass` — Update Mass of the Rigid Part Representation.
- `ixx` — Update the Ixx mass-inertial tensor component expressed in the im reference frame
- `iyy` — Update the Ixx mass-inertial tensor component expressed in the im reference frame
- `izz` — Update the Izz mass-inertial tensor component expressed in the im reference frame
- `ixy` — Update the Ixy mass-inertial tensor component expressed in the im reference frame
- `iyz` — Update the Iyz mass-inertial tensor component expressed in the im reference frame
- `izx` — Update the Izx mass-inertial tensor component expressed in the im reference frame
- `calculateProperties` — Update how the mass and inertia of the Rigid Part Representation is calculated
- `cm` — Update the Interface Point located at the Center of Mass for the Rigid Part Representation
- `im` — Update Interface Point located at the Inertia Reference for the Rigid Part Representation


## `apex.PartRep`  (extends `Entity`, `IDisplayable`, `IName`, `IActivatable`, `IPhysical`)
Properties: `highlighted`, `repProperty`, `repPropertyType`, `targets`

Methods:

#### `getRepProperty() -> apex.PartProperty`
returns the part property of this PartRep

Returns: the part property of this PartRep

#### `getRepPropertyType() -> apex.PartRepPropertyType`
returns Rep property type of this PartRep

Returns: Rep property type of this PartRep

#### `getTargets() -> apex.EntityCollection`
returns an EntityCollection of all entities directly composed by this PartRep.

Returns: an EntityCollection.

- `unsetColor() -> None` — unapplies the color of this Part Rep to all its children. This method provides the ability to allow the children of containers to control the color display.
- `unsetRender() -> None` — unapplies the renderStyle of this Part Rep to all its children.
#### `update(name: str, description: str, targets: apex.EntityCollection, repProperty: apex.PartProperty) -> None`
update a rigid part rep. One or more properties may be updated in each call to update().

- `name` — Update the name of the PartRep. The name must be unique within the scope of their parent Part. If a non-unique name is provided here it will be silently modified to ensure uniqueness.
- `description` — update the description for the PartRep
- `targets` — update the entities directly composed by this PartRep.
- `repProperty` — Update the rep Property type of the PartRep.


## `apex.PartRepCollection`  (extends `IPhysicalCollection`)
Iterable collection of PartReps, based on IPhysicalCollection.

Methods:

- `PartRepCollection() -> None` — Construct a new PartRepCollection.
- `PartRepCollection(collectionType: apex.CollectionType) -> None`
#### `appendList(partreplist: [PartRep]) -> None`
Add reps from a list to the end of this collection.

- `partreplist` — list to add to the collection.

For example:


## `apex.Region`  (extends `Entity`, `IPhysical`, `IUserAttributes`, `IName`, `IOrientation`)
Class used to persist collections of ILocation objects, including Mesh and Geometry sub-entities, with non-volatile names and pathNames. (NOTE: Don't support features of IUserHighLightable in current release, will support in future.) Regions support two critical behaviors, 1. Non-volatile names/pathNames for collections of mesh and geometry sub-entities. Neither Mesh nor Geometry sub-entities provided non-volatile names or IDs. 2. Generative update of the their contents.
Properties: `centroid`, `target`

Methods:

#### `addEntities(entities: apex.ILocationCollection) -> None`
Add entities to this Region. Entities in the input that are not supported by Region will be silently ignored. Entities in the input that are already referenced by this Region will be silently ignored.

- `entities` — The collection of ILocation entities that will comprise the Region. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `addEntity(entity: apex.ILocation) -> None`
Add entity to this Region. If the input Entity type is not supported by Region, it will be silently ignored If the input Entity type is already referenced by this Region, it will be silently ignored.

- `entity` — The Entity to add to this Region. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `getCentroid() -> apex.Coordinate`
returns the centroid of this Region as a Coordinate. If the Region references a single entity, the centroid of this Region is derived directly from the centroid of that single object. If the single object is a type that does not support a centroid property this property will return a None type. If the Region references multiple entities, the centroid of this Region is derived directly from the centroid of the oriented bounding box that encloses the referenced entities.

Returns: returns the centroid of this Region as a Coordinate.

- `getTarget() -> apex.ILocationCollection` — A collection of ILocation objects that represent this Region. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element.
#### `removeEntities(entities: apex.ILocationCollection) -> None`
Removes entities from this Region. Entities in the input that are not supported by Region will be silently ignored Entities in the input that are not referenced by this Region will be silently ignored.

- `entities` — The collection of ILocation objects to remove from this Region. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element

#### `removeEntity(entity: apex.ILocation) -> None`
Removes an entity from this Region. If the input Entity type is not supported by Region, it will be silently ignored If the input Entity type is not already referenced by this Region, it will be silently ignored.

- `entity` — The Entity to add to this Region. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element


## `apex.RegionCollection`  (extends `EntityCollection`)

Methods:

- `RegionCollection() -> None` — Construct a new RegionCollection.

## `apex.UserAttribute`  (extends `Entity`)
Object for tagging a string, integer, float, or bool values to Entities.
Properties: `attributeName`, `attributeType`, `boolValue`, `floatValue`, `intValue`, `owner`, `stringValue`

Methods:

- `getAttributeName() -> str` — attribute name
- `getAttributeType() -> apex.UserAttributeType` — UserAttributeType.
- `getBoolValue() -> bool` — bool attribute (if type == Bool).
- `getFloatValue() -> float` — float attribute (if type == Float).
- `getIntValue() -> int` — integer attribute (if type == Int).
- `getOwner() -> apex.Entity` — Entity owner (if assigned).
- `getStringValue() -> str` — string attribute (if type == Str).

## `apex.UserAttributeCollection`  (extends `EntityCollection`)
Iterable collection of UserAttributes, based on EntityCollection.

Methods:

- `UserAttributeCollection() -> None` — Construct a new UserAttributeCollection.

