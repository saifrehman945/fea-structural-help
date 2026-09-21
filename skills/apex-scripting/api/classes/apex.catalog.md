# apex.catalog — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.catalog.CatalogElementProperty`
Container class for all PropertiesElement2D and PropertiesElement3D objects in the project. Only one instance of CatalogElementProperty is supported within a Project.
Properties: `propertiesElement2Ds`, `propertiesElement3Ds`

Methods:

#### `getPropertiesElement2D(name: str) -> apex.attribute.PropertiesElement2D`
Retrieves specified PropertiesElement2D object in the catalog.

- `name` — Name of specified PropertiesElement2D.

- `getPropertiesElement2DDictionary() -> {str:apex.attribute.PropertiesElement2D}` — A dictionary containing all apex.attribute.PropertiesElement2D objects in the catalog. The dictionary key is a string type and represents the name of the PropertiesElement2D. The dictionary value is the apex.attribute.PropertiesElement2D object corresponding to the name.
- `getPropertiesElement2Ds() -> apex.attribute.PropertiesElement2DCollection` — Get all of PropertiesElement2D objects in the catalog.
#### `getPropertiesElement3D(name: str) -> apex.attribute.PropertiesElement3D`
Retrieves specified PropertiesElement3D object in the catalog.

- `name` — Name of specified PropertiesElement3D.

- `getPropertiesElement3DDictionary() -> {str:apex.attribute.PropertiesElement3D}` — A dictionary containing all apex.attribute.PropertiesElement3D objects in the catalog. The dictionary key is a string type and represents the name of the PropertiesElement3D. The dictionary value is the apex.attribute.PropertiesElement3D object corresponding to the name.
- `getPropertiesElement3Ds() -> apex.attribute.PropertiesElement3DCollection` — Get all of PropertiesElement3D objects in the catalog.

## `apex.catalog.CatalogMaterial`  (extends `Entity`)
Properties: `materials`, `materialSheets`, `materialSheetStacks`

Methods:

#### `getMaterial(name: str) -> apex.attribute.Material`
retrieves specified material in this catalog.

- `name` — Name of specified material.

#### `getMaterialSheet(name: str) -> apex.attribute.MaterialSheet`
retrieves specified material sheet in this catalog.

- `name` — Name of specified material sheet.

#### `getMaterialSheetStack(name: str) -> apex.attribute.MaterialSheetStack`
retrieves specified material sheet stack in this catalog.

- `name` — Name of specified material sheet stack.

- `getMaterialSheetStacks() -> apex.attribute.MaterialSheetStackCollection` — retrieves all of the MaterialSheetStacks in this catalog.
- `getMaterialSheets() -> apex.attribute.MaterialSheetCollection` — retrieves all of the MaterialSheets in this catalog.
- `getMaterials() -> apex.attribute.MaterialCollection` — retrieves all of the Materials in this catalog.

## `apex.catalog.CatalogParameters`
CatalogParameters is a collection of parameters sets, it can be customized and shared in Apex and user can add and remove parameters sets in the catalog.
Properties: `parametersSets`

Methods:

#### `activeParametersSet(parametersSet: apex.catalog.ParametersSet) -> None`
activate one parameters set

- `parametersSet` — The parameter set to be activated, omits it of ParametersType = CaseControl

#### `createParamSet(name: str, description: str, params: {str:value}, parametersType: apex.catalog.ParametersType) -> apex.catalog.ParametersSet`
create a parameters set.

- `name` — name of parameters set.
- `description` — description of parameters set.
- `params` — dictionary to specify a set of parameters, the key is name of PARAM, the value is the value of the PARAM, below is the example: {'AUTOMSET':"NO", 'K6ROT':100.00, 'SNORM':20.00}
- `parametersType` — Parameter type to be used in case control or bulk data, the default is case control.

- `getActiveParametersSetBulkData() -> apex.catalog.ParametersSet` — get the active parameters set.
#### `getParameterSet(name: str) -> apex.catalog.ParametersSet`
Return the parameter set by name.

- `name` — name of the parameter set

- `getParametersSets() -> apex.catalog.ParametersSetCollection` — Retrieves All available parameter sets in this catalog.
#### `remove(target: apex.catalog.ParametersSet, targets: apex.catalog.ParametersSetCollection) -> None`
Remove parameter set from this parameters catalog. If removing parameter set associated to a scenario, it will be remove from scenario as well.

- `target` — remove a parameter set.
- `targets` — remove parameter set collection.


## `apex.catalog.CatalogSystemCells`
CatalogParameters is a collection of parameters sets, it can be customized and shared in Apex and user can add and remove parameters sets in the catalog.
Properties: `systemCellsSets`

Methods:

#### `activeSystemCellsSet(systemCellsSet: apex.catalog.SystemCellsSet) -> None`
Activate one system cells set.

- `systemCellsSet` — Specify the system cells set to be activated

#### `createSystemCellsSet(name: str, description: str, systemCells: {str:value}) -> apex.catalog.SystemCellsSet`
create a parameters set.

- `name` — name of a system cells set.
- `description` — description of a system cells set.
- `systemCells` — dictionary to specify the values for system cells in the set, the key is the name of system cell, the value is the expression assigned to the system cell, below is the example: {'BUFFSIZE':10000, 'NLINES':60, 'MAXLINES':2000000}

- `getActiveSystemCellsSet() -> apex.catalog.SystemCellsSet` — get the active system cells set.
#### `getSystemCellsSet(name: str) -> apex.catalog.SystemCellsSet`
Return the system cells set by name.

- `name` — name of system cells set

- `getSystemCellsSets() -> apex.catalog.SystemCellsSetCollection` — Retrieves All available system cells sets in this catalog.
#### `remove(target: apex.catalog.SystemCellsSet, targets: apex.catalog.SystemCellsSetCollection) -> None`
Remove system cells set from this system cells catalog. If removed system cells set is associated to a scenario, it will be remove from scenario as well.

- `target` — remove a system cells set.
- `targets` — remove system cells set collection.


## `apex.catalog.DAMPING`  (extends `Entity`, `IName`)
DAMPING: Specifies the values for parameter damping and/or selects optional HYBRID damping.
Properties: `hybridDamping`, `hybridStructuralDampingFrequency`, `id`, `massScaleFactor`, `materialDampingFrequency`, `materialDampingScaleFactor`, `removeRotorStiffnessMassStructuralDamping`, `stiffnessScaleFactor`, `structuralDampingCoefficient`, `structuralDampingFrequency`

Methods:

