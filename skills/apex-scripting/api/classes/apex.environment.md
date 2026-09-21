# apex.environment — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.environment.Constraint`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
A constraint fixes one or more degrees of freedom during the simulation. Currently only structural displacement degrees of freedom can be constrained since Apex only supports structural simulation at this time.
Properties: `id`

Methods:

- `getId() -> int` — the id of the constraint.

## `apex.environment.ConstraintCombination`  (extends `Constraint`)
A constraint combination in this environment.
Properties: `combinedConstraints`

Methods:

- `getCombinedConstraints() -> apex.EntityCollection` — the collection of constraints to be combined.
#### `update(name: str, description: str, id: int, combinedConstraints: apex.EntityCollection) -> None`
Update the constraintCombination.

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `combinedConstraints` — Update the combinedConstraints.


## `apex.environment.ConstraintDisplacement`  (extends `Constraint`)
A displacement constraint that applies displacements in one or more degrees of freedom to Nodes. It can be used as a constraint or an enforced displacement. The constant constraint may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create one or more SPC entries for each Node. Apex supports a sets of pre-configured combinations of degrees of freedom to enable more convenient and robust constraint definitions by specifying the constraintType.
Properties: `constraintType`, `orientation`, `rotationX`, `rotationY`, `rotationZ`, `target`, `translationX`, `translationY`, `translationZ`

Methods:

- `getConstraintType() -> apex.attribute.ConstraintType` — the constraintType.
- `getOrientation() -> apex.IOrientation` — the orientation of the constraint, currently it must be a coordinate system.
- `getRotationX() -> float` — the rotation value about X. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getRotationY() -> float` — the rotation value about Y. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getRotationZ() -> float` — the rotation value about Z. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the constraint will be applied to. Constraints may be assigned to Solids, Cells, Faces, Curves, Edges and Nodes. Constraints assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTranslationX() -> float` — the translation value in X. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getTranslationY() -> float` — the translation value in X. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getTranslationZ() -> float` — the translation value in X. It is a Length quantity and must be defined using the units of Length from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, constraintType: apex.attribute.ConstraintType, orientation: apex.IOrientation) -> None`
Updates one or more properties of the constraint. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the constraint.
- `description` — Updates the description of the constraint.
- `id` — Updates the id of the constraint.
- `target` — Updates the target.
- `translationX` — Updates the translationX. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `translationY` — Updates the translationY. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `translationZ` — Updates the translationZ. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `rotationX` — Updates the rotationX. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `rotationY` — Updates the rotationY. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `rotationZ` — Updates the rotationZ. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `constraintType` — Updates the constraintType.
- `orientation` — Updates the orientation.


## `apex.environment.ConstraintDisplacementVariable`  (extends `Constraint`)
This class represents a spatially varying displacement constraint applied to Nodes. A single instance of this class may include a multiplicity of individual constraints each applied to a different node. All of the individual constraints composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one or several SPC entries for each node within the scope of the region with which it is associated. The variation of constraint across the nodes that this constraint references is defined using a DFEMFieldConstraintDisplacement. This field defines the nodes that represent the region to which this constraint is applied as well as the distribution of constraints across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldConstraintDisplacement` — a DFEMFieldConstraintDisplacement that identifies nodes that represent the region to which this load is applied as well as the distribution of constraints across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintDisplacement) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.ConstraintExcludeAuto`  (extends `Constraint`)
It defines a set of degrees of freedom to be excluded from automatic constraints of singularities. The constant ConstraintExcludeAuto may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create one or several Nastran SPCOFF entries on a Node.
Properties: `excludeRotationX`, `excludeRotationY`, `excludeRotationZ`, `excludeTranslationX`, `excludeTranslationY`, `excludeTranslationZ`, `target`

Methods:

- `getExcludeRotationX() -> bool` — the argument to indicate whether the rotation X is excluded or not.
- `getExcludeRotationY() -> bool` — the argument to indicate whether the rotation Y is excluded or not.
- `getExcludeRotationZ() -> bool` — the argument to indicate whether the rotation Z is excluded or not.
- `getExcludeTranslationX() -> bool` — the argument to indicate whether the translation X is excluded or not.
- `getExcludeTranslationY() -> bool` — the argument to indicate whether the translation Y is excluded or not.
- `getExcludeTranslationZ() -> bool` — the argument to indicate whether the translation Z is excluded or not.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the constraint will be applied to. Constraints may be assigned to Solids, Cells, Faces, Curves, Edges and Nodes. Constraints assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, target: apex.EntityCollection, excludeTranslationX: bool, excludeTranslationY: bool, excludeTranslationZ: bool, excludeRotationX: bool, excludeRotationY: bool, excludeRotationZ: bool) -> None`
Updates one or more properties of the ConstraintExcludeAuto. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the ConstraintExcludeAuto.
- `description` — Updates the description of the ConstraintExcludeAuto.
- `target` — Updates the target of the ConstraintExcludeAuto.
- `excludeTranslationX` — Updates the constrainTranslationX.
- `excludeTranslationY` — Updates the constrainTranslationY.
- `excludeTranslationZ` — Updates the constrainTranslationZ.
- `excludeRotationX` — Updates the constrainRotationX.
- `excludeRotationY` — Updates the constrainRotationY.
- `excludeRotationZ` — Updates the constrainRotationZ.


## `apex.environment.ConstraintExcludeAuto1`  (extends `Constraint`)
An alternate form of ConstraintExcludeAuto.
Properties: `excludeRotationX`, `excludeRotationY`, `excludeRotationZ`, `excludeTranslationX`, `excludeTranslationY`, `excludeTranslationZ`, `target`

Methods:

- `getExcludeRotationX() -> bool` — the argument to indicate whether the rotation X is excluded or not.
- `getExcludeRotationY() -> bool` — the argument to indicate whether the rotation Y is excluded or not.
- `getExcludeRotationZ() -> bool` — the argument to indicate whether the rotation Z is excluded or not.
- `getExcludeTranslationX() -> bool` — the argument to indicate whether the translation X is excluded or not.
- `getExcludeTranslationY() -> bool` — the argument to indicate whether the translation Y is excluded or not.
- `getExcludeTranslationZ() -> bool` — the argument to indicate whether the translation Z is excluded or not.
- `getTarget() -> apex.EntityCollection` — the target entities that the ConstraintExcludeDofs1 is applied to.
#### `update(name: str, description: str, excludeTranslationX: bool, excludeTranslationY: bool, excludeTranslationZ: bool, excludeRotationX: bool, excludeRotationY: bool, excludeRotationZ: bool, target: apex.EntityCollection) -> None`
Update this ConstraintExcludeDof1.One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `excludeTranslationX` — Update the constrainTranslationX.
- `excludeTranslationY` — Update the constrainTranslationY.
- `excludeTranslationZ` — Update the constrainTranslationZ.
- `excludeRotationX` — Update the constrainRotationX.
- `excludeRotationY` — Update the constrainRotationY.
- `excludeRotationZ` — Update the constrainRotationZ.
- `target` — Update the target.


## `apex.environment.ConstraintExcludeAuto1Variable`  (extends `Constraint`)
An alternate form of ConstraintExcludeAutoVariable.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldConstraintExcludeAuto` — the field that defines the dof distribution.
#### `update(name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintExcludeAuto) -> None`
Update method.One or more properties may be updated in each call to update().

- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.ConstraintExcludeAutoVariable`  (extends `Constraint`)
This class represents a spatially varying ConstraintExcludeAuto applied to Nodes. A single instance of this class may include a multiplicity of individual exclude each applied to a different node. All of the individual excludes composed by this exclude share a common ID. When used in a Nastran simulation this class will give rise to one or several SPCOFF entries for each node within the scope of the region with which it is associated. The variation of exclude across the nodes that this exclude references is defined using a DFEMFieldExcludeDof. This field defines the nodes that represent the region to which this exclude is applied as well as the distribution of excludes across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldConstraintExcludeAuto` — a DFEMFieldExcludeDof that identifies nodes that represent the region to which this exclude is applied as well as the distribution of excludes across that region.
#### `update(name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintExcludeAuto) -> None`
Updates one or more properties of the ConstraintExcludeAutoVariable. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name .
- `description` — Updates the description.
- `spatialTarget` — Updates the spatialTarget.


## `apex.environment.ConstraintSinglePoint`  (extends `Constraint`)
A single point constraint fixing one or more degrees of freedom on Node. The constant constraint may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create one or more SPC1 entries for each Node. Apex supports a sets of pre-configured combinations of degrees of freedom to enable more convenient and robust constraint definitions by specifying the constraintType.
Properties: `constrainRotationX`, `constrainRotationY`, `constrainRotationZ`, `constrainTranslationX`, `constrainTranslationY`, `constrainTranslationZ`, `constraintType`, `orientation`, `target`

Methods:

- `getConstrainRotationX() -> bool` — a boolean argument to constrain the rotation about X.
- `getConstrainRotationY() -> bool` — a boolean argument to constrain the rotation about Y.
- `getConstrainRotationZ() -> bool` — a boolean argument to constrain the rotation about Z.
- `getConstrainTranslationX() -> bool` — a boolean argument to constrain the translation in X.
- `getConstrainTranslationY() -> bool` — a boolean argument to constrain the translation in Y.
- `getConstrainTranslationZ() -> bool` — a boolean argument to constrain the translation in Z.
- `getConstraintType() -> apex.attribute.ConstraintType` — the constraintType that pre-defines the constrained degrees of freedom.
- `getOrientation() -> apex.IOrientation` — the orientation of the constraint. Currently it must be a coordinate system
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the constraint will be applied to. Constraints may be assigned to Solids, Cells, Faces, Curves, Edges and Nodes. Constraints assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool, target: apex.EntityCollection, constraintType: apex.attribute.ConstraintType, orientation: apex.IOrientation) -> None`
Updates one or more properties of the constraint. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the constraint.
- `description` — Updates the description of the constraint.
- `id` — Updates the id of the constraint.
- `constrainTranslationX` — Updates the constrainTranslationX.
- `constrainTranslationY` — Updates the constrainTranslationY.
- `constrainTranslationZ` — Updates the constrainTranslationZ.
- `constrainRotationX` — Updates the constrainRotationX.
- `constrainRotationY` — Updates the constrainRotationY.
- `constrainRotationZ` — Updates the constrainRotationZ.
- `target` — Updates the target.
- `constraintType` — Updates the constraintType.
- `orientation` — Updates the orientation.


## `apex.environment.ConstraintSinglePointVariable`  (extends `Constraint`)
This class represents a spatially varying constraint applied to Nodes. A single instance of this class may include a multiplicity of individual constraints each applied to a different node. All of the individual constraints composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one or several SPC1 entries for each node within the scope of the region with which it is associated. The variation of constraint across the nodes that this constraint references is defined using a DFEMFieldConstraintSinglePoint. This field defines the nodes that represent the region to which this constraint is applied as well as the distribution of constraints across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldConstraintSinglePoint` — a DFEMFieldConstraintSinglePoint that identifies nodes that represent the region to which this load is applied as well as the distribution of constraints across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldConstraintSinglePoint) -> None`
Updates one or more properties of the constraint. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the constraint.
- `name` — Updates the name of the constraint.
- `description` — Updates the description of the constraint.
- `spatialTarget` — Updates the spatialTarget of the constraint.


## `apex.environment.DFEMFieldAccelerationNodal`
A class describing a table like data structure defining the spatially varying acceleration magnitude across a multiplicity of nodes. Each "row" in this table identifies a node and the temperature data for that node. The table includes ten "columns", nodeIds, pathNames pathIndices accelerationVectorsX accelerationVectorsY accelerationVectorsZ orientations scaleFactors The acceleration vectors may be blank but at least one should be defined for each associated node so that the acceleration vector is not zero. Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated node. To define or determine the MeshBody associated with any node in the field use the entry in pathIndices corresponding to the node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, nodes 1000 and 1001 belong to "Mesh 1", while nodes 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and acceleration associated with each node in the field, the following code could be used, for index, node_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has an acceleration in X component of', accelerationVectorsX[index])
Properties: `accelerationVectorsX`, `accelerationVectorsY`, `accelerationVectorsZ`, `nodeIds`, `orientations`, `pathIndices`, `pathNames`, `scaleFactors`

Methods:

#### `DFEMFieldAccelerationNodal(orientations: [int], scaleFactors: [float], accelerationVectorsX: [float], accelerationVectorsY: [float], accelerationVectorsZ: [float], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldAccelerationNodal in this environment.

- `orientations` — The optional orientation. It can be either an IOrientation object which only accepts coordinate system or a list of IOrientation objects or a list of integers of the coordinate system IDs. If omitted, then basic coordinate system is used.
- `scaleFactors` — The optional scale factors for the acceleration vectors. It can be either a float value for all vectors or a list of floats to define different scale factors for each acceleration vector. If omitted, all scale factors are 1.0.
- `accelerationVectorsX` — The X component of the acceleration vector.
- `accelerationVectorsY` — The Y component of the acceleration vector.
- `accelerationVectorsZ` — The Z component of the acceleration vector.
- `nodeIds` — A list of integers to define target node IDs in the field.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getAccelerationVectorsX() -> [float]` — the X components of the acceleration vectors. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getAccelerationVectorsY() -> [float]` — the Y components of the acceleration vectors. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getAccelerationVectorsZ() -> [float]` — the Z components of the acceleration vectors. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getOrientations() -> [int]` — the orientations used to define the direction of the acceleration vectors. Currently it only accepts coordinate system object.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getScaleFactors() -> [float]` — a list of scale factors that will be applied to the acceleration vectors. The magnitude of the acceleration load applied to each Node in the target is based on the product of the resultant of the provided acceleration vector and this scale factor.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(orientations: [int], scaleFactors: [float], accelerationVectorsX: [float], accelerationVectorsY: [float], accelerationVectorsZ: [float], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the Acceleration load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `orientations` — Updates the orientations.
- `scaleFactors` — Updates the scaleFactors.
- `accelerationVectorsX` — Updates the accelerationVectorsX. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `accelerationVectorsY` — Updates the accelerationVectorsY. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `accelerationVectorsZ` — Updates the accelerationVectorsZ. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `nodeIds` — Updates the nodeIds.
- `pathNames` — Update the pathNames.
- `pathIndices` — Update the pathIndices .


## `apex.environment.DFEMFieldConstraintDisplacement`
A class describing a table like data structure defining the spatially varying constraint across a multiplicity of nodes. Each "row" in this table identifies a node and the constraint data on that node. The table includes the following "columns", nodeIds pathNames pathIndices orientations translationsX translationsY translationsZ rotationsX rotationsY rotationsZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and constraint in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a displacement constraint in translation X ', translationX[index]).
Properties: `nodeIds`, `orientations`, `pathIndices`, `pathNames`, `rotationsX`, `rotationsY`, `rotationsZ`, `translationsX`, `translationsY`, `translationsZ`

Methods:

#### `DFEMFieldConstraintDisplacement(nodeIds: [int], orientations: [int], translationsX: [float], translationsY: [float], translationsZ: [float], rotationsX: [float], rotationsY: [float], rotationsZ: [float], pathNames: [str], pathIndices: [int]) -> None`
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

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getOrientations() -> [int]` — a list of orientations for the displacement components.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getRotationsX() -> [float]` — a list of the rotation values about X axis. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getRotationsY() -> [float]` — a list of the rotation values about Y axis. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getRotationsZ() -> [float]` — a list of the rotation values about Z axis. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getTranslationsX() -> [float]` — a list of the translation values in X axis. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getTranslationsY() -> [float]` — a list of the translation values in Y axis. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getTranslationsZ() -> [float]` — a list of the translation values in Z axis. It is a Length quantity and must be defined using the units of Length from the active script unit system.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], orientations: [int], translationsX: [float], translationsY: [float], translationsZ: [float], rotationsX: [float], rotationsY: [float], rotationsZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the constraint. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `orientations` — Update the orientations.
- `translationsX` — Updates the translationsX
- `translationsY` — update the translationsY.
- `translationsZ` — Update the translationsZ.
- `rotationsX` — Update the rotationsX.
- `rotationsY` — Update the rotationsY.
- `rotationsZ` — Update the rotationsZ.
- `pathNames` — Update the pathNames of this DFEMFieldConstraintDisplacement
- `pathIndices` — Update the pathIndices of this DFEMFieldConstraintDisplacement


## `apex.environment.DFEMFieldConstraintExcludeAuto`
A class describing a table like data structure defining the spatially varying exclude across a multiplicity of nodes. Each "row" in this table identifies a node and the exclude data on that node. The table includes the following "columns", nodeIds pathNames pathIndices excludeTranslationX excludeTranslationY excludeTranslationZ excludeRotationX excludeRotationY excludeRotationZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and exclude in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a exclude in translation X is ', excludeTranslationX[index]).
Properties: `excludeRotationX`, `excludeRotationY`, `excludeRotationZ`, `excludeTranslationX`, `excludeTranslationY`, `excludeTranslationZ`, `nodeIds`, `pathIndices`, `pathNames`

Methods:

#### `DFEMFieldConstraintExcludeAuto(excludeTranslationX: [bool], excludeTranslationY: [bool], excludeTranslationZ: [bool], excludeRotationX: [bool], excludeRotationY: [bool], excludeRotationZ: [bool], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> None`
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

- `getExcludeRotationX() -> [bool]` — a list of booleans to exclude the rotation X for each node in the field. For example, excludeRotationX = [False, True, True, False].
- `getExcludeRotationY() -> [bool]` — a list of booleans to exclude the rotation Y for each node in the field. For example, excludeRotationY = [False, True, True, False].
- `getExcludeRotationZ() -> [bool]` — a list of booleans to exclude the rotation Z for each node in the field. For example, excludeRotationZ = [False, True, True, False].
- `getExcludeTranslationX() -> [bool]` — a list of booleans to exclude the translation X for each node in the field. For example, excludeTranslationX = [False, True, True, False].
- `getExcludeTranslationY() -> [bool]` — a list of booleans to exclude the translation Y for each node in the field. For example, excludeTranslationY = [False, True, True, False].
- `getExcludeTranslationZ() -> [bool]` — a list of booleans to exclude the translation Z for each node in the field. For example, excludeTranslationZ = [False, True, True, False].
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(excludeTranslationX: [bool], excludeTranslationY: [bool], excludeTranslationZ: [bool], excludeRotationX: [bool], excludeRotationY: [bool], excludeRotationZ: [bool], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `excludeTranslationX` — Updates the excludeTranslationX.
- `excludeTranslationY` — Updates the excludeTranslationY.
- `excludeTranslationZ` — Updates the excludeTranslationZ.
- `excludeRotationX` — Updates the excludeRotationX.
- `excludeRotationY` — Updates the excludeRotationY.
- `excludeRotationZ` — Updates the excludeRotationZ.
- `nodeIds` — Updates the nodeIds.
- `pathNames` — Update the pathNames of this DFEMFieldConstraintExcludeAuto
- `pathIndices` — Update the pathIndices of this DFEMFieldConstraintExcludeAuto


## `apex.environment.DFEMFieldConstraintSinglePoint`
A class describing a table like data structure defining the spatially varying constraint across a multiplicity of nodes. Each "row" in this table identifies a node and the constraint data on that node. The table includes the following "columns", nodeIds pathNames pathIndices orientations constrainTranslationX constrainTranslationY constrainTranslationZ constrainRotationX constrainRotationY constrainRotationZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and constraint in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a constraint in translation X is ', constrainTranslationX[index]).
Properties: `constrainRotationX`, `constrainRotationY`, `constrainRotationZ`, `constrainTranslationX`, `constrainTranslationY`, `constrainTranslationZ`, `nodeIds`, `orientations`, `pathIndices`, `pathNames`

Methods:

#### `DFEMFieldConstraintSinglePoint(orientations: [int], constrainTranslationX: [bool], constrainTranslationY: [bool], constrainTranslationZ: [bool], constrainRotationX: [bool], constrainRotationY: [bool], constrainRotationZ: [bool], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> None`
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

- `getConstrainRotationX() -> [bool]` — a list of booleans to indicate the whether the rotation X is constrained or not for each node in the field. For example, constrainRotationX = [False, True, True, False].
- `getConstrainRotationY() -> [bool]` — a list of booleans to indicate the whether the rotation Y is constrained or not for each node in the field. For example, constrainRotationY = [False, True, True, False].
- `getConstrainRotationZ() -> [bool]` — a list of booleans to indicate the whether the rotation Z is constrained or not for each node in the field. For example, constrainRotationZ = [False, True, True, False].
- `getConstrainTranslationX() -> [bool]` — a list of booleans to indicate the whether the translation X is constrained or not for each node in the field. For example, constrainTranslationX = [False, True, True, False].
- `getConstrainTranslationY() -> [bool]` — a list of booleans to indicate the whether the translation Y is constrained or not for each node in the field. For example, constrainTranslationY = [False, True, True, False].
- `getConstrainTranslationZ() -> [bool]` — a list of booleans to indicate the whether the translation Z is constrained or not for each node in the field. For example, constrainTranslationZ = [False, True, True, False].
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getOrientations() -> [int]` — a list of the orientations of the constraint.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(orientations: [int], constrainTranslationX: [bool], constrainTranslationY: [bool], constrainTranslationZ: [bool], constrainRotationX: [bool], constrainRotationY: [bool], constrainRotationZ: [bool], nodeIds: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `orientations` — Updates the orientations.
- `constrainTranslationX` — Update the constrainTranslationX of this DFEMFieldConstraintSinglePoint
- `constrainTranslationY` — Update the constrainTranslationY of this DFEMFieldConstraintSinglePoint
- `constrainTranslationZ` — Update the constrainTranslationZ of this DFEMFieldConstraintSinglePoint
- `constrainRotationX` — Update the constrainRotationX of this DFEMFieldConstraintSinglePoint
- `constrainRotationY` — Update the constrainRotationY of this DFEMFieldConstraintSinglePoint
- `constrainRotationZ` — Update the constrainRotationZ of this DFEMFieldConstraintSinglePoint
- `nodeIds` — Updates the nodeIds.
- `pathNames` — Update the pathNames of this DFEMFieldConstraintSinglePoint
- `pathIndices` — Update the pathIndices of this DFEMFieldConstraintSinglePoint


## `apex.environment.DFEMFieldDeformationAxial`
A class describing a table like data structure defining the spatially varying deformation across a multiplicity of elements/element faces. Each "row" in this table identifies an element and the load data for that element. The table includes ten "columns", elementIds, pathNames pathIndices deformations Deformation values for each element MUST be defined. Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds= [1000, 1001, 1002, 1003], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and deformation associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a deformation of', deformations[index])
Properties: `deformations`, `elementIds`, `pathIndices`, `pathNames`

Methods:

#### `DFEMFieldDeformationAxial(elementIds: [int], deformations: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldDeformationAxial in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `deformations` — A list of deformation values.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getDeformations() -> [float]` — a list of the deformation values along the element axis.
- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], deformations: [float], pathNames: [str], pathIndices: [int]) -> None`
Update method. One or more properties may be updated in each call to update().

- `elementIds` — Update the elementIds.
- `deformations` — Update the deformations.
- `pathNames` — Update the pathNames of this DFEMFieldDeformationAxial
- `pathIndices` — Update the pathIndices of this DFEMFieldDeformationAxial


## `apex.environment.DFEMFieldEnforcedMotion`
A class describing a table like data structure defining the spatially varying motion across a multiplicity of nodes. Each "row" in this table identifies a node and the motion data on that node. The table includes the following "columns", nodeIds pathNames pathIndices orientations translationsX translationsY translationsZ rotationsX rotationsY rotationsZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and motion in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a motion in X component of', motionsX[index]).
Properties: `nodeIds`, `orientations`, `pathIndices`, `pathNames`, `rotationsX`, `rotationsY`, `rotationsZ`, `translationsX`, `translationsY`, `translationsZ`

Methods:

#### `DFEMFieldEnforcedMotion(nodeIds: [int], orientations: [int], translationsX: [float], translationsY: [float], translationsZ: [float], rotationsX: [float], rotationsY: [float], rotationsZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldEnforcedMotion in this environment. It can be used for both EnforcedMotionTotalVariable and EnforcedMotionRelativeVariable.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `translationsY` — The list of translation values in Y axis.
- `translationsZ` — The list of translation values in Z axis.
- `rotationsX` — The list of rotation values about X axis.
- `rotationsY` — The list of rotation values about Y axis.
- `rotationsZ` — The list of rotation values about Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getOrientations() -> [int]` — an optional list of orientations for the load components. Each item in the list must be an id of a coordinate system. If all load components use the same orientation, the list must contain only one integer that points to the id of the coordinate system. If omitted, all load components are defined in the basic coordinate system.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getRotationsX() -> [float]` — a list of the motion values in rotation X. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system. If all motion values are the same, the list should only contain a float value.
- `getRotationsY() -> [float]` — a list of the motion values in rotation Y. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system. If all motion values are the same, the list should only contain a float value.
- `getRotationsZ() -> [float]` — a list of the motion values in rotation Z. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system. If all motion values are the same, the list should only contain a float value.
- `getTranslationsX() -> [float]` — a list of the motion values in translation X. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system. If all motion values are the same, the list should only contain a float value.
- `getTranslationsY() -> [float]` — a list of the motion values in translation Y. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system. If all motion values are the same, the list should only contain a float value.
- `getTranslationsZ() -> [float]` — a list of the motion values in translation Z. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system. If all motion values are the same, the list should only contain a float value.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], orientations: [int], translationsX: [float], translationsY: [float], translationsZ: [float], rotationsX: [float], rotationsY: [float], rotationsZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the enforced motion. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `orientations` — Update the orientations.
- `translationsX` — Update the translationsX. It is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `translationsY` — update the translationsY. It is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `translationsZ` — Update the translationsZ. It is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `rotationsX` — Update the rotationsX. It is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `rotationsY` — Update the rotationsY. It is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `rotationsZ` — Update the rotationsZ. It is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `pathNames` — Update the pathNames of this DFEMFieldEnforcedMotion
- `pathIndices` — Update the pathIndices of this DFEMFieldEnforcedMotion


## `apex.environment.DFEMFieldForceComponent`
A class describing a table like data structure defining the spatially varying force across a multiplicity of nodes. Each "row" in this table identifies a node and the force data on that node. The table includes the following "columns", nodeIds pathNames pathIndices orientations scaleFactors forcesX forcesY forcesZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and force in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a force in X component of', forcesX[index]).
Properties: `forcesX`, `forcesY`, `forcesZ`, `nodeIds`, `orientations`, `pathIndices`, `pathNames`, `scaleFactors`

Methods:

#### `DFEMFieldForceComponent(nodeIds: [int], orientations: [int], scaleFactors: [float], forcesX: [float], forcesY: [float], forcesZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldForceComponent in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — An optional orientations. It can be either an IOrientation object which only accepts a coordinate system object or a list of IOrientation objects. If omitted, the components are defined in the basic coordinate system.
- `scaleFactors` — An optional scale factor. It can be either a float value or a list of float. If omitted,the scale factor is 1.0.
- `forcesX` — A list of force component values in X axis.
- `forcesY` — A list of force component values in Y axis.
- `forcesZ` — A list of force component values in Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getForcesX() -> [float]` — a list to define the force X component values. If all component values are the same, the list should only contain one float value.
- `getForcesY() -> [float]` — a list to define the force Y component values. If all component values are the same, the list should only contain one float value.
- `getForcesZ() -> [float]` — a list to define the force Z component values. If all component values are the same, the list should only contain one float value.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getOrientations() -> [int]` — an optional list of integers to represent the orientations for the load components. Each element in the list must be the id of a coordinate system. If all load components use the same orientation, the list must contain only one integer that points to the id of the coordinate system. If omitted, all load components are defined in the basic coordinate system.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getScaleFactors() -> [float]` — an optional list of scale factors for the loads. If all loads in the field have the same scale factor, the list must contain only one float value. If omitted, the default value is 1.0 for all loads.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target element/node ids to be removed from the field.

#### `update(nodeIds: [int], orientations: [int], scaleFactors: [float], forcesX: [float], forcesY: [float], forcesZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `orientations` — Update the orientations.
- `scaleFactors` — Update the scaleFactors.
- `forcesX` — Update the forcesX.
- `forcesY` — Update the forcesY.
- `forcesZ` — Update the forcesZ.
- `pathNames` — Update the pathNames of this DFEMFieldForceComponent
- `pathIndices` — Update the pathIndices of this DFEMFieldForceComponent


## `apex.environment.DFEMFieldForceFollowerNormal`
A class describing a table like data structure defining the spatially varying force across a multiplicity of nodes. Each "row" in this table identifies a node and the force data on that node. The table includes the following "columns", nodeIds pathNames pathIndices forceMagnitudes points1 points2 points3 points4 Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and force associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a force magnitude of', forcesMagnitude[index]).
Properties: `forceMagnitudes`, `nodeIds`, `pathIndices`, `pathNames`, `points1`, `points2`, `points3`, `points4`

Methods:

#### `DFEMFieldForceFollowerNormal(nodeIds: [int], forceMagnitudes: [float], points1: [int], points2: [int], points3: [int], points4: [int], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldForceFollowerNormal in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `forceMagnitudes` — A list of force magnitude.
- `points1` — The starting point of the first vector. It can be either a point or a list of points.
- `points2` — The end point of the first vector. It can be either a point or a list of points.
- `points3` — The starting point of the second vector. It can be either a point or a list of points.
- `points4` — The end point of the second vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getForceMagnitudes() -> [float]` — a list to define the force magnitudes, forceMagnitudes is a Force quantity and is defined using the units of Force from the active script unit system. Each force direction is parallel to the cross product of two vectors defined by four points.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPoints1() -> [int]` — a list of starting points of the direction vectors. Each item in the list must be a node ID. If all starting points are the same, the list should only contain one node ID.
- `getPoints2() -> [int]` — a list of end points of the direction vectors. Each item in the list must be a node ID. If all starting points are the same, the list should only contain one node ID.
- `getPoints3() -> [int]` — a list of starting points of the direction vectors. Each item in the list must be a node ID. If all starting points are the same, the list should only contain one node ID.
- `getPoints4() -> [int]` — a list of end points of the direction vectors. Each item in the list must be a node ID. If all starting points are the same, the list should only contain one node ID.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], forceMagnitudes: [float], points1: [int], points2: [int], points3: [int], points4: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `forceMagnitudes` — Update the forceMagnitudes of the Force. forceMagnitudes is a Force quantity and is defined using the units of Force from the active script unit system.
- `points1` — Update the points1.
- `points2` — Update the points2.
- `points3` — Update the points3.
- `points4` — Update the points4.
- `pathNames` — Update the pathNames of this DFEMFieldForceFollowerNormal
- `pathIndices` — Update the pathIndices of this DFEMFieldForceFollowerNormal


## `apex.environment.DFEMFieldForceFollowerVector`
A class describing a table like data structure defining the spatially varying force across a multiplicity of nodes. Each "row" in this table identifies a node and the force data on that node. The table includes the following "columns", nodeIds pathNames pathIndices forceMagnitudes points1 points2 Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and force associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a force magnitude of', forcesMagnitude[index]).
Properties: `forceMagnitudes`, `nodeIds`, `pathIndices`, `pathNames`, `points1`, `points2`

Methods:

#### `DFEMFieldForceFollowerVector(nodeIds: [int], forceMagnitudes: [float], points1: [int], points2: [int], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldForceFollowerVector in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `forceMagnitudes` — A list of force magnitudes.
- `points1` — the starting point of the load vector. It can be either a point or a list points.
- `points2` — the end point of the load vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getForceMagnitudes() -> [float]` — a list of floats to define the force magnitudes, forceMagnitudes is a Force quantity and is defined using the units of Force from the active script unit system. If all force magnitudes are the same, the list should only contain one float value. Each force direction is along the vector from point1 to point2.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target node in the field. If only one pathName is existed in list of pathNames, this pathIndices only contains one integer of 0.
- `getPathNames() -> [str]` — a list of strings to define the pathNames of the mesh bodies that include target nodes. If all pathNames are the same, then the list only contains one string.
- `getPoints1() -> [int]` — a list of starting points of the direction vectors. Each item in the list must be a node or a vertex. If all starting points are the same, the list should contain only one node or vertex.
- `getPoints2() -> [int]` — a list of end points of the direction vectors. Each item in the list must be a node or a vertex.If all end points are the same, the list should contain only one node or vertex.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], forceMagnitudes: [float], points1: [int], points2: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `forceMagnitudes` — Update the forceMagnitudes. forceMagnitudes is a Force quantity and is defined using the units of Force from the active script unit system.
- `points1` — Update the points1.
- `points2` — Update the points2.
- `pathNames` — Update the pathNames of this DFEMFieldForceFollowerVector
- `pathIndices` — Update the pathIndices of this DFEMFieldForceFollowerVector


## `apex.environment.DFEMFieldInitialDisplacementVelocity`
A class describing a table like data structure defining the spatially varying initial displacement and velocity across a multiplicity of elements. Each "row" in this table identifies a node and the initial displacement and velocity data for that face The table includes ten "columns", nodeIds pathNames pathIndices displacementsX displacementsY ldisplacementsZ displacementsRx displacementsRy displacementsRz velocitiesX velocitiesY velocitiesZ velocitiesRx velocitiesRy velocitiesRz Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated node. To define or determine the MeshBody associated with any node in the field use the entry in pathIndices corresponding to the node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, nodes 1000 and 1001 belong to "Mesh 1", while nodes 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and displacement and velocity associated with each node in the field, the following code could be used, for index, node_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has an initial displacement in X component', displacementsX[index])
Properties: `displacementsRx`, `displacementsRy`, `displacementsRz`, `displacementsX`, `displacementsY`, `displacementsZ`, `nodeIds`, `pathIndices`, `pathNames`, `velocitiesRx`, `velocitiesRy`, `velocitiesRz`, `velocitiesX`, `velocitiesY`, `velocitiesZ`

Methods:

#### `DFEMFieldInitialDisplacementVelocity(nodeIds: [int], displacementsX: [float], displacementsY: [float], displacementsZ: [float], displacementsRx: [float], displacementsRy: [float], displacementsRz: [float], velocitiesX: [float], velocitiesY: [float], velocitiesZ: [float], velocitiesRx: [float], velocitiesRy: [float], velocitiesRz: [float], pathNames: [str], pathIndices: [int]) -> None`
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

- `getDisplacementsRx() -> [float]` — a list of the displacement values in the rotation X. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `getDisplacementsRy() -> [float]` — a list of the displacement values in the rotation Y. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `getDisplacementsRz() -> [float]` — a list of the displacement values in the rotation Z. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `getDisplacementsX() -> [float]` — a list of the displacement values in the translation X. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `getDisplacementsY() -> [float]` — a list of the displacement values in the translation Y. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `getDisplacementsZ() -> [float]` — a list of the displacement values in the translation Z. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getVelocitiesRx() -> [float]` — a list of the velocity values in rotation X. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `getVelocitiesRy() -> [float]` — a list of the velocity values in rotation Y. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `getVelocitiesRz() -> [float]` — a list of the velocity values in rotation Z. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `getVelocitiesX() -> [float]` — a list of the velocity values in translation X. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `getVelocitiesY() -> [float]` — a list of the velocity values in translation Y. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `getVelocitiesZ() -> [float]` — a list of the velocity values in translation Z. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], displacementsX: [float], displacementsY: [float], displacementsZ: [float], displacementsRx: [float], displacementsRy: [float], displacementsRz: [float], velocitiesX: [float], velocitiesY: [float], velocitiesZ: [float], velocitiesRx: [float], velocitiesRy: [float], velocitiesRz: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Updates the nodeIds.
- `displacementsX` — Updates the displacementsX. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `displacementsY` — Updates the displacementsY. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `displacementsZ` — Updates the displacementsZ. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `displacementsRx` — Updates the displacementsRx. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `displacementsRy` — Updates the displacementsRy. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `displacementsRz` — Updates the displacementsRz. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `velocitiesX` — Updates the velocitiesX. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `velocitiesY` — Updates the velocitiesY. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `velocitiesZ` — Updatez the velocitiesZ. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `velocitiesRx` — Updates the velocitiesRx. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `velocitiesRy` — Updates the velocitiesRy. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `velocitiesRz` — Updatez the velocitiesRz. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `pathNames` — Update the pathNames of this DFEMFieldInitialDisplacementVelocity
- `pathIndices` — Update the pathIndices of this DFEMFieldInitialDisplacementVelocity


