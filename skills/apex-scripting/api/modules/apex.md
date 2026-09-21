# apex

(apex module) Model, Assembly, Part, and Collection creation and access functions, and Transform and Measure functions.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.AutoManual`: `Automatic`, `Manual`
  - To identify whether operations, values etc, should be calculated Automatically by the system or provided as manual input

`apex.CollectionType`: `Collection`, `EntityCollection`, `AssemblyCollection`, `PartCollection`, `PartRepCollection`, `PartPropertyCollection`, `UserAttributeCollection`, `DesignVariableCollection`, `GeometryFeatureCollection`, `EdgeLoopCollection`, `GeometryTopologyCollection`, `GeometryBodyCollection`, `SolidCollection`, `SurfaceCollection`, `CurveCollection`, `PointCollection`, `FacetedSolidCollection`, `FacetedSurfaceCollection`, `FacetedCurveCollection`, `BoxCollection`, `CylinderCollection`, `SphereCollection`, `EllipsoidCollection`, `CellCollection`, `FaceCollection`, `EdgeCollection`, `VertexCollection`, `MeshControlEdgeCollection`, `SurfaceMeshCollection`, `CurveMeshCollection`, `SolidMeshCollection`, `HexMeshCollection`, `PointMeshCollection`, `MeshBodyCollection`, `NodeCollection`, `ElementCollection`, `ElementFaceCollection`, `ElementEdgeCollection`, `NodeIdSetCollection`, `ElementIdSetCollection`, `EdgeSeedCollection`, `SubMeshCollection`, `MeshIndependentTieCollection`, `MeshDependentTieCollection`, `ConnectorCollection`, `JointCollection`, `SeedPointCollection`, `PointSensorCollection`, `PointMassCollection`, `MaterialCollection`, `MaterialSheetCollection`, `MaterialSheetStackCollection`, `SectionCollection`, `ShellBehaviorCollection`, `PropertiesElement2DCollection`, `PropertiesElement3DCollection`, `BeamShapeCollection`, `BeamSpanCollection`, `NodeTieCollection`, `DiscreteTieCollection`, `RigidLinkCollection`, `Spring1DCollection`, `Damper1DCollection`, `SpringDamper1DCollection`, `FastenerCollection`, `BushingCollection`, `FlexibleLinkCollection`, `Spring1DRepPropertiesCollection`, `Damper1DRepPropertiesCollection`, `SpringDamper1DRepPropertiesCollection`, `BushingRepPropertiesCollection`, `SensorCollection`, `XSectionForceSensorCollection`, `XSectionForceSensorArrayCollection`, `ClearanceSensorCollection`, `InterfacePointCollection`, `AssemblyRepCollection`, `ScenarioCollection`, `StepCollection`, `EventCollection`, `LoadCaseCollection`, `ScenarioNastranCollection`, `SubcaseNastranCollection`, `StepNastranCollection`, `SubstepNastranCollection`, `ILocationCollection`, `IPhysicalCollection`, `Profile1DCollection`, `CoordinateSystemCollection`, `DatumPlaneCollection`, `LoadRepCollection`, `DisplacementConstraintCollection`, `MaterialCoverageRegionCollection`, `Property2DCoverageRegionCollection`, `NonstructuralMassCollection`, `PlyCollection`, `ZoneCollection`, `LayeredPanelCollection`, `CompoundInterfaceCollection`, `ClearanceRegionCollection`, `NonDesignRegionCollection`, `DesignSpaceCollection`, `RegionCollection`, `GroupCollection`, `ModelAssociationCollection`, `ConnectorDiscreteCollection`, `GDConfigurationCollection`, `LoadTemperatureCollection`, `LoadTractionCollection`, `LoadLugCollection`, `LoadPressureCollection`, `AdamsJointCollection`, `AdamsPointCurveCollection`, `AdamsCurveCurveCollection`, `AdamsJointMotionCollection`, `AdamsSingleComponentForceCollection`, `AdamsSingleComponentTorqueCollection`, `AdamsContactCollection`, `AdamsContactPropertyCollection`, `AdamsGeneralForceCollection`, `AdamsVectorForceCollection`, `AdamsVectorTorqueCollection`, `AdamsBushingCollection`, `AdamsTranslationalSpringCollection`, `AdamsDataElementCollection`, `AdamsMatrixCollection`, `AdamsCurveDataCollection`, `AdamsDataSplineCollection`, `DataSeriesCollection`, `DataSeriesOverStepsCollection`, `InteractionCollection`, `Bolt3DCollection`, `PreloadBoltCollection`, `ParametersSetCollection`, `SystemCellsSetCollection`, `FastenerRepPropertiesCollection`, `ContactBodyCollection`, `ThicknessOffsetFieldMidsurfaceCollection`, `DiscreteFEMFieldCollection`, `RigidFaceCollection`, `IOrientationCollection`, `NSMCombinationCollection`, `ContactTableCollection`, `NoType`
  - DEPRECATED: THIS ENUMERATOR IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. User can use type(object) to get the type directly. Enum defining all of the posible Types of Collections in Apex. A CollectionType can be obtained from any Collection using it's getCollectionType() method or "collectionType" property

`apex.ConstraintAxis`: `X`, `Y`, `Z`, `RX`, `RY`, `RZ`

`apex.DesignVariableRangeType`: `Absolute`, `Delta`, `PercentDelta`
  - Design variable range type

`apex.DesignVariableType`: `Real`, `Integer`, `String`, `Expression`, `Object`
  - Design variable type

`apex.DesignVariableUnit`: `NoUnitQuantity`, `Length`, `Mass`, `Time`, `Force`, `Angle`, `Density`, `Pressure`, `Area`, `Volume`, `Torque`, `Velocity`, `Acceleration`, `Frequency`, `Energy`, `Inertia`, `RotationalVelocity`, `RotationalAcceleration`, `AreaInertia`, `Stiffness`, `Damping`, `TorsionStiffness`, `TorsionDamping`
  - Unit

`apex.DiscreteValueMethod`: `Generate`, `EnterValues`
  - Discrete value method

`apex.DiscreteValueRange`: `EqualSpaced`, `MinStdMax`
  - Discrete value range

`apex.EntityType`: `Extension`, `Project`, `Model`, `Session`, `Catalog`, `CatalogMaterial`, `UserAttribute`, `Setting`, `DesignVariable`, `Instance`, `Assembly`, `Part`, `PartRep`, `PartProperty`, `PartPropertyRigid`, `PartPropertyModal`, `Geometry`, `GeometryBody`, `Solid`, `Surface`, `Curve`, `Point`, `FacetedSolid`, `FacetedSurface`, `FacetedCurve`, `Box`, `Cylinder`, `Sphere`, `Ellipsoid`, `GeometryTopology`, `Cell`, `Face`, `Edge`, `Vertex`, `MeshSeed`, `EdgeSeed`, `FaceSeed`, `GeometryFeature`, `Hole2D`, `Fillet2D`, `Chamfer2D`, `Hole3D`, `Fillet3D`, `Chamfer3D`, `EdgeLoop`, `MeshControlEdge`, `MeshBody`, `SolidMesh`, `SurfaceMesh`, `CurveMesh`, `HexMesh`, `PointMesh`, `SubMesh`, `SubMesh0D`, `SubMesh1D`, `SubMesh2D`, `SubMesh3D`, `Node`, `Element`, `ElementFace`, `ElementEdge`, `Penta`, `Tet`, `Hex`, `Quad`, `Tri`, `Bar`, `SeedPoint`, `Set`, `NodeIdSet`, `ElementIdSet`, `Construct`, `Sketch`, `Plane`, `DatumPlane`, `MirrorPlane`, `SketchPrimitive`, `Arc`, `Chamfer`, `Circle`, `Ellipse`, `Fillet`, `Polyline`, `Rectangle`, `SketchPoint`, `Spline`, `SketchEdge`, `SketchVertex`, `Profile1D`, `CoordinateSystem`, `Coordinate`, `Display`, `Tessellation0D`, `Tessellation1D`, `Tessellation2D`, `Attribution`, `Property`, `Material`, `MaterialCoverageRegion`, `MaterialSheet`, `MaterialSheetStack`, `ShellSection`, `ShellBehavior`, `PropertiesElement2D`, `SimpleShell`, `Shell`, `ShearPanel`, `Property2DCoverageRegion`, `PropertiesElement3D`, `PropertiesElement3DHomogeneous`, `BeamSpan`, `BeamShape`, `BeamShapeSolidRound`, `BeamShapeSolidRectangle`, `BeamShapeSolidHexagon`, `BeamShapeHollowRound`, `BeamShapeHollowRoundByThickness`, `BeamShapeHollowRectangularSymmetric`, `BeamShapeHollowRectangularAsymmetric`, `BeamShapeHollowDoubleRectangular`, `BeamShapeHat`, `BeamShapeHatClosed`, `BeamShapeCruciform`, `BeamShapeISymmetric`, `BeamShapeIAsymmetric`, `BeamShapeH`, `BeamShapeL`, `BeamShapeC`, `BeamShapeCAlternate`, `BeamShapeU`, `BeamShapeT`, `BeamShapeTSideways`, `BeamShapeTInverted`, `BeamShapeZ`, `BeamShapeNumeric`, `BeamShape1DProfile`, `BeamShapeType`, `DiscreteTie`, `NodeTie`, `PointMass`, `NonstructuralMass`, `Ply`, `Zone`, `LayeredPanel`, `Region`, `Group`, `StressStrainCurve`, `MaterialModel`, `ConstitutiveModel`, `Properties2DModel`, `Properties3DModel`, `Elasticity`, `ElasticityLinearIso`, `ElasticityLinear2DOrtho`, `ElasticityLinear2DAniso`, `ElasticityLinear3DAniso`, `ElasticityLinear3DOrtho`, `ElasticityLinear3DTransvIso`, `ViscoElasticity`, `ViscoElasticity3DAniso`, `ViscoElasticity2DAniso`, `Mass`, `ThermalExpansion`, `ThermalExpansionLinearIsotropic`, `ThermalExpansionLinear2DOrthotropic`, `ThermalExpansionLinear2DAnisotropic`, `ThermalExpansionLinear3DOrthotropic`, `ThermalExpansionLinear3DTransvIso`, `ThermalExpansionLinear3DAnisotropic`, `Failure`, `FailureIso`, `Failure2DOrth`, `Failure2DAniso`, `Failure3DOrth`, `Failure3DTransvIso`, `Plasticity`, `PlasticityStressStrain`, `PerfectlyPlastic`, `PlasticityHardeningSlope`, `Constraint`, `DisplacementConstraint`, `ConstraintDisplacementConstant`, `ConstraintSinglePointConstant`, `ConstraintExcludeAuto`, `ConstraintExcludeAuto1`, `Support1`, `Support`, `SupportFreeBody`, `SupportFreeBody1`, `ConstraintSinglePointVariable`, `ConstraintCombination`, `ConstraintDisplacementVariable`, `ConstraintExcludeAutoVariable`, `ConstraintExcludeAuto1Variable`, `SupportFreeBodyVariable`, `SupportFreeBody1Variable`, `ConstraintDisplacement`, `InitialCondition`, `InitialTemperature`, `InitialDisplacementVelocityConstant`, `InitialStrainConstant`, `InitialStressConstant`, `InitialTemperatureGradient2D`, `InitialTemperatureGradient2DHeat`, `InitialTemperatureDefault`, `InitialTemperatureGradientBeam2`, `InitialTemperatureGradientBeam3`, `InitialTemperatureNodalConstant`, `InitialTemperatureNodalVariable`, `InitialTemperatureGradient2DHeatVariable`, `InitialTemperatureGradient2DVariable`, `InitialTemperatureGradientBeam3Variable`, `InitialTemperatureGradientBeam2Variable`, `InitialStrainVariable`, `InitialStressVariable`, `InitialDisplacementVelocityVariable`, `InitialStress`, `InitialStrain`, `InitialDisplacementVelocity`, `InitialTemperatureNodal`, `Load`, `GravityLoad`, `ForceMoment`, `ForceMomentRep`, `EnforcedMotion`, `EnforcedMotionRep`, `LoadTemperature`, `LoadTemperaturePropertyStaticConstant`, `LoadTemperaturePropertyStaticVariable`, `LoadTraction`, `LoadTractionPropertyStaticConstant`, `LoadTractionPropertyStaticTotal`, `LoadLug`, `LoadLugPropertyStatic`, `LoadPressurePropertyStaticConstant`, `LoadPressurePropertyStaticVariable`, `LoadPressure`, `PreloadBolt`, `PreloadBoltRep`, `PreloadBoltProperty`, `PreloadBoltPropertyStatic`, `LoadForceComponent`, `LoadForceFollowerVector`, `LoadForceFollowerNormal`, `LoadMomentComponent`, `LoadMomentFollowerVector`, `LoadMomentFollowerNormal`, `LoadAreaFactor`, `LoadPressureArea`, `LoadPressure2D`, `Pressure`, `LoadDistributedBeam2`, `LoadDistributedBeam3`, `LoadEnforcedMotionTotal`, `LoadEnforcedMotionRelative`, `LoadTemperatureNodal`, `LoadTemperatureGradientBeam3`, `LoadTemperatureDefault`, `TemperatureHeatTransfer`, `LoadTemperatureGradient2DHeat`, `TemperatureSurface`, `LoadTemperatureGradient2D`, `LoadTemperatureGradientBeam2`, `LoadDeformationAxial`, `LoadAccelerationSpatial`, `LoadAccelerationNodal`, `LoadForceRotational`, `LoadDynamicAcoustic`, `LoadDynamicFrequency1`, `LoadDynamicFrequency2`, `LoadDynamicTimeTabular`, `LoadDynamicTimeAnalytical`, `LoadCombinationStatic`, `LoadCombinationDynamic`, `LoadForceComponentVariable`, `LoadForceFollowerVectorVariable`, `LoadForceFollowerNormalVariable`, `LoadMomentComponentVariable`, `LoadMomentFollowerVectorVariable`, `LoadMomentFollowerNormalVariable`, `LoadTimeDelay`, `LoadPhaseLead`, `LoadTemperatureNodalVariable`, `LoadTemperatureGradient2DVariable`, `LoadPressure2DVariable`, `LoadTemperatureGradientBeam3Variable`, `LoadTemperatureGradientBeam2Variable`, `LoadDistributed`, `LoadTemperatureGradient2DHeatVariable`, `LoadAccelerationNodalVariable`, `LoadDeformationAxialVariable`, `LoadDistributedBeam2Variable`, `LoadAreaFactorVariable`, `LoadPressureAreaVariable`, `LoadDistributedBeam3Variable`, `LoadEnforcedMotionTotalVariable`, `LoadEnforcedMotionRelativeVariable`, `LoadDistributedVariable`, `PressureVariable`, `LoadPhaseLeadVariable`, `LoadTimeDelayVariable`, `LoadTotal`, `Interaction`, `Joint`, `Connector`, `MeshIndependentTie`, `MeshDependentTie`, `InteractionRep`, `InteractionPropertyGeometric`, `InteractionPropertyPhysical`, `RigidFace`, `ContactBodyProperty`, `ContactBody`, `RigidLink`, `Spring1D`, `Damper1D`, `SpringDamper1D`, `Bushing`, `FlexibleLink`, `Gap`, `Fastener`, `Sensor`, `XSectionForceSensor`, `XSectionForceSensorArray`, `ClearanceSensor`, `InterfacePoint`, `Instrumentation`, `PointSensor`, `RemotePoint`, `Study`, `AssemblyRep`, `GenerativeDesignStudy`, `Scenario`, `Step`, `StaticStep`, `StaticStepNastranSol400`, `DynamicsStep`, `ModalFrequencyStep`, `MultiBodyTransientStep`, `BucklingStep`, `ModesStep`, `MeshlessGenerativeDesignStep`, `GenerativeDesignStaticStep`, `Event`, `LoadCase`, `ScenarioSetNastran`, `ScenarioSetTime`, `ScenarioSetFrequency`, `ScenarioSetRandId`, `ScenarioSetFrfcompId`, `ScenarioSetModeId`, `ScenarioSetGridComponent`, `ScenarioSetGridId`, `LoadCaseItem`, `ScenarioNastran`, `SubcaseNastran`, `StepNastran`, `SubstepNastran`, `SimulationSettingsGenerativeDesign`, `StatePlot`, `DeformVisualization`, `ContourVisualization`, `VectorVisualization`, `ResultProbe0D`, `ColorMap`, `Machining`, `ClearanceRegion`, `GenDes`, `CompoundInterface`, `NonDesignRegion`, `DesignSpace`, `GDConfiguration`, `ChartPlot`, `SBMTChart`, `ChartPlotXY`, `DataTable`, `MatrixMN`, `DataSeries`, `DataSeriesVMTBeamSpan`, `DataSeriesVMTSensorArray`, `DataSeriesOverSteps`, `DataSeriesTransient`, `ModelAssociation`, `XSectionForceSensorPlot`, `Block`, `Bolt`, `Bolt3D`, `ConnectorDiscrete`, `DiscreteFEMField`, `ThicknessOffsetField`, `ThicknessOffsetFieldConstant`, `ThicknessOffsetFieldMidsurface`, `MaterialOrientationField2D`, `MaterialOrientationField2DAlignCurve`, `MaterialOrientationField2DCoordinate`, `NSMCombination`, `ContactTable`, `ParametersSet`, `SystemCellsSet`, `ConstraintSinglePoint`, `Table`, `TABLED1`, `TABLED2`, `TABLED3`, `TABLED4`, `ITER`, `EIGB`, `EIGR`, `RCROSS`, `DAMPING`, `HYBDAMP`, `RANDPS`, `RANDT1`, `TSTEP`, `TABDMP1`, `TABRND1`, `EIGRL`, `NLSTEP`, `NoType`, `ModelSetNastran`, `ModelSet3Nastran`
  - DEPRECATED: THIS ENUMERATOR IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. User can use type(object) to get the type directly. Enum defining all of the posible Types of Entities in Apex. An EntityType can be obtained from any Entity using it's getEntityType() method or "entityType" property

`apex.ExportProperty`: `AsDefined`, `Inline`, `External`
  - Type of ExportProperty argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given: "Inline" or "External"

`apex.GeometryExportOrganization`: `Multiple`, `Single`
  - Whether export geometry top level parts/assemblies to a single geometry file or multiple geometry file

`apex.ModelAssociationScope`: `All`, `Visible`, `Selected`
  - Type of ModelAssociationScope in Apex

`apex.ModelResultsImportOptions`: `Model`, `Results`, `Both`
  - To control whether Model data, Results data or both Model and Results data is imported

`apex.PartRepPropertyType`: `FE`, `Rigid`, `Flex`, `Volume`, `UnKnown`
  - Possible PartRepPropertyType Options in glef

`apex.TransformMethod`: `TranslateRotate`, `Mirror`

`apex.TransformOption`: `Move`, `Copy`
  - Possible Transformation Options in Apex

`apex.UserAttributeType`: `Int`, `Str`, `Float`, `Bool`
  - Possible UserAttribute Types

`apex.VirtualFaceExportMethod`: `NurbsOnly`, `NurbsAndFaceted`
  - VirtualFaceExportMethod This enumeration controls the rules for exporting virtual faces. This applies to exportGeometry API only. It controls what is permitted for converting virtual topology to exportable faces with the same topology. If set to NurbsAndFaceted, then the system will try to convert to NURBS, and if that fails, it will then convert the face into a faceted face. If set to NurbsOnly, then it will only try NURBS for each face

## Module functions

### `apex.assemblyCollection(assemblyList: [Assembly] = []) -> AssemblyCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.AssemblyCollection().