- `getHybridDamping() -> int` — Gets ID of HYBDAMP entry for hybrid damping.
- `getHybridStructuralDampingFrequency() -> float` — Gets Average frequency for calculation of hybrid structural damping in transient response.(Real ≥ 0.0; Default = 0.0)
- `getId() -> int` — Gets SID: Set identification number.
- `getMassScaleFactor() -> float` — Gets Scale factor for mass portion of Rayleigh damping.
- `getMaterialDampingFrequency() -> float` — Gets Average frequency for calculation of material damping in transient response.(Real ≥ 0.0; Default = 0.0)
- `getMaterialDampingScaleFactor() -> float` — Gets Scale factor for material damping.
- `getRemoveRotorStiffnessMassStructuralDamping() -> str` — Gets Remove rotor stiffness, mass, and structural damping from the hybrid damping calculation (Character: YES or NO; Default=YES)
- `getStiffnessScaleFactor() -> float` — Gets Scale factor for stiffness portion of Rayleigh damping.
- `getStructuralDampingCoefficient() -> float` — Gets Structural damping coefficient.
- `getStructuralDampingFrequency() -> float` — Gets Average frequency for calculation of structural damping in transient response.(Real ≥ 0.0; Default = 0.0)
#### `update(name: str, description: str, id: int, structuralDampingCoefficient: float, massScaleFactor: float, stiffnessScaleFactor: float, hybridDamping: int, materialDampingScaleFactor: float, removeRotorStiffnessMassStructuralDamping: str, structuralDampingFrequency: float, materialDampingFrequency: float, hybridStructuralDampingFrequency: float) -> None`
update the DAMPING

- `name` — name of the DAMPING
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


## `apex.catalog.EIGB`  (extends `Entity`, `IName`)
EIGB: Real Eigenvalue Extraction Data for buckling analysis.
Properties: `componentNumber`, `desiredNumberOfNegativeRoots`, `desiredNumberOfPositiveRoots`, `eigenvalueExtractionMethod`, `estimateNumberOfRoots`, `id`, `lowerFrequencyBound`, `nodeId`, `normalizingEigenvectorsMethod`, `upperFrequencyBound`

Methods:

- `getComponentNumber() -> int` — Gets C: Component number. Required only if NORM = "POINT" and G is a geometric grid point. (1≤Integer≤6)
- `getDesiredNumberOfNegativeRoots() -> int` — Gets NDN: Desired number of roots, Integer > 0, default =3NEP.
- `getDesiredNumberOfPositiveRoots() -> int` — Gets NDP: Desired number of roots, Integer > 0, default =3NEP.
- `getEigenvalueExtractionMethod() -> str` — Gets String to define Method of eigenvalue extraction. (Character: "INV" for inverse power method or "SINV" for enhanced inverse power method.)
- `getEstimateNumberOfRoots() -> int` — Gets NEP: Estimate of number of roots, Integer > 0.
- `getId() -> int` — Gets SID: Set identification number.
- `getLowerFrequencyBound() -> float` — Gets L1: Lower Frequency Bound, Real ≥ 0.0.
- `getNodeId() -> int` — Gets G: Required only if NORM = "POINT".(Integer > 0)
- `getNormalizingEigenvectorsMethod() -> str` — Gets String to define Method for normalizing eigenvectors. (Character: "MAX" or "POINT"; Default ="MAX")
- `getUpperFrequencyBound() -> float` — Gets L2: Upper Frequency Bound, Real ≥ 0.0.
#### `update(name: str, description: str, id: int, eigenvalueExtractionMethod: str, lowerFrequencyBound: float, upperFrequencyBound: float, estimateNumberOfRoots: int, desiredNumberOfPositiveRoots: int, desiredNumberOfNegativeRoots: int, normalizingEigenvectorsMethod: str, nodeId: int, componentNumber: int) -> None`
update the EIGB

- `name` — name of the EIGB
- `description` — description of EIGB
- `id` — id of EIGB
- `eigenvalueExtractionMethod` — String to define Method of eigenvalue extraction. (Character: "INV" for inverse power method or "SINV" for enhanced inverse power method.)
- `lowerFrequencyBound` — L1: Lower Frequency Bound, Real ≥ 0.0.
- `upperFrequencyBound` — L2: Upper Frequency Bound, Real ≥ 0.0.
- `estimateNumberOfRoots` — NEP: Estimate of number of roots, Integer > 0
- `desiredNumberOfPositiveRoots` — NDP: Desired number of roots, Integer > 0
- `desiredNumberOfNegativeRoots` — NDN: Desired number of roots, Integer > 0
- `normalizingEigenvectorsMethod` — String to define Method for normalizing eigenvectors. (Character: "MAX" or "POINT"; Default ="MAX")
- `nodeId` — G: Required only if NORM = "POINT".(Integer > 0)
- `componentNumber` — C: Component number. Required only if NORM = "POINT" and G is a geometric grid point. (1≤Integer≤6)


## `apex.catalog.EIGR`  (extends `Entity`, `IName`)
EIGR: Real Eigenvalue Extraction Data.
Properties: `componentNumber`, `desiredNumberOfRoots`, `eigenvalueExtractionMethod`, `estimateNumberOfRoots`, `id`, `lowerFrequencyBound`, `nodeId`, `normalizingEigenvectorsMethod`, `upperFrequencyBound`

Methods:

- `getComponentNumber() -> int` — Gets C: Component number. Required only if NORM = "POINT" and G is a geometric grid point. (1≤Integer≤6)
- `getDesiredNumberOfRoots() -> int` — Gets ND: Desired number of roots, Integer > 0, default =3.
- `getEigenvalueExtractionMethod() -> str` — Gets String to define extraction method. Modern Methods: LAN: Lanczos Method AHOU: Automatic selection of HOU or MHOU method. Obsolete Methods: INV: Inverse Power method. SINV: Inverse Power method with enhancements. GIV: Givens method of tridiagonalization. MGIV: Modified Givens method. HOU: Householder method of tridiagonalization. MHOU: Modified Householder method. AGIV: Automatic selection of METHOD = "GIV" or "MGIV".
- `getEstimateNumberOfRoots() -> int` — Gets NE: Estimate of number of roots, Integer > 0.
- `getId() -> int` — Gets SID: Set identification number.
- `getLowerFrequencyBound() -> float` — Gets F1: Lower Frequency Bound, Real ≥ 0.0.
- `getNodeId() -> int` — Gets G: Required only if NORM = "POINT".(Integer > 0)
- `getNormalizingEigenvectorsMethod() -> str` — Gets String to define Method for normalizing eigenvectors. MASS: Normalize to unit value of the generalized mass(Default) MAX: Normalize to unit value of the largest component in the analysis set. POINT: Normalize to a positive or negative unit value of the component defined in fields 3 and 4.
- `getUpperFrequencyBound() -> float` — Gets F2: Upper Frequency Bound, Real ≥ 0.0.
#### `update(name: str, description: str, id: int, eigenvalueExtractionMethod: str, lowerFrequencyBound: float, upperFrequencyBound: float, estimateNumberOfRoots: int, desiredNumberOfRoots: int, normalizingEigenvectorsMethod: str, nodeId: int, componentNumber: int) -> None`
update the EIGR

- `name` — name of the EIGR
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


