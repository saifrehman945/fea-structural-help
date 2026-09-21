# Enumeration reference

Every enumeration in the apex package with its exact members.
Never invent an enum member; use one listed here.

## apex

- `apex.AutoManual`: `Automatic`, `Manual`
- `apex.CollectionType`: `Collection`, `EntityCollection`, `AssemblyCollection`, `PartCollection`, `PartRepCollection`, `PartPropertyCollection`, `UserAttributeCollection`, `DesignVariableCollection`, `GeometryFeatureCollection`, `EdgeLoopCollection`, `GeometryTopologyCollection`, `GeometryBodyCollection`, `SolidCollection`, `SurfaceCollection`, `CurveCollection`, `PointCollection`, `FacetedSolidCollection`, `FacetedSurfaceCollection`, `FacetedCurveCollection`, `BoxCollection`, `CylinderCollection`, `SphereCollection`, `EllipsoidCollection`, `CellCollection`, `FaceCollection`, `EdgeCollection`, `VertexCollection`, `MeshControlEdgeCollection`, `SurfaceMeshCollection`, `CurveMeshCollection`, `SolidMeshCollection`, `HexMeshCollection`, `PointMeshCollection`, `MeshBodyCollection`, `NodeCollection`, `ElementCollection`, `ElementFaceCollection`, `ElementEdgeCollection`, `NodeIdSetCollection`, `ElementIdSetCollection`, `EdgeSeedCollection`, `SubMeshCollection`, `MeshIndependentTieCollection`, `MeshDependentTieCollection`, `ConnectorCollection`, `JointCollection`, `SeedPointCollection`, `PointSensorCollection`, `PointMassCollection`, `MaterialCollection`, `MaterialSheetCollection`, `MaterialSheetStackCollection`, `SectionCollection`, `ShellBehaviorCollection`, `PropertiesElement2DCollection`, `PropertiesElement3DCollection`, `BeamShapeCollection`, `BeamSpanCollection`, `NodeTieCollection`, `DiscreteTieCollection`, `RigidLinkCollection`, `Spring1DCollection`, `Damper1DCollection`, `SpringDamper1DCollection`, `FastenerCollection`, `BushingCollection`, `FlexibleLinkCollection`, `Spring1DRepPropertiesCollection`, `Damper1DRepPropertiesCollection`, `SpringDamper1DRepPropertiesCollection`, `BushingRepPropertiesCollection`, `SensorCollection`, `XSectionForceSensorCollection`, `XSectionForceSensorArrayCollection`, `ClearanceSensorCollection`, `InterfacePointCollection`, `AssemblyRepCollection`, `ScenarioCollection`, `StepCollection`, `EventCollection`, `LoadCaseCollection`, `ScenarioNastranCollection`, `SubcaseNastranCollection`, `StepNastranCollection`, `SubstepNastranCollection`, `ILocationCollection`, `IPhysicalCollection`, `Profile1DCollection`, `CoordinateSystemCollection`, `DatumPlaneCollection`, `LoadRepCollection`, `DisplacementConstraintCollection`, `MaterialCoverageRegionCollection`, `Property2DCoverageRegionCollection`, `NonstructuralMassCollection`, `PlyCollection`, `ZoneCollection`, `LayeredPanelCollection`, `CompoundInterfaceCollection`, `ClearanceRegionCollection`, `NonDesignRegionCollection`, `DesignSpaceCollection`, `RegionCollection`, `GroupCollection`, `ModelAssociationCollection`, `ConnectorDiscreteCollection`, `GDConfigurationCollection`, `LoadTemperatureCollection`, `LoadTractionCollection`, `LoadLugCollection`, `LoadPressureCollection`, `AdamsJointCollection`, `AdamsPointCurveCollection`, `AdamsCurveCurveCollection`, `AdamsJointMotionCollection`, `AdamsSingleComponentForceCollection`, `AdamsSingleComponentTorqueCollection`, `AdamsContactCollection`, `AdamsContactPropertyCollection`, `AdamsGeneralForceCollection`, `AdamsVectorForceCollection`, `AdamsVectorTorqueCollection`, `AdamsBushingCollection`, `AdamsTranslationalSpringCollection`, `AdamsDataElementCollection`, `AdamsMatrixCollection`, `AdamsCurveDataCollection`, `AdamsDataSplineCollection`, `DataSeriesCollection`, `DataSeriesOverStepsCollection`, `InteractionCollection`, `Bolt3DCollection`, `PreloadBoltCollection`, `ParametersSetCollection`, `SystemCellsSetCollection`, `FastenerRepPropertiesCollection`, `ContactBodyCollection`, `ThicknessOffsetFieldMidsurfaceCollection`, `DiscreteFEMFieldCollection`, `RigidFaceCollection`, `IOrientationCollection`, `NSMCombinationCollection`, `ContactTableCollection`, `NoType`
- `apex.ConstraintAxis`: `X`, `Y`, `Z`, `RX`, `RY`, `RZ`
- `apex.DesignVariableRangeType`: `Absolute`, `Delta`, `PercentDelta`
- `apex.DesignVariableType`: `Real`, `Integer`, `String`, `Expression`, `Object`
- `apex.DesignVariableUnit`: `NoUnitQuantity`, `Length`, `Mass`, `Time`, `Force`, `Angle`, `Density`, `Pressure`, `Area`, `Volume`, `Torque`, `Velocity`, `Acceleration`, `Frequency`, `Energy`, `Inertia`, `RotationalVelocity`, `RotationalAcceleration`, `AreaInertia`, `Stiffness`, `Damping`, `TorsionStiffness`, `TorsionDamping`
- `apex.DiscreteValueMethod`: `Generate`, `EnterValues`
- `apex.DiscreteValueRange`: `EqualSpaced`, `MinStdMax`
- `apex.EntityType`: `Extension`, `Project`, `Model`, `Session`, `Catalog`, `CatalogMaterial`, `UserAttribute`, `Setting`, `DesignVariable`, `Instance`, `Assembly`, `Part`, `PartRep`, `PartProperty`, `PartPropertyRigid`, `PartPropertyModal`, `Geometry`, `GeometryBody`, `Solid`, `Surface`, `Curve`, `Point`, `FacetedSolid`, `FacetedSurface`, `FacetedCurve`, `Box`, `Cylinder`, `Sphere`, `Ellipsoid`, `GeometryTopology`, `Cell`, `Face`, `Edge`, `Vertex`, `MeshSeed`, `EdgeSeed`, `FaceSeed`, `GeometryFeature`, `Hole2D`, `Fillet2D`, `Chamfer2D`, `Hole3D`, `Fillet3D`, `Chamfer3D`, `EdgeLoop`, `MeshControlEdge`, `MeshBody`, `SolidMesh`, `SurfaceMesh`, `CurveMesh`, `HexMesh`, `PointMesh`, `SubMesh`, `SubMesh0D`, `SubMesh1D`, `SubMesh2D`, `SubMesh3D`, `Node`, `Element`, `ElementFace`, `ElementEdge`, `Penta`, `Tet`, `Hex`, `Quad`, `Tri`, `Bar`, `SeedPoint`, `Set`, `NodeIdSet`, `ElementIdSet`, `Construct`, `Sketch`, `Plane`, `DatumPlane`, `MirrorPlane`, `SketchPrimitive`, `Arc`, `Chamfer`, `Circle`, `Ellipse`, `Fillet`, `Polyline`, `Rectangle`, `SketchPoint`, `Spline`, `SketchEdge`, `SketchVertex`, `Profile1D`, `CoordinateSystem`, `Coordinate`, `Display`, `Tessellation0D`, `Tessellation1D`, `Tessellation2D`, `Attribution`, `Property`, `Material`, `MaterialCoverageRegion`, `MaterialSheet`, `MaterialSheetStack`, `ShellSection`, `ShellBehavior`, `PropertiesElement2D`, `SimpleShell`, `Shell`, `ShearPanel`, `Property2DCoverageRegion`, `PropertiesElement3D`, `PropertiesElement3DHomogeneous`, `BeamSpan`, `BeamShape`, `BeamShapeSolidRound`, `BeamShapeSolidRectangle`, `BeamShapeSolidHexagon`, `BeamShapeHollowRound`, `BeamShapeHollowRoundByThickness`, `BeamShapeHollowRectangularSymmetric`, `BeamShapeHollowRectangularAsymmetric`, `BeamShapeHollowDoubleRectangular`, `BeamShapeHat`, `BeamShapeHatClosed`, `BeamShapeCruciform`, `BeamShapeISymmetric`, `BeamShapeIAsymmetric`, `BeamShapeH`, `BeamShapeL`, `BeamShapeC`, `BeamShapeCAlternate`, `BeamShapeU`, `BeamShapeT`, `BeamShapeTSideways`, `BeamShapeTInverted`, `BeamShapeZ`, `BeamShapeNumeric`, `BeamShape1DProfile`, `BeamShapeType`, `DiscreteTie`, `NodeTie`, `PointMass`, `NonstructuralMass`, `Ply`, `Zone`, `LayeredPanel`, `Region`, `Group`, `StressStrainCurve`, `MaterialModel`, `ConstitutiveModel`, `Properties2DModel`, `Properties3DModel`, `Elasticity`, `ElasticityLinearIso`, `ElasticityLinear2DOrtho`, `ElasticityLinear2DAniso`, `ElasticityLinear3DAniso`, `ElasticityLinear3DOrtho`, `ElasticityLinear3DTransvIso`, `ViscoElasticity`, `ViscoElasticity3DAniso`, `ViscoElasticity2DAniso`, `Mass`, `ThermalExpansion`, `ThermalExpansionLinearIsotropic`, `ThermalExpansionLinear2DOrthotropic`, `ThermalExpansionLinear2DAnisotropic`, `ThermalExpansionLinear3DOrthotropic`, `ThermalExpansionLinear3DTransvIso`, `ThermalExpansionLinear3DAnisotropic`, `Failure`, `FailureIso`, `Failure2DOrth`, `Failure2DAniso`, `Failure3DOrth`, `Failure3DTransvIso`, `Plasticity`, `PlasticityStressStrain`, `PerfectlyPlastic`, `PlasticityHardeningSlope`, `Constraint`, `DisplacementConstraint`, `ConstraintDisplacementConstant`, `ConstraintSinglePointConstant`, `ConstraintExcludeAuto`, `ConstraintExcludeAuto1`, `Support1`, `Support`, `SupportFreeBody`, `SupportFreeBody1`, `ConstraintSinglePointVariable`, `ConstraintCombination`, `ConstraintDisplacementVariable`, `ConstraintExcludeAutoVariable`, `ConstraintExcludeAuto1Variable`, `SupportFreeBodyVariable`, `SupportFreeBody1Variable`, `ConstraintDisplacement`, `InitialCondition`, `InitialTemperature`, `InitialDisplacementVelocityConstant`, `InitialStrainConstant`, `InitialStressConstant`, `InitialTemperatureGradient2D`, `InitialTemperatureGradient2DHeat`, `InitialTemperatureDefault`, `InitialTemperatureGradientBeam2`, `InitialTemperatureGradientBeam3`, `InitialTemperatureNodalConstant`, `InitialTemperatureNodalVariable`, `InitialTemperatureGradient2DHeatVariable`, `InitialTemperatureGradient2DVariable`, `InitialTemperatureGradientBeam3Variable`, `InitialTemperatureGradientBeam2Variable`, `InitialStrainVariable`, `InitialStressVariable`, `InitialDisplacementVelocityVariable`, `InitialStress`, `InitialStrain`, `InitialDisplacementVelocity`, `InitialTemperatureNodal`, `Load`, `GravityLoad`, `ForceMoment`, `ForceMomentRep`, `EnforcedMotion`, `EnforcedMotionRep`, `LoadTemperature`, `LoadTemperaturePropertyStaticConstant`, `LoadTemperaturePropertyStaticVariable`, `LoadTraction`, `LoadTractionPropertyStaticConstant`, `LoadTractionPropertyStaticTotal`, `LoadLug`, `LoadLugPropertyStatic`, `LoadPressurePropertyStaticConstant`, `LoadPressurePropertyStaticVariable`, `LoadPressure`, `PreloadBolt`, `PreloadBoltRep`, `PreloadBoltProperty`, `PreloadBoltPropertyStatic`, `LoadForceComponent`, `LoadForceFollowerVector`, `LoadForceFollowerNormal`, `LoadMomentComponent`, `LoadMomentFollowerVector`, `LoadMomentFollowerNormal`, `LoadAreaFactor`, `LoadPressureArea`, `LoadPressure2D`, `Pressure`, `LoadDistributedBeam2`, `LoadDistributedBeam3`, `LoadEnforcedMotionTotal`, `LoadEnforcedMotionRelative`, `LoadTemperatureNodal`, `LoadTemperatureGradientBeam3`, `LoadTemperatureDefault`, `TemperatureHeatTransfer`, `LoadTemperatureGradient2DHeat`, `TemperatureSurface`, `LoadTemperatureGradient2D`, `LoadTemperatureGradientBeam2`, `LoadDeformationAxial`, `LoadAccelerationSpatial`, `LoadAccelerationNodal`, `LoadForceRotational`, `LoadDynamicAcoustic`, `LoadDynamicFrequency1`, `LoadDynamicFrequency2`, `LoadDynamicTimeTabular`, `LoadDynamicTimeAnalytical`, `LoadCombinationStatic`, `LoadCombinationDynamic`, `LoadForceComponentVariable`, `LoadForceFollowerVectorVariable`, `LoadForceFollowerNormalVariable`, `LoadMomentComponentVariable`, `LoadMomentFollowerVectorVariable`, `LoadMomentFollowerNormalVariable`, `LoadTimeDelay`, `LoadPhaseLead`, `LoadTemperatureNodalVariable`, `LoadTemperatureGradient2DVariable`, `LoadPressure2DVariable`, `LoadTemperatureGradientBeam3Variable`, `LoadTemperatureGradientBeam2Variable`, `LoadDistributed`, `LoadTemperatureGradient2DHeatVariable`, `LoadAccelerationNodalVariable`, `LoadDeformationAxialVariable`, `LoadDistributedBeam2Variable`, `LoadAreaFactorVariable`, `LoadPressureAreaVariable`, `LoadDistributedBeam3Variable`, `LoadEnforcedMotionTotalVariable`, `LoadEnforcedMotionRelativeVariable`, `LoadDistributedVariable`, `PressureVariable`, `LoadPhaseLeadVariable`, `LoadTimeDelayVariable`, `LoadTotal`, `Interaction`, `Joint`, `Connector`, `MeshIndependentTie`, `MeshDependentTie`, `InteractionRep`, `InteractionPropertyGeometric`, `InteractionPropertyPhysical`, `RigidFace`, `ContactBodyProperty`, `ContactBody`, `RigidLink`, `Spring1D`, `Damper1D`, `SpringDamper1D`, `Bushing`, `FlexibleLink`, `Gap`, `Fastener`, `Sensor`, `XSectionForceSensor`, `XSectionForceSensorArray`, `ClearanceSensor`, `InterfacePoint`, `Instrumentation`, `PointSensor`, `RemotePoint`, `Study`, `AssemblyRep`, `GenerativeDesignStudy`, `Scenario`, `Step`, `StaticStep`, `StaticStepNastranSol400`, `DynamicsStep`, `ModalFrequencyStep`, `MultiBodyTransientStep`, `BucklingStep`, `ModesStep`, `MeshlessGenerativeDesignStep`, `GenerativeDesignStaticStep`, `Event`, `LoadCase`, `ScenarioSetNastran`, `ScenarioSetTime`, `ScenarioSetFrequency`, `ScenarioSetRandId`, `ScenarioSetFrfcompId`, `ScenarioSetModeId`, `ScenarioSetGridComponent`, `ScenarioSetGridId`, `LoadCaseItem`, `ScenarioNastran`, `SubcaseNastran`, `StepNastran`, `SubstepNastran`, `SimulationSettingsGenerativeDesign`, `StatePlot`, `DeformVisualization`, `ContourVisualization`, `VectorVisualization`, `ResultProbe0D`, `ColorMap`, `Machining`, `ClearanceRegion`, `GenDes`, `CompoundInterface`, `NonDesignRegion`, `DesignSpace`, `GDConfiguration`, `ChartPlot`, `SBMTChart`, `ChartPlotXY`, `DataTable`, `MatrixMN`, `DataSeries`, `DataSeriesVMTBeamSpan`, `DataSeriesVMTSensorArray`, `DataSeriesOverSteps`, `DataSeriesTransient`, `ModelAssociation`, `XSectionForceSensorPlot`, `Block`, `Bolt`, `Bolt3D`, `ConnectorDiscrete`, `DiscreteFEMField`, `ThicknessOffsetField`, `ThicknessOffsetFieldConstant`, `ThicknessOffsetFieldMidsurface`, `MaterialOrientationField2D`, `MaterialOrientationField2DAlignCurve`, `MaterialOrientationField2DCoordinate`, `NSMCombination`, `ContactTable`, `ParametersSet`, `SystemCellsSet`, `ConstraintSinglePoint`, `Table`, `TABLED1`, `TABLED2`, `TABLED3`, `TABLED4`, `ITER`, `EIGB`, `EIGR`, `RCROSS`, `DAMPING`, `HYBDAMP`, `RANDPS`, `RANDT1`, `TSTEP`, `TABDMP1`, `TABRND1`, `EIGRL`, `NLSTEP`, `NoType`, `ModelSetNastran`, `ModelSet3Nastran`
- `apex.ExportProperty`: `AsDefined`, `Inline`, `External`
- `apex.GeometryExportOrganization`: `Multiple`, `Single`
- `apex.ModelAssociationScope`: `All`, `Visible`, `Selected`
- `apex.ModelResultsImportOptions`: `Model`, `Results`, `Both`
- `apex.PartRepPropertyType`: `FE`, `Rigid`, `Flex`, `Volume`, `UnKnown`
- `apex.TransformMethod`: `TranslateRotate`, `Mirror`
- `apex.TransformOption`: `Move`, `Copy`
- `apex.UserAttributeType`: `Int`, `Str`, `Float`, `Bool`
- `apex.VirtualFaceExportMethod`: `NurbsOnly`, `NurbsAndFaceted`