## `apex.environment.DFEMFieldInitialStrain`
A class describing a table like data structure defining the spatially varying initial strains across a multiplicity of elements. Each "row" in this table identifies an element and the initial strain data for that face The table includes ten "columns", element1Ids element2Ids pathNames pathIndices ints1 intsN layers1 layersN strains Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "element1Ids" - a list defining the ID of each starting element. Each ID in this list is the starting number. "element2Ids" - a list defining the ID of each end element. Each ID in this list is the end number. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: element1Ids= [ 1000, 2000 , 3000 ], element2Ids = [ 1900, 2900, 3900 ] pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 1, 1 ] In this field, elements 1000 to 1900 belong to "Mesh 1", while elements 2000 to 2900 and 3000 to 3900 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and strain with each Element in the field, the following code could be used, for index, element_id in enumerate(element1Ids): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a strain of', strains[index])
Properties: `element1Ids`, `element2Ids`, `ints1`, `intsN`, `layers1`, `layersN`, `pathIndices`, `pathNames`, `strains`

Methods:

#### `DFEMFieldInitialStrain(element1Ids: [int], element2Ids: [int], ints1: [int], intsN: [int], layers1: [int], layersN: [int], strains: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldInitialStrain in this environment.

- `element1Ids` — A list of integers to define the starting element IDs in the field.
- `element2Ids` — A list of integers to define the end element IDs in the field.
- `ints1` — The number of the first integration point. It can be one integer to indicate that all first integration points is are the same number or a list of integers to define different first integration point numbers.
- `intsN` — The number of the last integration point. It can be either one integer to indicate that all last integration point numbers are the same, or a list of integers to define different last integration point numbers. If omitted, the last integration point numbers are the same with the first integration point numbers.
- `layers1` — The number of the first integration layer. It can be either one integer to indicate that all first integration layer numbers are the same or a list of integers to define different first integration numbers.
- `layersN` — The number of the last integration layer. It can be either one integer to indicate that all last integration number is the same or a list of integers to define different last integration numbers. If omitted, the last layer number is the same with the first layer number.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getElement1Ids() -> [int]` — a list of integers to define the starting element IDs in the field.
- `getElement2Ids() -> [int]` — a list of integers to define the end element IDs in the field.
- `getInts1() -> [int]` — a list of integers to define the first integration point number.
- `getIntsN() -> [int]` — a list of integers to define the last integration point number.
- `getLayers1() -> [int]` — a list of integers to define the first integration layer number.
- `getLayersN() -> [int]` — a list of integers to define the last integration layer number.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getStrains() -> [float]`
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(element1Ids: [int], element2Ids: [int], ints1: [int], intsN: [int], layers1: [int], layersN: [int], strains: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `element1Ids` — Updates the element1Ids.
- `element2Ids` — Updates the element2Ids.
- `ints1` — Updates the ints1.
- `intsN` — Updates the intsN.
- `layers1` — Updates the layers1.
- `layersN` — Updates the layersN.
- `strains` — Update the strains of this DFEMFieldInitialStrain
- `pathNames` — Update the pathNames of this DFEMFieldInitialStrain
- `pathIndices` — Update the pathIndices of this DFEMFieldInitialStrain


## `apex.environment.DFEMFieldInitialStress`
A class describing a table like data structure defining the spatially varying initial stresses across a multiplicity of elements. Each "row" in this table identifies an element and the initial stress data for that face The table includes ten "columns", element1Ids element2Ids pathNames pathIndices ints1 intsN layers1 layersN stresses1 stresses2 stresses3 stresses4 stresses5 stresses6 stresses7 Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "element1Ids" - a list defining the ID of each starting element. Each ID in this list is the starting number. "element2Ids" - a list defining the ID of each end element. Each ID in this list is the end number. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: element1Ids= [ 1000, 2000 , 3000 ], element2Ids = [ 1900, 2900, 3900 ] pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 1, 1 ] In this field, elements 1000 to 1900 belong to "Mesh 1", while elements 2000 to 2900 and 3000 to 3900 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and stress with each Element in the field, the following code could be used, for index, element_id in enumerate(element1Ids): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a X component stress of', stresses1[index])
Properties: `coordinateSystemFlags`, `element1Ids`, `element2Ids`, `ints1`, `intsN`, `layers1`, `layersN`, `pathIndices`, `pathNames`, `stresses1`, `stresses2`, `stresses3`, `stresses4`, `stresses5`, `stresses6`, `stresses7`

Methods:

#### `DFEMFieldInitialStress(element1Ids: [int], element2Ids: [int], ints1: [int], intsN: [int], layers1: [int], layersN: [int], stresses1: [float], stresses2: [float], stresses3: [float], stresses4: [float], stresses5: [float], stresses6: [float], stresses7: [float], coordinateSystemFlags: [int], pathNames: [str], pathIndices: [int]) -> None`
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
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getCoordinateSystemFlags() -> [int]` — a list of integers to indicate the coordinate system that the initial stress is evaluated. It only accepts 0 (basic coordinate system) or -1 (element coordinate system).
- `getElement1Ids() -> [int]` — a list of integers to define the starting element IDs in the field.
- `getElement2Ids() -> [int]` — a list of integers to define the end element IDs in the field.
- `getInts1() -> [int]` — a list of the first integration point number.
- `getIntsN() -> [int]` — a list of the last integration point number.
- `getLayers1() -> [int]` — a list of the first integration layer number.
- `getLayersN() -> [int]` — a list of the last integration layer number.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getStresses1() -> [float]` — a list of the stress values of the first component.
- `getStresses2() -> [float]` — a list of the stress values of the second component.
- `getStresses3() -> [float]` — a list of the stress values of the third component.
- `getStresses4() -> [float]` — a list of the stress values of the fourth component.
- `getStresses5() -> [float]` — a list of the stress values of the fifth component.
- `getStresses6() -> [float]` — a list of the stress values of the sixth component.
- `getStresses7() -> [float]` — a list of the stress values of the seventh component.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(element1Ids: [int], element2Ids: [int], ints1: [int], intsN: [int], layers1: [int], layersN: [int], stresses1: [float], stresses2: [float], stresses3: [float], stresses4: [float], stresses5: [float], stresses6: [float], stresses7: [float], coordinateSystemFlags: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the initial stress. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `element1Ids` — Updates the element1Ids.
- `element2Ids` — Updates the element2Ids.
- `ints1` — Updates the ints1.
- `intsN` — Updates the intsN.
- `layers1` — Updates the layers1.
- `layersN` — Updates the layersN.
- `stresses1` — Updates the stresses1.
- `stresses2` — Updates the stresses2.
- `stresses3` — Updates the stresses3.
- `stresses4` — Updates the stresses4.
- `stresses5` — Updates the stresses5.
- `stresses6` — Updates the stresses6.
- `stresses7` — Updates the stresses7.
- `coordinateSystemFlags` — Updates the coordinateSystemFlags.
- `pathNames` — Update the pathNames of this DFEMFieldInitialStress
- `pathIndices` — Update the pathIndices of this DFEMFieldInitialStress


## `apex.environment.DFEMFieldLoadAreaFactor`
A class describing a table like data structure defining the spatially varying load area factor across a multiplicity of nodes. Each "row" in this table identifies a node and the load area factor data on that node. The table includes the following "columns", nodeIds pathNames pathIndices scaleFactorsX scaleFactorsY scaleFactorsZ scaleFactorsRx scaleFactorsRy scaleFactorsRz Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and load area factor in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a load area factor in X component of', scaleFactorsX[index]).
Properties: `nodeIds`, `pathIndices`, `pathNames`, `scaleFactorsRx`, `scaleFactorsRy`, `scaleFactorsRz`, `scaleFactorsX`, `scaleFactorsY`, `scaleFactorsZ`

Methods:

#### `DFEMFieldLoadAreaFactor(nodeIds: [int], scaleFactorsX: [float], scaleFactorsY: [float], scaleFactorsZ: [float], scaleFactorsRx: [float], scaleFactorsRy: [float], scaleFactorsRz: [float], pathNames: [str], pathIndices: [int]) -> None`
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

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getScaleFactorsRx() -> [float]` — a list of the load scale(area) factors in the rotation X axis, scaleFactorRx is a Moment quantity and must be defined using the units of Moment from the active script unit system.If all load scale factors are the same, the list should only contain one float value.
- `getScaleFactorsRy() -> [float]` — a list of the load scale(area) factors in the rotation Y axis, scaleFactorRy is a Moment quantity and must be defined using the units of Moment from the active script unit system. If all load scale factors are the same, the list should only contain one float value.
- `getScaleFactorsRz() -> [float]` — a list of the load scale(area) factors in the rotation Z axis, scaleFactorRz is a Moment quantity and must be defined using the units of Moment from the active script unit system. If all load scale factors are the same, the list should only contain one float value.
- `getScaleFactorsX() -> [float]` — a list of the load scale(area) factors in the translation X axis, scaleFactorsX is a Force quantity and must be defined using the units of Force from the active script unit system. If all load scale factors are the same, the list should only contain one float value.
- `getScaleFactorsY() -> [float]` — a list of the load scale(area) factors in the translation Y axis, scaleFactorsY is a Force quantity and must be defined using the units of Force from the active script unit system. If all load scale factors are the same, the list should only contain one float value.
- `getScaleFactorsZ() -> [float]` — a list of the load scale(area) factors in the translation Z axis, scaleFactorZ is a Force quantity and must be defined using the units of Force from the active script unit system. If all load scale factors are the same, the list should only contain one float value.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], scaleFactorsX: [float], scaleFactorsY: [float], scaleFactorsZ: [float], scaleFactorsRx: [float], scaleFactorsRy: [float], scaleFactorsRz: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `scaleFactorsX` — Update the scaleFactorsX.
- `scaleFactorsY` — Update the scaleFactorsY.
- `scaleFactorsZ` — Update the scaleFactorsZ.
- `scaleFactorsRx` — Update the scaleFactorsRx.
- `scaleFactorsRy` — Update the scaleFactorsRy.
- `scaleFactorsRz` — Update the scaleFactorsRz.
- `pathNames` — Update the pathNames of this DFEMFieldLoadAreaFactor
- `pathIndices` — Update the pathIndices of this DFEMFieldLoadAreaFactor


## `apex.environment.DFEMFieldLoadDistributed`
A class describing a table like data structure defining the spatially varying distributed load magnitude across a multiplicity of elements/element faces. Each "row" in this table identifies an element or element face and the load data for that face The table includes ten "columns", elementIds, pathIndices pressuresP1 pressuresP2 pressuresP3 pressuresP4 nodesP1 nodesP2 nodesP3 nodesP4 directionsX directionsY directionsZ orientations Pressure values for the first corner MUST be defined and will be used for all other corners if they are omitted. Defining only values for the first corner of each element/face enables creation of an "Element Uniform" pressure distribution where the pressure varies across different elements but is constant within a single element. Providing values for the second, third and fourth corners enables definition of a pressure that varies not only across different elements but also varies within a single element. The fourth corner values are silently ignored if the element/face is triangular and has just three corner nodes. Directions defines the pressure direction relative to the coordinate systems in orientations. Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and first corner pressure associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a first corner pressure of', pressuresCorner1[index])
Properties: `directionsX`, `directionsY`, `directionsZ`, `elementIds`, `inputType`, `node1Ids`, `node2Ids`, `node3Ids`, `node4Ids`, `orientations`, `pathIndices`, `pathNames`, `pressuresCorner1`, `pressuresCorner2`, `pressuresCorner3`, `pressuresCorner4`

Methods:

#### `DFEMFieldLoadDistributed(elementIds: [int], pressuresCorner1: [float], pressuresCorner2: [float], pressuresCorner3: [float], pressuresCorner4: [float], orientations: [int], directionsX: [float], directionsY: [float], directionsZ: [float], node1Ids: [int], node2Ids: [int], node3Ids: [int], node4Ids: [int], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
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
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only pressure is necessary and it is automatically applied to pressureCorner2, pressureCorner3 and pressureCorner4. If the inputType is element variable, pressure is the applied to corner1 and other three corners must be defined as well.

- `getDirectionsX() -> [float]` — the X components of the direction vectors.
- `getDirectionsY() -> [float]` — the Y components of the direction vectors.
- `getDirectionsZ() -> [float]` — the Z components of the direction vectors.
- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only pressuresCorner1 is necessary and it is automatically applied to other corners so that the distributed pressure is uniform on a single element. If the inputType is element variable, the pressures on all corners are necessary so that the distributed pressure can be variable on a single element.
- `getNode1Ids() -> [int]`
- `getNode2Ids() -> [int]`
- `getNode3Ids() -> [int]`
- `getNode4Ids() -> [int]`
- `getOrientations() -> [int]` — a list of orientations for the direction components.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPressuresCorner1() -> [float]` — a list of pressures at the first corner. If the inputType is element uniform, it is the pressure on the whole element. If the inputType is variable, it is the pressure at the first corner.
- `getPressuresCorner2() -> [float]` — a list of pressure pressure values at the second corner.
- `getPressuresCorner3() -> [float]` — a list of pressure values at the third corner.
- `getPressuresCorner4() -> [float]` — a list of pressure values at the fourth corner.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], pressuresCorner1: [float], pressuresCorner2: [float], pressuresCorner3: [float], pressuresCorner4: [float], orientations: [int], directionsX: [float], directionsY: [float], directionsZ: [float], node1Ids: [int], node2Ids: [int], node3Ids: [int], node4Ids: [int], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Updates the elementIds.
- `pressuresCorner1` — Updates the pressuresCorner1.
- `pressuresCorner2` — Updates the pressuresCorner2.
- `pressuresCorner3` — Updates the pressuresCorner3.
- `pressuresCorner4` — Updates the pressuresCorner4.
- `orientations` — Updates the orientations.
- `directionsX` — Updates the directionsX.
- `directionsY` — Updates the directionsY.
- `directionsZ` — Updates the directionsZ.
- `node1Ids` — Update the node1Ids of this DFEMFieldLoadDistributed
- `node2Ids` — Update the node2Ids of this DFEMFieldLoadDistributed
- `node3Ids` — Update the node3Ids of this DFEMFieldLoadDistributed
- `node4Ids` — Update the node4Ids of this DFEMFieldLoadDistributed
- `pathNames` — Update the pathNames of this DFEMFieldLoadDistributed
- `pathIndices` — Update the pathIndices of this DFEMFieldLoadDistributed
- `inputType` — Updates the inputType.


## `apex.environment.DFEMFieldLoadDistributedBeam2`
A class describing a table like data structure defining the spatially varying load magnitude across a multiplicity of elements. Each "row" in this table identifies an element or element face and the load data for that face The table includes ten "columns", elementIds loadTypes scaleTypes distancesX1 loadFactorsX1 distancesX2 loadFactorsX2 pathNames pathIndices inputType Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and load associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a distributed load of', distancesX1[index])
Properties: `distancesX1`, `distancesX2`, `elementIds`, `inputType`, `loadFactorsX1`, `loadFactorsX2`, `loadTypes`, `pathIndices`, `pathNames`, `scaleTypes`

Methods:

#### `DFEMFieldLoadDistributedBeam2(elementIds: [int], loadTypes: [apex.attribute.LoadTypeDistributedBeam2], scaleTypes: [apex.attribute.ScaleTypeDistributedBeam2], distancesX1: [float], loadFactorsX1: [float], distancesX2: [float], loadFactorsX2: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
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

- `getDistancesX1() -> [float]` — the distances X1 along element axis from end A. The distance may be a fractional value of the element length or a length value, depending on the scaleTypes.
- `getDistancesX2() -> [float]` — the distances X2 along element axis from end A. The distance may be a fractional value of the element length or a length value, depending on the scaleTypes.
- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getInputType() -> apex.attribute.InputType` — the optional argument to define the load distribution on a single element. If the inputType is element uniform, the loadFactorX2 is always equal to loa dFactorX1, distanceX1 is 0.0, distanceX2 is 1.0, scaleType is fractional. If omitted, the default value is element uniform.
- `getLoadFactorsX1() -> [float]` — a list of the load factors at the position of distance X1 from end A. The unit of the load factor value depends on the loadTypes, it can be a force or a moment.
- `getLoadFactorsX2() -> [float]` — a list of the load factors at the position of distance X2 from end A. The unit of the load factor value depends on the loadTypes, it can be a force or a moment.
- `getLoadTypes() -> [apex.attribute.LoadTypeDistributedBeam2]` — a list of the loadTypes of the beam distributed load applied to beam element with two nodes. apex.attribute.LoadTypeBeam2.ForceX, the load is concentrated force in X direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceY, the load is concentrated force in Y direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceZ, the load is concentrated force in Z direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentX, the load is moment in X direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentY, the load is moment in Y direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentZ, the load is moment in Z direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceXE, the load is concentrated force in X direction of the element coordinate system. apex.attribute.LoadTypeBeam2.ForceYE, the load is concentrated force in Y direction of the element coordinate system. apex.attribute.LoadTypeBeam2.ForceZE, the load is concentrated force in Z direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentXE, the load is moment in X direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentYE, the load is moment in Y direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentZE, the load is moment in Z direction of the element coordinate system.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getScaleTypes() -> [apex.attribute.ScaleTypeDistributedBeam2]` — a list of the scaleTypes of the load factors. apex.attribute.ScaleTypeBeam.Length, the distance values are actual distances along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeam.Fractional, the distance values are are ratios of the distance along the axis to the total length, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeam.LengthProjected, the distance values are projected lengths along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeam.FractionalProjected, the distance values are ratios of the actual distance to the length of the bar (CBAR entry), and if distance1 != distance 2, then the distributed load is specified in terms of the projected length of the bar.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], loadTypes: [apex.attribute.LoadTypeDistributedBeam2], scaleTypes: [apex.attribute.ScaleTypeDistributedBeam2], distancesX1: [float], loadFactorsX1: [float], distancesX2: [float], loadFactorsX2: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Updates the elementIds.
- `loadTypes` — Updates the loadTypes.
- `scaleTypes` — Updates the scaleTypes.
- `distancesX1` — Updates the distancesX1. The distance may be a fractional value of the element length or a length value, depending on the scaleTypes.
- `loadFactorsX1` — Updates the loadFactorsX1. The unit of the load factor value depends on the loadTypes, it can be a force or a moment.
- `distancesX2` — Updates the distancesX. The distance may be a fractional value of the element length or a length value, depending on the scaleTypes.
- `loadFactorsX2` — Updates the loadFactorsX1. The unit of the load factor value depends on the loadTypes, it can be a force or a moment.
- `pathNames` — Update the pathNames of this DFEMFieldLoadDistributedBeam2
- `pathIndices` — Update the pathIndices of this DFEMFieldLoadDistributedBeam2
- `inputType` — Updates the inputType.


## `apex.environment.DFEMFieldLoadDistributedBeam3`
A class describing a table like data structure defining the spatially varying load across a multiplicity of 1D elements. Each "row" in this table identifies an element and the load data for that element. The table includes ten "columns", elementIds loadTypes scaleTypes distancesX1 loadFactorsX1 distancesX2 loadFactorsX2 pathNames pathIndices Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and load associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a distributed load of', distancesX1[index])
Properties: `elementIds`, `inputType`, `loadScaleFactors`, `loadTypes`, `loadVectorsX`, `loadVectorsY`, `loadVectorsZ`, `magnitudesEndA`, `magnitudesEndB`, `magnitudesMidC`, `orientations`, `pathIndices`, `pathNames`

Methods:

#### `DFEMFieldLoadDistributedBeam3(elementIds: [int], orientations: [int], loadVectorsX: [float], loadVectorsY: [float], loadVectorsZ: [float], loadTypes: [apex.attribute.LoadTypeDistributedBeam3], loadScaleFactors: [float], magnitudesEndA: [float], magnitudesEndB: [float], magnitudesMidC: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Create DFEMFieldLoadDistributedBeam3 in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
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

- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, the loadScaleFactor is 1.0, magnitudes on end A, end B and mid C are 1.0. If the inputType is element variable, above parameters are defined by user.
- `getLoadScaleFactors() -> [float]` — a list of values to define the load scale factors.
- `getLoadTypes() -> [apex.attribute.LoadTypeDistributedBeam3]` — the loadTypes of the load. Each load can be different load types for associated element.
- `getLoadVectorsX() -> [float]` — a list of values to define the X components of the load vectors. The unit can be Force or Moment quantity(depending on loadTypes), which is defined by the units of Force/Moment from the active script unit system.
- `getLoadVectorsY() -> [float]` — a list of values to define the Y components of the load vectors. The unit can be Force or Moment quantity(depending on loadTypes), which is defined by the units of Force/Moment from the active script unit system.
- `getLoadVectorsZ() -> [float]` — a list of values to define the Z components of the load vectors. The unit can be Force or Moment quantity(depending on loadTypes), which is defined by the units of Force/Moment from the active script unit system.
- `getMagnitudesEndA() -> [float]` — the load magnitudes at end A.
- `getMagnitudesEndB() -> [float]` — the load magnitudes at end B.
- `getMagnitudesMidC() -> [float]` — the load magnitude at the point C.
- `getOrientations() -> [int]`
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames
- `getPathNames() -> [str]` — the full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], orientations: [int], loadVectorsX: [float], loadVectorsY: [float], loadVectorsZ: [float], loadTypes: [apex.attribute.LoadTypeDistributedBeam3], loadScaleFactors: [float], magnitudesEndA: [float], magnitudesEndB: [float], magnitudesMidC: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Updates the elementIds.
- `orientations` — Update the orientations of this DFEMFieldLoadDistributedBeam3
- `loadVectorsX` — Updates the loadVectorsX. The unit can be Force or Moment quantity(depending on loadTypes), which is defined by the units of Force/Moment from the active script unit system.
- `loadVectorsY` — Updates the loadVectorsY. The unit can be Force or Moment quantity(depending on loadTypes), which is defined by the units of Force/Moment from the active script unit system.
- `loadVectorsZ` — Updates the loadVectorsZ. The unit can be Force or Moment quantity(depending on loadTypes), which is defined by the units of Force/Moment from the active script unit system.
- `loadTypes` — Updates the loadTypes.
- `loadScaleFactors` — Updates the loadScaleFactors.
- `magnitudesEndA` — Updates the magnitudesEndA.
- `magnitudesEndB` — Updates the magnitudesEndB.
- `magnitudesMidC` — Updates the magnitudesMidC.
- `pathNames` — Updates the pathNames.
- `pathIndices` — Updates the pathIndices .
- `inputType` — Updates the inputType.


## `apex.environment.DFEMFieldMomentComponent`
A class describing a table like data structure defining the spatially varying moment across a multiplicity of nodes. Each "row" in this table identifies a node and the moment data on that node. The table includes the following "columns", nodeIds pathNames pathIndices orientations scaleFactors momentsX momentsY momentsZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and moment in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a moment in X component of', momentsX[index]).
Properties: `momentsX`, `momentsY`, `momentsZ`, `nodeIds`, `orientations`, `pathIndices`, `pathNames`, `scaleFactors`

Methods:

#### `DFEMFieldMomentComponent(nodeIds: [int], orientations: [int], scaleFactors: [float], momentsX: [float], momentsY: [float], momentsZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldMomentComponent in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `orientations` — An optional orientation. It can be either an IOrientation object which only accepts a coordinate system object or a list of IOrientation objects. If omitted, the components are defined in the basic coordinate system.
- `scaleFactors` — An optional scale factor. It can be either a float value or a list of float. If omitted,the scale factor is 1.0.
- `momentsX` — A list of moment component values in X axis.
- `momentsY` — A list of moment component values in Y axis.
- `momentsZ` — A list of moment component values in Z axis.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getMomentsX() -> [float]` — a list to define the X component values. If all component values are the same, the list should only contain one float value. momentsX is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getMomentsY() -> [float]` — a list to define the Y component values. If all component values are the same, the list should only contain one float value. momentsY is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getMomentsZ() -> [float]` — a list to define the Z component values. If all component values are the same, the list should only contain one float value. momentsZ is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getOrientations() -> [int]` — an optional list of orientations for the load components. Each item in the list must be an id of a coordinate system. If all load components use the same orientation, the list must contain only one integer that points to the id of the coordinate system. If omitted, all load components are defined in the basic coordinate system.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getScaleFactors() -> [float]` — an optional list of scale factors for the loads. If all loads in the field have the same scale factor, the list must contain only one float value. If omitted, the default value is 1.0 for all loads.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], orientations: [int], scaleFactors: [float], momentsX: [float], momentsY: [float], momentsZ: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Updates the nodeIds.
- `orientations` — Updates the orientations.
- `scaleFactors` — Updates the scaleFactors.
- `momentsX` — Updates the momentsX.
- `momentsY` — Updates the momentsY.
- `momentsZ` — Updates the momentsZ.
- `pathNames` — Update the pathNames of this DFEMFieldMomentComponent
- `pathIndices` — Update the pathIndices of this DFEMFieldMomentComponent


## `apex.environment.DFEMFieldMomentFollowerNormal`
A class describing a table like data structure defining the spatially varying moment across a multiplicity of nodes. Each "row" in this table identifies a node and the moment data on that node. The table includes the following "columns", nodeIds pathNames pathIndices momentMagnitudes points1 points2 points3 points4 Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and moment associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a moment magnitude of', momentsMagnitude[index]).
Properties: `momentMagnitudes`, `nodeIds`, `pathIndices`, `pathNames`, `points1`, `points2`, `points3`, `points4`

Methods:

#### `DFEMFieldMomentFollowerNormal(nodeIds: [int], momentMagnitudes: [float], points1: [int], points2: [int], points3: [int], points4: [int], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldMomentFollowerComponent in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `momentMagnitudes` — A list of moment magnitude.
- `points1` — The starting point of the first vector. It can be either a point or a list of points.
- `points2` — The end point of the first vector. It can be either a point or a list of points.
- `points3` — The starting point of the second vector. It can be either a point or a list of points.
- `points4` — The end point of the second vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getMomentMagnitudes() -> [float]` — a list to define the moment magnitudes. Each moment direction is parallel to the cross product of two vectors defined by four points. If all moment magnitudes are the same, the list should only contain one float value. momentMagnitudes is a Moment quantity and is defined using the units of Force from the active script unit system.
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPoints1() -> [int]` — a list of starting points of the direction vectors. Each item in the list must be a node or a vertex. If all starting points are the same, the list should only contain one node or vertex.
- `getPoints2() -> [int]` — a list of end points of the direction vectors. Each item in the list must be a node or a vertex. If all end points are the same, the list should only contain one node or vertex.
- `getPoints3() -> [int]` — a list of starting points of the direction vectors. Each item in the list must be a node or a vertex. If all starting points are the same, the list should only contain one node or vertex.
- `getPoints4() -> [int]` — a list of end points of the direction vectors. Each item in the list must be a node or a vertex. If all starting points are the same, the list should only contain one node or vertex.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], momentMagnitudes: [float], points1: [int], points2: [int], points3: [int], points4: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `momentMagnitudes` — Updates the momentMagnitudes. momentMagnitudes is a Moment quantity and is defined using the units of Force from the active script unit system.
- `points1` — Update the points1.
- `points2` — Update the points2.
- `points3` — Update the points3.
- `points4` — Update the points4.
- `pathNames` — Update the pathNames of this DFEMFieldMomentFollowerNormal
- `pathIndices` — Update the pathIndices of this DFEMFieldMomentFollowerNormal


## `apex.environment.DFEMFieldMomentFollowerVector`
A class describing a table like data structure defining the spatially varying moment across a multiplicity of nodes. Each "row" in this table identifies a node and the moment data on that node. The table includes the following "columns", nodeIds pathNames pathIndices momentMagnitudes points1 points2 Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and moment associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a moment magnitude of', momentsMagnitude[index]).
Properties: `momentMagnitudes`, `nodeIds`, `pathIndices`, `pathNames`, `points1`, `points2`

Methods:

#### `DFEMFieldMomentFollowerVector(nodeIds: [int], momentMagnitudes: [float], points1: [int], points2: [int], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldMomentFollowerVector in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `momentMagnitudes` — A list of moment magnitudes.
- `points1` — the starting point of the load vector. It can be either a point or a list points.
- `points2` — the end point of the load vector. It can be either a point or a list of points.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getMomentMagnitudes() -> [float]` — a list to define the moment magnitudes, each moment direction is defined by the vector from point1 to point2. If all moment magnitudes are the same, the list should only contain one float value. momentMagnitudes is a Moment quantity and must be defined using the units of Moment from the active script unit system
- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPoints1() -> [int]` — a list of starting points of the direction vectors. Each item in the list must be a node or a vertex. If all starting points is the same, then the list contains one node or vertex.
- `getPoints2() -> [int]` — a list of end points of the direction vectors. Each item in the list must be a node or a vertex. If all end points is the same, then the list contains one node or vertex.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], momentMagnitudes: [float], points1: [int], points2: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Updates the nodeIds.
- `momentMagnitudes` — Updates the momentMagnitudes. momentMagnitudes is a Moment quantity and must be defined using the units of Moment from the active script unit system
- `points1` — Updates the points1.
- `points2` — Updates the points2.
- `pathNames` — Update the pathNames of this DFEMFieldMomentFollowerVector
- `pathIndices` — Update the pathIndices of this DFEMFieldMomentFollowerVector