## `apex.catalog.EIGRL`  (extends `Entity`, `IName`)
EIGRL: Real Eigenvalue Extraction Data by Lanczos Method.
Properties: `calculationConstant`, `desiredNumberOfRoots`, `diagnosticLevel`, `estimatefFexibleModeFrequency`, `frequencySegmentValue`, `id`, `lowerFrequencyBound`, `normalizingEigenvectorsMethod`, `numberOfVectors`, `requencySegmentNumber`, `upperFrequencyBound`

Methods:

- `getCalculationConstant() -> float` — Gets ALPH: Specifies a constant for the calculation of frequencies (Fi) at the upper boundary segments for the parallel method. (Real > 0.0; Default = 1.0)
- `getDesiredNumberOfRoots() -> int` — Gets ND: Desired number of roots.
- `getDiagnosticLevel() -> int` — Gets MSGLVL: Diagnostic level. (0 < Integer < 4; Default = 0)
- `getEstimatefFexibleModeFrequency() -> float` — Gets SHFSCL: Estimate of the first flexible mode natural frequency.
- `getFrequencySegmentValue() -> [float]` — Gets Fi: Frequency at the upper boundary of the i-th segment. This is a list of float value up to 15.
- `getId() -> int` — Gets SID: Set identification number.
- `getLowerFrequencyBound() -> float` — Gets V1: Lower Frequency Bound, Real ≥ 0.0.
- `getNormalizingEigenvectorsMethod() -> str` — Gets String to define Method for normalizing eigenvectors. MASS: Normalize to unit value of the generalized mass. Not available for buckling analysis. (Default for normal modes analysis.) MAX: Normalize to unit value of the largest displacement in the analysis set. Displacements not in the analysis set may be larger than unity. (Default for buckling analysis.)
- `getNumberOfVectors() -> int` — Gets MAXSET: Number of vectors in block or set.
- `getRequencySegmentNumber() -> int` — Gets NUMS: Number of frequency segments for the parallel method. (Integer > 0; Default = 1)
- `getUpperFrequencyBound() -> float` — Gets V2: Upper Frequency Bound, Real ≥ 0.0.
#### `update(name: str, description: str, id: int, lowerFrequencyBound: float, upperFrequencyBound: float, desiredNumberOfRoots: int, diagnosticLevel: int, numberOfVectors: int, estimatefFexibleModeFrequency: float, normalizingEigenvectorsMethod: str, calculationConstant: float, requencySegmentNumber: int, frequencySegmentValue: [float]) -> None`
update the EIGRL

- `name` — name of the EIGRL
- `description` — description of EIGRL
- `id` — id of EIGRL
- `lowerFrequencyBound` — V1: Lower Frequency Bound, Real ≥ 0.0.
- `upperFrequencyBound` — V2: Upper Frequency Bound, Real ≥ 0.0.
- `desiredNumberOfRoots` — ND: Desired number of roots, Integer > 0
- `diagnosticLevel` — MSGLVL: Diagnostic level. (0 < Integer < 4)
- `numberOfVectors` — MAXSET: Number of vectors in block or set.
- `estimatefFexibleModeFrequency` — SHFSCL: Estimate of the first flexible mode natural frequency
- `normalizingEigenvectorsMethod` — String to define Method for normalizing eigenvectors. MASS: Normalize to unit value of the generalized mass. Not available for buckling analysis. (Default for normal modes analysis.) MAX: Normalize to unit value of the largest displacement in the analysis set. Displacements not in the analysis set may be larger than unity. (Default for buckling analysis.)
- `calculationConstant` — ALPH: Specifies a constant for the calculation of frequencies (Fi) at the upper boundary segments for the parallel method. (Real > 0.0; Default = 1.0)
- `requencySegmentNumber` — NUMS: Number of frequency segments for the parallel method. (Integer > 0; Default = 1)
- `frequencySegmentValue` — Fi: Frequency at the upper boundary of the i-th segment. This is a list of float value up to 15.


## `apex.catalog.HYBDAMP`  (extends `Entity`, `IName`)
Class representing the hybrid modal damping.
Properties: `id`, `modalDamping`, `modeMethod`, `printEigenSummary`, `useStructuralDamping`

Methods:

- `getId() -> int` — Gets the id of the HYBDAMP.
- `getModalDamping() -> int` — Gets SDAMP: the id of a modal damping table.
- `getModeMethod() -> int` — Gets METHOD: the id of the mode calculation method, should be the id of EIGR or EIGRL.
- `getPrintEigenSummary() -> str` — Gets PRTEIG: a string argument to define whether print eigen value summary from hybrid damping calculation. If it is "YES", the summary is printed. If it is "NO", the summary is not printed, default is "NO".
- `getUseStructuralDamping() -> str` — Gets KDAMP: a string argument to define whether use the vicious damping as the structural damping. If it is "YES", the viscous modal damping is entered into the complex stiffness matrix as structural damping. If it is "NO", the viscous modal damping is not entered into the complex stiffness as structural damping, default is "NO".
#### `update(name: str, description: str, id: int, modeMethod: int, modalDamping: int, useStructuralDamping: str, printEigenSummary: str) -> None`

- `id` — Update the id.
- `modeMethod` — METHOD: the id of the mode calculation method, should be the id of EIGR or EIGRL.
- `modalDamping` — SDAMP: the id of a modal damping table.
- `useStructuralDamping` — Updates the useStructuralDamping.
- `printEigenSummary` — Updates the printEigenSummary.


## `apex.catalog.ITER`  (extends `Entity`, `IName`)
ITER: Iterative Solver Options.
Properties: `convergenceCriterion`, `extractionLevel`, `id`, `maxNumberIterations`, `paddingValue`, `preconditionerOption`, `printMessageForEachIteration`, `terminationCriterion`, `userConvergenceParameter`

Methods:

- `getConvergenceCriterion() -> str` — Gets Convergence criterion. (String:"AR","GE","AREX","GEEX"; Default = "AREX")
- `getExtractionLevel() -> int` — Gets Extraction level in reduced incomplete Cholesky preconditioning, Integer = 0 thought 7.
- `getId() -> int` — Gets SID: Set identification number.
- `getMaxNumberIterations() -> int` — Gets Maximum number of iterations,Integer>0.
- `getPaddingValue() -> int` — Gets Padding value for RIC, RICS, BIC, and BICCMPLX preconditioning. (Integer > 0)
- `getPreconditionerOption() -> str` — Gets String to define Preconditioner option J: Jacobi JS: Jacobi with diagonal scaling. C: Incomplete Cholesky. CS: Incomplete Cholesky with diagonal scaling. RIC: Reduced incomplete Cholesky. RICS: Reduced incomplete Cholesky with diagonal scaling. BIC: Block incomplete Cholesky for real problems. BICCMPLX: Block incomplete Cholesky for complex problems. CASI: Element-based third party iterative solver. USER: User given preconditioning.
- `getPrintMessageForEachIteration() -> str` — Gets String to define Message flag. YES: Messages will be printed for each iteration. NO: Only minimal messages will be printed from the iterative solver(Default).
- `getTerminationCriterion() -> int` — Gets String argument to control early termination of the iterative solver. 0: Runs to completion (Default). -1: Terminates after preface giving resource estimates.
- `getUserConvergenceParameter() -> float` — Gets User-given convergence parameter epsilon.
#### `update(name: str, description: str, id: int, preconditionerOption: str, convergenceCriterion: str, printMessageForEachIteration: str, userConvergenceParameter: float, maxNumberIterations: int, paddingValue: int, extractionLevel: int, terminationCriterion: int) -> None`
update the ITER

