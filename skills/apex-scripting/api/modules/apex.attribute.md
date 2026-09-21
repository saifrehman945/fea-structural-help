# apex.attribute

(apex.attribute module) model Attribute (Beam, Span, PointMass, Tie, etc.) creation, assignment, and editing functions.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.attribute.AlignmentType`: `Offset`, `Mid`, `Top`, `FollowPanel`

`apex.attribute.ApplicationMethod`: `Direct`, `Remote`, `Free`, `Undefined`
  - Possible ApplicationMethod Options in Apex

`apex.attribute.Approach`: `FullyDynamic`, `TransferFunction`
  - Possible Approach Options in Apex

`apex.attribute.AxisLocationMode`: `Undefined`, `Manual`, `Auto`
  - Possible AxisLocationMode Options for the Joint object in Apex

`apex.attribute.BeamBehaviorType`: `Beam`, `Bar`, `Rod`
  - Possible BeamBehaviorType Options in Apex

`apex.attribute.BeamSpanOrientationType`: `Angle`, `Vector`
  - Possible BeamSpanOrientationType Options in Apex

`apex.attribute.BeamSpanType`: `Freestanding`, `Stiffener`
  - Possible BeamSpanType Options in Apex

`apex.attribute.ComponentDirectionAcceleration`: `X`, `Y`, `Z`
  - To identify the ComponentDirectionAcceleration: apex.attribute.ComponentDirectionAcceleration.X, the component direction of acceleration variation is the X direction of the coordinate system. apex.attribute.ComponentDirectionAcceleration.Y, the component direction of acceleration variation is the Y direction of the coordinate system. apex.attribute.ComponentDirectionAcceleration.Z, the component direction of acceleration variation is the Z direction of the coordinate system

`apex.attribute.ConnectorType`: `Spring1D`, `Damper1D`, `SpringDamper1D`, `Bushing`, `RigidLink`, `FlexibleLink`, `Gap`, `Fastener`, `Undefined`
  - Possible ConnectorType Options in Apex

`apex.attribute.ConstitutiveModelType`: `Elasticity`, `ViscoElasticity`, `Mass`, `ThermalExpansion`, `Failure`, `Plasticity`
  - This Enum is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported

`apex.attribute.ConstraintType`: `Clamped`, `General`, `Axial`, `Symmetry`, `Spherical`
  - Possible ConstraintType options in Apex

`apex.attribute.ContactBodyDimension`: `Dimension3D`, `Dimension2D`
  - Of contact body Dimension

`apex.attribute.ContactBodyForm`: `BCBODY1`, `BCSURF`, `BCGRID`, `Undefined`
  - Of contact body form

`apex.attribute.ContactBodyType`: `Deform`, `Rigid`, `SymmetryRigid`, `HeatRigid`
  - Of contact body type

`apex.attribute.ContactResultCalculation`: `Origin`, `EstimatedCentroid`
  - Of deform body calculation location for contact force/moment

`apex.attribute.ContactSearchOrder`: `DoubleSide`, `SingleSide`, `Automatic`
  - To contact search order for node to segment contact method

`apex.attribute.ContactSurfaceForm`: `FACE`, `GRID`, `RIGID`, `Undefined`
  - Of contact surface form when bodyForm = BCSURF

`apex.attribute.ControlNodeDefinitionMethod`: `Bottom`, `Mid`, `OffsetFromBottom`, `OffsetFromTop`, `Top`, `User`
  - Control node location

`apex.attribute.CoordinateSystemDefinition`: `SuperElement`, `Residual`
  - To identify the coordinate system location: apex.attribute.CoordinateSystemDefinition.SuperElement, the coordinate system is defined in the super-element and will be translated, rotated with the super-element. apex.attribute.CoordinateSystemDefinition.Residual, the coordinate system is defined in the residual structure and stationary with the basic coordinate system

`apex.attribute.CrossSectionMethod`: `Automatic`, `Manual`
  - Cross section of bolt

`apex.attribute.DOFDefinitionMode`: `All`, `Individual`
  - Possible DOFDefinitionMode Options for the DiscreteTie object in Apex

`apex.attribute.DiscontinuityDefinition`: `Auto`, `Manual`
  - Of Discontinuity Definition

`apex.attribute.DiscreteFEMFieldType`: `DiscreteThicknessField`, `DiscreteOffsetField`, `DiscreteAngleField`, `DiscreteCoordinateSystemField`
  - Type of DiscreteFEMField, which could be one of values: DiscreteThicknessField, DiscreteOffsetField, DiscreteAngleField, DiscreteCoordinateSystemField

`apex.attribute.DiscreteRegionType`: `Node`, `Element`, `ElementFace`, `ElementNode`, `FaceNode`
  - Possible DiscreteRegionType Options in Apex

`apex.attribute.Distribution`: `Cosine`
  - Distribution type for LoadLug

`apex.attribute.DistributionMode`: `Auto`, `Custom`
  - Possible DistributionMode Options for the DiscreteTie object in Apex

`apex.attribute.DistributionOrientation`: `Normal`, `Parallel`
  - DistributionOrientation for LoadLug

`apex.attribute.DistributionType`: `Rigid`, `Compliant`
  - Possible DistributionType Options for the DiscreteTie object in Apex

`apex.attribute.DynamicLoadType`: `AppliedLoad`, `Displacement`, `Velocity`, `Acceleration`
  - To identify the dynamic load type: apex.attribute.DynamicLoadType.AppliedLoad, the dynamic excitation load type should be the applied load. apex.attribute.DynamicLoadType.Displacement, the dynamic excitation load type should be the displacement. apex.attribute.DynamicLoadType.Velocity, dynamic excitation load type shouldbe the velocity. apex.attribute.DynamicLoadType.Acceleration, dynamic excitation load type should be the acceleration

`apex.attribute.EnforcedMotionType`: `Displacement`, `Velocity`, `Acceleration`
  - Possible EnforcedMotionType Options in Apex

`apex.attribute.ExportRenumberMethod`: `Internal`, `Export`
  - To control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Scenario Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex

`apex.attribute.ExtendedKeyword`: `Undefined`, `TABLES1`, `TABLEST`, `TABLEM1`, `TABLED1`

`apex.attribute.FailureCriteriaComposite`: `Undefined`, `HILL`, `HOFF`, `TSAI`, `FollowPanel`
  - Maximum Strain theory

`apex.attribute.FastenerStiffnessCoordinateSystem`: `Global`, `UserDefined`, `MinusOne`, `Unset`
  - Stiffness coordinate system value, which could be one of values: Global, UserDefined, MinusOne, Unset

`apex.attribute.FlagOfCoordinateSystem`: `Relative`, `Absolute`, `Auto`
  - Flag of coordinate system for Fastener, either in "Relative" or "Absolute"

`apex.attribute.HardeningRule`: `Isotropic`, `Kinematic`, `Both`
  - This Enum is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported

`apex.attribute.IdConflictResolutionMethod`: `Undefined`, `AutomaticOffset`, `AllowDuplicates`
  - Possible IdConflictResolutionMethod Options for the BDF import in Apex

`apex.attribute.ImportRenumberMethod`: `Internal`, `Import`
  - To control how renumbering of finite element entities is handled if duplicate ID's are detected within the scope of the exported Scenario Apex supports duplicate ID's for most finite element entities including Nodes and Elements, however most Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex

`apex.attribute.InputForm`: `Component`, `Resultant`

`apex.attribute.InputType`: `ElementUniform`, `ElementVariable`
  - To indicate the load distribution is uniform or variable on a single element. apex.attribute.InputType.ElementUniform, the load distribution is uniform on a single element. apex.attribute.InputType.ElementVariable, the load distribution is variable on a single element

`apex.attribute.IntegrationNetwork`: `Automatic`, `Bubble`, `Three`, `Two`
  - IntegrationNetwork for PropertiesElement3D

`apex.attribute.IntegrationScheme`: `Automatic`, `Reduced`, `Full`
  - IntegrationScheme for PropertiesElement3D

`apex.attribute.InteractionType`: `Glue`, `GeneralContact`, `SelfContact`
  - To indicate interaction type

`apex.attribute.InterferenceFitMethod`: `NormalDirection`, `UserDirection`, `ScaleFactor`, `Automatic`
  - Of Interference Fit Method

`apex.attribute.JointAxis`: `XAxis`, `YAxis`, `ZAxis`
  - Possible JointRenderType Options for the Joint object in Apex

`apex.attribute.JointRenderType`: `Undefined`, `RBE2`, `RJOINT`
  - Possible JointRenderType Options for the Joint object in Apex

`apex.attribute.JointType`: `Revolute`, `Cylindrical`, `Spherical`, `Prismatic`, `Planar`, `Undefined`
  - Type of Joint. Specific Joint types are enumerated using the syntax apex.attribute.JointType."<enum_value>" For example: apex.attribute.JointType.Revolute

`apex.attribute.KeywordMaterialPrimary`: `Undefined`, `MAT1`, `MAT2`, `MAT8`, `MAT9`, `MATORT`

`apex.attribute.KeywordMaterialSecondary`: `Undefined`, `MATEP`, `MATPE1`, `MATS1`, `MATSMA`, `MATT1`, `MAT1F`, `MATT2`, `MAT2F`, `MATT9`, `MAT9F`, `MATG`, `MATTG`, `MATHE`, `MATHP`

`apex.attribute.LineLoadDirection`: `Normal`, `Tangent`, `X`, `Y`, `Z`
  - To identify the scale type of beam distributed load: "apex.attribute.LineLoadDirection.Normal", the line load is in the mean plan, normal to the edge, and pointing outward from the element. "apex.attribute.LineLoadDirection.Tangent", the line load is in tangential direction of the edge, pointing from G1 to G2 if the edge is connecting G1 and G2. "apex.attribute.ScaleTypeBeam.Y", the line load is in Y direction of the element coordinate system. "apex.attribute.ScaleTypeBeam.Z", the line load is in Z direction of the element coordinate system. "apex.attribute.ScaleTypeBeam.X", the line load is in X direction of the element coordinate system

`apex.attribute.LoadMethodRotational`: `Centrifugal`, `RotationInertia`
  - To identify the load method of rotational force: apex.attribute.LoadMethodRotational.Centrifugal should be used when there is no coupling in mass matrix - the lumped mass is used with or without element offset. apex.attribute.LoadMethodRotational.RotationInertia should be used when lumped or consistent mass matrix is used without element offset

`apex.attribute.LoadTypeDistributedBeam2`: `ForceX`, `ForceY`, `ForceZ`, `ForceXE`, `ForceYE`, `ForceZE`, `MomentX`, `MomentY`, `MomentZ`, `MomentXE`, `MomentYE`, `MomentZE`
  - To identify the load type of distributed load applied to beam element with two nodes: apex.attribute.LoadTypeDistributedBeam2.ForceX, the load is force in X direction of the basic coordinate system. apex.attribute.LoadTypeDistributedBeam2.ForceY, the load is force in Y direction of the basic coordinate system. apex.attribute.LoadTypeDistributedBeam2.ForceZ, the load is force in Z direction of the basic coordinate system. apex.attribute.LoadTypeDistributedBeam2.ForceXE, the load is force in X direction of the element coordinate system. apex.attribute.LoadTypeDistributedBeam2.ForceYE, the load is force in Y direction of the element coordinate system. apex.attribute.LoadTypeDistributedBeam2.ForceZE, the load is force in Z direction of the element coordinate system. apex.attribute.LoadTypeDistributedBeam2.MomentX, the load is moment in X direction of the basic coordinate system. apex.attribute.LoadTypeDistributedBeam2.MomentY, the load is moment in Y direction of the basic coordinate system. apex.attribute.LoadTypeDistributedBeam2.MomentZ, the load is moment in Z direction of the basic coordinate system. apex.attribute.LoadTypeDistributedBeam2.MomentXE, the load is moment in X direction of the element coordinate system. apex.attribute.LoadTypeDistributedBeam2.MomentYE, the load is moment in Y direction of the element coordinate system. apex.attribute.LoadTypeDistributedBeam2.MomentZE, the load is moment in Z direction of the element coordinate system

`apex.attribute.LoadTypeDistributedBeam3`: `Force`, `Moment`, `Bimoment`
  - To identify the load type of distributed load applied to beam element with three nodes: apex.attribute.LoadTypeDistributedBeam3.Force, the load is a force. apex.attribute.LoadTypeDistributedBeam3.Moment, the load is a moment. apex.attribute.LoadTypeDistributedBeam3.Bimoment, the load is bimoment

`apex.attribute.MarcInputType`: `Dat`, `Mfd`, `Mud`
  - Marc input file format that will be requested when an Apex Scenario is exported to Marc

`apex.attribute.MassDistribution`: `TotalMass`, `MassPerArea`, `MassPerLength`
  - Possible MassDistribution Options for the Nonstructural Mass object in Apex

`apex.attribute.MaterialAlignmentMethod`: `Curve`, `CoordinateSystemAxis`, `EulerAngles`
  - This Enum is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported

`apex.attribute.MaterialModelType`: `Unknown`, `ConstitutiveModel`, `MaterialModel`
  - This Enum is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported

`apex.attribute.MaterialType`: `Isotropic`, `Orthotropic`, `Anisotropic3D`, `Orthotropic3D`, `TransversalIsotropic3D`, `Anisotropic`
  - Possible MaterialType Options in Apex

`apex.attribute.MaterialTypeDomain`: `Isotropic`, `Dim2`, `Dim3`, `NonDim2`, `NonDim3`
  - This Enum is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported

`apex.attribute.MeshDependentTieRenderStyle`: `AsRBARS`, `UnConnected`

`apex.attribute.MotionControlType`: `Velocity`, `Position`, `Load`
  - Of rigid body motion control type

`apex.attribute.NastranResultOutputType`: `Hdf5`, `Op2`, `Xdb`, `Master`, `Dball`
  - Nastran results file format that will be requested when an Apex Scenario is exported to Nastran

`apex.attribute.NonstructuralMassType`: `Constant`, `Variable`
  - Possible NonstructuralMassType Options for the Nonstructural Mass object in Apex

`apex.attribute.OrientationType3D`: `Unset`, `Global`, `DefautElement`, `AlternateElement`, `Local`
  - Material orientation type for PropertiesElement3D

`apex.attribute.OrientationTypeDistributedBeam3`: `Basic`, `Local`, `Element`
  - To identify the type of orientation for the beam distribute load applied to beam element with three nodes. apex.attribute.OrientationTypeDistributedBeam3.Basic, the load is defined in the basic coordinate system. apex.attribute.OrientationTypeDistributedBeam3.Element, the load is defined in the element coordinate system. apex.attribute.OrientationTypeDistributedBeam3.Local, the load is defined in the the local coordinate system on beam cross section

`apex.attribute.OutputLocation`: `Unset`, `Grid`, `Gauss`
  - OutputLocation for PropertiesElement3D

`apex.attribute.PlyBehavior`: `Default`, `Membrane`, `Bending`, `Smear`, `FollowPanel`

`apex.attribute.PlyIdBehavior`: `UseGlobal`, `NoGlobal`, `FollowPanel`

`apex.attribute.PropertiesElement2DType`: `SimpleShell`, `Shell`, `ShearPanel`
  - Types of 2D element properties

`apex.attribute.PropertiesElement3DType`: `Homogeneous`
  - PropertiesElement3DType for PropertiesElement3D

`apex.attribute.Property2DAlignmentMethod`: `Curve`, `CoordinateSystem`
  - Types of alignment method

`apex.attribute.RigidFaceType`: `BCNURBS`, `BCNURB2`, `BCBZIER`, `BCPATCH`
  - Rigid face type

`apex.attribute.ScaleTypeDistributedBeam2`: `Length`, `Fractional`, `LengthProjected`, `FractionalProjected`
  - To identify the scale type of beam distributed load applied to beam element with 2 nodes. apex.attribute.ScaleTypeDistributedBeam2.Length, the distance values are actual distances along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeDistributedBeam2.Fractional, the distance values are are ratios of the distance along the axis to the total length, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeDistributedBeam2.LengthProjected, the distance values are projected lengths along the element axis, and if distance1 != distance 2, then load factors are load intensities per unit length of the element. apex.attribute.ScaleTypeDistributedBeam2.FractionalProjected, the distance values are ratios of the actual distance to the length of the bar (CBAR entry), and if distance1 != distance 2, then the distributed load is specified in terms of the projected length of the bar

`apex.attribute.SelectionExtractionApproach`: `Automatic`, `ForceConstantThickness`, `ForceVariableThickness`
  - Possible SelectionExtractionApproach Options for thickness creation

`apex.attribute.ShapeMatingSide`: `XPositive`, `YPositive`, `XNegative`, `YNegative`
  - Possible ShapeMatingSide Options in Apex

`apex.attribute.ShellBehaviorType`: `ShearPanel`, `ThinShell`
  - This Enum is no longer supported in Apex

`apex.attribute.ShellLayer`: `TopAndButtom`, `TopOnly`, `ButtomOnly`
  - Which shell layer to be used for contact detection

`apex.attribute.StackSymmetry`: `Asymmetric`, `Odd`, `Even`
  - Whether the provided sheet stack definition will be reflected to add additional sheets to the stack or not

`apex.attribute.StrainType`: `Type1`, `Type2`
  - Possible StrainType Options in Apex

`apex.attribute.SurfOrLine`: `Surface`, `Line`
  - To indicate whether the load acts on the surface or edges. "apex.attribute.SurfOrLine.Surface", the load acts on the element face. "apex.attribute.SurfOrLine.Line", the load acts on the consistent edges of the element

`apex.attribute.TopBottom`: `Top`, `Bottom`
  - Possible TopBottom Options in Apex

`apex.attribute.createTypeForFastener`: `ByElement`, `ByProperty`
  - Fastener surface patch type

## Module functions

### `apex.attribute.assignAnalysisSystem(coordinateSystem: apex.construct.CoordinateSystem, targets: apex.EntityCollection) -> bool`
Assign a coordinate system as analysis coordinate system to the target entities.

- `coordinateSystem` — the coordinate system to be assigned to targets.
- `targets` — the targets that coordinate system is assigning to. It can be Assembly, Part, GeometryBody, Cell, Face, Edge, Vertex, MeshBody, Element, or a set of nodes. In current release, only supports nodes as assigned targets. If the targets are other entities, the system will give an exception: Unsupported targets to be assigned.

### `apex.attribute.assignBeamSpan(edges: apex.EntityCollection, beamSpan: BeamSpan) -> bool`
Assign a new BeamSpan to a set of edges.

- `edges` — the target of edges that the new BeamSpan is assgined to
- `beamSpan` — the new BeamSpan to be assigned

### `apex.attribute.assignMaterial(material: Material, target: apex.EntityCollection) -> bool`
This Function is no longer supported in Apex Nastran mission. Refer to PropertiesElement2D and PropertiesElement3D to determine how this capability is now supported.

- `material` — the Material to be assigned
- `target` — the target of elements that Material is asggined to

Assign a new Material to a set of elements.

### `apex.attribute.assignMaterialAlignCoordinate(material: Material, target: apex.EntityCollection, materialAxis: apex.EntityCollection) -> MaterialCoverageRegion`
This Function is no longer supported in Apex. Refer to apex.attribute.createFieldMaterialOrientationFromCoordinate to determine how this capability is now supported.

- `material` — The Material to assign an align. The Material must include an orthotropic constitutive model otherwise the method will throw an exception
- `target` — The collection of entities that the Material will be assigned to as an EntityCollection. Target may contain Solids, Surfaces, Faces or 2D elements - all other types will be silently ignored. When Solids are included they are internally expanded to the complete set of free faces of the apex.geometry.Solid. Any duplicate entities in target are ignored
- `materialAxis` — A collection of apex.construct.CoordinateSystem that will be used to define the Material orientation. NOTE : Current release of Apex support a single apex.construct.CoordinateSystem only which must be the first entry in the collection. If the Collection includes more than one entry only the first will be used and all others will be silently ignored.

Assigns an orthtropic or 2D anisotropic Material to a region of the model, aligns the material axis using a apex.construct.CoordinateSystem axis and returns a MaterialCoverageRegion.

### `apex.attribute.assignMaterialAlignCurve(material: Material, target: apex.EntityCollection, director: apex.EntityCollection) -> MaterialCoverageRegion`
This Function is no longer supported in Apex. Refer to apex.attribute.createFieldMaterialOrientationAlignCurve to determine how this capability is now supported.

- `material` — The Material to assign an align. The Material must include an orthotropic constitutive model otherwise the method will throw an exception
- `target` — The collection of entities that the Material will be assigned to as an EntityCollection. Target may contain Solids, Surfaces, Faces or 2D elements - all other types will be silently ignored. When Solids are included they are internally expanded to the complete set of free faces of the apex.geometry.Solid. Any duplicate entities in target are ignored
- `director` — A collection of apex.geometry.Curves and/or apex.geometry.Edges that will be used to define the Material orientation. director may include Curves or Edges. NOTE : Current releases of Apex support a single apex.geometry.Curve or apex.geometry.Edge only which must be the first entry in the collection. If the Collection includes more than one entry only the first will be used and all others will be silently ignored.

Assigns an orthtropic or 2D anisotropic Material to a region of the model and aligns the Material axis using a director apex.geometry.Curve or apex.geometry.Edge and returns a MaterialCoverageRegion.

### `apex.attribute.assignMaterialAlignEulerAngles(material: Material, target: apex.EntityCollection, orientation: apex.construct.Orientation, origin: apex.ILocation) -> MaterialCoverageRegion`
This Function is no longer supported in Apex. Refer to apex.attribute.createFieldMaterialOrientationFromCoordinate to determine how this capability is now supported.

- `material` — The Material to assign an align. The Material must include an 3D Anisotropic/Orthotropic constitutive model otherwise the method will throw an exception.
- `target` — The collection of entities that the Material will be assigned to as an EntityCollection. Target may contain Solids or 3D elements - all other types will be silently ignored. Any duplicate entities in target are ignored
- `orientation` — Define an internal coordinate system direction to determine the reference direction of the material
- `origin` — Defined the location of the coordinate system used to determine the direction of the material

Assigns an 3D orthtropic or 3D anisotropic Material to a region of the model, aligns the material axis using the Euler Angles of a Coordinates system and returns a MaterialCoverageRegion.

### `apex.attribute.assignPropertiesElement3D(target: apex.EntityCollection, property: apex.attribute.PropertiesElement3D) -> None`
Assigns a PropertiesElement3D to Apex entities.

- `target` — The target of entities that will be assigned with a PropertiesElement3D.
- `property` — The PropertiesElement3D to be assigned.

### `apex.attribute.assignProperty2D(property2d: apex.attribute.PropertiesElement2D, target: apex.EntityCollection, offset: float = NAN, assignOffset: bool = False, clearOverlapping: bool = False) -> apex.attribute.PropertiesElement2DCollection`
Assign a new 2D Property to a set of targets.

- `property2d` — The 2D property to assign
- `target` — The collection of entities that the 2d property will be assigned to as an EntityCollection.
- `offset` — Optional-the offset of the 2D property.
- `assignOffset` — Optional-the boolean argument to indicate whether the 2d element property assign the element offset.
- `clearOverlapping` — Optional-the boolean argument to indicate whether the 2d element property clear overlapping target whith thickness field. target may include Parts, Surfaces, Faces 2D Meshes/Elements, thicknessField/MidsurfacepropertyField. The target should be Parts, Surfaces, Faces 2D Meshes/Elements, thicknessField/MidsurfacepropertyField and all other types will be silently ignored. Any duplicate entities in target are ignored

### `apex.attribute.assignProperty2DAlignCoordinateAxis(property2d: apex.attribute.PropertiesElement2D, target: apex.EntityCollection, property2DAxis: apex.construct.CoordinateSystem) -> apex.attribute.Property2DCoverageRegionCollection`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.attribute.createFieldMaterialOrientationFromCoordinate. Assigns an 2D element property to a region of the model, aligns the 2d property axis using the X axis of a Coordinates system and returns a MaterialCoverageRegion.

- `property2d` — The 2D property to assign an align.
- `target` — The collection of entities that the 2d property will be assigned to as an EntityCollection. target may include Surfaces, Faces or 2D/3D elements. The target should be Surfaces, Faces or 2D elements and all other types will be silently ignored. Solids are internally expanded to the set of all exterior Faces of the Solids Any duplicate entities in target are ignored
- `property2DAxis` — A Coordinate system whose X axis defines the orientation.

### `apex.attribute.assignProperty2DAlignCurve(property2d: apex.attribute.PropertiesElement2D, target: apex.EntityCollection, director: apex.EntityCollection) -> apex.attribute.Property2DCoverageRegionCollection`
DEPRECATED: THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.PLEASE USE apex.attribute.createFieldMaterialOrientationAlignCurve. Assigns an 2d element property (include orthtropic or 2D anisotropic material ) to a region of the model and aligns the direction axis using a director Curve or Edge and returns a Property2DCoverageRegion.

- `property2d` — The 2D property to assign an align.
- `target` — The collection of entities that the 2d property will be assigned to as an EntityCollection. target may include Surfaces, Faces or 2D/3D elements. The target should be Surfaces, Faces or 2D elements and all other types will be silently ignored. Solids are internally expanded to the set of all exterior Faces of the Solids Any duplicate entities in target are ignored
- `director` — A collection of Curves and/or Edges that will be used to define the orientation. director may include Curves or Edges. NOTE : Current releases of Apex support a single Curve or Edge only which must be the first entry in the collection. If the Collection includes more than one entry only the first will be used and all others will be silently ignored.

### `apex.attribute.assignShellBehavior(behavior: ShellBehavior, target: apex.EntityCollection) -> None`
This Function is no longer supported in Apex. Refer to apex.attribute.assignProperty2D to determine how this capability is now supported.

- `behavior` — The ShellBehavior object to assign to the target
- `target` — The objects that the ShellBehavior will be assigned to as an EntityCollection.

Assign a ShellBehavior to a target region of the model. Any existing ShellBehavior assignments that are associated with objects in the target will be overwitten. ShellBehaviors of type "ShearPanel" are only supported on QUAD4 type elements. If the target contains 2D elements of any other type, or contains meshed geometry where the mesh contains elements of type other than QUAD4 the method will throw an exception. EntityCollection is expected to include Part, Solid, Surface, Face or 2D (Shell) elements. Entities of any other type will be silently ignored.

### `apex.attribute.assignShellSection(section: ShellSection, target: apex.EntityCollection) -> bool`
This Function is no longer supported in Apex. Refer to apex.attribute.createFieldThicknessOffsetConstant to determine how this capability is now supported.

- `section` — missing, add it for avoiding warning
- `target` — the target of elements that ShellSection is asggined to

Assign a new ShellSection to a set of targets (parts, geom bodies, meshes, faces)

### `apex.attribute.createBeamShapeC(name: str, overallWidth: float, overallHeight: float, webThickness: float, flangeThickness: float) -> BeamShapeC`
Create a new C BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `webThickness` — missing, add it for avoiding warning.
- `flangeThickness` — thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeCAlternate(name: str, flangeLength: float, webThickness: float, flangeSeparation: float, overallHeight: float) -> BeamShapeCAlternate`
Create a new C Alternate BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `flangeLength` — length of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.
- `flangeSeparation` — separation of the new BeamShape.
- `overallHeight` — height of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeCruciform(name: str, horizontalSparExtension: float, verticalSparExtension: float, overallHeight: float, horizontalSparWidth: float) -> BeamShapeCruciform`
Create a new Cruciform BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `horizontalSparExtension` — spar extension of the new BeamShape.
- `verticalSparExtension` — spar extension of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `horizontalSparWidth` — spar width of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeH(name: str, flangeSeparation: float, flangeThickness: float, overallHeight: float, webThickness: float) -> BeamShapeH`
Create a new H BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `flangeSeparation` — separation of the new BeamShape.
- `flangeThickness` — thickness of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHat(name: str, height: float, thickness: float, hatWidth: float, flangeWidth: float) -> apex.attribute.BeamShapeHat`
Create a new Hat BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `height` — of the new BeamShape.
- `thickness` — of the new BeamShape.
- `hatWidth` — width of the new BeamShape.
- `flangeWidth` — width of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHatClosed(name: str, overallWidth: float, overallHeight: float, hatWidth: float, hatThickness: float, headThickness: float) -> BeamShapeHatClosed`
Create a new Hat Closed BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `hatWidth` — width of the new BeamShape.
- `hatThickness` — thickness of the new BeamShape.
- `headThickness` — thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHollowDoubleRectangular(name: str, overallWidth: float, overallHeight: float, webOffset: float, leftWallThickness: float, webThickness: float, rightWallThickness: float, topLeftWallThickness: float, bottomLeftWallThickness: float, topRightWallThickness: float, bottomRightWallThickness: float) -> apex.attribute.BeamShapeHollowDoubleRectangular`
Create a new Hollow Double Rectangular BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `webOffset` — missing, add it for avoiding warning
- `leftWallThickness` — wall thickness of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.
- `rightWallThickness` — wall thickness of the new BeamShape.
- `topLeftWallThickness` — left wall thickness of the new BeamShape.
- `bottomLeftWallThickness` — left wall thickness of the new BeamShape.
- `topRightWallThickness` — right wall thickness of the new BeamShape.
- `bottomRightWallThickness` — right wall thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHollowRectangularAsymmetric(name: str, overallWidth: float, overallHeight: float, ceilingThickness: float, floorThickness: float, rightSideThickness: float, leftSideThickness: float) -> apex.attribute.BeamShapeHollowRectangularAsymmetric`
Create a new Hollow Rectangular Asymmetric BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `ceilingThickness` — thickness of the new BeamShape.
- `floorThickness` — thickness of the new BeamShape.
- `rightSideThickness` — side thickness of the new BeamShape.
- `leftSideThickness` — side thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHollowRectangularSymmetric(name: str, overallWidth: float, overallHeight: float, floorCeilingThickness: float, sideWallThickness: float) -> apex.attribute.BeamShapeHollowRectangularSymmetric`
Create a new Shape Hollow Rectangular Symmetric BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `floorCeilingThickness` — ceiling thickness of the new BeamShape.
- `sideWallThickness` — wall thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHollowRound(name: str, outerRadius: float, innerRadius: float) -> apex.attribute.BeamShapeHollowRound`
Create a new Hollow Round BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `outerRadius` — radius of the new BeamShape.
- `innerRadius` — radius of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeHollowRoundByThickness(name: str, outerRadius: float, thickness: float) -> apex.attribute.BeamShapeHollowRoundByThickness`
Create a new Hollow Round By Thickness BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `outerRadius` — radius of the new BeamShape.
- `thickness` — of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeIAsymmetric(name: str, overallHeight: float, bottomFlangeWidth: float, topFlangeWidth: float, webThickness: float, bottomFlangeThickness: float, topFlangeThickness: float) -> BeamShapeIAsymmetric`
Create a new I asymmetric BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallHeight` — height of the new BeamShape.
- `bottomFlangeWidth` — flange width of the new BeamShape.
- `topFlangeWidth` — flange width of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.
- `bottomFlangeThickness` — flange thickness of the new BeamShape.
- `topFlangeThickness` — flange thickness h of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeISymmetric(name: str, flangeExtension: float, webThickness: float, flangeSeparation: float, overallHeight: float) -> BeamShapeISymmetric`
Create a new I Symmetric BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `flangeExtension` — extension of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.
- `flangeSeparation` — separation of the new BeamShape.
- `overallHeight` — height of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeL(name: str, overallWidth: float, overallHeight: float, horizontalLegThickness: float, verticalLegThickness: float) -> BeamShapeL`
Create a new L BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `horizontalLegThickness` — leg thickness of the new BeamShape.
- `verticalLegThickness` — leg thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeNumericBar(name: str, areaCrossSection: float, areaMomentOfInertia_I11: float, areaMomentOfInertia_I22: float = 0.0, areaProductOfInertia_I12: float = 0.0, torsionalStiffness: float = 0.0, shearStiffnessFactor_K1: float = 1.0, shearStiffnessFactor_K2: float = 1.0, stressRecoveryPoints: [apex.construct.Point2D] = [], description: str = "") -> BeamShapeNumeric`
Creates a BeamShape with "Bar" type, by directly specifying the beam section properties. Numeric BeamShapes support "Beam", "Bar" and "Rod" sub-types and this method creates a "Bar" sub-type that will ultimately cause the creation of Nastran CBAR/PBAR type entities. To create "Beam" (CBEAM/PBEAM) or "Rod" (CROD/PROD) types, use the createBeamShapeNumericBeam() or createBeamShapeNumericRod() methods instead.