## `apex.environment.DFEMFieldPhaseLead`
A class describing a table like data structure defining the spatially varying phase lead across a multiplicity of nodes. Each "row" in this table identifies a node and the phase lead data for that node. The table includes ten "columns", nodeIds, pathNames pathIndices phaseLeadsX phaseLeadsY phaseLeadsZ phaseLeadsRx phaseLeadsRy phaseLeadsRz The phase leads may be blank but at least one should be defined for each associated node. Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated node. To define or determine the MeshBody associated with any node in the field use the entry in pathIndices corresponding to the node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, nodes 1000 and 1001 belong to "Mesh 1", while nodes 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and phase lead associated with each node in the field, the following code could be used, for index, node_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a time delay of ', phaseLeadsX[index], "in translation X degree of freedom")
Properties: `nodeIds`, `pathIndices`, `pathNames`, `phaseLeadsRx`, `phaseLeadsRy`, `phaseLeadsRz`, `phaseLeadsX`, `phaseLeadsY`, `phaseLeadsZ`

Methods:

#### `DFEMFieldPhaseLead(nodeIds: [int], phaseLeadsX: [float], phaseLeadsY: [float], phaseLeadsZ: [float], phaseLeadsRx: [float], phaseLeadsRy: [float], phaseLeadsRz: [float], pathNames: [str], pathIndices: [int]) -> None`
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

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPhaseLeadsRx() -> [float]` — a list of the phase lead values in the rotation X component.
- `getPhaseLeadsRy() -> [float]` — a list of the phase lead values in the rotation Y component.
- `getPhaseLeadsRz() -> [float]` — a list of the phase lead values in the rotation Z component.
- `getPhaseLeadsX() -> [float]` — a list of the phase lead values in the X component.
- `getPhaseLeadsY() -> [float]` — a list of the phase lead values in the Y component.
- `getPhaseLeadsZ() -> [float]` — a list of the phase lead values in the component.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], phaseLeadsX: [float], phaseLeadsY: [float], phaseLeadsZ: [float], phaseLeadsRx: [float], phaseLeadsRy: [float], phaseLeadsRz: [float], pathNames: [str], pathIndices: [int]) -> None`
Update method. One or more properties may be updated in each call to update().

- `nodeIds` — Update the nodeIds.
- `phaseLeadsX` — Update the phaseLeadsX.
- `phaseLeadsY` — Update the phaseLeadsY.
- `phaseLeadsZ` — Update the phaseLeadsZ.
- `phaseLeadsRx` — Update the phaseLeadsRx.
- `phaseLeadsRy` — Update the phaseLeadsRy.
- `phaseLeadsRz` — Update the phaseLeadsRz.
- `pathNames` — Update the pathNames of this DFEMFieldPhaseLead
- `pathIndices` — Update the pathIndices of this DFEMFieldPhaseLead


## `apex.environment.DFEMFieldPressure`
A class describing a table like data structure defining the spatially varying pressure magnitude across a multiplicity of elements/element faces. Each "row" in this table identifies an element or element face and the pressure data for that face The table includes ten "columns", elementIds, pathIndices pressuresP1 pressuresP2 pressuresP3 pressuresP4 nodesP1 nodesP2 nodesP3 nodesP4 Pressure values for the first corner MUST be defined and will be used for all other corners if they are omitted. Defining only values for the first corner of each element/face enables creation of an "Element Uniform" pressure distribution where the pressure varies across different elements but is constant within a single element. Providing values for the second, third and fourth corners enables definition of a pressure that varies not only across different elements but also varies within a single element. The fourth corner values are silently ignored if the element/face is triangular and has just three corner nodes. Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and first corner pressure associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a first corner pressure of', pressuresCorner1[index])
Properties: `elementIds`, `inputType`, `node1Ids`, `node2Ids`, `node3Ids`, `node4Ids`, `pathIndices`, `pathNames`, `pressuresCorner1`, `pressuresCorner2`, `pressuresCorner3`, `pressuresCorner4`

Methods:

#### `DFEMFieldPressure(elementIds: [int], pressuresCorner1: [float], pressuresCorner2: [float], pressuresCorner3: [float], pressuresCorner4: [float], node1Ids: [int], node2Ids: [int], node3Ids: [int], node4Ids: [int], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Create DFEMFieldPressure in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `pressuresCorner1` — A list of pressure values. If the inputType is element uniform, each pressure is defined on the whole element. If the inputType is element variable, each pressure is defined on the first corner of each element.
- `pressuresCorner2` — A list of pressure values defined on the second corner of each target element.
- `pressuresCorner3` — A list of pressure values defined on the third corner of each target element.
- `pressuresCorner4` — A list of pressure values defined on the fourth corner of each target element.
- `pathNames` — The full pathName of the target elements. It can be one string to indicate that all elements belong to one part or a list of strings to define different pathNames for each target element.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.
- `inputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only pressure is necessary and it is automatically applied to pressureCorner2, pressureCorner3 and pressureCorner4. If the inputType is element variable, pressure is the applied to corner1 and other three corners must be defined as well.

- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only "pressures" is necessary and it is automatically applied to other corners so that the pressure is uniform on a single element. If the inputType is element variable, the pressures on all corners are necessary so that the pressure can be variable on a single element.
- `getNode1Ids() -> [int]`
- `getNode2Ids() -> [int]`
- `getNode3Ids() -> [int]`
- `getNode4Ids() -> [int]`
- `getPathIndices() -> [int]` — Missing.
- `getPathNames() -> [str]` — Missing.
- `getPressuresCorner1() -> [float]`
- `getPressuresCorner2() -> [float]`
- `getPressuresCorner3() -> [float]`
- `getPressuresCorner4() -> [float]`
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], pressuresCorner1: [float], pressuresCorner2: [float], pressuresCorner3: [float], pressuresCorner4: [float], node1Ids: [int], node2Ids: [int], node3Ids: [int], node4Ids: [int], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Updates the elementIds.
- `pressuresCorner1` — Updates the pressuresCorner1.
- `pressuresCorner2` — Updates the pressuresCorner2.
- `pressuresCorner3` — Updates the pressuresCorner3.
- `pressuresCorner4` — Updates the pressuresCorner4.
- `node1Ids` — Update the node1Ids of this DFEMFieldPressure
- `node2Ids` — Update the node2Ids of this DFEMFieldPressure
- `node3Ids` — Update the node3Ids of this DFEMFieldPressure
- `node4Ids` — Update the node4Ids of this DFEMFieldPressure
- `pathNames` — Update the pathNames of this DFEMFieldPressure
- `pathIndices` — Update the pathIndices of this DFEMFieldPressure
- `inputType` — Updates the inputType.


## `apex.environment.DFEMFieldPressure2D`
A class describing a table like data structure defining the spatially varying pressure across a multiplicity of elements. Each "row" in this table identifies a element and the pressure data on that element. The table includes the following "columns", pathNames pathIndices elementIds pressuresMagnitude Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds " - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in the list of vertices is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with an Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and pressure associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', elementIds[index], 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a pressure of', pressuresMagnitude[index]).
Properties: `elementIds`, `pathIndices`, `pathNames`, `pressureMagnitudes`

Methods:

- `DFEMFieldPressure2D(pressureMagnitudes: [float], elementIds: [int], pathNames: [str], pathIndices: [int]) -> None`
- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPressureMagnitudes() -> [float]` — a list of pressure magnitudes. It is a Pressure quantity and is defined using the units of Pressure from the active script unit system. Each pressure direction is perpendicular to the element.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(pressureMagnitudes: [float], elementIds: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `pressureMagnitudes` — Update the pressureMagnitudes. It is a Pressure quantity and is defined using the units of Pressure from the active script unit system.
- `elementIds` — Update the elementIds.
- `pathNames` — Update the pathNames of this DFEMFieldPressure2D
- `pathIndices` — Update the pathIndices of this DFEMFieldPressure2D


## `apex.environment.DFEMFieldPressureArea`
A class describing a table like data structure defining the spatially varying pressure across a multiplicity of face areas. Each "row" in this table identifies a node and the pressure data on that node. The table includes the following "columns", pathNames pathIndices pressuresMagnitude vertices1 vertices2 vertices3 vertices4 Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "vertices1 " - a list defining the ID of every first node in the field. "vertices2 " - a list defining the ID of every second node in the field. "vertices3 " - a list defining the ID of every third node in the field. "vertices4 " - a list defining the ID of every fourth node in the field. "pathNames" - a list of unique pathNames. Every node in the list of vertices is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'vertices1'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: vertices1=[ 1, 5, 9, ], vertices2=[ 2, 6, 10 ], vertices3=[ 3, 7, 11 ], vertices4=[ 4, 8, 12, ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 1, 1 ] In this field, nodes 1,2,3,4 belong to "Mesh 1", while all other nodes belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and pressure associated with each Node in the field, the following code could be used, for index, element_id in enumerate(vertices): print('Node with ID', vertices1[index], 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a pressure of', pressuresMagnitude[index]).
Properties: `pathIndices`, `pathNames`, `pressureMagnitudes`, `vertices1`, `vertices2`, `vertices3`, `vertices4`

Methods:

#### `DFEMFieldPressureArea(pressureMagnitudes: [float], vertices1: [int], vertices2: [int], vertices3: [int], vertices4: [int], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldPressureArea in this environment.

- `pressureMagnitudes` — A list of floats to define the pressure values.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getPressureMagnitudes() -> [float]` — a list of pressure magnitudes. The magnitude is a Pressure quantity and is defined using the units of Pressure from the active script unit system.
- `getVertices1() -> [int]`
- `getVertices2() -> [int]`
- `getVertices3() -> [int]`
- `getVertices4() -> [int]`
#### `removeTargets(ids: [[int]]) -> None`
Remove the target nodes from the field.

- `ids` — A list of lists to identify the target node ids to be removed from the field. Each list must be 3 or 4 node ids.

#### `update(pressureMagnitudes: [float], vertices1: [int], vertices2: [int], vertices3: [int], vertices4: [int], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `pressureMagnitudes` — Updates the pressureMagnitudes. pressureMagnitude is a Pressure quantity and is defined using the units of Pressure from the active script unit system.
- `vertices1` — Updates the vertices1.
- `vertices2` — Updates the vertices2.
- `vertices3` — Updates the vertices3.
- `vertices4` — Updates the vertices4.
- `pathNames` — Update the pathNames of this DFEMFieldPressureArea
- `pathIndices` — Update the pathIndices of this DFEMFieldPressureArea


## `apex.environment.DFEMFieldSupportFreeBody`
A class describing a table like data structure defining the spatially varying support across a multiplicity of nodes. Each "row" in this table identifies a node and the support data on that node. The table includes the following "columns", nodeIds pathNames pathIndices orientations constrainTranslationX constrainTranslationY constrainTranslationZ constrainRotationX constrainRotationY constrainRotationZ Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every Node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Node. To define or determine the MeshBody associated with a Node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] There are two mesh bodies with same nodes ids in two different parts. The pathNames is used to identify which mesh body is associated with the node. The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and constraint in X component associated with each Node in the field, the following code could be used, for index, element_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a support in translation X is ', constrainTranslationX[index]).
Properties: `constrainRotationX`, `constrainRotationY`, `constrainRotationZ`, `constrainTranslationX`, `constrainTranslationY`, `constrainTranslationZ`, `nodeIds`, `orientations`, `pathIndices`, `pathNames`

Methods:

#### `DFEMFieldSupportFreeBody(nodeIds: [int], orientations: [int], constrainTranslationX: [bool], constrainTranslationY: [bool], constrainTranslationZ: [bool], constrainRotationX: [bool], constrainRotationY: [bool], constrainRotationZ: [bool], pathNames: [str], pathIndices: [int]) -> None`
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

- `getConstrainRotationX() -> [bool]` — a list of booleans to indicate the whether the rotation X is constrained or not for each node in the field. For example, constrainRotationX = [False, True, True, False].
- `getConstrainRotationY() -> [bool]` — a list of booleans to indicate the whether the rotation Y is constrained or not for each node in the field. For example, constrainRotationY = [False, True, True, False].
- `getConstrainRotationZ() -> [bool]` — a list of booleans to indicate the whether the rotation Z is constrained or not for each node in the field. For example, constrainRotationZ = [False, True, True, False].
- `getConstrainTranslationX() -> [bool]` — a list of booleans to indicate the whether the translation X is constrained or not for each node in the field. For example, constrainTranslationX = [False, True, True, False].
- `getConstrainTranslationY() -> [bool]` — a list of booleans to indicate the whether the translation Y is constrained or not for each node in the field. For example, constrainTranslationY = [False, True, True, False].
- `getConstrainTranslationZ() -> [bool]` — a list of booleans to indicate the whether the translation Z is constrained or not for each node in the field. For example, constrainTranslationZ = [False, True, True, False].
- `getNodeIds() -> [int]` — a list of integers to indicate the target nodes in the field.
- `getOrientations() -> [int]` — a list of the orientations of the constraint. Currently it must be a coordinate system
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], orientations: [int], constrainTranslationX: [bool], constrainTranslationY: [bool], constrainTranslationZ: [bool], constrainRotationX: [bool], constrainRotationY: [bool], constrainRotationZ: [bool], pathNames: [str], pathIndices: [int]) -> None`
Update this ConstraintGeneral. One or more properties may be updated in each call to update().

- `nodeIds` — Update the nodeIds.
- `orientations` — Update the orientations.
- `constrainTranslationX` — Update the constrainTranslationX.
- `constrainTranslationY` — Update the constrainTranslationY.
- `constrainTranslationZ` — Update the constrainTranslationZ.
- `constrainRotationX` — Update the constrainRotationX of this DFEMFieldSupportFreeBody
- `constrainRotationY` — Update the constrainRotationY of this DFEMFieldSupportFreeBody
- `constrainRotationZ` — Update the constrainRotationZ of this DFEMFieldSupportFreeBody
- `pathNames` — Update the pathNames of this DFEMFieldSupportFreeBody
- `pathIndices` — Update the pathIndices of this DFEMFieldSupportFreeBody


## `apex.environment.DFEMFieldTemperatureGradient2D`
A class describing a table like data structure defining the spatially varying temperatures across a multiplicity of elements. Each "row" in this table identifies an element and the temperature data for that face The table includes ten "columns", elementIds, pathNames pathIndices temperaturesReferencePlane temperaturesUpperSurface temperaturesLowerSurface thermalGradients Temperature values at reference plane MUST be defined. Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and temperature associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a temperature of', temperaturesReferencePlane[index])
Properties: `elementIds`, `pathIndices`, `pathNames`, `temperaturesLowerSurface`, `temperaturesReferencePlane`, `temperaturesUpperSurface`, `thermalGradients`

Methods:

#### `DFEMFieldTemperatureGradient2D(elementIds: [int], temperaturesReferencePlane: [float], thermalGradients: [float], temperaturesLowerSurface: [float], temperaturesUpperSurface: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldTemperatureGradient2D in this environment.

- `elementIds` — A list of integers to define target element IDs in the field.
- `temperaturesReferencePlane` — A list of temperature values at element reference plane.
- `thermalGradients` — A list of effective linear thermal gradients.
- `temperaturesLowerSurface` — A list of temperature values at lower surface.
- `temperaturesUpperSurface` — A list of temperature values at upper surface.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getTemperaturesLowerSurface() -> [float]` — a list of temperature values defined on lower surface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesReferencePlane() -> [float]` — a list of temperature values defined on the element reference plane. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesUpperSurface() -> [float]` — a list of temperature values defined on upper surface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradients() -> [float]` — a list of thermal gradients. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], temperaturesReferencePlane: [float], thermalGradients: [float], temperaturesLowerSurface: [float], temperaturesUpperSurface: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Update the elementIds.
- `temperaturesReferencePlane` — Update the temperaturesReferencePlane. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradients` — Update the thermalGradients. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `temperaturesLowerSurface` — Update the temperaturesLowerSurface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesUpperSurface` — Update the temperaturesUpperSurface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `pathNames` — Update the pathNames of this DFEMFieldTemperatureGradient2D
- `pathIndices` — Update the pathIndices of this DFEMFieldTemperatureGradient2D


## `apex.environment.DFEMFieldTemperatureGradient2DHeat`
A class describing a table like data structure defining the spatially varying temperatures across a multiplicity of Nodes. Each "row" in this table identifies an Node and the temperature data for that Node. The table includes ten "columns", nodeIds, pathNames pathIndices temperaturesTop temperaturesBottom temperaturesMid Temperature values at reference plane MUST be defined. Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated node. To define or determine the MeshBody associated with any node in the field use the entry in pathIndices corresponding to the Node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, nodes 1000 and 1001 belong to "Mesh 1", while nodes 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and temperature associated with each Node in the field, the following code could be used, for index, node_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a temperature of', temperaturesTop[index])
Properties: `nodeIds`, `pathIndices`, `pathNames`, `temperaturesBottom`, `temperaturesMid`, `temperaturesTop`

Methods:

#### `DFEMFieldTemperatureGradient2DHeat(nodeIds: [int], temperaturesTop: [float], temperaturesBottom: [float], temperaturesMid: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldTemperatureGradient2DHeat in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `temperaturesTop` — A list of floats to define the temperatures at top location through the thickness.
- `temperaturesBottom` — A list of floats to define the temperatures at bottom location through the thickness.
- `temperaturesMid` — A list of floats to define the temperatures at mid location through the thickness.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getTemperaturesBottom() -> [float]` — a list of temperature values defined on bottom location across thickness direction. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesMid() -> [float]` — a list of temperature values defined on the mid location across thickness direction. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesTop() -> [float]` — a list of temperature values defined on the top location across thickness direction. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(nodeIds: [int], temperaturesTop: [float], temperaturesBottom: [float], temperaturesMid: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Updates the nodeIds.
- `temperaturesTop` — Updates the temperaturesTop. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesBottom` — Updates the temperaturesBottom. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesMid` — Updates the temperaturesMid. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `pathNames` — Update the pathNames of this DFEMFieldTemperatureGradient2DHeat
- `pathIndices` — Update the pathIndices of this DFEMFieldTemperatureGradient2DHeat


## `apex.environment.DFEMFieldTemperatureGradientBeam2`
A class describing a table like data structure defining the spatially varying temperatures across a multiplicity of elements. Each "row" in this table identifies an element and the temperature data for that face The table includes ten "columns", elementIds, pathNames pathIndices temperaturesEndA temperaturesEndB thermalGradients1A thermalGradients1B thermalGradients2A thermalGradients2B temperaturesPointCendA temperaturesPointDendA temperaturesPointEendA temperaturesPointFendA temperaturesPointCendB temperaturesPointDendB temperaturesPointEendB temperaturesPointFendB Temperature values at endA and endB MUST be defined. Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and temperature associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a temperature of', temperaturesEndA[index])
Properties: `elementIds`, `inputType`, `pathIndices`, `pathNames`, `temperaturesEndA`, `temperaturesEndB`, `temperaturesPointCendA`, `temperaturesPointCendB`, `temperaturesPointDendA`, `temperaturesPointDendB`, `temperaturesPointEendA`, `temperaturesPointEendB`, `temperaturesPointFendA`, `temperaturesPointFendB`, `thermalGradients1A`, `thermalGradients1B`, `thermalGradients2A`, `thermalGradients2B`

Methods:

#### `DFEMFieldTemperatureGradientBeam2(elementIds: [int], temperaturesEndA: [float], temperaturesEndB: [float], thermalGradients1A: [float], thermalGradients1B: [float], thermalGradients2A: [float], thermalGradients2B: [float], temperaturesPointCendA: [float], temperaturesPointDendA: [float], temperaturesPointEendA: [float], temperaturesPointFendA: [float], temperaturesPointCendB: [float], temperaturesPointDendB: [float], temperaturesPointEendB: [float], temperaturesPointFendB: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
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

- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getTemperaturesEndA() -> [float]` — a list of temperature values at end A on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesEndB() -> [float]` — a list of temperature values at end B on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointCendA() -> [float]` — a list of temperature values on point C at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointCendB() -> [float]` — a list of temperature values on point C at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointDendA() -> [float]` — a list of temperature values on point D at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointDendB() -> [float]` — a list of temperature values on point D at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointEendA() -> [float]` — a list of temperature values on point E at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointEendB() -> [float]` — a list of temperature values on point E at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointFendA() -> [float]` — a list of temperature values on point F at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointFendB() -> [float]` — a list of temperature values on point F at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradients1A() -> [float]` — a list of effective linear thermal gradients in direction 1 on end A. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradients1B() -> [float]` — a list of effective linear thermal gradients in direction 1 on end B. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradients2A() -> [float]` — a list of effective linear thermal gradients in direction 2 on end A. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradients2B() -> [float]` — a list of effective linear thermal gradients in direction 2 on end B. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], temperaturesEndA: [float], temperaturesEndB: [float], thermalGradients1A: [float], thermalGradients1B: [float], thermalGradients2A: [float], thermalGradients2B: [float], temperaturesPointCendA: [float], temperaturesPointDendA: [float], temperaturesPointEendA: [float], temperaturesPointFendA: [float], temperaturesPointCendB: [float], temperaturesPointDendB: [float], temperaturesPointEendB: [float], temperaturesPointFendB: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Update the elementIds.
- `temperaturesEndA` — Updates the temperaturesEndA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesEndB` — Updates the temperaturesEndB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradients1A` — Updates the thermalGradients1A. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradients1B` — Updates the thermalGradients1B. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradients2A` — Updates the thermalGradients2A. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradients2B` — Updates the thermalGradients2B. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `temperaturesPointCendA` — Updates the temperaturesPointCendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointDendA` — Updates the temperaturesPointDendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointEendA` — Updates the temperaturesPointEendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointFendA` — Updates the temperaturesPointFendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointCendB` — Updates the temperaturesPointCendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointDendB` — Updates the temperaturesPointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointEendB` — Updates the temperaturesPointEendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointFendB` — Updates the temperaturesPointFendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `pathNames` — Update the pathNames of this DFEMFieldTemperatureGradientBeam2
- `pathIndices` — Update the pathIndices of this DFEMFieldTemperatureGradientBeam2
- `inputType` — Update the inputType.