- `name` — name of the ITER
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


## `apex.catalog.KeyResultCatalog`
Container class for all KeyResults in the project. Only one instance of KeyResultCatalog is supported within a Project.
Properties: `keyResults`

Methods:

#### `append(keyResult: apex.studies.KeyResult) -> None`
add keyresult in Catalog.

- `keyResult` — the keyresult object.

- `getKeyResults() -> [apex.studies.KeyResult]` — a List of all KeyResults in the KeyResultCatalog.

## `apex.catalog.NLSTEP`  (extends `Entity`, `IName`)
A class that defines the control parameters for mechanical, thermal and coupled analysis in SOL 400 and for contact analysis in SOL 101.
Properties: `activateArtificialDamping`, `activateCreep`, `adapt`, `arcln`, `constraintType`, `convergeCriteriaContact`, `convergeCriteriaHeat`, `convergeCriteriaMech`, `conversionFactorHeatFric`, `conversionFactorHeatPlastic`, `coup`, `dampingRatio`, `desiredIterationsArcLength`, `desiredIterationsPerInc`, `displacementTolerance`, `dominantPeriodSteps`, `effectiveStressFracton`, `errorToleranceDispContact`, `errorToleranceDispMech`, `errorToleranceHeatFlux`, `errorToleranceLoadContact`, `errorToleranceLoadMech`, `errorToleranceTemperature`, `errorToleranceWorkContact`, `errorToleranceWorkHeat`, `errorToleranceWorkMech`, `factorStepSizeChange`, `fixed`, `fixedTimeStepIncrements`, `general`, `heat`, `id`, `includeRotationsMoments`, `initLoadStepFraction`, `initTimeStepFraction`, `iterationLimitBeforeDiverge`, `itersBeforeStiffUpdateHeat`, `itersBeforeStiffUpdateMech`, `largesetRatio`, `lcnt`, `lineToleranceHeat`, `lineToleranceMech`, `maxAdjustRatioArcLength`, `maxBisections`, `maxBisectionsPerInc`, `maxCorrectionVectorsHeat`, `maxCorrectionVectorsMech`, `maxIncrementsLoadCase`, `maxIterations`, `maxIterationsLoadCase`, `maxIterationsPerInc`, `maxLineSearchesHeat`, `maxLineSearchesMech`, `maxTimeStepFraction`, `mech`, `minAdjustRatioArcLength`, `minIterations`, `minIterationsPerInc`, `minTimeStepFraction`, `numIncrements`, `outputFrequency`, `outputFrequencyControl`, `outputInterval`, `predefinedControlOptions`, `setupType`, `skipFactorTimeStep`, `smallestRatio`, `stiffUpdateMethodHeat`, `stiffUpdateMethodMech`, `timeStepBounds`, `totalTimeLoadCase`, `treatUserCriteria`, `usePhysicalCriteria`, `userCriteria`

Methods:

- `getActivateArtificialDamping() -> int` — Gets IDAMP: the integer argument to activate artificial damping for static analysis. 0: No damping considered. 4: Artificial damping is always turned on. 5: Artificial damping is not turned on. But time step is adjusted based on damping energy as 4. 6: When the time step reaches the minimum value and artificial damping is turned on.
- `getActivateCreep() -> int` — Gets CREEP: an integer flag to activate the creep. "1" will activate the creep while "0" will not activate the creep.
- `getAdapt() -> bool` — Gets a boolean argument to indicate that the adaptive load stepping procedure will be used.
- `getArcln() -> bool` — Gets a boolean argument to indicate that an arc length load stepping procedure will be used. It does not support general contact in SOL 400.
- `getConstraintType() -> str` — Gets TYPE: The string argument to define the constraint type in the arc length load stepping procedure. The following constraint types are supported: "CRIS" - Crisfield. "RIKS" - Riks. "MRIKS" - Modified Riks.
- `getConvergeCriteriaContact() -> str` — Gets CONVC: Flag to select convergence criteria. String ="U", "P", "W", "V" or any combination. U = displacement error P = load equilibrium error, W = work error, V = vector component method, This convergence criteria is only used in the contact analysis in SOL101.
- `getConvergeCriteriaHeat() -> str` — Gets CONVC: Flag to select convergence criteria. String ="U", "P", "W", "V", "N", "A" or any combination. U = displacement error P = load equilibrium error W = work error V = vector component method N = length method A = auto switch The criteria is only used for heat analysis in SOL400.
- `getConvergeCriteriaMech() -> str` — Gets CONVC: Flag to select convergence criteria. String ="U", "P", "W", "V", "N", "A" or any combination. U = displacement error P = load equilibrium error W = work error V = vector component method N = length method A = auto switch The criteria is only used for mechanical analysis in SOL400.
- `getConversionFactorHeatFric() -> float` — Gets HGENPLAS: Conversion factor for heat generated due to friction.
- `getConversionFactorHeatPlastic() -> float` — Gets HGENPLAS: Conversion factor for heat generated due to plasticity.
- `getCoup() -> bool` — Gets a boolean argument to indicate that the parameters for the coupled analysis will be used.
- `getDampingRatio() -> float` — Gets DAMP: damping ratio.
- `getDesiredIterationsArcLength() -> int` — Gets NDESIRA: Desired number of iterations for convergence to be used for the adaptive arc-length adjustment(Integer > 0).
- `getDesiredIterationsPerInc() -> int` — Gets NDESIR: Desired number of iterations per increment.
- `getDisplacementTolerance() -> float` — Gets UTOL: Defines tolerance on displacement, .0001 < Real < 1.0.
- `getDominantPeriodSteps() -> int` — Gets MSTEP: Number of steps to obtain the dominant period response(10 < Integer< 200 or = -1).
- `getEffectiveStressFracton() -> float` — Gets FSTRESS: Fraction of effective stress used to limit the sub increment size in material routines(0.0 < float < 1.0). For non material enhanced elements only.
- `getErrorToleranceDispContact() -> float` — Gets EPSUC: Error tolerance for displacement (U) criterion (Float > 0.0). Only used for contact analysis in SOL101.
- `getErrorToleranceDispMech() -> float` — Gets EPSUC: Error tolerance for displacement (U) criterion (Float > 0.0). Only used for mechanical analysis in SOL400.
- `getErrorToleranceHeatFlux() -> float` — Gets EPSPH: Error tolerance for heat flux (P) criterion. Only used in heat analysis in SOL400.
- `getErrorToleranceLoadContact() -> float` — Gets EPSPC: Error tolerance for load (V) criterion(Float > 0.0). Only used for contact analysis in SOL101.
- `getErrorToleranceLoadMech() -> float` — Gets EPSPC: Error tolerance for load (V) criterion(Float > 0.0). Only used for mechanical analysis in SOL400.
- `getErrorToleranceTemperature() -> float` — Gets EPSUH: Error tolerance for temperature (U) criterion. Only used in heat analysis in SOL400.
- `getErrorToleranceWorkContact() -> float` — Gets EPSWC: Error tolerance for work (W) criterion (Float > 0.0). Only used for contact analysis in SOL101.
- `getErrorToleranceWorkHeat() -> float` — Gets EPSWH: Error tolerance for work (W) criterion. Only used in heat analysis in SOL400.
- `getErrorToleranceWorkMech() -> float` — Gets EPSWC: Error tolerance for work (W) criterion (Float > 0.0). Only used for mechanical analysis in SOL400.
- `getFactorStepSizeChange() -> float` — Gets SFACT: factor for increasing time steps due to number of iterations.
- `getFixed() -> bool` — Gets a boolean argument to indicate that fixed time stepping will be used.
- `getFixedTimeStepIncrements() -> int` — Gets NINC: number of increments for fixed time stepping(integer > 0).
- `getGeneral() -> bool` — Gets a boolean argument to activate the parameters used for a variety of simulations.
- `getHeat() -> bool` — Gets a boolean argument to indicate that the parameters for heat transfer analysis will be used.
- `getId() -> int` — Gets the id of the NLSTEP.
- `getIncludeRotationsMoments() -> int` — Gets MRCONV: The integer argument to specify if rotations and moments should be included in the convergence testing when convergence criteria is set to UV, UN, PV, PN, UPV or UPN. 0: check on forces, moments, displacements and rotations. 1: check on forces, moments and displacements. 2: check on forces, displacements and rotations. 3:check on forces and displacements If there is no V and N in the CONV, MRCONV is ignored and all translational and rotational quantities are used to compute the convergence criteria.
- `getInitLoadStepFraction() -> float` — Gets DTINITF: Initial time step defined as fraction of total load step time (TOTTIM). If DTINITF>=DTMAXF(maxTimeStepFraction) then, DTINITF is reset to DTMAXF. If CTRLDEF is set to QLNEAR, the user should set DTINITF equal to TOTTIM.
- `getInitTimeStepFraction() -> float` — Gets DTINITFA: Initial time step defined as a fraction of the load step time(TOTTIME) for the arc-length procedure.
- `getIterationLimitBeforeDiverge() -> int` — Gets MAXDIVC: Limit on probable divergence conditions per iteration before the solution is assumed to diverge(Integer != 0). Only used for contact analysis in SOL101.
- `getItersBeforeStiffUpdateHeat() -> int` — Gets KSTEPH: Number of iterations before the stiffness update for the user defined(ITER) method. Only used in heat analysis in SOL400.
- `getItersBeforeStiffUpdateMech() -> int` — Gets KSTEP: Number of iterations before the stiffness update for the user defined(ITER) method. Only used in mechanical analysis in SOL400.
- `getLargesetRatio() -> float` — Gets RBIG: Largest ratio between time step changes due to user criteria.
- `getLcnt() -> bool` — Gets a boolean argument to indicate that the parameters in the contact analysis in SOL101 will be used.
- `getLineToleranceHeat() -> float` — Gets LSTOLH: Line search tolerance(0.01 < float < 0.9). Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400.
- `getLineToleranceMech() -> float` — Gets LSTOL: Line Search tolerance(0.01 < Float < 0.9). Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400.
- `getMaxAdjustRatioArcLength() -> float` — Gets MAXALR: Maximum allowable arc-length adjustment ratio between increments for the adaptive arc-length method(float > 1.0).
- `getMaxBisections() -> int` — Gets MAXBIS: the maximum number of bisections allowed in the current step.
- `getMaxBisectionsPerInc() -> int` — Gets MAXBISC: Maximum number of bisections allowed for each load increment(-10 < Integer <10).
- `getMaxCorrectionVectorsHeat() -> int` — Gets MAXQNH: Maximum number of quasi-Newton correction vectors to be saved on database. Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400.
- `getMaxCorrectionVectorsMech() -> int` — Gets MAXQN: Maximum number of quasi-Newton correction vectors to be saved on the database. Not used for pure full Newton-Raphson method. Only used in mechanical analysis in SOL400.
- `getMaxIncrementsLoadCase() -> int` — Gets NSMAX: Maximum number of increments in the current load case. The job will stop if this limit is reached.
- `getMaxIterations() -> int` — Gets MAXITER: the maximum iteration number allowed for each increment.
- `getMaxIterationsLoadCase() -> int` — Gets NSMAXA: Maximum number of increments in the current load case(Integer). The job will stop if this limit is reached.
- `getMaxIterationsPerInc() -> int` — Gets MAXITERC: Limit on number of iterations for each load increment(Integer >= 0).
- `getMaxLineSearchesHeat() -> int` — Gets MAXLSH: Maximum number of line searches allowed for each iteration. Not used for pure full Newton-Raphson method. Only used in heat analysis in SOL400.
- `getMaxLineSearchesMech() -> int` — Gets MAXLS: Maximum number of line searches allowed for each iteration. Not used for pure full Newton-Raphson method. Only used in mechanical analysis in SOL400.
- `getMaxTimeStepFraction() -> float` — Gets DTMAXF Maximum time step defined as fraction of total load step time (TOTTIM). For most nonlinear problems, this should be between 0.05 and 0.2 for dynamic simulations.
- `getMech() -> bool` — Gets a boolean argument to indicate that the parameters for the mechanical analysis will be used.
- `getMinAdjustRatioArcLength() -> float` — Gets MINALR: Minimum allowable arc-length adjustment ratio between increments for the adaptive arc-length method(0.0 < Float < 1.0).
- `getMinIterations() -> int` — Gets MINITER: the minimum iteration number needed for each increment (integer > 0).
- `getMinIterationsPerInc() -> int` — Gets MINITERC: Minimum number of iterations of a load increment (Integer > 0).
- `getMinTimeStepFraction() -> float` — Gets DTMINF: Minimum time step defined as fraction of total load step time (TOTTIM).
- `getNumIncrements() -> int` — Gets NINCC: Number of increments.
- `getOutputFrequency() -> int` — Gets INTOUT: an integer to control the output (integer >= -1). -1: Only the last increment of the step will be output. 0: Every computed load increment will be output. > 0: The output will be obtained at INTOUT equally spaced intervals. The time step will be temporarily adjusted if necessary in order to reach these points in time.
- `getOutputFrequencyControl() -> str` — Gets INTOUT: The control of the output frequency. -1: Only the last increment of the step will be output. 0: Every computed load increment will be output. > 0: The output will be obtained at INTOUT equally spaced intervals. The time step will be temporarily adjusted if necessary in order to reach these points in time.
- `getOutputInterval() -> int` — Gets NO: Interval for output. Every N-th increment will be saved for output (integer > 0).
- `getPredefinedControlOptions() -> str` — Gets CTRLDEF: a string argument to define the predefined control options. Following control options are supported. "QLINEAR" sets a linear convergence options. "MILDLY" sets a mild nonlinear convergence options. "SEVERELY" sets a severe nonlinear convergence options. "LCPERF" and "LCACCU" are only used in SOL101. "LCPERF" specifies the performance preference during analysis, while "LCACCU" prefers accuracy for analysis. These keywords must be defined if the smart contact in SOL 101 default is required.
- `getSetupType() -> str` — Gets a string argument to define the setup type of the control parameters: "SMART" or "MANUAL". "SMART" indicates a smart setup type, user only needs to specify the predefined control options(CTRLDEF) while leaving other options blank(except for transient analysis). "MANUAL" indicates a manual setup type, the predefined control option is ignored and user needs to manually specifies all the necessary options.
- `getSkipFactorTimeStep() -> int` — Gets ADJUST: time step skip factor for automatic time step adjustment. Only for dynamics.
- `getSmallestRatio() -> float` — Gets RSMALL: smallest ratio between time step changes due to user criteria.
- `getStiffUpdateMethodHeat() -> str` — Gets KMETHODH: A string argument to define the method for controlling the stiffness updates. Only used in heat analysis in SOL400. "PFNT" - Pure full Newton Raphson. ITER - User defined iteration. AUTO - System automatically selects the most efficient strategy based on convergence rates.
- `getStiffUpdateMethodMech() -> str` — Gets KMETHOD: A string argument to define the method for controlling the stiffness updates. Only used in mechanical analysis in SOL400. "PFNT" - Pure full Newton Raphson. ITER - User defined iteration.
- `getTimeStepBounds() -> float` — Gets RB: define bounds for maintaining the same time step for the stepping function during the adaptive process(0.1 < float <1.0).
- `getTotalTimeLoadCase() -> float` — Gets TOTTIM: The total time for the load case.
- `getTreatUserCriteria() -> int` — Gets LIMTAR: treat user criteria as limits or as targets. Only used if a user criterion is given through CRITTID. 0 to treat user criteria as limits, 1 to treat user criteria as targets.
- `getUsePhysicalCriteria() -> int` — Gets IPHYS: An integer flag to determine if automatic physical criteria should be added and how analysis should proceed if a user criterion is not satisfied. 2: Do not add automatic physical criteria; stop when any user criterion is not satisfied. -2: Do not add automatic physical criteria; continue when user criteria are not satisfied. 1: Add automatic physical criteria; stop when any user criterion is not satisfied. -1: Add automatic physical criteria; continue when any user criterion is not satisfied.
- `getUserCriteria() -> int` — Gets CRITTID: The user criteria for loading stepping control.
#### `update(name: str, description: str, id: int, totalTimeLoadCase: float, setupType: str, predefinedControlOptions: str, general: bool, maxIterations: int, minIterations: int, maxBisections: int, activateCreep: int, fixed: bool, fixedTimeStepIncrements: int, outputInterval: int, adapt: bool, initLoadStepFraction: float, minTimeStepFraction: float, maxTimeStepFraction: float, desiredIterationsPerInc: int, factorStepSizeChange: float, outputFrequencyControl: str, outputFrequency: int, maxIncrementsLoadCase: int, activateArtificialDamping: int, dampingRatio: float, userCriteria: int, usePhysicalCriteria: int, treatUserCriteria: int, smallestRatio: float, largesetRatio: float, skipFactorTimeStep: int, dominantPeriodSteps: int, timeStepBounds: float, displacementTolerance: float, arcln: bool, constraintType: str, initTimeStepFraction: float, minAdjustRatioArcLength: float, maxAdjustRatioArcLength: float, desiredIterationsArcLength: int, maxIterationsLoadCase: int, lcnt: bool, numIncrements: int, convergeCriteriaContact: str, errorToleranceDispContact: float, errorToleranceLoadContact: float, errorToleranceWorkContact: float, iterationLimitBeforeDiverge: int, maxBisectionsPerInc: int, maxIterationsPerInc: int, minIterationsPerInc: int, heat: bool, convergeCriteriaHeat: str, errorToleranceTemperature: float, errorToleranceHeatFlux: float, errorToleranceWorkHeat: float, stiffUpdateMethodHeat: str, itersBeforeStiffUpdateHeat: int, maxCorrectionVectorsHeat: int, maxLineSearchesHeat: int, lineToleranceHeat: float, mech: bool, convergeCriteriaMech: str, errorToleranceDispMech: float, errorToleranceLoadMech: float, errorToleranceWorkMech: float, stiffUpdateMethodMech: str, itersBeforeStiffUpdateMech: int, includeRotationsMoments: int, maxCorrectionVectorsMech: int, maxLineSearchesMech: int, lineToleranceMech: float, effectiveStressFracton: float, coup: bool, conversionFactorHeatPlastic: float, conversionFactorHeatFric: float) -> None`