- `assemblyList` — optional list of Assemblys to add to the collection.

For example:

### `apex.beginUndoIndent() -> None`
Begin indenting commands. Commands indented at the same level will undo/redo together.

### `apex.clone(target: apex.Entity = None) -> apex.Entity`
Clone the target object and return a new object with the same type. The new object will have the same attributes with the input target except the unique attributes such as the name and id.

- `target` — The entity that will need to be cloned. In current release, the acceptable objects are limited to material, load. The unsupported objects will raise exception. For example, force_new = apex.clone(target = force_1), after cloning, the force_new will have the same force values, components and orientations, while the force name and id are different from the force_1.

Returns: the new cloned entity

### `apex.createAssembly(name: str = "", parentName: str = "", parentAssembly: Assembly = None, parentModel: Model = None) -> Assembly`
Create a new Assembly in a Model.

- `name` — of the new assembly. default = "" (auto-named)
- `parentName` — of the parent assembly. default = "" (top level assembly)
- `parentAssembly` — object. default = 0 ( top level assembly)
- `parentModel` — object. default = 0 (top level assembly)

Returns: the created Assembly

The new assembly parent can be specified with one of the parentName, parentAssembly, or parentModel args. If the parentModel is given, the new assembly will be top level assembly in that model. If the parentAssembly is given, the new assembly will be a child of it. If the parentName is given, the new assembly will be a child of it. Any arg not needed can be omitted (defaults will be used)