## `apex.environment.DFEMFieldTemperatureGradientBeam3`
A class describing a table like data structure defining the spatially varying temperatures across a multiplicity of elements. Each "row" in this table identifies an element and the temperature data for that face The table includes ten "columns", elementIds, pathNames pathIndices thermalGradientsYA thermalGradientsZA thermalGradientsYB thermalGradientsZB thermalGradientsYC thermalGradientsZC temperaturesPointCendA temperaturesPointDendA temperaturesPointEendA temperaturesPointFendA temperaturesPointCendB temperaturesPointDendB temperaturesPointEendB temperaturesPointFendB temperaturesPointCmidC temperaturesPointDmidC temperaturesPointEmidC temperaturesPointFmidC Temperature values at endA, endB and midC MUST be defined. Apex supports duplicate Element IDs within a single Apex model. In order to uniquely identify an Element it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Element in this field a more compact scheme is used. "elementIds" - a list defining the ID of every element in the field. "pathNames" - a list of unique pathNames. Every element in elementIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'elementIds'. "pathIndices" - The indices of the MeshBody pathName for every Element in the field. This list has the same number of entries as elementIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated Element. To define or determine the MeshBody associated with any Element in the field use the entry in pathIndices corresponding to the Element ID entry in elementIds to lookup the MeshBody pathName in pathNames. For example: elementIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, elements 1000 and 1001 belong to "Mesh 1", while elements 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact element identification scheme. To print the pathName and temperature associated with each Element in the field, the following code could be used, for index, element_id in enumerate(elementIds): print('Element with ID', element_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a temperature of', temperaturesEndA[index])
Properties: `elementIds`, `inputType`, `pathIndices`, `pathNames`, `temperaturesEndA`, `temperaturesEndB`, `temperaturesMidC`, `temperaturesPointCendA`, `temperaturesPointCendB`, `temperaturesPointCmidC`, `temperaturesPointDendA`, `temperaturesPointDendB`, `temperaturesPointDmidC`, `temperaturesPointEendA`, `temperaturesPointEendB`, `temperaturesPointEmidC`, `temperaturesPointFendA`, `temperaturesPointFendB`, `temperaturesPointFmidC`, `thermalGradientsYA`, `thermalGradientsYB`, `thermalGradientsYC`, `thermalGradientsZA`, `thermalGradientsZB`, `thermalGradientsZC`

Methods:

#### `DFEMFieldTemperatureGradientBeam3(elementIds: [int], temperaturesEndA: [float], temperaturesEndB: [float], temperaturesMidC: [float], thermalGradientsYA: [float], thermalGradientsZA: [float], thermalGradientsYB: [float], thermalGradientsZB: [float], thermalGradientsYC: [float], thermalGradientsZC: [float], temperaturesPointCendA: [float], temperaturesPointDendA: [float], temperaturesPointEendA: [float], temperaturesPointFendA: [float], temperaturesPointCendB: [float], temperaturesPointDendB: [float], temperaturesPointEendB: [float], temperaturesPointFendB: [float], temperaturesPointCmidC: [float], temperaturesPointDmidC: [float], temperaturesPointEmidC: [float], temperaturesPointFmidC: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
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

- `getElementIds() -> [int]` — a list of integers to define target element IDs in the field.
- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B and mid C. If the inputType is element variable, all temperature values and thermal gradients can be defined.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getTemperaturesEndA() -> [float]` — a list of temperature values at end A on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesEndB() -> [float]` — a list of temperature values at end B on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesMidC() -> [float]` — a list of temperature values at a point C between end A and end B. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointCendA() -> [float]` — a list of temperature values on point C at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointCendB() -> [float]` — a list of temperature values on point C at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointCmidC() -> [float]` — a list of temperature values on point C at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointDendA() -> [float]` — a list of temperature values on point D at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointDendB() -> [float]` — a list of temperature values on point D at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointDmidC() -> [float]` — a list of temperature values on point D at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointEendA() -> [float]` — a list of temperature values on point E at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointEendB() -> [float]` — a list of temperature values on point E at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointEmidC() -> [float]` — a list of temperature values on point E at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointFendA() -> [float]` — a list of temperature values on point F at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointFendB() -> [float]` — a list of temperature values on point F at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturesPointFmidC() -> [float]` — a list of temperature values on point F at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradientsYA() -> [float]` — a list of effective linear thermal gradients in local direction y on end A. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradientsYB() -> [float]` — a list of effective linear thermal gradients in direction y on end B. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradientsYC() -> [float]` — a list of effective linear thermal gradients in direction y on mid C. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradientsZA() -> [float]` — a list of effective linear thermal gradients in direction z on end A. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradientsZB() -> [float]` — a list of effective linear thermal gradients in direction z on end B. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `getThermalGradientsZC() -> [float]` — a list of effective linear thermal gradients in direction z on mid C. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
#### `removeTargets(ids: [int]) -> None`
Remove the target elements from the field.

- `ids` — A list of integers to identify the target element ids to be removed from the field.

#### `update(elementIds: [int], temperaturesEndA: [float], temperaturesEndB: [float], temperaturesMidC: [float], thermalGradientsYA: [float], thermalGradientsZA: [float], thermalGradientsYB: [float], thermalGradientsZB: [float], thermalGradientsYC: [float], thermalGradientsZC: [float], temperaturesPointCendA: [float], temperaturesPointDendA: [float], temperaturesPointEendA: [float], temperaturesPointFendA: [float], temperaturesPointCendB: [float], temperaturesPointDendB: [float], temperaturesPointEendB: [float], temperaturesPointFendB: [float], temperaturesPointCmidC: [float], temperaturesPointDmidC: [float], temperaturesPointEmidC: [float], temperaturesPointFmidC: [float], pathNames: [str], pathIndices: [int], inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `elementIds` — Update the elementIds.
- `temperaturesEndA` — Updates the temperaturesEndA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesEndB` — Updates the temperaturesEndB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesMidC` — Updates the temperaturesMidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradientsYA` — Updates the thermalGradientsYA. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradientsZA` — Updates the thermalGradientsZA. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradientsYB` — Updates the thermalGradientsYB. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradientsZB` — Updates the thermalGradientsZB. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradientsYC` — Updates the thermalGradientsYC. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `thermalGradientsZC` — Updates the thermalGradientsZC. It represents a Thermal Gradient quantity and must be specified using units of Thermal Gradient from the active script unit system.
- `temperaturesPointCendA` — Updates the temperaturesPointCendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointDendA` — Updates the temperaturesPointDendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointEendA` — Updates the temperaturesPointEendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointFendA` — Updates the temperaturesPointFendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointCendB` — Updates the temperaturesPointCendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointDendB` — Updates the temperaturesPointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointEendB` — Updates the temperaturesPointEendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointFendB` — Updates the temperaturesPointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointCmidC` — Updates the temperaturesPointCmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointDmidC` — Updates the temperaturesPointDmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointEmidC` — Updates the temperaturesPointEmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturesPointFmidC` — Updates the temperaturesPointFmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `pathNames` — Update the pathNames of this DFEMFieldTemperatureGradientBeam3
- `pathIndices` — Update the pathIndices of this DFEMFieldTemperatureGradientBeam3
- `inputType` — Update the inputType.


## `apex.environment.DFEMFieldTemperatureNodal`
A class describing a table like data structure defining the spatially varying pressure magnitude across a multiplicity of nodes. Each "row" in this table identifies a node and the temperature data for that node. The table includes ten "columns", nodeIds, pathNames pathIndices temperatures Temperature values MUST be defined and is associated with the nodes defined in nodeIds. Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated node. To define or determine the MeshBody associated with any node in the field use the entry in pathIndices corresponding to the node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, nodes 1000 and 1001 belong to "Mesh 1", while nodes 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and temperature associated with each node in the field, the following code could be used, for index, node_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a temperature of', temperatures[index])
Properties: `nodeIds`, `pathIndices`, `pathNames`, `temperatureValues`

Methods:

#### `DFEMFieldTemperatureNodal(nodeIds: [int], temperatureValues: [float], pathNames: [str], pathIndices: [int]) -> None`
Create DFEMFieldTemperatureNodal in this environment.

- `nodeIds` — A list of integers to define target node IDs in the field.
- `temperatureValues` — A list of floats to define temperature values at each node.
- `pathNames` — The full pathName of the target nodes. It can be one string to indicate that all nodes belong to one part or a list of strings to define different pathNames for each target node.
- `pathIndices` — An optional list of integers mapped to the string indices in the pathNames. Each integer in the list indicates the full pathName of the target node/element in the field, so that system can find the unique node/element id in the model. This argument can be omitted when only one pathName is existed.

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getTemperatureValues() -> [float]` — a list of temperature values associated with the target nodes. Each value represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], temperatureValues: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Update the nodeIds.
- `temperatureValues` — Update the temperature values.
- `pathNames` — Update the pathNames of this DFEMFieldTemperatureNodal
- `pathIndices` — Update the pathIndices of this DFEMFieldTemperatureNodal


## `apex.environment.DFEMFieldTimeDelay`
A class describing a table like data structure defining the spatially varying time delay across a multiplicity of nodes. Each "row" in this table identifies a node and the time delay data for that node. The table includes ten "columns", nodeIds, pathNames pathIndices timeDelaysX timeDelaysY timeDelaysZ timeDelaysRx timeDelaysRy timeDelaysRz The time delays may be blank but at least one should be defined for each associated node. Apex supports duplicate Node IDs within a single Apex model. In order to uniquely identify a Node it is necessary to define both its ID and the MeshBody to which it is associated. In order to avoid storing a potentially large pathName string for every Node in this field a more compact scheme is used. "nodeIds" - a list defining the ID of every node in the field. "pathNames" - a list of unique pathNames. Every node in nodeIds is composed by one of the MeshBodies included in this List. Since a MeshBody appears a maximum of once in this list it typically has many fewer entries than 'nodeIds'. "pathIndices" - The indices of the MeshBody pathName for every node in the field. This list has the same number of entries as nodeIds and uses the same sequence. Each entry in pathIndices represents an index into pathNames that identifies the pathName of the MeshBody of the associated node. To define or determine the MeshBody associated with any node in the field use the entry in pathIndices corresponding to the node ID entry in nodeIds to lookup the MeshBody pathName in pathNames. For example: nodeIds=[ 1000, 1001, 1002, 1003 ], pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2" ] pathIndices = [ 0, 0, 1, 1 ] In this field, nodes 1000 and 1001 belong to "Mesh 1", while nodes 1002 and 1003 belong to "Mesh 2". The following code snippet may be useful to help understand the compact node identification scheme. To print the pathName and time delay associated with each node in the field, the following code could be used, for index, node_id in enumerate(nodeIds): print('Node with ID', node_id, 'is associated with MeshBody', pathNames[pathIndices[index], 'and has a time delay of ', timeDelaysX[index], "in translation X degree of freedom")
Properties: `nodeIds`, `pathIndices`, `pathNames`, `timeDelaysRx`, `timeDelaysRy`, `timeDelaysRz`, `timeDelaysX`, `timeDelaysY`, `timeDelaysZ`

Methods:

#### `DFEMFieldTimeDelay(nodeIds: [int], timeDelaysX: [float], timeDelaysY: [float], timeDelaysZ: [float], timeDelaysRx: [float], timeDelaysRy: [float], timeDelaysRz: [float], pathNames: [str], pathIndices: [int]) -> None`
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

- `getNodeIds() -> [int]` — a list of integers to define target node IDs in the field. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getPathIndices() -> [int]` — a list of integers mapped to the string indices in the pathNames. Each item in the list indicates the pathName of the target FEM entity in the field. So the number of indices equals to the number of target FEM entities in the field.
- `getPathNames() -> [str]` — a list to provide the unique pathNames of the mesh bodies that include target FEM entities. For example, pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1"] indicates that all target FEM entities is associated with the mesh body "/Part 1/Mesh 1" in the model. pathNames = [ apex.currentModel().name + "/Part 1/Mesh 1", apex.currentModel().name + "/Part 1/Mesh 2", apex.currentModel().name + "/Part 1/Mesh 3"] indicates that all target nodes/elements belong to the three mesh bodies.
- `getTimeDelaysRx() -> [float]` — a list of the time delay values in the rotation X component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelaysRy() -> [float]` — a list of the time delay values in the rotation Y component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelaysRz() -> [float]` — a list of the time delay values in the rotation Z component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelaysX() -> [float]` — a list of the time delay values in the X component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelaysY() -> [float]` — a list of the time delay value in the Y component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelaysZ() -> [float]` — a list of the time delay values in the Z component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
#### `removeTargets(ids: [int]) -> None`
Remove the target nodes from the field.

- `ids` — A list of integers to identify the target node ids to be removed from the field.

#### `update(nodeIds: [int], timeDelaysX: [float], timeDelaysY: [float], timeDelaysZ: [float], timeDelaysRx: [float], timeDelaysRy: [float], timeDelaysRz: [float], pathNames: [str], pathIndices: [int]) -> None`
Updates one or more properties of the field. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `nodeIds` — Updates the nodeIds.
- `timeDelaysX` — Updates the timeDelaysX. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelaysY` — Updates the timeDelaysY. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelaysZ` — Updates the timeDelaysZ. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelaysRx` — Updates the timeDelaysRx. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelaysRy` — Updates the timeDelaysRy. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelaysRz` — Updates the timeDelaysRz. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `pathNames` — Update the pathNames of this DFEMFieldTimeDelay
- `pathIndices` — Update the pathIndices of this DFEMFieldTimeDelay


## `apex.environment.DiscreteTable`
Properties: `fieldValuess`, `identifierss`, `identifierTypes`, `pathNames`

## `apex.environment.DisplacementConstraint`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class DisplacementConstraint. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
Properties: `applicationMethod`, `attachmentDistributionType`, `attachmentRegion`, `constraintType`, `displacementConstraintProperties`, `orientation`, `target`

Methods:

- `getApplicationMethod() -> apex.attribute.ApplicationMethod` — Returns ApplicationMethod of the DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
- `getAttachmentDistributionType() -> apex.attribute.DistributionType` — Returns AttachmentDistributionType of the DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
- `getAttachmentRegion() -> apex.EntityCollection` — Returns AttachmentRegion of the DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
- `getConstraintType() -> apex.attribute.ConstraintType` — Returns ConstraintType of the DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
- `getDisplacementConstraintProperties() -> apex.attribute.DisplacementConstraintProperty` — Returns DisplacementConstraintProperties of the DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
- `getOrientation() -> apex.construct.Orientation` — Returns Orientation of the DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
- `getTarget() -> apex.EntityCollection` — Returns a read only collection of the entities that the DisplacementConstraint is applied to. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
#### `update(name: str, description: str, constraintType: apex.attribute.ConstraintType, constraintProperties: apex.attribute.DisplacementConstraintProperty, applicationMethod: apex.attribute.ApplicationMethod, target: apex.EntityCollection, attachmentRegion: apex.EntityCollection, attachmentDistributionType: apex.attribute.DistributionType, orientation: apex.construct.Orientation) -> None`
Update this DisplacementConstraint. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.

- `name` — of this DisplacementConstraint
- `description` — of this DisplacementConstraint
- `constraintType` — of this DisplacementConstraint
- `constraintProperties` — of this DisplacementConstraint
- `applicationMethod` — of this DisplacementConstraint
- `target` — of this DisplacementConstraint
- `attachmentRegion` — of this DisplacementConstraint
- `attachmentDistributionType` — of this DisplacementConstraint
- `orientation` — of this DisplacementConstraint

One or more properties may be updated in each call to update().


## `apex.environment.DisplacementConstraintCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `DisplacementConstraintCollection() -> None` — Construct a new DisplacementConstraintCollection.

## `apex.environment.EnforcedMotion`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
class EnforcedMotion. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
Properties: `applicationMethod`, `attachmentDistributionType`, `attachmentRegion`, `constraintReference`, `orientation`, `target`

Methods:

- `addEnforcedMotionRep(rep: EnforcedMotionRep) -> None` — Add a EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `clearConstraint() -> None` — Remove referenced constraint of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
#### `createEnforcedMotionDynamicRepByComponent(name: str, description: str, motionType: apex.attribute.EnforcedMotionType, approach: apex.attribute.Approach, translationX: apex.DataTable3Col = None, translationY: apex.DataTable3Col = None, translationZ: apex.DataTable3Col = None, rotationX: apex.DataTable3Col = None, rotationY: apex.DataTable3Col = None, rotationZ: apex.DataTable3Col = None) -> EnforcedMotionDynamicRep`
Get a new EnforcedMotionRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.

- `name` — of the EnforcedMotionRep.
- `description` — of the EnforcedMotionRep.
- `motionType` — of the EnforcedMotionRep.
- `approach` — of the EnforcedMotionRep.
- `translationX` — of the EnforcedMotionRep.
- `translationY` — of the EnforcedMotionRep.
- `translationZ` — of the EnforcedMotionRep.
- `rotationX` — of the EnforcedMotionRep.
- `rotationY` — of the EnforcedMotionRep.
- `rotationZ` — of the EnforcedMotionRep.

#### `createEnforcedMotionStaticRepByComponent(name: str, description: str, translationX: float = NAN, translationY: float = NAN, translationZ: float = NAN, rotationX: float = NAN, rotationY: float = NAN, rotationZ: float = NAN) -> EnforcedMotionRep`
Get a new EnforcedMotionRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.

- `name` — of the EnforcedMotionRep.
- `description` — of the EnforcedMotionRep.
- `translationX` — of the EnforcedMotionRep.
- `translationY` — of the EnforcedMotionRep.
- `translationZ` — of the EnforcedMotionRep.
- `rotationX` — of the EnforcedMotionRep.
- `rotationY` — of the EnforcedMotionRep.
- `rotationZ` — of the EnforcedMotionRep.

#### `createEnforcedMotionStaticRepByResultant(name: str, description: str, forceMagnitude: float, momentMagnitude: float, forceOrientation: apex.construct.Orientation = None, momentOrientation: apex.construct.Orientation = None) -> EnforcedMotionRep`
Get a new EnforcedMotionRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.

- `name` — of the EnforcedMotionRep.
- `description` — of the EnforcedMotionRep.
- `forceMagnitude` — of the EnforcedMotionRep.
- `momentMagnitude` — of the EnforcedMotionRep.
- `forceOrientation` — of the EnforcedMotionRep.
- `momentOrientation` — of the EnforcedMotionRep.

- `getApplicationMethod() -> apex.attribute.ApplicationMethod` — Returns ApplicationMethod of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getAttachmentDistributionType() -> apex.attribute.DistributionType` — Returns AttachmentRegion of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getAttachmentRegion() -> apex.EntityCollection` — Returns AttachmentRegion of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getConstraintReference() -> DisplacementConstraint` — Returns ConstraintReference of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getEnforcedMotionDynamicRep(name: str = "#####") -> EnforcedMotionDynamicRep` — Returns EnforcedMotionDynamicRep of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getEnforcedMotionRep(name: str = "#####") -> EnforcedMotionRep` — Returns EnforcedMotionRep of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getEnforcedMotionRepIndex(name: str = "#####") -> SCA.SCAUInt64` — Returns EnforcedMotionRep index of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getOrientation() -> apex.construct.Orientation` — Returns apex.construct.Orientation of the EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTarget() -> apex.EntityCollection` — Returns a read only collection of the entities that the EnforcedMotion is applied to. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeRep(name: str) -> None` — Remove a EnforcedMotionRep by name. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
#### `update(name: str, description: str, enforcedMotionRep: EnforcedMotionRep, applicationMethod: apex.attribute.ApplicationMethod, target: apex.EntityCollection, attachmentRegion: apex.EntityCollection, attachmentDistributionType: apex.attribute.DistributionType, orientation: apex.construct.Orientation, constraintReference: DisplacementConstraint) -> None`
Update this EnforcedMotion. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.

- `name` — of this EnforcedMotion
- `description` — of this EnforcedMotion
- `enforcedMotionRep` — of this EnforcedMotion
- `applicationMethod` — of this EnforcedMotion
- `target` — of this EnforcedMotion
- `attachmentRegion` — of this EnforcedMotion
- `attachmentDistributionType` — of this EnforcedMotion
- `orientation` — of this EnforcedMotion
- `constraintReference` — of this EnforcedMotion

One or more properties may be updated in each call to update(). THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.


## `apex.environment.EnforcedMotionDynamicRep`  (extends `EnforcedMotionRep`)
class EnforcedMotionDynamicRep. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
Properties: `approach`, `motionType`, `rotationX`, `rotationY`, `rotationZ`, `translationX`, `translationY`, `translationZ`

Methods:

- `getApproach() -> apex.attribute.Approach` — Returns Approach of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getMotionType() -> apex.attribute.EnforcedMotionType` — Returns EnforcedMotionType of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getRotationX() -> DataTable3Col` — Returns MomentX value of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getRotationY() -> DataTable3Col` — Returns MomentY value of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getRotationZ() -> DataTable3Col` — Returns MomentZ value of the EnforcedMotionDynamicRep.THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationX() -> DataTable3Col` — Returns ForceX value of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationY() -> DataTable3Col` — Returns ForceY value of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationZ() -> DataTable3Col` — Returns ForceZ value of the EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeDRX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeDRY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeDRZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeDTX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeDTY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeDTZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
#### `update(name: str, description: str, motionType: apex.attribute.EnforcedMotionType, approach: apex.attribute.Approach, translationX: apex.DataTable3Col, translationY: apex.DataTable3Col, translationZ: apex.DataTable3Col, rotationX: apex.DataTable3Col, rotationY: apex.DataTable3Col, rotationZ: apex.DataTable3Col, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this EnforcedMotionDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.

- `name` — of this EnforcedMotionDynamicRep
- `description` — of this EnforcedMotionDynamicRep
- `motionType` — of this EnforcedMotionDynamicRep
- `approach` — of this EnforcedMotionDynamicRep
- `translationX` — of this EnforcedMotionDynamicRep
- `translationY` — of this EnforcedMotionDynamicRep
- `translationZ` — of this EnforcedMotionDynamicRep
- `rotationX` — of this EnforcedMotionDynamicRep
- `rotationY` — of this EnforcedMotionDynamicRep
- `rotationZ` — of this EnforcedMotionDynamicRep
- `color` — of this EnforcedMotionDynamicRep
- `renderStyle` — of this EnforcedMotionDynamicRep
- `enableTransparency` — of this EnforcedMotionDynamicRep
- `transparencyLevel` — of this EnforcedMotionDynamicRep

One or more properties may be updated in each call to update().


## `apex.environment.EnforcedMotionRep`  (extends `LoadRep`)
class EnforcedMotionRep. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
Properties: `rotationMagnitude`, `rotationX`, `rotationY`, `rotationZ`, `translationMagnitude`, `translationX`, `translationY`, `translationZ`

Methods:

- `getRotationMagnitude() -> float` — Returns MMagnitude value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getRotationX() -> float` — Returns MomentX value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getRotationY() -> float` — Returns MomentY value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getRotationZ() -> float` — Returns MomentZ value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationMagnitude() -> float` — Returns FMagnitude value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationX() -> float` — Returns ForceX value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationY() -> float` — Returns ForceY value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `getTranslationZ() -> float` — Returns ForceZ value of the EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeRX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeRY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeRZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeTX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeTY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
- `removeTZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.
#### `update(name: str, description: str, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, translationMagnitude: float, translationOrientation: apex.construct.Orientation, rotationMagnitude: float, rotationOrientation: apex.construct.Orientation, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this EnforcedMotionRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadEnforcedMotionTotal.

- `name` — of this EnforcedMotionRep
- `description` — of this EnforcedMotionRep
- `translationX` — of this EnforcedMotionRep
- `translationY` — of this EnforcedMotionRep
- `translationZ` — of thisEnforcedMotionRep
- `rotationX` — of this EnforcedMotionRep
- `rotationY` — of this EnforcedMotionRep
- `rotationZ` — of this EnforcedMotionRep
- `translationMagnitude` — of this EnforcedMotionRep
- `translationOrientation` — of this EnforcedMotionRep
- `rotationMagnitude` — of this EnforcedMotionRep
- `rotationOrientation` — of this EnforcedMotionRep
- `color` — of this EnforcedMotionRep
- `renderStyle` — of this EnforcedMotionRep
- `enableTransparency` — of this EnforcedMotionRep
- `transparencyLevel` — of this EnforcedMotionRep

One or more properties may be updated in each call to update(). For example:


## `apex.environment.ForceMoment`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
class ForceMoment. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
Properties: `applicationMethod`, `attachmentDistributionType`, `attachmentRegion`, `constraintReference`, `forceMomentDynamicRep`, `forceMomentRep`, `forceMomentRepIndex`, `orientation`, `target`

Methods:

- `addForceMomentRep(rep: ForceMomentRep) -> None` — Add a ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `clearConstraint() -> None` — Remove referenced constraint of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
#### `createForceMomentDynamicRepByComponent(name: str, description: str, approach: apex.attribute.Approach, forceX: apex.DataTable3Col = None, forceY: apex.DataTable3Col = None, forceZ: apex.DataTable3Col = None, momentX: apex.DataTable3Col = None, momentY: apex.DataTable3Col = None, momentZ: apex.DataTable3Col = None) -> ForceMomentDynamicRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `approach` — of the ForceMomentRep.
- `forceX` — of the ForceMomentRep.
- `forceY` — of the ForceMomentRep.
- `forceZ` — of the ForceMomentRep.
- `momentX` — of the ForceMomentRep.
- `momentY` — of the ForceMomentRep.
- `momentZ` — of the ForceMomentRep.

#### `createForceMomentStaticRepByComponent(name: str, description: str, forceX: float = NAN, forceY: float = NAN, forceZ: float = NAN, momentX: float = NAN, momentY: float = NAN, momentZ: float = NAN) -> ForceMomentRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `forceX` — of the ForceMomentRep.
- `forceY` — of the ForceMomentRep.
- `forceZ` — of the ForceMomentRep.
- `momentX` — of the ForceMomentRep.
- `momentY` — of the ForceMomentRep.
- `momentZ` — of the ForceMomentRep.

#### `createForceMomentStaticRepByResultant(name: str, description: str, forceMagnitude: float, momentMagnitude: float, forceOrientation: apex.construct.Orientation = None, momentOrientation: apex.construct.Orientation = None) -> ForceMomentRep`
Get a new ForceMomentRep in this environment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.

- `name` — of the ForceMomentRep.
- `description` — of the ForceMomentRep.
- `forceMagnitude` — of the ForceMomentRep.
- `momentMagnitude` — of the ForceMomentRep.
- `forceOrientation` — of the ForceMomentRep.
- `momentOrientation` — of the ForceMomentRep.

- `getApplicationMethod() -> apex.attribute.ApplicationMethod` — Returns ApplicationMethod of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getAttachmentDistributionType() -> apex.attribute.DistributionType` — Returns AttachmentRegion of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getAttachmentRegion() -> apex.EntityCollection` — Returns AttachmentRegion of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getConstraintReference() -> DisplacementConstraint` — Returns ConstraintReference of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceMomentDynamicRep(name: str = "#####") -> ForceMomentDynamicRep` — Returns ForceMomentDynamicRep of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceMomentRep(name: str = "#####") -> ForceMomentRep` — Returns ForceMomentRep of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceMomentRepIndex(name: str = "#####") -> SCA.SCAUInt64` — Returns ForceMomentRep index of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getOrientation() -> apex.construct.Orientation` — Returns apex.construct.Orientation of the ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getTarget() -> apex.EntityCollection` — Returns a read only collection of the entities that the ForceMoment is applied to. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeRep(name: str) -> None` — Remove a ForceMomentRep by name. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
#### `update(name: str, description: str, forceMomentRep: ForceMomentRep, applicationMethod: apex.attribute.ApplicationMethod, target: apex.EntityCollection, attachmentRegion: apex.EntityCollection, attachmentDistributionType: apex.attribute.DistributionType, orientation: apex.construct.Orientation, constraintReference: DisplacementConstraint) -> None`
Update this ForceMoment. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.

- `name` — of this ForceMoment
- `description` — of this ForceMoment
- `forceMomentRep` — of this ForceMoment
- `applicationMethod` — of this ForceMoment
- `target` — of this ForceMoment
- `attachmentRegion` — of this ForceMoment
- `attachmentDistributionType` — of this ForceMoment
- `orientation` — of this ForceMoment
- `constraintReference` — of this ForceMoment

One or more properties may be updated in each call to update().


## `apex.environment.ForceMomentDynamicRep`  (extends `ForceMomentRep`)
class ForceMomentDynamicRep. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
Properties: `approach`, `forceX`, `forceY`, `forceZ`, `momentX`, `momentY`, `momentZ`

Methods:

- `getApproach() -> apex.attribute.Approach` — Returns Approach of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceX() -> DataTable3Col` — Returns ForceX value of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceY() -> DataTable3Col` — Returns ForceY value of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceZ() -> DataTable3Col` — Returns ForceZ value of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getMomentX() -> DataTable3Col` — Returns MomentX value of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getMomentY() -> DataTable3Col` — Returns MomentY value of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getMomentZ() -> DataTable3Col` — Returns MomentZ value of the ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeDFX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeDFY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeDFZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeDMX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeDMY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeDMZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
#### `update(name: str, description: str, approach: apex.attribute.Approach, forceX: apex.DataTable3Col, forceY: apex.DataTable3Col, forceZ: apex.DataTable3Col, momentX: apex.DataTable3Col, momentY: apex.DataTable3Col, momentZ: apex.DataTable3Col, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this ForceMomentDynamicRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.

- `name` — of this ForceMomentDynamicRep
- `description` — of this ForceMomentDynamicRep
- `approach` — of this ForceMomentDynamicRep
- `forceX` — of this ForceMomentDynamicRep
- `forceY` — of this ForceMomentDynamicRep
- `forceZ` — of this ForceMomentDynamicRep
- `momentX` — of this ForceMomentDynamicRep
- `momentY` — of this ForceMomentDynamicRep
- `momentZ` — of this ForceMomentDynamicRep
- `color` — of this ForceMomentDynamicRep
- `renderStyle` — of this ForceMomentDynamicRep
- `enableTransparency` — of this ForceMomentDynamicRep
- `transparencyLevel` — of this ForceMomentDynamicRep

One or more properties may be updated in each call to update(). For example:


## `apex.environment.ForceMomentRep`  (extends `LoadRep`)
class ForceMomentRep. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
Properties: `forceX`, `forceY`, `forceZ`, `momentX`, `momentY`, `momentZ`

Methods:

- `getForceX() -> float` — Returns ForceX value of the ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceY() -> float` — Returns ForceY value of the ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getForceZ() -> float` — Returns ForceZ value of the ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getMomentX() -> float` — Returns MomentX value of the ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getMomentY() -> float` — Returns MomentY value of the ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `getMomentZ() -> float` — Returns MomentZ value of the ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeFX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeFY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeFZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeMX() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeMY() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
- `removeMZ() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.
#### `update(name: str, description: str, forceX: float, forceY: float, forceZ: float, momentX: float, momentY: float, momentZ: float, forceMagnitude: float, forceOrientation: apex.construct.Orientation, momentMagnitude: float, momentOrientation: apex.construct.Orientation, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this ForceMomentRep. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadForceComponent, LoadMomentComponent.

- `name` — of this ForceMomentRep
- `description` — of this ForceMomentRep
- `forceX` — of this ForceMomentRep
- `forceY` — of this ForceMomentRep
- `forceZ` — of this ForceMomentRep
- `momentX` — of this ForceMomentRep
- `momentY` — of this ForceMomentRep
- `momentZ` — of this ForceMomentRep
- `forceMagnitude` — of this ForceMomentRep
- `forceOrientation` — of this ForceMomentRep
- `momentMagnitude` — of this ForceMomentRep
- `momentOrientation` — of this ForceMomentRep
- `color` — of this ForceMomentRep
- `renderStyle` — of this ForceMomentRep
- `enableTransparency` — of this ForceMomentRep
- `transparencyLevel` — of this ForceMomentRep

One or more properties may be updated in each call to update(). For example:


## `apex.environment.Gravity`  (extends `Load`, `IActivatable`)
Class Gravity.
Properties: `coordinateSystem`, `coordinateSystemDefinition`, `gravConstant`, `gravConstantMultiplier`, `magnitudeAccel`, `orientation`

Methods:

- `getCoordinateSystem() -> apex.construct.CoordinateSystem` — Returns CoordinateSystem of the gravity.
- `getCoordinateSystemDefinition() -> int` — the coordinate system definition of the gravity: "apex.attribute.CoordinateSystemDefinition.SuperElement", the coordinate system is defined in the super-element and will be translated, rotated with the super-element. "apex.attribute.CoordinateSystemDefinition.Residual", the coordinate system is defined in the residual structure and stationary with the basic coordinate system.
- `getGravConstant() -> float` — Returns GravConstant of the gravity.
- `getGravConstantMultiplier() -> float` — Returns GravConstantMultiplier of the gravity.
- `getMagnitudeAccel() -> float` — Returns MagnitudeAccel of the gravity.
- `getOrientation() -> apex.construct.Orientation` — Returns Orientation of the gravity.
- `isValid() -> bool`
#### `setDescription(description: str) -> None`
Set the gravity description.

- `description` — of the gravity.

#### `setName(name: str) -> None`
Set the gravity name.

- `name` — of the gravity.

#### `update(name: str, description: str, orientation: apex.construct.Orientation, gravConstant: float, magnitude: float, gravConstantMultiplier: float, vector_x_component: float, vector_y_component: float, vector_z_component: float, coordinateSystem: apex.construct.CoordinateSystem, coordinateSystemDefinition: int) -> None`
Update this Gravity.

- `name` — of this Gravity
- `description` — of this Gravity
- `orientation` — of this Gravity
- `gravConstant` — of this Gravity
- `magnitude` — of this Gravity
- `gravConstantMultiplier` — of this Gravity
- `vector_x_component` — of this Gravity
- `vector_y_component` — of this Gravity
- `vector_z_component` — of this Gravity
- `coordinateSystem` — Update the coordinateSystem
- `coordinateSystemDefinition` — Update the coordinateSystemDefinition.

One or more properties may be updated in each call to update().


## `apex.environment.InitialCondition`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Initial Condition is a base class for all Initial Condition types supported in Apex.
Properties: `id`

Methods:

- `getId() -> int` — the id of the initial condition.

## `apex.environment.InitialDisplacementVelocity`  (extends `InitialCondition`)
An initial displacement and velocity acting on Node used in transient analysis. The constant initial displacement and velocity may be applied to solid, cell, surface, face, curve, edge, 3d/2d/1d mesh bodies and Nodes. When used to generate a Nastran model this class will create a Nastran TIC entry for each group of consistent element ids.
Properties: `displacementRx`, `displacementRy`, `displacementRz`, `displacementX`, `displacementY`, `displacementZ`, `target`, `velocityRx`, `velocityRy`, `velocityRz`, `velocityX`, `velocityY`, `velocityZ`

Methods:

- `getDisplacementRx() -> float` — the displacement value in the rotation X. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `getDisplacementRy() -> float` — the displacement value in the rotation Y. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `getDisplacementRz() -> float` — the displacement value in the rotation Z. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `getDisplacementX() -> float` — the displacement value in the translation X. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `getDisplacementY() -> float` — the displacement value in the translation Y. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `getDisplacementZ() -> float` — the displacement value in the translation Z. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the initial displacement and velocity will be applied to. Initial displacement and velocity may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Initial displacement and velocity assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getVelocityRx() -> float` — the velocity value in rotation X. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `getVelocityRy() -> float` — the velocity value in rotation Y. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `getVelocityRz() -> float` — the velocity value in rotation Z. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `getVelocityX() -> float` — the velocity value in translation X. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `getVelocityY() -> float` — the velocity value in translation Y. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `getVelocityZ() -> float` — the velocity value in translation Z. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, displacementX: float, displacementY: float, displacementZ: float, displacementRx: float, displacementRy: float, displacementRz: float, velocityX: float, velocityY: float, velocityZ: float, velocityRx: float, velocityRy: float, velocityRz: float) -> None`
Updates one or more properties of the initial displacement and velocity. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the initial displacement and velocity.
- `description` — Updates the description of the initial displacement and velocity.
- `id` — Updates the id of the initial displacement and velocity.
- `target` — Updates the target of the initial displacement and velocity.
- `displacementX` — Updates the displacementX. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `displacementY` — Updates the displacementY. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `displacementZ` — Updates the displacementZ. It is a Length quantity and is defined using the units of Length from the active script unit system.
- `displacementRx` — Updates the displacementRx. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `displacementRy` — Updates the displacementRy. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `displacementRz` — Updates the displacementRz. It is an Angle quantity and is defined using the units of Angle from the active script unit system.
- `velocityX` — Updates the velocityX. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `velocityY` — Updates the velocityY. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `velocityZ` — Updates the velocityZ. It is a Velocity quantity and is defined using the units of Velocity from the active script unit system.
- `velocityRx` — Updates the velocityRx. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `velocityRy` — Updates the velocityRy. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.
- `velocityRz` — Updates the velocityRz. It is a Rotation Velocity quantity and is defined using the units of Rotation Velocity from the active script unit system.


## `apex.environment.InitialDisplacementVelocityVariable`  (extends `InitialCondition`)
This class represents a spatially varying initial displacement and velocity applied to Node. A single instance of this class may include a multiplicity of individual initial displacement and velocity each applied to a different node. All of the individual initial displacement and velocity composed by this initial condition share a common ID. When used in a Nastran simulation this class will give rise to one TIC entry for each element within the scope of the region with which it is associated. The variation of displacements and velocities across the elements is defined using a DFEMFieldInitialDisplacementVelocity. This field defines the nodes that represent the region to which this initial condition is applied as well as the variation of displacement and velocity values across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldInitialDisplacementVelocity` — a DFEMFieldInitialDisplacementVelocity that identifies nodes that represent the region to which this initial condition is applied as well as the distribution of displacement and velocity values across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldInitialDisplacementVelocity) -> None`
Updates one or more properties of the initial displacement and velocity. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of this initial displacement and velocity.
- `name` — Updates the name of this initial displacement and velocity.
- `description` — Updates the description of this initial displacement and velocity.
- `spatialTarget` — Updates the spatialTarget of this initial displacement and velocity.


## `apex.environment.InitialStrain`  (extends `InitialCondition`)
An initial strain acting on Element used in nonlinear scenario(SOL400) only. The constant initial strain may be applied to solid, cell, surface, face, 3d/2d/1d mesh bodies and 3d/2d/1d elements. Note that the initial strain value are applied to Gaussion points. When used to generate a Nastran model this class will create a Nastran IPSTRAIN entry for each group of consistent element ids..
Properties: `int1`, `intN`, `layer1`, `layerN`, `strain`, `target`

Methods:

- `getInt1() -> int` — the first integration point number.
- `getIntN() -> int` — the last integration point number.
- `getLayer1() -> int` — the first integration layer number.
- `getLayerN() -> int` — the last integration layer number.
- `getStrain() -> float` — the initial strain value. It is a Strain quantity and is defined using the units of Strain from the active script unit system.
- `getTarget() -> apex.EntityCollection` — the target entities that the InitialStrain is applied to.
#### `update(name: str, description: str, target: apex.EntityCollection, int1: int, intN: int, layer1: int, layerN: int, strain: float) -> None`
Updates one or more properties of the initial strain. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the initial strain.
- `description` — Updates the description of the initial strain.
- `target` — Updates the target.
- `int1` — Updates the int1.
- `intN` — Updates the intN.
- `layer1` — Updates the layer1.
- `layerN` — Updates the layerN.
- `strain` — Updates the strainValue. It is a Strain quantity and is defined using the units of Strain from the active script unit system.


## `apex.environment.InitialStrainVariable`  (extends `InitialCondition`)
This class represents a spatially varying initial strain applied to Element. A single instance of this class may include a multiplicity of individual initial strain each applied to a different element. All of the individual initial strains composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one IPSTRAIN entry for each element within the scope of the region with which it is associated. The variation of strains across the elements that this initial stress references is defined using a DFEMFieldInitialStrain. This field defines the elements that represent the region to which this strain is applied as well as the variation of strain values across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldInitialStrain` — a DFEMFieldInitialStrain that identifies elements that represent the region to which this stress is applied as well as the distribution of stresses across that region.
#### `update(name: str, description: str, spatialTarget: apex.environment.DFEMFieldInitialStrain) -> None`
Updates one or more properties of the initial stress. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the initial stress.
- `description` — Updates the description of the initial stress.
- `spatialTarget` — Updates the spatialTarget.


## `apex.environment.InitialStress`  (extends `InitialCondition`)
An initial stress acting on Element used in nonlinear scenario(SOL400) only. The constant initial stress may be applied to solid, cell, surface, face, 3d/2d/1d mesh bodies and 3d/2d/1d elements. Note that the initial stress value are applied to Gaussion points. When used to generate a Nastran model this class will create a Nastran ISTRESS entry for each group of consistent element ids..
Properties: `coordinateSystemFlag`, `int1`, `intN`, `layer1`, `layerN`, `stress1`, `stress2`, `stress3`, `stress4`, `stress5`, `stress6`, `stress7`, `target`

Methods:

- `getCoordinateSystemFlag() -> int` — an integer to indicate the coordinate system that the initial stress is evaluated. -1 points to the element coordinate system and 0 points to the global coordinate system. If omitted, the default value is -1. Note that for CQUAD4 and CTRIA3 elements, only element coordinate system makes sense - even the label is 0, the initial stress will be transformed from global coordinate system to element coordinate system.
- `getInt1() -> int` — the first integration point number.
- `getIntN() -> int` — the last integration point number.
- `getLayer1() -> int` — the first integration layer number.
- `getLayerN() -> int` — the last integration layer number.
- `getStress1() -> float` — the stress value of the first component, for example, stress in X component for both solid and shell element, axial stress for beam element. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getStress2() -> float` — the stress value of the second component, for example, stress in Y component for both solid and shell element, twist stress for beam element. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getStress3() -> float` — the stress value of the third component, for example, stress in Z component for both solid and shell element. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getStress4() -> float` — the stress value of the fourth component, for example, stress in XY component for both solid and shell element. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getStress5() -> float` — the stress value of the fifth component, for example, stress in YZ component for both solid and shell element. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getStress6() -> float` — the stress value of the sixth component, for example, stress in ZX component for both solid and shell element. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getStress7() -> float` — the stress value of the seventh component, hydrostatic pressure for Herrmann elements only. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the initial stress will be applied to. Initial stresses may be assigned to solid, cell, surface, face, 3d/2d/1d mesh bodies and 3d/2d/1d elements. Initial stresses assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, target: apex.EntityCollection, int1: int, intN: int, layer1: int, layerN: int, stress1: float, stress2: float, stress3: float, stress4: float, stress5: float, stress6: float, stress7: float, coordinateSystemFlag: int) -> None`
Updates one or more properties of the initial stress. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the initial stress.
- `description` — Updates the description of the initial stress.
- `target` — Updates the target.
- `int1` — Updates the int1.
- `intN` — Updates the intN.
- `layer1` — Updates the layer1.
- `layerN` — Updates the layerN.
- `stress1` — Updates the stress1. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `stress2` — Updates the stress2. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `stress3` — Updates the stress3. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `stress4` — Updates the stress4. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `stress5` — Updates the stress5. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `stress6` — Updates the stress6. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `stress7` — Updates the stress7. It is a Pressure(Stress) quantity and is defined using the units of Pressure(Stress) from the active script unit system.
- `coordinateSystemFlag` — Updates the coordinateSystemFlag.


## `apex.environment.InitialStressVariable`  (extends `InitialCondition`)
This class represents a spatially varying initial stress applied to Element. A single instance of this class may include a multiplicity of individual initial stress each applied to a different element. All of the individual initial stresses composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one ISTRESS entry for each element within the scope of the region with which it is associated. The variation of stresses across the elements that this initial stress references is defined using a DFEMFieldInitialStress. This field defines the elements that represent the region to which this stress is applied as well as the variation of stress across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldInitialStress` — a DFEMFieldInitialStress that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(name: str, description: str, spatialTarget: apex.environment.DFEMFieldInitialStress) -> None`
Updates one or more properties of the initial stress. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name .
- `description` — Updates the description.
- `spatialTarget` — Updates the spatialTarget.


## `apex.environment.InitialTemperature`  (extends `Entity`, `IName`, `IUserAttributes`, `IDisplayable`, `IUserHighlightable`)
The InitialTemperature is an environment initial condition applied to local model regions. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: InitialTemperatureNodal.
Properties: `id`, `initialTemperatureValue`, `target`

Methods:

- `getId() -> int` — The ID of the InitialTemperature. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: InitialTemperatureNodal.
- `getInitialTemperatureValue() -> float` — The initial temperature value. Default value is 20 degrees centigrade in the standard SI unit system. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: InitialTemperatureNodal.
- `getTarget() -> apex.EntityCollection` — The target entities that the InitialTemperature is applied to. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: InitialTemperatureNodal.
#### `update(name: str, description: str, target: apex.EntityCollection, initialTemperatureValue: float, id: int) -> None`
Update this Initial Temperature condition. One or more properties may be updated in each call to update(). THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: InitialTemperatureNodal.

- `name` — Update the name of the TemperatureInitialCondition
- `description` — Update the description of the TemperatureInitialCondition
- `target` — Update the target of the TemperatureInitialCondition
- `initialTemperatureValue` — Update the temperature value of the TemperatureInitialCondition
- `id` — The ID of the InitialTemperature.


## `apex.environment.InitialTemperatureDefault`  (extends `InitialCondition`)
The default initial temperature applied to entities that are not associated with other temperature loads.
Properties: `defaultTemperature`

Methods:

- `getDefaultTemperature() -> float` — the default temperature value. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `update(name: str, description: str, id: int, defaultTemperature: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id.
- `defaultTemperature` — Updates the defaultTemperature. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.InitialTemperatureGradient2D`  (extends `InitialCondition`)
A spatially invariant initial temperature acting on 2D elements(plate, membrane, and combination elements) by an average temperature and a thermal gradient through the thickness. The constant temperature load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPP1 entry.
Properties: `target`, `temperatureLowerSurface`, `temperatureReferencePlane`, `temperatureUpperSurface`, `thermalGradient`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Forces may be assigned to Surfaces, Faces, 2D Mesh Bodies and 2D Elements. Temperatures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `getTemperatureLowerSurface() -> float` — the temperature for stress calculation at points on the lower surface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureReferencePlane() -> float` — the temperature applied on the element reference plane. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureUpperSurface() -> float` — the temperature for stress calculation at points on the upper surface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradient() -> float` — the effective linear thermal gradient. It represents a quantity and must be specified using units of thermal gradient from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureReferencePlane: float, thermalGradient: float, temperatureLowerSurface: float, temperatureUpperSurface: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureReferencePlane` — Updates the temperatureReferencePlane. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradient` — Updates the thermalGradient. It represents a quantity and must be specified using units of thermal gradient from the active script unit system.
- `temperatureLowerSurface` — Updates the temperatureLowerSurface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureUpperSurface` — Updates the temperatureUpperSurface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.InitialTemperatureGradient2DHeat`  (extends `InitialCondition`)
A spatially invariant initial temperature acting on Nodes belong to heat transfer shell elements used in nonlinear scenario. The constant temperature load may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPN1 entry.
Properties: `target`, `temperatureBottom`, `temperatureMid`, `temperatureTop`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Surfaces, Faces, 2D Mesh Bodies and Nodes. Temperatures assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTemperatureBottom() -> float` — the temperature at bottom location through the thickness. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureMid() -> float` — the temperature at mid location through the thickness. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureTop() -> float` — the temperature at top location through the thickness. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureTop: float, temperatureBottom: float, temperatureMid: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureTop` — Updates the temperatureTop. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureBottom` — Updates the temperatureBottom. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureMid` — Updates the temperatureMid. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.InitialTemperatureGradient2DHeatVariable`  (extends `InitialCondition`)
This class represents a spatially varying initial temperature load applied to 2D heat transfer elements. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPN1 entry for each element within the scope of the region with which it is associated.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradient2DHeat` — a DFEMFieldTemperatureGradient2DHeat that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2DHeat) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load.
- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `spatialTarget` — Updates the spatialTarget of the load.


## `apex.environment.InitialTemperatureGradient2DVariable`  (extends `InitialCondition`)
This class represents a spatially varying initial temperature load applied to 2D elements by an average temperature and a thermal gradient through the thickness. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPP1 entry for each element within the scope of the region with which it is associated.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradient2D` — a DFEMFieldTemperatureGradient2D that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2D) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the temperature load.
- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `spatialTarget` — Updates the spatialTarget of the temperature load.


## `apex.environment.InitialTemperatureGradientBeam2`  (extends `InitialCondition`)
A spatially invariant initial temperature acting on 1D elements with two nodes. The constant temperature load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPRB entry.
Properties: `inputType`, `target`, `temperatureEndA`, `temperatureEndB`, `temperaturePointCendA`, `temperaturePointCendB`, `temperaturePointDendA`, `temperaturePointDendB`, `temperaturePointEendA`, `temperaturePointEendB`, `temperaturePointFendA`, `temperaturePointFendB`, `thermalGradient1A`, `thermalGradient1B`, `thermalGradient2A`, `thermalGradient2B`

Methods:

- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Curves, Edges, 1D Mesh Bodies and 1D Elements. Temperatures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `getTemperatureEndA() -> float` — the temperature value at end A on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureEndB() -> float` — the temperature value at end B on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendA() -> float` — the temperature value on point C at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendB() -> float` — the temperature value on point C at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendA() -> float` — the temperature value on point D at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendB() -> float` — the temperature value on point D at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendA() -> float` — the temperature value on point E at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendB() -> float` — the temperature value on point E at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendA() -> float` — the temperature value on point F at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendB() -> float` — the temperature value on point F at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradient1A() -> float` — the effective linear thermal gradient in direction 1 on end A.
- `getThermalGradient1B() -> float` — the effective linear thermal gradient in direction 1 on end B.
- `getThermalGradient2A() -> float` — the effective linear thermal gradient in direction 2 on end A.
- `getThermalGradient2B() -> float` — the effective linear thermal gradient in direction 2 on end B.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, thermalGradient1A: float, thermalGradient1B: float, thermalGradient2A: float, thermalGradient2B: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureEndA` — Updates the temperatureEndA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureEndB` — Updates the temperatureEndB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradient1A` — Update the thermalGradient1A.
- `thermalGradient1B` — Update the thermalGradient1B.
- `thermalGradient2A` — Update the thermalGradient2A.
- `thermalGradient2B` — Update the thermalGradient2B.
- `temperaturePointCendA` — Updates the temperaturePointCendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendA` — Updates the temperaturePointDendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendA` — Updates the temperaturePointEendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendA` — Updates the temperaturePointFendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointCendB` — Updates the temperaturePointCendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendB` — Updates the temperaturePointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendB` — Updates the temperaturePointEendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendB` — Updates the temperaturePointFendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `inputType` — Updates the inputType.


## `apex.environment.InitialTemperatureGradientBeam2Variable`  (extends `InitialCondition`)
This class represents a spatially varying initial temperature applied to 1D Element with two nodes. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPRB entry for each element within the scope of the region with which it is associated. The variation of temperatures across the elements that this temperature references is defined using a DFEMFieldBeamDistributedLoad2. This field defines the elements that represent the region to which this temperature is applied as well as the variation of temperature values across that region. Two different types of temperature distributions are supported by DFEMFieldBeamDistributedLoad2, "Element uniform" distributions enable definition of a uniform temperature for each element within the scope of the initial condition. "Element variable" distributions enable definition of a variable temperature for each element within the scope of the initial condition.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradientBeam2` — a DFEMFieldTemperatureBeam2 that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam2) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.InitialTemperatureGradientBeam3`  (extends `InitialCondition`)
A spatially invariant initial temperature acting on 1D elements with three nodes. The constant temperature load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPB3 entry.
Properties: `inputType`, `target`, `temperatureEndA`, `temperatureEndB`, `temperatureMidC`, `temperaturePointCendA`, `temperaturePointCendB`, `temperaturePointCmidC`, `temperaturePointDendA`, `temperaturePointDendB`, `temperaturePointDmidC`, `temperaturePointEendA`, `temperaturePointEendB`, `temperaturePointEmidC`, `temperaturePointFendA`, `temperaturePointFendB`, `temperaturePointFmidC`, `thermalGradientYA`, `thermalGradientYB`, `thermalGradientYC`, `thermalGradientZA`, `thermalGradientZB`, `thermalGradientZC`

Methods:

- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B and mid C. If the inputType is element variable, all temperature values and thermal gradients can be defined.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Curves, Edges, 1D Mesh Bodies and 1D Elements. Temperatures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `getTemperatureEndA() -> float` — the temperature value at end A on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureEndB() -> float` — the temperature value at end B on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureMidC() -> float` — the temperature value at a point C between end A and end B. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendA() -> float` — the temperature value on point C at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendB() -> float` — the temperature value on point C at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCmidC() -> float` — the temperature value on point C at mid A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendA() -> float` — the temperature value on point D at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendB() -> float` — the temperature value on point D at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDmidC() -> float` — the temperature value on point D at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendA() -> float` — the temperature value on point E at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendB() -> float` — the temperature value on point E at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEmidC() -> float` — the temperature value on point E at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendA() -> float` — the temperature value on point F at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendB() -> float` — the temperature value on point F at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFmidC() -> float` — the temperature value on point F at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradientYA() -> float` — the effective linear thermal gradient in local direction y on end A.
- `getThermalGradientYB() -> float` — the effective linear thermal gradient in direction y on end B.
- `getThermalGradientYC() -> float` — the effective linear thermal gradient in direction y on mid C.
- `getThermalGradientZA() -> float` — the effective linear thermal gradient in direction z on end A.
- `getThermalGradientZB() -> float` — the effective linear thermal gradient in direction z on end B.
- `getThermalGradientZC() -> float` — the effective linear thermal gradient in direction z on mid C.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, temperatureMidC: float, thermalGradientYA: float, thermalGradientZA: float, thermalGradientYB: float, thermalGradientZB: float, thermalGradientYC: float, thermalGradientZC: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, temperaturePointCmidC: float, temperaturePointDmidC: float, temperaturePointEmidC: float, temperaturePointFmidC: float, inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureEndA` — Updates the temperatureEndA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureEndB` — Updates the temperatureEndB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureMidC` — Updates the temperatureMidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradientYA` — Updates the thermalGradientYA.
- `thermalGradientZA` — Updates the thermalGradientZA.
- `thermalGradientYB` — Updates the thermalGradientYB.
- `thermalGradientZB` — Updates the thermalGradientZB.
- `thermalGradientYC` — Updates the thermalGradientYC.
- `thermalGradientZC` — Updates the thermalGradientZC.
- `temperaturePointCendA` — Updates the temperaturePointCendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendA` — Updates the temperaturePointDendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendA` — Updates the temperaturePointEendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendA` — Updates the temperaturePointFendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointCendB` — Updates the temperaturePointCendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendB` — Updates the temperaturePointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendB` — Updates the temperaturePointEendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendB` — Updates the temperaturePointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointCmidC` — Updates the temperaturePointCmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDmidC` — Updates the temperaturePointDmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEmidC` — Updates the temperaturePointEmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFmidC` — Updates the temperaturePointFmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `inputType` — Updates the inputType.


## `apex.environment.InitialTemperatureGradientBeam3Variable`  (extends `InitialCondition`)
This class represents a spatially varying initial temperature applied to 1D Element with three nodes. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPB3 entry for each element within the scope of the region with which it is associated. The variation of temperatures across the elements that this temperature references is defined using a DFEMFieldBeamDistributedLoad3. This field defines the elements that represent the region to which this temperature is applied as well as the variation of temperature values across that region. Two different types of temperature distributions are supported by DFEMFieldBeamDistributedLoad3, "Element uniform" distributions enable definition of a uniform temperature for each element within the scope of the initial condition. "Element variable" distributions enable definition of a variable temperature for each element within the scope of the initial condition.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradientBeam3` — a DFEMFieldTemperatureBeam3 that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam3) -> None`
Update method. One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name.
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.InitialTemperatureNodal`  (extends `InitialCondition`)
A spatially invariant initial temperature acting on Nodes. The constant temperature load may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMP entry.
Properties: `target`, `temperatureValue`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D, 2D and 3D Mesh Bodies and Nodes. Temperatures assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTemperatureValue() -> float` — the temperature value. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureValue: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureValue` — Updates the temperatureValue. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.InitialTemperatureNodalVariable`  (extends `InitialCondition`)
This class represents a spatially varying initial temperature load applied to Nodes. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different node. All of the individual loads composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMP entry for each node within the scope of the region with which it is associated. The variation of temperature load across the nodes that this load references is defined using a DFEMFieldTemperatureNodal. This field defines nodes that represent the region to which this load is applied as well as the variation of load values across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureNodal` — a DFEMFieldLoadDistributed that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureNodal) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.Load`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Load is a base class for all Load types supported in Apex.
Properties: `id`

Methods:

- `getId() -> int` — the id of the load.

## `apex.environment.LoadAccelerationNodal`  (extends `Load`)
A spatially invariant acceleration load acting on Node. The load direction and magnitude are defined by a load vector with a scale factor. The vector is defined by three components and a coordinate system. The constant acceleration load may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran ACCEL1 entry.
Properties: `accelerationVectorX`, `accelerationVectorY`, `accelerationVectorZ`, `orientation`, `scaleFactor`, `target`

Methods:

- `getAccelerationVectorX() -> float` — the X component of the acceleration vector. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getAccelerationVectorY() -> float` — the Y component of the acceleration vector. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getAccelerationVectorZ() -> float` — the Z component of the acceleration vector. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getOrientation() -> apex.IOrientation` — the orientation used to define the direction of the acceleration vector. Currently it only accepts a coordinate system object.
- `getScaleFactor() -> float` — an optional scale factor that will be applied to the acceleration vectors. The magnitude of the acceleration load applied to each Node in the target is based on the product of the resultant of the provided acceleration vector and this scale factor.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Acceleration load will be applied to. Acceleration loads may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D, 2D and 3D Mesh Bodies and Nodes. Acceleration loads assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, orientation: apex.IOrientation, scaleFactor: float, accelerationVectorX: float, accelerationVectorY: float, accelerationVectorZ: float, target: apex.EntityCollection) -> None`
Updates one or more properties of the Acceleration. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the acceleration load.
- `description` — Updates the description of the acceleration load.
- `id` — Updates the id of the acceleration load.
- `orientation` — Updates the orientation of the acceleration load.
- `scaleFactor` — Updates the scaleFactor.
- `accelerationVectorX` — Updates the accelerationVectorX. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `accelerationVectorY` — Updates the accelerationVectorY. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `accelerationVectorZ` — Updates the accelerationVectorZ. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `target` — Updates the target of the acceleration load.


## `apex.environment.LoadAccelerationNodalVariable`  (extends `Load`)
This class represents a spatially varying acceleration load applied to Node. A single instance of this class may include a multiplicity of individual acceleration loads each applied to a different node. All of the individual acceleration loads composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one ACCEL1 entry for each node within the scope of the region with which it is associated.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldAccelerationNodal` — a DFEMFieldAccelerationNodal that identifies nodes that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldAccelerationNodal) -> None`
Updates one or more properties of the Acceleration load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load.
- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `spatialTarget` — Updates the spatialTarget of the load.


## `apex.environment.LoadAccelerationSpatial`  (extends `Load`)
A static acceleration load acting on whole model, the load may vary along one component direction: X, Y and Z. When used to generate a Nastran model this class will create a Nastran ACCEL entry in the model.
Properties: `accelerationVectorX`, `accelerationVectorY`, `accelerationVectorZ`, `componentDirection`, `loadVariation`, `orientation`

Methods:

- `getAccelerationVectorX() -> float` — the X component of the acceleration vector. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getAccelerationVectorY() -> float` — the Y component of the acceleration vector. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getAccelerationVectorZ() -> float` — the Z component of the acceleration vector. It is an Acceleration quantity and must be defined using the units of Acceleration from the active script unit system.
- `getComponentDirection() -> apex.attribute.ComponentDirectionAcceleration` — the component direction of the acceleration variation in the specified coordinate system.
- `getLoadVariation() -> dict` — The load variation along the component direction of the coordinate system. It is a dictionary with only two elements to represent the load variation along the axis: the value of the first element is a list of locations along the load direction, the value of the second element is a list of load scale factors associated with the locations. For example, loadVariation = {"locations": [0.00,1.00,2.00], "scale_factors": [1.00, 1.26, 2.37]} Note that both the lists of direction and scale factor require at least two values.
- `getOrientation() -> apex.IOrientation` — an optional CoordinateSystem used to define the orientation of the Acceleration components.
#### `update(name: str, description: str, id: int, orientation: apex.IOrientation, accelerationVectorX: float, accelerationVectorY: float, accelerationVectorZ: float, componentDirection: apex.attribute.ComponentDirectionAcceleration, loadVariation: dict) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `orientation` — Update the orientation.
- `accelerationVectorX` — Update the loadVectorX.
- `accelerationVectorY` — Update the loadVectorY.
- `accelerationVectorZ` — Update the loadVectorZ.
- `componentDirection` — Update the componentDirection.
- `loadVariation` — Update the loadVariation.


## `apex.environment.LoadAreaFactor`  (extends `Load`)
A load scale(area) factor applied to Node. The translation area scale factors can be used as force components, while the rotation area scale factors can be used as moment components. The components are defined in the basic coordinate system. The constant load scale(area) factor may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create one or several DAREA entries on each Node.
Properties: `scaleFactorRx`, `scaleFactorRy`, `scaleFactorRz`, `scaleFactorX`, `scaleFactorY`, `scaleFactorZ`, `target`

Methods:

- `getScaleFactorRx() -> float` — the load scale(area) factor in the rotation X axis, scaleFactorRx is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getScaleFactorRy() -> float` — the load scale(area) factor in the rotation Y axis, scaleFactorRy is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getScaleFactorRz() -> float` — the load scale(area) factor in the rotation Z axis, scaleFactorRz is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getScaleFactorX() -> float` — the load scale(area) factor in the translation X axis, scaleFactorX is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getScaleFactorY() -> float` — the load scale(area) factor in the translation Y axis, scaleFactorY is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getScaleFactorZ() -> float` — the load scale(area) factor in the translation Z axis, scaleFactorZ is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the load area factor will be applied to. Load area factors may be assigned to Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Load area factors assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, scaleFactorX: float, scaleFactorY: float, scaleFactorZ: float, scaleFactorRx: float, scaleFactorRy: float, scaleFactorRz: float) -> None`
Updates one or more properties of the load area factor. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load area factor.
- `description` — Updates the description of the load area factor.
- `id` — Updates the id of the load area factor.
- `target` — Updates the target of the load area factor.
- `scaleFactorX` — Updates the scaleFactorX. scaleFactorX is a Force quantity and must be defined using the units of Force from the active script unit system.
- `scaleFactorY` — Update the scaleFactorY. scaleFactorY is a Force quantity and must be defined using the units of Force from the active script unit system.
- `scaleFactorZ` — Update the scaleFactorZ. scaleFactorZ is a Force quantity and must be defined using the units of Force from the active script unit system.
- `scaleFactorRx` — Update the scaleFactorRx. scaleFactorRx is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `scaleFactorRy` — Update the scaleFactorRy. scaleFactorRy is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `scaleFactorRz` — Update the scaleFactorRz. scaleFactorRz is a Moment quantity and must be defined using the units of Moment from the active script unit system.


## `apex.environment.LoadAreaFactorVariable`  (extends `Load`)
This class represents a load scale(area) factor in the six components. The translation components can be used a force vector while translation components can be used a moment vector in static analysis. A single instance of this class may include a multiplicity of individual load area factor each applied to a different Node. All of the individual load area factors are composed by this LoadAreaFactor and share a common ID. When used in a Nastran simulation this class will give rise to a DAREA entry for each component on each Node within the scope of the region to which it is associated. LoadAreaFactor can be configured to represent either a spatially constant or spatially varying field of load area factors. The spatially constant configuration defines a single load area factor and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of load area factors to assign a different load area factors to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadAreaFactor() or apex.environment.createLoadAreaFactorVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldLoadAreaFactor` — a DFEMFieldForceComponent that identifies nodes that represent the region to which this load area factor is applied as well as the distribution of load area factors across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadAreaFactor) -> None`
Updates one or more properties of the load area factor. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load area factor.
- `name` — Updates the name of the load area factor.
- `description` — Updates the description of the load area factor.
- `spatialTarget` — Updates the spatialTarget of the load area factor.


## `apex.environment.LoadCombinationDynamic`  (extends `Load`)
The dynamic load combination to collect one or several dynamic loads to combine as one load. When used to generate a Nastran model this class will create a Nastran DLOAD entry.
Properties: `combinedLoads`, `overallScaleFactor`

Methods:

- `getCombinedLoads() -> dict` — a dictionary to define the combined loads and the scale factor for each load. For each element, the key is the load name, the value is the scale factor associated with the load. For example, combinedLoads = {"Dynamic Load 1": 1.0, "Dynamic Load 2": 2.0, "Dynamic Load 3": 1.2}
- `getOverallScaleFactor() -> float` — the overall scale factor applied to all the loads to be combined.
#### `update(name: str, description: str, id: int, overallScaleFactor: float, combinedLoads: dict) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `overallScaleFactor` — Update the overallScaleFactor.
- `combinedLoads` — Update the combinedLoads.


## `apex.environment.LoadCombinationStatic`  (extends `Load`)
The load combination to collect one or several static loads as one load. When used to generate a Nastran model this class will create a LOAD DELAY entry.
Properties: `combinedLoads`, `overallScaleFactor`

Methods:

- `getCombinedLoads() -> dict` — a dictionary to define the combined loads and the scale factor for each load. For each element, the key is the load name, the value is the scale factor associated with the load. For example, combinedLoads = {"Force 1": 1.0, "Force 2": 2.0, "Pressure 3": 1.2}
- `getOverallScaleFactor() -> float` — the overall scale factor applied to all the loads to be combined.
#### `update(name: str, description: str, id: int, overallScaleFactor: float, combinedLoads: dict) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `overallScaleFactor` — Update the overallScaleFactor.
- `combinedLoads` — Update the combinedLoads.


## `apex.environment.LoadDeformationAxial`  (extends `Load`)
A spatially invariant enforced axial deformation load acting on 1D Element used for static problems. The constant deformation load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran DEFORM entry to an element.
Properties: `deformation`, `target`

Methods:

- `getDeformation() -> float` — the deformation value along the element axis. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Deformation will be applied to. Deformations may be assigned to Curves, Edges, 1D Mesh Bodies and Elements. Deformations assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, deformation: float) -> None`
Updates one or more properties of the Deformation. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `target` — Updates the target of the load.
- `deformation` — Updates the deformation. It is a Length quantity and must be defined using the units of Length from the active script unit system.


## `apex.environment.LoadDeformationAxialVariable`  (extends `Load`)
A deformation applied to 1d elements only.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldDeformationAxial` — the field that defines the load distribution.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldDeformationAxial) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadDistributed`  (extends `Load`)
A spatially invariant distributed load acting on 2D elements or the faces of 3D elements. The load magnitude is a Pressure and the direction is defined by three components in a coordinate system. The constant distributed load may be applied to one or more 2D elements or 3D element faces directly or through their association to 2D mesh bodies and/or geometry faces. When used to generate a Nastran model this class will create a Nastran PLOAD4 entry.
Properties: `directionX`, `directionY`, `directionZ`, `orientation`, `pressure`, `target`

Methods:

- `getDirectionX() -> float` — the X component of the direction vector.
- `getDirectionY() -> float` — the Y component of the direction vector.
- `getDirectionZ() -> float` — the Z component of the direction vector.
- `getOrientation() -> apex.IOrientation` — the orientation used to define the direction of the pressure. Currently it only accepts a coordinate system object.
- `getPressure() -> float` — the pressure magnitude value. It is a Pressure quantity and is defined using the units of Pressure from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the load will be applied to. Loads may be assigned to Faces, 2D Mesh Bodies, 2D Elements and Element Faces. Loads assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, pressure: float, orientation: apex.IOrientation, directionX: float, directionY: float, directionZ: float) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `target` — Updates the target of the load.
- `pressure` — Updates the pressure value of the load.
- `orientation` — Updates the orientation of the load.
- `directionX` — Updates the directionVectorX of the load.
- `directionY` — Updates the directionVectorY of the load.
- `directionZ` — Updates the directionVectorZ of the load.


## `apex.environment.LoadDistributedBeam2`  (extends `Load`)
A spatially static load acting on 1D Element with two Nodes. It can be a concentrated or distributed Force or Moment. The load direction can be relative to the basic coordinate system or element coordinate system. Two different types of loads distributions are supported, "Element uniform" distributions enable definition of a uniform/concentrated load for each element within the scope of the load. "Element variable" distributions enable definition of a variable distributed load for each element within the scope of the load. The constant load may be applied to one or more 1D elements directly or through their association to 1D mesh bodies and/or geometry edges. When used to generate a Nastran model this class will create a Nastran PLOAD1 entry for each element.
Properties: `distanceX1`, `distanceX2`, `inputType`, `loadFactorX1`, `loadFactorX2`, `loadType`, `scaleType`, `target`

Methods:

- `getDistanceX1() -> float` — the distance X1 along element axis from end A. The distance may be a fractional value of the element length or a length value, depending on the scaleType.
- `getDistanceX2() -> float` — the distance X2 along element axis from end A. The distance may be a fractional value of the element length or a length value, depending on the scaleType.
- `getInputType() -> apex.attribute.InputType` — an optional argument to define the load distribution on a single element. If the inputType is element uniform, the loadFactorX2 is always equal to loa dFactorX1, distanceX1 is 0.0, distanceX2 is 1.0, scaleType is fractional. If omitted, the default value is element uniform.
- `getLoadFactorX1() -> float` — the load factor at the position of distance X1 from end A. The unit of the load factor value depends on the loadType, it can be a force or a moment.
- `getLoadFactorX2() -> float` — the load factor at the position of distance X2 from end A. The unit of the load factor value depends on the loadType, it can be a force or a moment.
- `getLoadType() -> apex.attribute.LoadTypeDistributedBeam2` — the loadType of the beam distributed load applied to beam element with two nodes. apex.attribute.LoadTypeBeam2.ForceX, the load is concentrated force in X direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceY, the load is concentrated force in Y direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceZ, the load is concentrated force in Z direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentX, the load is moment in X direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentY, the load is moment in Y direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.MomentZ, the load is moment in Z direction of the basic coordinate system. apex.attribute.LoadTypeBeam2.ForceXE, the load is concentrated force in X direction of the element coordinate system. apex.attribute.LoadTypeBeam2.ForceYE, the load is concentrated force in Y direction of the element coordinate system. apex.attribute.LoadTypeBeam2.ForceZE, the load is concentrated force in Z direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentXE, the load is moment in X direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentYE, the load is moment in Y direction of the element coordinate system. apex.attribute.LoadTypeBeam2.MomentZE, the load is moment in Z direction of the element coordinate system.
- `getScaleType() -> apex.attribute.ScaleTypeDistributedBeam2` — the scaleType of the load factors. apex.attribute.ScaleTypeBeam.Length, the distance values are actual distances along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeam.Fractional, the distance values are are ratios of the distance along the axis to the total length, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeam.LengthProjected, the distance values are projected lengths along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeBeam.FractionalProjected, the distance values are ratios of the actual distance to the length of the bar (CBAR entry), and if distance1 != distance 2, then the distributed load is specified in terms of the projected length of the bar.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the load will be applied to. Loads may be assigned to Curve, Edge, 1D Mesh Bodies and 1D Elements. Loads assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, loadType: apex.attribute.LoadTypeDistributedBeam2, scaleType: apex.attribute.ScaleTypeDistributedBeam2, distanceX1: float, loadFactorX1: float, distanceX2: float, loadFactorX2: float, inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Update the description of the load.
- `id` — Updates the id of the load.
- `target` — Update the target of the load.
- `loadType` — Updates the loadType.
- `scaleType` — Updates the scaleType.
- `distanceX1` — Updates the distanceX1. The distance may be a fractional value of the element length or a length value, depending on the scaleType.
- `loadFactorX1` — Updates the loadFactorX1. The unit of the load factor value depends on the loadType, it can be a force or a moment.
- `distanceX2` — Updates the distanceX2. The distance may be a fractional value of the element length or a length value, depending on the scaleType.
- `loadFactorX2` — Updates the loadFactorX1. The unit of the load factor value depends on the loadType, it can be a force or a moment.
- `inputType` — Updates the inputType of the load.


## `apex.environment.LoadDistributedBeam2Variable`  (extends `Load`)
This class represents a spatially varying load applied to 1D Element with two nodes. It can be a concentrated or distributed Force or Moment on each element. The load direction can be relative to the basic coordinate system or element coordinate system. A single instance of this class may include a multiplicity of individual loads each applied to a different element. All of the individual load composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one PLOAD1 entry for each element within the scope of the region with which it is associated. The variation of load across the elements that this load references is defined using a DFEMFieldBeamDistributedLoad2. This field defines the elements that represent the region to which this load is applied as well as the variation of load values across that region. Two different types of load distributions are supported by DFEMFieldBeamDistributedLoad2, "Element uniform" distributions enable definition of a uniform/concentrated load for each element within the scope of the load. "Element variable" distributions enable definition of a variable distributed load for each element within the scope of the load.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldLoadDistributedBeam2` — a DFEMFieldLoadDistributedBeam2 that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadDistributedBeam2) -> None`
Updates one or more properties of the Load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load.
- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `spatialTarget` — Updates the spatialTarget of the load.


## `apex.environment.LoadDistributedBeam3`  (extends `Load`)
A spatially static load acting on 1D Element with three Nodes. It can be a concentrated or distributed Force or Moment. The load direction can be relative to basic coordinate system, element coordinate system, local coordinate system of the beam cross section, or a user defined coordinate system. The load magnitude on each node of the beam is (loadScaleFacto)*(Magnitude)*(loadVector). Two different types of loads distributions are supported, "Element uniform" distributions enable definition of a uniform/concentrated load for each element within the scope of the load. "Element variable" distributions enable definition of a variable distributed load for each element within the scope of the load. The constant load may be applied to one or more 1D elements directly or through their association to 1D mesh bodies and/or geometry edges. When used to generate a Nastran model this class will create a Nastran PLOADB3 entry for each element.
Properties: `coordinateSystem`, `inputType`, `loadScaleFactor`, `loadType`, `loadVectorX`, `loadVectorY`, `loadVectorZ`, `magnitudeEndA`, `magnitudeEndB`, `magnitudeMidC`, `orientationType`, `target`

Methods:

- `getCoordinateSystem() -> apex.IOrientation` — the user defined coordinate system in which the load vector is defined. This argument must be provided when the orientationType is "apex.attribute.OrientationTypeBeam3.Local". This argument will be ignored when the orientationType is "apex.attribute.OrientationTypeBeam3.Basic" or "apex.attribute.OrientationTypeBeam3.Element".
- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, the loadScaleFactor is 1.0, magnitudes on end A, end B and mid C are 1.0. If the inputType is element variable, above parameters are defined by user.
- `getLoadScaleFactor() -> float` — the load scale factor. The load vector is scaled by the factor on all locations on a single element.
- `getLoadType() -> apex.attribute.LoadTypeDistributedBeam3` — the loadType of the beam distributed load. apex.attribute.LoadTypeBeam3.Force, the load is a force. apex.attribute.LoadTypeBeam3.Moment, the load is a moment. apex.attribute.LoadTypeBeam3.Bimoment, the load is bimoment.
- `getLoadVectorX() -> float` — the X component of the load vector. The unit can be Force or Moment quantity(depending on loadType), which is defined by the units of Force/Moment from the active script unit system.
- `getLoadVectorY() -> float` — the Y component of the load vector. The unit can be Force or Moment quantity(depending on loadType), which is defined by the units of Force/Moment from the active script unit system.
- `getLoadVectorZ() -> float` — the Z component of the load vector. The unit can be Force or Moment quantity(depending on loadType), which is defined by the units of Force/Moment from the active script unit system.
- `getMagnitudeEndA() -> float` — the load magnitude at end A. The load vector is scaled by magnitude on end A.
- `getMagnitudeEndB() -> float` — the load magnitude at end B. The load vector is scaled by magnitude on end B.
- `getMagnitudeMidC() -> float` — the load magnitude at the point C which is between end A and end B. The load vector is scaled by magnitude on mid C.
- `getOrientationType() -> apex.attribute.OrientationTypeDistributedBeam3` — the orientation type of the load. apex.attribute.OrientationTypeBeam3.Basic, the load is defined in the basic coordinate system. apex.attribute.OrientationTypeBeam3.Element, the load is defined in the element coordinate system. apex.attribute.OrientationTypeBeam3.Local, the load is defined in the local coordinate system of the beam cross section. If the load is defined in a user defined local coordinate system, then this argument should be None and coordinateSystem is used.
- `getTarget() -> apex.EntityCollection` — the entityCollection that the load is applied to.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, coordinateSystem: apex.IOrientation, orientationType: apex.attribute.OrientationTypeDistributedBeam3, loadVectorX: float, loadVectorY: float, loadVectorZ: float, loadType: apex.attribute.LoadTypeDistributedBeam3, loadScaleFactor: float, magnitudeEndA: float, magnitudeEndB: float, magnitudeMidC: float, inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `target` — Updates the target of the load.
- `coordinateSystem` — Updates the coordinateSystem.
- `orientationType` — Updates the orientationType.
- `loadVectorX` — Updates the loadVectorX. The unit can be Force or Moment quantity(depending on loadType), which is defined by the units of Force/Moment from the active script unit system.
- `loadVectorY` — Updates the loadVectorY. The unit can be Force or Moment quantity(depending on loadType), which is defined by the units of Force/Moment from the active script unit system.
- `loadVectorZ` — Updates the loadVectorZ. The unit can be Force or Moment quantity(depending on loadType), which is defined by the units of Force/Moment from the active script unit system.
- `loadType` — Updates the loadType.
- `loadScaleFactor` — Updates the loadScaleFactor.
- `magnitudeEndA` — Updates the magnitudeEndA.
- `magnitudeEndB` — Updates the magnitudeEndB.
- `magnitudeMidC` — Updates the magnitudeMidC.
- `inputType` — Updates the inputType of the load.


## `apex.environment.LoadDistributedBeam3Variable`  (extends `Load`)
This class represents a spatially varying load applied to 1D Elements with three nodes. It can be a concentrated or distributed Force or Moment on each element. The load direction can be relative to the basic coordinate system, element coordinate system, local coordinate system of the beam cross section or a user defined local coordinate system. The load magnitude on each node of the beam is (loadScaleFactor)*(Magnitude)*(loadVector). A single instance of this class may include a multiplicity of individual loads each applied to a different element. All of the individual load composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one PLOADB3 entry for each element within the scope of the region with which it is associated. The variation of load across the elements that this load references is defined using a DFEMFieldBeamDistributedLoad3. This field defines the elements that represent the region to which this load is applied as well as the variation of load values across that region. Two different types of load distributions are supported by DFEMFieldBeamDistributedLoad, "Element uniform" distributions enable definition of a uniform/concentrated load for each element within the scope of the load. "Element variable" distributions enable definition of a variable distributed load for each element within the scope of the load.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldLoadDistributedBeam3` — a DFEMFieldLoadDistributedBeam3 that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadDistributedBeam3) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load.
- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `spatialTarget` — Updates the spatialTarget of the load.