- `id` — Updates the id.
- `totalTimeLoadCase` — Updates the totalTimeLoadCase.
- `setupType` — Updates the setup type.
- `predefinedControlOptions` — Updates the predefinedControlOptions.
- `general` — Updates the general.
- `maxIterations` — Updates the maxIterations.
- `minIterations` — Updates the minIterations.
- `maxBisections` — Updates the maxBisections.
- `activateCreep` — Updates the activateCreep.
- `fixed` — Updates the fixed.
- `fixedTimeStepIncrements` — Updates the fixedTimeStepIncrements.
- `outputInterval` — Updates the outputInterval.
- `adapt` — Updates the adapt.
- `initLoadStepFraction` — Updates the initLoadStepFraction.
- `minTimeStepFraction` — Updates the minTimeStepFraction.
- `maxTimeStepFraction` — Updates the maxTimeStepFraction.
- `desiredIterationsPerInc` — Updates the desiredIterationsPerInc.
- `factorStepSizeChange` — Updates the factorStepSizeChange.
- `outputFrequencyControl` — Updates the outputFrequencyControl.
- `outputFrequency` — Updates the outputFrequency.
- `maxIncrementsLoadCase` — Updates the maxIncrementsLoadCase.
- `activateArtificialDamping` — Updates the activateArtificialDamping.
- `dampingRatio` — Updates the dampingRatio.
- `userCriteria` — Updates the userCriteria.
- `usePhysicalCriteria` — Updates the usePhysicalCriteria.
- `treatUserCriteria` — Updates the treatUserCriteria.
- `smallestRatio` — Updates the smallestRatio.
- `largesetRatio` — Updates the largestRatio.
- `skipFactorTimeStep` — Updates the skipFactorTimeStep.
- `dominantPeriodSteps` — Updates the dominantPeriodSteps.
- `timeStepBounds` — Updates the timeStepBounds.
- `displacementTolerance` — Updates the displacementTolerance.
- `constraintType` — Updates the constraintType.
- `initTimeStepFraction` — Updates the initTimeStepFraction.
- `minAdjustRatioArcLength` — Updates the minAdjustRatioArcLength.
- `maxAdjustRatioArcLength` — Updates the maxAdjustRatioArcLength.
- `desiredIterationsArcLength` — Updates the desiredIterationsArcLength.
- `maxIterationsLoadCase` — Updates the maxIterationsLoadCase.
- `lcnt` — Updates the lcnt.
- `numIncrements` — Updates the numIncrements.
- `convergeCriteriaContact` — Updates the convergeCriteriaContact.
- `errorToleranceDispContact` — Updates the errorToleranceDispContact.
- `errorToleranceLoadContact` — Updates the errorToleranceLoadContact.
- `errorToleranceWorkContact` — Updates the errorToleranceWorkContact.
- `iterationLimitBeforeDiverge` — Updates the iterationLimitBeforeDiverge.
- `maxBisectionsPerInc` — Updates the maxBisectionsPerInc.
- `maxIterationsPerInc` — Updates the maxIterationsPerInc.
- `minIterationsPerInc` — Updates the minIterationsPerInc.
- `heat` — Updates the heat.
- `convergeCriteriaHeat` — Updates the convergeCriteriaHeat.
- `errorToleranceTemperature` — Updates the errorToleranceTemperature.
- `errorToleranceHeatFlux` — Updates the errorToleranceHeatFlux.
- `errorToleranceWorkHeat` — Updates the errorToleranceWorkFlux.
- `stiffUpdateMethodHeat` — Updates the stiffUpdateMethodHeat.
- `itersBeforeStiffUpdateHeat` — Updates the itersBeforeStiffUpdateHeat.
- `maxCorrectionVectorsHeat` — Updates the maxCorrectionVectorsHeat.
- `maxLineSearchesHeat` — Updates the maxLineSearchesHeat.
- `lineToleranceHeat` — Updates the lineToleranceHeat.
- `mech` — Updates the mech.
- `convergeCriteriaMech` — Updates the convergeCriteriaMech.
- `errorToleranceDispMech` — Updates the errorToleranceDispMech.
- `errorToleranceLoadMech` — Updates the errorToleranceLoadMech.
- `errorToleranceWorkMech` — Updates the errorToleranceWorkMech.
- `stiffUpdateMethodMech` — Updates the stiffUpdateMethodMech.
- `itersBeforeStiffUpdateMech` — Updates the itersBeforeStiffUpdateMech.
- `includeRotationsMoments` — Updates the includeRotationsMoments.
- `maxCorrectionVectorsMech` — Updates the maxCorrectionVectorsMech.
- `maxLineSearchesMech` — Updates the maxLineSearchesMech.
- `lineToleranceMech` — Updates the lineToleranceMech.
- `effectiveStressFracton` — Updates the effectiveStressFracton.
- `coup` — Updates the coup.
- `conversionFactorHeatPlastic` — Updates the conversionFactorHeatPlastic.
- `conversionFactorHeatFric` — Updates the conversionFactorHeatFric.