## apex.attribute

- `apex.attribute.AlignmentType`: `Offset`, `Mid`, `Top`, `FollowPanel`
- `apex.attribute.ApplicationMethod`: `Direct`, `Remote`, `Free`, `Undefined`
- `apex.attribute.Approach`: `FullyDynamic`, `TransferFunction`
- `apex.attribute.AxisLocationMode`: `Undefined`, `Manual`, `Auto`
- `apex.attribute.BeamBehaviorType`: `Beam`, `Bar`, `Rod`
- `apex.attribute.BeamSpanOrientationType`: `Angle`, `Vector`
- `apex.attribute.BeamSpanType`: `Freestanding`, `Stiffener`
- `apex.attribute.ComponentDirectionAcceleration`: `X`, `Y`, `Z`
- `apex.attribute.ConnectorType`: `Spring1D`, `Damper1D`, `SpringDamper1D`, `Bushing`, `RigidLink`, `FlexibleLink`, `Gap`, `Fastener`, `Undefined`
- `apex.attribute.ConstitutiveModelType`: `Elasticity`, `ViscoElasticity`, `Mass`, `ThermalExpansion`, `Failure`, `Plasticity`
- `apex.attribute.ConstraintType`: `Clamped`, `General`, `Axial`, `Symmetry`, `Spherical`
- `apex.attribute.ContactBodyDimension`: `Dimension3D`, `Dimension2D`
- `apex.attribute.ContactBodyForm`: `BCBODY1`, `BCSURF`, `BCGRID`, `Undefined`
- `apex.attribute.ContactBodyType`: `Deform`, `Rigid`, `SymmetryRigid`, `HeatRigid`
- `apex.attribute.ContactResultCalculation`: `Origin`, `EstimatedCentroid`
- `apex.attribute.ContactSearchOrder`: `DoubleSide`, `SingleSide`, `Automatic`
- `apex.attribute.ContactSurfaceForm`: `FACE`, `GRID`, `RIGID`, `Undefined`
- `apex.attribute.ControlNodeDefinitionMethod`: `Bottom`, `Mid`, `OffsetFromBottom`, `OffsetFromTop`, `Top`, `User`
- `apex.attribute.CoordinateSystemDefinition`: `SuperElement`, `Residual`
- `apex.attribute.CrossSectionMethod`: `Automatic`, `Manual`
- `apex.attribute.DOFDefinitionMode`: `All`, `Individual`
- `apex.attribute.DiscontinuityDefinition`: `Auto`, `Manual`
- `apex.attribute.DiscreteFEMFieldType`: `DiscreteThicknessField`, `DiscreteOffsetField`, `DiscreteAngleField`, `DiscreteCoordinateSystemField`
- `apex.attribute.DiscreteRegionType`: `Node`, `Element`, `ElementFace`, `ElementNode`, `FaceNode`
- `apex.attribute.Distribution`: `Cosine`
- `apex.attribute.DistributionMode`: `Auto`, `Custom`
- `apex.attribute.DistributionOrientation`: `Normal`, `Parallel`
- `apex.attribute.DistributionType`: `Rigid`, `Compliant`
- `apex.attribute.DynamicLoadType`: `AppliedLoad`, `Displacement`, `Velocity`, `Acceleration`
- `apex.attribute.EnforcedMotionType`: `Displacement`, `Velocity`, `Acceleration`
- `apex.attribute.ExportRenumberMethod`: `Internal`, `Export`
- `apex.attribute.ExtendedKeyword`: `Undefined`, `TABLES1`, `TABLEST`, `TABLEM1`, `TABLED1`
- `apex.attribute.FailureCriteriaComposite`: `Undefined`, `HILL`, `HOFF`, `TSAI`, `FollowPanel`
- `apex.attribute.FastenerStiffnessCoordinateSystem`: `Global`, `UserDefined`, `MinusOne`, `Unset`
- `apex.attribute.FlagOfCoordinateSystem`: `Relative`, `Absolute`, `Auto`
- `apex.attribute.HardeningRule`: `Isotropic`, `Kinematic`, `Both`
- `apex.attribute.IdConflictResolutionMethod`: `Undefined`, `AutomaticOffset`, `AllowDuplicates`
- `apex.attribute.ImportRenumberMethod`: `Internal`, `Import`
- `apex.attribute.InputForm`: `Component`, `Resultant`
- `apex.attribute.InputType`: `ElementUniform`, `ElementVariable`
- `apex.attribute.IntegrationNetwork`: `Automatic`, `Bubble`, `Three`, `Two`
- `apex.attribute.IntegrationScheme`: `Automatic`, `Reduced`, `Full`
- `apex.attribute.InteractionType`: `Glue`, `GeneralContact`, `SelfContact`
- `apex.attribute.InterferenceFitMethod`: `NormalDirection`, `UserDirection`, `ScaleFactor`, `Automatic`
- `apex.attribute.JointAxis`: `XAxis`, `YAxis`, `ZAxis`
- `apex.attribute.JointRenderType`: `Undefined`, `RBE2`, `RJOINT`
- `apex.attribute.JointType`: `Revolute`, `Cylindrical`, `Spherical`, `Prismatic`, `Planar`, `Undefined`
- `apex.attribute.KeywordMaterialPrimary`: `Undefined`, `MAT1`, `MAT2`, `MAT8`, `MAT9`, `MATORT`
- `apex.attribute.KeywordMaterialSecondary`: `Undefined`, `MATEP`, `MATPE1`, `MATS1`, `MATSMA`, `MATT1`, `MAT1F`, `MATT2`, `MAT2F`, `MATT9`, `MAT9F`, `MATG`, `MATTG`, `MATHE`, `MATHP`
- `apex.attribute.LineLoadDirection`: `Normal`, `Tangent`, `X`, `Y`, `Z`
- `apex.attribute.LoadMethodRotational`: `Centrifugal`, `RotationInertia`
- `apex.attribute.LoadTypeDistributedBeam2`: `ForceX`, `ForceY`, `ForceZ`, `ForceXE`, `ForceYE`, `ForceZE`, `MomentX`, `MomentY`, `MomentZ`, `MomentXE`, `MomentYE`, `MomentZE`
- `apex.attribute.LoadTypeDistributedBeam3`: `Force`, `Moment`, `Bimoment`
- `apex.attribute.MarcInputType`: `Dat`, `Mfd`, `Mud`
- `apex.attribute.MassDistribution`: `TotalMass`, `MassPerArea`, `MassPerLength`
- `apex.attribute.MaterialAlignmentMethod`: `Curve`, `CoordinateSystemAxis`, `EulerAngles`
- `apex.attribute.MaterialModelType`: `Unknown`, `ConstitutiveModel`, `MaterialModel`
- `apex.attribute.MaterialType`: `Isotropic`, `Orthotropic`, `Anisotropic3D`, `Orthotropic3D`, `TransversalIsotropic3D`, `Anisotropic`
- `apex.attribute.MaterialTypeDomain`: `Isotropic`, `Dim2`, `Dim3`, `NonDim2`, `NonDim3`
- `apex.attribute.MeshDependentTieRenderStyle`: `AsRBARS`, `UnConnected`
- `apex.attribute.MotionControlType`: `Velocity`, `Position`, `Load`
- `apex.attribute.NastranResultOutputType`: `Hdf5`, `Op2`, `Xdb`, `Master`, `Dball`
- `apex.attribute.NonstructuralMassType`: `Constant`, `Variable`
- `apex.attribute.OrientationType3D`: `Unset`, `Global`, `DefautElement`, `AlternateElement`, `Local`
- `apex.attribute.OrientationTypeDistributedBeam3`: `Basic`, `Local`, `Element`
- `apex.attribute.OutputLocation`: `Unset`, `Grid`, `Gauss`
- `apex.attribute.PlyBehavior`: `Default`, `Membrane`, `Bending`, `Smear`, `FollowPanel`
- `apex.attribute.PlyIdBehavior`: `UseGlobal`, `NoGlobal`, `FollowPanel`
- `apex.attribute.PropertiesElement2DType`: `SimpleShell`, `Shell`, `ShearPanel`
- `apex.attribute.PropertiesElement3DType`: `Homogeneous`
- `apex.attribute.Property2DAlignmentMethod`: `Curve`, `CoordinateSystem`
- `apex.attribute.RigidFaceType`: `BCNURBS`, `BCNURB2`, `BCBZIER`, `BCPATCH`
- `apex.attribute.ScaleTypeDistributedBeam2`: `Length`, `Fractional`, `LengthProjected`, `FractionalProjected`
- `apex.attribute.SelectionExtractionApproach`: `Automatic`, `ForceConstantThickness`, `ForceVariableThickness`
- `apex.attribute.ShapeMatingSide`: `XPositive`, `YPositive`, `XNegative`, `YNegative`
- `apex.attribute.ShellBehaviorType`: `ShearPanel`, `ThinShell`
- `apex.attribute.ShellLayer`: `TopAndButtom`, `TopOnly`, `ButtomOnly`
- `apex.attribute.StackSymmetry`: `Asymmetric`, `Odd`, `Even`
- `apex.attribute.StrainType`: `Type1`, `Type2`
- `apex.attribute.SurfOrLine`: `Surface`, `Line`
- `apex.attribute.TopBottom`: `Top`, `Bottom`
- `apex.attribute.createTypeForFastener`: `ByElement`, `ByProperty`