### `apex.createCustomUnitSystem(unitSystemName: str) -> str`
create custom unit system.

- `unitSystemName` — stand for custom unit system data.

Returns: the created unit system label

### `apex.createDataTable2Col(column1: [float], column2: [float]) -> DataTable2Col`
Create a DataTable2Col.

- `column1` — of the DataTable2Col.
- `column2` — of the DataTable2Col.

### `apex.createDataTable3Col(column1: [float], column2: [float], column3: [float]) -> DataTable3Col`
Create a DataTable3Col.

- `column1` — of the DataTable3Col.
- `column2` — of the DataTable3Col.
- `column3` — of the DataTable3Col.

### `apex.createDesignVariable(name: str = "Design Variable", id: int = -INT32_MAX, description: str = "", type: apex.DesignVariableType = apex.DesignVariableType.Real, unit: apex.DesignVariableUnit = apex.DesignVariableUnit.NoUnitQuantity, value: object = 0.0, rangeType: apex.DesignVariableRangeType = apex.DesignVariableRangeType.Delta, minValue: float = -1, maxValue: float = 1, negativePercentage: float = -10, positivePercentage: float = 10, negativeDelta: float = -1, positiveDelta: float = 1, enableOptimizationParams: bool = False, moveLimit: float = 0.2, allowOptimizationToIgnoreRange: bool = False, specifyAllowableDiscreteValues: bool = False, discreteValueMethod: apex.DiscreteValueMethod = apex.DiscreteValueMethod.DiscreteValueMethodUndefined, discreteValueRange: apex.DiscreteValueRange = apex.DiscreteValueRange.DiscreteValueRangeUndefined, discreteValueNumber: int = 3, discreteValueIncludeMin: bool = True, discreteValueIncludeMax: bool = True, discreteValueList: [float] = [], allowDesignStudyToIgnoreList: bool = True) -> DesignVariable`
Create a new DesignVariable in a Model.