## `apex.catalog.ParametersSet`  (extends `Entity`)
Class to represent a set of Nastran Parameters entries.
Properties: `description`, `name`, `parametersType`, `params`

Methods:

- `clone() -> apex.catalog.ParametersSet` — Clone the parameter set.
- `getDescription() -> str` — description of parameters set.
- `getName() -> str` — name of parameters set.
- `getParametersType() -> apex.catalog.ParametersType` — Parameter type to be used in case control or bulk data.
- `getParams() -> {str:value}` — dictionary to specify a set of parameters, the key is name of PARAM, the value is the value of the PARAM, below is the example: {'AUTOMSET':"NO", 'K6ROT':100.00, 'SNORM':20.00}
#### `setParams(params: {str:value}) -> None`
set parameters of parameters set.

- `params` — dictionary to specify a set of parameters, the key is name of PARAM, the value is the value of the PARAM, below is the example: {'AUTOMSET':"NO", 'K6ROT':100.00, 'SNORM':20.00}

#### `update(name: str, description: str) -> apex.catalog.ParametersSet`
Update parameters set name and description.

- `name` — name of parameters set.
- `description` — description of parameters set.

#### `updateParams(params: {str:value}) -> apex.catalog.ParametersSet`
Update params of the set.

- `params` — dictionary to specify a set of parameters, the key is name of PARAM, the value is the value of the PARAM, below is the example: {'AUTOMSET':"NO", 'K6ROT':100.00, 'SNORM':20.00}


## `apex.catalog.ParametersSetCollection`  (extends `EntityCollection`)
A high performance container class for parameter set.

Methods:

- `ParametersSetCollection() -> None` — Construct a new ParametersSetCollection.

## `apex.catalog.RANDPS`  (extends `Entity`, `IName`)
This is class to represent RANDPS set.
Properties: `appliedLoadSubcase`, `excitedLoadSubcase`, `id`, `imaginary`, `real`, `table`

Methods:

- `getAppliedLoadSubcase() -> [int]` — Gets K: Subcase identification number of the applied load set. A list of applied load set subcases ID.
- `getExcitedLoadSubcase() -> [int]` — Gets J: Subcase identification number of the excited load set. A list of excited load set subcases ID.
- `getId() -> int` — Gets Id of RANDPS set.
- `getImaginary() -> [float]` — Gets Y: imaginary component of complex number A list of float value.
- `getReal() -> [float]` — Gets X: real component of complex number A list of float value.
- `getTable() -> [int]` — Gets TID: Identification number of a TABRNDi entry that defines G(F). A list of TABRNDi entry ID.
#### `update(name: str, description: str, id: int, excitedLoadSubcase: [int], appliedLoadSubcase: [int], real: [float], imaginary: [float], table: [int]) -> None`
update the RANDPS set

- `name` — name of the RANDPS set
- `description` — description of RANDPS set
- `id` — id of RANDPS set
- `excitedLoadSubcase` — J: Subcase identification number of the excited load set. A list of excited load set subcases ID.
- `appliedLoadSubcase` — K: Subcase identification number of the applied load set. A list of applied load set subcases ID.
- `real` — X: real component of complex number A list of float value.
- `imaginary` — Y: imaginary component of complex number A list of float value.
- `table` — TID: Identification number of a TABRNDi entry that defines G(F). A list of TABRNDi entry ID.


## `apex.catalog.RANDT1`  (extends `Entity`, `IName`)
This is class to represent RANDT1 set.
Properties: `id`, `maxTimeLag`, `startingTimeLag`, `timeLagNumber`

Methods:

- `getId() -> int` — Gets Id of RANDT1 set.
- `getMaxTimeLag() -> [float]` — Gets TMAX: Maximum time lag. (Real > T0) A list of float value.
- `getStartingTimeLag() -> [float]` — Gets T0： Starting time lag. (Real ≥ 0.0) A list of float value.
- `getTimeLagNumber() -> [int]` — Gets N: Number of time lag intervals. (Integer > 0) A list of int value.
#### `update(name: str, description: str, id: int, timeLagNumber: [int], startingTimeLag: [float], maxTimeLag: [float]) -> None`
update the RANDT1 set