## apex.catalog

- `apex.catalog.ParametersType`: `CaseControl`, `BulkData`

## apex.chart

- `apex.chart.Interpolation`: `Linear`, `Log`

## apex.compute

- `apex.compute.DeleteScratchFiles`: `Yes`, `No`, `Min`, `Post`
- `apex.compute.MemorymaxMethod`: `Fraction`, `User`
- `apex.compute.NastranMemoryAllocationMethod`: `Estimate`, `Max`, `User`
- `apex.compute.SolverExecutionPreference`: `Auto`, `Manual`
- `apex.compute.SolverType`: `Local`, `Remote`

## apex.construct

- `apex.construct.ArcDirection`: `Clockwise`, `CounterClockwise`
- `apex.construct.ConstructionMarkerType`: `ArcCenter`, `Centroid`, `CylindricalAxisStartPoint`, `CylindricalAxisMidPoint`, `CylindricalAxisEndPoint`, `StartPoint`, `EndPoint`, `MidPoint`, `FaceCenter`
- `apex.construct.CoordinateSystemAxis`: `X_Axis`, `Y_Axis`, `Z_Axis`
- `apex.construct.CoordinateSystemType`: `Cartesian`, `Cylindrical`, `Spherical`
- `apex.construct.GlobalPlane`: `XY`, `YZ`, `ZX`
- `apex.construct.OrientationMethod`: `Euler`, `MultiObject`

