# apex.catalog

(apex.catalog module) functions for creating/getting attribute.Material and attribute.ShellSection objects.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.catalog.ParametersType`: `CaseControl`, `BulkData`

## Module functions

### `apex.catalog.createMaterial(name: str = "", description: str = "", primaryMaterialModel: str = "", color: [int] = defaultMaterialColor, materialClass: str = "", materialSubclass: str = "") -> apex.attribute.Material`
Creates a Material and adds it to the Material catalog. Note that the material can be added under a Material Class or a Material Subclass if the name is provided.

- `name` — of the new apex.attribute.Material. default = "" (auto-named)
- `description` — of the new apex.attribute.Material. default = ""
- `primaryMaterialModel` — of the new apex.attribute.Material. default = ""
- `color` — of the new apex.attribute.Material. 3 vector(list) specifying the Red, Green, and Blue component of the color. Each value should be in the range 0-255.
- `materialClass` — an Optional string that specifies the parent level of the material. If provided, the material is created and added under this MaterialClass. If materialSubclass is also provided, the material is created and added under the materialSubclass, while the materialSubclass is under the materialClass. If omitted, the material is created and added in the default material catalog. If system cannot find the materialClass by the string, system will create a materialClass in the material catalog.
- `materialSubclass` — an optional string that specifies the parent level of the material. If provided, the material is created and added under this MaterialSubclass. Note that materialSubclass must be coexisted with materialClass as it is a children of materialClass. If omitted, system will create the material in the material catalog or in the materialClass if materialClass is specified. If system cannot find the materialSubclass by the string, system will create a materialSubclass in the material catalog.

Returns: the created apex.attribute.Material

### `apex.catalog.createPropertiesElement2D(name: str, description: str, primaryProperties2D: str, color: [int]) -> apex.attribute.PropertiesElement2D`
Creates and returns a PropertiesElement2D in the catalog.

- `name` — The name of this object as a string
- `description` — The description for this object
- `primaryProperties2D` — The primaryProperties2D should has a valid value like "PSHELL" , "PSHEAR", "PCOHE", "PLPLANE". if primaryProperties2D == "", then create a PSHELL
- `color` — of the new apex.attribute.PropertiesElement2D. 3 vector(list) specifying the Red, Green, and Blue component of the color. Each value should be in the range 0-255.

### `apex.catalog.createPropertiesElement3D(name: str, description: str, primaryProperties3D: str, color: [int]) -> apex.attribute.PropertiesElement3D`
Creates and returns a PropertiesElement3D in the catalog.

- `name` — The name of this object as a string
- `description` — The description for this object
- `primaryProperties3D` — The primaryProperties3D should has a valid value like "PSOLID" , "PLSOLID". if primaryProperties2D == "", then create a "PSOLID"
- `color` — of the new apex.attribute.PropertiesElement3D. 3 vector(list) specifying the Red, Green, and Blue component of the color. Each value should be in the range 0-255.

### `apex.catalog.createPropertiesElement3DHomogeneous(referenceMaterial: apex.attribute.Material, name: str = "#####", description: str = "#####", id: int = 0, orientationType: apex.attribute.OrientationType3D = apex.attribute.OrientationType3D.Unset, materialOrientation: apex.IOrientation = None, integrationNetwork: apex.attribute.IntegrationNetwork = apex.attribute.IntegrationNetwork.Automatic, integrationScheme: apex.attribute.IntegrationScheme = apex.attribute.IntegrationScheme.Automatic, outputLocation: apex.attribute.OutputLocation = apex.attribute.OutputLocation.Unset) -> apex.attribute.PropertiesElement3DHomogeneous`
Creates a PropertiesElement3DHomogeneous and adds it to the CatalogElementProperty.

- `referenceMaterial` — The material referenced by the PropertiesElement3D. It must be provided to create this PropertiesElement3D.
- `name` — An optional name for the PropertiesElement3D that will be created. If omitted, the system will assign a default name formed by concatenating the prefix '3D Element Property ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example '3D Element Property 1'.
- `description` — An optional description for the PropertiesElement3D that will be created. If omitted, the description will be left blank.
- `id` — The id of the PropertiesElement3D. If omitted, the system will assign the existing largest 3d element property ID + 1 to it.
- `orientationType` — An optional Enum defining the type of material orientation. If omitted, default is "apex.attribute.OrientationType3D.Unset", so that the material orientation follows the global coordinate system, this is same as "apex.attribute.OrientationType3D.Global". If "apex.attribute.OrientationType3D.DefaultElement" or If "apex.attribute.OrientationType3D.AlternateElement" is provided, then the material orientation follows the default or alternate element coordinate system. If "apex.attribute.OrientationType3D.Local" is provided, then materialOrientation is required to specify a coordinate system or an orientation.
- `materialOrientation` — Iorientation to define the material orientation when orientationType is "apex.attribute.OrientationType3D.Local". It can be a coordinate system or an orientation object. If omitted, global coordinate system is used.
- `integrationNetwork` — The integration network of the PropertiesElement3D. If omitted, the default value is "apex.attribute.IntegrationNetwork.Automatic".
- `integrationScheme` — The integration scheme of the PropertiesElement3D. If omitted, the default value is "apex.attribute.IntegrationScheme.Automatic".
- `outputLocation` — The location of stress output of the PropertiesElement3D. If omitted, the default value is "apex.attribute.OutputLocation.Unset", this is equivalent to "apex.attribute.OutputLocation.Grid".

Returns: the created apex.attribute.PropertiesElement3DHomogeneous

### `apex.catalog.createShellBehaviorShearPanel(name: str = "", description: str = "") -> apex.attribute.ShellBehavior`
This Function is no longer supported in Apex. Refer to apex.catalog.createPropertiesElement2D to determine how this capability is now supported.

- `name` — An optional string argument that provides a Name for the create apex.attribute.ShellBehavior. If omitted, the system will provide a default name for the creates apex.attribute.ShellBehavior by of the for "Shell Behavior <n>" where <n> is the lowest available integer value required for name uniqueness. If provided the name must be unique with the scope of all ShellBehaviors in the catalog
- `description` — An optional string argument that provides a description of the create apex.attribute.ShellBehavior. If omitted the description will be left blank.

Creates and returns a apex.attribute.ShellBehavior object of type ShearPanel.This method requires no apex.attribute.ShellBehavior property arguments.

### `apex.catalog.createShellBehaviorThinShell(name: str = "", description: str = "", enableMembraneStiffness: apex.ApexBool = ApexBoolTrue, enableBendingStiffness: apex.ApexBool = ApexBoolTrue, enableTransverseShearStiffness: apex.ApexBool = ApexBoolTrue, bendingRatio: float = 1.0, transverseShearRatio: float = 0.833333) -> apex.attribute.ShellBehavior`
This Function is no longer supported in Apex. Refer to apex.catalog.createPropertiesElement2D to determine how this capability is now supported.

- `name` — An optional string argument that provides a Name for the create apex.attribute.ShellBehavior. If omitted, the system will provide a default name for the creates apex.attribute.ShellBehavior by of the for "Shell Behavior <n>" where <n> is the lowest available integer value required for name uniqueness. If provided the name must be unique with the scope of all ShellBehaviors in the catalog
- `description` — An optional string argument that provides a description of the create ShellBehavior. If omitted the description will be left blank.
- `enableMembraneStiffness` — Optional boolean argument (Default = True) to enable/disable membrane stiffness in the created apex.attribute.ShellBehavior.
- `enableBendingStiffness` — Optional boolean argument (Default = True) to enable/disable bending stiffness in the created apex.attribute.ShellBehavior.
- `enableTransverseShearStiffness` — Optional boolean argument (Default = True) to enable/disable transverse shear stiffness in the created apex.attribute.ShellBehavior.
- `bendingRatio` — Optional argument to define the bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell, T^3/12. The default value is for a homogeneous shell (1.0).
- `transverseShearRatio` — Optional transverse shear thickness ratio Ts/T - the ratio of the shear thickness, Ts, to the membrane thickness of the shell, T. The default value is for a homogeneous shell (0.833333)

Returns: the created apex.attribute.ShellBehavior

Creates and returns a apex.attribute.ShellBehavior object of type ThinShell using the input properties.

### `apex.catalog.createShellSection(name: str = "", description: str = "", thickness: float = NAN, offset: float = NAN) -> apex.attribute.ShellSection`
This Function is no longer supported in Apex. Refer to apex.attribute.createFieldThicknessOffsetConstant to determine how this capability is now supported.

- `name` — of the new apex.attribute.ShellSection. default = "" (auto-named)
- `description` — of the new apex.attribute.ShellSection. default = ""
- `thickness` — missing, add it for avoiding warning
- `offset` — missing, add it for avoiding warning

Returns: the created apex.attribute.ShellSection

Create a new apex.attribute.ShellSection in this Catalog.

### `apex.catalog.getAssignedMaterial(name: str) -> apex.attribute.Material`
Get an assigned apex.attribute.Material.

- `name` — of the apex.attribute.Material.

Returns: the material object with name specified by user

### `apex.catalog.getAssignedMaterials() -> apex.attribute.MaterialCollection`
Get all assigned materials in this model.

Returns: a MaterialCollection of the requested materials

### `apex.catalog.getBeamShape(name: str) -> apex.attribute.BeamShape`
Retrieves a apex.attribute.BeamShape from the catalog using the input "name". If a apex.attribute.BeamShape with the input name does not exit the method will throw an exception.

- `name` — of the apex.attribute.BeamShape.

### `apex.catalog.getBeamShapeDictionary() -> {str:apex.attribute.BeamShape}`
Get all apex.attribute.BeamShape objects in this Catalog.

Returns: a apex.attribute.BeamShape dictionary which key is apex.attribute.BeamShape name and value is apex.attribute.BeamShape corresponding object.

### `apex.catalog.getBushingProperties() -> apex.attribute.BushingRepPropertiesCollection`
Returns a collection of all BushingRepProperties. If no BushingRepProperties objects exist, the collection will be empty.

Returns: a BushingRepPropertiesCollection of the requested bushingRepProperties

### `apex.catalog.getBushingProperty(name: str) -> apex.attribute.BushingRepProperties`
Retrieves a apex.attribute.BushingProperties from the catalog using the input "name". If a apex.attribute.BushingProperties with the input name does not exit the method will throw an exception.

- `name` — of the apex.attribute.BushingProperties.

### `apex.catalog.getBushingPropertyDictionary() -> {str:apex.attribute.BushingRepProperties}`
A dictionary containing all apex.attribute.BushingProperties objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.BushingProperties The dictionary value is the apex.attribute.BushingProperties corresponding to the apex.attribute.BushingProperties.

Returns: a apex.attribute.BushingProperties dictionary.

### `apex.catalog.getCatalogElementProperty() -> apex.catalog.CatalogElementProperty`
Returns the singleton ElementProperty catalog that contains all 2D and 3D element property objects from the Apex session.

### `apex.catalog.getCatalogKeyResult() -> apex.catalog.KeyResultCatalog`
Returns a KeyResult catalog that contains all keyresults.

### `apex.catalog.getCatalogMaterial() -> apex.catalog.CatalogMaterial`
Returns the singleton material catalog from the Apex session.

### `apex.catalog.getCatalogParameters() -> apex.catalog.CatalogParameters`
Returns the parameters catalog from the Apex session.

### `apex.catalog.getCatalogSystemCells() -> apex.catalog.CatalogSystemCells`
Returns the SystemCells catalog from the Apex session.

### `apex.catalog.getDAMPING(name: str = "#####") -> apex.catalog.DAMPING`

### `apex.catalog.getDAMPINGs() -> apex.EntityCollection`

### `apex.catalog.getDamper1DProperties() -> apex.attribute.Damper1DRepPropertiesCollection`
Returns a collection of all Damper1DRepProperties. If no Damper1DRepProperties objects exist, the collection will be empty.

Returns: a Damper1DRepPropertiesCollection of the requested damper1DRepProperties

### `apex.catalog.getDamper1DProperty(name: str) -> apex.attribute.Damper1DRepProperties`
Retrieves a apex.attribute.Damper1DProperties from the catalog using the input "name". If a apex.attribute.Damper1DProperties with the input name does not exit the method will throw an exception.

- `name` — of the apex.attribute.Damper1DProperties.

### `apex.catalog.getDamper1DPropertyDictionary() -> {str:apex.attribute.Damper1DRepProperties}`
A dictionary containing all apex.attribute.Damper1DProperties objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.Damper1DProperties The dictionary value is the apex.attribute.Damper1DProperties corresponding to the apex.attribute.Damper1DProperties.

Returns: a apex.attribute.Damper1DProperties dictionary.

### `apex.catalog.getEIGB(name: str = "#####") -> apex.catalog.EIGB`

### `apex.catalog.getEIGBs() -> apex.EntityCollection`

### `apex.catalog.getEIGR(name: str = "#####") -> apex.catalog.EIGR`

### `apex.catalog.getEIGRL(name: str = "#####") -> apex.catalog.EIGRL`

### `apex.catalog.getEIGRLs() -> apex.EntityCollection`

### `apex.catalog.getEIGRs() -> apex.EntityCollection`

### `apex.catalog.getFastenerProperties() -> apex.attribute.FastenerRepPropertiesCollection`
Returns a collection of all FastenerRepProperties. If no FastenerRepProperties objects exist, the collection will be empty.

Returns: a FastenerRepPropertiesCollection of the requested fastenerRepProperties

### `apex.catalog.getFastenerProperty(name: str) -> apex.attribute.FastenerRepProperties`
Retrieves a apex.attribute.FastenerProperties from the catalog using the input "name". If a apex.attribute.FastenerProperties with the input name does not exit the method will throw an exception.

- `name` — of the apex.attribute.FastenerProperties.

### `apex.catalog.getFastenerPropertyDictionary() -> {str:apex.attribute.FastenerRepProperties}`
A dictionary containing all apex.attribute.FastenerProperties objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.FastenerProperties The dictionary value is the apex.attribute.FastenerProperties corresponding to the apex.attribute.FastenerProperties.

Returns: a apex.attribute.FastenerProperties dictionary.

### `apex.catalog.getHYBDAMP(name: str = "#####") -> apex.catalog.HYBDAMP`

### `apex.catalog.getHYBDAMPs() -> apex.EntityCollection`

### `apex.catalog.getITER(name: str = "#####") -> apex.catalog.ITER`

### `apex.catalog.getITERs() -> apex.EntityCollection`

### `apex.catalog.getMaterial(name: str) -> apex.attribute.Material`
Get a new apex.attribute.Material in this Catalog.

- `name` — of the apex.attribute.Material.

### `apex.catalog.getMaterialByID(id: int) -> apex.attribute.Material`
User specify an id input and it will return the material object.

Returns: the material object with id specified by user

### `apex.catalog.getMaterialDictionary() -> {str:apex.attribute.Material}`
Get all apex.attribute.Material objects in this Catalog.

Returns: a Material dictionary which key is apex.attribute.Material name and value is apex.attribute.Material corresponding object.

### `apex.catalog.getMaterialSheet(pathName: str) -> apex.attribute.MaterialSheet`
Retrieves a MaterialSheet from the material catalog using the input MaterialSheet pathName.

- `pathName` — The pathName of the MaterialSheet to retrieve. MaterialSheets are composed by the MaterialCatalog.

### `apex.catalog.getMaterialSheetStack(pathName: str) -> apex.attribute.MaterialSheetStack`
Retrieves a MaterialSheetStack from the material catalog using the input MaterialSheetStack pathName.

- `pathName` — The pathName of the MaterialSheetStack to retrieve. MaterialSheetStacks are composed by the MaterialCatalog.

### `apex.catalog.getMaterials(target: [{str:str}]) -> apex.attribute.MaterialCollection`
Returns a collection of all Materials in the catalog, specified by target of key:value string dictionaries If no Material objects exist, the collection will be empty.

- `target` — of dictionaries (string:string) specifying the materials to retrieve. Valid keys are 'path' and 'name'. If omited, all materials in the model will be returned.

Returns: a MaterialCollection of the requested materials

For example:

### `apex.catalog.getMaterialsBy2DProperty() -> apex.attribute.MaterialCollection`
This API will return a list of material objects corresponding to the MID1 associated with the assigned 2D element property in the current apex DB.

Returns: a MaterialCollection of material objects corresponding to the MID1 associated with the assigned 2D element property in the current apex DB

### `apex.catalog.getNLSTEP(name: str = "#####") -> apex.catalog.NLSTEP`

### `apex.catalog.getNLSTEPs() -> apex.EntityCollection`

### `apex.catalog.getProfile1D_Dictionary() -> {str:apex.construct.Profile1D}`
Returns a dictionary containing all apex.construct.Profile1D objects in the catalog. The dictionary key is a string type and represents the Name of the apex.construct.Profile1D The dictionary value is the apex.construct.Profile1D corresponding to the Name.

Returns: a apex.construct.Profile1D dictionary which key is apex.construct.Profile1D name and value is apex.construct.Profile1D object.

### `apex.catalog.getProfile1Ds() -> apex.construct.Profile1DCollection`
Returns a cpllection of all Profile1Ds in this Catalog. If no apex.construct.Profile1D object exists, the collection will be empty.

Returns: a Profile1DCollection object.

### `apex.catalog.getPropertiesElement2D(name: str) -> apex.attribute.PropertiesElement2D`
Retrieves a apex.attribute.PropertiesElement2D from the catalog using the input name. If a PropertiesElement2D with the input specified name does not exist in the catalog the method will throw an exception.

- `name` — The name of the apex.attribute.PropertiesElement2D to retrieve from the catalog

### `apex.catalog.getPropertiesElement2DDictionary() -> {str:apex.attribute.PropertiesElement2D}`
A dictionary containing all apex.attribute.PropertiesElement2D objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.PropertiesElement2D. The dictionary value is the apex.attribute.PropertiesElement2D object corresponding to the Name.

Returns: a apex.attribute.PropertiesElement2D dictionary which key is apex.attribute.PropertiesElement2D name and value is apex.attribute.PropertiesElement2D corresponding object.

### `apex.catalog.getPropertiesElement2Ds(target: [{str:str}]) -> apex.attribute.PropertiesElement2DCollection`
Returns a collection of all PropertiesElement2Ds in the catalog If no apex.attribute.PropertiesElement2D objects exist and empty collection will be returned.

### `apex.catalog.getPropertiesElement3D(name: str) -> apex.attribute.PropertiesElement3D`
Retrieves a PropertiesElement3D object in the catalog by the name. If the name does not exist, the method will throw an exception.

- `name` — of the apex.attribute.PropertiesElement3D.

### `apex.catalog.getPropertiesElement3DDictionary() -> {str:apex.attribute.PropertiesElement3D}`
A dictionary containing all apex.attribute.PropertiesElement3D objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.PropertiesElement3D. The dictionary value is the apex.attribute.PropertiesElement3D object corresponding to the Name.

Returns: a apex.attribute.PropertiesElement3D dictionary which key is apex.attribute.PropertiesElement3D name and value is apex.attribute.PropertiesElement3D corresponding object.

### `apex.catalog.getPropertiesElement3Ds(target: [{str:str}]) -> apex.attribute.PropertiesElement3DCollection`
Returns a collection of PropertiesElement3D objects in the catalog, specified by target of key:value string dictionaries. If no PropertiesElement3D objects exist, the collection will be empty.

- `target` — of dictionaries (string:string) specifying the PropertiesElement3D to retrieve. Valid keys are 'path' and 'name'.

Returns: a MaterialCollection of the requested PropertiesElement3D

For example:

### `apex.catalog.getRANDPS(name: str = "#####") -> apex.catalog.RANDPS`

### `apex.catalog.getRANDPSs() -> apex.EntityCollection`

### `apex.catalog.getRANDT1(name: str = "#####") -> apex.catalog.RANDT1`

### `apex.catalog.getRANDT1s() -> apex.EntityCollection`

### `apex.catalog.getRCROSS(name: str = "#####") -> apex.catalog.RCROSS`

### `apex.catalog.getRCROSSs() -> apex.EntityCollection`

### `apex.catalog.getSectionDictionary() -> {str:apex.attribute.ShellSection}`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Get all apex.attribute.ShellSection objects in this Catalog.

Returns: a ShellSection dictionary which key is apex.attribute.ShellSection name and value is apex.attribute.ShellSection corresponding object.

### `apex.catalog.getSections(target: [{str:str}]) -> apex.attribute.SectionCollection`
This Function is no longer supported in Apex. Refer to apex.attribute.getDiscreteFEMFields to determine how this capability is now supported.

- `target` — of dictionaries (string:string) specifying the sections to retrieve. Valid keys are 'path' and 'name'.

Returns: a SectionCollection of the requested Sections

Returns a collection of all Sections in the catalog, specified by target of key:value string dictionaries If no Section objects exist, the collection will be empty

### `apex.catalog.getShellBehavior(name: str) -> apex.attribute.ShellBehavior`
This Function is no longer supported in Apex. Refer to apex.catalog.getPropertiesElement2D to determine how this capability is now supported.

- `name` — The name of the apex.attribute.ShellBehavior to retrieve from the catalog

Retrieves a apex.attribute.ShellBehavior from the catalog using the input name. If a ShellBehavior with the input specified name does not exist in the catalog the method will throw an exception

### `apex.catalog.getShellBehavior_Dictionary() -> {str:apex.attribute.ShellBehavior}`
This Function is no longer supported in Apex. Refer to apex.catalog.getPropertiesElement2Ds to determine how this capability is now supported.

Returns: a apex.attribute.ShellBehavior dictionary which key is apex.attribute.ShellBehavior name and value is apex.attribute.ShellBehavior corresponding object.

A dictionary containing all apex.attribute.ShellBehavior objects in the catalog. The dictionary key is string type and represents the Name of the apex.attribute.ShellBehavior. The dictionary value is the apex.attribute.ShellBehavior corresponding to the Name. If no apex.attribute.ShellBehavior are present in the catalog, the collection will be empty.

### `apex.catalog.getShellBehaviors(target: [{str:str}]) -> apex.attribute.ShellBehaviorCollection`
This Function is no longer supported in Apex. Refer to apex.catalog.getPropertiesElement2Ds to determine how this capability is now supported.

Returns a collection of all ShellBehaviors in the catalogIf no apex.attribute.ShellBehavior objects exist and empty collection will be returned

### `apex.catalog.getShellSection(name: str) -> apex.attribute.ShellSection`
This Function is no longer supported in Apex. Refer to apex.attribute.getDiscreteFEMField to determine how this capability is now supported.

- `name` — of the apex.attribute.ShellSection.

Get a new apex.attribute.ShellSection in this Catalog.

### `apex.catalog.getSpring1DProperties() -> apex.attribute.Spring1DRepPropertiesCollection`
Returns a collection of all Spring1DRepProperties. If no Spring1DRepProperties objects exist, the collection will be empty.

Returns: a Spring1DRepPropertiesCollection of the requested spring1DRepProperties

### `apex.catalog.getSpring1DProperty(name: str) -> apex.attribute.Spring1DRepProperties`
Retrieves a apex.attribute.Spring1DProperties from the catalog using the input "name". If a apex.attribute.Spring1DProperties with the input name does not exit the method will throw an exception.

- `name` — of the apex.attribute.Spring1DProperties.

### `apex.catalog.getSpring1DPropertyDictionary() -> {str:apex.attribute.Spring1DRepProperties}`
A dictionary containing all apex.attribute.Spring1DProperties objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.Spring1DProperties The dictionary value is the apex.attribute.Spring1DProperties corresponding to the apex.attribute.Spring1DProperties.

Returns: a apex.attribute.Spring1DProperties dictionary.

### `apex.catalog.getSpringDamper1DProperties() -> apex.attribute.SpringDamper1DRepPropertiesCollection`
Returns a collection of all SpringDamper1DRepProperties. If no SpringDamper1DRepProperties objects exist, the collection will be empty.

Returns: a SpringDamper1DRepPropertiesCollection of the requested springDamper1DRepProperties

### `apex.catalog.getSpringDamper1DProperty(name: str) -> apex.attribute.SpringDamper1DRepProperties`
Retrieves a apex.attribute.SpringDamper1DProperties from the catalog using the input "name". If a apex.attribute.SpringDamper1DProperties with the input name does not exit the method will throw an exception.

- `name` — of the apex.attribute.SpringDamper1DProperties.

### `apex.catalog.getSpringDamper1DPropertyDictionary() -> {str:apex.attribute.SpringDamper1DRepProperties}`
A dictionary containing all apex.attribute.SpringDamper1DProperties objects in the catalog. The dictionary key is a string type and represents the Name of the apex.attribute.SpringDamper1DProperties The dictionary value is the apex.attribute.SpringDamper1DProperties corresponding to the apex.attribute.SpringDamper1DProperties.

Returns: a apex.attribute.SpringDamper1DProperties dictionary.

### `apex.catalog.getTSTEP(name: str = "#####") -> apex.catalog.TSTEP`

### `apex.catalog.getTSTEPs() -> apex.EntityCollection`

## Classes in this module

Full method signatures are in `api/classes/apex.catalog.md`.

`CatalogElementProperty`, `CatalogMaterial`, `CatalogParameters`, `CatalogSystemCells`, `DAMPING`, `EIGB`, `EIGR`, `EIGRL`, `HYBDAMP`, `ITER`, `KeyResultCatalog`, `NLSTEP`, `ParametersSet`, `ParametersSetCollection`, `RANDPS`, `RANDT1`, `RCROSS`, `SystemCellsSet`, `SystemCellsSetCollection`, `TSTEP`