- `name` — An optional name for this design variable. If provided, the name must be unique within the scope of model that composes this design variable. If a non-unique name is provided, the system will silently rename the Region to ensure such name uniqueness If omitted, the system will provide a default name using the prefix "Design Variable" and concatenating the lowest integer value required to ensure name uniqueness. For example "Design Variable 5".
- `id` — Optional argument to define the ID of design variable for Real type. If omit one unique one in the model will be assigned by System automatically.
- `description` — Optional argument to describe the design variable, the description is set as blank if omit.
- `type` — Define the type of design variable.
- `unit` — Optional argument to define unit for the design variable for Real type.
- `value` — Optional argument for Real type, it is set as 0.0 if omit. Optional argument for Integer type, it is set as 10 if omit. For String type, one string must be provided. For Expression type, one expression must be provided. For Object type, one Apex.Entity object must be provided.
- `rangeType` — Optional argument to define the range type for design variable for Real or Integer type.
- `minValue` — Optional argument to define the minimum value of design variable for Real or Integer type.
- `maxValue` — Optional argument to define maximum value of design variable for Real or Integer type.
- `negativePercentage` — Optional argument to define the negative percentage of design variable for Real or Integer type.
- `positivePercentage` — Optional argument to define positive percentage of design variable for Real or Integer type.
- `negativeDelta` — Optional argument to define negative delta of design variable for Real or Integer type.
- `positiveDelta` — Optional argument to define positive delta of design variable for Real or Integer type.
- `enableOptimizationParams` — Optional argument to control the input optimization parameters take effect or not, for Real or Integer type.
- `moveLimit` — Optional argument to define the move limit of design variable for Real or Integer type.
- `allowOptimizationToIgnoreRange` — Optional argument to allow the optimization to ignore the range or not for Real or Integer type.
- `specifyAllowableDiscreteValues` — Optional boolean argument to let users to specify allowable discrete values for Real or Integer type.
- `discreteValueMethod` — Optional argument to define the method of discrete values for Real or Integer type. Users can create the list of Real values by one of two methods, and create the list of Integer values by "EnterValues" method.
- `discreteValueRange` — Optional argument to define the range for discrete value of design variable for Real type.
- `discreteValueNumber` — Optional argument to define the number of discrete values for Real type.
- `discreteValueIncludeMin` — Optional argument to control if minimum value is included in the list for Real type.
- `discreteValueIncludeMax` — Optional argument to control if maximum value is included in the list for Real type.
- `discreteValueList` — Define the list of discrete values if "discreteValueMethod" is set as "EnterValues" for Real or Integer type.
- `allowDesignStudyToIgnoreList` — Optional argument to control if allow design study to ignore List or not for Real or Integer type.

Returns: the created design variable

Create and return design variable. Any arg not needed can be omitted (defaults will be used)

### `apex.createGroup(name: str = "Group <N>", description: str = "", entities: apex.ILocationCollection = None) -> apex.Group`
Creates and return a persistent Group entity with a non-volatile name.

- `name` — An optional name for this Group. If provided, the name must be unique within the scope of model that composes this Group. If a non-unique name is provided, the system will silently rename the Group to ensure such name uniqueness. If omitted, the system will provide a default name using the prefix "Group " and concatenating the lowest integer value required to ensure name uniqueness. For example "Group 23".
- `description` — An optional description for the Group. If omitted, the description will be left blank.
- `entities` — The collection of ILocation entities that will comprise the Group. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh) 4. Node 5. Element Duplicate entities will be silently ignored Entities of unsupported type will be silently ignored.

### `apex.createModel(name: str, path: str) -> Model`
Closes current model and creates a new model.

- `name` — of the new model (folder)
- `path` — to the new model folder

Returns: the created Model

### `apex.createModelSet3Nastran(id: int = INT_MIN, name: str = "#####", set_type: str = "PROP", set_ids: [int] = []) -> apex.ModelSet3Nastran`
Creates and returns a ModelSet3Nastran The ModelSet3Nastran may optionally be initialized with an id, set type and list of ids.

- `id` — an id for this ModelSet3Nastran If omitted, Apex will assign an ID that is unique within this Model. If provided, the ID must be unique within this Model. If a non_unique ID is provided Apex will automatically and silently replace it with a unique ID
- `name` — an name for this ModelSet3Nastran
- `set_type` — the type of this ModelSet3Nastran as a string This argument may be assigned any one of the following values "GRID" - The IDs represent the IDs of finite element Grids (Nodes) "ELEM" - The IDs represent the IDs of finite element Elements "POINT" - The IDs represent the IDs of finite element Points "PROP" - The IDs represent the IDs of element properties "RBEin" - The IDs represent the IDs of rigid elements (to be INCLUIDED in MPC selections) "RBEex" - The IDs represent the IDs of rigid elements (to be EXCLUDED from MPC selections)
- `set_ids` — an optional iterable of integer values defining the IDs of the entities that this ModelSet3Nastran references

### `apex.createPart(name: str = "", parentName: str = "", parentAssembly: Assembly = None, parentModel: Model = None) -> Part`
Create a new Part in a Model.

- `name` — of the new part. default = "" (auto-named)
- `parentName` — of the new part. default = "" (top level part)
- `parentAssembly` — of the new part.
- `parentModel` — of the new part.

Returns: the created Part

The parent of the new part can be specified with one of the parentName, parentAssembly, or parentModel args. If the parentModel is given, the new part will be top level part in that model. If the parentAssembly is given, the new part will be a child of it. If the parentName is given, the new part will be a child of it. Any arg not needed can be omitted (defaults will be used)

### `apex.createPartPropertyRigid(mass: float, ixx: float, iyy: float, izz: float, ixy: float, iyz: float, izx: float, calculateProperties: bool, cm: apex.attribute.InterfacePoint, im: apex.attribute.InterfacePoint) -> apex.PartPropertyRigid`
Create a rigid part rep.

- `mass` — Mass of the Rigid Part Representation.
- `ixx` — the Ixx mass-inertial tensor component expressed in the im reference frame
- `iyy` — the Iyy mass-inertial tensor component expressed in the im reference frame
- `izz` — the Izz mass-inertial tensor component expressed in the im reference frame
- `ixy` — the Ixy mass-inertial tensor component expressed in the im reference frame
- `iyz` — the Iyz mass-inertial tensor component expressed in the im reference frame
- `izx` — the Izx mass-inertial tensor component expressed in the im reference frame
- `calculateProperties` — Update how the mass and inertia of the Rigid Part Representation is calculated
- `cm` — the Interface Point located at the Center of Mass for the Rigid Part Representation
- `im` — Interface Point located at the Inertia Reference for the Rigid Part Representation

### `apex.createRegion(name: str = "Region <N>", description: str = "", entities: apex.ILocationCollection = None) -> apex.Region`
Creates and return a persistent Region entity with a non-volatile name.

- `name` — An optional name for this Region. If provided, the name must be unique within the scope of model that composes this region. If a non-unique name is provided, the system will silently rename the Region to ensure such name uniqueness. If omitted, the system will provide a default name using the prefix "Region " and concatenating the lowest integer value required to ensure name uniqueness. For example "Region 23".
- `description` — An optional description for the Region. If omitted, the description will be left blank.
- `entities` — The collection of ILocation entities that will comprise the Region. The following entity types are currently supported, 1. GeometryBody (Solid, Surface, Curve, Point and all specializations thereof) 2. GeometryTopology (Cell, Face, Edge, Vertex) 3. MeshBody (SolidMesh, HexMesh, SurfaceMesh, CurveMesh, PointMesh) 4. Node 5. Element Duplicate entities will be silently ignored Entities of unsupported type will be silently ignored.

### `apex.createUserAttribute(userAttributeName: str, stringValue: str = "####", intValue: int = -12345, floatValue: float = NAN, boolValue: apex.ApexBool = ApexBoolUndefined) -> apex.UserAttribute`
Create a UserAttribute holding a Str, Int, Bool, or Float value. Only one of the arguments should be provided. UserAttributes can be added to Entities that support the IUserAttributes interface.

- `userAttributeName` — the attribute name.
- `stringValue` — a string.
- `intValue` — an integer value.
- `floatValue` — a floating point value.
- `boolValue` — a boolean value.

For example:

### `apex.currentModel() -> Model`
Returns the Model that is current within the Apex session. (NOTE : Current Apex releases support only a single Model per session)

### `apex.deleteCustomUnitSystem(unitSystemName: str) -> None`
delete custom unit system.

- `unitSystemName` — stand for custom unit system data.

### `apex.deleteEntities(target: EntityCollection) -> None`
Deletes multiple objects in the input target.

- `target` — the collection of Entities to delete

The input target is an EntityCollection containing all of the objects to delete. The objects in this collection can include any object that inherits from Entity

### `apex.disableParasolidCache() -> None`
Disables the Parasolid cache capability of Apex. This can be useful to improve the performance of script execution.