## apex.datavis

- `apex.datavis.CoordinateSystemMethod`: `Global`, `Local`, `User`
- `apex.datavis.DiscreteSummedVectorDisplay`: `Summed`, `Discrete`
- `apex.datavis.ForceMomentVectorDisplay`: `Both`, `Force`, `Moment`
- `apex.datavis.VectorComponent`: `Resultant`, `Component1`, `Component2`, `Component3`, `Resultant12`, `Resultant23`, `Resultant13`
- `apex.datavis.VectorDisplayAnchorStyle`: `Tip`, `Tail`
- `apex.datavis.VectorDisplayColorMethod`: `VectorValue`, `Component`
- `apex.datavis.VectorDisplayScalingMethod`: `Scaled`, `Constant`
- `apex.datavis.VectorDisplayStyle`: `ArrowShaded`, `ArrowWireFrame`, `Line`

## apex.display

- `apex.display.CaptureRegionType`: `Viewport`, `ViewCollection`
- `apex.display.GraphicsFontStyle`: `Normal`, `Bold`, `Italic`, `BoldItalic`
- `apex.display.GraphicsFontUnderlineStyle`: `NoUnderline`, `Single`, `Double`, `SingleBold`, `Dotted`, `Dashed`
- `apex.display.ImageType`: `jpg`, `png`, `bmp`, `tiff`, `gif`
- `apex.display.VideoType`: `gif`, `mp4`, `avi`

