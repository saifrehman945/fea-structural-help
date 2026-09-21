# apex.environment

(apex.environment module) functions for creating/getting Load, Constraint, Force, and Gravity objects.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.environment.BoltPreloadType`: `Force`, `Overclosure`

## Module functions

### `apex.environment.createConstraintCombination(name: str, description: str, id: int, combinedConstraints: apex.EntityCollection) -> ConstraintCombination`
Create ConstraintCombination in this environment.

- `name` — An optional name for the constraint combination that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Constraint Combination" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Constraint Combination 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest ID +1 to it.
- `combinedConstraints` — A collection of constraint objects to be combined.

### `apex.environment.createConstraintDisplacement(name: str, description: str, id: int, target: apex.EntityCollection, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, constraintType: apex.attribute.ConstraintType, orientation: apex.IOrientation, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> ConstraintDisplacement`
Create ConstraintDisplacement in this environment.

- `name` — An optional name for the ConstraintDisplacement that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `id` — Optional - the id of the Constraint. If omitted, system automatically assigns the existing largest constraint id + 1.
- `target` — An entityCollection that is applied to the ConstraintDisplacement.
- `translationX` — An optional argument to define the displacement constraint in translation X. This is only necessary when the constraintType is apex.attribute.ConstraintType.General.
- `translationY` — An optional argument to define the displacement constraint in translation Y. This is only necessary when the constraintType is apex.attribute.ConstraintType.General.
- `translationZ` — An optional argument to define the displacement constraint in translation Z. This is only necessary when the constraintType is apex.attribute.ConstraintType.General.
- `rotationX` — An optional argument to define the displacement constraint in rotation X. This is only necessary when the constraintType is apex.attribute.ConstraintType.General.
- `rotationY` — An optional argument to define the displacement constraint in rotation Y. This is only necessary when the constraintType is apex.attribute.ConstraintType.General.
- `rotationZ` — An optional argument to define the displacement constraint in rotation Z. This is only necessary when the constraintType is apex.attribute.ConstraintType.General.
- `constraintType` — the constraintType of the constraint.
- `orientation` — An optional orientation, currently it must be a coordinate system in which the components are defined. If omitted, the components are defined in the basic coordinate system.
- `applicationMethod` — The applicationMethod of the constraint.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote constraint is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createConstraintDisplacementVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintDisplacement) -> ConstraintDisplacementVariable`
Create ConstraintDisplacementVariable in this environment.

- `id` — Optional - the id of the Constraint. If omitted, system automatically assigns the existing largest constraint id + 1.
- `name` — An optional name for the ConstraintDisplacement that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the constraint.

### `apex.environment.createConstraintExcludeAuto(name: str, description: str, target: apex.EntityCollection, excludeTranslationX: bool, excludeTranslationY: bool, excludeTranslationZ: bool, excludeRotationX: bool, excludeRotationY: bool, excludeRotationZ: bool) -> ConstraintExcludeAuto`
Create ConstraintExcludeAuto in this environment. The degrees of freedom will be excluded from AUTOSPC.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `target` — An entityCollection that is applied to the ConstraintDisplacement.
- `excludeTranslationX` — An optional argument to exclude the translation X from AUTOSPC.
- `excludeTranslationY` — An optional argument to exclude the translation Y from AUTOSPC.
- `excludeTranslationZ` — An optional argument to exclude the translation Z from AUTOSPC.
- `excludeRotationX` — An optional argument to exclude the rotation X from AUTOSPC.
- `excludeRotationY` — An optional argument to exclude the rotation Y from AUTOSPC.
- `excludeRotationZ` — An optional argument to exclude the rotation Z from AUTOSPC.

### `apex.environment.createConstraintExcludeAuto1(name: str, description: str, excludeTranslationX: bool, excludeTranslationY: bool, excludeTranslationZ: bool, excludeRotationX: bool, excludeRotationY: bool, excludeRotationZ: bool, target: apex.EntityCollection) -> ConstraintExcludeAuto1`
Create ConstraintExcludeAuto1 in this environment. The degrees of freedom will be excluded from AUTOSPC.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `excludeTranslationX` — An optional argument to exclude the translation X from AUTOSPC.
- `excludeTranslationY` — An optional argument to exclude the translation Y from AUTOSPC.
- `excludeTranslationZ` — An optional argument to exclude the translation Z from AUTOSPC.
- `excludeRotationX` — An optional argument to exclude the rotation X from AUTOSPC.
- `excludeRotationY` — An optional argument to exclude the rotation Y from AUTOSPC.
- `excludeRotationZ` — An optional argument to exclude the rotation Z from AUTOSPC.
- `target` — An entityCollection that is applied to the ConstraintDisplacement.

### `apex.environment.createConstraintExcludeAuto1Variable(name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintExcludeAuto) -> ConstraintExcludeAuto1Variable`
Create ExcludeDof1Variable in this environment. The degrees of freedom will be excluded from AUTOSPC.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createConstraintExcludeAutoVariable(name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintExcludeAuto) -> ConstraintExcludeAutoVariable`
Create ConstraintExcludeAutoVariable in this environment. The degrees of freedom will be excluded from AUTOSPC.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the constraint.

### `apex.environment.createConstraintSinglePoint(name: str, description: str, id: int, constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool, target: apex.EntityCollection, constraintType: apex.attribute.ConstraintType, orientation: apex.IOrientation, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> ConstraintSinglePoint`
Create ConstraintSinglePoint in this environment.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `id` — Optional - the id of the Constraint. If omitted, system automatically assigns the existing largest constraint id + 1.
- `constrainTranslationX` — An optional argument to constrain the translation X. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainTranslationY` — An optional argument to constrain the translation Y. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainTranslationZ` — An optional argument to constrain the translation Z. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationX` — An optional argument to constrain the rotation X. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationY` — An optional argument to constrain the rotation Y. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationZ` — An optional argument to constrain the rotation Z. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `target` — An entityCollection that is applied to the ConstraintDisplacement.
- `constraintType` — the constraintType.
- `orientation` — An optional orientation, currently it must be a coordinate system in which the components are defined. If omitted, the components are defined in the basic coordinate system.
- `applicationMethod` — The applicationMethod of the constraint.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote constraint is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createConstraintSinglePointVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintSinglePoint) -> ConstraintSinglePointVariable`
Create ConstraintSinglePointVariable in this environment.

- `id` — Optional - the id of the Constraint. If omitted, system automatically assigns the existing largest constraint id + 1.
- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createDFEMFieldAccelerationNodal(orientations: [int], scaleFactors: [float], accelerationVectorsX: [float], accelerationVectorsY: [float], accelerationVectorsZ: [float], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldAccelerationNodal`
Create DFEMFieldAccelerationNodal in this environment.

- `orientations` — The optional orientation. It can be either an IOrientation object which only accepts coordinate system or a list of IOrientation objects or a list of integers of the coordinate system IDs. If omitted, then basic coordinate system is used.
- `scaleFactors` — The optional scale factors for the acceleration vectors. It can be either a float value for all vectors or a list of floats to define different scale factors for each acceleration vector. If omitted, all scale factors are 1.0.
- `accelerationVectorsX` — The X component of the acceleration vector.
- `accelerationVectorsY` — The Y component of the acceleration vector.
- `accelerationVectorsZ` — The Z component of the acceleration vector.
- `nodeIds` — A list of integers to define target node IDs in the field.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldAccelerationNodalByFileImport(filePath: str) -> DFEMFieldAccelerationNodal`
Create DFEMFieldAccelerationNodal by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldConstraintDisplacement(nodeIds: [int], orientations: [int], translationsX: [float], translationsY: [float], translationsZ: [float], rotationsX: [float], rotationsY: [float], rotationsZ: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldConstraintDisplacement`
Create DFEMFieldConstraintDisplacement in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — The optional orientations. It can be either an IOrientation object that accepts coordinate system or a list of IOrientation objects. If omitted, the constraint is defined in the basic coordinate system.
- `translationsX` — A list of translation values in X.
- `translationsY` — A list of translation values in Y.
- `translationsZ` — A list of translation values in Z.
- `rotationsX` — A list of rotation values about X axis.
- `rotationsY` — A list of rotation values about Y axis.
- `rotationsZ` — A list of rotation values about Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldConstraintDisplacementByFileImport(filePath: str) -> DFEMFieldConstraintDisplacement`

### `apex.environment.createDFEMFieldConstraintExcludeAuto(excludeTranslationX: [bool], excludeTranslationY: [bool], excludeTranslationZ: [bool], excludeRotationX: [bool], excludeRotationY: [bool], excludeRotationZ: [bool], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldConstraintExcludeAuto`
Create DFEMFieldConstraintExcludeAuto in this environment.

- `excludeTranslationX` — A list of booleans to exclude the translation X for target nodes. For example, excludeTranslationX = [True, False, False, True].
- `excludeTranslationY` — A list of booleans to exclude the translation Y for target nodes. For example, excludeTranslationY = [True, False, False, True].
- `excludeTranslationZ` — A list of booleans to exclude the translation Z for target nodes. For example, excludeTranslationZ = [True, False, False, True].
- `excludeRotationX` — A list of booleans to exclude the rotation X for target nodes. For example, excludeRotationX = [True, False, False, True].
- `excludeRotationY` — A list of booleans to exclude the rotation Y for target nodes. For example, excludeRotationY = [True, False, False, True].
- `excludeRotationZ` — A list of booleans to exclude the rotation Z for target nodes. For example, excludeRotationZ = [True, False, False, True].
- `nodeIds` — A list of integers to define target node IDs in the field.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldConstraintExcludeAutoByFileImport(filePath: str) -> DFEMFieldConstraintExcludeAuto`
Create DFEMFieldConstraintExcludeAuto by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldConstraintSinglePoint(orientations: [int], constrainTranslationX: [bool], constrainTranslationY: [bool], constrainTranslationZ: [bool], constrainRotationX: [bool], constrainRotationY: [bool], constrainRotationZ: [bool], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldConstraintSinglePoint`
Create DFEMFieldConstraintSinglePoint in this environment.

- `orientations` — The optional orientation. It can be either an IOrientation object which only accepts coordinate system or a list of IOrientation objects or a list of integers of the coordinate system IDs.
- `constrainTranslationX` — A list of booleans to constrain the translation X for target nodes. For example, constrainTranslationX = [True, False, False, True].
- `constrainTranslationY` — A list of booleans to constrain the translation Y for target nodes. For example, constrainTranslationY = [True, False, False, True].
- `constrainTranslationZ` — A list of booleans to constrain the translation Z for target nodes. For example, constrainTranslationZ = [True, False, False, True].
- `constrainRotationX` — A list of booleans to constrain the rotation X for target nodes. For example, constrainRotationX = [True, False, False, True].
- `constrainRotationY` — A list of booleans to constrain the rotation Y for target nodes. For example, constrainRotationY = [True, False, False, True].
- `constrainRotationZ` — A list of booleans to constrain the rotation Z for target nodes. For example, constrainRotationZ = [True, False, False, True].
- `nodeIds` — A list of integers to define target node IDs in the field.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldConstraintSinglePointByFileImport(filePath: str) -> DFEMFieldConstraintSinglePoint`

### `apex.environment.createDFEMFieldDeformationAxial(elementIds: [int], deformations: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldDeformationAxial`
Create DFEMFieldDeformationAxial in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `deformations` — A list of deformation values.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldDeformationAxialByFileImport(filePath: str) -> DFEMFieldDeformationAxial`
Create DFEMFieldDeformationAxial by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldEnforcedMotion(nodeIds: [int], orientations: [int], translationsX: [float], translationsY: [float], translationsZ: [float], rotationsX: [float], rotationsY: [float], rotationsZ: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldEnforcedMotion`
Create DFEMFieldEnforcedMotion in this environment. It can be used for both EnforcedMotionTotalVariable and EnforcedMotionRelativeVariable.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — The orientations of this DFEMFieldEnforcedMotion
- `translationsX` — The translationsX of this DFEMFieldEnforcedMotion
- `translationsY` — The list of translation values in Y axis.
- `translationsZ` — The list of translation values in Z axis.
- `rotationsX` — The list of rotation values about X axis.
- `rotationsY` — The list of rotation values about Y axis.
- `rotationsZ` — The list of rotation values about Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldEnforcedMotionByFileImport(filePath: str) -> DFEMFieldEnforcedMotion`
Create DFEMFieldEnforcedMotion by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldForceComponent(nodeIds: [int], orientations: [int], scaleFactors: [float], forcesX: [float], forcesY: [float], forcesZ: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldForceComponent`
Create DFEMFieldForceComponent in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — An optional orientations. It can be either an IOrientation object which only accepts a coordinate system object or a list of IOrientation objects. If omitted, the components are defined in the basic coordinate system.
- `scaleFactors` — An optional scale factor. It can be either a float value or a list of float. If omitted,the scale factor is 1.0.
- `forcesX` — A list of force component values in X axis.
- `forcesY` — A list of force component values in Y axis.
- `forcesZ` — A list of force component values in Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldForceComponentByFileImport(filePath: str) -> DFEMFieldForceComponent`
Create DFEMFieldForceComponent by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldForceFollowerNormal(nodeIds: [int], forceMagnitudes: [float], points1: [int], points2: [int], points3: [int], points4: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldForceFollowerNormal`
Create DFEMFieldForceFollowerNormal in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `forceMagnitudes` — A list of force magnitude.
- `points1` — The starting point of the first vector. It can be either a point or a list of points.
- `points2` — The end point of the first vector. It can be either a point or a list of points.
- `points3` — The starting point of the second vector. It can be either a point or a list of points.
- `points4` — The end point of the second vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldForceFollowerNormalByFileImport(filePath: str) -> DFEMFieldForceFollowerNormal`
Create DFEMFieldForceFollowerNormal by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldForceFollowerVector(nodeIds: [int], forceMagnitudes: [float], points1: [int], points2: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldForceFollowerVector`
Create DFEMFieldForceFollowerVector in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `forceMagnitudes` — A list of force magnitudes.
- `points1` — the starting point of the load vector. It can be either a point or a list points.
- `points2` — the end point of the load vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldForceFollowerVectorByFileImport(filePath: str) -> DFEMFieldForceFollowerVector`
Create DFEMFieldForceFollowerVector by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldInitialDisplacementVelocity(nodeIds: [int], displacementsX: [float], displacementsY: [float], displacementsZ: [float], displacementsRx: [float], displacementsRy: [float], displacementsRz: [float], velocitiesX: [float], velocitiesY: [float], velocitiesZ: [float], velocitiesRx: [float], velocitiesRy: [float], velocitiesRz: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldInitialDisplacementVelocity`
Create DFEMFieldInitialDisplacementVelocity in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `displacementsX` — A list of displacement values in X axis.
- `displacementsY` — A list of displacement values in Y axis.
- `displacementsZ` — A list of displacement values in Z axis.
- `displacementsRx` — A list of rotation values about X axis.
- `displacementsRy` — A list of rotation values about Y axis.
- `displacementsRz` — A list of rotation values about Z axis.
- `velocitiesX` — A list of velocity values in X axis.
- `velocitiesY` — A list of velocity values in Y axis.
- `velocitiesZ` — A list of velocity values in Z axis.
- `velocitiesRx` — A list of angular velocity values about X axis.
- `velocitiesRy` — A list of angular velocity values about Y axis.
- `velocitiesRz` — A list of angular velocity values about Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldInitialDisplacementVelocityByFileImport(filePath: str) -> DFEMFieldInitialDisplacementVelocity`
Create DFEMFieldInitialDisplacementVelocity by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldInitialStrain(element1Ids: [int], element2Ids: [int], ints1: [int], intsN: [int], layers1: [int], layersN: [int], strains: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldInitialStrain`
Create DFEMFieldInitialStrain in this environment.

- `element1Ids` — A list of integers to define the starting element IDs in the field.
- `element2Ids` — A list of integers to define the end element IDs in the field.
- `ints1` — The number of the first integration point. It can be one integer to indicate that all first integration points is are the same number or a list of integers to define different first integration point numbers.
- `intsN` — The number of the last integration point. It can be either one integer to indicate that all last integration point numbers are the same, or a list of integers to define different last integration point numbers. If omitted, the last integration point numbers are the same with the first integration point numbers.
- `layers1` — The number of the first integration layer. It can be either one integer to indicate that all first integration layer numbers are the same or a list of integers to define different first integration numbers.
- `layersN` — The number of the last integration layer. It can be either one integer to indicate that all last integration number is the same or a list of integers to define different last integration numbers. If omitted, the last layer number is the same with the first layer number.
- `strains` — The strains of this DFEMFieldInitialStrain
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldInitialStrainByFileImport(filePath: str) -> DFEMFieldInitialStrain`
Create DFEMFieldInitialStrain by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldInitialStress(element1Ids: [int], element2Ids: [int], ints1: [int], intsN: [int], layers1: [int], layersN: [int], stresses1: [float], stresses2: [float], stresses3: [float], stresses4: [float], stresses5: [float], stresses6: [float], stresses7: [float], coordinateSystemFlags: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldInitialStress`
Create DFEMFieldInitialStress in this environment.

- `element1Ids` — A list of integers to define the starting element IDs in the field.
- `element2Ids` — A list of integers to define the end element IDs in the field.
- `ints1` — The number of the first integration point. It can be one integer to indicate that all first integration points is are the same number or a list of integers to define different first integration point numbers.
- `intsN` — The number of the last integration point. It can be either one integer to indicate that all last integration point numbers are the same, or a list of integers to define different last integration point numbers. If omitted, the last integration point numbers are the same with the first integration point numbers.
- `layers1` — The number of the first integration layer. It can be either one integer to indicate that all first integration layer numbers are the same or a list of integers to define different first integration numbers.
- `layersN` — The number of the last integration layer. It can be either one integer to indicate that all last integration number is the same or a list of integers to define different last integration numbers. If omitted, the last layer number is the same with the first layer number.
- `stresses1` — A list of stress values in the first component.
- `stresses2` — A list of stress values in the second component.
- `stresses3` — A list of stress values in the third component.
- `stresses4` — A list of stress values in the fourth component.
- `stresses5` — A list of stress values in the fifth component.
- `stresses6` — A list of stress values in the sixth component.
- `stresses7` — A list of stress values in the seventh component.
- `coordinateSystemFlags` — The coordinateSystemFlags of this DFEMFieldInitialStress
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldInitialStressByFileImport(filePath: str) -> DFEMFieldInitialStress`
Create DFEMFieldInitialStress by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldLoadAreaFactor(nodeIds: [int], scaleFactorsX: [float], scaleFactorsY: [float], scaleFactorsZ: [float], scaleFactorsRx: [float], scaleFactorsRy: [float], scaleFactorsRz: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldLoadAreaFactor`
Create DFEMFieldLoadAreaFactor in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `scaleFactorsX` — A list of load scale(area) factors in the translation X axis. Note that the scale factor in translation dof has the unit of force.
- `scaleFactorsY` — A list of load scale(area) factors in the translation Y axis. Note that the scale factor in translation dof has the unit of force.
- `scaleFactorsZ` — A list of load scale(area) factors in the translation Z axis. Note that the scale factor in translation dof has the unit of force.
- `scaleFactorsRx` — A list of load scale(area) factors in the rotation X axis. Note that the scale factor in rotation dof has the unit of moment.
- `scaleFactorsRy` — A list of load scale(area) factors in the rotation Y axis. Note that the scale factor in rotation dof has the unit of moment.
- `scaleFactorsRz` — A list of load scale(area) factors in the rotation z axis. Note that the scale factor in rotation dof has the unit of moment.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldLoadAreaFactorByFileImport(filePath: str) -> DFEMFieldLoadAreaFactor`
Create DFEMFieldLoadAreaFactor by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldLoadDistributed(elementIds: [int], pressuresCorner1: [float], pressuresCorner2: [float], pressuresCorner3: [float], pressuresCorner4: [float], orientations: [int], directionsX: [float], directionsY: [float], directionsZ: [float], node1Ids: [int], node2Ids: [int], node3Ids: [int], node4Ids: [int], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> DFEMFieldLoadDistributed`
Create DFEMFieldLoadDistributed in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `pressuresCorner1` — A list of pressure values. If the inputType is element uniform, each pressure is defined on the whole element. If the inputType is element variable, each pressure is defined on the first corner of each element.
- `pressuresCorner2` — A list of pressure values defined on the second corner of each target element.
- `pressuresCorner3` — A list of pressure values defined on the third corner of each target element.
- `pressuresCorner4` — A list of pressure values defined on the fourth corner of each target element.
- `orientations` — An optional orientations. It can be either an IOrientation object which only accepts a coordinate system object or a list of IOrientation objects. If omitted, the load direction components are defined basic coordinate system.
- `directionsX` — One float value to indicate that all direction vectors have the same X component, or a list of float values to define different X components for each direction vector.
- `directionsY` — One float value to indicate that all direction vectors have the same Y component, or a list of float values to define different Y components for each direction vector.
- `directionsZ` — One float value to indicate that all direction vectors have the same Z component, or a list of float values to define different Z components for each direction vector.
- `node1Ids` — The node1Ids of this DFEMFieldLoadDistributed
- `node2Ids` — The node2Ids of this DFEMFieldLoadDistributed
- `node3Ids` — The node3Ids of this DFEMFieldLoadDistributed
- `node4Ids` — The node4Ids of this DFEMFieldLoadDistributed
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only pressure is necessary and it is automatically applied to pressureCorner2, pressureCorner3 and pressureCorner4. If the inputType is element variable, pressure is the applied to corner1 and other three corners must be defined as well.

### `apex.environment.createDFEMFieldLoadDistributedBeam2(elementIds: [int], loadTypes: [apex.attribute.LoadTypeDistributedBeam2], scaleTypes: [apex.attribute.ScaleTypeDistributedBeam2], distancesX1: [float], loadFactorsX1: [float], distancesX2: [float], loadFactorsX2: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> DFEMFieldLoadDistributedBeam2`
Create DFEMFieldLoadDistributedBeam2 in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `loadTypes` — The loadType of the beam distributed load applied to beam element with two nodes. It can be either an enumeration to define one load type for all loads or a list of enumeration to define different load types for each load.
- `scaleTypes` — The scaleType of distancesX1 and distancesX2. It can be either an enumeration to define one scale type for all distances or a list of enumeration to define different scale types for each distance. If inputType is element uniform, this argument should be omitted.
- `distancesX1` — The distance along element axis from end A for load factor X1. It can be either a float value to define one distance for all elements or a list of floats to define different distances for each element. If inputType is element uniform this argument should be omitted.
- `loadFactorsX1` — The load factors at X1. It can be either a float to define the load factor for all positions or a list of floats to define different load factors for each position.
- `distancesX2` — The distance along element axis from end A for load factor X2. It can be either a float value to define one distance for all elements or a list of floats to define different distances for each element. If inputType is element uniform this argument should be omitted.
- `loadFactorsX2` — The optional load factor at X2 position. It can be either a float to define the load factor for all positions or a list of floats to define different load factors for each position. If the inputType is element uniform this argument should be omitted.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, loadfaxtorX1 and loadType are necessary and it is automatically applied to loadFactorX2. The distanceX1 is 0.0, the distanceX2 is 1.0, the scaleType is "Fractional". If the inputType is element variable, both loadfaxtorX1 and loadfaxtorX2 can be defined. While distanceX1, distanceX2 and scaleType can be defined.

### `apex.environment.createDFEMFieldLoadDistributedBeam2ByFileImport(filePath: str) -> DFEMFieldLoadDistributedBeam2`
Create DFEMFieldLoadDistributedBeam2 by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldLoadDistributedBeam3(elementIds: [int], orientations: [int], loadVectorsX: [float], loadVectorsY: [float], loadVectorsZ: [float], loadTypes: [apex.attribute.LoadTypeDistributedBeam3], loadScaleFactors: [float], magnitudesEndA: [float], magnitudesEndB: [float], magnitudesMidC: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> DFEMFieldLoadDistributedBeam3`
Create DFEMFieldLoadDistributedBeam3 in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `orientations` — The orientations of this DFEMFieldLoadDistributedBeam3
- `loadVectorsX` — The X component of the load vector.
- `loadVectorsY` — The Y component of the load vector.
- `loadVectorsZ` — The Z component of the load vector.
- `loadTypes` — The loadType of the beam distributed load applied to beam element with two nodes. It can be either an enumeration to define one load type for all loads or a list of enumeration to define different load types for each load.
- `loadScaleFactors` — The optional load factor. It can be either a float value used for all load vectors or a list of floats to define different scale factors for each load vector. If omitted, the default value is 1.0.
- `magnitudesEndA` — The load magnitude at end A. It can be either a float value to define one magnitude for all ends or a list of float to define different magnitudes for each end. If the input type is element uniform, this argument should be omitted.
- `magnitudesEndB` — The load magnitude at end B. It can be either a float value to define one magnitude for all ends or a list of float to define different magnitudes for each end. If the input type is element uniform, this argument should be omitted.
- `magnitudesMidC` — The load magnitude at the point C which is between end A and end B. It can be either a float value to define one magnitude for all ends or a list of float to define different magnitudes for each end. If the input type is element uniform, this argument should be omitted.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, the magnitudes on end A, end B and end C are always 1.0 and load scale factor is 1.0. These four arguments should be omitted. If the inputType is element variable, all parameters can be defined.

### `apex.environment.createDFEMFieldLoadDistributedBeam3ByFileImport(filePath: str) -> DFEMFieldLoadDistributedBeam3`
Create DFEMFieldLoadDistributedBeam3 by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldLoadDistributedByFileImport(filePath: str) -> DFEMFieldLoadDistributed`

### `apex.environment.createDFEMFieldMomentComponent(nodeIds: [int], orientations: [int], scaleFactors: [float], momentsX: [float], momentsY: [float], momentsZ: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldMomentComponent`
Create DFEMFieldMomentComponent in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — An optional orientation. It can be either an IOrientation object which only accepts a coordinate system object or a list of IOrientation objects. If omitted, the components are defined in the basic coordinate system.
- `scaleFactors` — An optional scale factor. It can be either a float value or a list of float. If omitted,the scale factor is 1.0.
- `momentsX` — A list of moment component values in X axis.
- `momentsY` — A list of moment component values in Y axis.
- `momentsZ` — A list of moment component values in Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldMomentComponentByFileImport(filePath: str) -> DFEMFieldMomentComponent`
Create DFEMFieldMomentComponent by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldMomentFollowerNormal(nodeIds: [int], momentMagnitudes: [float], points1: [int], points2: [int], points3: [int], points4: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldMomentFollowerNormal`
Create DFEMFieldMomentFollowerComponent in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `momentMagnitudes` — A list of moment magnitude.
- `points1` — The starting point of the first vector. It can be either a point or a list of points.
- `points2` — The end point of the first vector. It can be either a point or a list of points.
- `points3` — The starting point of the second vector. It can be either a point or a list of points.
- `points4` — The end point of the second vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldMomentFollowerNormalByFileImport(filePath: str) -> DFEMFieldMomentFollowerNormal`
Create DFEMFieldMomentFollowerNormal by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldMomentFollowerVector(nodeIds: [int], momentMagnitudes: [float], points1: [int], points2: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldMomentFollowerVector`
Create DFEMFieldMomentFollowerVector in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `momentMagnitudes` — A list of moment magnitudes.
- `points1` — the starting point of the load vector. It can be either a point or a list points.
- `points2` — the end point of the load vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldMomentFollowerVectorByFileImport(filePath: str) -> DFEMFieldMomentFollowerVector`
Create DFEMFieldMomentFollowerVector by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldPhaseLead(nodeIds: [int], phaseLeadsX: [float], phaseLeadsY: [float], phaseLeadsZ: [float], phaseLeadsRx: [float], phaseLeadsRy: [float], phaseLeadsRz: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldPhaseLead`
Create DFEMFieldPhaseLead in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `phaseLeadsX` — A list of phase lead values in the X component.
- `phaseLeadsY` — A list of phase lead values in the Y component.
- `phaseLeadsZ` — A list of phase lead values in the Z component.
- `phaseLeadsRx` — A list of phase lead values in the rotation X component.
- `phaseLeadsRy` — A list of phase lead values in the rotation Y component.
- `phaseLeadsRz` — A list of phase lead values in the rotation Z component.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldPhaseLeadByFileImport(filePath: str) -> DFEMFieldPhaseLead`
Create DFEMFieldPhaseLead by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldPressure(elementIds: [int], pressuresCorner1: [float], pressuresCorner2: [float], pressuresCorner3: [float], pressuresCorner4: [float], node1Ids: [int], node2Ids: [int], node3Ids: [int], node4Ids: [int], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> DFEMFieldPressure`
Create DFEMFieldPressure in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `pressuresCorner1` — A list of pressure values. If the inputType is element uniform, each pressure is defined on the whole element. If the inputType is element variable, each pressure is defined on the first corner of each element.
- `pressuresCorner2` — A list of pressure values defined on the second corner of each target element.
- `pressuresCorner3` — A list of pressure values defined on the third corner of each target element.
- `pressuresCorner4` — A list of pressure values defined on the fourth corner of each target element.
- `node1Ids` — The node1Ids of this DFEMFieldPressure
- `node2Ids` — The node2Ids of this DFEMFieldPressure
- `node3Ids` — The node3Ids of this DFEMFieldPressure
- `node4Ids` — The node4Ids of this DFEMFieldPressure
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only pressure is necessary and it is automatically applied to pressureCorner2, pressureCorner3 and pressureCorner4. If the inputType is element variable, pressure is the applied to corner1 and other three corners must be defined as well.

### `apex.environment.createDFEMFieldPressure2D(pressureMagnitudes: [float], elementIds: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldPressure2D`

- `pressureMagnitudes` — The pressureMagnitudes of this DFEMFieldPressure2D
- `elementIds` — The elementIds of this DFEMFieldPressure2D
- `pathNames` — The pathNames of this DFEMFieldPressure2D
- `pathIndices` — The pathIndices of this DFEMFieldPressure2D

### `apex.environment.createDFEMFieldPressure2DByFileImport(filePath: str) -> DFEMFieldPressure2D`

### `apex.environment.createDFEMFieldPressureArea(pressureMagnitudes: [float], vertices1: [int], vertices2: [int], vertices3: [int], vertices4: [int], pathNames: [str], pathIndices: [int]) -> DFEMFieldPressureArea`
Create DFEMFieldPressureArea in this environment.

- `pressureMagnitudes` — A list of floats to define the pressure values.
- `vertices1` — The vertices1 of this DFEMFieldPressureArea
- `vertices2` — The vertices2 of this DFEMFieldPressureArea
- `vertices3` — The vertices3 of this DFEMFieldPressureArea
- `vertices4` — The vertices4 of this DFEMFieldPressureArea
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldPressureAreaByFileImport(filePath: str) -> DFEMFieldPressureArea`
Create DFEMFieldPressureArea by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldPressureByFileImport(filePath: str) -> DFEMFieldPressure`
Create DFEMFieldPressure by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldSupportFreeBody(nodeIds: [int], orientations: [int], constrainTranslationX: [bool], constrainTranslationY: [bool], constrainTranslationZ: [bool], constrainRotationX: [bool], constrainRotationY: [bool], constrainRotationZ: [bool], pathNames: [str], pathIndices: [int]) -> DFEMFieldSupportFreeBody`
Create DFEMFieldSupportFreeBody in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — The optional orientation. It can be either an IOrientation object which only accepts coordinate system or a list of IOrientation objects or a list of integers of the coordinate system IDs.
- `constrainTranslationX` — A list of booleans to constrain the translation X for target nodes. For example, constrainTranslationX = [True, False, False, True].
- `constrainTranslationY` — A list of booleans to constrain the translation Y for target nodes. For example, constrainTranslationY = [True, False, False, True].
- `constrainTranslationZ` — A list of booleans to constrain the translation Z for target nodes. For example, constrainTranslationZ = [True, False, False, True].
- `constrainRotationX` — A list of booleans to constrain the rotation X for target nodes. For example, constrainRotationX = [True, False, False, True].
- `constrainRotationY` — A list of booleans to constrain the rotation Y for target nodes. For example, constrainRotationY = [True, False, False, True].
- `constrainRotationZ` — A list of booleans to constrain the rotation Z for target nodes. For example, constrainRotationZ = [True, False, False, True].
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldSupportFreeBodyByFileImport(filePath: str) -> DFEMFieldSupportFreeBody`

### `apex.environment.createDFEMFieldTemperatureGradient2D(elementIds: [int], temperaturesReferencePlane: [float], thermalGradients: [float], temperaturesLowerSurface: [float], temperaturesUpperSurface: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldTemperatureGradient2D`
Create DFEMFieldTemperatureGradient2D in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `temperaturesReferencePlane` — A list of temperature values at element reference plane.
- `thermalGradients` — A list of effective linear thermal gradients.
- `temperaturesLowerSurface` — A list of temperature values at lower surface.
- `temperaturesUpperSurface` — A list of temperature values at upper surface.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldTemperatureGradient2DByFileImport(filePath: str) -> DFEMFieldTemperatureGradient2D`
Create DFEMFieldTemperatureGradient2D by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldTemperatureGradient2DHeat(nodeIds: [int], temperaturesTop: [float], temperaturesBottom: [float], temperaturesMid: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldTemperatureGradient2DHeat`
Create DFEMFieldTemperatureGradient2DHeat in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `temperaturesTop` — A list of floats to define the temperatures at top location through the thickness.
- `temperaturesBottom` — A list of floats to define the temperatures at bottom location through the thickness.
- `temperaturesMid` — A list of floats to define the temperatures at mid location through the thickness.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldTemperatureGradient2DHeatByFileImport(filePath: str) -> DFEMFieldTemperatureGradient2DHeat`
Create DFEMFieldTemperatureGradient2DHeat by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldTemperatureGradientBeam2(elementIds: [int], temperaturesEndA: [float], temperaturesEndB: [float], thermalGradients1A: [float], thermalGradients1B: [float], thermalGradients2A: [float], thermalGradients2B: [float], temperaturesPointCendA: [float], temperaturesPointDendA: [float], temperaturesPointEendA: [float], temperaturesPointFendA: [float], temperaturesPointCendB: [float], temperaturesPointDendB: [float], temperaturesPointEendB: [float], temperaturesPointFendB: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> DFEMFieldTemperatureGradientBeam2`
Create DiFEMFieldTemperatureGradientBeam2 in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `temperaturesEndA` — The list of temperature values at end A on neutral axis. If the inputType is element uniform, this temperature value is assigned to end B as well.
- `temperaturesEndB` — The list of temperature values at end B on neutral axis. If the inputType is element uniform, this temperature value is ignored and derived from temperaturesEndA.
- `thermalGradients1A` — The effective thermal gradient in direction 1 at end A. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradient1B as well.
- `thermalGradients1B` — The effective thermal gradient in direction 1 at end B. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradient1A.
- `thermalGradients2A` — The effective thermal gradient in direction 2 at end A. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradient2B as well.
- `thermalGradients2B` — The effective thermal gradient in direction 2 at end B. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradient2A.
- `temperaturesPointCendA` — A list of temperature values on point C at end A, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointDendA` — A list of temperature values on point D at end A, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointEendA` — A list of temperature values on point E at end A, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointFendA` — A list of temperature values on point F at end A, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointCendB` — A list of temperature value on point C at end B, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointDendB` — A list of temperature values on point D at end B, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointEendB` — A list of temperature values on point E at end B, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointFendB` — A list of temperature values on point F at end B, used for stress recovery. It can be either a float value to indicate that all values are the same or a list of floats to define different temperature values for each target element.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathName. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.

### `apex.environment.createDFEMFieldTemperatureGradientBeam2ByFileImport(filePath: str) -> DFEMFieldTemperatureGradientBeam2`
Create DFEMFieldTemperatureGradientBeam2 by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldTemperatureGradientBeam3(elementIds: [int], temperaturesEndA: [float], temperaturesEndB: [float], temperaturesMidC: [float], thermalGradientsYA: [float], thermalGradientsZA: [float], thermalGradientsYB: [float], thermalGradientsZB: [float], thermalGradientsYC: [float], thermalGradientsZC: [float], temperaturesPointCendA: [float], temperaturesPointDendA: [float], temperaturesPointEendA: [float], temperaturesPointFendA: [float], temperaturesPointCendB: [float], temperaturesPointDendB: [float], temperaturesPointEendB: [float], temperaturesPointFendB: [float], temperaturesPointCmidC: [float], temperaturesPointDmidC: [float], temperaturesPointEmidC: [float], temperaturesPointFmidC: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> DFEMFieldTemperatureGradientBeam3`
Create DFEMFieldTemperatureGradientBeam3 in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `temperaturesEndA` — The list of temperature values at end A on neutral axis. If the inputType is element uniform, this temperature value is assigned to end B as well.
- `temperaturesEndB` — The list of temperature values at end B on neutral axis. If the inputType is element uniform, this temperature value is ignored and derived from temperaturesEndA.
- `temperaturesMidC` — The list of temperature values at mid C on neutral axis. If the inputType is element uniform, this temperature value is ignored and derived from temperaturesEndA.
- `thermalGradientsYA` — The effective thermal gradient in direction y at end A. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradientYB and thermalGradientYC.
- `thermalGradientsZA` — The effective thermal gradient in direction z at end A. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradientZB and thermalGradientZC.
- `thermalGradientsYB` — The effective thermal gradient in direction y at end B. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradient1A.
- `thermalGradientsZB` — The effective thermal gradient in direction z at end B. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradientZA.
- `thermalGradientsYC` — The effective thermal gradient in direction y at mid C. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradientYA.
- `thermalGradientsZC` — The effective thermal gradient in direction z at mid C. It can be either a float value to indicate that all the gradients are the same or a list of floats to define different gradient values for each target element. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradientZA.
- `temperaturesPointCendA` — A list of temperature values on point C at end A, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointDendA` — A list of temperature values on point D at end A, used for stress recovery.It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointEendA` — A list of temperature values on point E at end A, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointFendA` — A list of temperature values on point F at end A, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointCendB` — A list of temperature values on point C at end B, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointDendB` — A list of temperature values on point D at end B, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointEendB` — A list of temperature values on point E at end B, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointFendB` — A list of temperature values on point F at end B, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointCmidC` — A list of temperature values on point C at mid C, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointDmidC` — A list of temperature values on point D at mid C, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointEmidC` — A list of temperature values on point E at mid C, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `temperaturesPointFmidC` — A list of temperature values on point F at mid C, used for stress recovery. It can be either a float value to indicate that all the temperatures are the same or a list of floats to define different temperature values for each target element.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.

### `apex.environment.createDFEMFieldTemperatureGradientBeam3ByFileImport(filePath: str) -> DFEMFieldTemperatureGradientBeam3`
Create DFEMFieldTemperatureGradientBeam3 by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldTemperatureNodal(nodeIds: [int], temperatureValues: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldTemperatureNodal`
Create DFEMFieldTemperatureNodal in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `temperatureValues` — A list of floats to define temperature values at each node.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldTemperatureNodalByFileImport(filePath: str) -> DFEMFieldTemperatureNodal`
Create DFEMFieldTemperatureNodal by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDFEMFieldTimeDelay(nodeIds: [int], timeDelaysX: [float], timeDelaysY: [float], timeDelaysZ: [float], timeDelaysRx: [float], timeDelaysRy: [float], timeDelaysRz: [float], pathNames: [str], pathIndices: [int]) -> DFEMFieldTimeDelay`
Create DFEMFieldTimeDelay in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `timeDelaysX` — A list of time delay values in the X component.
- `timeDelaysY` — A list of time delay values in the Y component.
- `timeDelaysZ` — A list of time delay values in the Z component.
- `timeDelaysRx` — A list of time delay values in the rotation X component.
- `timeDelaysRy` — A list of time delay values in the rotation Y component.
- `timeDelaysRz` — A list of time delay values in the rotation Z component.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

### `apex.environment.createDFEMFieldTimeDelayByFileImport(filePath: str) -> DFEMFieldTimeDelay`
Create DFEMFieldTimeDelay by import file.

- `filePath` — A string to define the file path. Currently Apex only supports csv file. For example, "C:\Users\KX\Desktop\FEMfield.csv". The target file is imported to generate the discrete FEM Field.

### `apex.environment.createDisplacementConstraint(name: str, constraintType: apex.attribute.ConstraintType, applicationMethod: apex.attribute.ApplicationMethod, target: apex.EntityCollection = None, attachmentRegion: apex.EntityCollection = None, attachmentDistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, constraintProperties: apex.attribute.DisplacementConstraintProperty = None, orientation: apex.construct.Orientation = None, description: str = "") -> DisplacementConstraint`
Create a new DisplacementConstraint in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createConstraintDisplacement().

- `name` — of the new DisplacementConstraint. default = "" (auto-named)
- `constraintType` — of the new DisplacementConstraint.
- `applicationMethod` — of the new DisplacementConstraint.
- `target` — of the new DisplacementConstraint.
- `attachmentRegion` — of the new DisplacementConstraint.
- `attachmentDistributionType` — of the new DisplacementConstraint.
- `constraintProperties` — of the new DisplacementConstraint.
- `orientation` — of the new DisplacementConstraint.
- `description` — of the new DisplacementConstraint. default = ""

Returns: the created DisplacementConstraint

### `apex.environment.createEnforcedMotion(name: str, enforcedMotionRep: EnforcedMotionRep, applicationMethod: apex.attribute.ApplicationMethod, target: apex.EntityCollection = None, attachmentRegion: apex.EntityCollection = None, attachmentDistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, orientation: apex.construct.Orientation = None, description: str = "", constraintReference: DisplacementConstraint = None) -> EnforcedMotion`
Get a new EnforcedMotion in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadEnforcedMotionTotal().

- `name` — of the EnforcedMotion.
- `enforcedMotionRep` — of the EnforcedMotion.
- `applicationMethod` — of the EnforcedMotion.
- `target` — of the EnforcedMotion.
- `attachmentRegion` — of the EnforcedMotion.
- `attachmentDistributionType` — of the EnforcedMotion.
- `orientation` — of the EnforcedMotion.
- `description` — of the EnforcedMotion.
- `constraintReference` — of the EnforcedMotion.

### `apex.environment.createEnforcedMotionDynamicRepByComponent(name: str, description: str, motionType: apex.attribute.EnforcedMotionType, approach: apex.attribute.Approach, translationX: apex.DataTable3Col = None, translationY: apex.DataTable3Col = None, translationZ: apex.DataTable3Col = None, rotationX: apex.DataTable3Col = None, rotationY: apex.DataTable3Col = None, rotationZ: apex.DataTable3Col = None, id: int = 0) -> EnforcedMotionDynamicRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadEnforcedMotionTotal().

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `motionType` — of the ForceMomentRep.
- `approach` — of the ForceMomentRep.
- `translationX` — of the ForceMomentRep.
- `translationY` — of the ForceMomentRep.
- `translationZ` — of the ForceMomentRep.
- `rotationX` — of the ForceMomentRep.
- `rotationY` — of the ForceMomentRep.
- `rotationZ` — of the ForceMomentRep.
- `id` — Optional - the id. Default value is zero.

### `apex.environment.createEnforcedMotionStaticRepByComponent(name: str, description: str, translationX: float = NAN, translationY: float = NAN, translationZ: float = NAN, rotationX: float = NAN, rotationY: float = NAN, rotationZ: float = NAN, id: int = 0) -> EnforcedMotionRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadEnforcedMotionTotal().

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `translationX` — of the ForceMomentRep.
- `translationY` — of the ForceMomentRep.
- `translationZ` — of the ForceMomentRep.
- `rotationX` — of the ForceMomentRep.
- `rotationY` — of the ForceMomentRep.
- `rotationZ` — of the ForceMomentRep.
- `id` — Optional - the id. Default value is zero.

### `apex.environment.createEnforcedMotionStaticRepByResultant(name: str, description: str, translationMagnitude: float = NAN, rotationMagnitude: float = NAN, translationOrientation: apex.construct.Orientation = None, rotationOrientation: apex.construct.Orientation = None, id: int = 0) -> EnforcedMotionRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadEnforcedMotionTotal().

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `translationMagnitude` — of the ForceMomentRep.
- `rotationMagnitude` — of the ForceMomentRep.
- `translationOrientation` — of the ForceMomentRep.
- `rotationOrientation` — of the ForceMomentRep.
- `id` — Optional - the id. Default value is zero.

### `apex.environment.createForceMoment(name: str, forceMomentRep: ForceMomentRep, applicationMethod: apex.attribute.ApplicationMethod, target: apex.EntityCollection = None, attachmentRegion: apex.EntityCollection = None, attachmentDistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, orientation: apex.construct.Orientation = None, description: str = "", constraintReference: DisplacementConstraint = None) -> ForceMoment`
Get a new ForceMoment in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadForceComponent(), createLoadMomentComponent().

- `name` — of the ForceMoment.
- `forceMomentRep` — of the ForceMoment.
- `applicationMethod` — of the ForceMoment.
- `target` — of the ForceMoment.
- `attachmentRegion` — of the ForceMoment.
- `attachmentDistributionType` — of the ForceMoment.
- `orientation` — of the ForceMoment.
- `description` — of the ForceMoment.
- `constraintReference` — of the ForceMoment.

### `apex.environment.createForceMomentDynamicRepByComponent(name: str, description: str, approach: apex.attribute.Approach, forceX: apex.DataTable3Col = None, forceY: apex.DataTable3Col = None, forceZ: apex.DataTable3Col = None, momentX: apex.DataTable3Col = None, momentY: apex.DataTable3Col = None, momentZ: apex.DataTable3Col = None, id: int = 0) -> ForceMomentDynamicRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadForceComponent(), createLoadMomentComponent().

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `approach` — of the ForceMomentRep.
- `forceX` — of the ForceMomentRep.
- `forceY` — of the ForceMomentRep.
- `forceZ` — of the ForceMomentRep.
- `momentX` — of the ForceMomentRep.
- `momentY` — of the ForceMomentRep.
- `momentZ` — of the ForceMomentRep.
- `id` — Optional - the id. Default value is zero.

### `apex.environment.createForceMomentStaticRepByComponent(name: str, description: str, forceX: float = NAN, forceY: float = NAN, forceZ: float = NAN, momentX: float = NAN, momentY: float = NAN, momentZ: float = NAN, id: int = 0) -> ForceMomentRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadForceComponent(), createLoadMomentComponent().

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `forceX` — of the ForceMomentRep.
- `forceY` — of the ForceMomentRep.
- `forceZ` — of the ForceMomentRep.
- `momentX` — of the ForceMomentRep.
- `momentY` — of the ForceMomentRep.
- `momentZ` — of the ForceMomentRep.
- `id` — Optional - the id. Default value is zero.

### `apex.environment.createForceMomentStaticRepByResultant(name: str, description: str, forceMagnitude: float = NAN, momentMagnitude: float = NAN, forceOrientation: apex.construct.Orientation = None, momentOrientation: apex.construct.Orientation = None, id: int = 0) -> ForceMomentRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadForceComponent(), createLoadMomentComponent().

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `forceMagnitude` — of the ForceMomentRep.
- `momentMagnitude` — of the ForceMomentRep.
- `forceOrientation` — of the ForceMomentRep.
- `momentOrientation` — of the ForceMomentRep.
- `id` — Optional - the id. Default value is zero.

### `apex.environment.createGravity(name: str, orientation: apex.construct.Orientation, magnitude: float, vector_x_component: float = 0.0, vector_y_component: float = 0.0, vector_z_component: float = 1.0, description: str = "", coordinateSystem: apex.construct.CoordinateSystem = None, coordinateSystemDefinition: int = 0) -> Gravity`
Create a new Gravity in this environment.

- `name` — of the new gravity. default = "" (auto-named)
- `orientation` — of the new gravity.
- `magnitude` — of the new gravity.
- `vector_x_component` — of the new gravity. default = 0.0
- `vector_y_component` — of the new gravity. default = 0.0
- `vector_z_component` — of the new gravity. default = 1.0
- `description` — of the new gravity. default = ""
- `coordinateSystem` — of the new gravity
- `coordinateSystemDefinition` — the optional coordinate system definition: "apex.attribute.CoordinateSystemDefinition.SuperElement", the coordinate system is defined in the super-element and will be translated, rotated with the super-element. "apex.attribute.CoordinateSystemDefinition.Residual", the coordinate system is defined in the residual structure and stationary with the basic coordinate system. If omitted, the default value is "apex.attribute.CoordinateSystemDefinition.SuperElement".

Returns: the created gravity

### `apex.environment.createGravityByG(name: str, gravConstant: float, orientation: apex.construct.Orientation, gravConstantMultiplier: float, vector_x_component: float = 0.0, vector_y_component: float = 0.0, vector_z_component: float = 1.0, description: str = "", coordinateSystem: apex.construct.CoordinateSystem = None, coordinateSystemDefinition: int = 0) -> Gravity`
Create a new Gravity by a gravity constant in this environment.

- `name` — of the new gravity. default = "" (auto-named)
- `gravConstant` — of the new gravity.
- `orientation` — of the new gravity.
- `gravConstantMultiplier` — of the new gravity.
- `vector_x_component` — of the new gravity. default = 0.0
- `vector_y_component` — of the new gravity. default = 0.0
- `vector_z_component` — of the new gravity. default = 1.0
- `description` — of the new gravity. default = ""
- `coordinateSystem` — of the new gravity
- `coordinateSystemDefinition` — the optional coordinate system definition: "apex.attribute.CoordinateSystemDefinition.SuperElement", the coordinate system is defined in the super-element and will be translated, rotated with the super-element. "apex.attribute.CoordinateSystemDefinition.Residual", the coordinate system is defined in the residual structure and stationary with the basic coordinate system. If omitted, the default value is "apex.attribute.CoordinateSystemDefinition.SuperElement".

Returns: the created gravity

### `apex.environment.createInitialDisplacementVelocity(name: str, description: str, id: int, target: apex.EntityCollection, displacementX: float, displacementY: float, displacementZ: float, displacementRx: float, displacementRy: float, displacementRz: float, velocityX: float, velocityY: float, velocityZ: float, velocityRx: float, velocityRy: float, velocityRz: float) -> InitialDisplacementVelocity`
Create InitialDisplacementVelocity in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialDisplacementVelocity. If omitted, system automatically assigns the largest id + 1 to it.
- `target` — The target entities that the InitialDisplacementVelocity is applied to.
- `displacementX` — The displacement value in X axis.
- `displacementY` — The displacement value in Y axis.
- `displacementZ` — The displacement value in Z axis.
- `displacementRx` — The displacement in rotation X axis.
- `displacementRy` — The displacement in rotation Y axis.
- `displacementRz` — The displacement in rotation Z axis.
- `velocityX` — The velocity value in X axis.
- `velocityY` — The velocity value in Y axis.
- `velocityZ` — The velocity value in Z axis.
- `velocityRx` — The velocity value in rotation X axis.
- `velocityRy` — The velocity value in rotation Y axis.
- `velocityRz` — The velocity value in rotation Z axis.

### `apex.environment.createInitialDisplacementVelocityVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldInitialDisplacementVelocity) -> InitialDisplacementVelocityVariable`
Create InitialDisplacementVelocityVariable in this environment.

- `id` — The id of this InitialDisplacementVelocity. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the initial displacement and velocity.

### `apex.environment.createInitialStrain(name: str, description: str, target: apex.EntityCollection, int1: int, intN: int, layer1: int, layerN: int, strain: float) -> InitialStrain`
Create InitialStrain in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `target` — The target that the initial strain is applied to.
- `int1` — The number of the first integration point. If omitted, the default value is 1.
- `intN` — The number of the last integration point. If omitted, the default value is 4.
- `layer1` — The number of the first integration layer. If omitted, the default value is 1.
- `layerN` — The number of the last integration layer. If omitted, the default value is 5.
- `strain` — The initial strain value.

### `apex.environment.createInitialStrainVariable(name: str, description: str, spatialTarget: apex.environment.DFEMFieldInitialStrain) -> InitialStrainVariable`
Create InitialStrainVariable in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the initial strain.

### `apex.environment.createInitialStress(name: str, description: str, target: apex.EntityCollection, int1: int, intN: int, layer1: int, layerN: int, stress1: float, stress2: float, stress3: float, stress4: float, stress5: float, stress6: float, stress7: float, coordinateSystemFlag: int) -> InitialStress`
Create InitialStress in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `target` — The entityCollection that the initialStress is applied to.
- `int1` — The number of the first integration point. If omitted, the default value is 1.
- `intN` — The number of the last integration point. If omitted, the default value is 4.
- `layer1` — The number of the first integration layer. If omitted, the default value is 1.
- `layerN` — The number of the last integration layer. If omitted, the default value is 5.
- `stress1` — The stress value of the first component, for example, stress in X component for both solid and shell element, axial stress for beam element.
- `stress2` — The stress value of the second component, for example, stress in Y component for both solid and shell element, twist stress for beam element.
- `stress3` — The stress value of the third component, for example, stress in Z component for both solid and shell element.
- `stress4` — The stress value of the fourth component, for example, stress in XY component for both solid and shell element.
- `stress5` — The stress value of the fifth component, for example, stress in YZ component for both solid and shell element.
- `stress6` — The stress value of the sixth component, for example, stress in ZX component for both solid and shell element.
- `stress7` — The stress value of the seventh component, hydrostatic pressure for Herrmann elements only.
- `coordinateSystemFlag` — An optional integer -1 or 0 to indicate the coordinate system that the initial stress is evaluated. -1 points to the element coordinate system and 0 points to the basic coordinate system. If omitted, the default value is -1. Note that for CQUAD4 and CTRIA3 elements, only element coordinate system makes sense - even the label is 0, the initial stress will be transformed from basic coordinate system to element coordinate system.

### `apex.environment.createInitialStressVariable(name: str, description: str, spatialTarget: apex.environment.DFEMFieldInitialStress) -> InitialStressVariable`
Create InitialStressVariable in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the initial stress.

### `apex.environment.createInitialTemperatureDefault(name: str, description: str, id: int, defaultTemperature: float) -> InitialTemperatureDefault`
Create InitialTemperatureDefault in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialCondition. If omitted, system automatically assigns the largest load id + 1 to it.
- `defaultTemperature` — The defaultTemperature of this InitialTemperatureDefault

### `apex.environment.createInitialTemperatureGradient2D(name: str, description: str, id: int, target: apex.EntityCollection, temperatureReferencePlane: float, thermalGradient: float, temperatureLowerSurface: float, temperatureUpperSurface: float) -> InitialTemperatureGradient2D`
Create InitialTemperatureGradient2D in this environment. Note it must be applied to the nodes on the surface elements.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialTemperatureSurface. If omitted, system automatically assigns the largest id + 1 to it.
- `target` — The target entities that the InitialTemperatureSurface is applied to.
- `temperatureReferencePlane` — The temperature at element reference plane. If not provided, the default value is 0.0.
- `thermalGradient` — The effective linear thermal gradient. If not provided, the default value is 0.0.
- `temperatureLowerSurface` — The temperature value at lower surface.
- `temperatureUpperSurface` — The temperature value at upper surface.

### `apex.environment.createInitialTemperatureGradient2DHeat(name: str, description: str, id: int, target: apex.EntityCollection, temperatureTop: float, temperatureBottom: float, temperatureMid: float) -> InitialTemperatureGradient2DHeat`
Create InitialTemperatureGradient2DHeat in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialCondition. If omitted, system automatically assigns the largest load id + 1 to it.
- `target` — The target entities that the InitialCondition is applied to.
- `temperatureTop` — the optional float value to define the temperature value at top location through the thickness.
- `temperatureBottom` — the optional float value to define the temperature value at bottom location through the thickness.
- `temperatureMid` — the optional float value to define the temperature value at mid location through the thickness.

### `apex.environment.createInitialTemperatureGradient2DHeatVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2DHeat) -> InitialTemperatureGradient2DHeatVariable`
Create InitialTemperatureGradient2DHeatVariable in this environment.

- `id` — The id of this InitialCondition. If omitted, system automatically assigns the largest load id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the temperature.

### `apex.environment.createInitialTemperatureGradient2DVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2D) -> InitialTemperatureGradient2DVariable`
Create InitialTemperatureGradient2DVariable in this environment. Note it must be applied to the nodes on the surface elements.

- `id` — The id of this InitialTemperatureSurface. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createInitialTemperatureGradientBeam2(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, thermalGradient1A: float, thermalGradient1B: float, thermalGradient2A: float, thermalGradient2B: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, inputType: apex.attribute.InputType) -> InitialTemperatureGradientBeam2`
Create InitialTemperatureGradientBeam2 in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialTemperatureBeam2. If omitted, system automatically assigns the largest id + 1 to it.
- `target` — The target entities that the InitialTemperatureBeam2 is applied to.
- `temperatureEndA` — The temperature value at end A on neutral axis. If the inputType is element uniform, this temperature value is assigned to end B as well.
- `temperatureEndB` — The temperature value at end B on neutral axis. If the inputType is element variable, this temperature value is ignored and derived from temperatureEndA.
- `thermalGradient1A` — The effective thermal gradient in direction 1 at end A. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradient1B as well.
- `thermalGradient1B` — The effective thermal gradient in direction 1 at end B. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradient1A.
- `thermalGradient2A` — The effective thermal gradient in direction 2 at end A. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradient2B as well.
- `thermalGradient2B` — The effective thermal gradient in direction 2 at end B. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradient2A.
- `temperaturePointCendA` — The temperature value on point C at end A, used for stress recovery.
- `temperaturePointDendA` — The temperature value on point D at end A, used for stress recovery.
- `temperaturePointEendA` — the temperature value on point E at end A, used for stress recovery.
- `temperaturePointFendA` — The temperature value on point F at end A, used for stress recovery.
- `temperaturePointCendB` — The temperature value on point C at end B, used for stress recovery.
- `temperaturePointDendB` — The temperature value on point D at end B, used for stress recovery.
- `temperaturePointEendB` — The temperature value on point E at end B, used for stress recovery.
- `temperaturePointFendB` — The temperature value on point F at end B, used for stress recovery.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.

### `apex.environment.createInitialTemperatureGradientBeam2Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam2) -> InitialTemperatureGradientBeam2Variable`
Create InitialTemperatureGradientBeam2Variable in this environment.

- `id` — The id of this InitialTemperatureBeam2. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the temperature.

### `apex.environment.createInitialTemperatureGradientBeam3(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, temperatureMidC: float, thermalGradientYA: float, thermalGradientZA: float, thermalGradientYB: float, thermalGradientZB: float, thermalGradientYC: float, thermalGradientZC: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, temperaturePointCmidC: float, temperaturePointDmidC: float, temperaturePointEmidC: float, temperaturePointFmidC: float, inputType: apex.attribute.InputType) -> InitialTemperatureGradientBeam3`
Create InitialTemperatureGradientBeam3 in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialTemperatureBeam3. If omitted, system automatically assigns the largest id + 1 to it.
- `target` — The target entities that the InitialTemperatureBeam3 is applied to.
- `temperatureEndA` — The temperature value at end A on neutral axis. If the inputType is element uniform, this temperature value is automatically assigned to end B and mid C.
- `temperatureEndB` — The temperature value at end B on neutral axis. If the inputType is element uniform, this temperature value is ignored and derived from end A.
- `temperatureMidC` — The temperature value at midside point C on neutral axis. If the inputType is element uniform, this temperature value is ignored and derived from end A.
- `thermalGradientYA` — The effective thermal gradient in direction y at end A. If the inputType is element uniform, this thermal gradient is automatically assigned to YB and YC.
- `thermalGradientZA` — The effective thermal gradient in direction z at end A. If the inputType is element uniform, this thermal gradient is automatically assigned to ZB and ZC.
- `thermalGradientYB` — The effective thermal gradient in direction y at end B. If the inputType is element uniform, this thermal gradient is ignored and derived from YA.
- `thermalGradientZB` — The effective thermal gradient in direction z at end B.If the inputType is element uniform, this thermal gradient is ignored and derived from ZA.
- `thermalGradientYC` — The effective thermal gradient in direction y at point C.If the inputType is element uniform, this thermal gradient is ignored and derived from YA.
- `thermalGradientZC` — The effective thermal gradient in direction z at point C. If the inputType is element uniform, this thermal gradient is ignored and derived from ZA.
- `temperaturePointCendA` — The temperature value on point C at end A, used for stress recovery.
- `temperaturePointDendA` — The temperature value on point D at end A, used for stress recovery.
- `temperaturePointEendA` — the temperature value on point E at end A, used for stress recovery.
- `temperaturePointFendA` — The temperature value on point F at end A, used for stress recovery.
- `temperaturePointCendB` — The temperature value on point C at end B, used for stress recovery.
- `temperaturePointDendB` — The temperature value on point D at end B, used for stress recovery.
- `temperaturePointEendB` — The temperature value on point E at end B, used for stress recovery.
- `temperaturePointFendB` — The temperature value on point F at end B, used for stress recovery.
- `temperaturePointCmidC` — The temperature value on point C at mid C, used for stress recovery.
- `temperaturePointDmidC` — The temperaturePointDmidC of this InitialTemperatureGradientBeam3
- `temperaturePointEmidC` — The temperature value on point E at mid C, used for stress recovery.
- `temperaturePointFmidC` — The temperature value on point F at mid C, used for stress recovery.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B and mid C. If the inputType is element variable, all temperature values and thermal gradients can be defined.

### `apex.environment.createInitialTemperatureGradientBeam3Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam3) -> InitialTemperatureGradientBeam3Variable`
Create InitialTemperatureGradientBeam3Variable in this environment.

- `id` — The id of this InitialTemperatureBeam3. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the temperature.

### `apex.environment.createInitialTemperatureNodal(name: str, description: str, id: int, target: apex.EntityCollection, temperatureValue: float) -> InitialTemperatureNodal`
Create InitialTemperatureNodal in this environment.

- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `id` — The id of this InitialCondition. If omitted, system automatically assigns the largest load id + 1 to it.
- `target` — The target entities that the InitialTemperature is applied to.
- `temperatureValue` — The temperature value.

### `apex.environment.createInitialTemperatureNodalVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureNodal) -> InitialTemperatureNodalVariable`
Create InitialTemperatureNodalVariable in this environment.

- `id` — The id of this InitialCondition. If omitted, system automatically assigns the largest load id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The field to define the spatial distribution of the temperature.

### `apex.environment.createLoadAccelerationNodal(name: str, description: str, id: int, orientation: apex.IOrientation, scaleFactor: float, accelerationVectorX: float, accelerationVectorY: float, accelerationVectorZ: float, target: apex.EntityCollection, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadAccelerationNodal`
Create LoadAccelerationNodal in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Acceleration Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Acceleration Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `orientation` — the orientation used to define the direction of the acceleration vector. Currently it only accepts a coordinate system object.
- `scaleFactor` — the optional scale factor of the acceleration load. If omitted, the default value is 1.0.
- `accelerationVectorX` — the acceleration component value in X.
- `accelerationVectorY` — the acceleration component value in Y.
- `accelerationVectorZ` — the acceleration component value in Z.
- `target` — The target entities that the load is applied to.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadAccelerationNodalVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldAccelerationNodal) -> LoadAccelerationNodalVariable`
Create LoadAccelerationNodalVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Acceleration Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Acceleration Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadAccelerationSpatial(name: str, description: str, id: int, orientation: apex.IOrientation, accelerationVectorX: float, accelerationVectorY: float, accelerationVectorZ: float, componentDirection: apex.attribute.ComponentDirectionAcceleration, loadVariation: dict) -> LoadAccelerationSpatial`
Create LoadAccelerationSpatial in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Acceleration Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Acceleration Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `orientation` — The orientation in which the components of the direction vector is defined. Currently it only accepts a coordinate system object. If omitted, the basic coordinate system is used.
- `accelerationVectorX` — The X component of the acceleration vector.
- `accelerationVectorY` — The Y component of the acceleration vector.
- `accelerationVectorZ` — The Z component of the acceleration vector.
- `componentDirection` — The argument to define the component direction of the acceleration variation.
- `loadVariation` — The load variation along the component direction of the coordinate system. It is a dictionary with only two elements to represent the load variation along the axis: the value of the first element is a list of locations along the load direction, the value of the second element is a list of load scale factors associated with the locations. For example, loadVariation = {"locations": [0.0,1.0,2.0], "scale_factors": [100.56,110.78,135.89]} Note that there must be at least two values in the lists associated with locations and scale factors.

### `apex.environment.createLoadAreaFactor(name: str, description: str, id: int, target: apex.EntityCollection, scaleFactorX: float, scaleFactorY: float, scaleFactorZ: float, scaleFactorRx: float, scaleFactorRy: float, scaleFactorRz: float, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadAreaFactor`
Create LoadAreaFactor in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Load Scale Factor" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Load Scale Factor 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `scaleFactorX` — the load scale(area) factor in the translation X axis. Note that the scale factor in translation dof has the unit of force.
- `scaleFactorY` — the load scale(area) factor in the translation Y axis. Note that the scale factor in translation dof has the unit of force.
- `scaleFactorZ` — the load scale(area) factor in the translation Z axis. Note that the scale factor in translation dof has the unit of force.
- `scaleFactorRx` — the load scale(area) factor in the rotation X axis. Note that the scale factor in rotation dof has the unit of moment.
- `scaleFactorRy` — the load scale(area) factor in the rotation Y axis. Note that the scale factor in rotation dof has the unit of moment.
- `scaleFactorRz` — the load scale(area) factor in the rotation z axis. Note that the scale factor in rotation dof has the unit of moment.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadAreaFactorVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadAreaFactor) -> LoadAreaFactorVariable`

- `id` — The id of this LoadAreaFactorVariable
- `name` — The name of this LoadAreaFactorVariable
- `description` — The description of this LoadAreaFactorVariable
- `spatialTarget` — The spatialTarget of this LoadAreaFactorVariable

### `apex.environment.createLoadCombinationDynamic(name: str, description: str, id: int, overallScaleFactor: float, combinedLoads: dict) -> LoadCombinationDynamic`
Create a LoadCombinationDynamic object in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Load Combination" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Load Combination 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `overallScaleFactor` — The overall scale factor. If omitted, the default value is 1.0.
- `combinedLoads` — A dictionary to define the combined loads and scale factors. For each element, the key is the load name, the value is the scale factor associated with the load. For example: combinedLoads = {"Dynamic Load 1": 1.0, "Dynamic Load 2": 2.0, "Dynamic Load 3": 1.0 }

### `apex.environment.createLoadCombinationStatic(name: str, description: str, id: int, overallScaleFactor: float, combinedLoads: dict) -> LoadCombinationStatic`
Create a LoadCombinationStatic object in this environment.

- `name` — An optional name for the load combination that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Load Combination" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Load Combination 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `overallScaleFactor` — The overall scale factor. If omitted, the default value is 1.0.
- `combinedLoads` — A dictionary to define the combined loads and scale factors. For each element, the key is the load name, the value is the scale factor associated with the load. For example: combinedLoads = {"Force 1": 1.0, "Force 2": 2.0, "Moment 1": 1.0, "Moment 2": 2.0}

### `apex.environment.createLoadDeformationAxial(name: str, description: str, id: int, target: apex.EntityCollection, deformation: float) -> LoadDeformationAxial`
Create LoadDeformationAxial in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "1D Axial Deformation" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "1D Axial Deformation 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `deformation` — The deformation value.

### `apex.environment.createLoadDeformationAxialVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldDeformationAxial) -> LoadDeformationAxialVariable`
Create LoadDeformationAxialVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "1D Axial Deformation" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "1D Axial Deformation 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadDistributed(name: str, description: str, id: int, target: apex.EntityCollection, pressure: float, orientation: apex.IOrientation, directionX: float, directionY: float, directionZ: float) -> LoadDistributed`
Create LoadDistributed in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `pressure` — The traction pressure value.
- `orientation` — The optional orientation in which the components of the direction vector is defined. Currently it only accepts a coordinate system object. If omitted, the basic coordinate system is used.
- `directionX` — The X component of the direction vector.
- `directionY` — The Y component of the direction vector.
- `directionZ` — The Z component of the direction vector.

### `apex.environment.createLoadDistributedBeam2(name: str, description: str, id: int, target: apex.EntityCollection, loadType: apex.attribute.LoadTypeDistributedBeam2, scaleType: apex.attribute.ScaleTypeDistributedBeam2, distanceX1: float, loadFactorX1: float, distanceX2: float, loadFactorX2: float, inputType: apex.attribute.InputType) -> LoadDistributedBeam2`
Create LoadDistributedBeam2 in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Distributed Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Distributed Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `loadType` — The loadType of the beam distributed load applied to beam element with two nodes. apex.attribute.LoadTypeBeamDistributedLoad2.ForceX, the load is concentrated force in X direction of the basic coordinate system. apex.attribute.LoadTypeBeamDistributedLoad2.ForceY, the load is concentrated force in Y direction of the basic coordinate system. apex.attribute.LoadTypeBeamDistributedLoad2.ForceZ, the load is concentrated force in Z direction of the basic coordinate system. apex.attribute.LoadTypeBeamDistributedLoad2.MomentX, the load is moment in X direction of the basic coordinate system. apex.attribute.LoadTypeBeamDistributedLoad2.MomentY, the load is moment in Y direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentZ, the load is moment in Z direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceXE, the load is concentrated force in X direction of the element coordinate system. apex.attribute.LoadTypeBeam2.ForceYE, the load is concentrated force in Y direction of the element coordinate system. apex.attribute.LoadTypeBeam2.ForceZE, the load is concentrated force in Z direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentXE, the load is moment in X direction of the element coordinate system. apex.attribute.LoadTypeBeamDistributedLoad2.MomentYE, the load is moment in Y direction of the element coordinate system. apex.attribute.LoadTypeBeamDistributedLoad2.MomentZE, the load is moment in Z direction of the element coordinate system.
- `scaleType` — The scaleType of the load factors. If inputType is element uniform this argument should be omitted. apex.attribute.ScaleTypeBeamDistributedLoad.Length, the distance values are actual distances along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeamDistributedLoad.Fractional, the distance values are are ratios of the distance along the axis to the total length, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeamDistributedLoad.LengthProjected, the distance values are projected lengths along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeamDistributedLoad.FractionalProjected, the distance values are ratios of the actual distance to the length of the bar (CBAR entry), and if distance1 != distance 2, then the distributed load is specified in terms of the projected length of the bar.
- `distanceX1` — The distance along element axis from end A for load factor X1. If inputType is element uniform this argument can be omitted and always 0.0.
- `loadFactorX1` — The load factor at X1.
- `distanceX2` — The distance along element axis from end A for load factor X2. If inputType is element uniform this argument should be omitted.
- `loadFactorX2` — The optional load factor at X2 position. If the inputType is element uniform this argument should be omitted. If the input type is element variable, this argument can be omitted and it is the same with loadFactorX1 by default.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only loadfaxtorX1, target and loadType are necessary and it is automatically applied to loadFactorX2. The distanceX1 is 0.0, the distanceX2 is 1.0, the scaleType is "Fractional". If the inputType is element variable, both loadfaxtorX1 and loadfaxtorX2 can be defined. While distanceX1, distanceX2 and scaleType can be defined.

### `apex.environment.createLoadDistributedBeam2Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadDistributedBeam2) -> LoadDistributedBeam2Variable`
Create LoadDistributedBeam2Variable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Distributed Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Distributed Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadDistributedBeam3(name: str, description: str, id: int, target: apex.EntityCollection, coordinateSystem: apex.IOrientation, orientationType: apex.attribute.OrientationTypeDistributedBeam3, loadVectorX: float, loadVectorY: float, loadVectorZ: float, loadType: apex.attribute.LoadTypeDistributedBeam3, loadScaleFactor: float, magnitudeEndA: float, magnitudeEndB: float, magnitudeMidC: float, inputType: apex.attribute.InputType) -> LoadDistributedBeam3`
Create LoadDistributedBeam3 in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Distributed Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Distributed Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `coordinateSystem` — The user defined local coordinate system in which the load vector is defined.
- `orientationType` — The orientation type of the load. apex.attribute.OrientationTypeBeamDistributedLoad3.Basic, the load is defined in the basic coordinate system. apex.attribute.OrientationTypeBeamDistributedLoad3.Element, the load is defined in the element coordinate system. apex.attribute.OrientationTypeBeamDistributedLoad3.Local, the load is defined in the a local coordinate system on beam cross section. If you want to use a user defined coordinate system, then do not provide this argument and coordinateSystem should be defined.
- `loadVectorX` — The X component of the load vector.
- `loadVectorY` — The Y component of the load vector.
- `loadVectorZ` — The Z component of the load vector.
- `loadType` — The loadType of the beam distributed load applied to beam element with three nodes.
- `loadScaleFactor` — The optional load factor. If omitted, the default value is 1.0.
- `magnitudeEndA` — The load magnitude at end A. If the input type is element uniform, this argument should be omitted.
- `magnitudeEndB` — The load magnitude at end B. If the input type is element uniform, this argument should be omitted.
- `magnitudeMidC` — The load magnitude at the point C which is between end A and end B. If the input type is element uniform, this argument should be omitted.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, the magnitudes on end A, end B and end C are always 1.0 and load scale factor is 1.0. These four arguments should be omitted. If the inputType is element variable, all parameters can be defined.

### `apex.environment.createLoadDistributedBeam3Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadDistributedBeam3) -> LoadDistributedBeam3Variable`
Create LoadDistributedBeam3Variable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Distributed Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Distributed Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadDistributedVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadDistributed) -> LoadDistributedVariable`
Create LoadDistributedVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadDynamicAcoustic(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, phaseLead: apex.environment.Load, phaseLeadValue: float, powerTable: apex.chart.Table, powerValue: float, fluidDensity: float, fluidBulkModulus: float) -> LoadDynamicAcoustic`
Create LoadDynamicAcoustic.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Dynamic Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Dynamic Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `excitationLoads` — The excitation loads referenced by the dynamic load. Only the loads with same SID can be used.
- `timeDelay` — A time delay object to define the time delay in different degrees of freedom.
- `timeDelayValue` — A time delay value used for all frequencies.
- `phaseLead` — A phase lead object to define the phase lead in different degrees of freedom.
- `phaseLeadValue` — A phase lead value used for all frequencies.
- `powerTable` — A table to define the power value versus frequency.
- `powerValue` — The powerValue.
- `fluidDensity` — The fluidDensity.
- `fluidBulkModulus` — The fluidBulkModulus.

### `apex.environment.createLoadDynamicFrequency1(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, phaseLead: apex.environment.Load, phaseLeadValue: float, realPartTable: apex.chart.Table, realPartValue: float, imagTable: apex.chart.Table, imagValue: float, loadType: apex.attribute.DynamicLoadType) -> LoadDynamicFrequency1`
Create LoadDynamicFrequency1 in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Dynamic Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Dynamic Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `excitationLoads` — The excitation loads referenced by the dynamic load. Only the loads with same SID can be used.
- `timeDelay` — A time delay object to define the time delay in different degrees of freedom.
- `timeDelayValue` — A time delay value used for all frequencies.
- `phaseLead` — A phase lead object to define the phase lead in different degrees of freedom.
- `phaseLeadValue` — A phase lead value used for all frequencies.
- `realPartTable` — A table to define the real part value versus frequency.
- `realPartValue` — The constant value as the real part used for all frequencies
- `imagTable` — A table to define the imaginary part value versus frequency.
- `imagValue` — An imaginary value used for all frequencies.
- `loadType` — The type to define the dynamic excitation type. If omitted, the default type is "apex.attribute.DynamicLoadType.AppliedLoad".

### `apex.environment.createLoadDynamicFrequency2(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, phaseLead: apex.environment.Load, phaseLeadValue: float, magnitudeTable: apex.chart.Table, magnitude: float, phaseAngleTable: apex.chart.Table, phaseAngle: float, loadType: apex.attribute.DynamicLoadType) -> LoadDynamicFrequency2`
Create LoadDynamicFrequency2 in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Dynamic Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Dynamic Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `excitationLoads` — The excitation loads referenced by the dynamic load. Only the loads with same SID can be used.
- `timeDelay` — A time delay object to define the time delay in different degrees of freedom.
- `timeDelayValue` — A time delay value used for all degrees of freedom in the excitation loads.
- `phaseLead` — A phase lead object to define the phase lead in different degrees of freedom.
- `phaseLeadValue` — A phase lead value used for all degrees of freedom in the excitation loads.
- `magnitudeTable` — A table to define the magnitude value versus frequency.
- `magnitude` — A magnitude value used for all frequencies.
- `phaseAngleTable` — A table to define the phase angle value versus frequency.
- `phaseAngle` — An phase angle value used for all frequencies.
- `loadType` — The type to define the dynamic excitation type. If omitted, the default type is "apex.attribute.DynamicLoadType.AppliedLoad".

### `apex.environment.createLoadDynamicTimeAnalytical(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, timeConstant1: float, timeConstant2: float, frequency: float, phaseAngle: float, exponentialCoefficient: float, growthCoefficient: float, initialDisplacement: float, initialVelocity: float, loadType: apex.attribute.DynamicLoadType) -> LoadDynamicTimeAnalytical`
Create LoadDynamicTimeAnalytical in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Dynamic Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Dynamic Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `excitationLoads` — The excitation loads referenced by the dynamic load. Only the loads with same SID can be used.
- `timeDelay` — A time delay object to define the time delay in different degrees of freedom.
- `timeDelayValue` — A time delay value used for all frequencies.
- `timeConstant1` — The time constant 1, should be >=0.
- `timeConstant2` — The time constant 2. It must be greater than timeConstan1.
- `frequency` — An optional frequency value in the unit of cycles per time. If omitted, it is 0.0 by default.
- `phaseAngle` — An optional phase angle value in degrees. If omitted, it is 0.0 by default.
- `exponentialCoefficient` — An optional exponential coefficient value. If omitted, it is 0.0 by default.
- `growthCoefficient` — An optional growth coefficient value. If omitted, it is 0.0 by default.
- `initialDisplacement` — The initial displacement. If omitted, it is 0.0 by default.
- `initialVelocity` — The initial velocity. If omitted, it is 0.0 by default.
- `loadType` — The type to define the dynamic excitation type. If omitted, the default type is "apex.attribute.DynamicLoadType.AppliedLoad".

### `apex.environment.createLoadDynamicTimeTabular(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, functionTable: apex.chart.Table, functionValue: float, initialDisplacement: float, initialVelocity: float, loadType: apex.attribute.DynamicLoadType) -> LoadDynamicTimeTabular`
Create LoadDynamicTimeTabular in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Dynamic Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Dynamic Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `excitationLoads` — The excitation loads referenced by the dynamic load. Only the loads with same SID can be used.
- `timeDelay` — A time delay object to define the time delay in different degrees of freedom.
- `timeDelayValue` — A time delay value used for all frequencies.
- `functionTable` — A table to define the function value versus time.
- `functionValue` — A function value used for all times.
- `initialDisplacement` — The initial displacement. If omitted, it is 0.0 by default.
- `initialVelocity` — The initial velocity. If omitted, it is 0.0 by default.
- `loadType` — The type to define the dynamic excitation type. If omitted, the default type is "apex.attribute.DynamicLoadType.AppliedLoad".

### `apex.environment.createLoadEnforcedMotionRelative(name: str, description: str, id: int, target: apex.EntityCollection, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, orientation: apex.IOrientation, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadEnforcedMotionRelative`
Create LoadEnforcedMotionRelative in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Motion" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Motion 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `translationX` — The optional float value to define the motion in X direction.
- `translationY` — The optional float value to define the motion in Y direction.
- `translationZ` — The optional float value to define the motion in Z direction.
- `rotationX` — The optional float value to define the rotation about X axis.
- `rotationY` — The optional float value to define the rotation about Y axis.
- `rotationZ` — The optional float value to define the rotation about Z axis.
- `orientation` — The orientation of this LoadEnforcedMotionRelative
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadEnforcedMotionRelativeVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldEnforcedMotion) -> LoadEnforcedMotionRelativeVariable`
Create LoadEnforcedMotionRelativeVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Load Scale Factor" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Load Scale Factor 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadEnforcedMotionTotal(name: str, description: str, id: int, target: apex.EntityCollection, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, orientation: apex.IOrientation, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadEnforcedMotionTotal`
Create LoadEnforcedMotionTotal in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Motion" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Motion 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `translationX` — The optional float value to define the motion in X direction.
- `translationY` — The optional float value to define the motion in Y direction.
- `translationZ` — The optional float value to define the motion in Z direction.
- `rotationX` — The optional float value to define the rotation about X direction.
- `rotationY` — The optional float value to define the rotation about Y direction.
- `rotationZ` — The optional float value to define the rotation about Z direction.
- `orientation` — The orientation of this LoadEnforcedMotionTotal
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadEnforcedMotionTotalVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldEnforcedMotion) -> LoadEnforcedMotionTotalVariable`
Create LoadEnforcedMotionTotalVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Load Scale Factor" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Load Scale Factor 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadForceComponent(name: str, description: str, id: int, target: apex.EntityCollection, orientation: apex.IOrientation, scaleFactor: float, forceX: float, forceY: float, forceZ: float, applicationMethod: apex.attribute.ApplicationMethod, attachmentRegion: apex.EntityCollection, attachmentDistributionType: apex.attribute.DistributionType) -> LoadForceComponent`
Create a LoadForceComponent in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `orientation` — An optional orientation, currently it must be a coordinate system in which the components are defined. If omitted, the components are defined in the basic coordinate system.
- `scaleFactor` — An optional scale factor of the force. If omitted, the default value is 1.0.
- `forceX` — the force value in X component.
- `forceY` — the force value in Y component.
- `forceZ` — the force value in Z component.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.
- `attachmentDistributionType` — The DistributionType used in the remote method.

### `apex.environment.createLoadForceComponentVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldForceComponent) -> LoadForceComponentVariable`
Create a LoadForceComponentVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadForceFollowerNormal(name: str, description: str, id: int, target: apex.EntityCollection, forceMagnitude: float, point1: apex.Entity, point2: apex.Entity, point3: apex.Entity, point4: apex.Entity, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadForceFollowerNormal`
Create LoadForceFollowerNormal in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `forceMagnitude` — the force magnitude.
- `point1` — the starting point of the first vector. It should be a vertex or a node.
- `point2` — the end point of the first vector. It should be a vertex or a node.
- `point3` — The starting point of the second vector. It should be a vertex or a node.
- `point4` — The end point of the second vector. It should be a vertex or a node.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadForceFollowerNormalVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldForceFollowerNormal) -> LoadForceFollowerNormalVariable`
Create LoadForceFollowerNormalVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadForceFollowerVector(name: str, description: str, id: int, target: apex.EntityCollection, forceMagnitude: float, point1: apex.Entity, point2: apex.Entity, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadForceFollowerVector`
Create LoadForceFollowerVector in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `forceMagnitude` — the force magnitude.
- `point1` — the starting point of the load vector. It should be a vertex or a node.
- `point2` — the end point of the load vector. It should be a vertex or a node.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadForceFollowerVectorVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldForceFollowerVector) -> LoadForceFollowerVectorVariable`
Create LoadForceFollowerVectorVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadForceRotational(name: str, description: str, id: int, rotationCenter: apex.Entity, orientation: apex.IOrientation, scaleFactorVel: float, rotationVectorX: float, rotationVectorY: float, rotationVectorZ: float, loadMethod: apex.attribute.LoadMethodRotational, scaleFactorAcc: float, coordinateSystemDefinition: apex.attribute.CoordinateSystemDefinition) -> LoadForceRotational`
Create LoadForceRotational in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Rotational Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Rotational Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `rotationCenter` — The center of rotation. If omitted, the origin of the basic coordinate system is used.
- `orientation` — The orientation in which the components of the rotation vector are defined. If omitted, the components are defined in the basic coordinate system.
- `scaleFactorVel` — The scale factor for angular velocity in revolutions per unit time.
- `rotationVectorX` — The X component of the rotation vector.
- `rotationVectorY` — The Y component of the rotation vector.
- `rotationVectorZ` — TheZ component of the rotation vector.
- `loadMethod` — The load method of the rotational force. If omitted, the default method is "apex.attribute.LoadMethodRotational.Centrifugal".
- `scaleFactorAcc` — The optional scale factor. If omitted, the scale factor is 0.0 by default.
- `coordinateSystemDefinition` — the optional coordinate system definition of this RotationalForce: apex.attribute.CoordinateSystemDefinition.SuperElement, the coordinate system is defined in the super-element and will be translated, rotated with the super-element. apex.attribute.CoordinateSystemDefinition.Residual, the coordinate system is defined in the residual structure and stationary with the basic coordinate system. If omitted, the default value is "apex.attribute.CoordinateSystemDefinition.SuperElement".

### `apex.environment.createLoadLug(lugProperty: LoadLugProperty, target: apex.EntityCollection, name: str, description: str) -> apex.environment.LoadLug`
Create a LoadLug in this environment.

- `lugProperty` — The property of the LoadLug.
- `target` — The target entities that the LoadLug is applied to. Apex only supports perfect circle edges or cylinder faces that span angle is less than 180 degree in 2021.2 release.
- `name` — An optional name for the LoadLug that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'Lug Load ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Lug Load 1'.
- `description` — An optional description for the LoadLug that will be created. If omitted, the description will be left blank.

Returns: the created LoadLug

### `apex.environment.createLoadLugPropertyStatic(loadMagnitude: float, distribution: apex.attribute.Distribution, distributionOrientation: apex.attribute.DistributionOrientation = apex.attribute.DistributionOrientation.Undefined, id: int) -> LoadLugPropertyStatic`
Create LoadLugPropertyStatic.

- `loadMagnitude` — The load magnitude of the LoadLugPropertyStatic.
- `distribution` — The distribution type of the LoadLugPropertyStatic. Apex supports cosine in the current release.
- `distributionOrientation` — Optional - the distributionOrientation of the LoadLug. Default is apex.attributes.DistributionOrientation.Normal if omitted.
- `id` — Optional - the id of the LoadLugPropertyStatic. If omitted, system will assign the smallest load id to it.

Returns: the created LoadLugPropertyStatic

### `apex.environment.createLoadMomentComponent(name: str, description: str, id: int, target: apex.EntityCollection, orientation: apex.IOrientation, scaleFactor: float, momentX: float, momentY: float, momentZ: float, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadMomentComponent`
Create LoadMomentComponent in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Moment" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Moment 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `orientation` — An optional orientation, currently it must be a coordinate system in which the components are defined. If omitted, the components are defined in the basic coordinate system.
- `scaleFactor` — the optional scale factor of the load.If omitted, the default value is 1.0.
- `momentX` — the moment value in X component.
- `momentY` — the moment value in Y component.
- `momentZ` — the moment value in Z component.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadMomentComponentVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldMomentComponent) -> LoadMomentComponentVariable`
Create LoadMomentComponentVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Moment" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Moment 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadMomentFollowerNormal(name: str, description: str, id: int, target: apex.EntityCollection, momentMagnitude: float, point1: apex.Entity, point2: apex.Entity, point3: apex.Entity, point4: apex.Entity, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadMomentFollowerNormal`
Create LoadMomentFollowerNormal in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Moment" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Moment 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `momentMagnitude` — the moment magnitude.
- `point1` — the starting point of the first vector. It should be a vertex or a node.
- `point2` — the end point of the first vector. It should be a vertex or a node.
- `point3` — The starting point of the second vector. It should be a vertex or a node.
- `point4` — The end point of the second vector. It should be a vertex or a node.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadMomentFollowerNormalVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldMomentFollowerNormal) -> LoadMomentFollowerNormalVariable`
Create LoadMomentFollowerNormalVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Force" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Force 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadMomentFollowerVector(name: str, description: str, id: int, target: apex.EntityCollection, momentMagnitude: float, point1: apex.Entity, point2: apex.Entity, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> LoadMomentFollowerVector`
Create LoadMomentFollowerVector in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Moment" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Moment 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `momentMagnitude` — the moment magnitude.
- `point1` — the starting point of the load vector. It should be a vertex or a node.
- `point2` — the end point of the load vector. It should be a vertex or a node.
- `applicationMethod` — The applicationMethod of the load.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote load is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createLoadMomentFollowerVectorVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldMomentFollowerVector) -> LoadMomentFollowerVectorVariable`
Create LoadMomentFollowerVectorVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Moment" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Moment 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadPhaseLead(name: str, description: str, id: int, target: apex.EntityCollection, phaseLeadX: float, phaseLeadY: float, phaseLeadZ: float, phaseLeadRx: float, phaseLeadRy: float, phaseLeadRz: float) -> LoadPhaseLead`
Create LoadPhaseLead in this environment.

- `name` — The name of this LoadPhaseLead
- `description` — The description of this LoadPhaseLead
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest time delay ID +1 to it.
- `target` — The target entities that the phase lead is applied to.
- `phaseLeadX` — The phase lead value in the X component.
- `phaseLeadY` — The phase lead value in the Y component.
- `phaseLeadZ` — The phase lead value in the Z component.
- `phaseLeadRx` — The phase lead value in the rotation X component.
- `phaseLeadRy` — the phase lead value in the rotation Y component.
- `phaseLeadRz` — The phase lead value in the rotation Z component.

### `apex.environment.createLoadPhaseLeadVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPhaseLead) -> LoadPhaseLeadVariable`
Create LoadPhaseLeadVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest ID +1 to it.
- `name` — The name of this LoadPhaseLeadVariable
- `description` — The description of this LoadPhaseLeadVariable
- `spatialTarget` — The field to define the phase lead for all degrees of freedom.

### `apex.environment.createLoadPressure(name: str = "", description: str = "", target: apex.EntityCollection = None, loadPressureProperty: apex.environment.LoadPressureProperty = None) -> LoadPressure`
Create a new LoadPressure in this environment, it returns a LoadPressure. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createPressureConstant(), createPressureVariable().

- `name` — the name of new pressureLoad, the default = "" (auto-named).
- `description` — the description of new pressure load, the default="".
- `target` — it defines the entities the pressure will be assigned to.
- `loadPressureProperty` — the property used to define one load pressure, it contains ID and pressureValue(s).

### `apex.environment.createLoadPressure2D(name: str, description: str, id: int, pressureMagnitude: float, target: apex.EntityCollection) -> LoadPressure2D`
Create LoadPressured2D in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `pressureMagnitude` — the pressure magnitude.
- `target` — The target that the load is applied to.

### `apex.environment.createLoadPressure2DVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPressure2D) -> LoadPressure2DVariable`
Create LoadPressured2DVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadPressureArea(name: str, description: str, id: int, pressureMagnitude: float, vertex1: apex.Entity, vertex2: apex.Entity, vertex3: apex.Entity, vertex4: apex.Entity) -> LoadPressureArea`
Create LoadPressuredArea in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `pressureMagnitude` — the pressure magnitude.
- `vertex1` — The first vertex of the loading face.
- `vertex2` — The second vertex of the loading face.
- `vertex3` — The third vertex of the loading face.
- `vertex4` — The fourth vertex of the loading face. If omitted, the load is applied to a triangular face.

### `apex.environment.createLoadPressureAreaVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPressureArea) -> LoadPressureAreaVariable`
Create LoadPressuredAreaVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the load.

### `apex.environment.createLoadTemperature(name: str, target: apex.EntityCollection, temperatureProperty: LoadTemperatureProperty, description: str = "") -> LoadTemperature`
Creates a LoadTemperature in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadTemperatureNodal(), createLoadTemperatureNodalVariable().

- `name` — An optional name for the load temperature that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Temperature 9".
- `target` — The target entities that the LoadTemperature is applied to. The supported target types are: Solid, cell, surface, curve, face, edge, vertex, 3D mesh, 2D mesh, 1D mesh, node.
- `temperatureProperty` — The temperature property of the LoadTemperature.
- `description` — An optional description for the load temperature that will be created. If omitted the description will be left blank.

Returns: the created LoadTemperature

### `apex.environment.createLoadTemperatureDefault(name: str, description: str, id: int, defaultTemperature: float) -> LoadTemperatureDefault`
Create LoadTemperatureDefault in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Temperature 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `defaultTemperature` — The default temperature value.

### `apex.environment.createLoadTemperatureGradient2D(name: str, description: str, id: int, target: apex.EntityCollection, temperatureReferencePlane: float, thermalGradient: float, temperatureLowerSurface: float, temperatureUpperSurface: float) -> LoadTemperatureGradient2D`
Create LoadTemperatureGradient2D in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Temperature 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `temperatureReferencePlane` — The temperature applied on the element reference plane.
- `thermalGradient` — The effective linear thermal gradient. If omitted, it is 0.0 by default.
- `temperatureLowerSurface` — The temperature for stress calculation at points on the lower surface.
- `temperatureUpperSurface` — The temperature for stress calculation at points on the upper surface.

### `apex.environment.createLoadTemperatureGradient2DHeat(name: str, description: str, id: int, target: apex.EntityCollection, temperatureTop: float, temperatureBottom: float, temperatureMid: float) -> LoadTemperatureGradient2DHeat`
Create LoadTemperatureGradient2DHeat in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Temperature 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `temperatureTop` — the optional float value to define the temperature value at top location through the thickness.
- `temperatureBottom` — the optional float value to define the temperature value at bottom location through the thickness.
- `temperatureMid` — the optional float value to define the temperature value at mid location through the thickness.

### `apex.environment.createLoadTemperatureGradient2DHeatVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2DHeat) -> LoadTemperatureGradient2DHeatVariable`
Create LoadTemperatureGradient2DHeatVariable in this environment.

- `id` — The id of this LoadTemperatureGradient2DHeatVariable. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The spatial field to define the spatial distribution of the temperature.

### `apex.environment.createLoadTemperatureGradient2DVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2D) -> LoadTemperatureGradient2DVariable`
Create LoadTemperatureGradient2DVariable in this environment.

- `id` — The id of this LoadTemperatureGradient2DVariable. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The spatial field to define the spatial distribution of the temperature.

### `apex.environment.createLoadTemperatureGradientBeam2(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, thermalGradient1A: float, thermalGradient1B: float, thermalGradient2A: float, thermalGradient2B: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, inputType: apex.attribute.InputType) -> LoadTemperatureGradientBeam2`
Create LoadTemperatureGradientBeam2 in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Temperature 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `temperatureEndA` — The temperature value at end A on neutral axis. If the inputType is element uniform, this temperature value is assigned to end B as well.
- `temperatureEndB` — The temperature value at end B on neutral axis. If the inputType is element variable, this temperature value is ignored and derived from temperatureEndA.
- `thermalGradient1A` — The effective thermal gradient in direction 1 at end A. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradient1B as well.
- `thermalGradient1B` — The effective thermal gradient in direction 1 at end B. If the inputType is element variable, this thermal gradient is ignored and derived from thermalGradient1A.
- `thermalGradient2A` — The effective thermal gradient in direction 2 at end A. If the inputType is element uniform, this thermal gradient value is assigned to thermalGradient2B as well.
- `thermalGradient2B` — The effective thermal gradient in direction 2 at end B. If the inputType is element uniform, this thermal gradient is ignored and derived from thermalGradient2A.
- `temperaturePointCendA` — The temperature value on point C at end A, used for stress recovery.
- `temperaturePointDendA` — The temperature value on point D at end A, used for stress recovery.
- `temperaturePointEendA` — The temperature value on point E at end A, used for stress recovery.
- `temperaturePointFendA` — The temperature value on point F at end A, used for stress recovery.
- `temperaturePointCendB` — The temperature value on point C at end B, used for stress recovery.
- `temperaturePointDendB` — The temperature value on point D at end B, used for stress recovery.
- `temperaturePointEendB` — The temperature value on point E at end B, used for stress recovery.
- `temperaturePointFendB` — The temperature value on point F at end B, used for stress recovery.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.

### `apex.environment.createLoadTemperatureGradientBeam2Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam2) -> LoadTemperatureGradientBeam2Variable`
Create LoadTemperatureGradientBeam2Variable in this environment.

- `id` — The id of this InitialTemperatureBeam2. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The spatial field to define the spatial distribution of the temperature.

### `apex.environment.createLoadTemperatureGradientBeam3(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, temperatureMidC: float, thermalGradientYA: float, thermalGradientZA: float, thermalGradientYB: float, thermalGradientZB: float, thermalGradientYC: float, thermalGradientZC: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, temperaturePointCmidC: float, temperaturePointDmidC: float, temperaturePointEmidC: float, temperaturePointFmidC: float, inputType: apex.attribute.InputType) -> LoadTemperatureGradientBeam3`
Create LoadTemperaturGradientBeam3 in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Temperature 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `temperatureEndA` — The temperature value at end A on neutral axis. If the inputType is element uniform, this temperature value is automatically assigned to end B and mid C.
- `temperatureEndB` — The temperature value at end B on the neutral axis. If the inputType is element uniform, this temperature value is ignored and derived from end A.
- `temperatureMidC` — the temperature value at a point C between end A and end B. If the inputType is element uniform, this temperature value is ignored and derived from end A.
- `thermalGradientYA` — The effective thermal gradient in direction y at end A. If the inputType is element uniform, this thermal gradient is automatically assigned to YB and YC.
- `thermalGradientZA` — The effective linear thermal gradient in local direction z on end A. If the inputType is element uniform, this thermal gradient is automatically assigned to ZB and ZC.
- `thermalGradientYB` — The effective linear thermal gradient in local direction Y on end B. If the inputType is element uniform, this thermal gradient is ignored and derived from YA.
- `thermalGradientZB` — The effective linear thermal gradient in local direction Z on end B. If the inputType is element uniform, this thermal gradient is ignored and derived from ZA.
- `thermalGradientYC` — The effective linear thermal gradient in direction y on mid C. If the inputType is element uniform, this thermal gradient is ignored and derived from YA.
- `thermalGradientZC` — The effective linear thermal gradient in direction z on mid C. If the inputType is element uniform, this thermal gradient is ignored and derived from ZA.
- `temperaturePointCendA` — The temperature value on point C at end A, used for stress recovery.
- `temperaturePointDendA` — The temperature value on point D at end A, used for stress recovery.
- `temperaturePointEendA` — The temperature value on point E at end A, used for stress recovery.
- `temperaturePointFendA` — The temperature value on point F at end A, used for stress recovery.
- `temperaturePointCendB` — The temperature value on point C at end B, used for stress recovery.
- `temperaturePointDendB` — The temperature value on point D at end B, used for stress recovery.
- `temperaturePointEendB` — The temperature value on point E at end B, used for stress recovery.
- `temperaturePointFendB` — The temperature value on point F at end B, used for stress recovery.
- `temperaturePointCmidC` — the temperature value on point C at mid C, used for stress recovery.
- `temperaturePointDmidC` — The temperature value on point D at mid C, used for stress recovery.
- `temperaturePointEmidC` — The temperature value on point E at mid C, used for stress recovery.
- `temperaturePointFmidC` — The temperature value on point F at mid C, used for stress recovery.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B and mid C. If the inputType is element variable, all temperature values and thermal gradients can be defined.

### `apex.environment.createLoadTemperatureGradientBeam3Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam3) -> LoadTemperatureGradientBeam3Variable`
Create LoadTemperatureGradientBeam3Variable in this environment.

- `id` — The id of this InitialTemperatureBeam3. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The spatial field to define the spatial distribution of the temperature.

### `apex.environment.createLoadTemperatureNodal(name: str, description: str, id: int, target: apex.EntityCollection, temperatureValue: float) -> LoadTemperatureNodal`
Create LoadTemperatureNodal in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Temperature 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `temperatureValue` — The temperature value.

### `apex.environment.createLoadTemperatureNodalVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureNodal) -> LoadTemperatureNodalVariable`
Create LoadTemperatureNodalVariable in this environment.

- `id` — The id of this LoadTemperatureNodalVariable. If omitted, system automatically assigns the largest id + 1 to it.
- `name` — An optional name for the object that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model.
- `description` — An optional description. If omitted the description will be left blank.
- `spatialTarget` — The spatial field to define the spatial distribution of the temperature.

### `apex.environment.createLoadTimeDelay(name: str, description: str, id: int, target: apex.EntityCollection, timeDelayX: float, timeDelayY: float, timeDelayZ: float, timeDelayRx: float, timeDelayRy: float, timeDelayRz: float) -> LoadTimeDelay`
Create LoadTimeDelay in this environment.

- `name` — The name of this LoadTimeDelay
- `description` — The description of this LoadTimeDelay
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest time delay ID +1 to it.
- `target` — The target entities that the time delay is applied to.
- `timeDelayX` — The time delay value in the X component.
- `timeDelayY` — The time delay value in the Y component.
- `timeDelayZ` — The time delay value in the Z component.
- `timeDelayRx` — The time delay value in the rotation X component.
- `timeDelayRy` — the time delay value in the rotation Y component.
- `timeDelayRz` — The time delay value in the rotation Z component.

### `apex.environment.createLoadTimeDelayVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTimeDelay) -> LoadTimeDelayVariable`
Create LoadTimeDelayVariable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest time delay ID +1 to it.
- `name` — The name of this LoadTimeDelayVariable
- `description` — The description of this LoadTimeDelayVariable
- `spatialTarget` — The field to define the time delays for all degrees of freedom.

### `apex.environment.createLoadTotal(name: str, description: str, id: int, orientation: apex.IOrientation, target: apex.EntityCollection, forceX: float, forceY: float, forceZ: float) -> LoadTotal`
Create LoadTotal in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `orientation` — an optional CoordinateSystem used to define the orientation of the force components. If omitted, the components are defined in the basic coordinate system.
- `target` — an EntityCollection identifying the entities that the total load will be applied to. Loads may be assigned to Faces, 2D Mesh Bodies, 2D Elements and Element Faces. Loads assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `forceX` — The total force value in X component. It is a Force quantity and must be defined using the units of Force from the active script unit system.
- `forceY` — The total force value in Y component. It is a Force quantity and must be defined using the units of Force from the active script unit system.
- `forceZ` — The total force value in Z component. It is a Force quantity and must be defined using the units of Force from the active script unit system.

### `apex.environment.createLoadTraction(tractionProperty: LoadTractionProperty, target: apex.EntityCollection, name: str = "", description: str = "", orientation: apex.construct.Orientation = None) -> LoadTraction`
Create a TractionLoad in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadDistributed(), createLoadTotal().

- `tractionProperty` — The property of the LoadTraction.
- `target` — The target entities that the LoadTraction is applied to. The supported target types are face, 2D mesh, 2D element and element face in 2021.2 release.
- `name` — An optional name for the LoadTraction that will be created. If omitted the system will assign a default name formed by concatenating the prefix 'Traction Load ' with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Traction Load 12'.
- `description` — An optional description for the LoadTraction that will be created. If omitted, the description will be left blank.
- `orientation` — Optional - the orientation of the LoadTraction. If omitted, the LoadTraction is oriented in the default coordinate system.

Returns: the created LoadTraction

### `apex.environment.createLoadTractionPropertyStaticConstant(pressureX: float = NAN, pressureY: float = NAN, pressureZ: float = NAN, id: int = 0) -> LoadTractionPropertyStaticConstant`
Creates a LoadTractionPropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadDistributed(), createLoadTotal().

- `pressureX` — Optional - the pressure value in X component.
- `pressureY` — Optional - the pressure value in Y component.
- `pressureZ` — Optional - the pressure value in Z component.
- `id` — Optional - the id of the LoadTractionPropertyStaticConstant. If omitted, system will assign the smallest load id to it.

Returns: the created LoadTractionPropertyStaticConstant

### `apex.environment.createLoadTractionPropertyStaticTotal(forceX: float = NAN, forceY: float = NAN, forceZ: float = NAN, id: int = 0) -> LoadTractionPropertyStaticTotal`
Creates a LoadTractionPropertyStaticTotal. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadDistributed(), createLoadTotal().

- `forceX` — Optional - the force value in X component.
- `forceY` — Optional - the force value in Y component.
- `forceZ` — Optional - the force value in Z component.
- `id` — Optional - the id of the LoadTractionPropertyStaticTotal. If omitted, system will assign the smallest load id to it.

Returns: the created LoadTractionPropertyStaticTotal

### `apex.environment.createPreloadBolt(name: str = "", description: str = "", target: apex.EntityCollection = None) -> apex.environment.PreloadBolt`
Create a Bolt preload object in this environment.

- `name` — Optional-name of the bolt preload.
- `description` — Optional-description of the bolt preload.
- `target` — The target entities that the PreloadBolt is applied to.The supported target is 3D bolt object.

### `apex.environment.createPreloadBoltPropertyStatic(preloadType: apex.environment.BoltPreloadType = apex.environment.BoltPreloadType.Force, force: float = NAN, overclosure: float = NAN) -> apex.environment.PreloadBoltPropertyStatic`
Create static bolt preload property.

- `preloadType` — Bolt preload definition type.
- `force` — Force of bolt preload, it is only available when preloadType = Force.
- `overclosure` — Overclosure of bolt preload, it is only available when preloadType = Overclosure object.

### `apex.environment.createPressureConstant(name: str, description: str, id: int, target: apex.EntityCollection, pressure: float) -> Pressure`
Create Pressure in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Pressure" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Pressure 5".
- `description` — An optional description. If omitted, the description is blank.
- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest load ID +1 to it.
- `target` — The target that the load is applied to.
- `pressure` — The pressure value.

### `apex.environment.createPressurePropertyStaticConstant(id: int = 0, pressureValue: float = 1.0) -> LoadPressurePropertyStaticConstant`
Create a LoadPressurePropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createPressureConstant().

- `id` — an optional load ID defined in PressurePropertyStaticConstant and assigned to the associated LoadPressure. If omitted, the system will assign a default load ID which is the smallest and unique among all existing loads IDs..
- `pressureValue` — value of static constant pressure property.

### `apex.environment.createPressurePropertyStaticVariable(id: int, pressureValues: {str:{dict}}) -> LoadPressurePropertyStaticVariable`
Create a LoadPressurePropertyStaticVariable. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createPressureVariable().

- `id` — an optional load ID defined in PressurePropertyStaticVariable and assigned to the associated LoadPressure. If omitted, the system will assign a default load ID which is the smallest and unique among all existing loads IDs.
- `pressureValues` — returns a nested Dictionary containing the pathNames of the MeshBody on which the pressure is applied and the element IDs/element face IDs/node IDs and associated pressure values. The key of the top level dictionary is a string type that represents the pathName of a MeshBody and the associated value is a secondary dictionary containing the individual elements/faces/pressures. Each MeshBody that has one or more elements referenced by the variable pressure load will be included in the top level dictionary. For example, is a pressure is applied to elements on two different MeshBodies the top level dictionary will include two items - {Model_1/Part 1/Mesh 1?: {dict1}, "Model_1/Part 2/Mesh 2": {dict2}} The secondary dictionary contains the information about which elements/element faces are included in the variable pressure load and the pressure values applied to each. A variable pressure load may have a single constant value per 2D element or 3D element face or may have different values defined at each corner node of 2D elements or 3D element faces. The type of distribution is identified in the secondary dictionary by the identifier_type?key which is a string type. The associated value is a string type that must be one of the following values, "ELEMENT_ID", "ELEMENT_ID_FACE_INDEX", "ELEMENT_ID_FACE_NODE_ID If identifier_type is ELEMENT_ID, the pressure field is defined using a single pressure value per 2D element and the secondary dictionary items with element_ids? and pressures? keys identify the 2D elements and pressure values. The value associated with the element_ids key is a List of integers, each integer identifying the element id. The value associated with the pressures key is a List of floats, each integer identifying the single pressure value associated with the corresponding element. The element_ids and pressure lists must be of equal length with the pressure value indices aligned with the element ids indices. If identifier_type is ELEMENT_ID_FACE_INDEX, the remainder of the pressure field is defined using a single pressure value per 3D element face and the secondary dictionary items with element_ids?, face_identifiers? and pressures? identify the 3D element faces and pressure values. The value associated with the element_ids key is a List of integers, each integer identifying the id of a 3D element. The value associated with the face_identifiers? key is a List of integers, each integer identifying a face on the associated 3D element. (Face indices per 3D element type are documented elsewhere). The value associated with the pressures key is a List of floats, each integer identifying the single pressure value associated with the corresponding element face. The element_ids, identifiers and pressures lists must be of equal length with the pressure value indices aligned with the element ids/Element face indices. If identifier_type is ELEMENT_ID_FACE_NODE_ID, the remainder of the pressure field is defined using multiple pressure values per 2D element or 3D element face ? one pressure value for each corner node of the 2D element or 3D element face and the secondary dictionary items with element_ids?, face_identifiers? and pressures? identify the 2D Elements or 3D element faces and pressure values. The value associated with the element_ids key is a List of integers, each integer identifying the id of a 2D or 3D element. The value associated with the face_identifiers? key is a List of Lists of integers. Each internal integer List identifies the corner nodes of the 2D element or 3D element face. There must be the same number of internal integer lists as there are IDs in element_ids, The value associated with the pressures key is a List of Lists of floats, Each internal list identifies the pressure values at the corner nodes of the associated 2D element or 3D element face. There must be the same number of internal float lists as there are IDs in element_ids and the pressure values must be aligned with the element corner node indices. Example : Pressure field defined on 3 2D elements with a single pressure per element { identifier_type? : ELEMENT_ID?, element_ids? : [1, 2, 6], pressures? : [15.0, 21.6, 35.9] } Example : Pressure field defined on 3 3D elements with a single pressure per element { identifier_type? : ELEMENT_ID_FACE_INDEX?, element_ids? : [11, 23, 915], face_identifiers? : [0, 3, 2], pressures? : [15.0, 21.6, 35.9] } Example : Pressure field defined on 3 elements with different pressures for one 2D element or 3D element face { identifier_type? : ELEMENT_ID_FACE_NODE_ID?, element_ids? : [11, 23, 915], face_identifiers? : [[15, 16, 18, 21], [17, 5, 89, 6], [99, 89, 70, 65]], pressures? : [[15.0, 17.6, 18.9, 17.2], [14.0, 17.2, 17.2], [13.2, 14.6, 15.9, 11.2]] }

### `apex.environment.createPressureVariable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPressure) -> PressureVariable`

- `id` — The id of this PressureVariable
- `name` — The name of this PressureVariable
- `description` — The description of this PressureVariable
- `spatialTarget` — The spatialTarget of this PressureVariable

### `apex.environment.createSupportFreeBody(name: str, description: str, target: apex.EntityCollection, constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool, orientation: apex.IOrientation, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> SupportFreeBody`
Create SupportFreeBody in this environment.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `target` — An entityCollection that is applied to the ConstraintDisplacement.
- `constrainTranslationX` — An optional argument to constrain the translation X. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainTranslationY` — An optional argument to constrain the translation Y. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainTranslationZ` — An optional argument to constrain the translation Z. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationX` — An optional argument to constrain the rotation X. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationY` — An optional argument to constrain the rotation Y. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationZ` — An optional argument to constrain the rotation Z. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `orientation` — An optional orientation, currently it must be a coordinate system in which the components are defined. If omitted, the components are defined in the basic coordinate system.
- `applicationMethod` — The applicationMethod of the support.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote support is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createSupportFreeBody1(name: str, description: str, id: int, target: apex.EntityCollection, constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool, orientation: apex.IOrientation, applicationMethod: apex.attribute.ApplicationMethod, attachmentDistributionType: apex.attribute.DistributionType, attachmentRegion: apex.EntityCollection) -> SupportFreeBody1`
Create SupportFreeBody1 in this environment.

- `name` — An optional name for the createConstraintGeneral that will be created. If omitted the system will assign a default name formed by concatenating a specific prefix with the smallest possible integer required to ensure name uniqueness within the current Model. For example 'Constraint 1'.
- `description` — An optional description. If omitted, the description will be left blank.
- `id` — Optional - the id of the Constraint. If omitted, system automatically assigns the existing largest constraint id + 1.
- `target` — An entityCollection that is applied to the ConstraintDisplacement.
- `constrainTranslationX` — An optional argument to constrain the translation X. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainTranslationY` — An optional argument to constrain the translation Y. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainTranslationZ` — An optional argument to constrain the translation Z. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationX` — An optional argument to constrain the rotation X. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationY` — An optional argument to constrain the rotation Y. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `constrainRotationZ` — An optional argument to constrain the rotation Z. If it is True, the dof is constrained. If it is False, the dof is free. If omitted, the default value is False.
- `orientation` — An optional orientation, currently it must be a coordinate system in which the components are defined. If omitted, the components are defined in the basic coordinate system.
- `applicationMethod` — The applicationMethod of the support1.
- `attachmentDistributionType` — The DistributionType used in the remote method.
- `attachmentRegion` — The attachment region that the remote support is distributed to. It is unnecessary when the applicationMethod is direct.

### `apex.environment.createSupportFreeBody1Variable(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldSupportFreeBody) -> SupportFreeBody1Variable`
Create SupportFreeBody1Variable in this environment.

- `id` — An optional integer to define the id. If omitted, system automatically assigns the existing largest ID +1 to it.
- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Distributed Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Distributed Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the support.

### `apex.environment.createSupportFreeBodyVariable(name: str, description: str, spatialTarget: apex.environment.DFEMFieldSupportFreeBody) -> SupportFreeBodyVariable`
Create SupportFreeBodyVariable in this environment.

- `name` — An optional name for the load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Beam Distributed Load" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Beam Distributed Load 5".
- `description` — An optional description. If omitted, the description is blank.
- `spatialTarget` — The field to define the spatial distribution of the support.

### `apex.environment.createTemperatureInitialConditionConstant(target: apex.EntityCollection, name: str = "", initialTemperatureValue: float = NAN, description: str = "", id: int = 0) -> InitialTemperature`
Create an initial temperature condition. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createInitialTemperatureNodal().

- `target` — The target entities that the TemperatureInitialCondition is applied to.
- `name` — An optional name for the Initial Temperature load that will be created. If omitted, the system will assign a default name formed by concatenating the prefix "Initial Temperature" with the smallest possible integer required to ensure name uniqueness within the current Model. For example "Initial Temperature 9".
- `initialTemperatureValue` — The initial temperature load value, default is 20 degrees centigrade.
- `description` — An optional description for the Initial Temperature load that will be created. If omitted the description will be left blank.
- `id` — The ID of the InitialTemperature.

### `apex.environment.createTemperaturePropertyStaticConstant(temperatureValue: float, id: int = 0) -> LoadTemperaturePropertyStaticConstant`
Creates a LoadTemperaturePropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadTemperatureNodal(), createLoadTemperatureNodalVariable().

- `temperatureValue` — Temperature value represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. The default unit system is ''mm-kg-s-N-K''. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `id` — An optional load ID defined in TemperaturePropertyStaticConstant and assigned to the associated LoadTemperature. If omitted, the system will assign a default load ID.

Returns: the created LoadTemperaturePropertyStaticConstant

### `apex.environment.createTemperaturePropertyStaticVariable(temperatureValues: {str:{dict}}, id: int) -> LoadTemperaturePropertyStaticVariable`
Creates a LoadTemperaturePropertyStaticVariable. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createLoadTemperatureNodal(), createLoadTemperatureNodalVariable().

- `temperatureValues` — The load temperature property values. A nested Dictionary containing the pathName of the MeshBody on which the LoadTemperature is applied and the nodes IDs and the associated temperature values. The key of the top level dictionary is a string that represents the pathName of a MeshBody and the associated value is a secondary dictionary containing the individual nodes/temperatures. Each MeshBody that has one or more nodes referenced by the variable LoadTemperature will be included in the top level dictionary. For example, a LoadTemperature is applied to two different MeshBodies the top level dictionary will include two items - {"Model_1/Part 1/Mesh 1" : {dict1}, "Model_1/Part 2/Mesh 2": {dict2}} The secondary dictionary contains the information about which nodes are included in the variable LoadTemperature and the temperature values applied to each node. The type of distribution is identified in the secondary dictionary by the "identifier_type" key which is a string type. The associated value is a string type that must be "NODE_ID" as Apex only supports nodal temperature in 2021.1 release. For identifier type of NODE_ID, the temperature field is defined by the secondary dictionary items with "node_ids" and "temperatures" keys that identify the nodes IDs and temperature values. The value associated with the node_ids key is a List of integers, each integer identifying the node id. The value associated with the temperatures key is a List of floats, each float identifying the single temperature value associated with the corresponding node. The node_ids and temperatures lists must be of equal length with the temperature values indices aligned with the node ids indices. Example : LoadTemperature defined on three nodes of "Mesh 1" in "Model_1". {"Model_1/Part 1/Mesh 1" : { "identifier_type" : "NODE_ID", "node_ids" : [1000,1001,1002], "temperatures" : [301.52,302.78,303.92] } }
- `id` — An optional load ID defined in TemperaturePropertyStaticVariable and assigned to the associated LoadTemperature. If omitted, the system will assign a default load ID.

Returns: the created LoadTemperaturePropertyStaticVariable

### `apex.environment.getConstraint(name: str) -> apex.environment.Constraint`
Get a specified Constraint by name.

- `name` — The name of the Constraint.

### `apex.environment.getConstraintCombination(name: str = "#####") -> ConstraintCombination`
Get a specified ConstraintCombination by name.

- `name` — The name of the ConstraintCombination.

### `apex.environment.getConstraintCombinations() -> apex.EntityCollection`
Get all ConstraintCombination objects in this environment.

### `apex.environment.getConstraintDisplacement(name: str = "#####") -> Constraint`
Get a specified ConstraintDisplacement or ConstraintDisplacementVariable by name.

- `name` — The name of the ConstraintGeneral.

### `apex.environment.getConstraintDisplacements() -> apex.EntityCollection`
Get all ConstraintDisplacement and ConstraintDisplacementVariable objects in this environment.

### `apex.environment.getConstraintExcludeAuto(name: str = "#####") -> Constraint`
Get a specified ConstraintExcludeAuto or ConstraintExcludeAutoVariable by name.

- `name` — The name of the ConstraintExcludeDofs.

### `apex.environment.getConstraintExcludeAuto1(name: str = "#####") -> Constraint`
Get a specified ConstraintExcludeAuto1 or ConstraintExcludeAuto1Variable by name.

- `name` — The name of the ConstraintExcludeDofs1.

### `apex.environment.getConstraintExcludeAuto1s() -> apex.EntityCollection`

### `apex.environment.getConstraintExcludeAutos() -> apex.EntityCollection`

### `apex.environment.getConstraintSinglePoint(name: str = "#####") -> Constraint`
Get a specified ConstraintSinglePoint or ConstraintSinglePointVariable by name.

- `name` — The name of the ConstraintGeneral.

### `apex.environment.getConstraintSinglePoints() -> apex.EntityCollection`
Get all ConstraintSinglePoint and ConstraintSinglePointVariable objects in this environment.

### `apex.environment.getConstraints() -> apex.EntityCollection`
Get all Constraints in this environment.

### `apex.environment.getDisplacementConstraint(name: str) -> DisplacementConstraint`
Get a new DisplacementConstraint in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getConstraintDisplacement().

- `name` — of the DisplacementConstraint.

### `apex.environment.getDisplacementConstraints() -> apex.environment.DisplacementConstraintCollection`
Get all DisplacementConstraints in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getConstraintDisplacements().

### `apex.environment.getEnforcedMotion(name: str) -> EnforcedMotion`
Get a EnforcedMotion in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getLoadEnforcedMotionTotal().

- `name` — of the EnforcedMotion.

### `apex.environment.getForceMoment(name: str) -> ForceMoment`
Get a ForceMoment in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getLoadForceComponent(), getLoadMomentComponent().

- `name` — of the ForceMoment.

### `apex.environment.getGravity(name: str) -> Gravity`
Get a new Gravity in this environment.

- `name` — of the gravity.

### `apex.environment.getGravityLoads() -> apex.EntityCollection`
Get all Gravity loads in this environment.

### `apex.environment.getInitialCondition(name: str) -> apex.environment.InitialCondition`
Get a specified InitialCondition by name.

- `name` — The name of the InitialCondition.

### `apex.environment.getInitialConditions() -> apex.EntityCollection`
Get all InitialConditions in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getInitialTemperatureNodals().

### `apex.environment.getInitialDisplacementVelocities() -> apex.EntityCollection`
Get all InitialDisplacementVelocity and InitialDisplacementVelocityVariable objects in this environment.

### `apex.environment.getInitialDisplacementVelocity(name: str = "#####") -> InitialCondition`
Get a specified InitialDisplacementVelocity or InitialDisplacementVelocity by name.

- `name` — The name of the InitialDisplacementVelocity.

### `apex.environment.getInitialStrain(name: str = "#####") -> InitialCondition`
Get a specified InitialStrain or InitialStrainVariable by name.

- `name` — The name of the InitialStrain.

### `apex.environment.getInitialStrains() -> apex.EntityCollection`
Get all initialStrain and InitialStrainVariable objects in this environment.

### `apex.environment.getInitialStress(name: str = "#####") -> InitialCondition`
Get a specified InitialStress or InitialStressVariable by name.

- `name` — The name of the InitialStress.

### `apex.environment.getInitialStresss() -> apex.EntityCollection`

### `apex.environment.getInitialTemperatureDefault(name: str = "#####") -> InitialTemperatureDefault`
Get a specified InitialTemperatureDefault by name.

- `name` — The name of the InitialTemperatureDefault.

### `apex.environment.getInitialTemperatureDefaults() -> apex.EntityCollection`
Get all InitialTemperatureDefault objects in this environment.

### `apex.environment.getInitialTemperatureGradient2D(name: str = "#####") -> InitialCondition`
Get a specified InitialTemperatureGradient2D or InitialTemperatureGradient2DVariable by name.

- `name` — The name of the InitialTemperaturePlate.

### `apex.environment.getInitialTemperatureGradient2DHeat(name: str = "#####") -> InitialCondition`
Get a specified InitialTemperatureGradient2DHeat or InitialTemperatureGradient2DHeatVariable by name.

- `name` — The name of the InitialTemperatureHeatTransfer.

### `apex.environment.getInitialTemperatureGradient2DHeats() -> apex.EntityCollection`
Get all InitialTemperatureGradient2DHeat and InitialTemperatureGradient2DHeatVariable objects in this environment.

### `apex.environment.getInitialTemperatureGradient2Ds() -> apex.EntityCollection`
Get all InitialTemperatureGradient2D and InitialTemperatureGradient2DVariable objects in this environment.

### `apex.environment.getInitialTemperatureGradientBeam2(name: str = "#####") -> InitialCondition`

- `name` — The name of the InitialTemperatureGradientBeam2

### `apex.environment.getInitialTemperatureGradientBeam2s() -> apex.EntityCollection`

### `apex.environment.getInitialTemperatureGradientBeam3(name: str = "#####") -> InitialCondition`

- `name` — The name of the InitialTemperatureGradientBeam3

### `apex.environment.getInitialTemperatureGradientBeam3s() -> apex.EntityCollection`

### `apex.environment.getInitialTemperatureNodal(name: str = "#####") -> InitialCondition`
Get a specified InitialTemperatureNodal or InitialTemperatureNodalVariable by name.

- `name` — The name of the InitialTemperature.

### `apex.environment.getInitialTemperatureNodals() -> apex.EntityCollection`
Get all InitialTemperatureNodal and InitialTemperatureNodalVariable objects in this environment.

### `apex.environment.getLoad(name: str) -> apex.environment.Load`
Get a specified Load by name.

- `name` — The name of the load.

### `apex.environment.getLoadAccelerationNodal(name: str = "#####") -> Load`
Get a specified LoadAccelerationNodal or LoadAccelerationNodalVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadAccelerationNodals() -> apex.EntityCollection`
Get all LoadAccelerationNodal and LoadAccelerationNodalVariable objects in this environment.

### `apex.environment.getLoadAccelerationSpatial(name: str = "#####") -> LoadAccelerationSpatial`
Get a specified LoadAccelerationSpatial by name.

- `name` — The name of the load.

### `apex.environment.getLoadAccelerationSpatials() -> apex.EntityCollection`
Get all LoadAccelerationSpatial objects in this environment.

### `apex.environment.getLoadAreaFactor(name: str = "#####") -> Load`
Get a specified LoadAreaFactor or LoadAreaFactorVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadAreaFactors() -> apex.EntityCollection`
Get all LoadAreaFactor objects in this environment.

### `apex.environment.getLoadCombinationDynamic(name: str = "#####") -> LoadCombinationDynamic`
Get a specified LoadCombinationDynamic by name.

- `name` — The name of the load.

### `apex.environment.getLoadCombinationDynamics() -> apex.EntityCollection`
Get all LoadCombinationDynamic objects in this environment.

### `apex.environment.getLoadCombinationStatic(name: str = "#####") -> LoadCombinationStatic`
Get a specified LoadCombinationStatic by name.

- `name` — The name of the load.

### `apex.environment.getLoadCombinationStatics() -> apex.EntityCollection`
Get all LoadCombinationStatic objects in this environment.

### `apex.environment.getLoadDeformationAxial(name: str = "#####") -> Load`
Get a specified LoadDeformationAxial or LoadDeformationAxialVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadDeformationAxials() -> apex.EntityCollection`
Get all LoadDeformationAxial and LoadDeformationAxialVariable objects in this environment.

### `apex.environment.getLoadDistributed(name: str = "#####") -> Load`
Get a specified LoadDistributed or LoadDistributedVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadDistributedBeam2(name: str = "#####") -> Load`
Get a specified LoadDistributedBeam2 or LoadDistributedBeam2Variable by name.

- `name` — The name of the load.

### `apex.environment.getLoadDistributedBeam2s() -> apex.EntityCollection`
Get all LoadDistributedBeam2 and LoadDistributedBeam2Variable objects in this environment.

### `apex.environment.getLoadDistributedBeam3(name: str = "#####") -> Load`
Get a specified LoadDistributedBeam3 or LoadDistributedBeam3Variable by name.

- `name` — The name of the load.

### `apex.environment.getLoadDistributedBeam3s() -> apex.EntityCollection`
Get all LoadDistributedBeam3 and LoadDistributedBeam3Variable in this environment.

### `apex.environment.getLoadDistributeds() -> apex.EntityCollection`

### `apex.environment.getLoadDynamicAcoustic(name: str = "#####") -> LoadDynamicAcoustic`
Get a specified LoadDynamicAcoustic by name.

- `name` — The name of the LoadDynamicAcoustic

### `apex.environment.getLoadDynamicAcoustics() -> apex.EntityCollection`
Get all LoadDynamicAcoustic objects in this environment.

### `apex.environment.getLoadDynamicFrequency1(name: str = "#####") -> LoadDynamicFrequency1`
Get a specified LoadDynamicFrequency1 by name.

- `name` — The name of the LoadDynamicFrequency1

### `apex.environment.getLoadDynamicFrequency1s() -> apex.EntityCollection`
Get all LoadDynamicFrequency1 objects in this environment.

### `apex.environment.getLoadDynamicFrequency2(name: str = "#####") -> LoadDynamicFrequency2`
Get a specified LoadDynamicFrequency2 by name.

- `name` — The name of the LoadDynamicFrequency2

### `apex.environment.getLoadDynamicFrequency2s() -> apex.EntityCollection`
Get all LoadDynamicFrequency2 objects in this environment.

### `apex.environment.getLoadDynamicTimeAnalytical(name: str = "#####") -> LoadDynamicTimeAnalytical`
Get a specified LoadDynamicTimeAnalytical by name.

- `name` — The name of the LoadDynamicTimeAnalytical

### `apex.environment.getLoadDynamicTimeAnalyticals() -> apex.EntityCollection`
Get all LoadDynamicTimeAnalytical objects in this environment.

### `apex.environment.getLoadDynamicTimeTabular(name: str = "#####") -> LoadDynamicTimeTabular`
Get a specified LoadDynamicTimeTabular by name.

- `name` — The name of the LoadDynamicTimeTabular

### `apex.environment.getLoadDynamicTimeTabulars() -> apex.EntityCollection`
Get all LoadDynamicTimeTabular objects in this environment.

### `apex.environment.getLoadEnforcedMotionRelative(name: str = "#####") -> Load`
Get a specified LoadEnforcedMotionRelative or LoadEnforcedMotionRelativeVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadEnforcedMotionRelatives() -> apex.EntityCollection`
Get all LoadEnforcedMotionRelative objects in this environment.

### `apex.environment.getLoadEnforcedMotionTotal(name: str = "#####") -> Load`
Get a specified LoadEnforcedMotionTotal or LoadEnforcedMotionTotalVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadEnforcedMotionTotals() -> apex.EntityCollection`
Get all LoadEnforcedMotionTotal objects in this environment.

### `apex.environment.getLoadForceComponent(name: str = "#####") -> Load`
Get a specified LoadForceComponent or LoadForceComponentVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadForceComponents() -> apex.EntityCollection`
Get all LoadForceComponent objects in this environment.

### `apex.environment.getLoadForceFollowerNormal(name: str = "#####") -> Load`
Get a specified LoadForceFollowerNormal or LoadForceFollowerNormalVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadForceFollowerNormals() -> apex.EntityCollection`

### `apex.environment.getLoadForceFollowerVector(name: str = "#####") -> Load`
Get a specified LoadForceFollowerVector or LoadForceFollowerVectorVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadForceFollowerVectors() -> apex.EntityCollection`
Get all LoadForceFollowerVector and LoadForceFollowerVectorVariable objects in this environment.

### `apex.environment.getLoadForceRotational(name: str = "#####") -> LoadForceRotational`
Get a specified LoadForceRotational by name.

- `name` — The name of the load.

### `apex.environment.getLoadForceRotationals() -> apex.EntityCollection`
Get all LoadForceRotational objects in this environment.

### `apex.environment.getLoadLug(name: str) -> apex.environment.LoadLug`
Get a LoadLug in this environment.

- `name` — of the LoadLug.

### `apex.environment.getLoadLugs() -> apex.environment.LoadLugCollection`
Get all LoadLugs in this environment.

### `apex.environment.getLoadMomentComponent(name: str = "#####") -> Load`
Get a specified LoadMomentComponent or LoadMomentComponentVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadMomentComponents() -> apex.EntityCollection`
Get all LoadMomentComponent and LoadMomentComponentVariable objects in this environment.

### `apex.environment.getLoadMomentFollowerNormal(name: str = "#####") -> Load`
Get a specified LoadMomentFollowerNormal or LoadMomentFollowerNormalVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadMomentFollowerNormals() -> apex.EntityCollection`
Get all LoadMomentNormal and LoadMomentFollowerNormalVariable objects in this environment.

### `apex.environment.getLoadMomentFollowerVector(name: str = "#####") -> Load`
Get a specified LoadMomentFollowerVector or LoadMomentFollowerVectorVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadMomentFollowerVectors() -> apex.EntityCollection`
Get all LoadMomentFollowerVector and LoadMomentFollowerVectorVariable objects in this environment.

### `apex.environment.getLoadPhaseLead(name: str = "#####") -> Load`
Get a specified LoadPhaseLead or LoadPhaseLeadVariable by name.

- `name` — The name of the PhaseLead or PhaseLeadVariable.

### `apex.environment.getLoadPhaseLeads() -> apex.EntityCollection`
Get all LoadPhaseLead and LoadPhaseLeadVariable objects in this environment.

### `apex.environment.getLoadPressure(name: str) -> LoadPressure`
Return a PressureLoad in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getPressure().

- `name` — of the pressureLoad.

### `apex.environment.getLoadPressure2D(name: str = "#####") -> Load`
Get a specified LoadPressure2D or LoadPressure2DVariable by name.

- `name` — The name of the LoadPressure2D

### `apex.environment.getLoadPressure2Ds() -> apex.EntityCollection`
Get all LoadPressure2D and LoadPressure2DVariable objects in this environment.

### `apex.environment.getLoadPressureArea(name: str = "#####") -> Load`
Get a specified LoadPressureArea and LoadPressureAreaVariable by name.

- `name` — the name of the load.

### `apex.environment.getLoadPressureAreas() -> apex.EntityCollection`
Get all LoadPressureArea and LoadPressureAreaVariable objects in this environment.

### `apex.environment.getLoadPressures() -> apex.environment.LoadPressureCollection`
get all LoadPressures in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getPressures().

### `apex.environment.getLoadTemperature(name: str) -> LoadTemperature`
Get a LoadTemperature in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getLoadTemperatureNodal().

- `name` — of the LoadTemperature.

### `apex.environment.getLoadTemperatureDefault(name: str = "#####") -> LoadTemperatureDefault`
Get a specified LoadTemperatureDefault by name.

- `name` — The name of the load.

### `apex.environment.getLoadTemperatureDefaults() -> apex.EntityCollection`
Get all LoadTemperatureDefault objects in this environment.

### `apex.environment.getLoadTemperatureGradient2D(name: str = "#####") -> Load`
Get a specified LoadTemperatureGradient2D or LoadTemperatureGradient2DVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadTemperatureGradient2DHeat(name: str = "#####") -> Load`
Get a specified LoadTemperatureGradient2DHeat or LoadTemperatureGradient2DHeatVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadTemperatureGradient2DHeats() -> apex.EntityCollection`
Get all LoadTemperatureGradient2DHeat and LoadTemperatureGradient2DHeatVariable objects in this environment.

### `apex.environment.getLoadTemperatureGradient2Ds() -> apex.EntityCollection`
Get all LoadTemperatureGradient2D and LoadTemperatureGradient2DVariable objects in this environment.

### `apex.environment.getLoadTemperatureGradientBeam2(name: str = "#####") -> Load`
Get a specified LoadTemperatureGradientBeam2 or LoadTemperatureGradientBeam2Variable by name.

- `name` — The name of the load.

### `apex.environment.getLoadTemperatureGradientBeam2s() -> apex.EntityCollection`
Get all LoadTemperatureGradientBeam2 and LoadTemperatureGradientBeam2Variable objects in the environment.

### `apex.environment.getLoadTemperatureGradientBeam3(name: str = "#####") -> Load`
Get a specified LoadTemperatureGradientBeam3 or LoadTemperatureGradientBeam3Variable by name.

- `name` — The name of the TemperatureBeam3.

### `apex.environment.getLoadTemperatureGradientBeam3s() -> apex.EntityCollection`
Get all LoadTemperatureGradientBeam3 and LoadTemperatureGradientBeam3Variable objects in the environment.

### `apex.environment.getLoadTemperatureNodal(name: str = "#####") -> Load`
Get a specified LoadTemperatureNodal or LoadTemperatureNodalVariable by name.

- `name` — The name of the load.

### `apex.environment.getLoadTemperatureNodals() -> apex.EntityCollection`
Get all TemperatureNodal and LoadTemperatureNodalVariable objects in this environment.

### `apex.environment.getLoadTemperatures() -> apex.environment.LoadTemperatureCollection`
Get all LoadTemperatures in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getLoadTemperatureNodals().

### `apex.environment.getLoadTimeDelay(name: str = "#####") -> Load`
Get a specified LoadTimeDelay or LoadTimeDelayVariable by name.

- `name` — The name of the ConstraintSupport1.

### `apex.environment.getLoadTimeDelays() -> apex.EntityCollection`
Get all LoadTimeDelay and LoadTimeDelayVariable objects in this environment.

### `apex.environment.getLoadTotal(name: str = "#####") -> LoadTotal`
Get a specified LoadTotal by name.

- `name` — The name of the load.

### `apex.environment.getLoadTotals() -> apex.EntityCollection`
Get all LoadTotal objects in this environment.

### `apex.environment.getLoadTraction(name: str) -> LoadTraction`
Get a LoadTraction in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getLoadDistributed(), getLoadTotal().

- `name` — of the LoadTraction.

### `apex.environment.getLoadTractions() -> apex.environment.LoadTractionCollection`
Get all LoadTractions in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getLoadDistributeds(), getLoadTotals().

### `apex.environment.getLoads() -> apex.EntityCollection`
Get all Loads in this environment.

### `apex.environment.getPreloadBolt(name: str) -> apex.environment.PreloadBolt`
Get a PreloadBolt in this environment.

- `name` — name of the PreloadBolt.

### `apex.environment.getPreloadBolts() -> apex.environment.PreloadBoltCollection`
Get all PreloadBolts in this environment.

### `apex.environment.getPressure(name: str = "#####") -> Load`
Get a specified Pressure by name.

- `name` — the name of the load.

### `apex.environment.getPressures() -> apex.EntityCollection`
Get all Pressure objects in this environment.

### `apex.environment.getSupportFreeBodies() -> apex.EntityCollection`
Get all SupportFreeBody and SupportFreeBodyVariable objects in this environment.

### `apex.environment.getSupportFreeBody(name: str = "#####") -> Constraint`
Get a specified SupportFreeBody or SupportFreeBodyVariable by name.

- `name` — The name of the ConstraintSupport1.

### `apex.environment.getSupportFreeBody1(name: str = "#####") -> Constraint`
Get a specified SupportFreeBody1 or SupportFreeBody1Variable by name.

- `name` — The name of the ConstraintSupport1.

### `apex.environment.getSupportFreeBody1s() -> apex.EntityCollection`
Get all SupportFreeBody1 and SupportFreeBody1Variable objects in this environment.

### `apex.environment.getTemperatureInitialCondition(name: str) -> InitialTemperature`
Get an InitialTemperature in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: getInitialTemperatureNodal().

- `name` — name of the InitialTemperature.

## Classes in this module

Full method signatures are in `api/classes/apex.environment.md`.

`Constraint`, `ConstraintCombination`, `ConstraintDisplacement`, `ConstraintDisplacementVariable`, `ConstraintExcludeAuto`, `ConstraintExcludeAuto1`, `ConstraintExcludeAuto1Variable`, `ConstraintExcludeAutoVariable`, `ConstraintSinglePoint`, `ConstraintSinglePointVariable`, `DFEMFieldAccelerationNodal`, `DFEMFieldConstraintDisplacement`, `DFEMFieldConstraintExcludeAuto`, `DFEMFieldConstraintSinglePoint`, `DFEMFieldDeformationAxial`, `DFEMFieldEnforcedMotion`, `DFEMFieldForceComponent`, `DFEMFieldForceFollowerNormal`, `DFEMFieldForceFollowerVector`, `DFEMFieldInitialDisplacementVelocity`, `DFEMFieldInitialStrain`, `DFEMFieldInitialStress`, `DFEMFieldLoadAreaFactor`, `DFEMFieldLoadDistributed`, `DFEMFieldLoadDistributedBeam2`, `DFEMFieldLoadDistributedBeam3`, `DFEMFieldMomentComponent`, `DFEMFieldMomentFollowerNormal`, `DFEMFieldMomentFollowerVector`, `DFEMFieldPhaseLead`, `DFEMFieldPressure`, `DFEMFieldPressure2D`, `DFEMFieldPressureArea`, `DFEMFieldSupportFreeBody`, `DFEMFieldTemperatureGradient2D`, `DFEMFieldTemperatureGradient2DHeat`, `DFEMFieldTemperatureGradientBeam2`, `DFEMFieldTemperatureGradientBeam3`, `DFEMFieldTemperatureNodal`, `DFEMFieldTimeDelay`, `DiscreteTable`, `DisplacementConstraint`, `DisplacementConstraintCollection`, `EnforcedMotion`, `EnforcedMotionDynamicRep`, `EnforcedMotionRep`, `ForceMoment`, `ForceMomentDynamicRep`, `ForceMomentRep`, `Gravity`, `InitialCondition`, `InitialDisplacementVelocity`, `InitialDisplacementVelocityVariable`, `InitialStrain`, `InitialStrainVariable`, `InitialStress`, `InitialStressVariable`, `InitialTemperature`, `InitialTemperatureDefault`, `InitialTemperatureGradient2D`, `InitialTemperatureGradient2DHeat`, `InitialTemperatureGradient2DHeatVariable`, `InitialTemperatureGradient2DVariable`, `InitialTemperatureGradientBeam2`, `InitialTemperatureGradientBeam2Variable`, `InitialTemperatureGradientBeam3`, `InitialTemperatureGradientBeam3Variable`, `InitialTemperatureNodal`, `InitialTemperatureNodalVariable`, `Load`, `LoadAccelerationNodal`, `LoadAccelerationNodalVariable`, `LoadAccelerationSpatial`, `LoadAreaFactor`, `LoadAreaFactorVariable`, `LoadCombinationDynamic`, `LoadCombinationStatic`, `LoadDeformationAxial`, `LoadDeformationAxialVariable`, `LoadDistributed`, `LoadDistributedBeam2`, `LoadDistributedBeam2Variable`, `LoadDistributedBeam3`, `LoadDistributedBeam3Variable`, `LoadDistributedVariable`, `LoadDynamicAcoustic`, `LoadDynamicFrequency1`, `LoadDynamicFrequency2`, `LoadDynamicTimeAnalytical`, `LoadDynamicTimeTabular`, `LoadEnforcedMotionRelative`, `LoadEnforcedMotionRelativeVariable`, `LoadEnforcedMotionTotal`, `LoadEnforcedMotionTotalVariable`, `LoadForceComponent`, `LoadForceComponentVariable`, `LoadForceFollowerNormal`, `LoadForceFollowerNormalVariable`, `LoadForceFollowerVector`, `LoadForceFollowerVectorVariable`, `LoadForceRotational`, `LoadLug`, `LoadLugCollection`, `LoadLugProperty`, `LoadLugPropertyStatic`, `LoadMomentComponent`, `LoadMomentComponentVariable`, `LoadMomentFollowerNormal`, `LoadMomentFollowerNormalVariable`, `LoadMomentFollowerVector`, `LoadMomentFollowerVectorVariable`, `LoadPhaseLead`, `LoadPhaseLeadVariable`, `LoadPressure`, `LoadPressure2D`, `LoadPressure2DVariable`, `LoadPressureArea`, `LoadPressureAreaVariable`, `LoadPressureCollection`, `LoadPressureProperty`, `LoadPressurePropertyStaticConstant`, `LoadPressurePropertyStaticVariable`, `LoadRep`, `LoadTemperature`, `LoadTemperatureCollection`, `LoadTemperatureDefault`, `LoadTemperatureGradient2D`, `LoadTemperatureGradient2DHeat`, `LoadTemperatureGradient2DHeatVariable`, `LoadTemperatureGradient2DVariable`, `LoadTemperatureGradientBeam2`, `LoadTemperatureGradientBeam2Variable`, `LoadTemperatureGradientBeam3`, `LoadTemperatureGradientBeam3Variable`, `LoadTemperatureNodal`, `LoadTemperatureNodalVariable`, `LoadTemperatureProperty`, `LoadTemperaturePropertyStaticConstant`, `LoadTemperaturePropertyStaticVariable`, `LoadTimeDelay`, `LoadTimeDelayVariable`, `LoadTotal`, `LoadTraction`, `LoadTractionCollection`, `LoadTractionProperty`, `LoadTractionPropertyStaticConstant`, `LoadTractionPropertyStaticTotal`, `PreloadBolt`, `PreloadBoltCollection`, `PreloadBoltProperty`, `PreloadBoltPropertyStatic`, `PreloadBoltRep`, `Pressure`, `PressureVariable`, `SupportFreeBody`, `SupportFreeBody1`, `SupportFreeBody1Variable`, `SupportFreeBodyVariable`, `VariablePressureProfile`

