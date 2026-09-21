# apex.post

(apex.post module) Post-Processing functions used to visualize results data.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.post.ColorMapSegmentMethod`: `Linear`, `Manual`
  - Possible ColorMapSegmentMethod options in Apex. Specify ColorMapSegmentMethod by using the syntax apex.post.ColorMapSegmentMethod."<enum_value>" For example: apex.post.ColorMapSegmentMethod.Linear

`apex.post.CompositeFailure`: `FailureIndex`, `StrengthRatio`
  - Possible CompositeFailure Options in Apex. Specify CompositeFailure by using the syntax apex.post.CompositeFailure."<enum_value>" For example: apex.post.CompositeFailure.FailureIndex

`apex.post.ContourStyle`: `Fringe`, `Fill`
  - Possible ContourStyle options in Apex. Specify ContourStyle by using the syntax apex.post.ContourStyle."<enum_value>" For example: apex.post.ContourStyle.Fringe

`apex.post.CoordinateSystemMethod`: `Global`, `Local`, `Material`, `Ply`, `User`
  - Which method is used to define coordinate system transformations to the result quantity data if it is vector or tensor type. Global - Display data is presented in the Gloabl coordinate system. Local - Display data is presented in aLlocal coordinate system. Material - Display data is presented in the Materical coordinate system of each element. Ply - Display data in presented in the Ply coordinate system. This option is only valid for ply base composite result quantities and typically varies per ply and per element., User - Display data is presented in the User defined coordinate system

`apex.post.DeformScalingMethod`: `Absolute`, `Relative`
  - Of supported deformation scaling methods in Apex. Specify DeformScalingMethod by using the syntax apex.post.DeformScalingMethod."<enum_value>" For example: apex.post.DeformScalingMethod.Absolute. Absolute scaling method causes the associated deformation scale factor to be used to directly scale the calculated displacements for display purposes. Relative scaling methods causes the associated deformation scale factor to be used to scale the calculated displacements relative to the Model size for display purposes

`apex.post.ElementNodalProcessing`: `Averaged`, `NonAveraged`, `Difference`, `SmartAveraged`
  - Of the supported element nodal processing methods in Apex. Some element based results quantities such as stress or strain are calculated by the solver at each Node of every Element. When Elements share Nodes (the element are connected) multiple result values are calculated for each shared Node - one per attached Element. When creating fringe or vector plots several options are possible to display such results, for example - Average all of the result data values at shared Nodes, reducing the data to a single value per Node. - Find the maximum difference between all result data values at shared Nodes, reducing the data to a single value per Node. - Leave the data unchanged at shared nodes, resulting in multiple data values per shared Node Specify ElementNodalProcessing by using the syntax apex.post.ElementNodalProcessing."<enum_value>" For example: apex.post.ElementNodalProcessing.Averaged Averaged causes the set of results data values at shared Nodes arising from multiple attached elements to be averaged, reducing the data to a single value per Node. NonAveraged leaves all the results data values at shared Nodes arising from multiple attached elements unchanged, resulting in multiple values per Node. This type of processing can cause discontinuity in the results data field across element boundaries. Difference determines that maximum difference between any two values of the results data at shared Nodes arising from multiple attached elements, reducint the data to a single value per Node

`apex.post.LayerEnvelopingMethod`: `Max`, `Min`, `Average`, `Unknown`
  - How data (ResultQuantity/ResultDerivation)from multiple layers in a shell element will be reduced to a single value. Since ContourVisualizations display just a single scalar value at each location on the target, if data for more than one layer is supplied an enveloping strategy is deployed to reduce the multiple input values to a single output/display value. Currently supported enveloping strategies are Max, Min and Average. Specify LayerEnvelopingMethod by using the syntax apex.post.LayerEnvelopingMethod."<enum_value>" For example: apex.post.LayerEnvelopingMethod.Max. Max - Use to display the Maximmum data value from the set of Layers. Min - Use to display the Minimum data value from the set of Layers. Average - Use to display the Averate data value across the set of Layers

`apex.post.LayerIdentificationMethod`: `Position`, `Ply`
  - Possible LayerIdentificationMethod options in Apex. Shell elements support (some) results data at multiple positions through the thickness. These positions can be identified using either the absolute position, starting at the bottom of the shell and incrementing or by using global (Panel) ply IDs. Specify a LayerIdentificationMethod by using the syntax apex.post.LayerIdentificationMethod"<enum_value>" For example: apex.post.LayerIdentificationMethod.Position. Position defines the layer using an integer position ID. Ply identifies the layer using Ply names

`apex.post.ProbeTargetUpdateMode`: `Add`, `Remove`
  - That controls how Probe targets Entities are processed when the target entities are changed. Specify ProbeTargetUpdateMode by using the syntax apex.post.ProbeTargetUpdateMode."<enum_value>" For example: apex.post.ProbeTargetUpdateMode.VectAddor3D Add will add all supplied Entities to any Entities that are already in the Probe target. Remove will remove all supplied Entities from the set of Entities that are already in the Probe target

`apex.post.ResultDerivation`: `VonMises`, `ShearMax`, `Comp1`, `Comp2`, `Comp3`, `Shear12`, `Shear23`, `Shear13`, `PrincipalMax`, `PrincipalMid`, `PrincipalMin`, `Invariant1`, `Tresca`, `Octahedral`, `Hydrostatic`, `StrainEnergy`, `StrainEnergyDensitiy`, `StrainEnergyPercentTotal`, `Vector`, `Magnitude`, `Component1`, `Component2`, `Component3`, `Resultant12`, `Resultant23`, `Resultant13`, `MomentBendingAxial`, `MomentBendingAxialMax`, `MomentBendingAxialMin`, `F1`, `F2`, `F12`, `M1`, `M2`, `M12`, `ForceAxial`, `ForceShearPlane1_V1`, `ForceShearPlane2_V2`, `TorqueTotal`, `TorqueWarping`, `MomentBendingPlane1_M1`, `MomentBendingPlane2_M2`, `Hill`, `Hoffman`, `TsaiWu`, `FailureStrain1Max`, `FailureStrain2Max`, `FailureStrain12Max`, `FailuresStressShearTrans13Max`, `FailuresStressShearTrans23Max`, `StressShearTransverse13`, `StressShearTransverse23`, `Other`, `MassFractionEffectiveTotal`, `MassMatrixEffective`, `MassMatrixRigidBody`, `MassFractionEffectiveTranslational`, `MassFractionEffectiveRotational`, `Transform16`, `CrossPlotResultant`, `CrossPlotX`, `CrossPlotY`, `CrossPlotZ`, `NormalContactStress`, `FrictionContactStress1`, `FrictionContactStress2`, `AxialStress`, `CombinedAxialBendingStress`, `TorsionalStress`, `ShearStressY`, `ShearStressZ`, `AxialStrain`, `CombinedAxialBendingStrain`, `TorsionalStrain`, `ShearStrainY`, `ShearStrainZ`, `CompMax`, `CompMin`, `Invariant2`, `Invariant3`, `Prin2DMajorCompX`, `Prin2DMajorCompY`, `Prin2DMinorCompX`, `Prin2DMinorCompY`, `PrinInterCompX`, `PrinInterCompY`, `PrinInterCompZ`, `PrinMajorCompX`, `PrinMajorCompY`, `PrinMajorCompZ`, `PrinMinorCompX`, `PrinMinorCompY`, `PrinMinorCompZ`, `ContactGridCheckMag`, `ContactFrictionForceMag`, `ContactFrictionStress1`, `ContactFrictionStress2`, `ContactNormalForceMag`, `ContactNormalStress`, `GridCheckReserve1`, `GridCheckReserve2`, `EffCreepStrain`, `EffCreepStress`, `EffPlasticStrain`, `EffPlasticStress`, `EquivalentStress`, `GasketClosure`, `GasketPressure`, `PlasticGasketClosure`, `Tensor1D`, `Tensor2D`, `TransverseShearStrainXZ`, `TransverseShearStrainYZ`, `ContactStatus`, `Undefined`
  - Of supported ResultDerivations in Apex. ResultsDerivations are used to reduce vector or Tensor results data to a single scalar value either by identify a specific vector/tensor component or by performing some computation on the vector or tensor data that results in a single value - for example calculation of the scalar VonMises stress from a stress tensor or the Resultant displacement from a displacement vector. Specify a ResultDerivation using the syntax apex.post.ResultDerivation."<enum_value>" For example: apex.post.ResultDerivation.VonMises

`apex.post.ResultFileType`: `AdamsCar`
  - By result file import functions to identify the type of result file that is being imported AdamsCar is used to request the import of an Adams/Car results file (.res)

`apex.post.ResultQuantity`: `Stress`, `Strain`, `StrainEnergy`, `DisplacementTranslational`, `DisplacementRotational`, `VelocityTranslational`, `VelocityRotational`, `AccelerationTranslational`, `AccelerationRotational`, `ForceAppliedLoad`, `MomentAppliedLoad`, `ForceReaction`, `MomentReaction`, `NodalForceBalanceAll`, `NodalMomentBalanceAll`, `NodalForceBalanceElements`, `NodalMomentBalanceElements`, `KineticEnergyNodalTranslational`, `KinecticEnergyNodalRotational`, `ForceAttachment`, `MomentAttachment`, `ForceConnector`, `MomentConnector`, `ForceSection`, `MomentSection`, `StressBeam`, `StrainBeam`, `ForceElement`, `MomentElement`, `ForceBeam`, `MomentBeam`, `FailureComposite`, `StressInterlaminar`, `Eigenvalue`, `ModalMassData`, `TransformMotion`, `ClearanceMotion`, `EnvelopeMotion`, `ForceGlueNormal`, `MomentGlueNormal`, `ForceGlueTangential`, `MomentGlueTangential`, `ForceInterface`, `MomentInterface`, `InternalForceAndMoment`, `CrossPlot`, `ContactStress`, `NormalContactForce`, `FrictionContactForce`, `ContactAdjustmentTranslational`, `ContactAdjustmentRotational`, `EigenVectorTranslational`, `EigenVectorRotational`, `ForceConnectorAxial`, `MomentConnectorAxial`, `OneDimElementForce`, `OneDimElementMoment`, `OneDimElementWarpingTorque`, `TorsionalStress`, `AxialBendingStress`, `AxialStress`, `TorsionalStrain`, `AxialBendingStrain`, `AxialStrain`, `StrainEnergyDensity`, `StrainEnergyPercent`, `AppliedLoadCriticalMoment`, `AppliedLoadCriticalForce`, `ContactDistanceMag`, `ContactFrictionForceMag`, `ContactFrictionStress1`, `ContactFrictionStress2`, `ContactNormalForceMag`, `ContactNormalStress`, `GridCheckReserve1`, `GridCheckReserve2`, `EffCreepStrain`, `EffCreepStress`, `EffPlasticStrain`, `EffPlasticStress`, `EquivalentStress`, `GasketClosure`, `GasketPressure`, `GridCheckDistance`, `InterlaminarStrainTensor`, `NodalKineticEnergyRot`, `NodalKineticEnergyTrans`, `KineticStrainEnergy`, `KineticElementStrainEnergyDensity`, `KineticPercentStrainEnergy`, `NormalStrain`, `NormalStress`, `PlasticGasketClosure`, `AxialForce1D`, `TotalTorque1D`, `ConnectorDisplacementAxial`, `ConnectorStrainRot`, `ConnectorStrainTrans`, `ConnectorStressRot`, `ConnectorStressTrans`, `ConnectorVelocityAxial`, `CompInterlaminarNormalStress`, `CompInterlaminarShearStress`, `CompPlyStress`, `DisplacementCriticalTranslational`, `DisplacementCriticalRotational`, `ContactStatus`, `Undefined`
  - Of all supported ResultQuantities in Apex. Specify a ResultQuantity using the syntax apex.post.ResultQuantity."<enum_value>" For example: apex.post.ResultQuantity.Stress

`apex.post.TargetEntityType`: `Node`, `ObjectEnds`, `ObjectMidPoint`
  - Possible TargetEntityType options in Apex. Specify TargetEntityType by using the syntax apex.post.TargetEntityType."<enum_value>" For example: apex.post.TargetEntityType.Node ObjectEnds and ObjectMidPoint are used when objects such as Connectors are targeted

`apex.post.VectorColorMethod`: `VectorValue`, `Component`
  - How displayed vectors will be colored. VectorValue, the default option causes individual vectors to be color coded according to the ColorMap color that maps to the vector value. This displays a plot where every vector is color coded according to its value. The Component option causes individual vectors to be color coded according to their component color. Colors can be specified independently for each component however all occurrences of that vector component will have the same color, regardless of its value

`apex.post.VectorComponent`: `Resultant`, `Component1`, `Component2`, `Component3`, `Resultant12`, `Resultant23`, `Resultant13`, `F1`, `F2`, `M1`, `M2`, `ForceAxial`, `ForceShearPlane1_V1`, `ForceShearPlane2_V2`, `TorqueTotal`, `MomentBendingPlane1_M1`, `MomentBendingPlane2_M2`, `ForceResultant`, `ForceX`, `ForceY`, `ForceZ`, `ForceXY`, `ForceYZ`, `ForceXZ`, `MomentResultant`, `MomentX`, `MomentY`, `MomentZ`, `MomentXY`, `MomentYZ`, `MomentXZ`, `ForceMoment1Axial`, `ForceMoment1Plane1`, `ForceMoment1Plane2`, `Axial1D1`, `TorqueTotal2`, `TorqueTotal3`, `Undefined`
  - Possible VectorComponent options in Apex. Specify VectorComponent by using the syntax apex.post.VectorComponent."<enum_value>" For example: apex.post.VectorComponent.Component1 is used for most vector data type specified by apex.post.ResultQuantity. The enumeration provides values for each of three orthogonal vector components of a vector in three dimensions, plut three "2D Resultants" and one "3D Resultant". F1, F2 are used with Shell Element Force, apex.post.ResultQuantity.ForceElement. M1, M2 are used with Shell Element Moment, apex.post.ResultQuantity.MomentElement. ForceAxial, ForceShearPlane1_V1, ForceShearPlane2_V2 are used with apex.post.ResultQuantity.ForceBeam. TorqueTotal, MomentBendingPlane1_M1, MomentBendingPlane2_M2 are used with apex.post.ResultQuantity.MomentBeam

`apex.post.VectorDisplayStyle`: `Vector3D`, `Vector1D`, `VectorLine`
  - Possible VectorDisplayStyle options in Apex. Specify VectorDisplayStyle by using the syntax apex.post.VectorDisplayStyle."<enum_value>" For example: apex.post.VectorDisplayStyle.Vector3D Vector3D is used to request a high fidelity solid (3D) arrow rendering. Vector1D is used to request an 3D arrow with line segment arrow rendering. VectorLine is used to render a line segment only, no arrow head

`apex.post.VectorOriginLocation`: `Tip`, `Tail`
  - Possible VectorOriginLocation options in Apex. Specify VectorOriginLocation by using the syntax apex.post.VectorOriginLocation."<enum_value>" For example: apex.post.VectorOriginLocation.Tip

`apex.post.VectorScalingMethod`: `Scaled`, `Constant`
  - Possible VectorScalingMethod options in Apex. Specify VectorScalingMethod by using the syntax apex.post.VectorScalingMethod."<enum_value>" For example: apex.post.VectorScalingMethod.Scaled

## Module functions

### `apex.post.createColorMap(name: str = "#####", colorMapSegmentMethod: apex.post.ColorMapSegmentMethod = apex.post.ColorMapSegmentMethod.Linear, start: float = 0.0f, end: float = 0.0f, tableValues: [apex.post.TableValue] = [], isLocked: apex.ApexBool = ApexBoolFalse, useOutOfRangeColors: apex.ApexBool = ApexBoolFalse, displayContinuousColors: apex.ApexBool = ApexBoolFalse) -> apex.post.ColorMap`
Creates a color map.

- `name` — ColorMap name. ColorMap names must be unique.
- `colorMapSegmentMethod` — Enumeration of type apex.post.ColorMapSegmentMethod: "Linear" or "Manual" are supported. If omitted the ColorMap will be created using a "Linear" colorMapSegmentMethod.
- `start` — The start value of the scalar data that will be color mapped. This value may represent either the minimum or maximum value of the scalar data. If the spectrum is not locked and the colorMapSegmentMethod is linear, then the minimum value of the quantity will be used.
- `end` — The end value of the scalar data that will be color mapped. This value may represent either the maximum or minimum value of the scalar data. If the spectrum is not lockedand the colorMapSegmentMethod is linear , then the maximum value of the quantity will be used.
- `tableValues` — Used if colorMapSegmentMethod = Manual, A list of monotonically increasing or decreasing data values pairs (data value, apex::ColorRGB) that define the color segments of the scalar data that will be color mapped. If the scalar data represents a quantity that has units these values must be entered usint the units system that is active int he script (ScriptUnitSystem).
- `isLocked` — if true, ColorMap definition can't be changed
- `useOutOfRangeColors` — Optional argument that sets how scalar data that is "out of range" (above or below the start and end values) is color mapped. If "False" data that is outside the range defined by the "start" and "end" values will be colored with the "start" or "end" values. If "True", data that is out of the range of "start" and "end" values will be colored with the out of range colors.
- `displayContinuousColors` — Optional argument that sets whether the ColorMap will use continuous colors (True) or not (False).

### `apex.post.createDataSeriesOverSteps(targets: apex.EntityCollection, steps: apex.studies.StepCollection, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation, unitYaxis: str, unitXaxis: str = "") -> apex.post.DataSeriesOverStepsCollection`
Creates a DataSeriesOverSteps for use in plotting XY chart diagrams based on targets results.

- `targets` — the Plot target from which the results data extracted
- `steps` — the steps collection from which the results extracted
- `resultQuantity` — the results quantity that user want to check and plot
- `resultDerivation` — The Result Derivation that user want to check and plot
- `unitYaxis` — the unit used in the Plot in Y
- `unitXaxis` — he unit used in the Plot X

### `apex.post.createDataSeriesTimeHistory(target: apex.Entity, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation, unit: str) -> apex.post.DataSeriesTransient`
Creates a DataSeriesTimeHistory for use in XY Charting.

- `target` — The Entity for which the time history data series will be generated.
- `event` — The event from which the time history will be extracted.
- `resultQuantity` — The time varying result quantity that will returned in the data series. The quantity must exist in all Events
- `resultDerivation` — The result derivation to include in the DataSeries as an apex.post.ResultDerivation enumeration. Must be one Magnitude, Component1, Component2, or Component3
- `unit` — The name of the unit in which the data is provided. Units vary by result quantity type. For example valid units for Axial Force include 'N', 'lbf', 'dyn' etc. whereas valid units for Torsion include 'Nm', 'lbf in' etc.

### `apex.post.createDataSeriesVMTBeamSpan(target: apex.attribute.BeamSpan, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation, unit: str) -> apex.post.DataSeriesVMTBeamSpan`
Creates a DataSeriesVMTBeamSpan for use in plotting VMT diagrams based on Beam Spans.

- `target` — The BeamSpan that the DataSeries will be based on.
- `event` — The Event that the VMT results quantities will be extracted from.
- `resultQuantity` — The result quantity to include in the DataSeries as an apex.post.ResultQuantity enumeration. Must be either ForceBeam or MomentBeam.
- `resultDerivation` — The result derivation to include in the DataSeries as an apex.post.ResultDerivation enumeration. Must be one of ForceAxial, ForceShearPlane1_V1, ForceShearPlane2_V2, TorqueTotal, MomentBendingPlane1_M1 or MomentBendingPlane2_M2.
- `unit` — The name of the unit in which the data is provided. Valid units vary by result quantity type. For example valid units for ForceAxial include 'N', 'lbf', 'dyn', etc. whereas valid units for TorqueTotal include 'N m', 'lbf in', etc.

### `apex.post.createDataSeriesVMTSensorArray(target: apex.instrument.XSectionForceSensorArray, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, vectorComponent: apex.post.VectorComponent, unit: str) -> apex.post.DataSeriesVMTSensorArray`
Create a DataSeriesVMTSensorArray for use in plotting VMT diagrams based on X-Section Sensor Arrays.

- `target` — The XSectionForceSensorArray that the DataSeries will be based on.
- `event` — The Event that the VMT results quantities will be extracted from.
- `resultQuantity` — The result quantity to include in the DataSeries as an apex.post.ResultQuantity enumeration. Must be either ForceSection or MomentSection.
- `vectorComponent` — The vector component to include in the DataSeries as an apex.post.VectorComponent enumeration. Must be one of Resultant, Component1, Component2, Component3, Resultant12, Resultant23, or Resultant13.
- `unit` — The name of the unit in which the data is provided. Valid units vary by result quantity type. For example valid units for ForceSection, Component1 include 'N', 'lbf', 'dyn', etc. whereas valid untis for ForceMoment, Component3 include 'N m', 'lbf in', etc.

### `apex.post.createKeyResult(name: str, description: str, target: apex.Entity, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation, resultDataSetIndex: int = 0, independentValue: float = NAN) -> apex.studies.KeyResult`
Create a KeyResult and adds it to the KeyResultCatalog.

- `name` — An optional name for this KeyResult. If omitted, the system will assign a default name
- `description` — An optional description for this KeyResult.
- `target` — The entity used for the KeyResult.
- `event` — Target Event of multibody dynamics transient Scenario for key results.
- `resultQuantity` — An enumeration of all supported ResultQuantities in Apex. In createKeyReult method, this argument currently only accept apex.post.ResultQuantity.ForceInterface and apex.post.ResultQuantity.MomentInterface, as Apex only supports load mapping of Force and Moment for now.
- `resultDerivation` — An enumeration of supported ResultDerivations in Apex. In createKeyReult method, this argument currently only accept apex.post.ResultDerivation.Magnitude, apex.post.ResultDerivation.Component1, apex.post.ResultDerivation.Component2 and apex.post.ResultDerivation.Component3,
- `resultDataSetIndex` — An optional integer to identify the frame of the result data to be used. This index is 1 based. For example, resultDataSetIndex = 10 indicates that result data at frame 10 is used. Both of this argument and 'independentValue' are optional, please make sure that at least one is specified. If both or none are specified, the API will error out.
- `independentValue` — An optional value used when the Event from which the key result is being extracted from is not atomic - for example when the Event represents a transient, frequency or incremental load/response. independentValue is ignored if the Event does not represent a variable quantity. Both of this argument and 'resultDataSetIndex' are optional, please make sure that at least one is specified. If both or none are specified, the API will error out.

### `apex.post.createResultProbe0D(dataVisualization: apex.post.DataVisualization) -> apex.post.ResultProbe0D`
Create a results 0D Probe that can be used to probe DataVisualizations.

- `dataVisualization` — DataVisualization that results will be returned.

### `apex.post.createStatePlot(event: apex.studies.Event, resultDataSetIndex: [int]) -> apex.post.StatePlot`
Creates and returns a StatePlot object. The "event" and optional "resultDataSetIndex" arguments are used to identify the results data that will be displayed in the plot. "event" identifies which Scenario that will be plotted. "resultDataSetIndex" index is required when the Event produces multiple discrete result data - for example, Normal Modes and Buckling simulations can give rise to multiple modes per event and the resultDataSetIndex is used to select which mode to use. In future releases, this index will also be used to select specific frequency, time and increment results data sets. The returned StatePlot is empty and hidden on creation and must be populated with DataVisualizations (Deform, Contour, Vector etc.) before it can display anything useful.

- `event` — The Scenario Event that created the results data that will be used in the created StatePlot.
- `resultDataSetIndex` — If the Scenario Event associated with this State Plot generates multiple sets of results data, for example, Normal Modes or Buckling, this argument defines which set of results data will be used. The index is 1 based. In the case of an Event associated with a Normal Modes analysis this index identifies the specific mode that will be plotted. In the case of an Event associated with a Buckling analysis this index identifies the specific buckling mode that will be plotted.

### `apex.post.createVectorComponentColor() -> {apex.post.VectorComponent:apex.ColorRGB}`
Creates a VectorComponentColor empty map used for VectorVisualization.

This can be populated with std::map syntax vectorComponentColor[apex::post::VectorComponent key] = ColorRGB() value

### `apex.post.createXSectionForceSensorPlot(xSectionForceSensors: apex.instrument.XSectionForceSensorCollection, loadEvent: apex.studies.Event) -> apex.datavis.XSectionForceSensorPlot`
Create a Cross section force sensor plot from an input collection of XSectionForceSensors and a Scenario Event. The plot that is created will include the force sensor displays of every sensor in the collection based on the results data from the single Scenario Event.

- `xSectionForceSensors` — The collection of cross section force sensors that will be displayed in the plot. The xSectionForceSensors should be got from execution scenario for post.
- `loadEvent` — The Scenario Event from which the raw force data will be extracted. This Event must be composed by a Static Step type. The Static Step may belong to any Scenario that includes a Static Step. This includes Static Steps that are used to generate pre-load for use in subsequent Steps - for example, Frequency Response or other dynamic steps. Results data, specifically "Section Force" (Grid point forces in Nastran) results quantities must exist for this Event otherwise the method will raise an exception.

### `apex.post.createXSectionForceSensorPlotFromSensorArray(xSectionForceSensorArray: apex.instrument.XSectionForceSensorArray, loadEvent: apex.studies.Event) -> apex.datavis.XSectionForceSensorPlot`
Create a Cross section force sensor plot from an input XSectionForceSensorArray and Scenario Event. The plot that is created will include the force sensor displays of every sensor in the array, based on the results data from the single Scenario Event.

- `xSectionForceSensorArray` — The XSectionForceSensorArray that will be displayed in the plot. The XSectionForceSensorArray should be got from execution scenario for post.
- `loadEvent` — The Scenario Event from which the raw force data will be extracted. This Event must be composed by a Static Step type. The Static Step may belong to any Scenario that includes a Static Step. This includes Static Steps that are used to generate pre-load for use in subsequent Steps - for example, Frequency Response or other dynamic steps. Results data, specifically "Section Force" (Grid point forces in Nastran) results quantities must exist for this Event otherwise the method will raise an exception.

### `apex.post.deleteColorMap(colorMap: apex.post.ColorMap) -> None`
Delete a ColorMap.

### `apex.post.deleteStatePlot(name: str = "#####") -> None`
Delete StatePlot.

### `apex.post.exitPostProcess() -> None`
Exits Post Processing.

### `apex.post.getColorMap(name: str) -> apex.post.ColorMap`
Get a ColorMap using ColorMap name.

### `apex.post.getCurrentStatePlot() -> apex.post.StatePlot`
get current StatePlot.

### `apex.post.getDataSeriesOverSteps(chart: apex.chart.ChartPlotXY, targets: apex.EntityCollection, quantity: apex.post.ResultQuantity, derivation: apex.post.ResultDerivation) -> apex.post.DataSeriesOverStepsCollection`
find DataSeriesOverSteps list by the input parameters of DataSeriesOverSteps

- `chart` — The chart which is used for query.
- `targets` — The nodes that the DataSeriesOverSteps list will be based on.
- `quantity` — the quantity that the DataSeriesOverSteps list used.
- `derivation` — the derivation that the DataSeriesOverSteps list used.

### `apex.post.getDataSeriesTimeHistory(chart: apex.chart.ChartPlotXY, target: apex.Entity, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation) -> apex.post.DataSeriesTransient`
Gets a DataSeriesTransient from XY Charting.

- `chart` — The chart which is used for query.
- `target` — The Entity for which the time history data series will be generated.
- `event` — The event from which the time history will be extracted.
- `resultQuantity` — The time varying result quantity that the data series used.
- `resultDerivation` — The result derivation that the data series used.

### `apex.post.getDataSeriesVMTBeamSpan(chart: apex.chart.ChartPlotXY, target: apex.attribute.BeamSpan, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation) -> apex.post.DataSeriesVMTBeamSpan`
Query a DataSeriesVMTBeamSpan by the input target, event, quantity and derivation in the input chart.

- `chart` — The chart which is used for query.
- `target` — The BeamSpan that the DataSeries will be based on.
- `event` — The Event that the VMT results quantities will be extracted from.
- `resultQuantity` — The result quantity to include in the DataSeries as an apex.post.ResultQuantity enumeration. Must be either ForceBeam or MomentBeam.
- `resultDerivation` — The result derivation to include in the DataSeries as an apex.post.ResultDerivation enumeration. Must be one of ForceAxial, ForceShearPlane1_V1, ForceShearPlane2_V2, TorqueTotal, MomentBendingPlane1_M1 or MomentBendingPlane2_M2.

### `apex.post.getDataSeriesVMTSensorArray(chart: apex.chart.ChartPlotXY, target: apex.instrument.XSectionForceSensorArray, event: apex.studies.Event, resultQuantity: apex.post.ResultQuantity, vectorComponent: apex.post.VectorComponent) -> apex.post.DataSeriesVMTSensorArray`
Query a DataSeriesVMTSensorArray by the input target, event, quantity and component in the input chart.

- `chart` — The chart which is used for query.
- `target` — The XSectionForceSensorArray that the DataSeries will be based on.
- `event` — The Event that the VMT results quantities will be extracted from.
- `resultQuantity` — The result quantity to include in the DataSeries as an apex.post.ResultQuantity enumeration. Must be either ForceSection or MomentSection.
- `vectorComponent` — The vector component to include in the DataSeries as an apex.post.VectorComponent enumeration. Must be one of Resultant, Component1, Component2, Component3, Resultant12, Resultant23, or Resultant13.

### `apex.post.getStatePlot(event: apex.studies.Event) -> apex.post.StatePlot`
returns an existed StatePlot object.

- `event` — The Scenario Event that is used created the StatePlot.

## Classes in this module

Full method signatures are in `api/classes/apex.post.md`.

`ChartPlot`, `ColorMap`, `ContourVisualization`, `DataSeriesOverSteps`, `DataSeriesOverStepsCollection`, `DataSeriesTransient`, `DataSeriesVMTBeamSpan`, `DataSeriesVMTSensorArray`, `DataVisualization`, `DeformVisualization`, `ResultProbe0D`, `StatePlot`, `TableValue`, `VectorVisualization`