## apex.environment

- `apex.environment.BoltPreloadType`: `Force`, `Overclosure`

## apex.gendes

- `apex.gendes.BoundingBoxOffsetType`: `Fixed`, `Proportional`
- `apex.gendes.BoundingBoxType`: `ObjectAligned`, `Global`
- `apex.gendes.TargetSolidBehavior`: `KeepCurrent`, `Reparent`, `Copy`

## apex.geometry

- `apex.geometry.CADFormat`: `ParasolidText`, `ParasolidBinary`, `STLText`, `STLBinary`, `ACISText`, `IGES_5_3`, `STP_AP214`
- `apex.geometry.CleanupOperation`: `CleanUp`, `RemoveSmallFeatures`, `FindSmallFeatures`, `RemoveSurfaceFeatures`, `FindSurfaceFeatures`
- `apex.geometry.CurveBehavior`: `Spline`, `Polyline`, `Circle`, `Arc`
- `apex.geometry.DefeatureOperation`: `Unknown`, `Automatic`, `RemoveSelected`, `EditOrDeleteFaces`, `FeatureIdentify`, `SelectedDefeature`
- `apex.geometry.DragEdgeBehavior`: `Follow`, `Extrude`, `Stretch`
- `apex.geometry.DragVertexBehavior`: `ForceStraight`, `KeepCurved`
- `apex.geometry.GeometryFaultType`: `Sliver`, `SmallEdge`, `SmallFace`, `Overhang`, `Gap`, `Crack`, `Spike`
- `apex.geometry.GeometryFeatureType`: `Hole2D`, `Fillet2D`, `Chamfer2D`, `Hole3D`, `Fillet3D`, `Chamfer3D`
- `apex.geometry.GeometrySplitBehavior`: `Split`, `Partition`
- `apex.geometry.GeometrySplitLineType`: `Spline`, `Polyline`
- `apex.geometry.LoftClampingMethod`: `No`, `Tangent`, `Curvature`
- `apex.geometry.MidSurfaceIncrementalMethod`: `Tapered`, `Left`, `Right`, `Planar`
- `apex.geometry.OffsetBehavior`: `Sharp`, `Rounded`
- `apex.geometry.PushPullBehavior`: `FollowShape`, `Extrude`, `Stretch`
- `apex.geometry.PushPullMethod`: `Normal`, `Fillet`, `Chamfer`
- `apex.geometry.STLImportBodyType`: `Mesh`, `Faceted`
- `apex.geometry.SnapModeType`: `OnEdge`, `Extension`, `OnSurface`, `SnapNone`, `MidPoint`, `Vertex`, `Tangent`, `Perpendicular`
- `apex.geometry.SweepProfileAlignmentMethod`: `Normal`, `Parallel`, `Arclength`
- `apex.geometry.SweepProfileClampingMethod`: `No`, `Smooth`, `Sharp`

## apex.instrument

- `apex.instrument.SensorLocationMethod`: `AtCentroid`, `OnPath`

## apex.license

- `apex.license.CheckoutStatus`: `NOT_LICENSED`, `AVAILABLE`, `CHECKED_OUT`, `FAILED_CHECKOUT`

## apex.mesh