### `apex.disableRecoveryFileRecording() -> None`
Disables the recovery file recording capability of Apex. This can be useful to improve the performance of script execution.

### `apex.disableShowOutput() -> None`
disable show output dialog.

### `apex.disableUndoRedo() -> None`
Disables the Undo/Redo capability of Apex. This can be useful to improve the performance of script execution.

### `apex.enableParasolidCache() -> None`
Enables the Parasolid cache capability of Apex. Parasolid cache is enabled by default, and can only be disabled by calling disableParasolidCache().

### `apex.enableRecoveryFileRecording() -> None`
Enables the recovery file recording capability of Apex. Recovery file recording is enabled by default, and can only be disabled by calling disableRecoveryFileRecording().

### `apex.enableShowOutput() -> None`
enable show output dialog.

### `apex.enableUndoRedo() -> None`
Enables the Undo/Redo capability of Apex. Undo/Redo is enabled by default, and can only be disabled by calling disableUndoRedo().

### `apex.endUndoIndent(description: str = "") -> None`
End indenting commands. Commands indented at the same level will undo/redo together.

- `description` — show this description in status bar when undo/redo for all commands between beginUndoIndent() and endUndoIndent()

### `apex.entityCollection(entityList: [Entity] = []) -> apex.EntityCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.EntityCollection().

- `entityList` — optional list of Entities to add to the collection.

For example:

### `apex.exitApp() -> None`
Under normal circumstances, closes the current model and shuts down the Apex application.

However, if Apex was started using remoting.launchApplication(), apex.exitApp() should NOT be used as it will raise an exception. Under these circumstances use remoting.shutdownApplication() instead.

### `apex.find(target: str) -> apex.Entity`
Finds and returns a single Entity within the scope of the singleton Apex Project database using the input target. The input name must match at least the "name" of an entity that exists within the project. Note that name uniqueness is not required within Apex ( pathName uniqueness IS required) therefore this function is not guaranteed to return an object. If multiple objects with the same name , (but different pathNames ) are present within the Project, the method will raise an exception. If no entities exist within the Project that match the input name the method will raise an exception. In all other cases, the method will return the entity as an Entity.

- `target` — A string defining the name of entity to find.

Returns: found entity

### `apex.get(target: [{str:str}]) -> apex.EntityCollection`
Get a collection of Entities, specified by target list of key:value string dictionaries.

- `target` — list of dictionaries (string:string) specifying the Entities to retrieve. Each dictionary can identify objects of a single apex type. Multiple dictionaries can be added to the list to enable retrieval of collections of different Entity types from this method. Each Dictionary contains three key/value pairs from the following list of supported keys:

Retrieve a collection of Entities, identified using a target List of key:value Dictionaries. This method can retrieve combinations of objects of any Apex type that inherits from apex.Entity type keyThe "type" key is a required key of type string. The associated value is a string type and identifies the type of the Entities that will be recovered. The type is identified using the Class name of the required Entity - for example "Part", "Surface", "Element" etc.path keyThe "path" key is required key of type string. The associated value is a string type that uniquely identifies a named Apex object (any objects that implements the IName interface) using the pathName of that object. The Entity identified here is not retrieved, but composes the required entities which are then identified using the following name, ids or indices key/value pairs.name keyThe "name" key is an optional key of type string. The associated value is a string type and identifies the name of the named object (any object that implements the IName interface) to be retrieved. The named object must exist within object defined by path.ids keyThe "ids" key is an optional key of type string. This key is used when retrieving sub-entity object types (Types that do no implement IName) such as Cells, Faces, Edges, Vertices, Nodes or Elements). The associated value is a string type and represents a run length encoded collection of sub-entity ids for example "ids":"1-5000, 5002-5005, 5009, 50013, 60000-1000000.indices keyThe "indices" key is semantically equivalent to ids with the exception that requested entities are identified using indices instead of ids. Using indices is typically faster than using ids for nodes and elements.Example: apex.EntityCollection consisting of the Solid - "Solid 3". Identifying multiple sub-entities. The ids and indices key are used to identify objects that support ID's and Indices instead of names - these entity types are referred to as sub-entities. Nodes and Elements are sub-entities of MeshBodies. Cells, Faces, Edges and Vertices are sub-entities of GeometryBodies.Example: EntityCollection consisting of four nodes.Example: EntityCollection consisting of one Solids and four nodes.

### `apex.getApplicationInfo() -> {str:str}`
Returns a str:str dictionary containing information about the current Application instance.

Returns: str:str dictionary containing information about the current Application

The dictionary supports the following key strings: "name" - associated value string holds the name of the Application "release" - associated value string holds release name of the current Application instance "releaseDate" - associated value string holds the release date of the current Application instance "releaseType" - associated value string holds the release type string: "Pre", "Alpha", "Beta", "Production" "buildVersion" - associated value string holds the Build Version of the current Application instance

### `apex.getApplicationUnitSystemLabel() -> str`
returns the 'asciilabel' of the current Application unit system.

Returns: string 'asciilabel' of the current Application unit system.

### `apex.getAssemblies(target: [{str:str}]) -> AssemblyCollection`
Get a collection of Assemblies, specified by target list of key:value string dictionaries.

- `target` — list of dictionaries (string:string) specifying the assemblies to retrieve. Valid keys are 'path', 'name', and 'recursive'.

Returns: an AssemblyCollection of the requested assemblies

### `apex.getAssembly(pathName: str) -> Assembly`
Get a Assembly in a Model.

- `pathName` — of the assembly to get including the model name as in 'MyModel/Assembly 1'.

Returns: the found Assembly

### `apex.getBeamSpan(pathName: str) -> apex.attribute.BeamSpan`
Retrieve a apex.attribute.BeamSpan from a Model using the apex.attribute.BeamSpan pathName.

- `pathName` — pathName of the apex.attribute.BeamSpan to retrieve

Returns: a reference to the apex.attribute.BeamSpan object

### `apex.getByUserAttribute(entity: apex.Entity, userAttributeNames: [str], userAttributeValues: apex.UserAttributeCollection, recursive: bool = False) -> apex.EntityCollection`
Retrieves Apex objects as an EntityCollection, based on their associated UserAttributes..

- `entity` — A valid Apex entity.
- `userAttributeNames` — An optional list of names. If supplied, only objects that have associated UserAttributes with names that match one of the entries in this List will be returned..
- `userAttributeValues` — optional Collection of User attribute values. If supplied, only objects that have associated UserAttributes with values that match one of the entries in this List will be returned.
- `recursive` — An optional boolean argument (False by default) If False or omitted (False by default) the method will return only the names of UserAttributes associated with the entity. If True, the method will return the names of UserAttributes associated with the entity AND all of its children, childrens children etc. in a recursive manner..

Returns: collection of entities

Retrieves Apex objects as an EntityCollection, based on their associated UserAttributes. The method requires a valid existing entity and supports an optional 'recursive' argument. If 'recursive' is False or omitted (False by default) then the scope of objects that may be returned is limited to the single entity. If 'recursive' is True, the scope of objects that may be returned includes the entity plus all of its children, childrens children etc. in a recursive manner. If either of the optional 'names' ( a List of UserAttribute names) or 'values" arguments are supplied, the method will return only those objects that have associated UserAttributes whose names and values match those that are provided The optional 'names' argument defines a list of UserAttribute names. If omitted, the method will return all Apex objects in the scope of the method that have ANY associated UserAttributes. If supplied, the method will return all Apex objects in the scope of the method that have ANY associated UserAttribute that has a name that is present in the 'names' List. Note : If the optional 'values' argument is also provided, the method will return only those objects that have matching names AND matching values The optional 'values' argument defines a list of UserAttribute values. If omitted, the method will return all Apex objects in the scope of the method that have ANY associated UserAttributes. If supplied, the method will return all Apex objects in the scope of the method that have ANY associated UserAttribute that has a value that is present in the 'values' List. Note : If the optional 'names' argument is also provided, the method will return only those objects that have matching values AND matching names