## `apex.environment.LoadDistributedVariable`  (extends `Load`)
This class represents a spatially varying distributed load applied to 2D elements or the faces of 3D elements. The load direction is defined by three components in a coordinate system. A single instance of this class may include a multiplicity of individual distributed loads each applied to a different element/element face. All of the individual loads composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one PLOAD4 entry for each element/element face within the scope of the region with which it is associated. The variation of distributed loads across the elements that this load references is defined using a DFEMFieldLoadDistributed. This field defines both the elements/element faces that represent the region to which this load is applied as well as the variation of load values across that region. Two different types of load distributions are supported by DFEMFieldLoadDistributed, "Element uniform" distributions enable definition of a single distributed load value for each element/element face within the scope of the load "Element variable" distributions enable definition of a unique distributed load values at each corner node of each element/element face within the scope of this load.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldLoadDistributed` — a DFEMFieldLoadDistributed that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldLoadDistributed) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load.
- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `spatialTarget` — Updates the spatialTarget of the load.


## `apex.environment.LoadDynamicAcoustic`  (extends `Load`)
An acoustic source defined as a function of power vs. frequency. The excitation load should be only load area factor or scalar force. When used to generate a Nastran model this class will create a Nastran ACSRCE entry.
Properties: `excitationLoads`, `fluidBulkModulus`, `fluidDensity`, `phaseLead`, `phaseLeadValue`, `powerTable`, `powerValue`, `timeDelay`, `timeDelayValue`

Methods:

- `getExcitationLoads() -> apex.EntityCollection` — A collection of loads that will be used as the excitation loads of the dynamic load.
- `getFluidBulkModulus() -> float` — the bulk modulus of fluid. It is a Pressure(Stress) quantity and must be defined using the units of Pressure(Stress) from the active script unit system.
- `getFluidDensity() -> float` — the density of fluid. It is a Density quantity and must be defined using the units of Density from the active script unit system.
- `getPhaseLead() -> apex.environment.Load` — a PhaseLead or PhaseLeadVariable object to define the phase lead in different dofs.
- `getPhaseLeadValue() -> float` — a phase lead value used for all dofs.
- `getPowerTable() -> apex.chart.Table` — the table to define the power versus frequency.
- `getPowerValue() -> float` — the power value used for all frequencies. It is a Heat Transfer Rate(power) quantity and must be defined using the units of Heat Transfer Rate from the active script unit system.
- `getTimeDelay() -> apex.environment.Load` — a TimeDelay or TimeDelayVariable object to define the time delay in different dofs.
- `getTimeDelayValue() -> float` — a time delay value used for all dofs.
#### `update(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, phaseLead: apex.environment.Load, phaseLeadValue: float, powerTable: apex.chart.Table, powerValue: float, fluidDensity: float, fluidBulkModulus: float) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `excitationLoads` — Updates the excitationLoads of the load.
- `timeDelay` — Updates the timeDelay.
- `timeDelayValue` — Updates the timeDelayValue. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `phaseLead` — Updates the phaseLead.
- `phaseLeadValue` — Updates the phaseLeadValue. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `powerTable` — Updates the powerTable.
- `powerValue` — Updates the powerValue. It is a Heat Transfer Rate(power) quantity and must be defined using the units of Heat Transfer Rate from the active script unit system.
- `fluidDensity` — Updates the density of fluid. It is a Density quantity and must be defined using the units of Density from the active script unit system.
- `fluidBulkModulus` — Updates the bulk modulus of fluid. It is a Pressure(Stress) quantity and must be defined using the units of Pressure(Stress) from the active script unit system.