- `apex.mesh.BiasType`: `EndBias`, `MiddleBias`
- `apex.mesh.ConflictResolveOption`: `AllowDuplicateIds`, `AutomaticResolve`
- `apex.mesh.CurvatureType`: `EdgeOnly`, `EdgeAndFace`
- `apex.mesh.ElementOrder`: `Linear`, `Quadratic`
- `apex.mesh.ElementTopology`: `Bar2`, `Bar3`, `Tria3`, `Tria6`, `Quad4`, `Quad8`, `Quad5`, `Quad9`, `Tetra4`, `Tetra10`, `Penta6`, `Penta15`, `Hexa8`, `Hexa20`, `Pyramid5`, `Pyramid13`
- `apex.mesh.FEModelFormat`: `NastranBulk`
- `apex.mesh.FEModelImportOrganizationOptions`: `ByMaterial`, `ByProperty`, `ByContiguousMesh`, `ByElementType`, `SinglePart`
- `apex.mesh.FEModelType`: `Nastran`
- `apex.mesh.FeatureMeshType`: `Fillet`, `Chamfer`, `Cylinder`, `CylinderPartial`, `Washer`, `FourSidedFace`, `ArbirtaryHole`
- `apex.mesh.HexMeshMethod`: `Auto`, `Loft`, `Sweep`
- `apex.mesh.HybridCoreType`: `Tet`, `HexPrismatic`
- `apex.mesh.HybridSkinType`: `QuadDominant`, `Tria`
- `apex.mesh.IDConflictResolveMethod`: `AllowDuplicates`, `ResolveAuto`
- `apex.mesh.MeshFlow`: `Grid`, `FollowEdges`
- `apex.mesh.MeshTopology`: `PointMeshTopology`, `CurveMeshTopology`, `SurfaceMeshTopology`, `SolidMeshTopology`, `HexMeshTopology`
- `apex.mesh.MeshZone`: `Exterior`, `Interior`
- `apex.mesh.OrphanBodySetting`: `WithinAndBetween`, `Between`, `Within`, `BetweenParts`
- `apex.mesh.RetainId`: `LowerId`, `HigherId`
- `apex.mesh.SolidMeshElementShape`: `Tetra`, `Pyramid`
- `apex.mesh.SplitPattern`: `Cross`
- `apex.mesh.SurfaceMeshElementShape`: `Mixed`, `Quadrilateral`, `Triangle`
- `apex.mesh.SurfaceMeshMethod`: `Auto`, `Pave`, `Mapped`

## apex.post

- `apex.post.ColorMapSegmentMethod`: `Linear`, `Manual`
- `apex.post.CompositeFailure`: `FailureIndex`, `StrengthRatio`
- `apex.post.ContourStyle`: `Fringe`, `Fill`
- `apex.post.CoordinateSystemMethod`: `Global`, `Local`, `Material`, `Ply`, `User`
- `apex.post.DeformScalingMethod`: `Absolute`, `Relative`
- `apex.post.ElementNodalProcessing`: `Averaged`, `NonAveraged`, `Difference`, `SmartAveraged`
- `apex.post.LayerEnvelopingMethod`: `Max`, `Min`, `Average`, `Unknown`
- `apex.post.LayerIdentificationMethod`: `Position`, `Ply`
- `apex.post.ProbeTargetUpdateMode`: `Add`, `Remove`
- `apex.post.ResultDerivation`: `VonMises`, `ShearMax`, `Comp1`, `Comp2`, `Comp3`, `Shear12`, `Shear23`, `Shear13`, `PrincipalMax`, `PrincipalMid`, `PrincipalMin`, `Invariant1`, `Tresca`, `Octahedral`, `Hydrostatic`, `StrainEnergy`, `StrainEnergyDensitiy`, `StrainEnergyPercentTotal`, `Vector`, `Magnitude`, `Component1`, `Component2`, `Component3`, `Resultant12`, `Resultant23`, `Resultant13`, `MomentBendingAxial`, `MomentBendingAxialMax`, `MomentBendingAxialMin`, `F1`, `F2`, `F12`, `M1`, `M2`, `M12`, `ForceAxial`, `ForceShearPlane1_V1`, `ForceShearPlane2_V2`, `TorqueTotal`, `TorqueWarping`, `MomentBendingPlane1_M1`, `MomentBendingPlane2_M2`, `Hill`, `Hoffman`, `TsaiWu`, `FailureStrain1Max`, `FailureStrain2Max`, `FailureStrain12Max`, `FailuresStressShearTrans13Max`, `FailuresStressShearTrans23Max`, `StressShearTransverse13`, `StressShearTransverse23`, `Other`, `MassFractionEffectiveTotal`, `MassMatrixEffective`, `MassMatrixRigidBody`, `MassFractionEffectiveTranslational`, `MassFractionEffectiveRotational`, `Transform16`, `CrossPlotResultant`, `CrossPlotX`, `CrossPlotY`, `CrossPlotZ`, `NormalContactStress`, `FrictionContactStress1`, `FrictionContactStress2`, `AxialStress`, `CombinedAxialBendingStress`, `TorsionalStress`, `ShearStressY`, `ShearStressZ`, `AxialStrain`, `CombinedAxialBendingStrain`, `TorsionalStrain`, `ShearStrainY`, `ShearStrainZ`, `CompMax`, `CompMin`, `Invariant2`, `Invariant3`, `Prin2DMajorCompX`, `Prin2DMajorCompY`, `Prin2DMinorCompX`, `Prin2DMinorCompY`, `PrinInterCompX`, `PrinInterCompY`, `PrinInterCompZ`, `PrinMajorCompX`, `PrinMajorCompY`, `PrinMajorCompZ`, `PrinMinorCompX`, `PrinMinorCompY`, `PrinMinorCompZ`, `ContactGridCheckMag`, `ContactFrictionForceMag`, `ContactFrictionStress1`, `ContactFrictionStress2`, `ContactNormalForceMag`, `ContactNormalStress`, `GridCheckReserve1`, `GridCheckReserve2`, `EffCreepStrain`, `EffCreepStress`, `EffPlasticStrain`, `EffPlasticStress`, `EquivalentStress`, `GasketClosure`, `GasketPressure`, `PlasticGasketClosure`, `Tensor1D`, `Tensor2D`, `TransverseShearStrainXZ`, `TransverseShearStrainYZ`, `ContactStatus`, `Undefined`
- `apex.post.ResultFileType`: `AdamsCar`
- `apex.post.ResultQuantity`: `Stress`, `Strain`, `StrainEnergy`, `DisplacementTranslational`, `DisplacementRotational`, `VelocityTranslational`, `VelocityRotational`, `AccelerationTranslational`, `AccelerationRotational`, `ForceAppliedLoad`, `MomentAppliedLoad`, `ForceReaction`, `MomentReaction`, `NodalForceBalanceAll`, `NodalMomentBalanceAll`, `NodalForceBalanceElements`, `NodalMomentBalanceElements`, `KineticEnergyNodalTranslational`, `KinecticEnergyNodalRotational`, `ForceAttachment`, `MomentAttachment`, `ForceConnector`, `MomentConnector`, `ForceSection`, `MomentSection`, `StressBeam`, `StrainBeam`, `ForceElement`, `MomentElement`, `ForceBeam`, `MomentBeam`, `FailureComposite`, `StressInterlaminar`, `Eigenvalue`, `ModalMassData`, `TransformMotion`, `ClearanceMotion`, `EnvelopeMotion`, `ForceGlueNormal`, `MomentGlueNormal`, `ForceGlueTangential`, `MomentGlueTangential`, `ForceInterface`, `MomentInterface`, `InternalForceAndMoment`, `CrossPlot`, `ContactStress`, `NormalContactForce`, `FrictionContactForce`, `ContactAdjustmentTranslational`, `ContactAdjustmentRotational`, `EigenVectorTranslational`, `EigenVectorRotational`, `ForceConnectorAxial`, `MomentConnectorAxial`, `OneDimElementForce`, `OneDimElementMoment`, `OneDimElementWarpingTorque`, `TorsionalStress`, `AxialBendingStress`, `AxialStress`, `TorsionalStrain`, `AxialBendingStrain`, `AxialStrain`, `StrainEnergyDensity`, `StrainEnergyPercent`, `AppliedLoadCriticalMoment`, `AppliedLoadCriticalForce`, `ContactDistanceMag`, `ContactFrictionForceMag`, `ContactFrictionStress1`, `ContactFrictionStress2`, `ContactNormalForceMag`, `ContactNormalStress`, `GridCheckReserve1`, `GridCheckReserve2`, `EffCreepStrain`, `EffCreepStress`, `EffPlasticStrain`, `EffPlasticStress`, `EquivalentStress`, `GasketClosure`, `GasketPressure`, `GridCheckDistance`, `InterlaminarStrainTensor`, `NodalKineticEnergyRot`, `NodalKineticEnergyTrans`, `KineticStrainEnergy`, `KineticElementStrainEnergyDensity`, `KineticPercentStrainEnergy`, `NormalStrain`, `NormalStress`, `PlasticGasketClosure`, `AxialForce1D`, `TotalTorque1D`, `ConnectorDisplacementAxial`, `ConnectorStrainRot`, `ConnectorStrainTrans`, `ConnectorStressRot`, `ConnectorStressTrans`, `ConnectorVelocityAxial`, `CompInterlaminarNormalStress`, `CompInterlaminarShearStress`, `CompPlyStress`, `DisplacementCriticalTranslational`, `DisplacementCriticalRotational`, `ContactStatus`, `Undefined`
- `apex.post.TargetEntityType`: `Node`, `ObjectEnds`, `ObjectMidPoint`
- `apex.post.VectorColorMethod`: `VectorValue`, `Component`
- `apex.post.VectorComponent`: `Resultant`, `Component1`, `Component2`, `Component3`, `Resultant12`, `Resultant23`, `Resultant13`, `F1`, `F2`, `M1`, `M2`, `ForceAxial`, `ForceShearPlane1_V1`, `ForceShearPlane2_V2`, `TorqueTotal`, `MomentBendingPlane1_M1`, `MomentBendingPlane2_M2`, `ForceResultant`, `ForceX`, `ForceY`, `ForceZ`, `ForceXY`, `ForceYZ`, `ForceXZ`, `MomentResultant`, `MomentX`, `MomentY`, `MomentZ`, `MomentXY`, `MomentYZ`, `MomentXZ`, `ForceMoment1Axial`, `ForceMoment1Plane1`, `ForceMoment1Plane2`, `Axial1D1`, `TorqueTotal2`, `TorqueTotal3`, `Undefined`
- `apex.post.VectorDisplayStyle`: `Vector3D`, `Vector1D`, `VectorLine`
- `apex.post.VectorOriginLocation`: `Tip`, `Tail`
- `apex.post.VectorScalingMethod`: `Scaled`, `Constant`