### `apex.getCoordinateSystem(name: str) -> apex.construct.CoordinateSystem`
Get a CoordinateSystem in a Model.

- `name` — of the CoordinateSystem to get.

Returns: the CoordinateSystem object

### `apex.getCoordinateSystemById(id: int) -> apex.construct.CoordinateSystem`
Get a CoordinateSystem in a Model.

- `id` — of the CoordinateSystem to get.

Returns: the CoordinateSystem object

### `apex.getCoordinateSystems(target: [{str:str}]) -> apex.construct.CoordinateSystemCollection`
Get CoordinateSystem objects in a Model.

- `target` — of dictionaries (string:string) specifying the coordinate systems to retrieve. Valid keys are 'path' and 'name'.

Returns: the collection of coordinate system objects

### `apex.getCurrentProjectFolderName() -> str`
Returns the name of the folder that contains the current Apex project.

Current releases of Apex persist the model data into multiple files and folders.All of these files are contained within a single folder.This method returns the name of that folder.Users are advised not to manually or programmatically add, modify or delete files or folders within the Apex project folder - only UI functions with Apex should be used to modify this folder or its contents.Example: A user creates a folder on their machine called "C:\Users\john doe\Documents\Projects"This folder contains three Apex "databases" - "Wing", "Fuselage", "Empennage".Each Apex database is represented by a "project folder" giving rise to the following folder structure "C:\Users\john doe\Documents\Projects\Wing" "C:\Users\john doe\Documents\Projects\Fuselage" "C:\Users\john doe\Documents\Projects\Empennage" Using the getCurrentProjectFolderName() method in an Apex session that has the "Fuselage" project open will return "Fuselage".(Note that the related getCurrentProjectFolderPath() method in an Apex session that has the "Fuselage" project open will return "C:\Users\john doe\Documents\Projects".)

### `apex.getCurrentProjectFolderPath() -> str`
Returns the fully qualified path to the folder that contains the current Apex project.

Current releases of Apex persist the model data into multiple files and folders.All of these files are contained within a single folder.This method returns the name of that folder.Users are advised not to manually or programmatically add, modify or delete files or folders within the Apex project folder - only UI functions with Apex should be used to modify this folder or its contents.Example: A user creates a folder on their machine called "C:\Users\john doe\Documents\Projects" "C:\Users\john doe\Documents\Projects\Wing" "C:\Users\john doe\Documents\Projects\Fuselage" "C:\Users\john doe\Documents\Projects\Empennage" Using the getCurrentProjectFolderPath() method in an Apex session that has the "Fuselage" project open will return "C:\Users\john doe\Documents\Projects\"(Note that the related getCurrentProjectFolderName() method in an Apex session that has the "Fuselage" project open will return "Fuselage".)

### `apex.getCurve(pathName: str) -> apex.geometry.Curve`
Get a Curve in a Model.

- `pathName` — of the curve to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Curve 1'.

Returns: the Curve

### `apex.getCurveMesh(pathName: str) -> apex.mesh.CurveMesh`
Get a apex.mesh.CurveMesh in a Model.

- `pathName` — of the CurveMesh to get.

Returns: the CurveMesh

### `apex.getDatumPlane(pathName: str) -> apex.construct.DatumPlane`
Get a DatumPlane in the current session using the pathName of DatumPlane.

- `pathName` — of the datum plane to get including the model name as in 'MyModel/Assembly1/Part1/Datum Plane 1'.

Returns: the created DatumPlane

If a DatumPlane with the input pathName does not exist the method will throw an exception.

### `apex.getDesignVariable(pathName: str) -> DesignVariable`
Retrieves a design variable by using the input pathName.

- `pathName` — path name of the design variable.

Returns: the design variable

### `apex.getDesignVariables() -> DesignVariableCollection`
return all design variables in the model.

Returns: a DesignVariableCollection of all design variables in the model.

### `apex.getElements(elementsOfPartVec: [{str:str}] = []) -> apex.mesh.ElementCollection`
Get a apex.mesh.ElementCollection in multi Part.

- `elementsOfPartVec` — vectors of the element in one part.

Returns: the ElementCollection

### `apex.getEntities(pathNames: [str]) -> apex.EntityCollection`
Get a collection of named Entities.

- `pathNames` — list of the entities to get. Must use full names as in 'MyModel/Assembly 1/Assembly 2'.

Returns: Iterable collection of the Entities

### `apex.getFacetedCurve(pathName: str) -> apex.geometry.FacetedCurve`
Get a FacetedCurve in a Model.

- `pathName` — of the faceted curve to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Faceted Curve 1'.

Returns: the FacetedCurve

### `apex.getFacetedSolid(pathName: str) -> apex.geometry.FacetedSolid`
Get a Faceted Solid in a Model.

- `pathName` — of the faceted solid to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Faceted Solid 1'.

Returns: the FacetedSolid

### `apex.getFacetedSurface(pathName: str) -> apex.geometry.FacetedSurface`
Get a Faceted Surface in a Model.

- `pathName` — of the faceted surface to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Faceted Surface 1'.

Returns: the FacetedSurface

### `apex.getGeometryBody(pathName: str) -> apex.geometry.GeometryBody`
Get a GeometryBody in a Model.

- `pathName` — of the body to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Solid 1'.

Returns: the GeometryBody

### `apex.getGroup(pathName: str) -> apex.Group`
Retrieve a Group from the current Model using its pathName.

- `pathName` — pathName of the Group to return. Must use full pathName as in 'MyModel/Group 1".

Returns: the Group

### `apex.getHexMesh(pathName: str) -> apex.mesh.HexMesh`
Get a apex.mesh.HexMesh in a Model.

- `pathName` — of the HexMesh to get.

Returns: the HexMesh

### `apex.getMesh(pathName: str) -> apex.mesh.MeshBody`
Get a apex.mesh.MeshBody in a Model.

- `pathName` — of the MeshBody to get.

Returns: the MeshBody

### `apex.getModelSetNastran(id: int) -> apex.ModelSetNastran`
gets a ModelSetNastran from this Model using the ID provided in the argument The ModelSetNastran is returned as an instance of the actual type of the Set and not as the base class ModelSetNastran type

- `id` — The ID of the ModelSetNastran to retrieve. If a ModelSetNastran with this ID does not exist in this Model the method will raise an exception

### `apex.getNodes(nodesOfPartVec: [{str:str}] = []) -> apex.mesh.NodeCollection`
DEPRECATED:

- `nodesOfPartVec` — vectors of the node in one part.

Returns: the NodeCollection

THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN A FUTURE RELEASE. Please use one of the following methods to recover nodes from the model:apex.mesh.getNodes()/ apex.mesh.MeshBody.getNodes()/ apex.Model.getNodes()Get a apex.mesh.NodeCollection in multi Part.

### `apex.getPart(pathName: str) -> Part`
Get a Part in a Model.

- `pathName` — of the part to get including the model name as in 'MyModel/Assembly1/Part1'.

Returns: the created Part

### `apex.getParts(target: [{str:str}]) -> PartCollection`
Get a collection of Parts, specified by target list of key:value string dictionaries.

- `target` — list of dictionaries (string:string) specifying the parts to retrieve. Valid keys are 'path' and 'name'.

Returns: a PartCollection of the requested Parts

### `apex.getPoint(pathName: str) -> apex.geometry.Point`
Get a Point in a Model.

- `pathName` — of the point to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Point 1'.

Returns: the Point

### `apex.getPointMesh(pathName: str) -> apex.mesh.PointMesh`
Get a apex.mesh.PointMesh in a Model.

- `pathName` — of the PointMesh to get.

Returns: the PointMesh

### `apex.getPrimaryStudy() -> apex.studies.Study`
find the entity in the model

Returns: the found entity.

### `apex.getProfile1D(pathName: str) -> apex.construct.Profile1D`
Returns the Profile1D identified by the pathName argument. If the pathName does not exist the method will throw an exception.

- `pathName` — Name of the Profile1D.

Returns: the Profile1D object