## `apex.environment.LoadDynamicFrequency1`  (extends `Load`)
A frequency-dependent dynamic load defined by real and imaginary parts. It is used in frequency response problem. The dynamic load is driven by one or several excitation loads. Each excitation load must be a static or thermal load that defines the load application region. When used to generate a Nastran model this class will create a Nastran RLOAD1 entry.
Properties: `excitationLoads`, `imagTable`, `imagValue`, `loadType`, `phaseLead`, `phaseLeadValue`, `realPartTable`, `realPartValue`, `timeDelay`, `timeDelayValue`

Methods:

- `getExcitationLoads() -> apex.EntityCollection` — A collection of loads that will be used as the excitation loads of the dynamic load.
- `getImagTable() -> apex.chart.Table` — a table to define the imaginary part value versus frequency.
- `getImagValue() -> float` — the imaginary value used for all frequencies.
- `getLoadType() -> apex.attribute.DynamicLoadType` — the argument to define the dynamic excitation type.
- `getPhaseLead() -> apex.environment.Load` — the PhaseLead or PhaseLeadVariable object.
- `getPhaseLeadValue() -> float` — The phase lead value used for all frequencies. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getRealPartTable() -> apex.chart.Table` — a table to define the real part value versus frequency.
- `getRealPartValue() -> float` — a constant value as the real part used for all frequencies.
- `getTimeDelay() -> apex.environment.Load` — the TimeDelay or TimeDelayVariable object.
- `getTimeDelayValue() -> float` — the time delay value used for all frequencies. It is a Time quantity and must be defined using the units of Time from the active script unit system.
#### `update(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, phaseLead: apex.environment.Load, phaseLeadValue: float, realPartTable: apex.chart.Table, realPartValue: float, imagTable: apex.chart.Table, imagValue: float, loadType: apex.attribute.DynamicLoadType) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `excitationLoads` — Updates the excitationLoads.
- `timeDelay` — Updates the timeDelay.
- `timeDelayValue` — Updates the timeDelayValue.
- `phaseLead` — Updates the phaseLead.
- `phaseLeadValue` — Updates the phaseLeadValue.
- `realPartTable` — Updates the realPartTable.
- `realPartValue` — Updates the realPartValue.
- `imagTable` — Updates the imagTable.
- `imagValue` — Updates the imagValue.
- `loadType` — Updates the loadType.


## `apex.environment.LoadDynamicFrequency2`  (extends `Load`)
A frequency-dependent dynamic load defined by magnitude and phase angle. It is used in frequency response problem. The dynamic load is driven by one or several excitation loads. Each excitation load must be a static or thermal load that defines the load application region. When used to generate a Nastran model this class will create a Nastran RLOAD2 entry.
Properties: `excitationLoads`, `loadType`, `magnitude`, `magnitudeTable`, `phaseAngle`, `phaseAngleTable`, `phaseLead`, `phaseLeadValue`, `timeDelay`, `timeDelayValue`

Methods:

- `getExcitationLoads() -> apex.EntityCollection` — a collection of loads that will be used as the excitation loads of the dynamic load.
- `getLoadType() -> apex.attribute.DynamicLoadType` — the argument to define the dynamic excitation type.
- `getMagnitude() -> float` — the magnitude value used for all frequencies.
- `getMagnitudeTable() -> apex.chart.Table` — a table to define the magnitude value versus frequency.
- `getPhaseAngle() -> float` — a phase angle value used for all frequencies. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getPhaseAngleTable() -> apex.chart.Table` — a table to define the phase angle versus frequency.
- `getPhaseLead() -> apex.environment.Load` — a PhaseLead or PhaseLeadVariable object to define the phase lead in different dofs.
- `getPhaseLeadValue() -> float` — a phase lead value used for all dofs.It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getTimeDelay() -> apex.environment.Load` — a TimeDelay or TimeDelayVariable to define the time delay in different dofs.
- `getTimeDelayValue() -> float` — a time delay value used for all dofs. It is a Time quantity and must be defined using the units of Time from the active script unit system.
#### `update(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, phaseLead: apex.environment.Load, phaseLeadValue: float, magnitudeTable: apex.chart.Table, magnitude: float, phaseAngleTable: apex.chart.Table, phaseAngle: float, loadType: apex.attribute.DynamicLoadType) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `excitationLoads` — Updates the excitationLoads.
- `timeDelay` — Updates the timeDelay.
- `timeDelayValue` — Updates the timeDelayValue.
- `phaseLead` — Updates the phaseLead.
- `phaseLeadValue` — Updates the phaseLeadValue.
- `magnitudeTable` — Updates the magnitudeTable.
- `magnitude` — Updates the magnitude.
- `phaseAngleTable` — Updates the phaseAngleTable.
- `phaseAngle` — Updates the phaseAngle.
- `loadType` — Updates the loadType.


## `apex.environment.LoadDynamicTimeAnalytical`  (extends `Load`)
A time-dependent dynamic load defined by an analytical function. It is used in transient response analysis. The dynamic load is driven by one or several excitation loads. Each excitation load must be a static or thermal load that defines the load application region. When used to generate a Nastran model this class will create a Nastran TLOAD2 entry.
Properties: `excitationLoads`, `exponentialCoefficient`, `frequency`, `growthCoefficient`, `initialDisplacement`, `initialVelocity`, `loadType`, `phaseAngle`, `timeConstant1`, `timeConstant2`, `timeDelay`, `timeDelayValue`

Methods:

- `getExcitationLoads() -> apex.EntityCollection` — A collection of loads that will be used as the excitation loads of the dynamic load.
- `getExponentialCoefficient() -> float` — exponential coefficient.
- `getFrequency() -> float` — frequency in cycles per unit time. It is a Frequency quantity and must be defined using the units of Frequency from the active script unit system.
- `getGrowthCoefficient() -> float` — growth coefficient.
- `getInitialDisplacement() -> float` — the initial displacement of the dynamic load. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getInitialVelocity() -> float` — the initial velocity of the dynamic load. It is a Velocity quantity and must be defined using the units of Velocity from the active script unit system.
- `getLoadType() -> apex.attribute.DynamicLoadType` — the load type to define the dynamic excitation type.
- `getPhaseAngle() -> float` — phase angle in degrees. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getTimeConstant1() -> float` — time constant 1. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeConstant2() -> float` — time constant 2, must be >=time constant 1. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelay() -> apex.environment.Load` — a TimeDelay or TimeDelayVariable object to define the time delay in different dofs.
- `getTimeDelayValue() -> float` — a time delay value used for all dofs. It is a Time quantity and must be defined using the units of Time from the active script unit system.
#### `update(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, timeConstant1: float, timeConstant2: float, frequency: float, phaseAngle: float, exponentialCoefficient: float, growthCoefficient: float, initialDisplacement: float, initialVelocity: float, loadType: apex.attribute.DynamicLoadType) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `excitationLoads` — Update the excitationLoads.
- `timeDelay` — Updates the timeDelay.
- `timeDelayValue` — Updates the timeDelayValue. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeConstant1` — Updates the timeconstant1. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeConstant2` — Updates the timeConstant2. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `frequency` — Updates the frequency. It is a Frequency quantity and must be defined using the units of Frequency from the active script unit system.
- `phaseAngle` — Updates the phaseAngle. It is an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `exponentialCoefficient` — Updates the exponentialCoefficient.
- `growthCoefficient` — Updates the growthCoefficient.
- `initialDisplacement` — Updates the initialDisplacement. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `initialVelocity` — Updates the initialVelocity. It is a Velocity quantity and must be defined using the units of Velocity from the active script unit system.
- `loadType` — Update the loadType.


## `apex.environment.LoadDynamicTimeTabular`  (extends `Load`)
A time-dependent dynamic load defined by a table data or a constant value used for all times. It is used in transient response analysis. The dynamic load is driven by one or several excitation loads. Each excitation load must be a static or thermal load that defines the load application region. When used to generate a Nastran model this class will create a Nastran TLOAD1 entry.
Properties: `excitationLoads`, `functionTable`, `functionValue`, `initialDisplacement`, `initialVelocity`, `loadType`, `timeDelay`, `timeDelayValue`

Methods:

- `getExcitationLoads() -> apex.EntityCollection` — A collection of loads that will be used as the excitation loads of the dynamic load.
- `getFunctionTable() -> apex.chart.Table` — a table to define the function value versus time.
- `getFunctionValue() -> float` — the function value used for all times.
- `getInitialDisplacement() -> float` — the initial displacement of the dynamic load. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `getInitialVelocity() -> float` — the initial velocity of the dynamic load. It is a Velocity quantity and must be defined using the units of Velocity from the active script unit system.
- `getLoadType() -> apex.attribute.DynamicLoadType` — the load type to define the dynamic excitation type.
- `getTimeDelay() -> apex.environment.Load` — a TimeDelay or TimeDelayVariable object to define the time delay in different dofs.
- `getTimeDelayValue() -> float` — a time delay value used for all dofs. It is a Time quantity and must be defined using the units of Time from the active script unit system.
#### `update(name: str, description: str, id: int, excitationLoads: apex.EntityCollection, timeDelay: apex.environment.Load, timeDelayValue: float, functionTable: apex.chart.Table, functionValue: float, initialDisplacement: float, initialVelocity: float, loadType: apex.attribute.DynamicLoadType) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `excitationLoads` — Updates the excitationLoads of the load.
- `timeDelay` — Updates the timeDelay.
- `timeDelayValue` — Updates the timeDelayValue. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `functionTable` — Updates the functionTable.
- `functionValue` — Updates the functionValue.
- `initialDisplacement` — Updates the initialDisplacement. It is a Length quantity and must be defined using the units of Length from the active script unit system.
- `initialVelocity` — Updates the initialVelocity. It is a Velocity quantity and must be defined using the units of Velocity from the active script unit system.
- `loadType` — Updates the loadType of the load.


## `apex.environment.LoadEnforcedMotionRelative`  (extends `Load`)
An enforced relative displacement for a step only used in nonlinear analysis. The enforced motion has six components. The translation vector is defined by three translation components and rotation vector is defined by three rotation components. The vector may be defined relative to a local coordinate system. The constant enforced motion may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create one or several Nastran SPCR with SPC1 entries on each Node.
Properties: `orientation`, `rotationX`, `rotationY`, `rotationZ`, `target`, `translationX`, `translationY`, `translationZ`

Methods:

- `getOrientation() -> apex.IOrientation` — an optional CoordinateSystem used to define the orientation of the motion components. If omitted, the default is the basic coordinate system.
- `getRotationX() -> float` — the motion value in rotation X. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getRotationY() -> float` — the motion value in rotation Y. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getRotationZ() -> float` — the motion value in rotation Z. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the enforced motion will be applied to. Enforced motions may be assigned to Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Enforced motions assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTranslationX() -> float` — the motion value in translation X. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getTranslationY() -> float` — the motion value in translation Y. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getTranslationZ() -> float` — the motion value in translation Z. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, orientation: apex.IOrientation) -> None`
Updates one or more properties of the enforced motion. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name of the enforced motion.
- `description` — Update the description of the enforced motion.
- `id` — Update the id of the enforced motion.
- `target` — Update the target of the enforced motion.
- `translationX` — Updates the translationX. It is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `translationY` — updates the translationY. It is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `translationZ` — Updates the translationZ. It is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `rotationX` — Updates the rotationX. It is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `rotationY` — Update the rotationY. It is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `rotationZ` — Update the rotationZ. It is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `orientation` — Update the orientation of this LoadEnforcedMotionRelative


## `apex.environment.LoadEnforcedMotionRelativeVariable`  (extends `Load`)
This class represents a relative enforced displacement in both translation and rotation components. A single instance of this class may include a multiplicity of individual enforced motions each applied to a different Node. All of the individual enforced motions are composed by this LoadEnforcedMotionTotal and share a common ID. When used in a Nastran simulation this class will give rise to a SPCR entry with a SPC1 entry for component and each Node within the scope of the region to which it is associated. LoadEnforcedMotionTotalVariable can be configured to represent either a spatially constant or spatially varying field of enforced motions. The spatially constant configuration defines an enforced motion and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of enforced motions and coordinate systems to assign a different enforced motion to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadEnforcedMotionTotal() or apex.environment.createLoadEnforcedMotionTotalVariable() functions. Note: the total enforced motion can be only used as a relative enforced displacement in nonlinear analysis.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldEnforcedMotion` — a DFEMFieldEnforcedMotion that identifies nodes that represent the region to which this load is applied as well as the distribution of enforced motions across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldEnforcedMotion) -> None`
Updates one or more properties of the enforced motion. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Update the id of the enforced motion.
- `name` — Updates the name of the enforced motion.
- `description` — Update the description of the enforced motion.
- `spatialTarget` — Update the spatialTarget of the enforced motion.


## `apex.environment.LoadEnforcedMotionTotal`  (extends `Load`)
A total enforced displacement for static analysis and enforced motion(displacement, velocity and acceleration) for dynamic analysis depending on the dynamic load. In nonlinear analysis, it is a total enforced displacement for a step. The enforced motion has six components. The translation vector is defined by three translation components and rotation vector is defined by three rotation components. The vector may be defined relative to a local coordinate system. The constant enforced motion may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create one or several Nastran SPCD with SPC1 entries on each Node.
Properties: `orientation`, `rotationX`, `rotationY`, `rotationZ`, `target`, `translationX`, `translationY`, `translationZ`

Methods:

- `getOrientation() -> apex.IOrientation` — an optional CoordinateSystem used to define the orientation of the motion components. If omitted, the default is the basic coordinate system.
- `getRotationX() -> float` — the motion value in rotation X. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getRotationY() -> float` — the motion value in rotation Y. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getRotationZ() -> float` — the motion value in rotation Z. The value is an Angle quantity in static analysis, while it can be a Angle/Angle veloctity/Angle acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the enforced motion will be applied to. Enforced motions may be assigned to Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Enforced motions assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTranslationX() -> float` — the motion value in translation X. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getTranslationY() -> float` — the motion value in translation Y. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
- `getTranslationZ() -> float` — the motion value in translation Z. The value is a length quantity in static analysis, while it can be a length/veloctity/acceleration quantity in a dynamic analysis. The unit is defined from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, translationX: float, translationY: float, translationZ: float, rotationX: float, rotationY: float, rotationZ: float, orientation: apex.IOrientation) -> None`
Updates one or more properties of the enforced motion. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `target` — Update the target.
- `translationX` — Update the translationX.
- `translationY` — update the translationY.
- `translationZ` — Update the translationZ.
- `rotationX` — Update the rotationX.
- `rotationY` — Update the rotationY.
- `rotationZ` — Update the rotationZ.
- `orientation` — Update the orientation of this LoadEnforcedMotionTotal


## `apex.environment.LoadEnforcedMotionTotalVariable`  (extends `Load`)
This class represents an enforced motion in both translation and rotation components. A single instance of this class may include a multiplicity of individual enforced motions each applied to a different Node. All of the individual enforced motions are composed by this LoadEnforcedMotionTotal and share a common ID. When used in a Nastran simulation this class will give rise to a SPCD entry with a SPC1 entry for component and each Node within the scope of the region to which it is associated. LoadEnforcedMotionTotalVariable can be configured to represent either a spatially constant or spatially varying field of enforced motions. The spatially constant configuration defines an enforced motion and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of enforced motions and coordinate systems to assign a different enforced motion to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadEnforcedMotionTotal() or apex.environment.createLoadEnforcedMotionTotalVariable() functions. Note: the total enforced motion can be used as enforced displacement for static analysis and enforced motion(displacement, velocity and acceleration) for dynamic analysis. In nonlinear analysis, it is a total enforced displacement for a step.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldEnforcedMotion` — a DFEMFieldEnforcedMotion that identifies nodes that represent the region to which this load is applied as well as the distribution of enforced motions across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldEnforcedMotion) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadForceComponent`  (extends `Load`)
A spatially invariant static concentrated force acting on a Node. The force direction and magnitude are defined by a load vector with a scale factor. The vector is defined by three components and a coordinate system. The constant Force may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create a Nastran FORCE entry on a Node.
Properties: `forceX`, `forceY`, `forceZ`, `orientation`, `scaleFactor`, `target`

Methods:

- `getForceX() -> float` — the value of the X component of the Force. The component direction is relative to the orientation. forceX is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getForceY() -> float` — the value of the Y component of the Force. The component direction is relative to the orientation. forceY is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getForceZ() -> float` — the value of the Z component of the Force. The component direction is relative to the orientation. forceZ is a Force quantity and is defined using the units of Force from the active script unit system.
- `getOrientation() -> apex.IOrientation` — an optional CoordinateSystem used to define the orientation of the Force components. If omitted, the default is the basic coordinate system.
- `getScaleFactor() -> float` — an optional scale factor that will be applied to the force vectors. The magnitude of the Force applied to each Node in the target is based on the product of the resultant of the provided Force vector and this scale factor.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Force will be applied to. Forces may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Forces assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution .
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, orientation: apex.IOrientation, scaleFactor: float, forceX: float, forceY: float, forceZ: float) -> None`
Update method.One or more properties may be updated in each call to update().

- `name` — Update the name of the Force.
- `description` — Update the description of the Force.
- `id` — Update the id of the Force.
- `target` — Update the target of the Force.
- `orientation` — Updates the orientation of the Force vector components to match the IOrientation provided here.
- `scaleFactor` — Updates the scale factor that will be applied to the Force vector. The total magnitude of the Force applied to each Node in the target is based on the product of the resultant of the Force vector and this scale factor.
- `forceX` — Updates the value of the X component of the Force. The component direction is relative to the orientation. forceX is a Force quantity and must be defined using the units of Force from the active script unit system.
- `forceY` — Updates the value of the Y component of the Force. The component direction is relative to the orientation. forceY is a Force quantity and must be defined using the units of Force from the active script unit system.
- `forceZ` — Updates the value of the Z component of the Force. The component direction is relative to the orientation. forceZ is a Force quantity and must be defined using the units of Force from the active script unit system.


## `apex.environment.LoadForceComponentVariable`  (extends `Load`)
This class represents a static concentrated force where the direction and magnitude of the force are defined by a vector and a scale factor. The vector axes may be defined relative to a local coordinate system. A single instance of this class may include a multiplicity of individual concentrated forces each applied to a different Node. All of the individual forces are composed by this LoadForceComponent and share a common ID. When used in a Nastran simulation this class will give rise to a FORCE entry for each Node within the scope of the region to which it is associated. LoadForceComponentVariable can be configured to represent either a spatially constant or spatially varying field of forces. The spatially constant configuration defines a single force magnitude and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of force vectors, scale factors and coordinate systems to assign a different force magnitude to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadForceComponent() or apex.environment.createLoadForceComponentVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldForceComponent` — a DFEMFieldForceComponent that identifies nodes that represent the region to which this load is applied as well as the distribution of forces across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldForceComponent) -> None`
Updates one or more properties of the Force. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Update the id of the Force.
- `name` — Updates the name of the Force.
- `description` — Updates the description of the Force.
- `spatialTarget` — Updates the spatialTarget of the Force.


## `apex.environment.LoadForceFollowerNormal`  (extends `Load`)
A spatially invariant static concentrated force acting on a Node. The force is defined by a magnitude with a direction parallel to the cross product of two vectors defined by four nodes. The constant Force may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create a Nastran FORCE2 entry on a Node.
Properties: `forceMagnitude`, `point1`, `point2`, `point3`, `point4`, `target`

Methods:

- `getForceMagnitude() -> float` — the magnitude of the force, forceMagnitude is a Force quantity and must be defined using the units of Force from the active script unit system. The force direction is parallel to the cross product of two vectors defined by four points.
- `getPoint1() -> apex.Entity` — the starting point of the first vector. It can be a vertex or a node.
- `getPoint2() -> apex.Entity` — the end point of the first vector. It can be a vertex or a node.
- `getPoint3() -> apex.Entity` — the starting point of the second vector. It can be a vertex or a node.
- `getPoint4() -> apex.Entity` — the end point of the second vector. It can be a vertex or a node.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Force will be applied to. Forces may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Forces assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, forceMagnitude: float, point1: apex.Entity, point2: apex.Entity, point3: apex.Entity, point4: apex.Entity) -> None`
Updates one or more properties of the Force. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the Force.
- `description` — Updates the description of the Force.
- `id` — Updates the id of the Force.
- `target` — Updates the target of the Force.
- `forceMagnitude` — Updates the forceMagnitude of the Force. forceMagnitude is a Force quantity and must be defined using the units of Force from the active script unit system.
- `point1` — Updates the starting point of the first vector.
- `point2` — Updates the end point of the first vector.
- `point3` — Updates the starting point of the second vector.
- `point4` — Updates the end point of the second vector.


## `apex.environment.LoadForceFollowerNormalVariable`  (extends `Load`)
This class represents a static concentrated force where the direction and magnitude of the force are defined by two vectors and a magnitude. The direction is parallel to the cross produce of the two vectors defined by four nodes. A single instance of this class may include a multiplicity of individual concentrated forces each applied to a different Node. All of the individual forces are composed by this LoadForceNormal and share a common ID. When used in a Nastran simulation this class will give rise to a FORCE2 entry for each Node within the scope of the region to which it is associated. LoadForceNormal can be configured to represent either a spatially constant or spatially varying field of forces. The spatially constant configuration defines a single force magnitude and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of force magnitudes directions to assign a different force magnitude to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadForceNormal() or apex.environment.createLoadForceNormalVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldForceFollowerNormal` — a DFEMFieldForceNormal that identifies nodes that represent the region to which this load is applied as well as the distribution of forces across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldForceFollowerNormal) -> None`
Updates one or more properties of the Force. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Update the id of the Force.
- `name` — Update the name of the Force.
- `description` — Update the description of the Force.
- `spatialTarget` — Update the spatialTarget of the Force.


## `apex.environment.LoadForceFollowerVector`  (extends `Load`)
A spatially invariant static concentrated force acting on a Node. The force direction and magnitude are defined by a vector and a magnitude. The vector is defined by two nodes. The constant Force may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create a Nastran FORCE1 entry on each Node.
Properties: `forceMagnitude`, `point1`, `point2`, `target`

Methods:

- `getForceMagnitude() -> float` — the magnitude of the Force, forceMagnitude is a Force quantity and must be defined using the units of Force from the active script unit system. The force direction is along the vector from point1 to point2.
- `getPoint1() -> apex.Entity` — The starting point of the force vector.
- `getPoint2() -> apex.Entity` — the end point of the force vector.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Force will be applied to. Forces may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Forces assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution .
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, forceMagnitude: float, point1: apex.Entity, point2: apex.Entity) -> None`
Updates one or more properties of the Force. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name .
- `description` — Update the description of the Force.
- `id` — Update the id of the Force.
- `target` — Update the target of the Force.
- `forceMagnitude` — Update the forceMagnitude of the Force. forceMagnitude is a Force quantity and must be defined using the units of Force from the active script unit system. The force direction is along the vector from point1 to point2.
- `point1` — Update the point1.
- `point2` — Update the point2.