## apex.session

- `apex.session.DisplayRenderStyle`: `Wireframe`, `HiddenLines`, `Filled`, `FilledWithEdges`, `Shaded`, `ShadedWithEdges`, `NoRender`, `Undefined`
- `apex.session.DisplayShellThickness`: `Thickness_2D`, `Offset_2D`, `ThicknessAndOffset_3D`, `Display_None`
- `apex.session.ElementDimensionMetric`: `MinimumLength_2D`, `MaximumLength_2D`, `LengthDegeneracy_2D`, `AngleDegeneracy_2D`
- `apex.session.ElementQualityMetric`: `QualityIndex_2D`, `AspectRatio_2D`, `WarpageAngle_2D`, `WarpageFactor_2D`, `Skew_2D`, `Taper_2D`, `Jacobian_2D`, `QuadMinInteriorAngle_2D`, `QuadMaxInteriorAngle_2D`, `TriMinInteriorAngle_2D`, `TriMaxInteriorAngle_2D`, `AspectRatio_3D`, `Jacobian_3D`
- `apex.session.MarkerSize`: `Small`, `Large`
- `apex.session.MaskableEntities`: `All`, `AllFEM`, `Nodes`, `Elements`, `Elements1D`, `Elements1DBeam2`, `Elements2D`, `Elements2DTria3`, `Elements2DTria6`, `Elements2DQuad4`, `Elements2DQuad8`, `Elements3D`, `Elements3DTetra4`, `Elements3DTetra10`, `Elements3DHex8`, `Elements3DPenta6`, `Elements3DHex20`, `Elements3DPenta15`, `Seeds`, `SeedsPointSeeds`, `SeedsEdgeSeeds`, `PointMasses`, `AllGeometry`, `GeometryVertices`, `GeometryPoints`, `GeometryCurves`, `GeometrySurfaces`, `GeometryNonManifoldSurfaces`, `GeometrySolids`
- `apex.session.MaskableEntities_Apex`: `AllInteractions`, `InteractionsGluePairs`, `InteractionsGluePatches`, `InteractionsTies`, `AllConnections`, `ConnectionsSprings`, `ConnectionsSpringDampers`, `ConnectionsDampers`, `ConnectionsBushings`, `ConnectionsRigidLinks`, `ConnectionsFlexibleLinks`, `AllLBCs`, `LBCsForceMoments`, `LBCsGeneralConstraints`, `LBCsClampedConstraints`, `LBCsAxialConstraints`, `LBCsSphericalConstraints`, `LBCsSymmetryConstraints`, `LBCsPressures`, `LBCsGravities`, `LBCsEnforcedMotions`, `AllSensors`, `SensorsPointSensors`, `SensorsCrossSectionSensors`, `Spans_2D`, `Spans_3D`
- `apex.session.SuppressableEntities`: `AllEntities`, `EdgesAndCurves`, `Vertices`
- `apex.session.Visibility`: `Hidden`, `Visible`, `NotSet`