### `apex.getRegion(pathName: str) -> apex.Region`
Retrieve a Region from the current Model using its pathName.

- `pathName` — pathName of the Region to return. Must use full pathName as in 'MyModel/Region 1".

Returns: the Region

### `apex.getScriptUnitSystemLabel() -> str`
returns the 'asciilabel' of the current "Scripting" unit system.

Returns: string 'asciilabel' of the current Apex unit system.

### `apex.getSolid(pathName: str) -> apex.geometry.Solid`
Get a Solid in a Model.

- `pathName` — of the solid to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Solid 1'.

Returns: the Solid

### `apex.getSolidMesh(pathName: str) -> apex.mesh.SolidMesh`
Get a apex.mesh.SolidMesh in a Model.

- `pathName` — of the SolidMesh to get.

Returns: the SolidMesh

### `apex.getSurface(pathName: str) -> apex.geometry.Surface`
Get a Surface in a Model.

- `pathName` — of the surface to get. Must use full name as in 'MyModel/Assembly 1/Part 1/Surface 1'.

Returns: the Surface

### `apex.getSurfaceMesh(pathName: str) -> apex.mesh.SurfaceMesh`
Get a apex.mesh.SurfaceMesh in a Model.

- `pathName` — of the SurfaceMesh to get.

Returns: the SurfaceMesh

### `apex.getUserAttributesNames(entity: apex.Entity, recursive: bool = False) -> [str]`
Get a list of all custom attribute names contained in/under the specified entity.

- `entity` — A valid Apex entity.
- `recursive` — An optional boolean argument (False by default) If False or omitted (False by default) the method will return only the names of UserAttributes associated with the entity If True, the method will return the names of UserAttributes associated with the entity AND all of its children.

Returns: list of user attribute names

Recovers UserAttribute names from the valid Apex entity, which must reference a valid Apex entity otherwise the method will throw an exception. If the optional 'recursive' argument is False or omitted (False by default) the method will return only the names of UserAttributes associated with the entity If the optional 'recursive' argument is True, the method will return the names of UserAttributes associated with the entity AND all of its children, childrens children etc. in a recursive manner.

### `apex.getUserAttributesValues(entity: apex.Entity, userAttributeName: str, recursive: bool = False) -> apex.UserAttributeCollection`
Get a collection of all user attribute associated with a user attribute names contained in/under the specified Apex entity.

- `entity` — A valid Apex entity.
- `userAttributeName` — string name associated with the user attribute.
- `recursive` — boolean flag specifying whether child objects of the entity will be included (default = False).

Returns: collection of user attribute

### `apex.hideUI() -> None`
Causes the application UI to be hidden.

This method (and the related showUI()) is provided primarily to support workflow where Apex is being controlled by a remote application and the remote application needs to hide Apex UI.Care should be excercised when invoking this method from a script that is invoked directly by Apex since - once the UI is hidden there is no way to redisplay it interactively.The mehtod will be silently ignored if the UI is already hidden.

### `apex.iPhysicalCollection(entityList: [Entity] = []) -> IPhysicalCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.ILocationCollection().

- `entityList` — optional list of Entities to add to the collection.

For example:

### `apex.initialize() -> None`

### `apex.isUIShown() -> bool`
Check state of UI.

Boolean property that indicates whether the Apex UI is currently shown (True) or hidden (False)

### `apex.measureAngle(source: Entity, target: Entity) -> float`
Measures angle between 2 entities.

- `source` — first entity.
- `target` — second entity.

### `apex.measureAngle3Locations(startLocation: apex.ILocation, vertexLocation: apex.ILocation, endLocation: apex.ILocation) -> float`
Measures angle with 3 locations.

- `startLocation` — first location of an angle.
- `vertexLocation` — vertex location of an angle.
- `endLocation` — second location of an angle.

### `apex.measureDiameter(target: Entity) -> float`
Measures diameter of an entity.

- `target` — entity.

### `apex.measureDistance(source: apex.ILocation, target: apex.ILocationCollection) -> [float]`
Measures the shortest distance between a single source geometry object and multiple target geometry objects and returns one distance for each object in target as a List of floats. The distances in the List are ordered to reflect the order of entities in target The distances represent units of Length and must be interpreted using the units of Length from the active ScriptUnitSystem.

- `source` — - a single source object that can be of any apex.geometry or apex.Coordinate type that supports the ILocation interface
- `target` — - a collection of objects that can contain any apex,geometry or apex.Coordinate object type that implements the ILocation interface

### `apex.measureDistanceByComponents(source: apex.ILocation, target: apex.ILocationCollection, displayComponents: bool = True, coordinateSystem: apex.construct.CoordinateSystem = None) -> {str:[]}`
Measures the shortest distance between a single source geometry object and multiple target geometry objects and returns one dictionary for all objects in target, the dictionary contains 2 keys: distance and components, "distance" is a list of float, values in the List are ordered to reflect the order of entities in target, "components" is a list of lists (or call it a 2D array of x,y,z triplets), [[dx1,dy1,dz1], [dx2,dy2,dz2],[dx3,dy3,dz3]] The distances represent units of Length and must be interpreted using the units of Length from the active ScriptUnitSystem. For example: A user measures the distances by components for one entity to other two.

- `source` — - a single source object that can be of any apex.geometry or apex.Coordinate type that supports the ILocation interface
- `target` — - a collection of objects that can contain any apex,geometry or apex.Coordinate object type that implements the ILocation interface
- `displayComponents` — - an optional boolean argument (default =True) to display X/Y/Z components or not
- `coordinateSystem` — - it defines the directions of the axes along which the x-component, y-component and z-component dimensions are measured

### `apex.openModel(name: str, path: str) -> Model`
Closes current model and opens the specified model.

- `name` — of the model (folder)
- `path` — to the model folder

Returns: the created Model

### `apex.partCollection(partList: [Part] = []) -> PartCollection`
This function has been deprecated and we intend to remove it in the next Apex release. Instead use the standard constuctor apex.PartCollection().

- `partList` — optional list of Parts to add to the collection.

For example:

### `apex.redo() -> None`
if a command exists on redo stack, Redo it.

### `apex.registerTerminateCallback(callback: cb_type) -> None`
register a terminate callback.

- `callback` — to be called after script is run.

### `apex.reparent(target: EntityCollection, parent: Entity) -> None`
Changes the parent of multiple objects (Assembly, Part, geometry::GeometryBody, mesh::MeshBody, construct::DatumPlanes).

- `target` — EntityCollection of (Assembly, Part, geometry::GeometryBody, mesh::MeshBody or construct::DatumPlanes) that will be re-parented.
- `parent` — The Assembly or Part that will become the new parent of the objects in target.

Note that some target entities / parent entity combinations are invalid. For example you may NOT reparent a MeshBody to an Assembly object.

### `apex.scriptRecordPause() -> bool`
Pause recording Macro scripting commands.

Returns: true if script pause is successful

### `apex.scriptRecordResume() -> bool`
Resume recording Macro scripting commands.

Returns: true if script resume is successful

### `apex.scriptRecordStart(filename: str) -> bool`
Begin recording Macro scripting commands into named file.

- `filename` — of the script file to create

Returns: true if script creation is successful

### `apex.scriptRecordStop() -> bool`
Stop recording Macro scripting commands.

Returns: true if script stop is successful

### `apex.scriptRun(filename: str, showOutput: bool = False) -> str`
Executes the named python script, and optionally shows script output in popup dialog.

- `filename` — of the script to execute
- `showOutput` — determines if and output dialog pops open after the run showing output (or error)

Returns: the script output text if script execution is successful

### `apex.setApplicationUnitSystem(unitSystemName: str) -> None`
Sets the current unit system to the spcified one.