- `name` — The name of the BeamShapeNumeric. If the name is omitted Apex will assign a default name
- `areaCrossSection` — The cross sectional area of the BeamShape. This is a required argument Area is a quantity that has units so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `areaMomentOfInertia_I11` — The area moment of inertia for bending about the "1" axis of the BeamShape neutral axis This is a required argument. Area moment of inertia is a quantity that has units (Length^4) so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `areaMomentOfInertia_I22` — The area moment of inertia for bending about the "2" axis of the BeamShape neutral axis This is a required argument. Area moment of inertia is a quantity that has units (Length^4) so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `areaProductOfInertia_I12` — The area product of inertia for the BeamShape neutral axis This is an optional argument with a default value of 0.0. Area product of inertia is a quantity that has units (Length^4) so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `torsionalStiffness` — The torsional stiffness parameter of the BeamShape neutral axis This is an optional argument with a default value of 0.0 This quantity is unitless
- `shearStiffnessFactor_K1` — Optional argument defining the shear stiffness factor for the BeaShape "1" plane. Defaults to 1.0 Shear stiffness factors adjust the effective transverse shear cross-section area according to the Timoshenko beam theory. The default values of 1.0 approximate the effects of shear deformation. To neglect shear deformation (i.e., to obtain the Bernoulli-Euler beam theory), the values of shearStiffnessFactor_K1 and shearStiffnessFactor_K2 should be set to 0.0.
- `shearStiffnessFactor_K2` — Optional shear stiffness factor for the BeamShape "1" plane. Defaults to 1.0. Shear stiffness factors adjust the effective transverse shear cross-section area according to the Timoshenko beam theory. The default values of 1.0 approximate the effects of shear deformation. To neglect shear deformation (i.e., to obtain the Bernoulli-Euler beam theory), the values of shearStiffnessFactor_K1 and shearStiffnessFactor_K2 should be set to 0.0.
- `stressRecoveryPoints` — Optional list of four Point2D objects that define the fibre locations where stress outputs will be generated. If omitted default outputs will be provided at the corners of a unit square section. Each Point2D object defines a location in the "1-2" plane of the BeamShape relative to the shear center. The locations are quantities that have units of Length so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `description` — An optional argument defining the description of the BeamShape. If omitted, the description will be blank.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeNumericBeam(name: str, areaCrossSection: float, areaMomentOfInertia_I11: float, areaMomentOfInertia_I22: float = 0.0, areaProductOfInertia_I12: float = 0.0, torsionalStiffness: float = 0.0, neutralAxisOffset_1: float = 0.0, neutralAxisOffset_2: float = 0.0, shearStiffnessFactor_K1: float = 1.0, shearStiffnessFactor_K2: float = 1.0, stressRecoveryPoints: [apex.construct.Point2D] = [], description: str = "") -> BeamShapeNumeric`
Create a new numeric BeamShape of Beam type, by directly specifying the beam section properties. Numeric BeamShapes support "Beam", "Bar" and "Rod" sub-types and this method creates a "Beam" sub-type that will ultimately cause the creation of Nastran CBEAM/PBEAM type entries. To create "Bar" (CBAR/PBAR) or "Rod" (CROD/PROD) types, use the createBeamShapeNumericBar() or createBeamShapeNumericRod() methods instead.

- `name` — The name of the BeamShapeNumeric. If the name is omitted Apex will assign a default name
- `areaCrossSection` — The cross sectional area of the BeamShape. This is a required argument. Area is a quantity that has units so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `areaMomentOfInertia_I11` — The area moment of inertia for bending about the "1" axis of the BeamShape neutral axis This is a required argument. Area moment of inertia is a quantity that has units (Length^4) so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `areaMomentOfInertia_I22` — The area moment of inertia for bending about the "2" axis of the BeamShape neutral axis This is a required argument. Area moment of inertia is a quantity that has units (Length^4) so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `areaProductOfInertia_I12` — The area product of inertia for the BeamShape neutral axis This is an optional argument with a default value of 0.0. Area product of inertia is a quantity that has units (Length^4) so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `torsionalStiffness` — The torsional stiffness parameter of the BeamShape neutral axis This is an optional argument with a default value of 0.0 This quantity is unitless
- `neutralAxisOffset_1` — An optional argument defining the offset of the neutral axis from the shear center in the Beam Shape "1" direction. The offset is a quantity that has units of Length so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `neutralAxisOffset_2` — An optional argument defining the offset of the neutral axis from the shear center in the Beam Shape "2" direction. The offset is a quantity that has units of Length so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `shearStiffnessFactor_K1` — Optional argument defining the shear stiffness factor for the BeaShape "1" plane. Defaults to 1.0 Shear stiffness factors adjust the effective transverse shear cross-section area according to the Timoshenko beam theory. The default values of 1.0 approximate the effects of shear deformation. To neglect shear deformation (i.e., to obtain the Bernoulli-Euler beam theory), the values of shearStiffnessFactor_K1 and shearStiffnessFactor_K2 should be set to 0.0.
- `shearStiffnessFactor_K2` — Optional shear stiffness factor for the BeamShape "1" plane. Defaults to 1.0. Shear stiffness factors adjust the effective transverse shear cross-section area according to the Timoshenko beam theory. The default values of 1.0 approximate the effects of shear deformation. To neglect shear deformation (i.e., to obtain the Bernoulli-Euler beam theory), the values of shearStiffnessFactor_K1 and shearStiffnessFactor_K2 should be set to 0.0.
- `stressRecoveryPoints` — Optional list of four Point2D objects that define the fibre locations where stress outputs will be generated. If omitted default outputs will be provided at the corners of a unit square section. Each Point2D object defines a location in the "1-2" plane of the BeamShape relative to the shear center. The locations are quantities that have units of Length so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `description` — An optional argument defining the description of the BeamShape. If omitted, the description will be blank.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeNumericRod(name: str, areaCrossSection: float, torsionalStiffness: float = 0.0, torsionalStressCoefficient: float = 0.0, description: str = "") -> BeamShapeNumeric`
Create Creates a BeamShape with "Rod" type, by directly specifying the beam section properties. Numeric BeamShapes support "Beam", "Bar" and "Rod" sub-types and this method creates a "Rod" sub-type that will ultimately cause the creation of Nastran CROD/PROD type entities. To create "Beam" (CBEAM/PBEAM) or "Bar" (CBAR/PBAR) types, use the createBeamShapeNumericBeam() or createBeamShapeNumericBar() methods instead.