## `apex.environment.LoadForceFollowerVectorVariable`  (extends `Load`)
This class represents a static concentrated force where the direction and magnitude of the force are defined by a vector and a magnitude. The vector is defined by two nodes. A single instance of this class may include a multiplicity of individual concentrated forces each applied to a different Node. All of the individual forces are composed by this LoadForceVector and share a common ID. When used in a Nastran simulation this class will give rise to a FORCE1 entry for each Node within the scope of the region to which it is associated. LoadForceVector can be configured to represent either a spatially constant or spatially varying field of forces. The spatially constant configuration defines a single force magnitude and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of force vectors, scale factors and coordinate systems to assign a different force magnitude to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadForceVector() or apex.environment.createLoadForceVectorVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldForceFollowerVector` — a DFEMFieldForceVector that identifies nodes that represent the region to which this load is applied as well as the distribution of forces across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldForceFollowerVector) -> None`
Updates one or more properties of the load scale factor. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadForceRotational`  (extends `Load`)
A static loading condition due to an angular velocity and/or acceleration acting on Node. The inertia forces due to a constant angular velocity, act in the positive radial direction. The forces due to a constant angular acceleration, act in the same direction as the angular acceleration. These forces would be opposite to the inertia forces on the structure due to a constant angular acceleration. When used to generate a Nastran model this class will create a Nastran RFORCE entry.
Properties: `coordinateSystemDefinition`, `loadMethod`, `orientation`, `rotationCenter`, `rotationVectorX`, `rotationVectorY`, `rotationVectorZ`, `scaleFactorAcc`, `scaleFactorVel`

Methods:

- `getCoordinateSystemDefinition() -> apex.attribute.CoordinateSystemDefinition` — the coordinate system definition of the rotational force: apex.attribute.CoordinateSystemDefinition.SuperElement, the coordinate system is defined in the super-element and will be translated, rotated with the super-element. apex.attribute.CoordinateSystemDefinition.Residual, the coordinate system is defined in the residual structure and stationary with the basic coordinate system.
- `getLoadMethod() -> apex.attribute.LoadMethodRotational` — the load method of the rotational force. apex.attribute.LoadMethod.Centrifugal should be used when there is no coupling in mass matrix - the lumped mass is used with or without element offset. apex.attribute.LoadMethod.RotationInertia should be used when lumped or consistent mass matrix is used without element offset.
- `getOrientation() -> apex.IOrientation` — the orientation used to define the direction of the RotationalForce. Currently it only accepts a coordinate system object.
- `getRotationCenter() -> apex.Entity` — the rotation center of the rotational force. If omitted, the rotation center is the origin of the basic coordinate system.
- `getRotationVectorX() -> float` — the X component of the rotation vector.
- `getRotationVectorY() -> float` — the Y component of the rotation vector.
- `getRotationVectorZ() -> float` — the Z component of the rotation vector.
- `getScaleFactorAcc() -> float` — the scale factor of the angular acceleration. The unit is Rotation Acceleration and must be defined using the units of Rotation Acceleration from the active script unit system.
- `getScaleFactorVel() -> float` — the scale factor for angular velocity in revolutions per unit time. The unit is Rotation Velocity and must be defined using the units of Rotation Velocity from the active script unit system.
#### `update(name: str, description: str, id: int, rotationCenter: apex.Entity, orientation: apex.IOrientation, scaleFactorVel: float, rotationVectorX: float, rotationVectorY: float, rotationVectorZ: float, loadMethod: apex.attribute.LoadMethodRotational, scaleFactorAcc: float, coordinateSystemDefinition: apex.attribute.CoordinateSystemDefinition) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `rotationCenter` — Update the rotationCenter.
- `orientation` — Update the orientation.
- `scaleFactorVel` — Update the scaleFactorVel.
- `rotationVectorX` — Update the rotationVectorX.
- `rotationVectorY` — Update the rotationVectorY.
- `rotationVectorZ` — Update the rotationVectorZ.
- `loadMethod` — Update the loadMethod.
- `scaleFactorAcc` — Update the scaleFactorAcc.
- `coordinateSystemDefinition` — Update the coordinateSystemDefinition.


## `apex.environment.LoadLug`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
LoadLug represents a commonly used lug loading on the mechanical system. It can be applied to Faces or Edges.
Properties: `angle`, `lugProperty`, `target`

Methods:

- `getAngle() -> float` — The span angle of the selected target in the LoadLug.This is automatically determined by the selected edges or faces.In future release, user can manually define the distribution angle.
- `getDescription() -> str` — An optional description for the LoadLug that will be created. If omitted, the description will be left blank.
- `getLugProperty() -> LoadLugProperty` — The property of the LoadLug.
- `getTarget() -> apex.EntityCollection` — Returns the target entities that the LoadLug is applied to. The supported target types are face and edge.
#### `update(name: str, description: str, target: apex.EntityCollection, lugProperty: LoadLugProperty) -> None`
Update this LoadLug.

- `name` — Update the name.
- `description` — Update the descripting.
- `target` — Update the target.
- `lugProperty` — Update the lugProperty.

One or more properties may be updated in each call to update().


## `apex.environment.LoadLugCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of LoadLug, based on EntityCollection.

Methods:

- `LoadLugCollection() -> None` — Construct a new LoadLugCollection.

## `apex.environment.LoadLugProperty`  (extends `Entity`)
Base Class LoadLugProperty. In the first release, Apex only support LoadLugPropertyStatic.

## `apex.environment.LoadLugPropertyStatic`  (extends `LoadLugProperty`)
In the first release, Apex only support LoadLugPropertyStatic.
Properties: `distribution`, `distributionOrientation`, `id`, `loadMagnitude`, `orientation`

Methods:

- `getDistribution() -> apex.attribute.Distribution` — Returns the distribution of the LoadLugPropertyStatic.
- `getDistributionOrientation() -> apex.attribute.DistributionOrientation` — Returns the distribution orientation of the LoadLugPropertyStatic.
- `getId() -> int` — Returns the load id of the LoadLugPropertyStatic.
- `getLoadMagnitude() -> float` — Returns the magnitude of the LoadLugPropertyStatic.
- `getOrientation() -> apex.construct.Orientation` — Returns the orientation of the LoadLugPropertyStatic. For parallel distribution, the X axis of the orientation is the distributed load direction. For normal distribution, the X axis is the total load direction. In 2021.2 release, the orientation is automatically determined by the selected entities.
#### `update(loadMagnitude: float, distribution: apex.attribute.Distribution, distributionOrientation: apex.attribute.DistributionOrientation, id: int) -> None`
Update this LoadLugPropertyStatic. One or more properties may be updated in each call to update().

- `loadMagnitude` — Update the magnitude.
- `distribution` — Update the distribution.
- `distributionOrientation` — Update the distribution orientation.
- `id` — Update the id.


## `apex.environment.LoadMomentComponent`  (extends `Load`)
A spatially invariant static concentrated moment acting on a Node. The moment direction and magnitude are defined by a load vector with a scale factor. The vector is defined by three components and a coordinate system. The constant Moment may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create a Nastran MOMENT entry on a Node.
Properties: `momentX`, `momentY`, `momentZ`, `orientation`, `scaleFactor`, `target`

Methods:

- `getMomentX() -> float` — the value of the X component of the Moment. The component direction is relative to the orientation. momentX is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getMomentY() -> float` — the value of the Y component of the Moment. The component direction is relative to the orientation. momentY is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getMomentZ() -> float` — the value of the Z component of the Moment. The component direction is relative to the orientation. momentZ is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getOrientation() -> apex.IOrientation` — an optional CoordinateSystem used to define the orientation of the Moment components. If omitted, the default is the basic coordinate system.
- `getScaleFactor() -> float` — an optional scale factor that will be applied to the moment vectors. The magnitude of the Moment applied to each Node in the target is based on the product of the resultant of the provided Moment vector and this scale factor.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Moment will be applied to. Moments may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Moments assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, orientation: apex.IOrientation, scaleFactor: float, momentX: float, momentY: float, momentZ: float) -> None`
Updates one or more properties of the Moment. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name of the Moment.
- `description` — Update the description of the Moment.
- `id` — Update the id of the Moment.
- `target` — Updates the target entities to which this Moment will be applied. an EntityCollection identifying the entities that the Force will be applied to. Forces may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Moments assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `orientation` — Updates the orientation of the Moment vector components to match the IOrientation provided here.
- `scaleFactor` — Updates the scale factor that will be applied to the Moment vector. The total magnitude of the Moment applied to each Node in the target is based on.
- `momentX` — Updates the value of the X component of the Moment. The component direction is relative to the orientation. momentX is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `momentY` — Updates the value of the Y component of the Moment. The component direction is relative to the orientation. momentY is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `momentZ` — Updates the value of the Z component of the Moment. The component direction is relative to the orientation. momentZ is a Moment quantity and must be defined using the units of Moment from the active script unit system.


## `apex.environment.LoadMomentComponentVariable`  (extends `Load`)
This class represents a static concentrated moment where the direction and magnitude of the moment are defined by a vector and a scale factor. The vector axes may be defined relative to a local coordinate system. A single instance of this class may include a multiplicity of individual concentrated moments each applied to a different Node. All of the individual moments are composed by this LoadMomentComponent and share a common ID. When used in a Nastran simulation this class will give rise to a MOMENT entry for each Node within the scope of the region to which it is associated. LoadMomentComponentVariable can be configured to represent either a spatially constant or spatially varying field of moments. The spatially constant configuration defines a single moment magnitude and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of moment vectors, scale factors and coordinate systems to assign a different moment magnitude to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadMomentComponent() or apex.environment.createLoadMomentComponentVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldMomentComponent` — a DFEMFieldMomentComponent that identifies nodes that represent the region to which this load is applied as well as the distribution of moments across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldMomentComponent) -> None`
Updates one or more properties of the Moment. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the Moment.
- `name` — Updates the name of the Moment.
- `description` — Updates the description of the Moment.
- `spatialTarget` — Updates the spatialTarget of the Moment.


## `apex.environment.LoadMomentFollowerNormal`  (extends `Load`)
A spatially invariant static moment acting on a Node. The moment is defined by a magnitude with a directionparallel to the cross product of two vectors defined by four nodes. The first vector direction is from point1 to point2, the second vector direction is from point3 to point4. The constant Moment may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create a Nastran MOMENT2 entry on a Node.
Properties: `momentMagnitude`, `point1`, `point2`, `point3`, `point4`, `target`

Methods:

- `getMomentMagnitude() -> float` — the magnitude of the moment, momentMagnitude is a Moment quantity and must be defined using the units of Moment from the active script unit system. The moment direction is parallel to the cross product of the two vectors defined by four points.
- `getPoint1() -> apex.Entity` — the starting point of the first vector.
- `getPoint2() -> apex.Entity` — the end point of the first vector.
- `getPoint3() -> apex.Entity` — the starting point of the second vector.
- `getPoint4() -> apex.Entity` — the end point of the second vector.
- `getTarget() -> apex.EntityCollection` — the entityCollection that the load is applied to.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, momentMagnitude: float, point1: apex.Entity, point2: apex.Entity, point3: apex.Entity, point4: apex.Entity) -> None`
Updates one or more properties of the Moment. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the Moment.
- `description` — Updates the description of the Moment.
- `id` — Updates the id of the Moment.
- `target` — Updates the target of the Moment.
- `momentMagnitude` — Updates the momentMagnitude. momentMagnitude is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `point1` — Updates the starting point of the first vector.
- `point2` — Updates the end point of the first vector.
- `point3` — Updates the starting point of the second vector.
- `point4` — Updates the end point of the second vector.


## `apex.environment.LoadMomentFollowerNormalVariable`  (extends `Load`)
This class represents a static concentrated moment where the direction and magnitude of the moment are defined by two vectors and a magnitude. The direction is parallel to the cross produce of the two vectors defined by four nodes. A single instance of this class may include a multiplicity of individual concentrated moments each applied to a different Node. All of the individual moments are composed by this LoadMomentNormal and share a common ID. When used in a Nastran simulation this class will give rise to a MOMENT2 entry for each Node within the scope of the region to which it is associated. LoadMomentNormal can be configured to represent either a spatially constant or spatially varying field of moments. The spatially constant configuration defines a single moment magnitude and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of moment magnitudes and directions to assign a different moment magnitude to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadMomentNormal() or apex.environment.createLoadMomentNormalVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldMomentFollowerNormal` — a DFEMFieldMomentNormal that identifies nodes that represent the region to which this load is applied as well as the distribution of moments across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldMomentFollowerNormal) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadMomentFollowerVector`  (extends `Load`)
A spatially invariant static moment acting on a Node. The moment direction and magnitude are defined by a vector and a magnitude. The vector is defined by two nodes. The constant Moment may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create a Nastran MOMENT1 entry on Node.
Properties: `momentMagnitude`, `point1`, `point2`, `target`

Methods:

- `getMomentMagnitude() -> float` — the moment magnitude. momentMagnitude is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `getPoint1() -> apex.Entity` — The starting point of the moment vector.
- `getPoint2() -> apex.Entity` — the end point of the moment vector.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Moment will be applied to. Moments may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Moments assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, momentMagnitude: float, point1: apex.Entity, point2: apex.Entity) -> None`
Updates one or more properties of the Moment. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the Moment.
- `description` — Update the description of the Moment.
- `id` — Update the id of the Moment.
- `target` — Update the target of the Moment.
- `momentMagnitude` — Updates the momentMagnitude. momentMagnitude is a Moment quantity and must be defined using the units of Moment from the active script unit system.
- `point1` — Updates the point1.
- `point2` — Updates the point2.


## `apex.environment.LoadMomentFollowerVectorVariable`  (extends `Load`)
This class represents a static concentrated moment where the direction and magnitude of the moment are defined by a vector and a magnitude. The vector is defined by two nodes. A single instance of this class may include a multiplicity of individual concentrated moments each applied to a different Node. All of the individual moments are composed by this LoadMomentVector and share a common ID. When used in a Nastran simulation this class will give rise to a MOMENT1 entry for each Node within the scope of the region to which it is associated. LoadMomentVector can be configured to represent either a spatially constant or spatially varying field of moments. The spatially constant configuration defines a single moment magnitude and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of moment vectors, scale factors and coordinate systems to assign a different moment magnitude to each Node in the target region. Instances of this class can be created using the apex.environment.createLoadMomentVector() or apex.environment.createLoadMomentVectorVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldMomentFollowerVector` — a DFEMFieldMomentVector that identifies nodes that represent the region to which this load is applied as well as the distribution of moments across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldMomentFollowerVector) -> None`
Updates one or more properties of the Moment. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the Moment.
- `name` — Update the name of the Moment.
- `description` — Update the description of the Moment.
- `spatialTarget` — Updates the spatialTarget of the Moment.


## `apex.environment.LoadPhaseLead`  (extends `Load`)
The phase lead term in the equations of the dynamic loading function. It should be applied to the nodes of the excitation loads of the dynamitic load, with the same degrees of freedom. When used to generate a Nastran model this class will create a Nastran DPHASE entry.
Properties: `phaseLeadRx`, `phaseLeadRy`, `phaseLeadRz`, `phaseLeadX`, `phaseLeadY`, `phaseLeadZ`, `target`

Methods:

- `getPhaseLeadRx() -> float` — the phase lead value in the rotation X component. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getPhaseLeadRy() -> float` — the phase lead value in the rotation Y component. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getPhaseLeadRz() -> float` — the phase lead value in the rotation Z component. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getPhaseLeadX() -> float` — the phase lead value in the X component. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getPhaseLeadY() -> float` — the phase lead value in the Y component. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getPhaseLeadZ() -> float` — the phase lead value in the component. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the phase lead will be applied to. Phase leads may be assigned to Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Phase leads assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, phaseLeadX: float, phaseLeadY: float, phaseLeadZ: float, phaseLeadRx: float, phaseLeadRy: float, phaseLeadRz: float) -> None`
Updates one or more properties of the phase lead. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name of this LoadPhaseLead
- `description` — Update the description of this LoadPhaseLead
- `id` — Updates the id.
- `target` — Updates the target of the phase lead.
- `phaseLeadX` — Updates the phaseLeadX. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `phaseLeadY` — Updates the phaseLeadY. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `phaseLeadZ` — Updates the phaseLeadZ. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `phaseLeadRx` — Updates the phaseLeadRx. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `phaseLeadRy` — Updates the phaseLeadRy. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.
- `phaseLeadRz` — Updates the phaseLeadRz. It is a Angle quantity and must be defined using the units of Angle from the active script unit system.


## `apex.environment.LoadPhaseLeadVariable`  (extends `Load`)
DFEMFieldTimeDelay.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldPhaseLead` — the field that defines the phase lead distribution.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPhaseLead) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadPressure`  (extends `Entity`, `IName`, `IUserHighlightable`, `IDisplayable`)
The Pressure load defines a distributed load (load per unit area) that acts perpendicularly to the region that it applies to. Pressure loads can be constant across the target region to which they are applied or they can vary across the region. The spatial variation of pressure can be defined using a number of different filed representations including, * Mesh2DData * Mesh3DData * HydrostaticData * Equation * PointCloud2DData * PointCloud3DData Currently Apex supports Static pressure loads. Future releases of Apex will support Dynamic (Frequency and time dependent), Random (PSD) and Buckling (Unit) pressure load reps. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure, PressureVariable.
Properties: `loadPressureProperty`, `target`

Methods:

- `getLoadPressureProperty() -> LoadPressureProperty` — the property used to define one load pressure, it contains ID and pressureValue(s). THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure, PressureVariable.
- `getTarget() -> apex.EntityCollection` — The entities which the pressure load is assigned to. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure, PressureVariable.
#### `update(name: str, description: str, target: apex.EntityCollection, loadPressureProperty: LoadPressureProperty) -> None`
Update this LoadPressure. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure, PressureVariable.

- `name` — of this LoadPressure
- `description` — of this LoadPressure
- `target` — of this LoadPressure
- `loadPressureProperty` — loadPressureProperty of this LoadPressure

One or more properties may be updated in each call to update().


## `apex.environment.LoadPressure2D`  (extends `Load`)
A static uniform pressure applied to 2D element only. The pressure direction is perpendicular to the element. The constant pressure may be applied to one or more 2D Elements directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create one Nastran PLOAD2 entry on one element.
Properties: `pressureMagnitude`, `target`

Methods:

- `getPressureMagnitude() -> float` — the magnitude of the pressure, pressureMagnitude is a Pressure quantity and is defined using the units of Pressure from the active script unit system. The pressure direction is perpendicular to the element.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the pressure will be applied to. Pressures may be assigned to Face, Surface Mesh and 2D element. Pressures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, pressureMagnitude: float, target: apex.EntityCollection) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name of the Pressure.
- `description` — Update the description of the Pressure.
- `id` — Update the id of the Pressure.
- `pressureMagnitude` — Updates the pressureMagnitude. pressureMagnitude is a Pressure quantity and is defined using the units of Pressure from the active script unit system.
- `target` — Update the target of the Pressure.


## `apex.environment.LoadPressure2DVariable`  (extends `Load`)
A spatially variable pressure directly applied to one or several 2D element only. The pressure magnitudes may be different on each element. When used to generate a Nastran model this class will create one Nastran PLOAD2 entry on each element.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldPressure2D` — a DFEMFieldPressure2DSurface that identifies elements that represent the region to which this load is applied as well as the distribution of pressures across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPressure2D) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the Pressure.
- `name` — Updates the name of the Pressure.
- `description` — Updates the description of the Pressure.
- `spatialTarget` — Updates the spatialTarget of the Pressure.


## `apex.environment.LoadPressureArea`  (extends `Load`)
A static pressure applied to a triangular face area or a quadrilateral face area surrounded by three or four vertices. The total load value is equal to the pressure magnitude multiplies the face area. The constant pressure may be applied to one or more Nodes directly or indirectly through their association to geometry. When used to generate a Nastran model this class will create one Nastran PLOAD entry on the selected nodes.
Properties: `pressureMagnitude`, `vertex1`, `vertex2`, `vertex3`, `vertex4`

Methods:

- `getPressureMagnitude() -> float` — the magnitude of the pressure, pressureMagnitude is a Pressure quantity and is defined using the units of Pressure from the active script unit system. The pressure direction is normal to the face defined by the vertices.
- `getVertex1() -> apex.Entity` — the first vertex of the face.
- `getVertex2() -> apex.Entity` — the second vertex of the face.
- `getVertex3() -> apex.Entity` — the third vertex of the face.
- `getVertex4() -> apex.Entity` — the fourth vertex of the face. This argument can be "None" if the face only has three vertices.
#### `update(name: str, description: str, id: int, pressureMagnitude: float, vertex1: apex.Entity, vertex2: apex.Entity, vertex3: apex.Entity, vertex4: apex.Entity) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name of the Pressure.
- `description` — Update the description of the Pressure.
- `id` — Update the id of the Pressure.
- `pressureMagnitude` — Update the pressureMagnitude. pressureMagnitude is a Pressure quantity and is defined using the units of Pressure from the active script unit system.
- `vertex1` — Update the vertex1.
- `vertex2` — Update the vertex2.
- `vertex3` — Update the vertex3.
- `vertex4` — Update the vertex4.


## `apex.environment.LoadPressureAreaVariable`  (extends `Load`)
This class represents a uniform pressure applied to one or several triangular areas or a quadrilateral face areas. A single instance of this class may include a multiplicity of individual pressures each applied to a different face area defined by three or four nodes. All of the individual pressures are composed by this LoadPressureArea and share a common ID. When used in a Nastran simulation this class will give rise to a PLOAD entry for each Node within the scope of the region to which it is associated. LoadPressureAreaVariable can be configured to represent either a spatially constant or spatially varying field of pressures. The spatially constant configuration defines a pressure and direction and assigns it to all Nodes in the target region. The spatially varying configuration uses a field of pressures and nodes to assign a different pressure to each face area defined by the nodes in the target region. Instances of this class can be created using the apex.environment.createLoadPressureArea() or apex.environment.createLoadPressureAreaVariable() functions.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldPressureArea` — a DFEMFieldPressureArea that identifies nodes that represent the region to which this load is applied as well as the distribution of pressures across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPressureArea) -> None`
Updates one or more properties of the Pressure. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Update the ids of the Pressure.
- `name` — Updates the name of the Pressure.
- `description` — Updates the description of the Pressure.
- `spatialTarget` — Updates the spatialTarget of the Pressure.


## `apex.environment.LoadPressureCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of LoadPressure, based on EntityCollection.

Methods:

- `LoadPressureCollection() -> None` — Construct a new LoadPressureCollection.

## `apex.environment.LoadPressureProperty`  (extends `Entity`)
Base Class of LoadPressureProperty. In the first release, Apex will support the derived classes: LoadPressurePropertyStaticConstant LoadPressurePropertyStaticVariable In future releases, Apex will support: LoadPressurePropDynamic LoadPressurePropRandom LoadPressurePropBuckling THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure, PressureVariable.

## `apex.environment.LoadPressurePropertyStaticConstant`  (extends `LoadPressureProperty`)
class of static constant pressure load property. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure.
Properties: `id`, `pressureValue`

Methods:

- `getId() -> int` — an optional load ID defined in PressurePropertyStaticConstant and assigned to the associated LoadPressure. If omitted, the system will assign a default load ID which is the smallest and unique among all existing loads IDs. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure.
- `getPressureValue() -> float` — value of static constant pressure property. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure.
#### `update(pressureValue: float, id: int) -> None`
Update this LoadPressurePropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: Pressure.

- `pressureValue` — Pressure value assigned to the target.
- `id` — is an optional load ID defined in PressurePropertyStaticConstant and assigned to the associated LoadPressure. If omitted, the system will assign a default load ID which is the smallest and unique among all existing loads IDs.

One or more properties may be updated in each call to update().


## `apex.environment.LoadPressurePropertyStaticVariable`  (extends `LoadPressureProperty`)
class of static variable pressure load property. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: PressureVariable.
Properties: `id`

Methods:

- `getId() -> int` — an optional load ID defined in LoadPressurePropertyStaticVariable and assigned to the associated LoadPressure. If omitted, the system will assign a default load ID which is the smallest and unique among all existing loads IDs. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: PressureVariable.
- `getPressureValues() -> {str:{dict}}` — returns a nested Dictionary containing the pathNames of the MeshBody on which the pressure is applied and the element IDs/element face IDs/node IDs and associated pressure values. The key of the top level dictionary is a string type that represents the pathName of a MeshBody and the associated value is a secondary dictionary containing the individual elements/faces/pressures. Each MeshBody that has one or more elements referenced by the variable pressure load will be included in the top level dictionary. For example, is a pressure is applied to elements on two different MeshBodies the top level dictionary will include two items - {"Model_1/Part 1/Mesh 1?: {dict1}, "Model_1/Part 2/Mesh 2": {dict2}} The secondary dictionary contains the information about which elements/element faces are included in the variable pressure load and the pressure values applied to each. A variable pressure load may have a single constant value per 2D element or 3D element face or may have different values defined at each corner node of 2D elements or 3D element faces. The type of distribution is identified in the secondary dictionary by the "identifier_type"key which is a string type. The associated value is a string type that must be one of the following values, "ELEMENT_ID", "ELEMENT_ID_FACE_INDEX", "ELEMENT_ID_FACE_NODE_ID" If identifier_type is ELEMENT_ID, the pressure field is defined using a single pressure value per 2D element and the secondary dictionary items with "element_ids" and "pressures" keys identify the 2D elements and pressure values. The value associated with the element_ids key is a List of integers, each integer identifying the element id. The value associated with the pressures key is a List of floats, each integer identifying the single pressure value associated with the corresponding element. The element_ids and pressure lists must be of equal length with the pressure value indices aligned with the element ids indices. If identifier_type is ELEMENT_ID_FACE_INDEX, the remainder of the pressure field is defined using a single pressure value per 3D element face and the secondary dictionary items with "element_ids" "face_identifiers" and "pressures" identify the 3D element faces and pressure values. The value associated with the element_ids key is a List of integers, each integer identifying the id of a 3D element. The value associated with the "face_identifiers" key is a List of integers, each integer identifying a face on the associated 3D element. (Face indices per 3D element type are documented elsewhere). The value associated with the pressures key is a List of floats, each integer identifying the single pressure value associated with the corresponding element face. The element_ids, identifiers and pressures lists must be of equal length with the pressure value indices aligned with the element ids/Element face indices. If identifier_type is ELEMENT_ID_FACE_NODE_ID, the remainder of the pressure field is defined using multiple pressure values per 2D element or 3D element face ?one pressure value for each corner node of the 2D element or 3D element face and the secondary dictionary items with "element_ids" "face_identifiers" and "pressures" identify the 2D Elements or 3D element faces and pressure values. The value associated with the element_ids key is a List of integers, each integer identifying the id of a 2D or 3D element. The value associated with the "face_identifiers" key is a List of Lists of integers. Each internal integer List identifies the corner nodes of the 2D element or 3D element face. There must be the same number of internal integer lists as there are IDs in element_ids, The value associated with the pressures key is a List of Lists of floats, Each internal list identifies the pressure values at the corner nodes of the associated 2D element or 3D element face. There must be the same number of internal float lists as there are IDs in element_ids and the pressure values must be aligned with the element corner node indices. Example : Pressure field defined on 3 2D elements with a single pressure per element { "identifier_type": "ELEMENT_ID" "element_ids": [1, 2, 6], "pressures": [15.0, 21.6, 35.9] } Example : Pressure field defined on 3 3D elements with a single pressure per element { "identifier_type": "ELEMENT_ID_FACE_INDEX" "element_ids": [11, 23, 915], "face_identifiers": [0, 3, 2], "pressures": [15.0, 21.6, 35.9] } Example : Pressure field defined on 3 elements with different pressures for one 2D element or 3D element face { "identifier_type": "ELEMENT_ID_FACE_NODE_ID" "element_ids": [11, 23, 915], "face_identifiers": [[15, 16, 18, 21], [17, 5, 89, 6], [99, 89, 70, 65]], "pressures": [[15.0, 17.6, 18.9, 17.2], [14.0, 17.2, 17.2], [13.2, 14.6, 15.9, 11.2]] } THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: PressureVariable.
#### `update(pressureValues: {str:{dict}}, id: int) -> None`
update a static variable pressure load property. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: PressureVariable.

- `pressureValues` — returns a nested Dictionary containing the pathName of the parts that are applied with the LoadPressure, the element IDs, element Face IDs, nodes IDs and the associated pressure values.
- `id` — is an optional load ID defined in PressurePropertyStaticVariable and assigned to the associated LoadPressure. If omitted, the system will assign a default load ID which is the smallest and unique among all existing loads IDs.

One or more properties may be updated in each call to update().


## `apex.environment.LoadRep`  (extends `Entity`, `IDisplayable`, `IUserAttributes`, `IName`)
Properties: `fAlpha`, `fBeta`, `fGamma`, `fMagnitude`, `mAlpha`, `mBeta`, `mGamma`, `mMagnitude`

Methods:

- `getFAlpha() -> float` — Returns FAlpha value of the LoadRep.
- `getFBeta() -> float` — Returns FBeta value of the LoadRep.
- `getFGamma() -> float` — Returns FGamma value of the LoadRep.
- `getFMagnitude() -> float` — Returns FMagnitude value of the LoadRep.
- `getMAlpha() -> float` — Returns MAlpha value of the LoadRep.
- `getMBeta() -> float` — Returns MBeta value of the LoadRep.
- `getMGamma() -> float` — Returns MGamma value of the LoadRep.
- `getMMagnitude() -> float` — Returns MMagnitude value of the LoadRep.
- `getParentLoad() -> apex.Entity` — Returns parent Load entity.

## `apex.environment.LoadTemperature`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class LoadTemperature prescribes temperatures on the mechanical system. LoadTemperature may be applied to Nodes, MeshBodies, GeometryBodies, Faces, Edges and Vertices. Internally the solver will apply the LoadTemperature to all nodes associated with the application region. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal, LoadTemperatureNodalVariable.
Properties: `target`, `temperatureProperty`

Methods:

- `getTarget() -> apex.EntityCollection` — Returns the target entities that the LoadTemperature is applied to. The supported target types are: Solid, cell, surface, curve, face, edge, vertex, 3D mesh, 2D mesh, 1D mesh, node. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal, LoadTemperatureNodalVariable.
- `getTemperatureProperty() -> LoadTemperatureProperty` — Returns the property of the LoadTemperature. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal, LoadTemperatureNodalVariable.
#### `update(name: str, description: str, target: apex.EntityCollection, temperatureProperty: LoadTemperatureProperty) -> None`
Update this LoadTemperature. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal, LoadTemperatureNodalVariable.

- `name` — of this LoadTemperature
- `description` — of this LoadTemperature
- `target` — of this LoadTemperature
- `temperatureProperty` — of this LoadTemperature

One or more properties may be updated in each call to update().


## `apex.environment.LoadTemperatureCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of LoadTemperature, based on EntityCollection.

Methods:

- `LoadTemperatureCollection() -> None` — Construct a new LoadTemperatureCollection.

## `apex.environment.LoadTemperatureDefault`  (extends `Load`)
The default temperature automatically applied to the entities that are not associated with other temperature loads. So there is no target in the load. When used to generate a Nastran model this class will create a Nastran TEMPD entry.
Properties: `defaultTemperature`

Methods:

- `getDefaultTemperature() -> float` — the default temperature value. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `update(name: str, description: str, id: int, defaultTemperature: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id.
- `defaultTemperature` — Updates the defaultTemperature. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.LoadTemperatureGradient2D`  (extends `Load`)
A spatially invariant temperature load acting on 2D elements(plate, membrane, and combination elements) by an average temperature and a thermal gradient through the thickness. The constant temperature load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPP1 entry.
Properties: `target`, `temperatureLowerSurface`, `temperatureReferencePlane`, `temperatureUpperSurface`, `thermalGradient`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Forces may be assigned to Surfaces, Faces, 2D Mesh Bodies and 2D Elements. Temperatures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `getTemperatureLowerSurface() -> float` — the temperature for stress calculation at points on the lower surface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureReferencePlane() -> float` — the temperature applied on the element reference plane. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureUpperSurface() -> float` — the temperature for stress calculation at points on the upper surface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradient() -> float` — the effective linear thermal gradient. It represents a quantity and must be specified using units of thermal gradient from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureReferencePlane: float, thermalGradient: float, temperatureLowerSurface: float, temperatureUpperSurface: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureReferencePlane` — Updates the temperatureReferencePlane. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradient` — Updates the thermalGradient. It represents a quantity and must be specified using units of thermal gradient from the active script unit system.
- `temperatureLowerSurface` — Updates the temperatureLowerSurface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureUpperSurface` — Updates the temperatureUpperSurface. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.LoadTemperatureGradient2DHeat`  (extends `Load`)
A spatially invariant temperature load acting on Nodes belong to heat transfer shell elements used in nonlinear scenario. The constant temperature load may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPN1 entry.
Properties: `target`, `temperatureBottom`, `temperatureMid`, `temperatureTop`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Surfaces, Faces, 2D Mesh Bodies and Nodes. Temperatures assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTemperatureBottom() -> float` — the temperature at bottom location through the thickness. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureMid() -> float` — the temperature at mid location through the thickness. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureTop() -> float` — the temperature at top location through the thickness. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureTop: float, temperatureBottom: float, temperatureMid: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureTop` — Updates the temperatureTop. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureBottom` — Updates the temperatureBottom. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureMid` — Updates the temperatureMid. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.LoadTemperatureGradient2DHeatVariable`  (extends `Load`)
This class represents a spatially varying temperature load applied to 2D heat transfer elements. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPN1 entry for each element within the scope of the region with which it is associated.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradient2DHeat` — a DFEMFieldTemperatureGradient2DHeat that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2DHeat) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the load.
- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `spatialTarget` — Updates the spatialTarget of the load.


## `apex.environment.LoadTemperatureGradient2DVariable`  (extends `Load`)
This class represents a spatially varying temperature load applied to 2D elements by an average temperature and a thermal gradient through the thickness. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPP1 entry for each element within the scope of the region with which it is associated.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradient2D` — a DFEMFieldTemperatureGradient2D that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradient2D) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the temperature load.
- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `spatialTarget` — Updates the spatialTarget of the temperature load.