- `unitSystemName` — The 'label' or the 'asciilabel' of the Apex unit system in which values entered into or returned by the API are defined. For example, if the unit system is set to 'mm-kg-s-N' and a value of '25.0' is entered for a Length quantity, Apex will interpret the length to be 25.0mm'. The 'values of name' and 'asciiname' for all unit systems included with Apex are shown below label asciilabel m-kg-s-N-K m-kg-s-N-K cm-kg-s-cN-K cm-kg-s-cN-K cm-kg-ms-10⁴N-K cm-kg-ms-dakN-K cm-kg-μs-10¹⁰N-K cm-kg-us-daGN-K mm-kg-ms-kN-K mm-kg-ms-kN-K cm-g-s-dyn-K cm-g-s-dyn-K cm-g-μs-10⁷N-K cm-g-us-daMN-K mm-g-s-μN-K mm-g-s-uN-K mm-g-ms-N-K mm-g-ms-N-K mm-t-s-N-K mm-t-s-N-K in-slinch-s-lbf-℉ in-slinch-s-lbf-degF ft-slug-s-lbf-℉ ft-slug-s-lbf-degF mm-khyl-s-kgf-K mm-khyl-s-kgf-K mm-kg-s-mN-K mm-kg-s-mN-K cm-g-ms-daN-K cm-g-ms-daN-K ft-lb-s-lbf-℉ ft-lb-s-lbf-degF ft-lb-s-lbf-℉-BTU ft-lb-s-lbf-degF-BTU mm-kg-s-N-K mm-kg-s-N-K in-lb-s-lbf-°R-BTU in-lb-s-lbf-degR-BTU m-kg-s-N-K-deg m-kg-s-N-K-deg mm-t-s-N-K-deg mm-t-s-N-K-deg mm-kg-s-mN-K-deg mm-kg-s-mN-K-deg mm-g-s-μN-K-deg mm-g-s-uN-K-deg mm-kg-s-N-K-deg mm-kg-s-N-K-deg in-slinch-s-lbf-℉-deg in-slinch-s-lbf-degF-deg ft-slug-s-lbf-℉-deg ft-slug-s-lbf-degF-deg m-kg-s-N-℃ m-kg-s-N-degC mm-kg-s-N-℃ mm-kg-s-N-degC

### `apex.setScriptUnitSystem(unitSystemName: str) -> None`
Sets the unit system that represents the "default" units that will be used when a Python script is executed. All data contained in the script that does not have specific units defined, will be assumed to be defined in this default systems and Apex will convert them appropriately during execution of the script. The script will use the active application unit system when not set in the sciprt.

- `unitSystemName` — The 'label' or the 'asciilabel' of the Apex unit system in which values entered into or returned by the API are defined. For example, if the unit system is set to 'mm-kg-s-N' and a value of '25.0' is entered for a Length quantity, Apex will interpret the length to be 25.0mm'. The 'values of name' and 'asciiname' for all unit systems included with Apex are shown below label asciilabel m-kg-s-N-K m-kg-s-N-K cm-kg-s-cN-K cm-kg-s-cN-K cm-kg-ms-10⁴N-K cm-kg-ms-dakN-K cm-kg-μs-10¹⁰N-K cm-kg-us-daGN-K mm-kg-ms-kN-K mm-kg-ms-kN-K cm-g-s-dyn-K cm-g-s-dyn-K cm-g-μs-10⁷N-K cm-g-us-daMN-K mm-g-s-μN-K mm-g-s-uN-K mm-g-ms-N-K mm-g-ms-N-K mm-t-s-N-K mm-t-s-N-K in-slinch-s-lbf-℉ in-slinch-s-lbf-degF ft-slug-s-lbf-℉ ft-slug-s-lbf-degF mm-khyl-s-kgf-K mm-khyl-s-kgf-K mm-kg-s-mN-K mm-kg-s-mN-K cm-g-ms-daN-K cm-g-ms-daN-K ft-lb-s-lbf-℉ ft-lb-s-lbf-degF ft-lb-s-lbf-℉-BTU ft-lb-s-lbf-degF-BTU mm-kg-s-N-K mm-kg-s-N-K in-lb-s-lbf-°R-BTU in-lb-s-lbf-degR-BTU m-kg-s-N-K-deg m-kg-s-N-K-deg mm-t-s-N-K-deg mm-t-s-N-K-deg mm-kg-s-mN-K-deg mm-kg-s-mN-K-deg mm-g-s-μN-K-deg mm-g-s-uN-K-deg mm-kg-s-N-K-deg mm-kg-s-N-K-deg in-slinch-s-lbf-℉-deg in-slinch-s-lbf-degF-deg ft-slug-s-lbf-℉-deg ft-slug-s-lbf-degF-deg m-kg-s-N-℃ m-kg-s-N-degC mm-kg-s-N-℃ mm-kg-s-N-degC

### `apex.showUI() -> None`
Causes the application UI to be displayed.

This method (and the related hideUI()) is provided primarily to support workflow where Apex is being controlled by a remote application and the remote application needs to show Apex UI - for example if the remote application initially started Apex with the UI hidden.The mehtod will be silently ignored if the UI is already displayed.

### `apex.terminate() -> None`

@ terminate for DEV.

### `apex.transformMirror(target: EntityCollection, planeNormal: [float], planePoint: apex.ILocation, makeCopy: bool) -> EntityCollection`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems.

- `target` — The collection of Entities to be mirrored.
- `planeNormal` — A vector defining the normal of the mirror plane. This argument is not required if the mirrorPlane argument is provided
- `planePoint` — Any point on the mirror plane. This argument is not required if the mirrorPlane argument is provided
- `makeCopy` — An optional boolean argument (default = False) that determines whether the transform operation will "move" the input objects or "copy" them.

Transforms target Entities by reflecting about a supplied mirror plane. An option is provided to control whether the target Entities are Moved (Default) or Copied. When the "Move" option is active the method returns all input target Entities that were successfully transformed. When the "Copy" option is active the method returns all of the new Entities that were successfully created.

### `apex.transformRotate(target: EntityCollection, axisDirection: [float], axisPoint: apex.ILocation, angle: float, makeCopy: bool) -> EntityCollection`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. Rotate a target entity.

- `target` — The collection of Entities to be translated.
- `axisDirection` — The direction of rotation axis.
- `axisPoint` — a point on the rotation axis. The location of the point represnts a Length quantity and must be defined using the units of Length from the active script unit system.
- `angle` — The angle of rotation about the rotation axis. angle represents an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `makeCopy` — optional argument, default = False, that defines whether the target will be moved (False) or copied (True) by this method.

### `apex.transformTranslate(target: EntityCollection, direction: [float], distance: float, makeCopy: bool) -> EntityCollection`
Translate a target entity.

- `target` — The collection of Entities to be translated.
- `direction` — The direction of translation.
- `distance` — The distance of translation.
- `makeCopy` — Determine if this call is for move or copy.

### `apex.undo() -> None`
if a command exists on undo stack, Undo it.

### `apex.userAttributeCollection(userAttributeList: [apex.UserAttribute] = []) -> apex.UserAttributeCollection`
return a UserAttributeCollection, optionally initialized from a list of UserAttributes.

- `userAttributeList` — optional list of UserAttributes to add to the collection.

## Classes in this module

Full method signatures are in `api/classes/apex.md`.

`Assembly`, `AssemblyCollection`, `AssemblyRep`, `AssemblyRepCollection`, `AxisAlignedBoundingBox`, `ColorRGB`, `Coordinate`, `DataTable2Col`, `DataTable3Col`, `DesignVariable`, `DesignVariableCollection`, `Entity`, `EntityCollection`, `Group`, `GroupCollection`, `IActivatable`, `IDisplayable`, `IIdentifier`, `ILocation`, `ILocationCollection`, `IName`, `IOrientation`, `IOrientationCollection`, `IPath`, `IPhysical`, `IPhysicalCollection`, `IUserAttributes`, `IUserHighlightable`, `LocationInternal`, `Model`, `ModelAssociation`, `ModelAssociationCollection`, `ModelRep`, `ModelSet3Nastran`, `ModelSetNastran`, `Orientation`, `Part`, `PartCollection`, `PartProperty`, `PartPropertyCollection`, `PartPropertyRigid`, `PartRep`, `PartRepCollection`, `Region`, `RegionCollection`, `UserAttribute`, `UserAttributeCollection`