## apex.setting

- `apex.setting.CreateGeometryInNewPart`: `CurrentPart`, `NewPart`
- `apex.setting.GeometryTessellationTolerance`: `VeryCoarse`, `Coarse`, `Medium`, `Fine`, `VeryFine`
- `apex.setting.ScriptTriggerType`: `PreModelClose`, `PostModelDefault`, `PostModelNew`, `PostModelOpen`, `PostFEMImport`, `PostFEMExport`, `PostGeometryImport`

## apex.studies

- `apex.studies.ArcLengthMethod`: `Crisfield`, `RiksRamm`, `ModifiedRiksRamm`
- `apex.studies.ArtificialDamping`: `No`, `Always`, `DampingEnergy`, `Automatic`
- `apex.studies.AugmentationMethod`: `NotUse`, `Automatic`, `Constant`, `Bilinear`
- `apex.studies.ContactMethod`: `SegmentToSegment`, `NodeToSegment`
- `apex.studies.DTIBlockType`: `SystemCells`, `FileManagement`, `ExecutiveControl`, `CaseControl`, `BulkData`
- `apex.studies.DTIExportOptions`: `doNotWrite`, `writeAtStart`, `writeAtEnd`
- `apex.studies.DataDeckEcho`: `Unset`, `Unsorted`, `Sorted`
- `apex.studies.ExecutionStatus`: `CompletedNoErrors`, `CompletedWithDiagnostics`, `CompletedWithErrors`, `NotSubmitted`, `Running`, `Submitted`
- `apex.studies.FailureAssessMethod`: `safetyFactor`, `stressGoal`
- `apex.studies.FailureCriteria`: `FFFThumbRule`, `TsaiHill`, `TsaiWu`, `VonMises`
- `apex.studies.FrictionType`: `Frictionless`, `BilinearCoulomb`, `BilinearShear`
- `apex.studies.IncrementalScheme`: `Fixed`, `Adaptive`, `ArcLength`
- `apex.studies.InitialStepState`: `PreviousStep`, `StepInThisLoadCase`, `StepInAnotherLoadCase`
- `apex.studies.IterationProcedure`: `PureFullNewton`, `ControlledIterations`
- `apex.studies.MNFMassInvariantOptions`: `partial`, `constant`, `full`, `none`, `rigid`
- `apex.studies.ManufacturingMethod`: `genericAM`, `metalAM`, `FFF`
- `apex.studies.MassCalculationMethod`: `Coupled`, `Lumped`
- `apex.studies.MultiBodyDynamic`: `Dynamic`, `QuasiStatic`
- `apex.studies.NastranAnalysisType`: `Statics`, `LinearCombination`, `RepeatedOutput`, `Symmetry`, `SymmetricCombination`, `Modes`, `ModalOutput`, `Buckling`, `ModalTransient`, `DirectTransient`, `ModalFrequency`, `DirectFrequency`, `ModalComplexEigenvalue`, `DirectComplexEigenvalue`, `CyclicStatics`, `CyclicModes`, `CyclicBuckling`, `CyclicFrequency`, `StaticAeroelasticity`, `StaticAeroelasticDivergence`, `Flutter`, `DynamicAeroelasticity`, `NonlinearStatics`, `NonlinearTransient`, `NonlinearSteadyStateHeat`, `NonlinearTransientHeat`, `DesignOptimization`, `NonlinearHarmonic`, `ALL`, `NonlinearStatics1XX`, `Hot2Cold`, `SteadyStateHeat153`, `CoupledThermalStructural153`, `NonlinearTransient159`, `Undefined`
- `apex.studies.NastranSolutionType`: `Statics_101`, `Modes_103`, `Buckling_105`, `DirectComplexEigenvalue_107`, `DirectFrequency_108`, `DirectTransient_109`, `ModalComplexEigenvalue_110`, `ModelFrequency_111`, `ModalTransient_112`, `CyclicStatics_114`, `CyclicModes_115`, `CyclicBuckling_116`, `CyclicDirectFrequency_118`, `NonlinearHarmonic_128`, `NonlinearTransient_129`, `StaticAeroelasticity_144`, `AerodynamicFlutter_145`, `DynamicAeroelasticity_146`, `TransientStructuralThermal_153`, `DesignOptimization_200`, `Nonlinear_400`, `ALL`, `Undefined`
- `apex.studies.OutputRequestQuantities`: `Stress`, `NonlinearStress`, `Strain`, `StrainEnergy`, `ElementForce`, `NodalForce`, `SectionForce`, `AppliedLoad`, `ConstraintReactionForce`, `ContactResults`, `NodalKineticEnergy`, `Displacement`, `Velocity`, `Acceleration`, `Undefined`
- `apex.studies.PredefinedOption`: `QLinear`, `Mildly`, `Severely`, `NoCharacterization`
- `apex.studies.ReductionStrategy`: `NoneOption`, `Low`, `Medium`, `High`
- `apex.studies.ScenarioConfiguration`: `Static`, `NormalModes`, `LinearBucklingNoPrestiffening`, `LinearBucklingWithPrestiffening`, `ModalFrequencyNoPrestiffening`, `ModalFrequencyWithPrestiffening`, `ModalTransferFrequencyNoPrestiffening`, `ModalTransferFrequencyWithPrestiffening`, `ModalTransientNoprestiffening`, `ModalTransientWithPrestiffening`, `ModalRandomNoPrestiffening`, `ModalRandomWithPrestiffening`, `ShockResponseNoPrestiffening`, `ShockResponseWithPrestiffening`, `MultiBodyTransient`, `MultiBodyTransientStaticPreload`, `MultibodyScripted`, `GenerativeDesign`, `NastranSol400Static`
- `apex.studies.SeparationIn`: `Current`, `Next`
- `apex.studies.SeparationMethod`: `Force`, `AbsoluteStressWithForceArea`, `AbsoluteStressExtrapolation`, `RelativeStressForceArea`, `RelativeStressExtrapolation`
- `apex.studies.ShapeQuality`: `Preview`, `Balanced`, `FineTune`
- `apex.studies.SimulationType`: `Static`, `NormalModes`, `LinearBuckling`, `ModalFrequency`
- `apex.studies.StepOutput`: `LastIncrement`, `Everyincrement`, `FixedIncrement`
- `apex.studies.StepSettingMethod`: `Smart`, `Advanced`
- `apex.studies.StepType`: `Static`, `NormalModes`, `LinearBuckling`, `ModalFrequency`
- `apex.studies.StrutDensity`: `Dense`, `Medium`, `Sparse`

## apex.utility

- `apex.utility.AddRemoveBehavior`: `Add`, `Remove`
- `apex.utility.PolyDataType`: `Triangle`, `Quadrilateral`, `Line`, `QuadraticTriangle`, `QuadraticQuadrilateral`, `QuadraticLine`