- `name` — The name of the BeamShapeNumeric. If the name is omitted Apex will assign a default name
- `areaCrossSection` — The cross sectional area of the BeamShape. Area is a quantity that has units so the provided value will be interpreted using the units defined in the current ScriptUnitSystem
- `torsionalStiffness` — The torsional stiffness parameter of the BeamShape neutral axis. This quantity is unitless
- `torsionalStressCoefficient` — Coefficient used to calculate torsional stresses. The formula used to calculate torsional stress is t=CM0/J (This needs to be formatted as an equation "Tau = CMsubTheta/J) where MsubTheta is the torsional moment.
- `description` — An optional argument defining the description of the BeamShape. If omitted, the description will be blank.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeProfile1D(name: str, profile: apex.construct.Profile1D, segmentThicknesses: {int:float}, description: str = "") -> BeamShape1DProfile`
Creates a BeamShape1DProfile and adds it to the catalog.

- `name` — The name of the BeamShape1DProfile. If the name is omitted Apex will assign a default name
- `profile` — The 1DProfile that defines the mid-plane of the BeamShape
- `segmentThicknesses` — A Dictionary defining the thickness of each segment of the 1DProfile. The dictionary keys are the segment ID (int) and the values are the segment thickness (float). Segments that do not have assigned thicknesses will return null thickness values Thickness value have units of Length The dictionary keys are the segment ID (int) and the values are the segment thickness (float). Segments that do not have assigned thicknesses will return null thickness values Thickness value have units of Length
- `description` — An optional description for the BeamShape1DProfile.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeSolidHexagon(name: str, offset: float, width: float, height: float) -> apex.attribute.BeamShapeSolidHexagon`
Create a new Solid Hexagon BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `offset` — of the new BeamShape.
- `width` — of the new BeamShape.
- `height` — of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeSolidRectangle(name: str, width: float, height: float) -> apex.attribute.BeamShapeSolidRectangle`
Create a new Shape Solid Rectangle BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `width` — of the new BeamShape.
- `height` — of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeSolidRound(name: str, radius: float) -> apex.attribute.BeamShapeSolidRound`
Create a new Solid Round BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `radius` — of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeT(name: str, overallWidth: float, overallHeight: float, baseThickness: float, sparThickness: float) -> BeamShapeT`
Create a new T BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `baseThickness` — thickness of the new BeamShape.
- `sparThickness` — thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeTInverted(name: str, overallWidth: float, overallHeight: float, baseThickness: float, sparThickness: float) -> BeamShapeTInverted`
Create a new T Inverted BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallWidth` — width of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `baseThickness` — thickness of the new BeamShape.
- `sparThickness` — thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeTSideways(name: str, overallHeight: float, sparLength: float, baseThickness: float, sparThickness: float) -> BeamShapeTSideways`
Create a new T Sideways BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `overallHeight` — height of the new BeamShape.
- `sparLength` — length of the new BeamShape.
- `baseThickness` — thickness of the new BeamShape.
- `sparThickness` — thickness of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeU(name: str, flangeThickness: float, webThickness: float, overallHeight: float, overallWidth: float) -> BeamShapeU`
Create a new U BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `flangeThickness` — thickness of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.
- `overallHeight` — height of the new BeamShape.
- `overallWidth` — width of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamShapeZ(name: str, flangeExtension: float, webThickness: float, flangeSeparation: float, overallHeight: float) -> BeamShapeZ`
Create a new Z BeamShape.

- `name` — of the new BeamShape. default = "" (auto-named)
- `flangeExtension` — extension of the new BeamShape.
- `webThickness` — thickness of the new BeamShape.
- `flangeSeparation` — separation of the new BeamShape.
- `overallHeight` — height of the new BeamShape.

Returns: the created BeamShape

### `apex.attribute.createBeamSpanFree(name: str, beamTarget: apex.geometry.EdgeCollection, shapeEndA: BeamShape = None, shapeEndB: BeamShape = None, shapeEndA_orientation: float = NAN, shapeEndB_orientation: float = NAN, shapeEndA_offset1: float = 0.0, shapeEndA_offset2: float = 0.0, shapeEndB_offset1: float = 0.0, shapeEndB_offset2: float = 0.0, positionShearCenter: bool = False, material: apex.attribute.Material = None) -> BeamSpanCollection`
Creates one or more free standing BeamSpans using geometry support Edges, BeamShapes, offset and orientation data and retunrs the spans in a BeamSpanCollection. The orientation and offset of a free standing span are defined independently of any other object. This method defines the orientation of the BeamShape by defining an orientation angle about the BeamSpan axis. To define the orientation of the BeamShape using vectors use the alternative "createBeamSpanFreeByVector()" method For stiffener spans, the orientation and offset of the span is determined automatically using the BeamShapes, and a reference plate. To create a stiffener type span use the createBeamSpanStiffener() method.

- `name` — The name of the BeamSpan. If the name is omitted Apex will assign a default name
- `beamTarget` — The geometry Edges that support the BeamSpans. One BeamSpan will be created for each Edge in the target EdgeCollection and all BeamSpans will use the same shapes and properties
- `shapeEndA` — The BeamShape that will be used at the first end of the support edge
- `shapeEndB` — The BeamShape that will be used at the second end of the support edge. If this shape is omitted the shape assigned to the first end will be used. BeamShapes must be compatible between the two ends, The Shape types must be the same Numeric (Beam, Bar, Rod)Standard (The same standard shape must be used on both ends although the shape dimensions be different)Profile1D - The number of segments and vertices must be the same on both profiles
- `shapeEndA_orientation` — An Orientation defining the rotation of the BeamShape axes relative to the Span axes at EndA of the Span. BeamSpans support a rectangular axis system at each End (and in fact at any intermediate location along the length) of the support Edge. The origin of the axis system lies on the Vertex at the end of the support Edge and one axis is defined to be tangential to the support Edge at the end vertex. The other two axes lie in a plane that is perpendicular to the first axis (perpendicular to the tangent at the end of the Edge). The precise direction of these two axes is inherited from the underlying geometry Edge.This argument defines the orientation of the shape axis about the Span axis. A Value of 0.0 will align the BeamShape axis with the BeamSpan axis (and thereby the underlying Edge) axis.The orientation supports units and is a measure Angle
- `shapeEndB_orientation` — An Orientation defining the rotation of the BeamShape axes relative to the Span axes at EndB of the Span. BeamSpans support a rectangular axis system at each End (and in fact at any intermediate location along the length) of the support Edge. The origin of the axis system lies on the Vertex at the end of the support Edge and one axis is defined to be tangential to the support Edge at the end vertex. The other two axes lie in a plane that is perpendicular to the first axis (perpendicular to the tangent at the end of the Edge). The precise direction of these two axes is inherited from the underlying geometry Edge.This argument defines the orientation of the shape axis about the Span axis. A Value of 0.0 will align the BeamShape axis with the BeamSpan axis (and thereby the underlying Edge) axis.The orientation supports units and is a measure Angle
- `shapeEndA_offset1` — The offset of the BeamShape centroid from the support Edge in the "1" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `shapeEndA_offset2` — The offset of the BeamShape centroid from the support Edge in the "2" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `shapeEndB_offset1` — The offset of the BeamShape centroid from the support Edge in the "1" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `shapeEndB_offset2` — The offset of the BeamShape centroid from the support Edge in the "2" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `positionShearCenter` — An optional parameter (default = False) that causes the supplied offset values to position the shear center of the BeamShape relative to the support Edge. This option is ignored if the BeamSpan is being defined using BeamShapeProfile1D beam shapes. If omitted or set to False, the supplied offset values will be used to position the centroid of the BeamShape relative to the support Edge
- `material` — The Material that will be used at the span

Returns: the created BeamSpan collection

### `apex.attribute.createBeamSpanFreeByVector(name: str, beamTarget: apex.geometry.EdgeCollection, shapeEndA: BeamShape = None, shapeEndB: BeamShape = None, shapeEndA_direction1: apex.construct.Vector3D = None, shapeEndA_direction2: apex.construct.Vector3D = None, shapeEndB_direction1: apex.construct.Vector3D = None, shapeEndB_direction2: apex.construct.Vector3D = None, shapeEndA_offset1: float = 0.0, shapeEndA_offset2: float = 0.0, shapeEndB_offset1: float = 0.0, shapeEndB_offset2: float = 0.0, positionShearCenter: bool = False, material: apex.attribute.Material = None) -> BeamSpanCollection`
Creates one or more free standing BeamSpans using geometry support Edges, BeamShapes, offset and orientation data. The orientation and offset of a free standing span are defined independently of any other object. This method uses vectors to define the orientation of the BeamShape axes. use the alternative "createBeamSpanFree_ByVector()" method to define the BeamShape using Orientations relative to the support edge axes. For stiffener spans, the orientation and offset of the span is determined automatically using the BeamShapes, and a reference plate. To create a stiffener type span use the createBeamSpanStiffener() method.

- `name` — The name of the BeamSpan. If the name is omitted Apex will assign a default name
- `beamTarget` — The geometry Edges that support the BeamSpans. One BeamSpan will be created for each Edge in the target EdgeCollection and all BeamSpans will use the same shapes and properties
- `shapeEndA` — The BeamShape that will be used at the first end of the support edge
- `shapeEndB` — The BeamShape that will be used at the second end of the support edge. If this shape is omitted the shape assigned to the first end will be used. BeamShapes must be compatible between the two ends, The Shape types must be the same Numeric (Beam, Bar, Rod)Standard (The same standard shape must be used on both ends although the shape dimensions be different)Profile1D - The number of segments and vertices must be the same on both profiles
- `shapeEndA_direction1` — A vector defining the desired orientation of the "1" axis of the "End A" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End A, it will be projected onto that plane and the projected vector will be used. If omitted, but shapeEndA_direction2 is provided, the system will orient the shape using shapeEndA_direction2. If both the direction 1 and direction 2 arguments are omitted the system will orient the shape automatically.
- `shapeEndA_direction2` — A vector defining the desired orientation of the "2" axis of the "End A" BeamShape. If this vector does not lie in the plane that is perpendicular to the tangent at End A, it will be projected onto that plane and the projected vector will be used. This argument will be silently ignored if shapeEndA_direction1 is defined. If both the direction 1 and direction 2 arguments are omitted the system will orient the shape automatically.
- `shapeEndB_direction1` — A vector defining the desired orientation of the "1" axis of the "End B" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End A, it will be projected onto that plane and the projected vector will be used If omitted, but shapeEndB_direction2 is provided, the system will orient the shape using shapeEndB_direction2. If both the direction 1 and direction 2 arguments are omitted the system will orient the shape automatically.
- `shapeEndB_direction2` — A vector defining the desired orientation of the "2" axis of the "End B" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End B, it will be projected onto that plane and the projected vector will be used This argument will be silently ignored if shapeEndB_direction1 is defined. If both the direction 1 and direction 2 arguments are omitted the system will orient the shape automatically.
- `shapeEndA_offset1` — The offset of the BeamShape centroid from the support Edge in the "1" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `shapeEndA_offset2` — The offset of the BeamShape centroid from the support Edge in the "2" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `shapeEndB_offset1` — The offset of the BeamShape centroid from the support Edge in the "1" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `shapeEndB_offset2` — The offset of the BeamShape centroid from the support Edge in the "2" direction of the BeamShape orientation. If 'positionShearCenter = True, the supplied offsets will offset the shear center instead of the centroid.
- `positionShearCenter` — An optional parameter (default = False) that causes the supplied offset values to position the shear center of the BeamShape relative to the support Edge. If omitted or set to False, the supplied offset values will be used to position the centroid of the BeamShape relative to the support Edge. This option is ignored if the BeamSpan is being defined using BeamShapeProfile1D beam shapes.
- `material` — The Material that will be used at the span

Returns: the created BeamSpan collection

### `apex.attribute.createBeamSpanStiffener(name: str, shapeEndA: BeamShape, shapeEndB: BeamShape, beamTarget: apex.geometry.EdgeCollection, plateTarget: apex.geometry.FaceCollection, shapeMatingDirection: apex.attribute.ShapeMatingSide = apex.attribute.ShapeMatingSide.XPositive, plateSide: apex.attribute.TopBottom = apex.attribute.TopBottom.Top, shapeEndA_offset1: float = NAN, shapeEndA_offset2: float = NAN, shapeEndB_offset1: float = NAN, shapeEndB_offset2: float = NAN, shapeBoundaryDistanceA: float = NAN, shapeBoundaryDistanceB: float = NAN, material: apex.attribute.Material = None) -> BeamSpanCollection`
Creates one or more Stiffener BeamSpans using geometry support Edges, plate orientation Faces and one or two BeamShapes. The orientation and offset of the stiffener span is determined automatically using the reference Face whereas the orientation and offset of a free standing span are defined independently of any other object and must be supplied by the user. To create a free standing type span use the createBeamSpanFree() method.

- `name` — The name of the BeamSpan. If the name is omitted Apex will assign a default name
- `shapeEndA` — The BeamShape that will be used at the first end of the support edge
- `shapeEndB` — The BeamShape that will be used at the second end of the support edge. If this shape is omitted the shape assigned to the first end will be used. BeamShapes must be compatible between the two ends, The Shape types must be the same Numeric (Beam, Bar, Rod)Standard (The same standard shape must be used on both ends although the shape dimensions be different)Profile1D - The number of segments and vertices must be the same on both profiles
- `beamTarget` — The geometry Edges that support the BeamSpans. One BeamSpan will be created for each Edge in the target EdgeCollection and all BeamSpans will use the same shapes and properties
- `plateTarget` — The geometry Faces that represent the plate that the span will stiffen. These Faces will be used in conjunction with the BeamShapes and support Edges to automatically determine the offset and orientation of the BeamShape
- `shapeMatingDirection` — A parameter, using an enumeration, which defines which side of the beam shape touches the plate. the default value is XPositive All BeamShapes can be considered 2D planar representations of the beam cross section. The cross section is define in a "1-2" axis system and the section properties (I11, I22 etc.)are defined relative to this axis system.When a Beam is used as a stiffener, it it is necessary to define how it should be oriented relative to the plate that it is stiffening - for example should the top flange face of the "T" or the bottom edge of the web be touching the plate.The parameter value, YPositive will cause the top flange face of the "T" to touch the plate.
- `plateSide` — An optional parameter that defines, using an enumeration, which side of the plate Face the stiffener will be positioned on. The default value ("Top") will cause the span to positioned on the positive normal side of the Face.
- `shapeEndA_offset1` — of the new BeamSpan
- `shapeEndA_offset2` — of the new BeamSpan
- `shapeEndB_offset1` — of the new BeamSpan
- `shapeEndB_offset2` — of the new BeamSpan
- `shapeBoundaryDistanceA` — the boundary distance of shape A
- `shapeBoundaryDistanceB` — the boundary distance of shape B
- `material` — The Material that will be used at the span

Returns: the created BeamSpan collection

### `apex.attribute.createBolt3DByCrossSectionAutomatic(name: str = "#####", description: str = "#####", id: int = 0, boltBody: apex.Entity = None, crossSectionOffset: float = NAN, controlNodeDefinitionMethod: apex.attribute.ControlNodeDefinitionMethod = apex.attribute.ControlNodeDefinitionMethod.Mid, controlNode: apex.mesh.Node = None, scaleOfOffset: float = 0.1) -> apex.attribute.Bolt3D`
Create 3D bolt with the cross section method = automatic.

- `name` — Optional- name of the bolt
- `description` — Optional- description of the bolt
- `id` — Optional - id of the bolt
- `boltBody` — Body to represent the 3D bolt. It can be a geometry body, mesh body, or a group of geometry body, mesh body.
- `crossSectionOffset` — Optional-Cross section offset of the bolt.
- `controlNodeDefinitionMethod` — Control node definition method.
- `controlNode` — Control node of the bolt. It is only available when controlNodeDefinitionMethod = User.
- `scaleOfOffset` — The scale used to determine the offset value from top or bottom. The offset = scale*Bolt Length. It is only available when controlNodeDefinitionMethod = OffsetFromTop or OffsetFromBottom.

### `apex.attribute.createBolt3DByCrossSectionManual(name: str = "#####", description: str = "#####", id: int = 0, crossSectionElements: apex.EntityCollection = None, crossSectionNodes: apex.EntityCollection = None, boltAxisOrientation: apex.construct.Vector3D = None, crossSectionFaces: apex.EntityCollection = None, controlNodeDefinitionMethod: apex.attribute.ControlNodeDefinitionMethod = apex.attribute.ControlNodeDefinitionMethod.Mid, controlNode: apex.mesh.Node = None) -> apex.attribute.Bolt3D`
Create 3D bolt with the cross section method = Manual.

- `name` — Optional- name of the bolt
- `description` — Optional- description of the bolt
- `id` — Optional - id of the bolt
- `crossSectionElements` — Cross section elements opposites to bolt axis orientation. It can be elements or a group of elements. Omits it if argument crossSectionFaces is defined.
- `crossSectionNodes` — Nodes of the cross section of bolt. It can be elements or a group of nodes, if the cross section elements are defined by group, cross section nodes should be a group of node. Omits it if argument crossSectionFaces is defined.
- `boltAxisOrientation` — Bolt axis orientation with a 3D vector.
- `crossSectionFaces` — Cross section Faces to detect cross section elements and nodes. If it is defined, the arguments of crossSectionElements and crossSectionNodes are skipped.
- `controlNodeDefinitionMethod` — Control node definition method
- `controlNode` — Control node of the bolt. It is only available when controlNodeDefinitionMethod = User.

### `apex.attribute.createBolts3DByCrossSectionAutomatic(name: str = "#####", description: str = "#####", id: int = 0, targets: apex.EntityCollection = None, crossSectionOffset: float = NAN, controlNodeDefinitionMethod: apex.attribute.ControlNodeDefinitionMethod = apex.attribute.ControlNodeDefinitionMethod.Mid, scaleOfOffset: float = 0.1) -> apex.attribute.Bolt3DCollection`
Create multiple 3D bolts with the cross section method = automatic by input multiple bodies.

- `name` — Optional- name prefix of the bolts to be created.
- `description` — Optional- description of the bolts
- `id` — Optional - start id of the bolts
- `targets` — A collection of target entities such as geometry body, mesh body or group to represent as bolt body. The system will create bolt per each body.
- `crossSectionOffset` — Optional-Cross section offset of the bolts.
- `controlNodeDefinitionMethod` — Control node definition method. If ControlNodeDefinitionMethod = User, return error.
- `scaleOfOffset` — The scale used to determine the offset value from top or bottom. The offset = scale*Bolt Length. It is only available when controlNodeDefinitionMethod = OffsetFromTop or OffsetFromBottom.

### `apex.attribute.createBushingRepProperties(translationalStiffnessX: float = NAN, translationalStiffnessY: float = NAN, translationalStiffnessZ: float = NAN, rotationalStiffnessX: float = NAN, rotationalStiffnessY: float = NAN, rotationalStiffnessZ: float = NAN, translationalDampingX: float = NAN, translationalDampingY: float = NAN, translationalDampingZ: float = NAN, rotationalDampingX: float = NAN, rotationalDampingY: float = NAN, rotationalDampingZ: float = NAN, translationalStructuralDampingX: float = NAN, translationalStructuralDampingY: float = NAN, translationalStructuralDampingZ: float = NAN, rotationalStructuralDampingX: float = NAN, rotationalStructuralDampingY: float = NAN, rotationalStructuralDampingZ: float = NAN, translationalStressRecovery: float = NAN, rotationalStressRecovery: float = NAN, translationalStrainRecovery: float = NAN, rotationalStrainRecovery: float = NAN, mass: float = NAN, thermalExpansionCoefficient: float = NAN, referenceTemperature: float = NAN, lengthOfCoincidentGrids: float = NAN, embedded: bool = True, name: str = "", description: str = "", id: int = 0) -> apex.attribute.BushingRepProperties`
Creates BushingRepProperties.

- `translationalStiffnessX` — The translationalStiffness in the connector X direction.
- `translationalStiffnessY` — The translationalStiffness in Y direction
- `translationalStiffnessZ` — The translationalStiffness in Z direction.
- `rotationalStiffnessX` — The rotationalStiffness in X direction.
- `rotationalStiffnessY` — The rotationalStiffness in Y direction.
- `rotationalStiffnessZ` — The rotationalStiffness in Z direction.
- `translationalDampingX` — The translationalDamping in X direction.
- `translationalDampingY` — The translationalDamping in Y direction.
- `translationalDampingZ` — The translationalDamping in Z direction.
- `rotationalDampingX` — The rotationalDamping in X direction.
- `rotationalDampingY` — The rotationalDamping in Y direction.
- `rotationalDampingZ` — The rotationalDamping in Z direction.
- `translationalStructuralDampingX` — Optional argument to define translational Structural Damping in connector X direction.
- `translationalStructuralDampingY` — Optional argument to define translational Structural Damping in connector Y direction.
- `translationalStructuralDampingZ` — Optional argument to define translational Structural Damping in connector Z direction.
- `rotationalStructuralDampingX` — Optional argument to define rotational Structural Damping in connector X direction.
- `rotationalStructuralDampingY` — Optional argument to define rotational Structural Damping in connector Y direction.
- `rotationalStructuralDampingZ` — Optional argument to define rotational Structural Damping in connector Z direction.
- `translationalStressRecovery` — Optional argument to define translational stress recovery coefficient.
- `rotationalStressRecovery` — Optional argument to define rotational stress recovery coefficient.
- `translationalStrainRecovery` — Optional argument to define translational strain recovery coefficient.
- `rotationalStrainRecovery` — Optional argument to define rotational strain recovery coefficient.
- `mass` — Optional argument to define lumped mass.
- `thermalExpansionCoefficient` — Optional argument to define the thermal expansion coefficient.
- `referenceTemperature` — Optional argument to define reference temperature.
- `lengthOfCoincidentGrids` — Optional argument to define the length for coincident grids.
- `embedded` — Optional argument to define embedded.
- `name` — Optional argument to define name.
- `description` — Optional argument to define description.
- `id` — Optional argument to define id.

Returns: the created BushingRepProperties

### `apex.attribute.createConnector(name: str, connectorProperties: ConnectorProperty, applicationMethod1: ApplicationMethod, applicationMethod2: ApplicationMethod, connectorType: ConnectorType = apex.attribute.ConnectorType.Undefined, end1InterfacePoint: apex.Coordinate = 0, end2InterfacePoint: apex.Coordinate = 0, end1AttachmentRegion: apex.EntityCollection = 0, end1DistributionMethod: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, end2AttachmentRegion: apex.EntityCollection = 0, end2DistributionMethod: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, orientation: apex.construct.Orientation = None, description: str = "") -> Connector`
Create a new Connector. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Instead use createConnectorDiscrete()

- `name` — of the Connector. default = "" (auto-named)
- `connectorProperties` — of the Connector.
- `applicationMethod1` — of the Connector - the application method (Direct or Remote).
- `applicationMethod2` — of the Connector - the application method (Direct or Remote).
- `connectorType` — of the Connector.
- `end1InterfacePoint` — the first end location of the Connector object Optional - could be None if applicationMethod1 is Direct.
- `end2InterfacePoint` — the second end location of the Connector object Optional - could be None if applicationMethod2 is Direct.
- `end1AttachmentRegion` — Optional - the attachment region used for the remote method.
- `end1DistributionMethod` — Optional - the distribution type (rigid or compliant).
- `end2AttachmentRegion` — Optional - the attachment region used for the remote method.
- `end2DistributionMethod` — Optional - the distribution type (rigid or compliant).
- `orientation` — Optional - the orientation relative to the global coordinate system.
- `description` — Optional - the description.

Returns: the created Connector

### `apex.attribute.createConnectorDiscrete(name: str, connectorProperties: ConnectorDiscreteProperty, applicationMethod1: ApplicationMethod = apex.attribute.ApplicationMethod.Direct, applicationMethod2: ApplicationMethod = apex.attribute.ApplicationMethod.Direct, end1InterfacePoint: apex.Coordinate = None, end2InterfacePoint: apex.Coordinate = None, end1AttachmentRegion: apex.EntityCollection = None, end1DistributionMethod: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, end2AttachmentRegion: apex.EntityCollection = None, end2DistributionMethod: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, orientation: apex.construct.Orientation = None, orientationByLocation: apex.ILocation = None, orientationByVector: apex.construct.Vector3D = None, locationParametric: float = NAN, locationOffsetCoordinateSystem: apex.construct.CoordinateSystem = None, locationOffsetCoordinates: apex.ILocation = None, description: str = "", end1DOF: str = "1", end2DOF: str = "1", end1IndependentDOF: str = "123456", end1DependentDOF: str = "", end2IndependentDOF: str = "", end2DependentDOF: str = "123456", piercingNodeForPatchA: apex.Coordinate = None, piercingNodeForPatchB: apex.Coordinate = None, masterNodeForPatches: apex.Coordinate = None, masterLocationForPatches: apex.ILocation = None, createTypeForFastener: apex.attribute.createTypeForFastener = apex.attribute.createTypeForFastener.Undefined, id: int = 0) -> ConnectorDiscrete`
Creates a new connector.

- `name` — The name of the Connector. default = "" (auto-named)
- `connectorProperties` — of the connector.
- `applicationMethod1` — ApplicationMethod1 of the Connector - the application method (Direct or Remote).
- `applicationMethod2` — ApplicationMethod2 of the Connector - the application method (Direct or Remote).
- `end1InterfacePoint` — the first end location of the Connector object Optional - could be None if applicationMethod1 is Direct.
- `end2InterfacePoint` — the second end location of the Connector object Optional - could be None if applicationMethod2 is Direct.
- `end1AttachmentRegion` — Optional - the attachment region used for the remote method.
- `end1DistributionMethod` — Optional - the distribution type (rigid or compliant).
- `end2AttachmentRegion` — Optional - the attachment region used for the remote method.
- `end2DistributionMethod` — Optional - the distribution type (rigid or compliant).
- `orientation` — Optional - the orientation relative to the global coordinate system. If orientation is provided, other 2 arguments "orientationByLocation" and "orientationByVector" will be silently ignored. If all 3 types of orientation methods are provided, the priority is: orientation>orientationByVector>orientationByLocation.
- `orientationByLocation` — Optional - Location used to define the orientation of bushing (from 1st and to this location).
- `orientationByVector` — Optional - Vector used to define the orientation of bushing
- `locationParametric` — Optional - parametric value indicates the location of bushing along the line between 1st and 2nd ends.
- `locationOffsetCoordinateSystem` — Optional - offset coordinate system used to define the location of bushing.
- `locationOffsetCoordinates` — Optional - the location in the offset coordinate system.
- `description` — Optional - the description.
- `end1DOF` — Optional - degree of freedom for the first end of spring or damper, it could be one of "1,2,3,4,5,6". It is also used for grounded spring or damper.
- `end2DOF` — Optional - degree of freedom for the second end of spring or damper, it could be one of "1,2,3,4,5,6".
- `end1IndependentDOF` — Optional - independent DOF at end 1 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `end1DependentDOF` — Optional - Dependent DOF at end 1 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `end2IndependentDOF` — Optional - independent DOF at end 2 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `end2DependentDOF` — Optional - dependent DOF at end 2 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `piercingNodeForPatchA` — Argument of piercing point for patch A.
- `piercingNodeForPatchB` — Argument of piercing location for patch B.
- `masterNodeForPatches` — Argument of location of master node for two patches.
- `masterLocationForPatches` — Argument of master location for patches.
- `createTypeForFastener` — Indicate the creation type as one of the enumerations: "ByElement" or "ByProperty".
- `id` — Optional - id of the created connector.

Returns: the created ConnectorDiscrete

### `apex.attribute.createConnectorProperties(stiffness: float = NAN, damping: float = NAN, translationalStiffnessX: float = NAN, translationalStiffnessY: float = NAN, translationalStiffnessZ: float = NAN, rotationalStiffnessX: float = NAN, rotationalStiffnessY: float = NAN, rotationalStiffnessZ: float = NAN, translationalDampingX: float = NAN, translationalDampingY: float = NAN, translationalDampingZ: float = NAN, rotationalDampingX: float = NAN, rotationalDampingY: float = NAN, rotationalDampingZ: float = NAN, diameter: float = NAN, linkMaterial: Material = None) -> ConnectorProperty`
Create a new ConnectorProperty THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Instead use createBushingRepProperties(),createDamper1DRepProperties(),createFlexibleLinkRepProperties(),createGapRepProperties(),createRigidLinkRepProperties(),createSpring1DRepProperties(),createSpringDamper1DRepProperties().

- `stiffness` — of the Connector.
- `damping` — of the Connector.
- `translationalStiffnessX` — of the Connector.
- `translationalStiffnessY` — of the Connector.
- `translationalStiffnessZ` — of the Connector.
- `rotationalStiffnessX` — of the Connector.
- `rotationalStiffnessY` — of the Connector.
- `rotationalStiffnessZ` — of the Connector.
- `translationalDampingX` — of the Connector.
- `translationalDampingY` — of the Connector.
- `translationalDampingZ` — of the Connector.
- `rotationalDampingX` — of the Connector.
- `rotationalDampingY` — of the Connector.
- `rotationalDampingZ` — of the Connector.
- `diameter` — of the Connector.
- `linkMaterial` — of the Connector.

Returns: the created ConnectorProperty

### `apex.attribute.createContactBody(name: str, description: str, id: int, bodyType: apex.attribute.ContactBodyType, target: apex.EntityCollection, bodyProperty: apex.attribute.ContactBodyProperty, contactResultCalculation: apex.attribute.ContactResultCalculation) -> apex.attribute.ContactBody`
Creates and returns an contact body.

- `name` — Optional name for the contact body.
- `description` — Optional string providing a description for the contact body.
- `id` — ID of the contact body. If omits, the system will automatically assign an ID.
- `bodyType` — Defines if the body is rigid or deformable.
- `target` — An entity collection for contact body. For deform body, the target entities can be solid body, solid cell, sheet body, solid mesh body, shell mesh body, 3D elements, 2D elements, face, element face and 2D/3D element property. For rigid body, the target entities can be solid body, sheet body, curve body, shell mesh body, curve mesh body.
- `bodyProperty` — Contact body properties. If omits, the default contact body properties will be used.
- `contactResultCalculation` — Optional-calculate the global resultant contact force/moment in Origin or Estimated centroid. Omits it if body type is not deform.

### `apex.attribute.createContactBodyProperty(smoothingState: bool, smoothingFeatureAngle: float, projectMidNode: bool, shellLayer: apex.attribute.ShellLayer, ignoreShellThickness: bool, discontinuityDefinition: apex.attribute.DiscontinuityDefinition, discontinuityTarget: apex.EntityCollection) -> apex.attribute.ContactBodyProperty`
Creates and returns an contact body properties.

- `smoothingState` — Optional - enable to control geometric smoothing of boundary of deformable body.Omits it if it is not a deform body.
- `smoothingFeatureAngle` — Optional - Angle to detect feature edges. Edges between Elements with face normal deviation equal to or larger will be detected as an edge feature, and not be smoothed. It is used when DiscontinuityDefinition = Auto and smoothinStage is true.
- `projectMidNode` — Optional - The mid-side grid of quadratic elements are projected onto the selected spline surfaces. Ignored if smoothing is false.
- `shellLayer` — - Optional-Shell layer to be used for contact detection.
- `ignoreShellThickness` — - Optional- Consider or ignore shell thickness during detection of contact.
- `discontinuityDefinition` — - Optional- Discontinuity Definition for smoothing. It is used when smoothingStage is true.
- `discontinuityTarget` — - Optional- the target discontinuities entities for smoothing. It can be geometry edge or element edge. It is used when DiscontinuityDefinition = Manual and smoothingStage is true.

### `apex.attribute.createContactTable(name: str, description: str, id: int, interactions: InteractionCollection) -> apex.attribute.ContactTable`
Creates and returns a contact table.

- `name` — Optional name for the ContactTabl.
- `description` — Optional string providing a description for the ContactTabl.
- `id` — ID of the ContactTabl. If omits, the system will automatically assign an ID.
- `interactions` — A collection of interactions for the contact table(BCTABL1).

### `apex.attribute.createDAMPING(name: str, description: str, id: int, structuralDampingCoefficient: float, massScaleFactor: float, stiffnessScaleFactor: float, hybridDamping: int, materialDampingScaleFactor: float, removeRotorStiffnessMassStructuralDamping: str, structuralDampingFrequency: float, materialDampingFrequency: float, hybridStructuralDampingFrequency: float) -> apex.catalog.DAMPING`
create DAMPING object

- `name` — name of DAMPING
- `description` — description of DAMPING
- `id` — id of DAMPING
- `structuralDampingCoefficient` — Structural damping coefficient
- `massScaleFactor` — Scale factor for mass portion of Rayleigh damping
- `stiffnessScaleFactor` — Scale factor for stiffness portion of Rayleigh damping
- `hybridDamping` — ID of HYBDAMP entry for hybrid damping
- `materialDampingScaleFactor` — Scale factor for material damping
- `removeRotorStiffnessMassStructuralDamping` — Remove rotor stiffness, mass, and structural damping from the hybrid damping calculation (Character: YES or NO; Default=YES)
- `structuralDampingFrequency` — Average frequency for calculation of structural damping in transient response.(Real ≥ 0.0; Default = 0.0)
- `materialDampingFrequency` — Average frequency for calculation of material damping in transient response.(Real ≥ 0.0; Default = 0.0)
- `hybridStructuralDampingFrequency` — Average frequency for calculation of hybrid structural damping in transient response.(Real ≥ 0.0; Default = 0.0)

### `apex.attribute.createDamper1DRepProperties(damping: float = NAN, embedded: bool = True, name: str = "", description: str = "", id: int = 0) -> Damper1DRepProperties`
Creates Damper1DRepProperties.

- `damping` — The damping of the Damper1D connector.
- `embedded` — Optional argument to define embedded.
- `name` — Optional argument to define name.
- `description` — Optional argument to define description.
- `id` — Optional argument to define id.

Returns: the created Damper1DRepProperties

### `apex.attribute.createDiscreteFEMField(name: str, type: apex.attribute.DiscreteFEMFieldType, fieldValues: {str:{dict}}) -> apex.attribute.DiscreteFEMField`
Creates and returns one DiscreteFEMField.

- `name` — Name prefix of the fields that will be created. If more than one field is created each field will be named using the prefix plus an appended integer to ensure name uniqueness.
- `type` — the type of field, include DiscreteThicknessField, DiscreteOffsetField, DiscreteAngleField, DiscreteCoordinateSystemField
- `fieldValues` — the value of discrete. Example : fieldValues_= { "Model/Part 1/Mesh 1": { 'element_ids' : [1,2,3,4,5], 'values' : [-55.,22.,2.,3.,4.]} }

Returns: the created field

### `apex.attribute.createDisplacementConstraintProperties(constrainTranslationX: bool, constrainTranslationY: bool, constrainTranslationZ: bool, constrainRotationX: bool, constrainRotationY: bool, constrainRotationZ: bool) -> DisplacementConstraintProperty`
Create a new DisplacementConstraintProperty. THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with the function: createConstraintDisplacement().

- `constrainTranslationX` — of the DisplacementConstraintProperty.
- `constrainTranslationY` — of the DisplacementConstraintProperty.
- `constrainTranslationZ` — of the DisplacementConstraintProperty.
- `constrainRotationX` — of the DisplacementConstraintProperty.
- `constrainRotationY` — of the DisplacementConstraintProperty.
- `constrainRotationZ` — of the DisplacementConstraintProperty.

Returns: the created ConnectorProperty

### `apex.attribute.createEIGB(name: str, description: str, id: int, eigenvalueExtractionMethod: str, lowerFrequencyBound: float, upperFrequencyBound: float, estimateNumberOfRoots: int, desiredNumberOfPositiveRoots: int, desiredNumberOfNegativeRoots: int, normalizingEigenvectorsMethod: str, nodeId: int, componentNumber: int) -> apex.catalog.EIGB`
create EIGB object

- `name` — name of EIGB
- `description` — description of EIGB
- `id` — id of EIGB
- `eigenvalueExtractionMethod` — String to define Method of eigenvalue extraction. (Character: "INV" for inverse power method or "SINV" for enhanced inverse power method.)
- `lowerFrequencyBound` — L1: Lower Frequency Bound, Real ≥ 0.0.
- `upperFrequencyBound` — L2: Upper Frequency Bound, Real ≥ 0.0.
- `estimateNumberOfRoots` — NEP: Estimate of number of roots, Integer > 0
- `desiredNumberOfNegativeRoots` — NDN: Desired number of roots, Integer > 0
- `normalizingEigenvectorsMethod` — String to define Method for normalizing eigenvectors. (Character: "MAX" or "POINT"; Default ="MAX")
- `nodeId` — G: Required only if NORM = "POINT".(Integer > 0)
- `componentNumber` — C: Component number. Required only if NORM = "POINT" and G is a geometric grid point. (1≤Integer ≤6)

### `apex.attribute.createEIGR(name: str, description: str, id: int, eigenvalueExtractionMethod: str, lowerFrequencyBound: float, upperFrequencyBound: float, estimateNumberOfRoots: int, desiredNumberOfRoots: int, normalizingEigenvectorsMethod: str, nodeId: int, componentNumber: int) -> apex.catalog.EIGR`
create EIGR object

- `name` — name of EIGR
- `description` — description of EIGR
- `id` — id of EIGR
- `eigenvalueExtractionMethod` — String to define extraction method. Modern Methods: LAN: Lanczos Method AHOU: Automatic selection of HOU or MHOU method. Obsolete Methods: INV: Inverse Power method. SINV: Inverse Power method with enhancements. GIV: Givens method of tridiagonalization. MGIV: Modified Givens method. HOU: Householder method of tridiagonalization. MHOU: Modified Householder method. AGIV: Automatic selection of METHOD = "GIV" or "MGIV".
- `lowerFrequencyBound` — F1: Lower Frequency Bound, Real ≥ 0.0.
- `upperFrequencyBound` — F2: Upper Frequency Bound, Real ≥ 0.0.
- `estimateNumberOfRoots` — NE: Estimate of number of roots, Integer > 0
- `desiredNumberOfRoots` — ND: Desired number of roots, Integer > 0, default =3
- `normalizingEigenvectorsMethod` — String to define Method for normalizing eigenvectors. MASS: Normalize to unit value of the generalized mass(Default) MAX: Normalize to unit value of the largest component in the analysis set. POINT: Normalize to a positive or negative unit value of the component defined in fields 3 and 4.
- `nodeId` — G: Required only if NORM = "POINT".(Integer > 0)
- `componentNumber` — C: Component number. Required only if NORM = "POINT" and G is a geometric grid point. (1≤Integer≤6)

### `apex.attribute.createEIGRL(name: str, description: str, id: int, lowerFrequencyBound: float, upperFrequencyBound: float, desiredNumberOfRoots: int, diagnosticLevel: int, numberOfVectors: int, estimatefFexibleModeFrequency: float, normalizingEigenvectorsMethod: str, calculationConstant: float, requencySegmentNumber: int, frequencySegmentValue: [float]) -> apex.catalog.EIGRL`
create EIGRL object

- `name` — name of EIGRL
- `description` — description of EIGRL
- `id` — id of EIGRL
- `lowerFrequencyBound` — F1: Lower Frequency Bound, Real ≥ 0.0.
- `upperFrequencyBound` — F2: Upper Frequency Bound, Real ≥ 0.0.
- `desiredNumberOfRoots` — ND: Desired number of roots, Integer > 0, default =3
- `diagnosticLevel` — MSGLVL: Diagnostic level. (0 < Integer < 4; Default = 0)
- `numberOfVectors` — MAXSET: Number of vectors in block or set.
- `estimatefFexibleModeFrequency` — SHFSCL: Estimate of the first flexible mode natural frequency
- `normalizingEigenvectorsMethod` — String to define Method for normalizing eigenvectors. MASS: Normalize to unit value of the generalized mass. Not available for buckling analysis. (Default for normal modes analysis.) MAX: Normalize to unit value of the largest displacement in the analysis set. Displacements not in the analysis set may be larger than unity. (Default for buckling analysis.)
- `calculationConstant` — ALPH: Specifies a constant for the calculation of frequencies (Fi) at the upper boundary segments for the parallel method. (Real > 0.0; Default = 1.0)
- `requencySegmentNumber` — NUMS: Number of frequency segments for the parallel method. (Integer > 0; Default = 1)
- `frequencySegmentValue` — Fi: Frequency at the upper boundary of the i-th segment. This is a list of float value up to 15.

### `apex.attribute.createFastenerRepProperties(transverseStiffnessX: float = NAN, transverseStiffnessY: float = NAN, transverseStiffnessZ: float = NAN, rotationalStiffnessX: float = NAN, rotationalStiffnessY: float = NAN, rotationalStiffnessZ: float = NAN, mass: float = NAN, structuralDamping: float = NAN, thermalExpansionCoefficient: float = NAN, referenceTemperature: float = NAN, lengthWithCoincidentGrids: float = NAN, diameter: float = 10.0, flagOfCoordinateSystem: apex.attribute.FlagOfCoordinateSystem = apex.attribute.FlagOfCoordinateSystem.Auto, stiffnessCoordinateSystem: apex.attribute.FastenerStiffnessCoordinateSystem = apex.attribute.FastenerStiffnessCoordinateSystem.Unset, userDefinedStiffnessCoordinateSystem: apex.construct.CoordinateSystem = None, embedded: bool = True, name: str = "", description: str = "", id: int = 0) -> apex.attribute.FastenerRepProperties`
Create a fastener property.

- `transverseStiffnessX` — argument for the transverse stiffness along X direction.
- `transverseStiffnessY` — argument for the transverse stiffness along Y direction.
- `transverseStiffnessZ` — argument for the transverse stiffness along Z direction.
- `rotationalStiffnessX` — argument for the rotational stiffness about X axis
- `rotationalStiffnessY` — argument for the rotational stiffness about Y axis
- `rotationalStiffnessZ` — argument for the rotational stiffness about Z axis
- `mass` — optional argument for mass
- `structuralDamping` — Optional argument for structural damping
- `thermalExpansionCoefficient` — Optional argument for thermal expansion coefficient
- `referenceTemperature` — Optional argument for reference temperature
- `lengthWithCoincidentGrids` — Optional argument for length with coincident grids
- `diameter` — the diameter of fastener.
- `flagOfCoordinateSystem` — Optional argument for how the coordinate system is used in either "Relative" or "Absolute" way
- `stiffnessCoordinateSystem` — Optional argument indicate the element stiffness coordinate system.
- `userDefinedStiffnessCoordinateSystem` — User defined element stiffness coordinate system, which takes effect only when the argument"stiffnessCoordinateSystem" is set as "userDefined".
- `embedded` — Optional argument to indicate whether the created property is an embedded one or not, it determines whether the property will be displayed in the property list or not. the value is set as true by default if it is not provided.
- `name` — Optional argument to define name.
- `description` — Optional argument to describe the fastener property.
- `id` — optional argument for id of this fastener property, if it is not provided, system will assign one automatically.

Returns: the created FastenerRepProperties

### `apex.attribute.createFieldMaterialOrientationAlignCurve(name: str, target: apex.EntityCollection, director: apex.Entity) -> MaterialOrientationField2DAlignCurve`
Create an MaterialOrientation to a region of the model and aligns the Material axis using a director apex.geometry.Curve or apex.geometry.Edge and returns a MaterialOrientationField2DAlignCurve.

- `name` — The name of this MaterialOrientationField2DAlignCurve
- `target` — The collection of entities that the MaterialOrientationField2DCoordinate will be assigned to as an EntityCollection. Target may contain Parts, Surfaces, Faces or 2D meshes or 2D elements - all other types will be silently ignored. When Parts are included they are internally expanded to the complete set of surfaces of the apex.Part. Any duplicate entities in target are ignored
- `director` — A entity of apex.geometry.Curve and/or apex.geometry.Edge that will be used to define the Material orientation. director may include single Curve or Edge.

### `apex.attribute.createFieldMaterialOrientationFromCoordinate(name: str, target: apex.EntityCollection, materialAxis: apex.Entity) -> MaterialOrientationField2DCoordinate`
Create an MaterialOrientation to a region of the model, aligns the material axis using a apex.construct.CoordinateSystem axis and returns a MaterialOrientationField2DCoordinate.

- `name` — The name of this MaterialOrientationField2DCoordinate
- `target` — The collection of entities that the MaterialOrientationField2DCoordinate will be assigned to as an EntityCollection. Target may contain Parts, Surfaces, Faces or 2D meshes or 2D elements - all other types will be silently ignored. When Parts are included they are internally expanded to the complete set of surfaces of the apex.Part. Any duplicate entities in target are ignored
- `materialAxis` — A entity of apex.construct.CoordinateSystem that will be used to define the Material orientation.

### `apex.attribute.createFieldMidSurfaceFromSolids(targetMidsurface: apex.EntityCollection, targetSolids: apex.geometry.SolidCollection, name: str, thicknessLimit: float, groupingTolerance: float, selectionExtractionApproach: apex.attribute.SelectionExtractionApproach, createOffsets: bool) -> apex.attribute.ThicknessOffsetFieldMidsurfaceCollection`
Creates and returns one or more fields (thickness, offset) from the input Surfaces/Faces and Solids and assigns the fields to the meshes/elements associated with Surfaces/Faces. The input Surfaces must be meshed. The method assumes that the input Surface/Faces represent the mid-surface of the input Solids therefore the input Surfaces/Faces must be reasonably positioned w.r.t. the Solid mid-surface location for the method to effective although it is NOT required that the input Surfaces/Faces were created by the mid-surface tool. If None of the input Surfaces/Faces are meshed the method will throw an exception. If some of the input Surfaces/Faces are meshed Apex will attempt to create fields and assign them to those input Surfaces/Faces and will ignore any unmeshed Faces/Surfaces Several parameters to control how the thickness and offsets of the fields are created as provided as input arguments. The method returns zero or more fields in a field Collection - if no fields could be calculated, the Collection will be empty. Each field will be assigned to a collection of Elements from the input Surfaces/Faces.

- `targetMidsurface` — A collection of Surfaces/Faces, as an EntityCollection, that represents the mid-surface of the input targetSolids. The Surfaces/Faces must be meshed otherwise the method will fail. Any Surfaces in the target will be expanded internally to the set of Faces that the Surface composes and any duplicate Faces in the resulting expanded set will be silently ignored..
- `targetSolids` — a collection of Solids that represent the 3D shape that is being approximated by the combination of the targetMidsurfaces and the generated fields..
- `name` — Name prefix of the fields that will be created. If more than one field is created each field will be named using the prefix plus an appended integer to ensure name uniqueness. If omitted a default name prefix of 'AutoThick' will be used.
- `thicknessLimit` — Optional argument to specify an upper bound for the thicknesses in the fields created by this method. If omitted, no upper bound will be applied. thicknessLimit is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem.
- `groupingTolerance` — The groupingTolerance is used to merge constant thickness fields with similar thicknesses. After determining the distribution of thickness across all elements referenced by the input Surfaces and Faces the methods will merge the elements into sets such that no individual element in the set has a calculated thickness different from any other in the same set by more than this tolerance and a unique Sectiosn will be created for each set of elements groupingTolerance is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem.
- `selectionExtractionApproach` — Optional enumeration controlling whether constant or variable thickness fields will be created. If omitted, the default SelectionExtractionApproach.Automatic option will be used. Use the default SelectionExtractionApproach.Automatic option to let the system decide whether a constant or variable thickness field should be created. Use SelectionExtractionApproach.ForceConstantThickness to force creation of a constant thickness field even if the system finds a variable thickness field (The system will use the average thickness of the field for the constant thickness value in this case) Use SelectionExtractionApproach.ForceVariableThickness to force creation of variable thickness fields even if the system finds that the thickness field is constant.
- `createOffsets` — optional boolean argument that allows offsets to be included or ignored from the fields that are created. If True (default) the method will cause offsets to be included in the created fields If False the method will NOT create offsets in the fields and only the thickness will be included. Use this option carefully since it will create fields that assume the thickness is evenly distributed about the element midplane, even though the input geometry may not reflect that.

Returns: the created fields

### `apex.attribute.createFieldThicknessOffsetConstant(type: apex.attribute.DiscreteFEMFieldType, name: str, targets: apex.EntityCollection, constantValue: float) -> apex.attribute.ThicknessOffsetFieldConstant`
Creates and returns one field (thickness, offset) from the input Surfaces/Faces/Elements/Meshs/Solids/Parts and assigns the fields to the meshes/elements associated with Surfaces/Faces/Solids/Parts. The input geometry must be meshed.

- `type` — the type of field, include DiscreteThicknessField, DiscreteOffsetField
- `name` — Name prefix of the fields that will be created. If more than one field is created each field will be named using the prefix plus an appended integer to ensure name uniqueness.
- `targets` — a collection of Surfaces/Faces/Elements/Meshs/Solids/Parts..
- `constantValue` — the constant value of fields(thickness, offset)

Returns: the created field

### `apex.attribute.createFlexibleLinkRepProperties(diameter: float = NAN, linkMaterial: Material = None) -> apex.attribute.FlexibleLinkRepProperties`
Creates FlexibleLinkRepProperties.

- `diameter` — The diameter of the FlexibleLink connector.
- `linkMaterial` — The material assigned to the FlexibleLink connector.

Returns: the created FlexibleLinkRepProperties

### `apex.attribute.createGapRepProperties(initialOpening: float = NAN, preload: float = NAN, closedStiffness: float = NAN, openStiffness: float = NAN, transverseStiffness: float = NAN, staticFriction: float = NAN, kineticFriction: float = NAN) -> apex.attribute.GapRepProperties`
Creates GapRepProperties.

- `initialOpening` — The optional initial gap opening.
- `preload` — The preload applied on the gap connector.
- `closedStiffness` — The axial stiffness for the closed gap.
- `openStiffness` — the axial stiffness for the open gap.
- `transverseStiffness` — The transverse stiffness when the gap is closed.
- `staticFriction` — Coefficient of static friction
- `kineticFriction` — Coefficient of kinetic friction

Returns: the created GapProperty

### `apex.attribute.createHYBDAMP(name: str, description: str, id: int, modeMethod: int, modalDamping: int, useStructuralDamping: str, printEigenSummary: str) -> apex.catalog.HYBDAMP`
Create and return HYBDAMP.

- `name` — An optional name. If omitted, the name is automatically assigned to the object.
- `description` — The optional description. If omitted, it is leaved as blank.
- `id` — An optional id. If omitted, system will automatically assign the existing id + 1 to it.
- `modeMethod` — METHOD: the id of a mode calculation method, should be the id of EIGR or EIGRL.
- `modalDamping` — SDAMP: the id of a modal damping table.
- `useStructuralDamping` — KDAMP: an optional string argument("YES" or "NO") to define whether use the vicious damping as the structural damping. If it is "YES", the viscous modal damping is entered into the complex stiffness matrix as structural damping. If omitted, the default is "NO".
- `printEigenSummary` — PRTEIG: an optional boolean argument("YES" or "NO")to define whether print eigenvalue summary from hybrid damping calculation. If it is "YES", the solver will print the eigenvalue summary from hybrid damping calculation. If omitted, the default is "NO".

### `apex.attribute.createITER(name: str, description: str, id: int, preconditionerOption: str, convergenceCriterion: str, printMessageForEachIteration: str, userConvergenceParameter: float, maxNumberIterations: int, paddingValue: int, extractionLevel: int, terminationCriterion: int) -> apex.catalog.ITER`
create ITER object

- `name` — name of ITER
- `description` — description of ITER
- `id` — id of ITER
- `preconditionerOption` — String to define Preconditioner option J: Jacobi JS: Jacobi with diagonal scaling. C: Incomplete Cholesky. CS: Incomplete Cholesky with diagonal scaling. RIC: Reduced incomplete Cholesky. RICS: Reduced incomplete Cholesky with diagonal scaling. BIC: Block incomplete Cholesky for real problems. BICCMPLX: Block incomplete Cholesky for complex problems. CASI: Element-based third party iterative solver. USER: User given preconditioning.
- `convergenceCriterion` — Convergence criterion. (String:"AR","GE","AREX","GEEX"; Default = "AREX")
- `printMessageForEachIteration` — String to define Message flag. YES: Messages will be printed for each iteration. NO: Only minimal messages will be printed from the iterative solver(Default).
- `userConvergenceParameter` — User-given convergence parameter epsilon.
- `maxNumberIterations` — Maximum number of iterations,Integer>0.
- `paddingValue` — Padding value for RIC, RICS, BIC, and BICCMPLX preconditioning. (Integer > 0)
- `extractionLevel` — Extraction level in reduced incomplete Cholesky preconditioning, Integer = 0 thought 7.
- `terminationCriterion` — String argument to control early termination of the iterative solver. 0: Runs to completion (Default). -1: Terminates after preface giving resource estimates.

### `apex.attribute.createInteractionAutoPair(name: str, description: str, targetSide: apex.EntityCollection, body1Property: apex.attribute.ContactBodyProperty, body2Property: apex.attribute.ContactBodyProperty, pairTolerance: float, interactionType: apex.attribute.InteractionType, interactionPropertyGeometric: apex.attribute.InteractionPropertyGeometric, interactionPropertyPhysical: apex.attribute.InteractionPropertyPhysical, allowSelfContactSide1: bool, allowSelfContactSide2: bool) -> apex.attribute.InteractionCollection`
Creates and returns one or more interaction based on an input collection of Geometry and/or Mesh bodies and tolerance parameters.

- `name` — Optional name for the interaction. If omitted, Apex will provide a default name by concatenating the prefix 'Interaction' with the lowest possible integer required to ensure name uniqueness within the scope of the Model.
- `description` — Optional string providing a description for the Interaction. If omitted, the description will be blank
- `targetSide` — A collection containing at least two of the following entity types Geometry Solids Geometry Surfaces Solid Mesh SurfaceMesh
- `body1Property` — Optional - Contact body property of side 1 side of interaction pair. If omits, the default contact body properties will be used.
- `body2Property` — Optional - Contact body property of side 1 side of interaction pair. If omits, the default contact body properties will be used.
- `pairTolerance` — An optional distance tolerance value (default =0.005m) used to determine the subset of all possible pairs of bodies from target that an interaction will be created for. An interaction will only be created for pairs where the minimum distance between the two sides of the pair is less than the PairTolerance. In currently, we only support auto detect pair for interaction type = glue. Provide and exceptation if the type is contact.
- `interactionType` — Interaction type of the interaction object: Glue, General Contact or Self Contact.
- `interactionPropertyGeometric` — Interaction Geometric Properties.
- `interactionPropertyPhysical` — Interaction Physical Properties.
- `allowSelfContactSide1` — Optional - Boolean to choose self Contact for primary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.
- `allowSelfContactSide2` — Optional - Boolean to choose self Contact for secondary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.

### `apex.attribute.createInteractionManualPair(name: str, description: str, targetSide1: apex.EntityCollection, targetSide2: apex.EntityCollection, body1Property: apex.attribute.ContactBodyProperty, body2Property: apex.attribute.ContactBodyProperty) -> apex.attribute.Interaction`
Creates and returns an Interaction based on two inputs each representing opposite sides of the interaction.

- `name` — Optional name for the interaction. If omitted, Apex will provide a default name by concatenating the prefix 'Interaction' with the lowest possible integer required to ensure name uniqueness within the scope of the Model.
- `description` — Optional string providing a description for the Interaction. If omitted, the description will be blank
- `targetSide1` — A collection of entities that represent the first side (Side 1) of the Interaction. The collection may contain, - geometry Solids, Surfaces, Cells and Faces - Solid and Surface MeshBodies - arbitrary sets of solid elements/faces and shell elements
- `targetSide2` — A collection of entities that represent the second side (Side 2) of the Interaction. The collection may contain, - geometry Solids, Surfaces, Cells and Faces - Solid and Surface MeshBodies - arbitrary sets of solid elements/faces and shell elements
- `body1Property` — Optional - Contact body property of side 1 side of interaction pair. If omits, the default contact body properties will be used.
- `body2Property` — Optional - Contact body property of side 1 side of interaction pair. If omits, the default contact body properties will be used.

### `apex.attribute.createInteractionPropertyGeometric(contactToleranceCalculationMethod: apex.AutoManual, contactTolerance: float, biasFactor: float, shellLayerSide1: apex.attribute.ShellLayer, shellLayerSide2: apex.attribute.ShellLayer, ignoreShellThicknessSide1: bool, ignoreShellThicknessSide2: bool, normalPenaltyFactor: float, tangentPenaltyFactor: float, penetrationDistance: float, slipDistance: float, contactSearchOrder: apex.attribute.ContactSearchOrder, hardSoftRatio: float, stressFreeInitialContact: bool, delayedSlideOff: bool, slideOffDistance: float, retainMoment: bool, allowSeparation: bool, breakingGlueCriteria: bool, stepGlue: bool, flexibleGlue: bool, normalStiffness: float, tangentStiffness: float, interferenceFit: bool, interferenceFitMethod: apex.attribute.InterferenceFitMethod, interferenceClosure: float, cosinesVector: [float], scaleCenter: [float], scaleFactorVector: [float], penetrationSearchTolerance: float, coordinateSystemWithVector: apex.construct.CoordinateSystem, adjustedSecondaryBodyInterferenceFit: bool, initialClearance: bool, clearanceSearchTolerance: float, adjustedMagnitude: float, adjustedSecondaryBodyClearance: bool, id: int, name: str) -> apex.attribute.InteractionPropertyGeometric`
Creates and returns an Interaction properties.

- `contactToleranceCalculationMethod` — An optional argument (default True) that controls whether the ContactTolerance should be calculated automatically by the system or defined manually via this method. The Automatic option works well in most cases and should only be replaced with a manual value for complex geometry where the automatic value is observed to produce unwanted results.
- `contactTolerance` — An optional distance tolerance value (default =0.005m) used to determine the subset of elements specified in targetSide1 and targetSide2 that will actually be glued/contact during the simulations.
- `biasFactor` — Optional - Contact tolerance bias factor
- `shellLayerSide1` — Shell layer to be used for contact detection in side 1. In segment to segment contact method, it only supports "ShellLayer = TopAndButtom", skip other shell layer method. In node to segment contact method, it supports all 3 options.
- `shellLayerSide2` — Shell layer to be used for contact detection in side 2. In segment to segment contact method, it only supports "ShellLayer = TopAndButtom", skip other shell layer method. In node to segment contact method, it supports all 3 options.
- `ignoreShellThicknessSide1` — Consider or ignore shell thickness during detection of contact side 1
- `ignoreShellThicknessSide2` — Consider or ignore shell thickness during detection of contact side 2
- `normalPenaltyFactor` — Optional - Augmented Lagrange penalty factor in normal direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `tangentPenaltyFactor` — Optional - Augmented Lagrange penalty factor in tangent direction The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `penetrationDistance` — Optional - Penetration distance beyond which an augmentation will be applied The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `slipDistance` — Optional - Maximum allowable slip distance for sticking, beyond it there is no sticking, only sliding exists The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `contactSearchOrder` — Optional - contact search order for node to segment contact method.
- `hardSoftRatio` — Optional - Hard soft ratio of the contact pair. This argument is not available for node to segment contact method, which will be skipped in segment to segment method.
- `stressFreeInitialContact` — Optional - Activate/Deactivate stress-free initial contact can be obtained
- `delayedSlideOff` — Optional - Activate/Deactivate delay-slide off
- `slideOffDistance` — Optional - Slide Off Distance which is only available when "delayedSlideOff = True". Otherwise,it will be skipped.
- `retainMoment` — Optional - enable to retain moment for shell glue. Omits it if the interaction type is contact.
- `allowSeparation` — Optional - enable to allow glue separation during simulation. Omits it if the interaction type is contact.
- `breakingGlueCriteria` — Optional - enable to use breaking blue parameters to define separation when allowSeparation = True. Omits it if the interaction type is contact.
- `stepGlue` — Optional- Step Glue for Large Displacement and Rotation. Omits it if the interaction type is contact.
- `flexibleGlue` — Optional - Activate/Deactivate Flexible Glue. Omits it if the interaction type is contact.
- `normalStiffness` — Optional - Normal Stiffness for flexible glue. Omits it if the interaction type is contact.
- `tangentStiffness` — Optional - Tangent Stiffness for flexible glue. Omits it if the interaction type is contact.
- `interferenceFit` — Optional - active to Adjust Interference Fit
- `interferenceFitMethod` — Optional - Method to define Interference Fit.
- `interferenceClosure` — Optional - Adjust gap(>0.0) or overlap(<0.0) based on the value The option will be available when InterferenceFitMethod = NormalDirection or UserDireaction. If both interferenceClosure and interferenceClosureVariable are defined, the interferenceClosureVariable will be used in priority.
- `cosinesVector` — Optional - Cosines Vector[a1,a2,a3] of the interference fit direction. a1 will be the angle of x axis; a2 will be the angle of y axis; a3 will be the angle of z axis. The option will be available when InterferenceFitMethod = UserDirection.
- `scaleCenter` — Optional - Scale Center[x,y,z] with interference fit. The option will be available when InterferenceFitMethod = ScaleCenter.
- `scaleFactorVector` — Optional - Scale Factor Vector [a1,a2,a3] of the interference fit. The option will be available when InterferenceFitMethod = ScaleFactor.
- `penetrationSearchTolerance` — Optional - Penetration Search Tolerance. The option will be available when InterferenceFitMethod = Automatic.
- `coordinateSystemWithVector` — Optional - Coordinate system to define the interference fit vector. The option will be available when InterferenceFitMethod = UserDirection or ScaleFactor
- `adjustedSecondaryBodyInterferenceFit` — Optional to define which Contact body to be adjust for interference fit. True: Secondary body False: Primary body
- `initialClearance` — Optional - active to Adjust Initial gap or overlap
- `clearanceSearchTolerance` — Optional - Search tolerance of initial gap or overlap. It is only available when initialClearance is true.
- `adjustedMagnitude` — Optional - initial Gap or overlap magnitude. It is only available when initialClearance is true.
- `adjustedSecondaryBodyClearance` — Optional to define which Contact body to be adjust for Initial gap/overlap. True: Secondary body False: Primary body It is only available when initialClearance is true.
- `id` — ID of Interaction geometric properties.
- `name` — Optional-name of interaction geometric properties.

### `apex.attribute.createInteractionPropertyPhysical(frictionCoefficient: float, frictionStressLimit: float, maxNormalStress: float, maxTangentStress: float, exponent1: float, exponent2: float, separationForce: float, separationStress: float, id: int, name: str) -> apex.attribute.InteractionPropertyPhysical`
Creates and returns an Interaction Physical properties.

- `frictionCoefficient` — Optional - Friction Coefficient of the contact pair
- `frictionStressLimit` — Optional - Friction stress limit of the contact pairglued/contact during the simulations.
- `maxNormalStress` — Optional - it is only available when breakingGlue = True. Omits it if the interaction type is contact.
- `maxTangentStress` — Optional - it is only available when breakingGlue = True. Omits it if the interaction type is contact.
- `exponent1` — Optional - Exponent of Max Normal Stress. It is only available when maxNormalStress is defined. Omits it if the interaction type is contact.
- `exponent2` — Optional - Exponent of Max Tangent Stress. It is only available when maxTangentStress is defined. Omits it if the interaction type is contact.
- `separationForce` — Optional - max force of separation, which is only available when separation method define in scenario is based on "Force". Otherwise,it will be skipped.
- `separationStress` — Optional - max stress of separation, which is only available when separation method define in scenario is based on "Stress". Otherwise,it will be skipped.
- `id` — ID of interaction physical properties
- `name` — Optional-name of interaction physical properties.

### `apex.attribute.createInterfacePoint(applicationMethod: ApplicationMethod, target: apex.EntityCollection, name: str = "Interface Point", description: str = "", location: apex.ILocation = None, distributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, orientation: apex.IOrientation = None, activeDofs: str = "123456", generateASET: bool = True, useLocalValue: bool = True) -> apex.attribute.InterfacePoint`
Creates and returns an InterfacePoint.

- `applicationMethod` — Enumeration defining the application method Options are: 1. ApplicationMethod.Direct 2. ApplicationMethod.Remote 3. ApplicationMethod.Free, the method is only available in Adams Mission. Returns Error if the option is used for creation in non-Adams Mission.
- `target` — A collection of entities as an ILocationCollection that define regions of the MechanicalSystem to which this InterfacePoint connects. Valid entity types are Parts, geometry bodies, geometry topologies or nodes.
- `name` — An optional name for this InterfacePoint. If omitted, the system will assign a default name consisting of the prefix "Interface Point " plus the lowest possible integer required to create a unique Interface Point name within the scope of the current Apex model. If provided, the name must be unique within the Part or Assembly that composes the Interface Point. If a non-unique name is provided, the system will silently update the provided name to ensure uniqueness.
- `description` — An optional description for this InterfacePoint. If omitted, the description will be left blank.
- `location` — The location of the InterfacePoint as an ILocation. The location of the InterfacePoint will be at the global x, y, z coordinate locations defined by ILocation. While application method is "Direct", skip the location definition and the system will automatically calculation the location. While application method is "Remote" or "Free", the location is required.
- `distributionType` — An optional enumeration argument defining how loads will be distributed between the interface point and the attachment region. The default "Compliant" option causes the motion of the reference point to be calculated as the average of the Motion of the points in the attachment region. It adds no stiffness to the regions that it attaches to and will distribute load according to the relative stiffness distributions across the attachment region. The optional "Rigid" option will cause the entire attachment region to be considered as a rigid body. If the attachment region is already part of a rigid body, the options are equivalent. If applicationMethod is "ApplicationMethod.Free", distribution type will be skipped.
- `orientation` — An optional orientation for the InterfacePoint as an IOrientation object. If omitted, the orientation is parallel to the global cartesian coordinate system.
- `activeDofs` — An optional string argument defining the degrees of freedom that are active on this InterfacePoint. Each degrees of freedom is represented by an integer between 1 and 6. The translation degrees of freedom are represented by the values 1, 2 and 3 (corresponding the x, y and z directions) with rotational degrees of freedom represented by the values 4, 5 and 6 representing rotations about the x, y and z axes. The active degrees of freedom may be entered in any order and duplicate values will be silently ignored. Providing more than six characters is considered an error wan will cause the method to raise an exception. If omitted, all six degrees of freedom will be active. The argument of "activeDofs" is not required in "ApplicationMethod.Free".
- `generateASET` — Optional Boolean argument to control if ASET creates for the interface point. If true, the ASET will be created to generate MNF. If false, No ASET will be created. If ApplicationMethod.Free is used, it will be omitted.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.

Returns: Creates and returns an InterfacePoint.

### `apex.attribute.createJointCylindrical(name: str = "", description: str = "", jointAxis: apex.attribute.JointAxis = apex.attribute.JointAxis.XAxis, side1: apex.EntityCollection = None, side1DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, side2: apex.EntityCollection = None, side2DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, jointOrigin: apex.Entity = None, jointOrientation: apex.construct.Orientation = None, joint: Joint = None, axisLocationMode: apex.attribute.AxisLocationMode = apex.attribute.AxisLocationMode.Undefined, jointRenderType: apex.attribute.JointRenderType = apex.attribute.JointRenderType.Undefined) -> CylindricalJoint`
Create a new CylindricalJoint entity.

- `name` — name of the new CylindricalJoint object.
- `description` — description of the new CylindricalJoint object.
- `jointAxis` — joint axis of the new CylindricalJoint object.
- `side1` — side1 attachment region of the new CylindricalJoint object.
- `side1DistributionType` — distribution type of the side1 of the new CylindricalJoint object
- `side2` — side2 attachment region of the new CylindricalJoint object.
- `side2DistributionType` — distribution type of the side2 of the new CylindricalJoint object
- `jointOrigin` — origin of the new CylindricalJoint object
- `jointOrientation` — orientation of the new CylindricalJoint Object
- `joint` — to create CylindricalJoint Object
- `axisLocationMode` — axisLocationMode of the new Revolute object
- `jointRenderType` — jointRenderType of the new Revolute object - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

Returns: the created CylindricalJoint

### `apex.attribute.createJointPlanar(name: str = "", description: str = "", jointAxis: apex.attribute.JointAxis = apex.attribute.JointAxis.XAxis, side1: apex.EntityCollection = None, side1DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, side2: apex.EntityCollection = None, side2DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, jointOrigin: apex.Entity = None, jointOrientation: apex.construct.Orientation = None, joint: Joint = None, axisLocationMode: apex.attribute.AxisLocationMode = apex.attribute.AxisLocationMode.Undefined, jointRenderType: apex.attribute.JointRenderType = apex.attribute.JointRenderType.Undefined) -> PlanarJoint`
Create a new PlanarJoint entity.

- `name` — name of the new PlanarJoint object.
- `description` — description of the new PlanarJoint object.
- `jointAxis` — joint axis of the new PlanarJoint object.
- `side1` — side1 attachment region of the new PlanarJoint object.
- `side1DistributionType` — distribution type of the side1 of the new PlanarJoint object
- `side2` — side2 attachment region of the new PlanarJoint object.
- `side2DistributionType` — distribution type of the side2 of the new PlanarJoint object
- `jointOrigin` — origin of the new PlanarJoint object
- `jointOrientation` — orientation of the new PlanarJoint Object
- `joint` — to create PlanarJoint Object
- `axisLocationMode` — axisLocationMode of the new Revolute object
- `jointRenderType` — jointRenderType of the new Revolute object- optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

Returns: the created PlanarJoint

### `apex.attribute.createJointPrismatic(name: str = "", description: str = "", jointAxis: apex.attribute.JointAxis = apex.attribute.JointAxis.XAxis, side1: apex.EntityCollection = None, side1DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, side2: apex.EntityCollection = None, side2DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, jointOrigin: apex.Entity = None, jointOrientation: apex.construct.Orientation = None, joint: Joint = None, axisLocationMode: apex.attribute.AxisLocationMode = apex.attribute.AxisLocationMode.Undefined, jointRenderType: apex.attribute.JointRenderType = apex.attribute.JointRenderType.Undefined) -> PrismaticJoint`
Create a new PrismaticJoint entity.

- `name` — name of the new PrismaticJoint object.
- `description` — description of the new PrismaticJoint object.
- `jointAxis` — joint axis of the new PrismaticJoint object.
- `side1` — side1 attachment region of the new PrismaticJoint object.
- `side1DistributionType` — distribution type of the side1 of the new PrismaticJoint object
- `side2` — side2 attachment region of the new PrismaticJoint object.
- `side2DistributionType` — distribution type of the side2 of the new PrismaticJoint object
- `jointOrigin` — origin of the new PrismaticJoint object
- `jointOrientation` — orientation of the new PrismaticJoint Object
- `joint` — to create PrismaticJoint Object
- `axisLocationMode` — axisLocationMode of the new Revolute object
- `jointRenderType` — jointRenderType of the new Revolute object - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

Returns: the created PrismaticJoint

### `apex.attribute.createJointRevolute(name: str = "", description: str = "", jointAxis: apex.attribute.JointAxis = apex.attribute.JointAxis.XAxis, side1: apex.EntityCollection = 0, side1DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, side2: apex.EntityCollection = 0, side2DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, jointOrigin: apex.Entity = 0, jointOrientation: apex.construct.Orientation = None, joint: Joint = 0, axisLocationMode: apex.attribute.AxisLocationMode = apex.attribute.AxisLocationMode.Undefined, jointRenderType: apex.attribute.JointRenderType = apex.attribute.JointRenderType.Undefined) -> RevoluteJoint`
Create a new RevoluteJoint entity.

- `name` — name of the new RevoluteJoint object.
- `description` — description of the new RevoluteJoint object.
- `jointAxis` — joint axis of the new RevoluteJoint object.
- `side1` — side1 attachment region of the new RevoluteJoint object.
- `side1DistributionType` — distribution type of the side1 of the new RevoluteJoint object
- `side2` — side2 attachment region of the new RevoluteJoint object.
- `side2DistributionType` — distribution type of the side2 of the new RevoluteJoint object
- `jointOrigin` — origin of the new RevoluteJoint object
- `jointOrientation` — orientation of the new RevoluteJoint object
- `joint` — to create RevoluteJoint Object
- `axisLocationMode` — axisLocationMode of the new Revolute object
- `jointRenderType` — jointRenderType of the new Revolute object - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

Returns: the created RevoluteJoint

### `apex.attribute.createJointSpherical(name: str = "", description: str = "", jointAxis: apex.attribute.JointAxis = apex.attribute.JointAxis.XAxis, side1: apex.EntityCollection = None, side1DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, side2: apex.EntityCollection = None, side2DistributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, jointOrigin: apex.Entity = None, jointOrientation: apex.construct.Orientation = None, joint: Joint = None, axisLocationMode: apex.attribute.AxisLocationMode = apex.attribute.AxisLocationMode.Undefined, jointRenderType: apex.attribute.JointRenderType = apex.attribute.JointRenderType.Undefined) -> SphericalJoint`
Create a new SphericalJoint entity.

- `name` — name of the new SphericalJoint object.
- `description` — description of the new SphericalJoint object.
- `jointAxis` — joint axis of the new SphericalJoint object.
- `side1` — side1 attachment region of the new SphericalJoint object.
- `side1DistributionType` — distribution type of the side1 of the new SphericalJoint object
- `side2` — side2 attachment region of the new SphericalJoint object.
- `side2DistributionType` — distribution type of the side2 of the new SphericalJoint object
- `jointOrigin` — origin of the new SphericalJoint object
- `jointOrientation` — orientation of the new SphericalJoint Object
- `joint` — to create SphericalJoint Object
- `axisLocationMode` — axisLocationMode of the new Revolute object
- `jointRenderType` — jointRenderType of the new Revolute object - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

Returns: the created SphericalJoint

### `apex.attribute.createLayeredPanel(target: apex.geometry.Surface, name: str = "", description: str = "") -> LayeredPanel`
Creates and returns a LayeredPanel using an input Surface. The LayeredPanel is added to the parent Part of the input Surface.

- `target` — The Surface that defines the extent of the LayeredPanel.
- `name` — The name of the LayeredPanel. If omitted, the system will assign a default name If provided, the name must be unique within the scope of the parent Part. If the supplied name is not unique within the scope of the parent Part the system will modify the supplied name to ensure uniqueness
- `description` — An optional description of the LayeredPanel. If omitted, the description will be left blank

Returns: the created LayeredPanel

### `apex.attribute.createMaterialSheet(name: str = "", description: str = "", material: apex.attribute.Material = None, thickness: float = NAN) -> apex.attribute.MaterialSheet`
Creates and returns a MaterialSheet and adds it to the Material catalog.

- `name` — An optional name for this MaterialSheet. If omitted, the system will provide a default name using the prefix "Sheet material" with an appended integer to ensure uniqueness of the name within the Material Catalog. If provided, the name must be unique within the Materials catalog. If a non-unique name is provided, the system will append an integer to ensure name uniqueness within the Material catalog.
- `description` — An optional description for this MaterialSheet.
- `material` — The Material from which the MaterialSheet is made. The Material must exist within the Material catalog.
- `thickness` — The thickness of this MaterialSheet. thickness represents a Length quantity and is defined in the units of Length from the active script unit system.

### `apex.attribute.createMaterialSheetStack(sheetStackDefinition: [dict], name: str = "Sheet stack <n>", description: str = "", symmetry: apex.attribute.StackSymmetry = apex.attribute.StackSymmetry.Asymmetric) -> apex.attribute.MaterialSheetStack`
Creates and returns a MaterialSheetStack and adds it to the Materials catalog. Input arguments define the order and relative orientations of the MaterialSheets within the stack and enable creation of symmetric stacks based on definition of just half of the stacked sheets.

- `sheetStackDefinition` — stackDefinition defines an ordered list of oriented MaterialSheets. stackDefinition is a "List of Dictionaries" data structure. Each dictionary in the list identifies a MaterialSheet and the orientation of that sheet in the stack.The order of the Dictionaries in this List defines the order of the sheets in the stack. Each Dictionary identifies the Sheet and the sheet orientation using to key value pairs as follows, key = "sheet_name" of type string has an associated string type value identifying the name of the MaterialSheet key = "sheet_orientation" of type string has an associated float value defining the relative orientation of the sheet in the MaterialSheetStack The value of sheet_orientation represents an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `name` — An optional name for the MaterialSheetStack. If omitted, the system will provide a default name using the prefix "Sheet stack" with an appended integer to ensure uniqueness of the name within the Material catalog. If provided, the name must be unique within the Materials catalog. If a non-unique name is provided, the system will append an integer to ensure name uniqueness within the Material catalog.
- `description` — An optional description for this MaterialSheetStack.
- `symmetry` — optional enumeration argument (default = Asymmetric) to indicate whether the input stack definition represents the entire MaterialSheetStack or if it should be copied and reflected to define the complete stack definition. The default value of "Asymmetric" causes the input stack definition to completely define the stack contents. Setting the value to "Odd" will create a stack that is symmetric about the first sheet in the stack. The first sheet will NOT be reflected and the stack will contain an Odd numbers of sheets Setting the value to "Even" will create a stack where all sheets in the definition are copied and reflected resulting in an even number of sheets in the stack.

### `apex.attribute.createMeshDependentTie(name: str, description: str, target1: apex.EntityCollection, target2: apex.EntityCollection = None, cleanupTolerance: float = NAN, touchingCurveSearchTolerance: float = NAN) -> apex.attribute.MeshDependentTieCollection`
Creates one or more MeshDependentTies from the input geometry topology and returns them in a MeshDependentTieCollection. MeshDependentTies can be created between the Edges/Faces of Surfaces/Solids. When a tie is created between a Face and an Edge, a new 'virtual' Edge is added to the Face and the tie is actually created between this 'virtual' Edge and the 'real' Edge.

- `name` — A name used to identify the MeshDependentTie. If the method creates multiple MeshDependentTies this name will be used as a prefix and the full name of each tie will be created by appending an integer with the lowest value possible to avoid duplicate MeshDependentTie names in the scope of the Model.
- `description` — A description for the MeshDependentTie. If the method creates multiple MeshDependentTies this description will be used for ALL of the created ties.
- `target1` — A MeshDependentTie connects two 'Sides'. This method supports creation of multiple MeshDependentTies in a single call. The entities to be tied are usually provided to the method in two groups and the method will attempt to tie everything in the first group to everything in the second group. This argument - 'target1' - identifies all of the entities in the first group. (Entities in the second group are identified using the 'target2' argument). It may contain EITHER Edges or Faces but not both otherwise it will throw an exception. Entities of any other type will be silently ignored
- `target2` — A MeshDependentTie connects two 'Sides'. This method supports creation of multiple MeshDependentTies in a single call. The entities to be tied are usually provided to the method in two groups and the method will attempt to tie everything in the first group to everything in the second group. This argument - 'target2' - identifies all of the entities in the second group. (Entities in the first group are identified using the 'target1' argument). target2 may only contain Edges. If entities of any other type are included in target2 they will be silently ignored. target2 is optional if target1 identifies Edges but is required if target1 identifies Faces. If target2 is omitted and target1 identifies Edges the method will attempt to tie every Edge in target 1 to every other Edge in target1. If target 2 is omitted and target1 identifies Faces, the method will throw an exception.
- `cleanupTolerance` — A tolerance used to avoid creation of unwanted small geometry features such as short edges and sliver faces.
- `touchingCurveSearchTolerance` — An optional tolerance (default = 0.1mm) controlling whether Curves that do not lie entirely ON the Faces/Surfaces of target1 will cause MeshDependentTies to be created. If target1 contains Surfaces or Faces and target1 contains Curves, any Curve (but not Edge) that has both end points touching a Face/Surface in target1 will cause MeshDependentTies to be created if the distance between all locations on the Curve and the Surfaces/Faces that it touches are less than this tolerance. Under these circumstances, this tolerance can be used to create MeshDependentTies even though a substantial gap may exits between the Curve and the target Faces touchingCurveSearchTolerance represents a Length quantity and must be defined using the units of Length from the active script unit system.

Returns: a target of the created "MeshDependentTie"s

### `apex.attribute.createNLSTEP(name: str, description: str, id: int, totalTimeLoadCase: float, setupType: str, predefinedControlOptions: str, general: bool, maxIterations: int, minIterations: int, maxBisections: int, activateCreep: int, fixed: bool, fixedTimeStepIncrements: int, outputInterval: int, adapt: bool, initLoadStepFraction: float, minTimeStepFraction: float, maxTimeStepFraction: float, desiredIterationsPerInc: int, factorStepSizeChange: float, outputFrequencyControl: str, outputFrequency: int, maxIncrementsLoadCase: int, activateArtificialDamping: int, dampingRatio: float, userCriteria: int, usePhysicalCriteria: int, treatUserCriteria: int, smallestRatio: float, largesetRatio: float, skipFactorTimeStep: int, dominantPeriodSteps: int, timeStepBounds: float, displacementTolerance: float, arcln: bool, constraintType: str, initTimeStepFraction: float, minAdjustRatioArcLength: float, maxAdjustRatioArcLength: float, desiredIterationsArcLength: int, maxIterationsLoadCase: int, lcnt: bool, numIncrements: int, convergeCriteriaContact: str, errorToleranceDispContact: float, errorToleranceLoadContact: float, errorToleranceWorkContact: float, iterationLimitBeforeDiverge: int, maxBisectionsPerInc: int, maxIterationsPerInc: int, minIterationsPerInc: int, heat: bool, convergeCriteriaHeat: str, errorToleranceTemperature: float, errorToleranceHeatFlux: float, errorToleranceWorkHeat: float, stiffUpdateMethodHeat: str, itersBeforeStiffUpdateHeat: int, maxCorrectionVectorsHeat: int, maxLineSearchesHeat: int, lineToleranceHeat: float, mech: bool, convergeCriteriaMech: str, errorToleranceDispMech: float, errorToleranceLoadMech: float, errorToleranceWorkMech: float, stiffUpdateMethodMech: str, itersBeforeStiffUpdateMech: int, includeRotationsMoments: int, maxCorrectionVectorsMech: int, maxLineSearchesMech: int, lineToleranceMech: float, effectiveStressFracton: float, coup: bool, conversionFactorHeatPlastic: float, conversionFactorHeatFric: float) -> apex.catalog.NLSTEP`
Create and return NLSTEP.

- `name` — An optional name. If omitted, the name is automatically assigned to the object.
- `description` — The optional description. If omitted, it is leaved as blank.
- `id` — An optional id. If omitted, system will automatically assign the existing id + 1 to it.
- `totalTimeLoadCase` — TOTTIM: An optional total time for the load case. If omitted, the default value is 1.0.
- `setupType` — String argument to define the setup type of the control parameters: "SMART" or "MANUAL". "SMART" indicates a smart setup type, user only needs to specify the predefined control options(CTRLDEF) while leaving other options blank(except for transient analysis). "MANUAL" indicates a manual setup type, the predefined control option is ignored and user needs to manually specifies all the necessary options.
- `predefinedControlOptions` — CTRLDEF: a string argument to set the predefined control options when the setup type is "SMART". Note that the options are different depending on the scenario type using the NLSTEP. "QLINEAR" sets a linear convergence options. "MILDLY" sets a mild nonlinear convergence options. "SEVERELY" sets a severe nonlinear convergence options. "LCPERF" and "LCACCU" are only used in SOL101. "LCPERF" specifies the performance preference during analysis, while "LCACCU" prefers accuracy for analysis. These keywords must be defined if the smart contact in SOL 101 default is required.
- `general` — A boolean argument to activate the parameters used for a variety of simulations.
- `maxIterations` — MAXITER: the optional maximum iteration number allowed for each increment. If omitted, the default is 10.
- `minIterations` — MINITER: the minimum iteration number needed for each increment (integer > 0). This argument can be left blank, because Nastran solver will set different default values. The default is 1, but in contact analysis or CTRLDEF = SEVERELY, the default is 2. When high accuracy is required, it is also recommended to set MINITER = 2.
- `maxBisections` — MAXBIS: the maximum number of bisections allowed in the current step. If omitted, the default is 10.
- `activateCreep` — CREEP: an integer flag to activate the creep. "1" will activate the creep while "0" will not activate the creep.
- `fixed` — A boolean argument to indicate that fixed time stepping will be used.
- `fixedTimeStepIncrements` — NINC: number of increments for fixed time stepping(integer > 0). If omitted, the default is 50.
- `outputInterval` — NO: Interval for output. Every N-th increment will be saved for output (integer >= 0). If omitted, the default is 1.
- `adapt` — A boolean argument to indicate that the adaptive load stepping procedure will be used.
- `initLoadStepFraction` — DTINITF: Initial time step defined as fraction of total load step time (TOTTIM). If DTINITF>=DTMAXF(maxTimeStepFraction) then, DTINITF is reset to DTMAXF. If CTRLDEF is set to QLNEAR, the user should set DTINITF equal to TOTTIM. If omitted, the default is 0.01.
- `minTimeStepFraction` — DTMINF: Minimum time step defined as fraction of total load step time (TOTTIM). If omitted, the default is 1e-5.
- `maxTimeStepFraction` — DTMAXF: Maximum time step defined as fraction of total load step time (TOTTIM). For most nonlinear problems, this should be between 0.05 and 0.2 for dynamic simulations. If omitted, the default is 0.5.
- `desiredIterationsPerInc` — NDESIR: Desired number of iterations per increment. If omitted, the default is 4.
- `factorStepSizeChange` — SFACT: factor for increasing time steps due to number of iterations. If omitted, the default is 1.2.
- `outputFrequency` — INTOUT: an integer to control the output (integer >= -1). If omitted, the default is 0. -1: Only the last increment of the step will be output. 0: Every computed load increment will be output. > 0: The output will be obtained at INTOUT equally spaced intervals. The time step will be temporarily adjusted if necessary in order to reach these points in time.
- `maxIncrementsLoadCase` — NSMAX: Maximum number of increments in the current load case. The job will stop if this limit is reached. if omitted, the default is 99999.
- `activateArtificialDamping` — IDAMP: activate artificial damping for static analysis. 0: No damping considered. 4: Artificial damping is always turned on. 5: Artificial damping is not turned on. But time step is adjusted based on damping energy as 4. 6: When the time step reaches the minimum value and artificial damping is turned on. If omitted, the default is 0.
- `dampingRatio` — DAMP: Damping ratio. If omitted, the default is 2.e-4.
- `userCriteria` — CRITTID: defines the user criteria for loading stepping control.
- `usePhysicalCriteria` — IPHYS: Flag to determine if automatic physical criteria should be added and how analysis should proceed if a user criterion is not satisfied. If omitted, the default is 2. 2: Do not add automatic physical criteria; stop when any user criterion is not satisfied. -2: Do not add automatic physical criteria; continue when user criteria are not satisfied. 1: Add automatic physical criteria; stop when any user criterion is not satisfied. -1: Add automatic physical criteria; continue when any user criterion is not satisfied.
- `treatUserCriteria` — LIMTAR: an integer to treat user criteria as limits or as targets. Only used if a user criterion is given through CRITTID. If omitted, the default is 0. 0 to treat user criteria as limits. 1 to treat user criteria as targets.
- `smallestRatio` — RSMALL: smallest ratio between time step changes due to user criteria. If omitted, the default is 0.1.
- `largesetRatio` — RBIG: Largest ratio between time step changes due to user criteria. If omitted, the default is 10.0.
- `skipFactorTimeStep` — ADJUST: time step skip factor for automatic time step adjustment. Only for dynamics. If omitted, the default is 0.0.
- `dominantPeriodSteps` — MSTEP: Number of steps to obtain the dominant period response(10 < Integer< 200 or = -1). If omitted, the default is 10.
- `timeStepBounds` — RB: define bounds for maintaining the same time step for the stepping function during the adaptive process(0.1 < float <1.0). If omitted, the default is 0.6.
- `displacementTolerance` — UTOL: Defines tolerance on displacement, .0001 < Real < 1.0. If omitted, the default is 1.0.
- `arcln` — A boolean argument to indicate that an arc length load stepping procedure will be used. It does not support general contact in SOL 400.
- `constraintType` — TYPE: A string argument to define constraint type in the arc length load stepping procedure. "CRIS" - Crisfield. "RIKS" - Riks. "MRIKS" - Modified Riks. If omitted, the default is "CRIS".
- `initTimeStepFraction` — DTINITFA: Initial time step defined as a fraction of the load step time(TOTTIME) for the arc-length procedure. If omitted, the default is 0.01.
- `minAdjustRatioArcLength` — MINALR: Minimum allowable arc-length adjustment ratio between increments for the adaptive arc-length method (0.0 < Float < 1.0). If omitted, the default is 0.25.
- `maxAdjustRatioArcLength` — MAXALR: Maximum allowable arc-length adjustment ratio between increments for the adaptive arc-length method (float > 1.0). If omitted, the default is 4.0.
- `desiredIterationsArcLength` — NDESIRA: Desired number of iterations for convergence to be used for the adaptive arc-length adjustment(Integer > 0). If omitted, the default is 4.
- `maxIterationsLoadCase` — NSMAXA: Maximum number of increments in the current load case(Integer). The job will stop if this limit is reached. If omitted, the default is 1000.
- `lcnt` — A boolean argument to indicate that the parameters in the contact analysis in SOL101 will be used.
- `numIncrements` — NINCC: Number of increments. If omitted, the Nastran solver will define different default increments. Default = 10 for CTRLDEF=""; Default=1 for CTRLDEF="LCPERF" or "LCACCU".
- `convergeCriteriaContact` — CONVC: Flag to select convergence criteria. String ="U", "P", "W", "V" or any combination. U = displacement error P = load equilibrium error, W = work error, V = vector component method, This convergence criteria is only used in the contact analysis in SOL101. If omitted, the Nastran solver will set different criteria: Default = "PV" for CTRLDEF = "" or "LCPERF"; Default = "UPV" for CTRLDEF= "LCACCU".
- `errorToleranceDispContact` — EPSUC: Error tolerance for displacement (U) criterion (Float > 0.0). Only used for contact analysis in SOL101. If omitted, the Nastran solver will set different default values: Default = 1.0E-3 for CTRLDEF = "LCPERF"; Default = 1.0E-2 for CTRLDEF= "" or "LCACCU".
- `errorToleranceLoadContact` — EPSPC: Error tolerance for load (V) criterion(Float > 0.0). Only used for contact analysis in SOL101. If omitted, the Nastran solver will set different default values: Default = 1.0E-3 for CTRLDEF = "LCPERF"; Default = 1.0E-2 for CTRLDEF= "" or "LCACCU".
- `errorToleranceWorkContact` — EPSWC: Error tolerance for work (W) criterion (Float > 0.0). Only used for contact analysis in SOL101. If omitted, the Nastran solver will set different default values: Default = 1.0E-7 for CTRLDEF = "LCPERF"; Default = 1.0E-2 for CTRLDEF= "" or "LCACCU".
- `iterationLimitBeforeDiverge` — MAXDIVC: Limit on probable divergence conditions per iteration before the solution is assumed to diverge(Integer != 0). Only used for contact analysis in SOL101. If omitted, the Nastran solver will set different default values: Default = 3 for CTRLDEF = "" or "LCPERF"; Default = 5 for CTRLDEF= "LCACCU".
- `maxBisectionsPerInc` — MAXBISC: Maximum number of bisections allowed for each load increment(-10 < Integer <10). If omitted, the default is 5.
- `maxIterationsPerInc` — MAXITERC: Limit on number of iterations for each load increment. (Integer >= 0) If omitted, the default is 25.
- `minIterationsPerInc` — MINITERC: Minimum number of iterations of a load increment (Integer > 0). If omitted, the Nastran solver will define different default values: Default =1, in contact analysis, default =2.
- `heat` — A boolean argument to indicate that the parameters for heat transfer analysis will be used.
- `convergeCriteriaHeat` — CONVH: Flag to select convergence criteria. String ="U", "P", "W", "V", "N", "A" or any combination. If omitted, the default is UPW. U = displacement error P = load equilibrium error W = work error V = vector component method N = length method A = auto switch The criteria is only used for heat analysis in SOL400.
- `errorToleranceTemperature` — EPSUH: Error tolerance for temperature (U) criterion. Only used in heat analysis in SOL400. If omitted, the default is 1.0E-2.
- `errorToleranceHeatFlux` — EPSPH: Error tolerance for heat flux (P) criterion. Only used in heat analysis in SOL400. If omitted, the default is 1.0E-2.
- `errorToleranceWorkHeat` — EPSWH: Error tolerance for work (W) criterion. Only used in heat analysis in SOL400. If omitted, the default is 1.0E-2.
- `stiffUpdateMethodHeat` — KMETHODH: A string argument to define the method for controlling stiffness updates. Only used in heat analysis in SOL400. "PFNT" - Pure full Newton Raphson. ITER - User defined iteration. AUTO - System automatically selects the most efficient strategy based on convergence rates. If omitted, the default is "AUTO".
- `itersBeforeStiffUpdateHeat` — KSTEPH: Number of iterations before the stiffness update for the user defined(ITER) method. Only used in heat analysis in SOL400. If omitted, the default is 1.
- `maxCorrectionVectorsHeat` — MAXQNH: Maximum number of quasi-Newton correction vectors to be saved on database. Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400. If omitted, the default is equal to MAXITER(maxIterationNumber).
- `maxLineSearchesHeat` — MAXLSH: Maximum number of line searches allowed for each iteration. Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400. If omitted, the default is 4.
- `lineToleranceHeat` — LSTOLH: Line search tolerance(0.01 < float < 0.9). Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400. If omitted, the default is 0.5.
- `mech` — A boolean argument to indicate that the parameters for the mechanical analysis will be used.
- `convergeCriteriaMech` — CONVC: Flag to select convergence criteria. String ="U", "P", "W", "V", "N", "A" or any combination. U = displacement error P = load equilibrium error W = work error V = vector component method N = length method A = auto switch The criteria is only used for mechanical analysis in SOL400. If omitted, the default is PV.
- `errorToleranceDispMech` — EPSUC: Error tolerance for displacement (U) criterion (Float > 0.0). Only used for mechanical analysis in SOL400. If omitted, the default is -0.1.
- `errorToleranceLoadMech` — EPSPC: Error tolerance for load (V) criterion(Float > 0.0). Only used for mechanical analysis in SOL400. If omitted, the default is 0.1.
- `errorToleranceWorkMech` — EPSWC: Error tolerance for work (W) criterion (Float > 0.0). Only used for mechanical analysis in SOL400. If omitted, the default is 0.1.
- `stiffUpdateMethodMech` — KMETHOD: A string argument to define the method for controlling stiffness updates. Only used in mechanical analysis in SOL400. "PFNT" - Pure full Newton Raphson. ITER - User defined iteration. If omitted, the default is "PFNT"
- `itersBeforeStiffUpdateMech` — KSTEP: Number of iterations before the stiffness update for the user defined(ITER) method. Only used in mechanical analysis in SOL400. If omitted, the default is 10.
- `includeRotationsMoments` — MRCONV: The integer argument to specify if rotations and moments should be included in the convergence testing when convergence criteria is set to UV, UN, PV, PN, UPV or UPN. 0: check on forces, moments, displacements and rotations. 1: check on forces, moments and displacements. 2: check on forces, displacements and rotations. 3:check on forces and displacements If omitted, the default is 3. If there is no V and N in the CONV, MRCONV is ignored and all translational and rotational quantities are used to compute the convergence criteria.
- `maxCorrectionVectorsMech` — MAXQN: Maximum number of quasi-Newton correction vectors to be saved on the database. Not used for pure full Newton-Raphson method. Only used in mechanical analysis in SOL400. If omitted, the default is equal to MAXITER(maxIterationNumber).
- `maxLineSearchesMech` — MAXLS: Maximum number of line searches allowed for each iteration. Not used for pure full Newton-Raphson method. Only used in mechanical analysis in SOL400. If omitted, the default is 4.
- `lineToleranceMech` — LSTOL: Line Search tolerance(0.01 < Float < 0.9). Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400. If omitted, the default is 0.5.
- `effectiveStressFracton` — FSTRESS: Fraction of effective stress used to limit the sub increment size in material routines(0.0 < float < 1.0). For non material enhanced elements only. If omitted, the default is 0.2.
- `coup` — A boolean argument to indicate that the parameters for the coupled analysis will be used.
- `conversionFactorHeatPlastic` — HGENPLAS: Conversion factor for heat generated due to plasticity. If omitted, the default is 0.0.
- `conversionFactorHeatFric` — HGENPLAS: Conversion factor for heat generated due to friction. If omitted, the default is 0.0.

### `apex.attribute.createNSMCombination(name: str, description: str, id: int, NSM: NonstructuralMassCollection) -> apex.attribute.NSMCombination`
Creates and returns a NSMCombination.

- `name` — Optional name for the NSM Combination.
- `description` — Optional string providing a description for the NSM Combination.
- `id` — ID of the NSM Combination. If omits, the system will automatically assign an ID.
- `NSM` — A collection of interactions for the NSM Combination.

### `apex.attribute.createNodeTie(referencePoint: apex.Entity = None, dependentDoF: str = "", dofDefinitionMode: apex.attribute.DOFDefinitionMode = apex.attribute.DOFDefinitionMode.All, attachmentRegions: apex.EntityCollection = None, DOFAndWeightFactors: {str:{str:float}} = {}, distributionType: apex.attribute.DistributionType = apex.attribute.DistributionType.Compliant, distributionMode: apex.attribute.DistributionMode = apex.attribute.DistributionMode.Auto, thermalExpansionCoeff: float = NAN) -> NodeTie`
Create a new NodeTie entity.

- `referencePoint` — of the new NodeTie
- `dependentDoF` — of the new NodeTie
- `dofDefinitionMode` — of the new NodeTie
- `attachmentRegions` — of the new NodeTie
- `DOFAndWeightFactors` — of the new NodeTie
- `distributionType` — of the new NodeTie
- `distributionMode` — of the new NodeTie
- `thermalExpansionCoeff` — of the new NodeTie

Returns: the created NodeTie

### `apex.attribute.createNonstructuralMassConstant(name: str, massDistribution: apex.attribute.MassDistribution, constantMass: float, target: apex.EntityCollection, id: int = 0, description: str = "") -> apex.attribute.NonstructuralMass`
Create a new constant NonstructuralMass.

- `name` — the name of the new NonstructuralMass.
- `massDistribution` — distribution type of the new NonstructuralMass.
- `constantMass` — mass value of the new NonstructuralMass.
- `target` — the attachment reginon used for the remote method.
- `id` — Optional - the id. Default value is zero.
- `description` — Optional - description of the new NonstructuralMass.

Returns: the created NonstructuralMass

### `apex.attribute.createNonstructuralMassVariable(name: str, massDistribution: apex.attribute.MassDistribution, variableMass: {float:apex.EntityCollection}, id: int = 0, description: str = "") -> apex.attribute.NonstructuralMass`
Create a new variable NonstructuralMass.

- `name` — the name of the new NonstructuralMass.
- `massDistribution` — distribution type of the new NonstructuralMass.
- `variableMass` — mass value-reginon collections of the new NonstructuralMass.
- `id` — Optional - the id. Default value is zero.
- `description` — Optional - description of the new NonstructuralMass.

Returns: the created NonstructuralMass

### `apex.attribute.createPointMass(name: str, mass: float, ixx: float, iyy: float, izz: float, ixy: float, ixz: float, iyz: float, applicationMethod: ApplicationMethod, location: apex.Coordinate, target: apex.EntityCollection = 0, orientation: apex.construct.Orientation = None, description: str = "") -> PointMass`
Create a new PointMass.

- `name` — the name of the new PointMass. default = "" (auto-named)
- `mass` — Mass of the PointMass.
- `ixx` — Ixx Mass Moment of Inertia.
- `iyy` — Iyy Mass Moment of Inertia.
- `izz` — Izz Mass Moment of Inertia.
- `ixy` — Ixy Mass Moment of Inertia.
- `ixz` — Ixz Mass Moment of Inertia.
- `iyz` — Iyz Mass Moment of Inertia.
- `applicationMethod` — missing, add it for avoiding warning.
- `location` — the location of the new PointMass.
- `target` — Optional - the attachment reginon used for the remote method.
- `orientation` — Optional - the orientation relative to the global coordinate system.
- `description` — Optional - the description.

Returns: the created PointMass

### `apex.attribute.createPointMassByMassMatrix(name: str, massMatrix: apex.attribute.PointMassMatrix, applicationMethod: ApplicationMethod, location: apex.Coordinate, target: apex.EntityCollection = None, orientation: apex.construct.Orientation = None, description: str = "") -> PointMass`
Create a new PointMass by Matrix.

- `name` — the name of the new PointMass. default = "" (auto-named)
- `massMatrix` — mass matrix of the new PointMass.
- `applicationMethod` — missing, add it for avoiding warning.
- `location` — the location of the new PointMass.
- `target` — Optional - the attachment reginon used for the remote method.
- `orientation` — Optional - the orientation relative to the global coordinate system.
- `description` — Optional - the description.

Returns: the created PointMass

### `apex.attribute.createQuasiStaticScenarioFromKeyResults(modelAssociation: apex.ModelAssociation, keyResultsPerEvent: {str:[str]}) -> apex.studies.Scenario`
Creates and returns a Static Scenario based on the input of ModelAssociation and KeyResults. This method takes a ModelAssociation and one or more keyResults as the input. From this input the method will create, 1.One or more ForceMoments with one or more ForceMometReps. One ForceMoment will be created for each NodeTie that is associated to an InterfacePoint within the input ModelAssociation. A series of ForceMomentReps will be created within each ForceMoment, corresponding to the number of keyResults provided in the input. 2.A single Static Scenario that references the primary Assembly from the input ModelAssociation as its Scenario ModelRep. 3.One Event will be created for each keyResult provided in the input. Each Event will reference the ForceMoments associated with the KeyResults. Each Event will have InertiaRelief enabled and will include no constraints.

- `modelAssociation` — A modelAssociation that associates the primary multibody dynamics assembly to an assembly that references geometry or finite element meshes. The Scenario created by this method will use as its Scenario ModelRep, the secondary Assembly from this ModelAssociations and will include.
- `keyResultsPerEvent` — Dictionary defining the Events and KeyResults that will be used to create the ForceMoments and Events in the Static Scenario created by this method. The dictionary key is a string type and represents the pathName of an Event from a multibody dynamics transient Scenario. The dictionary value is a List of strings where each string identifies a KeyResult using the KeyResult pathName. One Event will be added to the static Scenario created by this method for each keyResult for each multi-body dynamics Scenario Event.

Returns: Creates and returns a static scenario.

### `apex.attribute.createRANDPS(name: str, description: str, id: int, excitedLoadSubcase: [int], appliedLoadSubcase: [int], real: [float], imaginary: [float], table: [int]) -> apex.catalog.RANDPS`
create RANDPS set object

- `name` — name of RANDPS set
- `description` — description of RANDPS set
- `id` — id of RANDPS set
- `excitedLoadSubcase` — J: Subcase identification number of the excited load set. A list of excited load set subcases ID.
- `appliedLoadSubcase` — K: Subcase identification number of the applied load set. A list of applied load set subcases ID.
- `real` — X: real component of complex number A list of float value.
- `imaginary` — Y: imaginary component of complex number A list of float value.
- `table` — TID: Identification number of a TABRNDi entry that defines G(F). A list of TABRNDi entry ID.

### `apex.attribute.createRANDT1(name: str, description: str, id: int, timeLagNumber: [int], startingTimeLag: [float], maxTimeLag: [float]) -> apex.catalog.RANDT1`
create RANDT1 set object

- `name` — name of RANDT1 set
- `description` — description of RANDT1 set
- `id` — id of RANDT1 set
- `timeLagNumber` — N: Number of time lag intervals. (Integer > 0) A list of int value.
- `startingTimeLag` — T0： Starting time lag. (Real ≥ 0.0) A list of float value.
- `maxTimeLag` — TMAX: Maximum time lag. (Real > T0) A list of float value.

### `apex.attribute.createRCROSS(name: str, description: str, id: int, responseQuantityType1: [str], id1: [int], componentId1: [int], responseQuantityType2: [str], id2: [int], componentId2: [int], curveId: [int]) -> apex.catalog.RCROSS`
Create and return RCROSS.

- `name` — An optional name. If omitted, the name is automatically assigned to the object.
- `description` — The optional description. If omitted, it is leaved as blank.
- `id` — An optional id. If omitted, system will automatically assign the existing id + 1 to it.
- `responseQuantityType1` — RTYPE1: a list of strings to define the first response quantity type. Following strings are supported: "DISP" - displacement vector. "VELO" - velocity vector. "ACCEL" - acceleration vector. "OLOAD" - applied load vector. "SPCF" - single point constraint force vector. "MPCF" - multi point constraint force vector. "STRESS" - element stress. "STRAIN" - element strain. "FORCE" - element force. None - same with the responseQuantityType2, note that it is not "None". If omitted, the default is the type of responseQuantityType2.
- `id1` — ID1: a list of ids, each id points to element, node or scalar point.
- `componentId1` — COMP1: a list of component code ids of the first response quantity.
- `responseQuantityType2` — RTYPE2: a list of strings to define the second response quantity type. Following strings are supported: "DISP" - displacement vector. "VELO" - velocity vector. "ACCEL" - acceleration vector. "OLOAD" - applied load vector. "SPCF" - single point constraint force vector. "MPCF" - multi point constraint force vector. "STRESS" - element stress. "STRAIN" - element strain. "FORCE" - element force. None - same with the responseQuantityType1, note that it is not "None". If omitted, the default is the type of responseQuantityType1.
- `id2` — ID2: a list of ids, each id points to element, node or scalar point.
- `componentId2` — COMP2: a list of component code ids of the second response quantity.
- `curveId` — CURID: an optional list of curve ids, each item should be an integer >=0.

### `apex.attribute.createRemotePointEntity(x: float, y: float, z: float) -> RemotePointEntity`
Create a new remote point entity.

- `x` — x-coordinate.
- `y` — coordinate.
- `z` — of the new Orientation.

Returns: the created Orientation

### `apex.attribute.createRigidFace(name: str, description: str, id: int, rigidFaceType: apex.attribute.RigidFaceType, target: apex.EntityCollection, fittingTolerance: float, subdivisionsUdirection: int, subdivisionsVdirection: int, subdivisionsForCurves: int, deleteSelectedMeshBody: bool) -> apex.attribute.RigidFaceCollection`
Creates and returns a rigid face collection.

- `name` — Optional name for the rigid face.
- `description` — Optional string providing a description for the rigid face.
- `id` — ID of the rigid face. If omits, the system will automatically assign an ID.
- `rigidFaceType` — Defines the rigid face type.
- `target` — An entity collection to extract rigid face. If rigidFacType = BCNURBS, it is entity collection of faces/edge If rigidFacType = BCNURBS2, it is entity collection of edge If rigidFacType = BCPATCH, it is entity collection of 2D mesh body with linear elements
- `fittingTolerance` — Fitting Tolerance to extract rigid face from geometry. Omits it if Rigid face type = BCPATCH
- `subdivisionsUdirection` — Optional, Subdivisions in U direction, only use in BCNURBS creation.
- `subdivisionsVdirection` — Optional, Subdivisions in V direction, only use in BCNURBS creation.
- `subdivisionsForCurves` — Optional, Subdivisions for curves, only use in BCNURB2 creation.
- `deleteSelectedMeshBody` — Boolean value to control if delete targeted mesh body using to extraction rigid face. Only use when rigidFacType = BCPATCH

### `apex.attribute.createRigidLinkRepProperties(thermalExpansionCoefficient: float = NAN, referenceTemperature: float = NAN) -> apex.attribute.RigidLinkRepProperties`
Creates RigidLinkRepProperties.

- `thermalExpansionCoefficient` — Define Thermal Expansion Coefficient.
- `referenceTemperature` — reference Temperature.

Returns: the created RigidLinkRepProperties

### `apex.attribute.createSectionsMidsurfaceFromSolids(targetMidsurface: apex.EntityCollection, targetSolids: apex.geometry.SolidCollection, name: str = "AutoThick", description: str = "", thicknessLimit: float = 100, groupingTolerance: float = 1, selectionExtractionApproach: apex.attribute.SelectionExtractionApproach = apex.attribute.SelectionExtractionApproach.Automatic, createOffsets: bool = True) -> apex.attribute.SectionCollection`
This Function is no longer supported in Apex. Refer to apex.attribute.createFieldMidSurfaceFromSolids to determine how this capability is now supported.

- `targetMidsurface` — A collection of Surfaces/Faces, as an EntityCollection, that represents the mid-surface of the input targetSolids. The Surfaces/Faces must be meshed otherwise the method will fail. Any Surfaces in the target will be expanded internally to the set of Faces that the Surface composes and any duplicate Faces in the resulting expanded set will be silently ignored..
- `targetSolids` — a collection of Solids that represent the 3D shape that is being approximated by the combination of the targetMidsurfaces and the generated Sections..
- `name` — Name prefix of the Sections that will be created. If more than one Section is created each Section will be named using the prefix plus an appended integer to ensure name uniqueness. If omitted a default name prefix of 'AutoThick' will be used.
- `description` — A description for the Sections created by this method. If the method creates multiple Sections, this description will be assigned to each of them
- `thicknessLimit` — Optional argument to specify an upper bound for the thicknesses in the Sections created by this method. If omitted, no upper bound will be applied. thicknessLimit is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem.
- `groupingTolerance` — The groupingTolerance is used to merge constant thickness Sections with similar thicknesses. After determining the distribution of thickness across all elements referenced by the input Surfaces and Faces the methods will merge the elements into sets such that no individual element in the set has a calculated thickness different from any other in the same set by more than this tolerance and a unique Sectiosn will be created for each set of elements groupingTolerance is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem.
- `selectionExtractionApproach` — Optional enumeration controlling whether constant or variable thickness sections will be created. If omitted, the default SelectionExtractionApproach.Automatic option will be used. Use the default SelectionExtractionApproach.Automatic option to let the system decide whether a constant or variable thickness section should be created. Use SelectionExtractionApproach.ForceConstantThickness to force creation of a constant thickness section even if the system finds a variable thickness field (The system will use the average thickness of the field for the constant thickness value in this case) Use SelectionExtractionApproach.ForceVariableThickness to force creation of variable thickness fields even if the system finds that the thickness field is constant.
- `createOffsets` — optional boolean argument that allows offsets to be included or ignored from the Sections that are created. If True (default) the method will cause offsets to be included in the created Sections If False the method will NOT create offsets in the sections and only the thickness will be included. Use this option carefully since it will create Sections that assume the thickness is evenly distributed about the element midplane, even though the input geometry may not reflect that.

Returns: the created sections

Creates and returns one or more Sections (thickness, offset) from the input Surfaces/Faces and Solids and assigns the Sections to the meshes/elements associated with Surfaces/Faces. The input Surfaces must be meshed. The method assumes that the input Surface/Faces represent the mid-surface of the input Solids therefore the input Surfaces/Faces must be reasonably positioned w.r.t. the Solid mid-surface location for the method to effective although it is NOT required that the input Surfaces/Faces were created by the mid-surface tool. If None of the input Surfaces/Faces are meshed the method will throw an exception. If some of the input Surfaces/Faces are meshed Apex will attempt to create Sections and assign them to those input Surfaces/Faces and will ignore any unmeshed Faces/Surfaces Several parameters to control how the thickness and offsets of the Sections are created as provided as input arguments. The method returns zero or more Sections in a SectionCollection - if no Sections could be calculated, the Collection will be empty. Each Section will be assigned to a collection of Elements from the input Surfaces/Faces

### `apex.attribute.createShearPanel(shearMaterial: apex.attribute.Material, name: str = "#####", description: str = "#####", id: int = 0, thickness: float = NAN, nonStructuralMass: float = NAN, effectiveFactor1: float = NAN, effectiveFactor2: float = NAN) -> apex.attribute.ShearPanel`
This Function is no longer supported in Apex. Refer to apex.catalog.createPropertiesElement2D to determine how this capability is now supported.

- `shearMaterial` — The referenced material used in the ElementProperties2D to define the shear panel. It must be provided to create the ElementProperties2D.
- `name` — The name of this object as a string
- `description` — The description of this object as a string
- `id` — The Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
- `thickness` — The Thickness value of shear panel then the 2D element will have the thickness,offset and association from the Section object. If user defined the thickness/offset directly then ignore the referred section.
- `nonStructuralMass` — Nonstructural mass per unit area
- `effectiveFactor1` — Effectiveness factor for extensional stiffness along edges 1-2 and 3-4
- `effectiveFactor2` — Effectiveness factor for extensional stiffness along edges 1-2 and 3-4

Creates and returns a shear panel

### `apex.attribute.createShell(membraneMaterial: apex.attribute.Material, bendingMaterial: apex.attribute.Material, transversMaterial: apex.attribute.Material, couplingMaterial: apex.attribute.Material = None, name: str = "#####", description: str = "#####", id: int = 0, overrideSection: bool = False, thickness: float = NAN, offset: float = NAN, enableMembraneStiffness: bool = False, enableBendingStiffness: bool = False, bendingRatio: float = 1.0, enableTransverseShearStiffness: bool = False, transverseShearRatio: float = 0.833333, enableCoupling: bool = False, nonStructuralMass: float = NAN, topFiberDistance: float = NAN, bottomFiberDistance: float = NAN) -> apex.attribute.Shell`
This Function is no longer supported in Apex. Refer to apex.catalog.createPropertiesElement2D to determine how this capability is now supported.

- `membraneMaterial` — The referenced material used in the ElementProperties2D to define the membrane stiffness. It must be provided to create the ElementProperties2D.
- `bendingMaterial` — The referenced material used in the ElementProperties2D to define the bending stiffness. It must be provided to create the ElementProperties2D.
- `transversMaterial` — The referenced material used in the ElementProperties2D to define the transverse stiffness. It must be provided to create the ElementProperties2D.
- `couplingMaterial` — The optional material for membrane-bending coupling.
- `name` — The name of this object as a string
- `description` — The description for this object
- `id` — The Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
- `overrideSection` — the boolean argument to indicate whether the 2d element property overrides the section property when both of them are assigned to same entities.
- `thickness` — Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries.
- `offset` — Offset from the surface of grid points to the element reference plane.
- `enableMembraneStiffness` — Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `enableBendingStiffness` — Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `bendingRatio` — Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `enableTransverseShearStiffness` — Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `transverseShearRatio` — Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
- `enableCoupling` — Boolean value (Default = False) that defines whether or not membrane-bending coupling stiffness is activated. This value is only applicable if the 2D element property Type is set to "Shell".
- `nonStructuralMass` — Define the Nonstructural mass per unit area
- `topFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule
- `bottomFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule

Creates and returns a shell.

### `apex.attribute.createSimpleShell(referMaterial: apex.attribute.Material, name: str = "#####", description: str = "#####", id: int = 0, overrideSection: bool = False, thickness: float = NAN, offset: float = NAN, enableMembraneStiffness: bool = False, enableBendingStiffness: bool = False, enableTransverseShearStiffness: bool = False, bendingRatio: float = 1.0, transverseShearRatio: float = 0.833333, nonStructuralMass: float = NAN, topFiberDistance: float = NAN, bottomFiberDistance: float = NAN) -> apex.attribute.SimpleShell`
This Function is no longer supported in Apex. Refer to apex.catalog.createPropertiesElement2D to determine how this capability is now supported.

- `referMaterial` — The referenced material used in the ElementProperties2D. This means that all the Membrane, Bending, Transverse Shear will use the referred material. It must be provided to create the ElementProperties2D.
- `name` — Define the name for simple shell 2D element property
- `description` — Define the description for a simple 2d element property
- `id` — The Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
- `overrideSection` — the boolean argument to indicate whether the 2d element property overrides the section property when both of them are assigned to same entities.
- `thickness` — Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries. (Real or blank) Average thickness if TFLAG = 1 .
- `offset` — Offset from the surface of grid points to the element reference plan This means that all the Membrane, Bending, Transvers Shear will use the referred material
- `enableMembraneStiffness` — Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `enableBendingStiffness` — Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `enableTransverseShearStiffness` — Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `bendingRatio` — Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `transverseShearRatio` — Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
- `nonStructuralMass` — Define the Nonstructural mass per unit area
- `topFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule
- `bottomFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule

Creates and returns a simple shell

### `apex.attribute.createSpring1DRepProperties(stiffness: float = NAN, dampingCoefficient: float = NAN, stressCoefficient: float = NAN, embedded: bool = True, name: str = "", description: str = "", id: int = 0) -> apex.attribute.Spring1DRepProperties`
Create a Spring1DRepProperties.

- `stiffness` — The stiffness of the Spring1D connector.
- `dampingCoefficient` — Optional argument to define the damping coefficient of the Spring1D connector.
- `stressCoefficient` — Optional argument to define the stress coefficient of the Spring1D connector.
- `embedded` — Optional argument to define embedded.
- `name` — Optional argument to define name.
- `description` — Optional argument to define description.
- `id` — Optional argument to define id.

Returns: the created Spring1DRepProperties

### `apex.attribute.createSpringDamper1DRepProperties(stiffness: float = NAN, damping: float = NAN, mass: float = NAN, stressRecoveryCoefficient: float = NAN, strainRecoveryCoefficient: float = NAN, embedded: bool = True, name: str = "", description: str = "", id: int = 0) -> apex.attribute.SpringDamper1DRepProperties`
Create a SpringDamper1DRepProperties.

- `stiffness` — The stiffness of the SpringDamper1D connector.
- `damping` — The damping of the SpringDampe1D connector.
- `mass` — Optional argument to define the mass of 1DSpringDamper.
- `stressRecoveryCoefficient` — Optional argument to define the stress recovery coefficient for 1DSpringDamper.
- `strainRecoveryCoefficient` — Optional argument to define the strain recovery coefficient for 1DSpringDamper.
- `embedded` — Optional argument to define embedded.
- `name` — Optional argument to define name.
- `description` — Optional argument to define description.
- `id` — Optional argument to define id.

Returns: the created SpringDamper1DRepProperties

### `apex.attribute.createStressStrainCurve(name: str = "", description: str = "", xvalues: [float], ydata: [float], xunitQuantity: str = "", xunit: str = "", yunitQuantity: str = "", yunit: str = "", strainType: apex.attribute.StrainType = apex.attribute.StrainType.Type1) -> apex.attribute.StressStrainCurve`
This Function is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported.

### `apex.attribute.createTABDMP1(name: str, description: str, id: int, type: str, xdata: [float], ydata: [float]) -> apex.attribute.TABDMP1`
Create and return TABDMP1.

- `name` — An optional name. If omitted, the name is automatically assigned to the object.
- `description` — The optional description. If omitted, it is leaved as blank.
- `id` — An optional id. If omitted, system will automatically assign the existing id + 1 to it.
- `type` — Type of damping units: "G", "CRIT", or "Q"; If omitted, the default is "G". If the string is not "G", "CRIT", or "Q", the system will omits it and use the default.
- `xdata` — A list of scalar values representing the x-axis data of Natural frequency value in cycles per unit time
- `ydata` — A list of scalar values representing the y-axis data of Damping value.

### `apex.attribute.createTABRND1(name: str, description: str, id: int, xInterpolation: str, yInterpolation: str, xdata: [float], ydata: [float]) -> apex.attribute.TABRND1`
Create and return TABRND1.

- `name` — An optional name. If omitted, the name is automatically assigned to the object.
- `description` — The optional description. If omitted, it is leaved as blank.
- `id` — An optional id. If omitted, system will automatically assign the existing id + 1 to it.
- `xInterpolation` — An optional string argument ("LINEAR" or "LOG") to define a linear or logarithmic interpolation for the x-axis. If omitted, the default is "LINEAR".
- `yInterpolation` — An optional string argument ("LINEAR" or "LOG") to define a linear or logarithmic interpolation for the y-axis. If omitted, the default is "LINEAR".
- `xdata` — A list of scalar values representing the x-axis data of Frequency value, each value should be >=0.
- `ydata` — A list of scalar values representing the y-axis data of power spectral density.

### `apex.attribute.createTSTEP(name: str, description: str, id: int, timeStepNumber: [int], timeIncrement: [float], outputSkipFactor: [int]) -> apex.catalog.TSTEP`
create TSTEP object

- `name` — name of TSTEP
- `description` — description of TSTEP
- `id` — id of TSTEP
- `timeStepNumber` — A list of time step number. Ni: Number of time steps of value DTi. (Integer > 1)
- `timeIncrement` — A list of time increment. DTi: Time increment. (Real > 0.0)
- `outputSkipFactor` — A list of output skip factor. NOi: Skip factor for output. Every NOi-th step will be saved for output. (Integer > 0; Default= 1)

### `apex.attribute.createYieldBarlat(m: float, c1: float, c2: float, c3: float, c6: float) -> apex.attribute.YieldBarlat`
This Function is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported.

- `m` — M Barlat M coefficient
- `c1` — Barlat C1 coefficient
- `c2` — Barlat C2 coefficient
- `c3` — Barlat C3 coefficient
- `c6` — Barlat C6 coefficient

Constructor. Usage example: $$ New a Barlat yield criteria. myYieldCriteria = apex.attributes.createYieldBarlat(m = 1.0, c1 = 1.0, c2 = 1.0, c3 = 1.0, c6 = 1.0)

### `apex.attribute.createYieldHill(r11: float, r22: float, r33: float, r12: float, r23: float, r13: float) -> apex.attribute.YieldHill`
Constructor. Usage example: $$ New a Hills 1948 yield criteria yield criteria myYieldCriteria = apex.attributes.createYieldHill(r11 = 1.0, r22 = 1.0, r33 = 1.0, r12 = 1.0, r23 = 1.0, r13 = 1.0 )

- `r11` — Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r22` — Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r33` — Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r12` — Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r23` — Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r13` — Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.

### `apex.attribute.createYieldImpCreep(eqVonMises: float) -> apex.attribute.YieldImpCreep`
This Function is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported.

- `eqVonMises` — Equivalent (von Mises) tensile yield stress. (Real, no Default)

Constructor. Usage example: $$ New a Barlat yield criteria. myYieldCriteria = apex.attributes.createYieldImpCreep(m = 1.0, c1 = 1.0, c2 = 1.0, c3 = 1.0, c6 = 1.0)

### `apex.attribute.createYieldLinearMohr(alpha: float) -> apex.attribute.YieldLinearMohr`
This Function is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported.

- `alpha` — Specifies the parameter alpha for linear Mohr-Coulomb model.

Constructor. Usage example: $$ New a Linear Mohr-Coulomb yield criteria myYieldCriteria = apex.attributes.createYieldLinearMohr(alpha = 1.0)

### `apex.attribute.createYieldParabolicMohr(alpha: float, beta: float) -> apex.attribute.YieldParabolicMohr`
This Function is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported.

- `alpha` — Specifies the parameter alpha for linear Mohr-Coulomb model.
- `beta` — Specifies the parameter beta for parabolic Mohr-Coulomb model.

Constructor. Usage example: $$ New a Parabolic Mohr-Coulomb model yield criteria myYieldCriteria = apex.attributes.createYieldParabolicMohr(alpha = 1.0,beta = 1.0 )

### `apex.attribute.createYieldVonMises() -> apex.attribute.YieldVonMises`
This Function is no longer supported in Apex. Refer to apex.attribute.MaterialModel to determine how this capability is now supported.

Constructor. Usage example: $$ New a VonMises YieldCriteria myYieldCriteria = apex.attributes.createYieldVonMises()

### `apex.attribute.enableAttributesLibraryUIRefresh(bEnable: bool) -> None`

### `apex.attribute.get1DDampers(target: [{str:str}]) -> Damper1DCollection`
Get a collection of 1DDampers, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a 1DDamperCollection of the requested 1DDampers

### `apex.attribute.get1DSpringDampers(target: [{str:str}]) -> SpringDamper1DCollection`
Get a collection of 1DSpringDampers, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a 1DSpringDamperCollection of the requested 1DSpringDampers

### `apex.attribute.get1DSprings(target: [{str:str}]) -> Spring1DCollection`
Get a collection of 1DSprings, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a Spring1DCollection of the requested 1DSprings

### `apex.attribute.getAppliedLoads(ent: apex.Entity) -> apex.EntityCollection`

### `apex.attribute.getBeamSpan(pathName: str) -> BeamSpan`
get an existing BeamSpan

- `pathName` — of the new BeamSpan.

Returns: the created BeamSpan

### `apex.attribute.getBeamSpans(target: [{str:str}]) -> BeamSpanCollection`
Get a collection of BeamSpans, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the spans to retrieve. Valid keys are 'path' and 'name'.

Returns: a BeamSpanCollection of the requested BeamSpans

### `apex.attribute.getBolt3D(pathName: str) -> apex.attribute.Bolt3D`
Retrieves a Bolt3D using the input pathName.

- `pathName` — The pathName of the Bolt3D to retrieve.

### `apex.attribute.getBolt3Ds(target: [{str:str}]) -> apex.attribute.Bolt3DCollection`
Get a collection of Bolt3Ds, specified by target of key:value string dictionaries.

- `target` — target of dictionaries (string:string) specifying the Bolt3Ds to retrieve. Valid keys are 'path' and 'name'.

### `apex.attribute.getBushings(target: [{str:str}]) -> BushingCollection`
Get a collection of Bushings, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a BushingCollection of the requested Bushings

### `apex.attribute.getConnector(pathName: str) -> Connector`
Get a Connector THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Instead use getConnectorDiscrete.

- `pathName` — of the Connector.

### `apex.attribute.getConnectorDiscrete(pathName: str) -> ConnectorDiscrete`
Get a ConnectorDiscrete.

- `pathName` — of the ConnectorDiscrete.

### `apex.attribute.getConnectorDiscretes(target: [{str:str}]) -> ConnectorDiscreteCollection`
Get a collection of Connectors, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a ConnectorDiscreteCollection of the requested Connectors

### `apex.attribute.getConnectors(target: [{str:str}]) -> ConnectorCollection`
Get a collection of Connectors, specified by target of key:value string dictionaries THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Instead use getConnectorDiscretes.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a ConnectorCollection of the requested Connectors

### `apex.attribute.getContactBodies() -> ContactBodyCollection`
Get a collection of contact bodies from the whole model.

Returns: a ContactBodyCollection

### `apex.attribute.getContactBody(name: str) -> apex.attribute.ContactBody`
Retrieves a contact body using the input name.

- `name` — The name of the contact body to retrieve.

### `apex.attribute.getContactTable(name: str) -> apex.attribute.ContactTable`
Retrieves a contact table using the input pathName.

- `name` — Optional pathName for the ContactTable.

Returns: a ContactTable using the input pathName

### `apex.attribute.getContactTables() -> apex.attribute.ContactTableCollection`
Get all ContactTable.

Returns: a collection of ContactTable from the whole model.

### `apex.attribute.getDiscreteFEMField(pathName: str) -> apex.attribute.DiscreteFEMField`
Retrieves a discrete FEM field using the input path name.

- `pathName` — The path name of the discrete FEM field to retrieve.

### `apex.attribute.getDiscreteFEMFields(target: [{str:str}]) -> apex.attribute.DiscreteFEMFieldCollection`
Get a collection of discrete FEM field from the whole model.

Returns: a DiscreteFEMFieldCollection

### `apex.attribute.getDiscreteTie(pathName: str) -> DiscreteTie`
get an existing DiscreteTie

- `pathName` — of the new DiscreteTie.

Returns: the created DiscreteTie

### `apex.attribute.getDiscreteTies(target: [{str:str}]) -> DiscreteTieCollection`
Get a collection of DiscreteTies, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the DiscreteTies to retrieve. Valid keys are 'path' and 'name'.

Returns: a DiscreteTieCollection of the requested DiscretTies

### `apex.attribute.getElementBeamSpan(elem: apex.mesh.Element) -> apex.attribute.BeamSpan`

### `apex.attribute.getElementFields(elem: apex.mesh.Element) -> apex.attribute.DiscreteFEMFieldCollection`

### `apex.attribute.getElementMaterial(elem: apex.mesh.Element) -> apex.attribute.Material`

### `apex.attribute.getElementProperty2D(elem: apex.mesh.Element) -> apex.attribute.PropertiesElement2D`

### `apex.attribute.getElementProperty3D(elem: apex.mesh.Element) -> apex.attribute.PropertiesElement3D`

### `apex.attribute.getElementShellBehavior(elem: apex.mesh.Element) -> apex.attribute.ShellBehavior`
This Function is no longer supported in Apex. Refer to apex.attribute.getElementProperty2D to determine how this capability is now supported.

### `apex.attribute.getElementShellSection(elem: apex.mesh.Element) -> apex.attribute.ShellSection`
This Function is no longer supported in Apex. Refer to apex.attribute.getElementFields to determine how this capability is now supported.

### `apex.attribute.getFasteners(target: [{str:str}]) -> FastenerCollection`
Get a collection of Fasteners, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a FastenerCollection of the requested Fasteners

### `apex.attribute.getFieldDictionary() -> {str:apex.attribute.DiscreteFEMField}`
Get all apex.attribute.DiscreteFEMField objects in this Catalog.

Returns: a DiscreteFEMField dictionary which key is apex.attribute.DiscreteFEMField name and value is apex.attribute.DiscreteFEMField corresponding object.

### `apex.attribute.getFlexibleLinks(target: [{str:str}]) -> FlexibleLinkCollection`
Get a collection of FlexibleLinks, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a FlexibleLinkCollection of the requested FlexibleLinks

### `apex.attribute.getGaps(target: [{str:str}]) -> GapCollection`
Get a collection of Gaps, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a GapCollection of the requested Gaps

### `apex.attribute.getInteraction(pathName: str) -> apex.attribute.Interaction`
Get an Interaction.

- `pathName` — of the Interaction

### `apex.attribute.getInteractions(target: [{str:str}]) -> InteractionCollection`
Get a collection of Interactions, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the ties to retrieve. Valid keys are 'path' and 'name'.

Returns: a InteractionCollection of the requested Interactions

### `apex.attribute.getInterfacePoint(pathName: str) -> apex.attribute.InterfacePoint`
Get an InterfacePoint.

- `pathName` — of the InterfacePoint.

### `apex.attribute.getJoint(pathName: str) -> Joint`
get an existing Joint

- `pathName` — of the new Joint.

Returns: the created Joint

### `apex.attribute.getJoints(target: [{str:str}]) -> JointCollection`
Get a collection of Joints, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the Joints to retrieve. Valid keys are 'path' and 'name'.

Returns: a JointCollection of the requested Joints

### `apex.attribute.getLayeredPanel(pathName: str) -> LayeredPanel`
get an existing LayeredPanel

- `pathName` — of the new LayeredPanel.

Returns: the created LayeredPanel

### `apex.attribute.getLayeredPanels(target: [{str:str}]) -> LayeredPanelCollection`
Get a collection of LayeredPanels, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the LayeredPanels to retrieve. Valid keys are 'path' and 'name'.

Returns: a LayeredPanelCollection of the requested LayeredPanels

### `apex.attribute.getMeshDependentTie(pathName: str) -> MeshDependentTie`
Get a getMeshDependentTie.

- `pathName` — of the MeshDependentTie

### `apex.attribute.getMeshDependentTieByFullName(pathName: str) -> MeshDependentTie`
Get a getMeshDependentTieByFullName.

- `pathName` — of the MeshDependentTie

### `apex.attribute.getMeshDependentTies(target: [{str:str}]) -> MeshDependentTieCollection`
Get a collection of MeshDependentTies, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the ties to retrieve. Valid keys are 'path' and 'name'.

Returns: a MeshDependentTieCollection of the requested MeshDependentTies

### `apex.attribute.getNSMCombination(name: str) -> apex.attribute.NSMCombination`
Get NSMCombination by name.

- `name` — Optional name for the NSM Combination.

Returns: a NSM Combination using the input pathName

### `apex.attribute.getNSMCombinations() -> apex.attribute.NSMCombinationCollection`
Get all NSMCombination.

Returns: a collection of NSM Combinations from the whole model.

### `apex.attribute.getNodeConstraints(node: apex.mesh.Node) -> apex.EntityCollection`

### `apex.attribute.getNodeTie(pathName: str) -> NodeTie`
get an existing NodeTie

- `pathName` — of the new NodeTie.

Returns: the created NodeTie

### `apex.attribute.getNodeTieByID(id: int) -> NodeTie`
get an existing NodeTie

- `id` — of the new NodeTie.

Returns: the created NodeTie

### `apex.attribute.getNodeTies(target: [{str:str}]) -> NodeTieCollection`
Get a collection of NodeTies, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the NodeTies to retrieve. Valid keys are 'path' and 'name'.

Returns: a NodeTieCollection of the requested NodeTies

### `apex.attribute.getNonstructuralMass(name: str) -> apex.attribute.NonstructuralMass`
Get a NonstructuralMass.

- `name` — of the NonstructuralMass.

### `apex.attribute.getNonstructuralMassDictionary() -> {str:apex.attribute.NonstructuralMass}`
Get all apex.attribute.NonstructuralMass objects in this Catalog.

Returns: a NonstructuralMass dictionary which key is apex.attribute.NonstructuralMass name and value is apex.attribute.NonstructuralMass corresponding object.

### `apex.attribute.getNonstructuralMasses() -> NonstructuralMassCollection`
Get a collection of NonstructuralMasses,.

Returns: a NonstructuralMassCollection

### `apex.attribute.getPointMass(pathName: str) -> PointMass`
Get a PointMass.

- `pathName` — of the PointMass.

### `apex.attribute.getPointMasses(target: [{str:str}]) -> PointMassCollection`
Get a collection of PointMasses, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the masses to retrieve. Valid keys are 'path' and 'name'.

Returns: a PointMassCollection of the requested PointMasses

### `apex.attribute.getRigidFace(name: str) -> apex.attribute.RigidFace`
Retrieves a rigid face using the input pathName.

- `name` — The name of the rigid face to retrieve.

### `apex.attribute.getRigidFaces() -> RigidFaceCollection`
Get a collection of rigid faces from the whole model.

Returns: a RigidFaceCollection

### `apex.attribute.getRigidLinks(target: [{str:str}]) -> RigidLinkCollection`
Get a collection of RigidLinks, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the connectors to retrieve. Valid keys are 'path' and 'name'.

Returns: a RigidLinkCollection of the requested RigidLinks

### `apex.attribute.getSensors(target: [{str:str}]) -> PointSensorCollection`
Get a collection of Sensors, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the sensors to retrieve. Valid keys are 'path' and 'name'.

Returns: a PointSensorCollection of the requested Sensors

### `apex.attribute.getTABDMP1(name: str = "#####") -> apex.attribute.TABDMP1`

### `apex.attribute.getTABDMP1s() -> apex.EntityCollection`

### `apex.attribute.getTABRND1(name: str = "#####") -> apex.attribute.TABRND1`

### `apex.attribute.getTABRND1s() -> apex.EntityCollection`

### `apex.attribute.removeAnalysisSystem(targets: apex.EntityCollection) -> bool`
remove analysis coordinate system from target entities.

- `targets` — the targets that analysis coordinate system to be removed. It can be Assembly, Part, GeometryBody, Cell, Face, Edge, Vertex, MeshBody, Element, or a set of nodes. In current release, only supports nodes as assigned targets. If the targets are other entities, the system will give an exception: Unsupported targets.

### `apex.attribute.removeBodiesFromMeshDependentTie(target: apex.EntityCollection, bodies: apex.EntityCollection) -> MeshDependentTieCollection`
removes Geometry Bodies from a collection MeshDependentTies.

- `target` — collection of MeshDependentTies that the method will operate on
- `bodies` — collection of Solids, Surfaces and Curves that the method will attempt to remove from the target ties. Bodies of other types will be ignored

Returns: MeshDependentTieCollection that contains all ties that were modified (but not deleted).

target is a collection of MeshDependentTies and bodies is a collection of Geometry Bodies that may contain apex.geometry.Solid, apex.geometry.Surface or apex.geometry.Curve bodies only. If the bodies collection includes Points or Geometry bodies that are not currently associated with any of the ties they will be ignored. If all of the bodies are removed from any tie or if only a single body remains after the bodies are removed the tie will be deleted. The method returns a MeshDependentTieCollection that contains all ties that were modified (but not deleted).

### `apex.attribute.targetBeamSpan(ent: apex.Entity) -> apex.attribute.BeamSpan`

### `apex.attribute.targetReferencedBy(ent: apex.Entity) -> apex.EntityCollection`

### `apex.attribute.unassign(target: apex.EntityCollection) -> bool`
Unassigns PropertiesElement3D or PropertiesElement2D or Material from the target.

- `target` — The target that properties or material to be removed. If omitted, all properties or material will be unassigned from all associated entities.

### `apex.attribute.unassignPropertiesElement3D(target: apex.EntityCollection = None) -> bool`
Unassigns PropertiesElement3D from the target. Note that if target is not provided, all PropertiesElement3Ds will be unassigned from all associated entities.

- `target` — The optional target that PropertiesElement3D to be removed. If omitted, all PropertiesElement3Ds will be unassigned from all associated entities.

### `apex.attribute.unassignPropertiesElement3Ds(properties: apex.attribute.PropertiesElement3DCollection = None) -> bool`
Unassigns one or more PropertiesElement3D from the model.

- `properties` — The collection of PropertiesElement3D to be removed. If omitted, all PropertiesElement3Ds will be unassigned from the model.

### `apex.attribute.updateFieldMidsurfaceFromFaces(targetMidsurfaceFaces: apex.EntityCollection, thicknessLimit: float, groupingTolerance: float, name: str, targetTopFaces: apex.geometry.FaceCollection, targetBottomFaces: apex.geometry.FaceCollection, selectionExtractionApproach: apex.attribute.SelectionExtractionApproach, createOffsets: bool) -> apex.attribute.ThicknessOffsetFieldMidsurfaceCollection`
Updates/creates and returns one or more auto thickness fields associated with elements from a single meshed Surface using the input 'Top' and 'Bottom' FaceCollections Given a single meshed Face, a pair of collections of Faces representing the 'Top' and 'Bottom' boundaries of the shape that the field is intended to describe and some other controlling parameters - updates any existing auto thickness fields or creates New(fields,distributions of thickness and offsets) using the relative positions of the input meshed faces and 'Top' and 'Bottom' boundaries.

- `targetMidsurfaceFaces` — the Face that is associated to the elements who's fields will be updated All fields associated to any any elements associated with this Face will be updated. New fields will be created if required.
- `thicknessLimit` — Optional argument to specify an upper bound for the thicknesses in the fields updated/created by this method. If omitted, no upper bound will be applied. thicknessLimit is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem
- `groupingTolerance` — The groupingTolerance is used to merge constant thickness fields with similar thicknesses. After determining the distribution of thickness across all elements referenced by the input Surfaces and Faces the methods will merge the elements into sets such that no individual element in the set has a calculated thickness different from any other in the same set by more than this tolerance and a unique Sectiosn will be created for each set of elements groupingTolerance is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem
- `name` — Name prefix of the fields that will be created. If more than one field is created each field will be named using the prefix plus an appended integer to ensure name uniqueness. Existing fields that are modified retain their own existing names If omitted a default name prefix of 'AutoThick' will be used.
- `targetTopFaces` — a collection of Faces that represent the 'Top' boundary of the region that the fields created by this method are intended to represent. If omitted, the Faces that are currently associated with the targetMidsurface are used. If no 'Top' Faces are currently associated with the targetMidsurface this argument MUST be supplied or the method will throw an exception. Faces that are currently associated with the targetMidsurface can be extracted directly from the targetMidsurface using methods/properties of the Face class
- `targetBottomFaces` — a collection of Faces that represent the 'Bottom' boundary of the region that the fields created by this method are intended to represent. If omitted, the Faces that are currently associated with the targetMidsurface are used. If no 'Top' Faces are currently associated with the targetMidsurface this argument MUST be supplied or the method will throw an exception. Faces that are currently associated with the targetMidsurface can be extracted directly from the targetMidsurface using methods/properties of the Face class
- `selectionExtractionApproach` — Optional enumeration controlling whether constant or variable thickness fields will be created. If omitted, the default SelectionExtractionApproach.Automatic option will be used. Use the default SelectionExtractionApproach.Automatic option to let the system decide whether a constant or variable thickness field should be created. Use SelectionExtractionApproach.ForceConstantThickness to force creation of a constant thickness field even if the system finds a variable thickness field (The system will use the average thickness of the field for the constant thickness value in this case) Use SelectionExtractionApproach.ForceVariableThickness to force creation of variable thickness fields even if the system finds that the thickness field is constant
- `createOffsets` — optional boolean argument that allows offsets to be included or ignored from the fields that are created. If True (default) the method will cause offsets to be included in the created fields If False the method will NOT create offsets in the fields and only the thickness will be included. Use this option carefully since it will create fields that assume the thickness is evenly distributed about the element midplane, even though the input geometry may not reflect that.*

Returns: the created fields.

### `apex.attribute.updateSectionMidsurfaceFromFaces(targetMidsurfaceFaces: apex.EntityCollection, thicknessLimit: float, groupingTolerance: float, name: str = "", description: str = "", targetTopFaces: apex.geometry.FaceCollection = None, targetBottomFaces: apex.geometry.FaceCollection = None, selectionExtractionApproach: apex.attribute.SelectionExtractionApproach = apex.attribute.SelectionExtractionApproach.Automatic, createOffsets: bool = True) -> apex.attribute.SectionCollection`
This Function is no longer supported in Apex. Refer to apex.attribute.updateFieldMidsurfaceFromFaces to determine how this capability is now supported.

- `targetMidsurfaceFaces` — the Face that is associated to the elements who's Sections will be updated All Sections associated to any any elements associated with this Face will be updated. New Sections will be created if required.
- `thicknessLimit` — Optional argument to specify an upper bound for the thicknesses in the Sections updated/created by this method. If omitted, no upper bound will be applied. thicknessLimit is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem
- `groupingTolerance` — The groupingTolerance is used to merge constant thickness Sections with similar thicknesses. After determining the distribution of thickness across all elements referenced by the input Surfaces and Faces the methods will merge the elements into sets such that no individual element in the set has a calculated thickness different from any other in the same set by more than this tolerance and a unique Sectiosn will be created for each set of elements groupingTolerance is a Length quantity and must be defined using the unit of Length from the ScriptUnitSystem
- `name` — Name prefix of the Sections that will be created. If more than one Section is created each Section will be named using the prefix plus an appended integer to ensure name uniqueness. Existing Sections that are modified retain their own existing names If omitted a default name prefix of 'AutoThick' will be used.
- `description` — A description for any new Sections created by this method. If the method creates multiple new Sections, this description will be assigned to each of them
- `targetTopFaces` — a collection of Faces that represent the 'Top' boundary of the region that the Sections created by this method are intended to represent. If omitted, the Faces that are currently associated with the targetMidsurface are used. If no 'Top' Faces are currently associated with the targetMidsurface this argument MUST be supplied or the method will throw an exception. Faces that are currently associated with the targetMidsurface can be extracted directly from the targetMidsurface using methods/properties of the Face class
- `targetBottomFaces` — a collection of Faces that represent the 'Bottom' boundary of the region that the Sections created by this method are intended to represent. If omitted, the Faces that are currently associated with the targetMidsurface are used. If no 'Top' Faces are currently associated with the targetMidsurface this argument MUST be supplied or the method will throw an exception. Faces that are currently associated with the targetMidsurface can be extracted directly from the targetMidsurface using methods/properties of the Face class
- `selectionExtractionApproach` — Optional enumeration controlling whether constant or variable thickness sections will be created. If omitted, the default SelectionExtractionApproach.Automatic option will be used. Use the default SelectionExtractionApproach.Automatic option to let the system decide whether a constant or variable thickness section should be created. Use SelectionExtractionApproach.ForceConstantThickness to force creation of a constant thickness section even if the system finds a variable thickness field (The system will use the average thickness of the field for the constant thickness value in this case) Use SelectionExtractionApproach.ForceVariableThickness to force creation of variable thickness fields even if the system finds that the thickness field is constant
- `createOffsets` — optional boolean argument that allows offsets to be included or ignored from the Sections that are created. If True (default) the method will cause offsets to be included in the created Sections If False the method will NOT create offsets in the sections and only the thickness will be included. Use this option carefully since it will create Sections that assume the thickness is evenly distributed about the element midplane, even though the input geometry may not reflect that.*

Returns: the created sections.

Updates/creates and returns one or more Sections associated with elements from a single meshed Surface using the input 'Top' and 'Bottom' FaceCollections Given a single meshed Face, a pair of collections of Faces representing the 'Top' and 'Bottom' boundaries of the shape that the Section is intended to describe and some other controlling parameters - updates any existing Sections or creates New(Sections,distributions of thickness and offsets) using the relative positions of the input meshed faces and 'Top' and 'Bottom' boundaries.

## Classes in this module

Full method signatures are in `api/classes/apex.attribute.md`.

`BeamShape`, `BeamShape1DProfile`, `BeamShapeC`, `BeamShapeCAlternate`, `BeamShapeCollection`, `BeamShapeCruciform`, `BeamShapeFactory`, `BeamShapeH`, `BeamShapeHat`, `BeamShapeHatClosed`, `BeamShapeHollowDoubleRectangular`, `BeamShapeHollowRectangularAsymmetric`, `BeamShapeHollowRectangularSymmetric`, `BeamShapeHollowRound`, `BeamShapeHollowRoundByThickness`, `BeamShapeIAsymmetric`, `BeamShapeISymmetric`, `BeamShapeL`, `BeamShapeNumeric`, `BeamShapeProperty`, `BeamShapeSolidHexagon`, `BeamShapeSolidRectangle`, `BeamShapeSolidRound`, `BeamShapeT`, `BeamShapeTInverted`, `BeamShapeTSideways`, `BeamShapeU`, `BeamShapeZ`, `BeamSpan`, `BeamSpanCollection`, `Bolt`, `Bolt3D`, `Bolt3DCollection`, `Bushing`, `BushingCollection`, `BushingRepProperties`, `BushingRepPropertiesCollection`, `Connector`, `ConnectorCollection`, `ConnectorDiscrete`, `ConnectorDiscreteCollection`, `ConnectorDiscreteProperty`, `ConnectorProperty`, `ConstitutiveModel`, `ContactBody`, `ContactBodyCollection`, `ContactBodyProperty`, `ContactTable`, `ContactTableCollection`, `CylindricalJoint`, `Damper1D`, `Damper1DCollection`, `Damper1DRepProperties`, `Damper1DRepPropertiesCollection`, `DiscreteDataTable`, `DiscreteFEMField`, `DiscreteFEMFieldCollection`, `DiscreteRegion`, `DiscreteTie`, `DiscreteTieCollection`, `DisplacementConstraintProperty`, `Elasticity`, `ElasticityLinear2DAniso`, `ElasticityLinear2DOrtho`, `ElasticityLinear3DAniso`, `ElasticityLinear3DOrtho`, `ElasticityLinear3DTransvIso`, `ElasticityLinearIso`, `Failure`, `Failure2DAniso`, `Failure2DOrth`, `Failure3DOrth`, `Failure3DTransvIso`, `FailureIso`, `Fastener`, `FastenerCollection`, `FastenerRepProperties`, `FastenerRepPropertiesCollection`, `FlexibleLink`, `FlexibleLinkCollection`, `FlexibleLinkRepProperties`, `Gap`, `GapCollection`, `GapRepProperties`, `Interaction`, `InteractionCollection`, `InteractionPropertyGeometric`, `InteractionPropertyPhysical`, `InteractionRep`, `InterfacePoint`, `InterfacePointCollection`, `Joint`, `JointCollection`, `LayeredPanel`, `LayeredPanelCollection`, `Mass`, `Material`, `MaterialCollection`, `MaterialCoverageRegion`, `MaterialCoverageRegionCollection`, `MaterialModel`, `MaterialOrientationField2D`, `MaterialOrientationField2DAlignCurve`, `MaterialOrientationField2DCoordinate`, `MaterialSheet`, `MaterialSheetCollection`, `MaterialSheetStack`, `MaterialSheetStackCollection`, `MeshDependentTie`, `MeshDependentTieCollection`, `NSMCombination`, `NSMCombinationCollection`, `NodeTie`, `NodeTieCollection`, `NonstructuralMass`, `NonstructuralMassCollection`, `PerfectlyPlastic`, `PlanarJoint`, `Plasticity`, `PlasticityHardeningSlope`, `PlasticityStressStrain`, `Ply`, `PlyCollection`, `PointMass`, `PointMassCollection`, `PointMassMatrix`, `PointSensor`, `PointSensorCollection`, `PrismaticJoint`, `Properties2DModel`, `Properties3DModel`, `PropertiesElement2D`, `PropertiesElement2DCollection`, `PropertiesElement3D`, `PropertiesElement3DCollection`, `PropertiesElement3DHomogeneous`, `Property2DCoverageRegion`, `Property2DCoverageRegionCollection`, `RemotePointEntity`, `RevoluteJoint`, `RigidFace`, `RigidFaceCollection`, `RigidLink`, `RigidLinkCollection`, `RigidLinkRepProperties`, `SectionCollection`, `ShearPanel`, `Shell`, `ShellBehavior`, `ShellBehaviorCollection`, `ShellSection`, `SimpleShell`, `Spans`, `SphericalJoint`, `Spring1D`, `Spring1DCollection`, `Spring1DRepProperties`, `Spring1DRepPropertiesCollection`, `SpringDamper1D`, `SpringDamper1DCollection`, `SpringDamper1DRepProperties`, `SpringDamper1DRepPropertiesCollection`, `StressStrainCurve`, `TABDMP1`, `TABRND1`, `ThermalExpansion`, `ThermalExpansionLinear2DAnisotropic`, `ThermalExpansionLinear2DOrthotropic`, `ThermalExpansionLinear3DAnisotropic`, `ThermalExpansionLinear3DOrthotropic`, `ThermalExpansionLinear3DTransvIso`, `ThermalExpansionLinearIsotropic`, `ThicknessOffsetField`, `ThicknessOffsetFieldConstant`, `ThicknessOffsetFieldMidsurface`, `ThicknessOffsetFieldMidsurfaceCollection`, `ViscoElasticity`, `ViscoElasticity2DAniso`, `ViscoElasticity3DAniso`, `YieldBarlat`, `YieldCriteria`, `YieldHill`, `YieldImpCreep`, `YieldLinearMohr`, `YieldParabolicMohr`, `YieldVonMises`, `Zone`, `ZoneCollection`