## `apex.environment.LoadTemperatureGradientBeam2`  (extends `Load`)
A spatially invariant temperature load acting on 1D elements with two nodes. The constant temperature load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPRB entry.
Properties: `inputType`, `target`, `temperatureEndA`, `temperatureEndB`, `temperaturePointCendA`, `temperaturePointCendB`, `temperaturePointDendA`, `temperaturePointDendB`, `temperaturePointEendA`, `temperaturePointEendB`, `temperaturePointFendA`, `temperaturePointFendB`, `thermalGradient1A`, `thermalGradient1B`, `thermalGradient2A`, `thermalGradient2B`

Methods:

- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B. If the inputType is element variable, all temperature values and thermal gradients can be defined.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Curves, Edges, 1D Mesh Bodies and 1D Elements. Temperatures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `getTemperatureEndA() -> float` — the temperature value at end A on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureEndB() -> float` — the temperature value at end B on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendA() -> float` — the temperature value on point C at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendB() -> float` — the temperature value on point C at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendA() -> float` — the temperature value on point D at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendB() -> float` — the temperature value on point D at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendA() -> float` — the temperature value on point E at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendB() -> float` — the temperature value on point E at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendA() -> float` — the temperature value on point F at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendB() -> float` — the temperature value on point F at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradient1A() -> float` — the effective linear thermal gradient in direction 1 on end A.
- `getThermalGradient1B() -> float` — the effective linear thermal gradient in direction 1 on end B.
- `getThermalGradient2A() -> float` — the effective linear thermal gradient in direction 2 on end A.
- `getThermalGradient2B() -> float` — the effective linear thermal gradient in direction 2 on end B.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, thermalGradient1A: float, thermalGradient1B: float, thermalGradient2A: float, thermalGradient2B: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureEndA` — Updates the temperatureEndA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureEndB` — Updates the temperatureEndB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradient1A` — Update the thermalGradient1A.
- `thermalGradient1B` — Update the thermalGradient1B.
- `thermalGradient2A` — Update the thermalGradient2A.
- `thermalGradient2B` — Update the thermalGradient2B.
- `temperaturePointCendA` — Updates the temperaturePointCendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendA` — Updates the temperaturePointDendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendA` — Updates the temperaturePointEendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendA` — Updates the temperaturePointFendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointCendB` — Updates the temperaturePointCendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendB` — Updates the temperaturePointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendB` — Updates the temperaturePointEendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendB` — Updates the temperaturePointFendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `inputType` — Updates the inputType.


## `apex.environment.LoadTemperatureGradientBeam2Variable`  (extends `Load`)
This class represents a spatially varying temperature load applied to 1D Element with two nodes. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPRB entry for each element within the scope of the region with which it is associated. The variation of temperatures across the elements that this load references is defined using a DFEMFieldBeamDistributedLoad2. This field defines the elements that represent the region to which this load is applied as well as the variation of load values across that region. Two different types of load distributions are supported by DFEMFieldBeamDistributedLoad2, "Element uniform" distributions enable definition of a uniform temperature for each element within the scope of the load. "Element variable" distributions enable definition of a variable temperature for each element within the scope of the load.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradientBeam2` — a DFEMFieldTemperatureBeam2 that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam2) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadTemperatureGradientBeam3`  (extends `Load`)
A spatially invariant temperature load acting on 1D elements with three nodes. The constant temperature load may be applied to one or more Elements directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMPB3 entry.
Properties: `inputType`, `target`, `temperatureEndA`, `temperatureEndB`, `temperatureMidC`, `temperaturePointCendA`, `temperaturePointCendB`, `temperaturePointCmidC`, `temperaturePointDendA`, `temperaturePointDendB`, `temperaturePointDmidC`, `temperaturePointEendA`, `temperaturePointEendB`, `temperaturePointEmidC`, `temperaturePointFendA`, `temperaturePointFendB`, `temperaturePointFmidC`, `thermalGradientYA`, `thermalGradientYB`, `thermalGradientYC`, `thermalGradientZA`, `thermalGradientZB`, `thermalGradientZC`

Methods:

- `getInputType() -> apex.attribute.InputType` — The argument to define the load distribution on a single element. If the inputType is element uniform, only temperature value and thermal gradient at end A are necessary and they are automatically applied to end B and mid C. If the inputType is element variable, all temperature values and thermal gradients can be defined.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Curves, Edges, 1D Mesh Bodies and 1D Elements. Temperatures assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
- `getTemperatureEndA() -> float` — the temperature value at end A on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureEndB() -> float` — the temperature value at end B on the neutral axis. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperatureMidC() -> float` — the temperature value at a point C between end A and end B. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendA() -> float` — the temperature value on point C at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCendB() -> float` — the temperature value on point C at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointCmidC() -> float` — the temperature value on point C at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendA() -> float` — the temperature value on point D at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDendB() -> float` — the temperature value on point D at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointDmidC() -> float` — the temperature value on point D at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendA() -> float` — the temperature value on point E at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEendB() -> float` — the temperature value on point E at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointEmidC() -> float` — the temperature value on point E at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendA() -> float` — the temperature value on point F at end A, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFendB() -> float` — the temperature value on point F at end B, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getTemperaturePointFmidC() -> float` — the temperature value on point F at mid C, used for stress recovery. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `getThermalGradientYA() -> float` — the effective linear thermal gradient in local direction y on end A.
- `getThermalGradientYB() -> float` — the effective linear thermal gradient in direction y on end B.
- `getThermalGradientYC() -> float` — the effective linear thermal gradient in direction y on mid C.
- `getThermalGradientZA() -> float` — the effective linear thermal gradient in direction z on end A.
- `getThermalGradientZB() -> float` — the effective linear thermal gradient in direction z on end B.
- `getThermalGradientZC() -> float` — the effective linear thermal gradient in direction z on mid C.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureEndA: float, temperatureEndB: float, temperatureMidC: float, thermalGradientYA: float, thermalGradientZA: float, thermalGradientYB: float, thermalGradientZB: float, thermalGradientYC: float, thermalGradientZC: float, temperaturePointCendA: float, temperaturePointDendA: float, temperaturePointEendA: float, temperaturePointFendA: float, temperaturePointCendB: float, temperaturePointDendB: float, temperaturePointEendB: float, temperaturePointFendB: float, temperaturePointCmidC: float, temperaturePointDmidC: float, temperaturePointEmidC: float, temperaturePointFmidC: float, inputType: apex.attribute.InputType) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureEndA` — Updates the temperatureEndA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureEndB` — Updates the temperatureEndB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperatureMidC` — Updates the temperatureMidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `thermalGradientYA` — Updates the thermalGradientYA.
- `thermalGradientZA` — Updates the thermalGradientZA.
- `thermalGradientYB` — Updates the thermalGradientYB.
- `thermalGradientZB` — Updates the thermalGradientZB.
- `thermalGradientYC` — Updates the thermalGradientYC.
- `thermalGradientZC` — Updates the thermalGradientZC.
- `temperaturePointCendA` — Updates the temperaturePointCendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendA` — Updates the temperaturePointDendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendA` — Updates the temperaturePointEendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendA` — Updates the temperaturePointFendA. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointCendB` — Updates the temperaturePointCendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDendB` — Updates the temperaturePointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEendB` — Updates the temperaturePointEendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFendB` — Updates the temperaturePointDendB. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointCmidC` — Updates the temperaturePointCmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointDmidC` — Updates the temperaturePointDmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointEmidC` — Updates the temperaturePointEmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `temperaturePointFmidC` — Updates the temperaturePointFmidC. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
- `inputType` — Updates the inputType.


## `apex.environment.LoadTemperatureGradientBeam3Variable`  (extends `Load`)
This class represents a spatially varying temperature load applied to 1D Element with three nodes. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different element. All of the individual temperatures composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMPB3 entry for each element within the scope of the region with which it is associated. The variation of temperatures across the elements that this load references is defined using a DFEMFieldBeamDistributedLoad3. This field defines the elements that represent the region to which this load is applied as well as the variation of load values across that region. Two different types of load distributions are supported by DFEMFieldBeamDistributedLoad3, "Element uniform" distributions enable definition of a uniform temperature for each element within the scope of the load. "Element variable" distributions enable definition of a variable temperature for each element within the scope of the load.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureGradientBeam3` — a DFEMFieldTemperatureBeam3 that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureGradientBeam3) -> None`
Update method. One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name.
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadTemperatureNodal`  (extends `Load`)
A spatially invariant temperature load acting on Nodes. The constant temperature load may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create a Nastran TEMP entry.
Properties: `target`, `temperatureValue`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the Temperature will be applied to. Temperatures may be assigned to Solids, Cells, Surfaces, Faces, Curves, Edges, Points, Vertices, 1D, 2D and 3D Mesh Bodies and Nodes. Temperatures assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTemperatureValue() -> float` — the temperature value. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, temperatureValue: float) -> None`
Updates one or more properties of the Temperature. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the temperature load.
- `description` — Updates the description of the temperature load.
- `id` — Updates the id of the temperature load.
- `target` — Updates the target of the temperature load.
- `temperatureValue` — Updates the temperatureValue. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system. You can specify other temperature unit by setting apex.createCustomUnitSystem.


## `apex.environment.LoadTemperatureNodalVariable`  (extends `Load`)
This class represents a spatially varying temperature load applied to Nodes. A single instance of this class may include a multiplicity of individual temperature loads each applied to a different node. All of the individual loads composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one TEMP entry for each node within the scope of the region with which it is associated. The variation of temperature load across the nodes that this load references is defined using a DFEMFieldTemperatureNodal. This field defines nodes that represent the region to which this load is applied as well as the variation of load values across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTemperatureNodal` — a DFEMFieldLoadDistributed that identifies elements that represent the region to which this load is applied as well as the distribution of loads across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTemperatureNodal) -> None`
Update method.One or more properties may be updated in each call to update().

- `id` — Update the id.
- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.LoadTemperatureProperty`  (extends `Entity`)
Base Class LoadTemperatureProperty. In 2021.1 release, Apex supports the sub classes: LoadTemperaturePropertyStaticConstant and LoadTemperaturePropertyStaticVariable. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal, LoadTemperatureNodalVariable.

## `apex.environment.LoadTemperaturePropertyStaticConstant`  (extends `LoadTemperatureProperty`)
Class LoadTemperaturePropertyStaticConstant. It represents a constant LoadTemperature uniformly applied to the model region, the temperatures on the whole model region are the same value. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal.
Properties: `id`, `temperatureValue`

Methods:

- `getId() -> int` — An optional load ID defined in TemperaturePropertyStaticConstant and assigned to the associated LoadTemperature. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal.
- `getTemperatureValue() -> float` — the temperature value. It represents a Temperature quantity and must be specified using units of Temperature from the active script unit system.You can specify other temperature unit by setting apex.createCustomUnitSystem. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal.
#### `update(temperatureValue: float, id: int) -> None`
Update this LoadTemperaturePropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodal.

- `temperatureValue` — of this LoadTemperaturePropertyStaticConstant
- `id` — An optional load ID defined in TemperaturePropertyStaticConstant and assigned to the associated LoadTemperature. If omitted, the system will assign a default load ID.

One or more properties may be updated in each call to update().


## `apex.environment.LoadTemperaturePropertyStaticVariable`  (extends `LoadTemperatureProperty`)
Class LoadTemperaturePropertyStaticVariable. It represents a spatial varying LoadTemperature applied to the model region, the temperatures on the whole model region are not the same. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodalVariable.
Properties: `id`, `temperatureValues`

Methods:

- `getId() -> int` — An optional load ID defined in LoadTemperaturePropertyStaticVariable and assigned to the associated LoadTemperature. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodalVariable.
- `getTemperatureValues() -> {str:{dict}}` — A nested Dictionary containing the pathName of the MeshBody on which the LoadTemperature is applied and the nodes IDs and the associated temperature values. The key of the top level dictionary is a string that represents the pathName of a MeshBody and the associated value is a secondary dictionary containing the individual nodes/temperatures. Each MeshBody that has one or more nodes referenced by the variable LoadTemperature will be included in the top level dictionary. For example, a LoadTemperature is applied to two different MeshBodies the top level dictionary will include two items - {"Model_1/Part 1/Mesh 1" : {dict1}, "Model_1/Part 2/Mesh 2": {dict2}} The secondary dictionary contains the information about which nodes are included in the variable LoadTemperature and the temperature values applied to each node. The type of distribution is identified in the secondary dictionary by the "identifier_type" key which is a string type. The associated value is a string type that must be "NODE_ID" as Apex only supports nodal temperature in 2021.1 release. For identifier type of NODE_ID, the temperature field is defined by the secondary dictionary items with "node_ids" and "temperatures" keys that identify the nodes IDs and temperature values. The value associated with the node_ids key is a List of integers, each integer identifying the node id. The value associated with the temperatures key is a List of floats, each float identifying the single temperature value associated with the corresponding node. The node_ids and temperatures lists must be of equal length with the temperature values indices aligned with the node ids indices. Example : LoadTemperature defined on three nodes of "Mesh 1" in "Model_1". {"Model_1/Part 1/Mesh 1" : { "identifier_type" : "NODE_ID", "node_ids" : [1000,1001,1002], "temperatures" : [301.52,302.78,303.92] } } THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodalVariable.
#### `update(temperatureValues: {str:{dict}}, id: int) -> None`
Update this LoadTemperaturePropertyStaticVariable. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTemperatureNodalVariable.

- `temperatureValues` — of this LoadTemperaturePropertyStaticVariable
- `id` — An optional load ID defined in LoadTemperaturePropertyStaticVariable and assigned to the associated LoadTemperature.

One or more properties may be updated in each call to update().


## `apex.environment.LoadTimeDelay`  (extends `Load`)
The time delay term in the equations of the dynamic loading function. It should be applied to the nodes of the excitation loads of the dynamitic load, with the same degrees of freedom. When used to generate a Nastran model this class will create a Nastran DELAY entry.
Properties: `target`, `timeDelayRx`, `timeDelayRy`, `timeDelayRz`, `timeDelayX`, `timeDelayY`, `timeDelayZ`

Methods:

- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the time delay will be applied to. Time delays may be assigned to Surfaces, Faces, Curves, Edges, Points, Vertices, 1D and 2D Mesh Bodies and Nodes. Time delays assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
- `getTimeDelayRx() -> float` — the time delay value in the rotation X component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelayRy() -> float` — the time delay value in the rotation Y component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelayRz() -> float` — the time delay value in the rotation Z component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelayX() -> float` — the time delay value in the translation X Component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelayY() -> float` — the time delay value in the Y component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `getTimeDelayZ() -> float` — the time delay value in the Z component. It is a Time quantity and must be defined using the units of Time from the active script unit system.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, timeDelayX: float, timeDelayY: float, timeDelayZ: float, timeDelayRx: float, timeDelayRy: float, timeDelayRz: float) -> None`
Updates one or more properties of the time delay. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Update the name of this LoadTimeDelay
- `description` — Update the description of this LoadTimeDelay
- `id` — Updates the id of the time delay.
- `target` — Updates the target of the time delay.
- `timeDelayX` — Updates the timeDelayX. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelayY` — Updates the timeDelayY. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelayZ` — Updates the timeDelayZ. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelayRx` — Updates the timeDelayRx. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelayRy` — Updates the timeDelayRy. It is a Time quantity and must be defined using the units of Time from the active script unit system.
- `timeDelayRz` — Updates the timeDelayRz. It is a Time quantity and must be defined using the units of Time from the active script unit system.


## `apex.environment.LoadTimeDelayVariable`  (extends `Load`)
This class represents a spatially varying time delay applied to Node. A single instance of this class may include a multiplicity of individual time delays each applied to a different node. All of the individual time delays composed by this time delay object share a common ID. When used in a Nastran simulation this class will give rise to one DELAY entry for each active degree of freedom and the nodes applied with the excitation loads.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldTimeDelay` — a DFEMFieldTimeDelay that identifies nodes that represent the region to which this time delay is applied as well as the distribution of delays across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldTimeDelay) -> None`
Updates one or more properties of the time delay. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id.
- `name` — Update the name of this LoadTimeDelayVariable
- `description` — Update the description of this LoadTimeDelayVariable
- `spatialTarget` — Updates the spatialTarget.


## `apex.environment.LoadTotal`  (extends `Load`)
A spatially invariant total load acting on 2D elements or the faces of 3D elements. The load magnitude is a Force and the direction is defined by three force components in a coordinate system. The force is uniformly distributed on the total area of the elements or element faces. The constant total load may be applied to one or more 2D elements or 3D element faces directly or through their association to 2D mesh bodies and/or geometry faces. When used to generate a Nastran model this class will create a Nastran PLOAD4 entry.
Properties: `forceX`, `forceY`, `forceZ`, `orientation`, `target`

Methods:

- `getForceX() -> float` — the total force in X component, it is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getForceY() -> float` — the total force in Y component, it is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getForceZ() -> float` — the total force in Z component, it is a Force quantity and must be defined using the units of Force from the active script unit system.
- `getOrientation() -> apex.IOrientation` — the orientation used to define the direction of the pressure. Currently it only accepts a coordinate system object.
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the load will be applied to. Loads may be assigned to Faces, 2D Mesh Bodies, 2D Elements and Element Faces. Loads assigned to geometry entities will be transferred to the Elements associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, orientation: apex.IOrientation, target: apex.EntityCollection, forceX: float, forceY: float, forceZ: float) -> None`
Updates one or more properties of the load. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the load.
- `description` — Updates the description of the load.
- `id` — Updates the id of the load.
- `orientation` — Updates the orientation of the load.
- `target` — Updates the target of the load.
- `forceX` — Updates the total force in X component, it is a Force quantity and must be defined using the units of Force from the active script unit system.
- `forceY` — Updates the total force in Y component, it is a Force quantity and must be defined using the units of Force from the active script unit system.
- `forceZ` — Updates the total force in Z component, it is a Force quantity and must be defined using the units of Force from the active script unit system.


## `apex.environment.LoadTraction`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
LoadTraction is used to define a distributed load across a model region. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed, LoadTotal. The magnitude and/or the direction of the load may be defined as a: Constant load per unit area or load per unit length, causing the constant load/(area, length) value to be applied equally to every element in the target region. Spatially varying load per unit area or load per unit length, causing a field of load/(area, length) values to be applied to every element/node in the target region. Single value representing the total aggregate force, causing a distribution of individual loads across the elements/nodes in the target region. In current release, Apex only supports static and constant LoadTractionProperty: LoadTractionPropertyStaticConstant LoadTractionPropertyStaticTotal Note that the properties for 1D and 2D types use different properties since the quantity is different - 2D LoadTractions are defined as load/unit area and 1D LoadTractions are defined as load/unit length. Only 2D type is supported in 2021.2 release.
Properties: `orientation`, `target`, `tractionProperty`

Methods:

- `getOrientation() -> apex.construct.Orientation` — Returns Orientation of the LoadTraction. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed, LoadTotal.
- `getTarget() -> apex.EntityCollection` — Returns the target entities that the LoadTraction is applied to. The supported target types are face, 2D mesh, 2D element and element face in 2021.2 release. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed, LoadTotal.
- `getTractionProperty() -> LoadTractionProperty` — Returns the property of this LoadTraction. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed, LoadTotal.
#### `update(name: str, description: str, target: apex.EntityCollection, tractionProperty: LoadTractionProperty, orientation: apex.construct.Orientation) -> None`
Update this LoadTraction. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed, LoadTotal.

- `name` — of this LoadTraction
- `description` — of this LoadTraction
- `target` — of this LoadTraction
- `tractionProperty` — of this LoadTraction
- `orientation` — of this LoadTraction

One or more properties may be updated in each call to update().


## `apex.environment.LoadTractionCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of LoadTraction, based on EntityCollection.

Methods:

- `LoadTractionCollection() -> None` — Construct a new LoadTractionCollection.

## `apex.environment.LoadTractionProperty`  (extends `Entity`)
Base Class LoadTractionProperty. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed, LoadTotal.

## `apex.environment.LoadTractionPropertyStaticConstant`  (extends `LoadTractionProperty`)
Class LoadTractionPropertyStaticConstant. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
Properties: `id`, `pressureX`, `pressureY`, `pressureZ`

Methods:

- `getId() -> int` — Gets the load ID of the LoadTractionPropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
- `getPressureX() -> float` — Gets Optional - the pressure value in X component. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
- `getPressureY() -> float` — Gets Optional - the pressure value in Y component. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
- `getPressureZ() -> float` — Gets Optional - the pressure value in Z component. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
- `removePressureX() -> None` — Remove the X component of this TractionLoad. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
- `removePressureY() -> None` — Remove the Y component of this TractionLoad. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
- `removePressureZ() -> None` — Remove the Y component of this TractionLoad. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.
#### `update(pressureX: float, pressureY: float, pressureZ: float, id: int) -> None`
Update this LoadTractionPropertyStaticConstant. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadDistributed.

- `pressureX` — of this LoadTractionPropertyStaticConstant
- `pressureY` — of this LoadTractionPropertyStaticConstant
- `pressureZ` — of this LoadTractionPropertyStaticConstant
- `id` — of this LoadTractionPropertyStaticConstant

One or more properties may be updated in each call to update().


## `apex.environment.LoadTractionPropertyStaticTotal`  (extends `LoadTractionProperty`)
Class LoadTractionPropertyStaticTotal. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
Properties: `forceX`, `forceY`, `forceZ`, `id`

Methods:

- `getForceX() -> float` — Gets Optional - the force value in X component. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
- `getForceY() -> float` — Gets Optional - the force value in Y component. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
- `getForceZ() -> float` — Gets Optional - the force value in Z component. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
- `getId() -> int` — Gets the load ID of the LoadTractionPropertyStaticTotal. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
- `removeForceX() -> None` — Remove the X component of this TractionLoad. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
- `removeForceY() -> None` — Remove the Y component of this TractionLoad. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
- `removeForceZ() -> None` — Remove the Z component of this TractionLoad. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.
#### `update(forceX: float, forceY: float, forceZ: float, id: int) -> None`
Update this LoadTractionPropertyStaticTotal. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadTotal.

- `forceX` — of this LoadTractionPropertyStaticTotal
- `forceY` — of this LoadTractionPropertyStaticTotal
- `forceZ` — of this LoadTractionPropertyStaticTotal
- `id` — of this LoadTractionPropertyStaticTotal

One or more properties may be updated in each call to update().


## `apex.environment.PreloadBolt`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class PreloadBolt. PreloadBolt prescribes preload of 3D bolts on the mechanical system. The bolt preload can either a force or displacement applying to the bolt.
Properties: `activeRep`, `target`

Methods:

#### `createPreloadBoltRep(id: int = 0, name: str = "####", description: str = "####", repProperty: apex.environment.PreloadBoltProperty = None) -> apex.environment.PreloadBoltRep`
Create and add a new PreloadBoltRep to this Bolt preload.

- `id` — Optional-id of the bolt preload rep.
- `name` — Optional-name of the bolt preload rep.
- `description` — Optional-description of the bolt preload rep.
- `repProperty` — Property of the Bolt Preload rep.

- `getActiveRep() -> apex.environment.PreloadBoltRep` — Get the currently used BoltPreloadRep in this bolt preload.
- `getTarget() -> apex.EntityCollection` — Get the target entities that the PreloadBolt is applied to. The supported target is 3D bolt object.
#### `update(name: str, description: str, target: apex.EntityCollection) -> None`
Update this bolt preload.

- `name` — Optional-name of the bolt preload.
- `description` — Optional-description of the bolt preload.
- `target` — The target entities that the PreloadBolt is applied to.The supported target is 3D bolt object.


## `apex.environment.PreloadBoltCollection`  (extends `EntityCollection`)
Iterable collection of PreloadBolt, based on EntityCollection.

Methods:

- `PreloadBoltCollection() -> None` — Construct a new PreloadBoltCollection.

## `apex.environment.PreloadBoltProperty`  (extends `Entity`)

## `apex.environment.PreloadBoltPropertyStatic`  (extends `PreloadBoltProperty`)
Class PreloadBoltPropertyStatic. Base Class PreloadBoltProperty. In the first release, Apex will support the derived classes: PreloadBoltPropertyStatic. In future release, Apex will support PreloadBoltPropertyDynamic.
Properties: `force`, `overclosure`, `preloadType`

Methods:

- `getForce() -> float` — Get the force of bolt preload, it is only available when preloadType = Force.
- `getOverclosure() -> float` — Get the overclosure of bolt preload, it is only available when preloadType = Overclosure.
- `getPreloadType() -> apex.environment.BoltPreloadType` — Get the bolt preload definition type.
#### `update(preloadType: apex.environment.BoltPreloadType, force: float, overclosure: float) -> None`
Update static bolt preload property.

- `preloadType` — Bolt preload definition type.
- `force` — Force of bolt preload, it is only available when preloadType = Force
- `overclosure` — Overclosure of bolt preload, it is only available when preloadType = Overclosure


## `apex.environment.PreloadBoltRep`  (extends `Entity`, `IName`)
Class PreloadBoltRep. The PreloadBoltRep of this bolt preload. The PreloadBoltRep can be only constructed by addRep() method in an existing PreloadBolt object. Note that there can be multiple PreloadBoltReps in one Bolt preload, for each PreloadBoltRep, it can reference one PreloadBoltRepProperty. In current release, only single rep is supported.
Properties: `id`, `repProperty`

Methods:

- `getId() -> int` — Get the ID of the bolt preload rep.
- `getRepProperty() -> apex.environment.PreloadBoltProperty` — Get the property of the Bolt preload rep.
#### `update(name: str, description: str, id: int, repProperty: PreloadBoltProperty) -> None`
Update the bolt preload rep.

- `name` — Optional-name of the bolt preload rep.
- `description` — Optional-description of the bolt preload rep.
- `id` — Optional-id of the bolt preload rep.
- `repProperty` — Property of the Bolt Preload rep.


## `apex.environment.Pressure`  (extends `Load`)
A normal pressure load applied on surfaces or faces of solids, the pressure direction is always normal to the surfaces or faces and the pressure value is constant across the regions.
Properties: `pressure`, `target`

Methods:

- `getPressure() -> float` — the pressure value on the 1st corner of the element.
- `getTarget() -> apex.EntityCollection` — the entityCollection that the load is applied to.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, pressure: float) -> None`
Update method. One or more properties may be updated in each call to update().

- `name` — Update the name.
- `description` — Update the description.
- `id` — Update the id.
- `target` — Update the target.
- `pressure` — Update the pressure.


## `apex.environment.PressureVariable`  (extends `Load`)
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldPressure`
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldPressure) -> None`

- `id` — Update the id of this PressureVariable
- `name` — Update the name of this PressureVariable
- `description` — Update the description of this PressureVariable
- `spatialTarget` — Update the spatialTarget of this PressureVariable


## `apex.environment.SupportFreeBody`  (extends `Constraint`)
A constraint defines the reference degrees-of-freedom for rigid body motion. It is usually used for inertia relief. The constant support may be applied to one or more Nodes directly or through their association to mesh bodies and/or geometry bodies. When used to generate a Nastran model this class will create one or more SUPORT entries for each Node.
Properties: `constrainRotationX`, `constrainRotationY`, `constrainRotationZ`, `constrainTranslationX`, `constrainTranslationY`, `constrainTranslationZ`, `orientation`, `target`

Methods:

- `getConstrainRotationX() -> bool` — the argument to indicate whether the rotation X is constrained or not.
- `getConstrainRotationY() -> bool` — the argument to indicate whether the rotation Y is constrained or not.
- `getConstrainRotationZ() -> bool` — the argument to indicate whether the rotation Z is constrained or not.
- `getConstrainTranslationX() -> bool` — the argument to indicate whether the translation X is constrained or not.
- `getConstrainTranslationY() -> bool` — the argument to indicate whether the translation Y is constrained or not.
- `getConstrainTranslationZ() -> bool` — the argument to indicate whether the translation Z is constrained or not.
- `getOrientation() -> apex.IOrientation` — the orientation of the constraint. Currently it must be a coordinate system
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the constraint will be applied to. Constraints may be assigned to Solids, Cells, Faces, Curves, Edges and Nodes. Constraints assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, target: apex.EntityCollection, constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool, orientation: apex.IOrientation) -> None`
Updates one or more properties of the constraint. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the support.
- `description` — Updates the description of the support.
- `target` — Updates the target of the support.
- `constrainTranslationX` — Updates the constrainTranslationX.
- `constrainTranslationY` — Updates the constrainTranslationY.
- `constrainTranslationZ` — Updates the constrainTranslationZ.
- `constrainRotationX` — Updates the constrainRotationX.
- `constrainRotationY` — Updates the constrainRotationY.
- `constrainRotationZ` — Updates the constrainRotationZ.
- `orientation` — Updates the orientation.


## `apex.environment.SupportFreeBody1`  (extends `Constraint`)
An alternate form of Support, the only difference is that Support1 has id.
Properties: `constrainRotationX`, `constrainRotationY`, `constrainRotationZ`, `constrainTranslationX`, `constrainTranslationY`, `constrainTranslationZ`, `orientation`, `target`

Methods:

- `getConstrainRotationX() -> bool` — the argument to indicate whether the rotation X is constrained or not.
- `getConstrainRotationY() -> bool` — the argument to indicate whether the rotation Y is constrained or not.
- `getConstrainRotationZ() -> bool` — the argument to indicate whether the rotation Z is constrained or not.
- `getConstrainTranslationX() -> bool` — the argument to indicate whether the translation X is constrained or not.
- `getConstrainTranslationY() -> bool` — the argument to indicate whether the translation Y is constrained or not.
- `getConstrainTranslationZ() -> bool` — the argument to indicate whether the translation Z is constrained or not.
- `getOrientation() -> apex.IOrientation` — the orientation of the constraint. Currently it must be a coordinate system
- `getTarget() -> apex.EntityCollection` — an EntityCollection identifying the entities that the constraint will be applied to. Constraints may be assigned to Solids, Cells, Faces, Curves, Edges and Nodes. Constraints assigned to geometry entities will be transferred to the Nodes associated with these geometry entities when the model is exported for solution.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool, orientation: apex.IOrientation) -> None`
Updates one or more properties of the support. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `name` — Updates the name of the support.
- `description` — Updates the description of the support.
- `id` — Updates the id of the support.
- `target` — Updates the target of the support.
- `constrainTranslationX` — Updates the constrainTranslationX.
- `constrainTranslationY` — Updates the constrainTranslationY.
- `constrainTranslationZ` — Updates the constrainTranslationZ.
- `constrainRotationX` — Updates the constrainRotationX.
- `constrainRotationY` — Updates the constrainRotationY.
- `constrainRotationZ` — Updates the constrainRotationZ.
- `orientation` — Updates the orientation.


## `apex.environment.SupportFreeBody1Variable`  (extends `Constraint`)
An alternate form of SupportFreeBodyVariable, the only difference is that Support1 has id.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldSupportFreeBody` — a DFEMFieldSupport that identifies nodes that represent the region to which this support is applied as well as the distribution of supports across that region.
#### `update(id: int, name: str, description: str, spatialTarget: apex.environment.DFEMFieldSupportFreeBody) -> None`
Updates one or more properties of the support. All property arguments are optional. Properties omitted from the argument list when this method is called will be unchanged by the method and will retain their original values.

- `id` — Updates the id of the support.
- `name` — Updates the name of the support.
- `description` — Updates the description of the support.
- `spatialTarget` — Updates the spatialTarget.


## `apex.environment.SupportFreeBodyVariable`  (extends `Constraint`)
This class represents a spatially varying support applied to Nodes. A single instance of this class may include a multiplicity of individual supports each applied to a different node. All of the individual supports composed by this load share a common ID. When used in a Nastran simulation this class will give rise to one or several SUPORT entries for each node within the scope of the region with which it is associated. The variation of support across the nodes that this support references is defined using a DFEMFieldSupport. This field defines the nodes that represent the region to which this support is applied as well as the distribution of supports across that region.
Properties: `spatialTarget`

Methods:

- `getSpatialTarget() -> apex.environment.DFEMFieldSupportFreeBody` — a DFEMFieldSupport that identifies nodes that represent the region to which this support is applied as well as the distribution of supports across that region.
#### `update(name: str, description: str, spatialTarget: apex.environment.DFEMFieldSupportFreeBody) -> None`
Update method.One or more properties may be updated in each call to update().

- `name` — Update the name .
- `description` — Update the description.
- `spatialTarget` — Update the spatialTarget.


## `apex.environment.VariablePressureProfile`
Properties: `elementIds`, `faceIndices`, `faceNodeIndices`, `identifierType`, `pressureOn2DFaces`, `pressureOnFaceNodes`

