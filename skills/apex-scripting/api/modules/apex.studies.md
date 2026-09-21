# apex.studies

(apex.studies module) Objects and methods for setting up and executing simulations.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.studies.ArcLengthMethod`: `Crisfield`, `RiksRamm`, `ModifiedRiksRamm`
  - Arc length method

`apex.studies.ArtificialDamping`: `No`, `Always`, `DampingEnergy`, `Automatic`
  - Artificial damping

`apex.studies.AugmentationMethod`: `NotUse`, `Automatic`, `Constant`, `Bilinear`
  - Augmentation Method in segment to segment contact method

`apex.studies.ContactMethod`: `SegmentToSegment`, `NodeToSegment`
  - Contact method

`apex.studies.DTIBlockType`: `SystemCells`, `FileManagement`, `ExecutiveControl`, `CaseControl`, `BulkData`
  - Direct Text Input Block are typed and this enumeration is used to identify all Direct Text Input Block types

`apex.studies.DTIExportOptions`: `doNotWrite`, `writeAtStart`, `writeAtEnd`
  - Direct Text Input Export Options are typed and this enumeration is used to identify all Direct Text Input Export Options types

`apex.studies.DataDeckEcho`: `Unset`, `Unsorted`, `Sorted`
  - Echo (i.e., printout) of the Bulk Data

`apex.studies.ExecutionStatus`: `CompletedNoErrors`, `CompletedWithDiagnostics`, `CompletedWithErrors`, `NotSubmitted`, `Running`, `Submitted`
  - ExecutionStatus is an enumerated value the defines the calculation status of the Event. The ExecutionStatus always starts out as "NotSubmitted" and can subsequently change to various other states (descriptions are provided for each) such as "Running", "CompletedNoErrors" etc. ExecutionStatus is composed by the Event but is aggregated at the Step and Scenario level

`apex.studies.FailureAssessMethod`: `safetyFactor`, `stressGoal`
  - To Enumeration Failure Assess Method. Options are provide with "safetyFactor" and "stressGoal"

`apex.studies.FailureCriteria`: `FFFThumbRule`, `TsaiHill`, `TsaiWu`, `VonMises`
  - This used to Enumeration failure Criteria method. Options are provide with "FFFThumbRule", "TsaiHill", "TsaiWu" and "VonMises"

`apex.studies.FrictionType`: `Frictionless`, `BilinearCoulomb`, `BilinearShear`
  - Friction type

`apex.studies.IncrementalScheme`: `Fixed`, `Adaptive`, `ArcLength`
  - Incremental scheme

`apex.studies.InitialStepState`: `PreviousStep`, `StepInThisLoadCase`, `StepInAnotherLoadCase`
  - Initial step state

`apex.studies.IterationProcedure`: `PureFullNewton`, `ControlledIterations`
  - Nastran solution 400 iteration strategies - "Pure Full Newton" and "Controlled Iterations"

`apex.studies.MNFMassInvariantOptions`: `partial`, `constant`, `full`, `none`, `rigid`
  - To select mass invariant outputs during calculation of Modal Neutral Files

`apex.studies.ManufacturingMethod`: `genericAM`, `metalAM`, `FFF`
  - To Enumeration Manufacturing Method. Options are provide with "AM Generic", "Metal AM" and "FFF"

`apex.studies.MassCalculationMethod`: `Coupled`, `Lumped`
  - Mass calculation method

`apex.studies.MultiBodyDynamic`: `Dynamic`, `QuasiStatic`
  - Multi Body Scenario Dynamic Step Simulation Type

`apex.studies.NastranAnalysisType`: `Statics`, `LinearCombination`, `RepeatedOutput`, `Symmetry`, `SymmetricCombination`, `Modes`, `ModalOutput`, `Buckling`, `ModalTransient`, `DirectTransient`, `ModalFrequency`, `DirectFrequency`, `ModalComplexEigenvalue`, `DirectComplexEigenvalue`, `CyclicStatics`, `CyclicModes`, `CyclicBuckling`, `CyclicFrequency`, `StaticAeroelasticity`, `StaticAeroelasticDivergence`, `Flutter`, `DynamicAeroelasticity`, `NonlinearStatics`, `NonlinearTransient`, `NonlinearSteadyStateHeat`, `NonlinearTransientHeat`, `DesignOptimization`, `NonlinearHarmonic`, `ALL`, `NonlinearStatics1XX`, `Hot2Cold`, `SteadyStateHeat153`, `CoupledThermalStructural153`, `NonlinearTransient159`, `Undefined`
  - To identify the type of analysis that will be carried out by a LoadCaseItem (Subcase, Step, Substep)

`apex.studies.NastranSolutionType`: `Statics_101`, `Modes_103`, `Buckling_105`, `DirectComplexEigenvalue_107`, `DirectFrequency_108`, `DirectTransient_109`, `ModalComplexEigenvalue_110`, `ModelFrequency_111`, `ModalTransient_112`, `CyclicStatics_114`, `CyclicModes_115`, `CyclicBuckling_116`, `CyclicDirectFrequency_118`, `NonlinearHarmonic_128`, `NonlinearTransient_129`, `StaticAeroelasticity_144`, `AerodynamicFlutter_145`, `DynamicAeroelasticity_146`, `TransientStructuralThermal_153`, `DesignOptimization_200`, `Nonlinear_400`, `ALL`, `Undefined`
  - To identify the type of a ScenarioNastran

`apex.studies.OutputRequestQuantities`: `Stress`, `NonlinearStress`, `Strain`, `StrainEnergy`, `ElementForce`, `NodalForce`, `SectionForce`, `AppliedLoad`, `ConstraintReactionForce`, `ContactResults`, `NodalKineticEnergy`, `Displacement`, `Velocity`, `Acceleration`, `Undefined`
  - Output request quantity for scenario, load case or step

`apex.studies.PredefinedOption`: `QLinear`, `Mildly`, `Severely`, `NoCharacterization`
  - Describing the severity of the nonlinearity present in this Step

`apex.studies.ReductionStrategy`: `NoneOption`, `Low`, `Medium`, `High`
  - Argument to define the reduction strategy

`apex.studies.ScenarioConfiguration`: `Static`, `NormalModes`, `LinearBucklingNoPrestiffening`, `LinearBucklingWithPrestiffening`, `ModalFrequencyNoPrestiffening`, `ModalFrequencyWithPrestiffening`, `ModalTransferFrequencyNoPrestiffening`, `ModalTransferFrequencyWithPrestiffening`, `ModalTransientNoprestiffening`, `ModalTransientWithPrestiffening`, `ModalRandomNoPrestiffening`, `ModalRandomWithPrestiffening`, `ShockResponseNoPrestiffening`, `ShockResponseWithPrestiffening`, `MultiBodyTransient`, `MultiBodyTransientStaticPreload`, `MultibodyScripted`, `GenerativeDesign`, `NastranSol400Static`
  - This enumeration is used to identify common Scenario configurations such as Static, Normal Modes, Buckling, Frequency Response etc. It is used to conveniently create specific configurations of Scenarios and avoid the use of multiple "addStep()" calls

`apex.studies.SeparationIn`: `Current`, `Next`
  - Contact Separation In which increment

`apex.studies.SeparationMethod`: `Force`, `AbsoluteStressWithForceArea`, `AbsoluteStressExtrapolation`, `RelativeStressForceArea`, `RelativeStressExtrapolation`
  - Contact Separation Method

`apex.studies.ShapeQuality`: `Preview`, `Balanced`, `FineTune`
  - To indicate what shape quality can be made during Apex generative design optimization. Options are provide with "Preview", "Balanced" and "Fine Tune"

`apex.studies.SimulationType`: `Static`, `NormalModes`, `LinearBuckling`, `ModalFrequency`
  - This enumeration is used to identify common simulation types such as Static, Normal Modes, Buckling, Frequency Response etc. The possible SimulationType Options in Apex

`apex.studies.StepOutput`: `LastIncrement`, `Everyincrement`, `FixedIncrement`
  - Artificial damping

`apex.studies.StepSettingMethod`: `Smart`, `Advanced`
  - Step setting method

`apex.studies.StepType`: `Static`, `NormalModes`, `LinearBuckling`, `ModalFrequency`
  - Steps are typed and this enumeration is used to identify all supported Step types

`apex.studies.StrutDensity`: `Dense`, `Medium`, `Sparse`
  - To indicate what strut density can be made during Apex generative design optimization. Options are provide with "Dense", "Medium" and "Sparse"

## Classes in this module

Full method signatures are in `api/classes/apex.studies.md`.

`ANALYSIS`, `AUTOSPC`, `AXISYMMETRIC`, `AdvancedSettingGenerativeDesign`, `BC`, `BCONCHK`, `BCONTACT`, `BCPARA`, `BucklingSimulationSettings`, `BucklingStep`, `DBSAVE`, `DEFORM`, `DLOAD`, `DesignRules`, `DirectTextInput`, `DynamicsStep`, `ECHO`, `Event`, `EventCollection`, `ExecutedScenario`, `FEMCHECK`, `FREQUENCY`, `FRF`, `FailureSetting3DOrth`, `FailureSetting3DTranseIso`, `FailureSettingIso`, `FailureSettings`, `FrequencyResponseSimulationSettings`, `GROUNDCHECK`, `GenerativeDesignStaticStep`, `IC`, `IRLOAD`, `IncrementalSchemeAdaptive`, `IncrementalSchemeArcLength`, `IncrementalSchemeFixed`, `InteractionControl`, `IterationAndConvergence`, `KeyResult`, `LINE`, `LOAD`, `LoadCase`, `LoadCaseCollection`, `LoadCaseItem`, `MAPMODES`, `MASTER`, `MAXLINES`, `MAXMINDEF`, `METHOD`, `MFREQUENCY`, `MNFGenerationProperty`, `MODES`, `MODESELECT`, `MONITOR`, `MeshlessGenerativeDesignStep`, `ModalFrequencyStep`, `ModesSimulationSettings`, `ModesStep`, `MultiBodyTransientStep`, `NLBUCK`, `NLIC`, `NLOPRM`, `NLSTEP`, `NSM`, `NastranSol400StepSettings`, `NastranSol400StepSettingsStatic`, `ODSFREQ`, `OFREQUENCY`, `OMODES`, `OTIME`, `PAGE`, `PARTN`, `PEAKOUT`, `POST`, `RANDOM`, `RCROSS`, `RESVEC`, `RIGID`, `RSDAMP`, `SDAMPING`, `SLDSKIN`, `SMETHOD`, `SPC`, `STATSUB_BUCKLING`, `STATSUB_PRELOAD`, `STOCHASTICS`, `SUBSEQ`, `SUBSEQ1`, `SUPORT1`, `SYMSEQ`, `Scenario`, `ScenarioCollection`, `ScenarioCommand`, `ScenarioNastran`, `ScenarioNastranCollection`, `ScenarioSetFrequency`, `ScenarioSetFrfcompId`, `ScenarioSetGridComponent`, `ScenarioSetGridId`, `ScenarioSetModeId`, `ScenarioSetNastran`, `ScenarioSetRandId`, `ScenarioSetTime`, `SimulationSettings`, `SimulationSettingsBucklingNastran`, `SimulationSettingsGenerativeDesign`, `SimulationSettingsModesNastran`, `SimulationSettingsNastranSol400`, `SimulationSettingsStaticNastran`, `SolverControlSettingsNastran`, `StaticSimulationSettings`, `StaticStep`, `StaticStepNastranSol400`, `Step`, `StepCollection`, `StepNastran`, `StepNastranCollection`, `Study`, `StudyGenerativeDesign`, `SubcaseNastran`, `SubcaseNastranCollection`, `SubstepNastran`, `SubstepNastranCollection`, `TEMPERATURE`, `TSTEP`, `WEIGHTCHECK`