- `name` — name of the RANDT1 set
- `description` — description of RANDT1 set
- `id` — id of RANDT1 set
- `timeLagNumber` — N: Number of time lag intervals. (Integer > 0) A list of int value.
- `startingTimeLag` — T0： Starting time lag. (Real ≥ 0.0) A list of float value.
- `maxTimeLag` — TMAX: Maximum time lag. (Real > T0) A list of float value.


## `apex.catalog.RCROSS`  (extends `Entity`, `IName`)
Class to define a pair of response quantities for computing the cross-power spectral density and cross-correlation functions in random analysis.
Properties: `componentId1`, `componentId2`, `curveId`, `id`, `id1`, `id2`, `responseQuantityType1`, `responseQuantityType2`

Methods:

- `getComponentId1() -> [int]` — Gets COMP1: a list of component code ids of the first response quantity. For elements, the item code COMPi represents a component of the element stress, strain, and force and is described in Tables Element Stress-Strain Item Codes and Element Force Item Codes Part 1 in the Nastran Quick Reference Guide. For an item having both a real and imaginary part, the code of the real part must be selected. This is required for computing both the cross-power spectral density function and cross-correlation function. For grid point, the item code is one of 1, 2, 3, 4, 5, and 6, which represent the mnemonics T1, T2, T3, R1, R2, and R3, respectively. For scalar point, always use 1.
- `getComponentId2() -> [int]` — Gets COMP2: a list of the component code ids of the second response quantity. For elements, the item code COMPi represents a component of the element stress, strain, and force and is described in Tables Element Stress-Strain Item Codes and Element Force Item Codes Part 1 in the Nastran Quick Reference Guide. For an item having both a real and imaginary part, the code of the real part must be selected. This is required for computing both the cross-power spectral density function and cross-correlation function. For grid point, the item code is one of 1, 2, 3, 4, 5, and 6, which represent the mnemonics T1, T2, T3, R1, R2, and R3, respectively. For scalar point, always use 1.
- `getCurveId() -> [int]` — Gets CURID: a list of curve ids, it is used to identify the output.
- `getId() -> int` — Gets the id of the RCROSS.
- `getId1() -> [int]` — Gets ID1: a list of ids, each id points to element, node or scalar point.
- `getId2() -> [int]` — Gets ID2: a list of ids, each id points to element, node or scalar point.
- `getResponseQuantityType1() -> [str]` — Gets RTYPE1: a list of strings to define the first response quantity type. Following strings are supported: "DISP" - displacement vector. "VELO" - velocity vector. "ACCEL" - acceleration vector. "OLOAD" - applied load vector. "SPCF" - single point constraint force vector. "MPCF" - multi point constraint force vector. "STRESS" - element stress. "STRAIN" - element strain. "FORCE" - element force. None - same with the responseQuantityType2, note that it is not "None".
- `getResponseQuantityType2() -> [str]` — Gets RTYPE2: a list of strings to define the second response quantity type. Following strings are supported: "DISP" - displacement vector. "VELO" - velocity vector. "ACCEL" - acceleration vector. "OLOAD" - applied load vector. "SPCF" - single point constraint force vector. "MPCF" - multi point constraint force vector. "STRESS" - element stress. "STRAIN" - element strain. "FORCE" - element force. None - same with the responseQuantityType1, note that it is not "None".
#### `update(name: str, description: str, id: int, responseQuantityType1: [str], id1: [int], componentId1: [int], responseQuantityType2: [str], id2: [int], componentId2: [int], curveId: [int]) -> None`

- `id` — Update the id.
- `responseQuantityType1` — Updates the responseQuantityType1.
- `id1` — Updates the id1.
- `componentId1` — Updates the componentId1.
- `responseQuantityType2` — Updates the responseQuantityType2.
- `id2` — Updates the id2.
- `componentId2` — Updates the componentId2.
- `curveId` — Updates the curveId.


## `apex.catalog.SystemCellsSet`  (extends `Entity`)
Class to represent a set of Nastran System cells entries.
Properties: `description`, `name`, `systemCells`

Methods:

- `clone() -> apex.catalog.SystemCellsSet` — Clone the system cells set.
- `getDescription() -> str` — description of system cells set.
- `getName() -> str` — name of a system cells set.
- `getSystemCells() -> {str:value}` — dictionary to specify the values for system cells in the set, the key is the name of system cell, the value is the expression assigned to the system cell, below is the example: {'BUFFSIZE':10000, 'NLINES':60, 'MAXLINES':2000000}
#### `setSystemCells(systemCells: {str:value}) -> None`
set systemCells of system cells set.

- `systemCells` — dictionary to specify the values for system cells in the set, the key is the name of system cell, the value is the expression assigned to the system cell, below is the example: {'BUFFSIZE':10000, 'NLINES':60, 'MAXLINES':2000000}

#### `update(name: str, description: str) -> apex.catalog.SystemCellsSet`
Update system cells set name and description.

- `name` — name of system cells set.
- `description` — description of system cells set.

#### `updateSystemCells(systemCells: {str:value}) -> apex.catalog.SystemCellsSet`
update system cells set.

- `systemCells` — dictionary to specify the values for system cells in the set, the key is the name of system cell, the value is the expression assigned to the system cell, below is the example: {'BUFFSIZE':10000, 'NLINES':60, 'MAXLINES':2000000}


## `apex.catalog.SystemCellsSetCollection`  (extends `EntityCollection`)
A high performance container class for system cells set.

Methods:

- `SystemCellsSetCollection() -> None` — Construct a new SystemCellsSetCollection.

## `apex.catalog.TSTEP`  (extends `Entity`, `IName`)
TSTEP: Transient Time Step.
Properties: `id`, `outputSkipFactor`, `timeIncrement`, `timeStepNumber`

Methods:

- `getId() -> int` — Gets SID: Set identification number.
- `getOutputSkipFactor() -> [int]` — Gets A list of output skip factor. NOi: Skip factor for output. Every NOi-th step will be saved for output. (Integer > 0; Default= 1)
- `getTimeIncrement() -> [float]` — Gets A list of time increment. DTi: Time increment. (Real > 0.0)
- `getTimeStepNumber() -> [int]` — Gets A list of time step number. Ni: Number of time steps of value DTi. (Integer > 1)
#### `update(name: str, description: str, id: int, timeStepNumber: [int], timeIncrement: [float], outputSkipFactor: [int]) -> None`
update the TSTEP

- `name` — name of the tstep
- `description` — description of tstep
- `id` — id of tstep
- `timeStepNumber` — A list of time increment. DTi: Time increment. (Real > 0.0)
- `outputSkipFactor` — A list of output skip factor. NOi: Skip factor for output. Every NOi-th step will be saved for output. (Integer > 0; Default= 1)


