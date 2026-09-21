# apex.studies — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.studies.ANALYSIS`  (extends `ScenarioCommand`)
Class representing a Nastran "ANALYSIS' case control command The ANALYSIS command is used to specify the type of analysis that will be performed in a Subcase, Step or Substep in Solution 200 or Solution 400 jobs.

## `apex.studies.AUTOSPC`  (extends `ScenarioCommand`)
Class representing a Nastran AUTOSPC case control command. AUTOSPC commands are used to automatically constrain stiffness singularities, and near singularities, using single or multi point constraints Boundary conditions are identified by an integer ID.
Properties: `printSingularities`, `printZeros`, `punchConstraints`, `residual`, `setId`, `spcOrMpc`, `stiffnessConstraintRatio`, `stiffnessIdentificationtRatio`, `value`

Methods:

- `getPrintSingularities() -> str` — Gets Optional property that controls printing of the singularities to a table in the Nastran output. This property may be assigned any one of the following values, "NOPRINT" - No singularity info will be output to the print file None - same as "NOPRINT" with the exception that this field will not be written to the Nastran file. ("NOPRINT" is the Nastran default value for this field "PRINT" - Singularity information will be written to the print file.
- `getPrintZeros() -> str` — Gets Optional property that controls whether or not singularities with zero stiffness ratios will be included in the printed output This property may be assigned any one of the following values, "ZERO" - singularities with zero stiffness ratios will be written to the print file None - same as "ZERO" with the exception that this field will not be written to the Nastran file. ("ZERO" is the Nastran default value for this field "NOZERO" - singularities with zero stiffness ratios will NOT be written to the print file.
- `getPunchConstraints() -> str` — Gets Optional property that controls output of the constraints (SPC, MPC) to the Nastran punch file This property may be assigned any one of the following values, "NOPUNCH" - No singularity info will be output to the punch file None - same as "NOPUNCH" with the exception that this field will not be written to the Nastran file. ("NOPUNCH" is the Nastran default value for this field "PUNCH" - Singularity information will be written to the punch file.
- `getResidual() -> str` — Gets Optional property to define the scope of this automatic constraint to either the superelements only or the superelements AND the residual. This property may be assigned either of the following values, 'RESIDUAL' - both the superelements and the residual will be constrained by this AUTOSPC None - only the superelements will be automatically constrained by this AUTOSPC and this field will not be written to the Nastran file - this is the Nastran default for this field.
- `getSetId() -> int` — Gets Optional property that defines a SET ID to be used when constraints are output to the punch file If omitted, a default SID of 999 will be used.
- `getSpcOrMpc() -> str` — Gets Optional string property that controls whether singularities are applied using single point constraints (SPC) or multi point constraints (MPC) This property may be assigned any one of the following values, "SPC" - causes Nastran to use SPCs to constrain singular degrees of freedom None - same as "SPC" with the exception that this field will not be written to the Nastran file ("SPC" is the Nastran default value for this field) "MPC" - causes Nastran to use MPCs to constrain singular degrees of freedom.
- `getStiffnessConstraintRatio() -> float` — Gets Optional property that defines a stiffness ratio constraint threshold. Degrees of freedom with stiffness values below this threshold will be automatically constrained by this AUTOSPC. Degrees of freedom with stiffness values greater than this threshold will NOT be constrained by this AUTOSPEC. If omitted, a default threshold value will be used which is dependent on the value of the 'residual' property. If 'residual' is True a default value of 1.0E-5 is used, otherwise a default value of 1.0E-8 is used.
- `getStiffnessIdentificationtRatio() -> float` — Gets Optional property that defines a stiffness identification ratio threshold. Degrees of freedom with stiffness values below this threshold will be automatically identified (but not constrained) as potential singularities by this AUTOSPC. Degrees of freedom with stiffness values greater than this threshold will NOT be identified as potential singularities by this AUTOSPEC. If omitted, a default identification threshold value will be used which is dependent on the value of the 'residual' property. If 'residual' is True a default value of 1.0E-5 is used, otherwise a default value of 1.0E-8 is used.
- `getValue() -> str` — Gets a property indicating whether or not automatic singularity constraints will be applied or not This property may be assigned either of the following values - no default value is provided "YES" - Constraints WILL be assigned to singular degrees of freedom automatically "NO" - Constraints WILL NOT be assigned to singular degrees of freedom automatically.
#### `setPrintSingularities(printSingularities: str) -> None`
Sets Optional property that controls printing of the singularities to a table in the Nastran output. This property may be assigned any one of the following values, "NOPRINT" - No singularity info will be output to the print file None - same as "NOPRINT" with the exception that this field will not be written to the Nastran file. ("NOPRINT" is the Nastran default value for this field "PRINT" - Singularity information will be written to the print file.

- `printSingularities` — Set the printSingularities of this AUTOSPC

#### `setPrintZeros(printZeros: str) -> None`
Sets Optional property that controls whether or not singularities with zero stiffness ratios will be included in the printed output This property may be assigned any one of the following values, "ZERO" - singularities with zero stiffness ratios will be written to the print file None - same as "ZERO" with the exception that this field will not be written to the Nastran file. ("ZERO" is the Nastran default value for this field "NOZERO" - singularities with zero stiffness ratios will NOT be written to the print file.

- `printZeros` — Set the printZeros of this AUTOSPC

#### `setPunchConstraints(punchConstraints: str) -> None`
Sets Optional property that controls output of the constraints (SPC, MPC) to the Nastran punch file This property may be assigned any one of the following values, "NOPUNCH" - No singularity info will be output to the punch file None - same as "NOPUNCH" with the exception that this field will not be written to the Nastran file. ("NOPUNCH" is the Nastran default value for this field "PUNCH" - Singularity information will be written to the punch file.

- `punchConstraints` — Set the punchConstraints of this AUTOSPC

#### `setResidual(residual: str) -> None`
Sets Optional property to define the scope of this automatic constraint to either the superelements only or the superelements AND the residual. This property may be assigned either of the following values, 'RESIDUAL' - both the superelements and the residual will be constrained by this AUTOSPC None - only the superelements will be automatically constrained by this AUTOSPC and this field will not be written to the Nastran file - this is the Nastran default for this field.

- `residual` — Set the residual of this AUTOSPC

#### `setSetId(setId: int) -> None`
Sets Optional property that defines a SET ID to be used when constraints are output to the punch file If omitted, a default SID of 999 will be used.

- `setId` — Set the setId of this AUTOSPC

#### `setSpcOrMpc(spcOrMpc: str) -> None`
Sets Optional string property that controls whether singularities are applied using single point constraints (SPC) or multi point constraints (MPC) This property may be assigned any one of the following values, "SPC" - causes Nastran to use SPCs to constrain singular degrees of freedom None - same as "SPC" with the exception that this field will not be written to the Nastran file ("SPC" is the Nastran default value for this field) "MPC" - causes Nastran to use MPCs to constrain singular degrees of freedom.

- `spcOrMpc` — Set the spcOrMpc of this AUTOSPC

#### `setStiffnessConstraintRatio(stiffnessConstraintRatio: float) -> None`
Sets Optional property that defines a stiffness ratio constraint threshold. Degrees of freedom with stiffness values below this threshold will be automatically constrained by this AUTOSPC. Degrees of freedom with stiffness values greater than this threshold will NOT be constrained by this AUTOSPEC. If omitted, a default threshold value will be used which is dependent on the value of the 'residual' property. If 'residual' is True a default value of 1.0E-5 is used, otherwise a default value of 1.0E-8 is used.

- `stiffnessConstraintRatio` — Set the stiffnessConstraintRatio of this AUTOSPC

#### `setStiffnessIdentificationtRatio(stiffnessIdentificationtRatio: float) -> None`
Sets Optional property that defines a stiffness identification ratio threshold. Degrees of freedom with stiffness values below this threshold will be automatically identified (but not constrained) as potential singularities by this AUTOSPC. Degrees of freedom with stiffness values greater than this threshold will NOT be identified as potential singularities by this AUTOSPEC. If omitted, a default identification threshold value will be used which is dependent on the value of the 'residual' property. If 'residual' is True a default value of 1.0E-5 is used, otherwise a default value of 1.0E-8 is used.

- `stiffnessIdentificationtRatio` — Set the stiffnessIdentificationtRatio of this AUTOSPC

#### `setValue(value: str) -> None`
Sets a property indicating whether or not automatic singularity constraints will be applied or not This property may be assigned either of the following values - no default value is provided "YES" - Constraints WILL be assigned to singular degrees of freedom automatically "NO" - Constraints WILL NOT be assigned to singular degrees of freedom automatically.

- `value` — Set the value of this AUTOSPC


## `apex.studies.AXISYMMETRIC`  (extends `ScenarioCommand`)
Class representing a Nastran AXISYMMETRIC case control command. The AXISYMMETRIC command is used to define how boundary conditions for axisymmetric conical shells are interpreted OR to indicate the existence of fluid harmonics for hydroelatsic problems.
Properties: `value`

Methods:

- `getValue() -> str` — Gets required property to select axisymmetric boundary condition behavior value must be set to one of three possible string values, 'SINE' - indicates that sinusoidal boundary conditions will be use 'COSINE' - indicates that cosinusoidal boundary conditions will be used 'FLUID' - indicates the existence of fluid harmonics.
#### `setValue(value: str) -> None`
Sets required property to select axisymmetric boundary condition behavior value must be set to one of three possible string values, 'SINE' - indicates that sinusoidal boundary conditions will be use 'COSINE' - indicates that cosinusoidal boundary conditions will be used 'FLUID' - indicates the existence of fluid harmonics.

- `value` — Set the value of this AXISYMMETRIC


## `apex.studies.AdvancedSettingGenerativeDesign`
class representing user defined settings used by the generative design solver during simulation of the Scenario
Properties: `advancedSetting`, `startSpaceName`

Methods:

- `getAdvancedSetting() -> [str]` — A list of strings that are intended to represent advanced user setting Statements in the Generative design solver file.
- `getStartSpaceName() -> str` — List of fully qualified path names of the start space STL file to be used for the scenario.
#### `update(advancedSetting: [str], startSpaceName: str) -> None`
A method to update advanced setting, start space STL file.

- `advancedSetting` — A list of strings that are intended to represent advanced user setting Statements in the Generative design solver
- `startSpaceName` — List of fully qualified path names of the start space STL file to be used for the scenario.


## `apex.studies.BC`  (extends `ScenarioCommand`)
Class representing a Nastran BC case control command. BC commands are used to identify multiple boundary conditions in normal modes and buckling analyses Boundary conditions are identified by an integer ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID assigned to a Subcase to identify which Subcases are associated wit the same eigenvalue extraction, This command is only required if a normal modes or buckling analysis includes multiple subcases with different boundary conditions. In this case case, all Subcases that share the same BC ID will be associate with a single eigenvalue extraction Use this command to assign a BNC ID to a Subcase.
#### `setValue(value: int) -> None`
Sets the ID assigned to a Subcase to identify which Subcases are associated wit the same eigenvalue extraction, This command is only required if a normal modes or buckling analysis includes multiple subcases with different boundary conditions. In this case case, all Subcases that share the same BC ID will be associate with a single eigenvalue extraction Use this command to assign a BNC ID to a Subcase.

- `value` — Set the value of this BC


## `apex.studies.BCONCHK`  (extends `ScenarioCommand`)
Class representing a Nastran BCONCHK case control command The BCONCHK command is used to entry is used to activate contact model checks before analysis in Solution sequences 101, 103, 105, 107~112, 200 and 400. Properties defined on this class can be used to control the output of initial contact information and control whether or not to proceed with solution after the checks are complete.
Properties: `output`, `value`

Methods:

- `getOutput() -> str` — Gets optional argument (Default = None) used to control output of initial contact information. The following values may be assigned to this property 'PRINT' - causes initial contact data to be written to printed output and to all results file(s) 'PUNCH' - causes initial contact data to be written to the punch file and to all results file(s) 'PRINT, PLOT'- causes initial contact data to be written to the printed output, the punch file and to all results file(s) 'PLOT' - causes initial contact data to be written to the results file(s) only None - causes the same behavior as 'PLOT' but will not cause the 'PLOT' string to be exported as part of the BCONCHK command. 'PLOT' is the default behavior if this property is not set.
- `getValue() -> str` — Gets optional property used to define how Nastran will proceed after completion of the initial contact checks value may be assigned any one of the following values, 'RUN' (Default) - Analysis will proceed normally after initial contact checks are complete 'STOP' - Analysis will terminate immediately after initial contact checks are complete 'STEP' - Analysis will proceed after initial contact checks are complete AND further contact checks will be performed (and output) at each output request load/time step.
#### `setOutput(output: str) -> None`
Sets optional argument (Default = None) used to control output of initial contact information. The following values may be assigned to this property 'PRINT' - causes initial contact data to be written to printed output and to all results file(s) 'PUNCH' - causes initial contact data to be written to the punch file and to all results file(s) 'PRINT, PLOT'- causes initial contact data to be written to the printed output, the punch file and to all results file(s) 'PLOT' - causes initial contact data to be written to the results file(s) only None - causes the same behavior as 'PLOT' but will not cause the 'PLOT' string to be exported as part of the BCONCHK command. 'PLOT' is the default behavior if this property is not set.

- `output` — Set the output of this BCONCHK

#### `setValue(value: str) -> None`
Sets optional property used to define how Nastran will proceed after completion of the initial contact checks value may be assigned any one of the following values, 'RUN' (Default) - Analysis will proceed normally after initial contact checks are complete 'STOP' - Analysis will terminate immediately after initial contact checks are complete 'STEP' - Analysis will proceed after initial contact checks are complete AND further contact checks will be performed (and output) at each output request load/time step.

- `value` — Set the value of this BCONCHK


## `apex.studies.BCONTACT`  (extends `ScenarioCommand`)
Class representing a Nastran BCONTACT case control command BCONTACT is used to activate contact in an analysis and to select which contact pairs will participate during solution of specific load case items (Subcases, Steps, Substeps)
Properties: `auto_contact_type`, `value`

Methods:

- `getAuto_contact_type() -> str` — Gets optional property used to define the type of contact that Nastran will use when automatic contact body creation is selected by setting value='AUTO' on this command. This property may be assigned any of the following values 'TOUCH' - invokes Nastran touching contact to be used when automatic Nastran contact body creation is requested None - has the same effect as 'TOUCH' but omits writing this field to the Nastran file since 'TOUCH' is the default 'PGLUE' - invokes Nastran permanent glue contact to be used when automatic Nastran contact body creation is requested 'GGLUE' - invokes Nastran general glued contact to be used when automatic Nastran contact body creation is requested 'SGLUE' - invokes Nastran stepped glued contact to be used when automatic Nastran contact body creation is requested This property is ignored unless the value property is set to 'AUTO'.
- `getValue() -> str` — Gets required property (Default = 'NONE') used to identify which contact pairs will be activated by this BCONTACT command This property may take any of the forms shown below, 'NONE' - indicates that no contact will be active during the load case item that this BCONTACT command is assigned to 'ALLBODY' - indicates that all contact bodies defined in the model may potentially contact each other. 'AUTO' - indicates that Nastran will automatically create contact bodies and all of these contact bodies may potentially contact each other. When value is set to 'AUTO', the optional 'auto_contact_type' property may also be defined to specify what type of contact Nastran will implement for the automatically created bodies n - integer that will activate all contact entities defined using BCTABL1, BCONECT, BCHANGE, BCMOVE an BCTABLE entries with ID=n Setting this property to any value other than the ones defined above will cause Apex to raise an exception when this command is assigned to a load case item.
#### `setAuto_contact_type(auto_contact_type: str) -> None`
Sets optional property used to define the type of contact that Nastran will use when automatic contact body creation is selected by setting value='AUTO' on this command. This property may be assigned any of the following values 'TOUCH' - invokes Nastran touching contact to be used when automatic Nastran contact body creation is requested None - has the same effect as 'TOUCH' but omits writing this field to the Nastran file since 'TOUCH' is the default 'PGLUE' - invokes Nastran permanent glue contact to be used when automatic Nastran contact body creation is requested 'GGLUE' - invokes Nastran general glued contact to be used when automatic Nastran contact body creation is requested 'SGLUE' - invokes Nastran stepped glued contact to be used when automatic Nastran contact body creation is requested This property is ignored unless the value property is set to 'AUTO'.

- `auto_contact_type` — Set the auto_contact_type of this BCONTACT

#### `setValue(value: str) -> None`
Sets required property (Default = 'NONE') used to identify which contact pairs will be activated by this BCONTACT command This property may take any of the forms shown below, 'NONE' - indicates that no contact will be active during the load case item that this BCONTACT command is assigned to 'ALLBODY' - indicates that all contact bodies defined in the model may potentially contact each other. 'AUTO' - indicates that Nastran will automatically create contact bodies and all of these contact bodies may potentially contact each other. When value is set to 'AUTO', the optional 'auto_contact_type' property may also be defined to specify what type of contact Nastran will implement for the automatically created bodies n - integer that will activate all contact entities defined using BCTABL1, BCONECT, BCHANGE, BCMOVE an BCTABLE entries with ID=n Setting this property to any value other than the ones defined above will cause Apex to raise an exception when this command is assigned to a load case item.

- `value` — Set the value of this BCONTACT


## `apex.studies.BCPARA`  (extends `ScenarioCommand`)
Class representing a Nastran BCPARA bulk data entry The BCPARA entry is used to define contact parameters in Solutions 101 and 400.
Properties: `augdist`, `augment`, `backctl`, `beamb`, `bias`, `ddulmt`, `dynprfa`, `errbas`, `error`, `fgcflg`, `fgcnst`, `fgcnsti`, `fgcnstr`, `fgcrcen`, `fgcrcn1`, `fgctst`, `fgctsti`, `fgctstr`, `fntol`, `ftype`, `glueout`, `ibsep`, `icsep`, `lincnt`, `maxsep`, `method`, `nlglue`, `nodsep`, `osplnfrq`, `penalt`, `rvcnst`, `segangl`, `segsym`, `sepacc`, `sfnpnlt`, `sftpnlt`, `skip_separation_checks`, `sldlmt`, `stkslp`, `taugmnt`, `tcntctl`, `thkoff`, `tpenalt`, `version`

Methods:

- `getAugdist() -> float` — Gets specifies a penetration distance beyond which augmentation will be applied This property must be assigned one of the following values, any real number. This value represents a distance. If contact surfaces penetrate each other by more than this distance, augmentation will be applied None - Nastran will automatically calculate a default augmentation distance and this field will not be written to the Nastran file for this BCPARA.
- `getAugment() -> int` — Gets specifies the augmentation method that will be used when segment to segment contact is active This property may must be assigned any one of the following values, 0 - No augmentation None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Augmentation based on a constant Lagrange multiplier field for linear elements and on a (bi)linear Lagrange multiplier field for quadratic elements 2 - Augmentation based on a constant Lagrange multiplier field 3 - Augmentation based on a (bi)linear Lagrange multiplier field.
- `getBackctl() -> int` — Gets specifies backward compatibility contact analysis options This property may must be assigned any one of the following values, -1 - Activate all of compatibility items defined individually by values greater than 1 (shown below) 0 - No backward compatibility options will be activated None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Body order independent 2 - Evaluation of contact matrix/force on segment coordinates (old logic) 4 - Segment sequence renumbering (old method) 8 - No reset iteration count after separation (old logic) 15 - Creating new polygon under sliding condition (old logic) 32 - Scaled incremental displacement update in small rotation (old method) 64 - Ramping down penalty when angle of segment normals between 180 degree and SEGANGL 128 - Old algorithm of nodal projection in contact From release 2021.3 onwards, the default uses the enhanced contact projection algorithm, which helps in consistent contact detection at corners and for warped surface.
- `getBeamb() -> int` — Gets activates/deactivates beam to beam contact This property may be assigned any one of the following values, 0 - Beam to beam contact is disabled None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Activates beam to beam contact.
- `getBias() -> float` — Gets defines the contact tolerance bias factor This property may be assigned either of the following values, a floating point value between 0.0 and 1.0 None - This field will not be written to the Nastran file for this BCPARA entry and Nastran will determine a default contact bias factor as follows, Default = 0.9 for IGLUE=0. Default = 0.0 for IGLUE <>0 Default = 0.0 for BEHAVE=SYMM on BCBODY.
- `getDdulmt() -> float` — Gets.
- `getDynprfa() -> float` — Gets specifies the dynamic contact projection factor This property may be assigned any one of the following values, any real number >=0.0 and <=1.0 None - same as setting this property value to 0.0 with the exception that this field will not be written to the Nastran file.(0.0 is the default Nastran value for this field) A value of 0.0 may show some penetration. Values greater than 0 reduce penetration and can introduce transient vibration. It is strongly recommended to use the default values in NLTRAN to avoid the chattering in contact analysis.
- `getErrbas() -> int` — Gets defines the basis for contact error calculation, 0 - Use global error claculations None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - calculate error based on each contact pair.
- `getError() -> float` — Gets optional property defining a distance below which a node is considered to be touching a body This property may be assigned either of the following values, any positive floating point value. The value defines a distance below which a nodes is considered to be touching a bod None - Nastran will calculate a default distance value as the smallest value resulting from either: Dividing the smallest nonzero element dimension (plates or solids) in the contact body by 20. Dividing the thinnest shell thickness in the contact body by 4 This value is then used for all contact pairs. error represents a Length quantity and is defined using the units of Length from the active script unit system.
- `getFgcflg() -> int` — Gets.
- `getFgcnst() -> float` — Gets specifies the equivalent normal contact stiffness FOR cohesive (flexible) glued contact This property may be assigned any one of the following values, any positive floating point value to define the normal contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default normal contact stiffness to all glued contact pairs.
- `getFgcnsti() -> int` — Gets specifies the equivalent normal contact stiffness for cohesive (flexible) glued contact using a table of stiffness values v's relative displacement This property may be assigned any one of the following values, n - any positive integer identify an existing TABL3D that defines the normal contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default normal contact stiffness to all glued contact pairs.
- `getFgcnstr() -> int` — Gets specifies the equivalent normal contact stiffness for cohesive (flexible) glued contact using a table of stiffness values This property may be assigned any one of the following values, n - any positive integer identify an existing TABL3D that defines the normal contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default normal contact stiffness to all glued contact pairs.
- `getFgcrcen() -> int` — Gets specifies an optional Grid ID at which the resultant contact force of secondary body to primary body will be evaluated This property may be assigned either one of the following values, any positive integer that uniquely identifies an exiting Grid in the model where the resultant force will be calculated None - this field will not be written to the Nastran file for this BCPARA entry.
- `getFgcrcn1() -> int` — Gets specifies an optional Grid ID at which the resultant contact force of the primary body to the secondary body will be evaluated This property may be assigned either one of the following values, any positive integer that uniquely identifies an exiting Grid in the model where the resultant force will be calculated None - this field will not be written to the Nastran file for this BCPARA entry.
- `getFgctst() -> float` — Gets specifies the equivalent tangent contact stiffness FOR cohesive (flexible) glued contact This property may be assigned any one of the following values, any positive floating point value to define the tangent contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default tangential contact stiffness to all glued contact pairs.
- `getFgctsti() -> int` — Gets.
- `getFgctstr() -> int` — Gets specifies the equivalent tangential contact stiffness for cohesive (flexible) glued contact using a table of stiffness values This property may be assigned any one of the following values, n - any positive integer identifying an existing TABL3D that defines the tangent contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default tangential contact stiffness to all glued contact pairs.
- `getFntol() -> float` — Gets specifies the separation force (or stress) above which a node will separate from a body the value assigned here will represent either a Force or a Stress depending on the value assigned to the 'ibsep' property of this class This property may be assigned either of the following values, any real number representing the separation force or stress None - this field will not be written to the Nastran file for the BCPARA entry and Nastran will assign a default value based on the value assigned to the "ibsep" property of this BCPARA entry.
- `getFtype() -> int` — Gets specifies which type of friction will be used in contact pairs This property may be assigned any one of the following values, 0 - No friction None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 6 - Bilinear Coulomb friction 7 - Bilinear Shear friction.
- `getGlueout() -> int` — Gets specifies how contact force and stress are output for glued contact This property may must be assigned any one of the following values, 0 -Normal and tangential components are separated (segment to segment only) 1 - Normal and tangential components are combined None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (1 is the Nastran default value for this field)
- `getIbsep() -> int` — Gets specifies how contact pairs use forces or stresses for separation This property may be assigned any one of the following values, 0 - Separation is based on forces None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Separation is based on absolute stresses (Force/Area) 2 - Separation based on absolute stress (extrapolating integration point stresses) 3 - Separation is based on relative nodal stress (force/area) 4 - Separation based on relative stress (extrapolating integration point stresses)
- `getIcsep() -> int` — Gets specifies how contact pairs separate during solution. This property may be assigned any one of the following values, 0 - The node separates and an iteration occurs if the force on the node is greater than the separation force None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - If a node which was in contact at the end of the previous increment has a force greater than the separation force, the node does NOT separate in this increment, but separates at the beginning of the next increment 2 - If a new node comes into contact during this increment, it is not allowed to separate during this increment to prevent chattering 3 - Combines the effects of 1 and 2.
- `getLincnt() -> int` — Gets specifies whether linear (under infinitesimal assumption, small sliding with small deformation and rotation or general contact assumptions will be used This property may be assigned any one of the following values, 0 - General contact assumptions will be used None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Linear contact assumptions will be used - contact force is distributed based upon undeformed geometry -1 - force Linear Contact with large displacement (not recommended).
- `getMaxsep() -> int` — Gets specifies the maximum number of times contact pairs are allowed to separate during each solution increment This property may be assigned either of the following values, any positive integer greater than 0 - this is the number of separations allowed per increment None - this file will not be written to the Nastran file for this BCPARA and Nastran will assign a default value of 9999.
- `getMethod() -> str` — Gets defines which contact method will be used for all contact pairs This property may be assigned any one of the following values, "NODESURF" - Node to segment contact None - same as "NODESURF" with the exception that this field will not be written to the Nastran file for this BCPARA ("NODESURF" is the Nastran default value for this field) "SEGTOSEG" - Segment to segment contact (distributed penalty) "S2SNP" = Segment to segment contact (nodal penalty)
- `getNlglue() -> int` — Gets specifies the use of permanent glued contact with small rotations under certain conditions, This property may be assigned either of the following values, 0 - does not specify the use of permanent glued contact under the conditions described below None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - If all secondary's for the BCTABLE or BCONPRG corresponding to the first loadcase (first subcase and first step) contain IGLUE >0, permanent glued contact with small rotation condition will be used for all SECNDRY entries in all subcases and all steps unless BCPARA,0,NLGLUE,1 is specified. If IGLUE < 0 exists in the first subcase and first step, STEP Glued Contact is activated, it behaves as conventional Permanent Glued Contact but for large deformation and rotation within the corresponding load case.
- `getNodsep() -> int` — Gets specifies whether or not separation checks will be carried out for grids that have previously touched and subsequently separated This property may be assigned any of the following values, any positive integer - continue separation checks for grids even though they have previously touched and subsequently separated None - same as assigning any positive integer with the exception that this field will not be written to the Nastran file for this BCPARA (this is the Nastran default behavior for this field) any negative integer - separation checks will be skipped for grids that have previously touched and subsequently separated.
- `getOsplnfrq() -> int` — Gets specifies how often smooth line representations of deformable contact bodies will be output when BOUTPUT is requested This property may must be assigned any one of the following values, -1 smooth line representations will be output at the first output request only None - same as -1 with the exception that this field will not be written to the Nastran file for this BCPARA (-1 is the Nastran default value for this field) 0 - No output of smooth line representations n - any positive integer, Smooth line representations will be output at the first output request and at every "nth" output increment Note that this property is based on the number of output load increments, but not calculated load increments. It is determined by "NO" in fixed time stepping or "NOUT" in adaptive time stepping on NLSTEP.
- `getPenalt() -> float` — Gets specifies the augmented Lagrange penalty factor when Lagrange augmentation is requested by the "method" property This property may be assigned any one of the following values, any real number. This value will be used as the penalty factor for Lagrange augmentation None - Nastran will use a default penalty factor and this this field will not be written to the Nastran file for this BCPARA. The default penalty is calculated internally by Nastran.
- `getRvcnst() -> float` — Gets specifies a slip threshold when bilinear friction is active in contact pairs This property may be assigned either of the following values, any real number greater than or equal to 0.0 None - same as setting this value to 0.0 with the exception that this field will not be written to the Nastran file for this BCPARA (0.0 is the Nastran default value for this field and causes Nastran to create a default slip threshold value)
- `getSegangl() -> float` — Gets specifies the minimum angle between segment normal vectors that allows the segments to come into contact This property is only valid when segment to segment contact is active This property may be assigned any one of the following values, any real number greater than 90. and less than 180. This value will be used to define the minimum angle in degrees between segment normals that will allow the segments to come into contact None - same as setting this property value to 120.0 with the exception that this field will not be written to the Nastran file.(120.0 is the default Nastran value for this field)
- `getSegsym() -> int` — Gets specifies the use of symmetric or non-symmetric friction matrices when segment to segment contact is active This property may be assigned either of the following values, 0 - A symmetric friction matrix will be used None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - A non-symmetric friction matrix will be used.
- `getSepacc() -> int` — Gets specifies whether or not to use accelerated separation checks in node to segment contact in Solution 400 This property may must be assigned any one of the following values, 0 - Accelerated separation checks are disabled None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (1 is the Nastran default value for this field) 1 - Accelerated separation checks are enabled.
- `getSfnpnlt() -> float` — Gets specifies the scale factor used by the augmented Lagrange penalty factor along the normal contact direction when segment to segment contact is active This property may be assigned any one of the following values, any real number. This value will be used to scale the penalty factor assigned using the "penalt" property of this BCPARA None - same as setting this property to 1.0. Nastran will use the value assigned to the "penalt" property of this BCPARA directly as the Lagrange penalty factor.
- `getSftpnlt() -> float` — Gets specifies the scale factor used by the augmented Lagrange penalty factor along the tangential contact direction when segment to segment contact is active This property may be assigned any one of the following values, any real number. This value will be used to scale the penalty factor assigned using the "penalt" property of this BCPARA None - same as setting this property value to 1.0. Nastran will use the value assigned to the "penalt" property of this BCPARA directly as the Lagrange penalty factor.
- `getSkip_separation_checks() -> str` — Gets a property to enable skipping of separation checks after a grid has initially touched and subsequently separated within an increment. In addition to enabling skipping of separation checks this property can define how the affect grids will behave during the period that separation checks are skipped This property may be assigned any one of the following values, "KEEP" - the grid will be retained in the contact definition even though separation checks are skipped "REMOVE" - the grid will be removed from the contact definition "OMIT" - Separation checks will NOT be skipped.
- `getSldlmt() -> float` — Gets defines a maximum allowed sliding distance beyond which contact segments will be redefined This property may be assigned either of the following values, any real number. This value defines a distance. If contact sliding greater than this value is detected, the contact segments will be recalculated None - same as setting this value to 0.0 with the exception that this field will not be written to the Nastran file for this BCPARA (0.0 is the Nastran default value for this field and will cause Nastran to use a sliding distance of 5 times the error tolerance)
- `getStkslp() -> float` — Gets specifies the maximum allowable slip distance for sticking. Beyond this distance sticking will not occur and only sliding will be present. This property is only valid when segment to segment contact is active This property may be assigned any one of the following values, any real number. This value will be used to define a distance beyond which sticking will not occur None - same as setting this property to 0.0. Nastran will set the sticking stiffness K1 equal to the maximum friction force divided by the maximum sticking displacement.
- `getTaugmnt() -> int` — Gets specifies whether or not augmentation will be used for the sticking part of contact when segment to segment contact is active This property may be assigned any one of the following values, 0 - augmentation will NOT be used for the sticking part of friction None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - use augmentation for the sticking part of friction.
- `getTcntctl() -> int` — Gets specifies how contact will be processed during linear perturbation analysis when contact has previously been calculated by an NLSTAUC analysis This property may must be assigned any one of the following values, 0 - Keep the original contact status defined during he original NLSTATIC analysis None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Linear perturbation analysis will assume sliding status of touching contact for contact and frictional stiffness matrix calculation. 2 - Linear perturbation analysis will assume sticking status of touching contact for contact and frictional stiffness matrix calculation. 3 - Linear perturbation analysis will assume glued contact status for touching contact for contact stiffness matrix calculation.
- `getThkoff() -> int` — Gets specifies whether or not thickness will be excluded in the tolerance when node to segment contact is active or from the characteristic length for augmentation when segment top segment contact is active This property may be assigned any one of the following values, 0 - include thickness in the tolerance/characteristic length calculations None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Remove thickness from the tolerance/characteristic length calculations.
- `getTpenalt() -> float` — Gets specifies the augmented Lagrange penalty factor for the sticking part of friction This property may be assigned any one of the following values, any real number. This value will be used as the penalty factor for Lagrange augmentation for the sticking part of contact None - Nastran will use a default penalty factor calculated from the value assigned to the "penalt" property divided 1000. and this this field will not be written to the Nastran file for this BCPARA.
- `getVersion() -> int` — Gets specifies whether to use Version 1 or Version 2 segment to segment contact default values This property may must be assigned any one of the following values, 1 - Use Version 1 segment to segment contact defaults. (These defaults are used "method" property of this BCPARA is set to "S2SNP") None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 2 - Use Version 2 segment to segment contact defaults. These defaults use a lower default penalty and are recommended None -.
#### `setAugdist(augdist: float) -> None`
Sets specifies a penetration distance beyond which augmentation will be applied This property must be assigned one of the following values, any real number. This value represents a distance. If contact surfaces penetrate each other by more than this distance, augmentation will be applied None - Nastran will automatically calculate a default augmentation distance and this field will not be written to the Nastran file for this BCPARA.

- `augdist` — Set the augdist of this BCPARA

#### `setAugment(augment: int) -> None`
Sets specifies the augmentation method that will be used when segment to segment contact is active This property may must be assigned any one of the following values, 0 - No augmentation None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Augmentation based on a constant Lagrange multiplier field for linear elements and on a (bi)linear Lagrange multiplier field for quadratic elements 2 - Augmentation based on a constant Lagrange multiplier field 3 - Augmentation based on a (bi)linear Lagrange multiplier field.

- `augment` — Set the augment of this BCPARA

#### `setBackctl(backctl: int) -> None`
Sets specifies backward compatibility contact analysis options This property may must be assigned any one of the following values, -1 - Activate all of compatibility items defined individually by values greater than 1 (shown below) 0 - No backward compatibility options will be activated None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Body order independent 2 - Evaluation of contact matrix/force on segment coordinates (old logic) 4 - Segment sequence renumbering (old method) 8 - No reset iteration count after separation (old logic) 15 - Creating new polygon under sliding condition (old logic) 32 - Scaled incremental displacement update in small rotation (old method) 64 - Ramping down penalty when angle of segment normals between 180 degree and SEGANGL 128 - Old algorithm of nodal projection in contact From release 2021.3 onwards, the default uses the enhanced contact projection algorithm, which helps in consistent contact detection at corners and for warped surface.

- `backctl` — Set the backctl of this BCPARA

#### `setBeamb(beamb: int) -> None`
Sets activates/deactivates beam to beam contact This property may be assigned any one of the following values, 0 - Beam to beam contact is disabled None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Activates beam to beam contact.

- `beamb` — Set the beamb of this BCPARA

#### `setBias(bias: float) -> None`
Sets defines the contact tolerance bias factor This property may be assigned either of the following values, a floating point value between 0.0 and 1.0 None - This field will not be written to the Nastran file for this BCPARA entry and Nastran will determine a default contact bias factor as follows, Default = 0.9 for IGLUE=0. Default = 0.0 for IGLUE <>0 Default = 0.0 for BEHAVE=SYMM on BCBODY.

- `bias` — Set the bias of this BCPARA

#### `setDdulmt(ddulmt: float) -> None`
Sets.

- `ddulmt` — Set the ddulmt of this BCPARA

#### `setDynprfa(dynprfa: float) -> None`
Sets specifies the dynamic contact projection factor This property may be assigned any one of the following values, any real number >=0.0 and <=1.0 None - same as setting this property value to 0.0 with the exception that this field will not be written to the Nastran file.(0.0 is the default Nastran value for this field) A value of 0.0 may show some penetration. Values greater than 0 reduce penetration and can introduce transient vibration. It is strongly recommended to use the default values in NLTRAN to avoid the chattering in contact analysis.

- `dynprfa` — Set the dynprfa of this BCPARA

#### `setErrbas(errbas: int) -> None`
Sets defines the basis for contact error calculation, 0 - Use global error claculations None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - calculate error based on each contact pair.

- `errbas` — Set the errbas of this BCPARA

#### `setError(error: float) -> None`
Sets optional property defining a distance below which a node is considered to be touching a body This property may be assigned either of the following values, any positive floating point value. The value defines a distance below which a nodes is considered to be touching a bod None - Nastran will calculate a default distance value as the smallest value resulting from either: Dividing the smallest nonzero element dimension (plates or solids) in the contact body by 20. Dividing the thinnest shell thickness in the contact body by 4 This value is then used for all contact pairs. error represents a Length quantity and is defined using the units of Length from the active script unit system.

- `error` — Set the error of this BCPARA

#### `setFgcflg(fgcflg: int) -> None`
Sets.

- `fgcflg` — Set the fgcflg of this BCPARA

#### `setFgcnst(fgcnst: float) -> None`
Sets specifies the equivalent normal contact stiffness FOR cohesive (flexible) glued contact This property may be assigned any one of the following values, any positive floating point value to define the normal contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default normal contact stiffness to all glued contact pairs.

- `fgcnst` — Set the fgcnst of this BCPARA

#### `setFgcnsti(fgcnsti: int) -> None`
Sets specifies the equivalent normal contact stiffness for cohesive (flexible) glued contact using a table of stiffness values v's relative displacement This property may be assigned any one of the following values, n - any positive integer identify an existing TABL3D that defines the normal contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default normal contact stiffness to all glued contact pairs.

- `fgcnsti` — Set the fgcnsti of this BCPARA

#### `setFgcnstr(fgcnstr: int) -> None`
Sets specifies the equivalent normal contact stiffness for cohesive (flexible) glued contact using a table of stiffness values This property may be assigned any one of the following values, n - any positive integer identify an existing TABL3D that defines the normal contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default normal contact stiffness to all glued contact pairs.

- `fgcnstr` — Set the fgcnstr of this BCPARA

#### `setFgcrcen(fgcrcen: int) -> None`
Sets specifies an optional Grid ID at which the resultant contact force of secondary body to primary body will be evaluated This property may be assigned either one of the following values, any positive integer that uniquely identifies an exiting Grid in the model where the resultant force will be calculated None - this field will not be written to the Nastran file for this BCPARA entry.

- `fgcrcen` — Set the fgcrcen of this BCPARA

#### `setFgcrcn1(fgcrcn1: int) -> None`
Sets specifies an optional Grid ID at which the resultant contact force of the primary body to the secondary body will be evaluated This property may be assigned either one of the following values, any positive integer that uniquely identifies an exiting Grid in the model where the resultant force will be calculated None - this field will not be written to the Nastran file for this BCPARA entry.

- `fgcrcn1` — Set the fgcrcn1 of this BCPARA

#### `setFgctst(fgctst: float) -> None`
Sets specifies the equivalent tangent contact stiffness FOR cohesive (flexible) glued contact This property may be assigned any one of the following values, any positive floating point value to define the tangent contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default tangential contact stiffness to all glued contact pairs.

- `fgctst` — Set the fgctst of this BCPARA

#### `setFgctsti(fgctsti: int) -> None`
Sets.

- `fgctsti` — Set the fgctsti of this BCPARA

#### `setFgctstr(fgctstr: int) -> None`
Sets specifies the equivalent tangential contact stiffness for cohesive (flexible) glued contact using a table of stiffness values This property may be assigned any one of the following values, n - any positive integer identifying an existing TABL3D that defines the tangent contact stiffness None - this field will not be written to the Nastran file for this BCPARA entry and Nastran will assign a default tangential contact stiffness to all glued contact pairs.

- `fgctstr` — Set the fgctstr of this BCPARA

#### `setFntol(fntol: float) -> None`
Sets specifies the separation force (or stress) above which a node will separate from a body the value assigned here will represent either a Force or a Stress depending on the value assigned to the 'ibsep' property of this class This property may be assigned either of the following values, any real number representing the separation force or stress None - this field will not be written to the Nastran file for the BCPARA entry and Nastran will assign a default value based on the value assigned to the "ibsep" property of this BCPARA entry.

- `fntol` — Set the fntol of this BCPARA

#### `setFtype(ftype: int) -> None`
Sets specifies which type of friction will be used in contact pairs This property may be assigned any one of the following values, 0 - No friction None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 6 - Bilinear Coulomb friction 7 - Bilinear Shear friction.

- `ftype` — Set the ftype of this BCPARA

#### `setGlueout(glueout: int) -> None`
Sets specifies how contact force and stress are output for glued contact This property may must be assigned any one of the following values, 0 -Normal and tangential components are separated (segment to segment only) 1 - Normal and tangential components are combined None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (1 is the Nastran default value for this field)

- `glueout` — Set the glueout of this BCPARA

#### `setIbsep(ibsep: int) -> None`
Sets specifies how contact pairs use forces or stresses for separation This property may be assigned any one of the following values, 0 - Separation is based on forces None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Separation is based on absolute stresses (Force/Area) 2 - Separation based on absolute stress (extrapolating integration point stresses) 3 - Separation is based on relative nodal stress (force/area) 4 - Separation based on relative stress (extrapolating integration point stresses)

- `ibsep` — Set the ibsep of this BCPARA

#### `setIcsep(icsep: int) -> None`
Sets specifies how contact pairs separate during solution. This property may be assigned any one of the following values, 0 - The node separates and an iteration occurs if the force on the node is greater than the separation force None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - If a node which was in contact at the end of the previous increment has a force greater than the separation force, the node does NOT separate in this increment, but separates at the beginning of the next increment 2 - If a new node comes into contact during this increment, it is not allowed to separate during this increment to prevent chattering 3 - Combines the effects of 1 and 2.

- `icsep` — Set the icsep of this BCPARA

#### `setLincnt(lincnt: int) -> None`
Sets specifies whether linear (under infinitesimal assumption, small sliding with small deformation and rotation or general contact assumptions will be used This property may be assigned any one of the following values, 0 - General contact assumptions will be used None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Linear contact assumptions will be used - contact force is distributed based upon undeformed geometry -1 - force Linear Contact with large displacement (not recommended).

- `lincnt` — Set the lincnt of this BCPARA

#### `setMaxsep(maxsep: int) -> None`
Sets specifies the maximum number of times contact pairs are allowed to separate during each solution increment This property may be assigned either of the following values, any positive integer greater than 0 - this is the number of separations allowed per increment None - this file will not be written to the Nastran file for this BCPARA and Nastran will assign a default value of 9999.

- `maxsep` — Set the maxsep of this BCPARA

#### `setMethod(method: str) -> None`
Sets defines which contact method will be used for all contact pairs This property may be assigned any one of the following values, "NODESURF" - Node to segment contact None - same as "NODESURF" with the exception that this field will not be written to the Nastran file for this BCPARA ("NODESURF" is the Nastran default value for this field) "SEGTOSEG" - Segment to segment contact (distributed penalty) "S2SNP" = Segment to segment contact (nodal penalty)

- `method` — Set the method of this BCPARA

#### `setNlglue(nlglue: int) -> None`
Sets specifies the use of permanent glued contact with small rotations under certain conditions, This property may be assigned either of the following values, 0 - does not specify the use of permanent glued contact under the conditions described below None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - If all secondary's for the BCTABLE or BCONPRG corresponding to the first loadcase (first subcase and first step) contain IGLUE >0, permanent glued contact with small rotation condition will be used for all SECNDRY entries in all subcases and all steps unless BCPARA,0,NLGLUE,1 is specified. If IGLUE < 0 exists in the first subcase and first step, STEP Glued Contact is activated, it behaves as conventional Permanent Glued Contact but for large deformation and rotation within the corresponding load case.

- `nlglue` — Set the nlglue of this BCPARA

#### `setNodsep(nodsep: int) -> None`
Sets specifies whether or not separation checks will be carried out for grids that have previously touched and subsequently separated This property may be assigned any of the following values, any positive integer - continue separation checks for grids even though they have previously touched and subsequently separated None - same as assigning any positive integer with the exception that this field will not be written to the Nastran file for this BCPARA (this is the Nastran default behavior for this field) any negative integer - separation checks will be skipped for grids that have previously touched and subsequently separated.

- `nodsep` — Set the nodsep of this BCPARA

#### `setOsplnfrq(osplnfrq: int) -> None`
Sets specifies how often smooth line representations of deformable contact bodies will be output when BOUTPUT is requested This property may must be assigned any one of the following values, -1 smooth line representations will be output at the first output request only None - same as -1 with the exception that this field will not be written to the Nastran file for this BCPARA (-1 is the Nastran default value for this field) 0 - No output of smooth line representations n - any positive integer, Smooth line representations will be output at the first output request and at every "nth" output increment Note that this property is based on the number of output load increments, but not calculated load increments. It is determined by "NO" in fixed time stepping or "NOUT" in adaptive time stepping on NLSTEP.

- `osplnfrq` — Set the osplnfrq of this BCPARA

#### `setPenalt(penalt: float) -> None`
Sets specifies the augmented Lagrange penalty factor when Lagrange augmentation is requested by the "method" property This property may be assigned any one of the following values, any real number. This value will be used as the penalty factor for Lagrange augmentation None - Nastran will use a default penalty factor and this this field will not be written to the Nastran file for this BCPARA. The default penalty is calculated internally by Nastran.

- `penalt` — Set the penalt of this BCPARA

#### `setRvcnst(rvcnst: float) -> None`
Sets specifies a slip threshold when bilinear friction is active in contact pairs This property may be assigned either of the following values, any real number greater than or equal to 0.0 None - same as setting this value to 0.0 with the exception that this field will not be written to the Nastran file for this BCPARA (0.0 is the Nastran default value for this field and causes Nastran to create a default slip threshold value)

- `rvcnst` — Set the rvcnst of this BCPARA

#### `setSegangl(segangl: float) -> None`
Sets specifies the minimum angle between segment normal vectors that allows the segments to come into contact This property is only valid when segment to segment contact is active This property may be assigned any one of the following values, any real number greater than 90. and less than 180. This value will be used to define the minimum angle in degrees between segment normals that will allow the segments to come into contact None - same as setting this property value to 120.0 with the exception that this field will not be written to the Nastran file.(120.0 is the default Nastran value for this field)

- `segangl` — Set the segangl of this BCPARA

#### `setSegsym(segsym: int) -> None`
Sets specifies the use of symmetric or non-symmetric friction matrices when segment to segment contact is active This property may be assigned either of the following values, 0 - A symmetric friction matrix will be used None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - A non-symmetric friction matrix will be used.

- `segsym` — Set the segsym of this BCPARA

#### `setSepacc(sepacc: int) -> None`
Sets specifies whether or not to use accelerated separation checks in node to segment contact in Solution 400 This property may must be assigned any one of the following values, 0 - Accelerated separation checks are disabled None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (1 is the Nastran default value for this field) 1 - Accelerated separation checks are enabled.

- `sepacc` — Set the sepacc of this BCPARA

#### `setSfnpnlt(sfnpnlt: float) -> None`
Sets specifies the scale factor used by the augmented Lagrange penalty factor along the normal contact direction when segment to segment contact is active This property may be assigned any one of the following values, any real number. This value will be used to scale the penalty factor assigned using the "penalt" property of this BCPARA None - same as setting this property to 1.0. Nastran will use the value assigned to the "penalt" property of this BCPARA directly as the Lagrange penalty factor.

- `sfnpnlt` — Set the sfnpnlt of this BCPARA

#### `setSftpnlt(sftpnlt: float) -> None`
Sets specifies the scale factor used by the augmented Lagrange penalty factor along the tangential contact direction when segment to segment contact is active This property may be assigned any one of the following values, any real number. This value will be used to scale the penalty factor assigned using the "penalt" property of this BCPARA None - same as setting this property value to 1.0. Nastran will use the value assigned to the "penalt" property of this BCPARA directly as the Lagrange penalty factor.

- `sftpnlt` — Set the sftpnlt of this BCPARA

#### `setSkip_separation_checks(skip_separation_checks: str) -> None`
Sets a property to enable skipping of separation checks after a grid has initially touched and subsequently separated within an increment. In addition to enabling skipping of separation checks this property can define how the affect grids will behave during the period that separation checks are skipped This property may be assigned any one of the following values, "KEEP" - the grid will be retained in the contact definition even though separation checks are skipped "REMOVE" - the grid will be removed from the contact definition "OMIT" - Separation checks will NOT be skipped.

- `skip_separation_checks` — Set the skip_separation_checks of this BCPARA

#### `setSldlmt(sldlmt: float) -> None`
Sets defines a maximum allowed sliding distance beyond which contact segments will be redefined This property may be assigned either of the following values, any real number. This value defines a distance. If contact sliding greater than this value is detected, the contact segments will be recalculated None - same as setting this value to 0.0 with the exception that this field will not be written to the Nastran file for this BCPARA (0.0 is the Nastran default value for this field and will cause Nastran to use a sliding distance of 5 times the error tolerance)

- `sldlmt` — Set the sldlmt of this BCPARA

#### `setStkslp(stkslp: float) -> None`
Sets specifies the maximum allowable slip distance for sticking. Beyond this distance sticking will not occur and only sliding will be present. This property is only valid when segment to segment contact is active This property may be assigned any one of the following values, any real number. This value will be used to define a distance beyond which sticking will not occur None - same as setting this property to 0.0. Nastran will set the sticking stiffness K1 equal to the maximum friction force divided by the maximum sticking displacement.

- `stkslp` — Set the stkslp of this BCPARA

#### `setTaugmnt(taugmnt: int) -> None`
Sets specifies whether or not augmentation will be used for the sticking part of contact when segment to segment contact is active This property may be assigned any one of the following values, 0 - augmentation will NOT be used for the sticking part of friction None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - use augmentation for the sticking part of friction.

- `taugmnt` — Set the taugmnt of this BCPARA

#### `setTcntctl(tcntctl: int) -> None`
Sets specifies how contact will be processed during linear perturbation analysis when contact has previously been calculated by an NLSTAUC analysis This property may must be assigned any one of the following values, 0 - Keep the original contact status defined during he original NLSTATIC analysis None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Linear perturbation analysis will assume sliding status of touching contact for contact and frictional stiffness matrix calculation. 2 - Linear perturbation analysis will assume sticking status of touching contact for contact and frictional stiffness matrix calculation. 3 - Linear perturbation analysis will assume glued contact status for touching contact for contact stiffness matrix calculation.

- `tcntctl` — Set the tcntctl of this BCPARA

#### `setThkoff(thkoff: int) -> None`
Sets specifies whether or not thickness will be excluded in the tolerance when node to segment contact is active or from the characteristic length for augmentation when segment top segment contact is active This property may be assigned any one of the following values, 0 - include thickness in the tolerance/characteristic length calculations None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 1 - Remove thickness from the tolerance/characteristic length calculations.

- `thkoff` — Set the thkoff of this BCPARA

#### `setTpenalt(tpenalt: float) -> None`
Sets specifies the augmented Lagrange penalty factor for the sticking part of friction This property may be assigned any one of the following values, any real number. This value will be used as the penalty factor for Lagrange augmentation for the sticking part of contact None - Nastran will use a default penalty factor calculated from the value assigned to the "penalt" property divided 1000. and this this field will not be written to the Nastran file for this BCPARA.

- `tpenalt` — Set the tpenalt of this BCPARA

#### `setVersion(version: int) -> None`
Sets specifies whether to use Version 1 or Version 2 segment to segment contact default values This property may must be assigned any one of the following values, 1 - Use Version 1 segment to segment contact defaults. (These defaults are used "method" property of this BCPARA is set to "S2SNP") None - same as 0 with the exception that this field will not be written to the Nastran file for this BCPARA (0 is the Nastran default value for this field) 2 - Use Version 2 segment to segment contact defaults. These defaults use a lower default penalty and are recommended None -.

- `version` — Set the version of this BCPARA


## `apex.studies.BucklingSimulationSettings`  (extends `SimulationSettings`)
This class manages the simulation settings for Normal Modes Simulation Steps. An instance of this class is created and populated with default values whenever a Normal Modes Step is created.
Properties: `interactionControl`, `numBucklingModes`

Methods:

- `getInteractionControl() -> apex.studies.InteractionControl`
- `getNumBucklingModes() -> int`
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None`
- `setNumBucklingModes(numBucklingModes: int) -> None`

## `apex.studies.BucklingStep`  (extends `Step`)
BucklingStep is used to define the calculation of the linear buckling modes of a system.

Methods:

#### `getSimulationSettings() -> apex.studies.BucklingSimulationSettings`
returns the simulation settings from this scenario

Returns: the simulationSettings object


## `apex.studies.DBSAVE`  (extends `ScenarioCommand`)
Class representing the Nastran "DBSAVE" case control command The DBSAVE command is used to save data associated with advanced nonlinear elements to enable use of these elements in linear perturbation steps or other steps that require nonlinear initial conditions.
Properties: `value`

Methods:

- `getValue() -> int` — Gets integer value used to select how often the nonlinear element data will be saved. This property may be assigned the following values, 0 (Default) - Data will be saved to the Nastran database at the end of each load case -1 - No advanced nonlinear element data will be saved n - save the advanced nonlinear element data every nth output request.
#### `setValue(value: int) -> None`
Sets integer value used to select how often the nonlinear element data will be saved. This property may be assigned the following values, 0 (Default) - Data will be saved to the Nastran database at the end of each load case -1 - No advanced nonlinear element data will be saved n - save the advanced nonlinear element data every nth output request.

- `value` — Set the value of this DBSAVE


## `apex.studies.DEFORM`  (extends `ScenarioCommand`)
Class representing a Nastran DEFORM case control command. DEFORM commands are used to select one or more element deformation sets applied to the model, for inclusion in a LoadCaseItem. Element deformations are identified by their ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of a element deformation load assigned to the model referenced by the Scenario that this command is composed by Use this command to assign element deformation loads to a Scenario, Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets the ID of a element deformation load assigned to the model referenced by the Scenario that this command is composed by Use this command to assign element deformation loads to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this DEFORM


## `apex.studies.DLOAD`  (extends `ScenarioCommand`)
Class representing a Nastran DLOAD case control command. DLOAD commands are used to select one or more dynamic Loads, applied to the model, for inclusion in a LoadCaseItem. Dynamic Loads are identified by their ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of a dynamic load assigned to the model referenced by the Scenario that this command is composed by. Use this command to assign a dynamic load to a Scenario, Subcase or Step.
#### `setValue(value: int) -> None`
Sets the ID of a dynamic load assigned to the model referenced by the Scenario that this command is composed by. Use this command to assign a dynamic load to a Scenario, Subcase or Step.

- `value` — Set the value of this DLOAD


## `apex.studies.DesignRules`
Define the Design Rules Setting for the current scenario setting. An example as below: # -------------------------------------------------------------------------------------- # create a Design Rules Setting and set the values for it. gdSimSetting = simSettings[0].asSimulationSettingsGenerativeDesign() myDesignRuleSetting = gdSimSetting.gdSimSetting.designRules() myDesignRuleSetting.update( reductionStrategy = Active ) # -------------------------------------------------------------------------------------- # create the simulationSettings and set a Design Rules setting to the simulation simSetting1 = scenario1.simulationSettings() simSetting1.manufacturing = apex.studies.FDM simSetting1.designRules = myDesignRuleSetting # set a design rules setting to the simulation simSetting1.buildDirection = apex.construct.createOrientation(alpha=270., beta=90., gamma=0.0) simSetting1.strutDensity = xx simSetting1.shapeQuality = xx simSetting1.complexity = xx simSetting1.keepNonDesignRegions = xx # # --------------------------------------------------------------------------------------
Properties: `reductionStrategy`

Methods:

- `getReductionStrategy() -> apex.studies.ReductionStrategy` — These are just names that we invented for the different strategies of the support reduction. Low is only influencing the design a little bit but Medium and High are more aggressive and can be influenced by the intensity value.
#### `setReductionStrategy(reductionStrategy: apex.studies.ReductionStrategy) -> None`
Define a Reduction Strategy for current scenario.

- `reductionStrategy` — Define the reduction strategy for current scenario

#### `update(reductionStrategy: apex.studies.ReductionStrategy) -> None`
update the Design Rules for current scenario

- `reductionStrategy` — Define the reduction strategy for current scenario


## `apex.studies.DirectTextInput`
Properties: `bulkDataStatements`, `caseControlsStatements`, `executiveControlStatements`, `exportOptions`, `fileManagementStatements`, `systemCells`

Methods:

- `clearDirectTextInput(target: [apex.studies.DTIBlockType]) -> None` — Removes all content from selected Direct Text Input blocks. The blocks to be cleared are passed into this method using the "target" argument. If "target" is omitted, the content of all Direct Text Input blocks will be removed.
- `getBulkDataStatements() -> str` — A list of strings that are intended to represent Bulk Data Statements in the Nastran solver file.
- `getCaseControlsStatements() -> str` — A list of strings that are intended to represent Case Control Statements in the Nastran solver file.
- `getExecutiveControlStatements() -> str` — A list of strings that are intended to represent Executive Control Statements in the Nastran solver file.
- `getExportOptions() -> {apex.studies.DTIBlockType:apex.studies.DTIExportOptions}` — A map of Direct Text Input Export Options types.
- `getFileManagementStatements() -> str` — A list of strings that are intended to represent File Management Statements in the Nastran solver file.
- `getSystemCells() -> str` — A List of strings that represent system cells.
- `update(SystemCells: str, FileManagement: str, ExecutiveControl: str, CaseControl: str, BulkData: str, exportOptions: {apex.studies.DTIBlockType:apex.studies.DTIExportOptions}) -> None`

## `apex.studies.DynamicsStep`  (extends `Step`)
DynamicsStep is used to define calculation of the normal modes of a system.

## `apex.studies.ECHO`  (extends `ScenarioCommand`)
Class represnting a Nastran "ECHO" case control command The ECHO command is used to control output of the bulk data entries from the input file to the print and punch output files.
Properties: `output_punch`, `sort_print`, `sort_punch`, `unsorted_entries`

Methods:

- `getOutput_punch() -> str` — Gets optional property that enables/disables output (echo) of bulk data entries to the punch file This property may be assigned the following values, "None" (or omitted) - no bulk data entries will be written to the punch file "PUNCH" - bulk data entries will be written to the punch file/ This property must be set to "PUNCH" to activate the "sort_punch" options.
- `getSort_print() -> str` — Gets optional property used to control sorting of the bulk data when written to the printed output file, This property accepts the following values, "SORT" - Bulk data will be sorted in alphabetical order when written to the printed output file None - Same as "SORT" except that this field will not be written to the Nastran file for this ECHO command - "SORT" is the Nastran default "UNSORT" - Include unsorted bulk data (entries defined using the "except" property of this class) in the printed output "BOTH" - Include both sorted and unsorted entries in the printed output "NONE" - Do not print bulk data to the printed output.
- `getSort_punch() -> str` — Gets optional property used to control sorting of the bulk data when written to the PUNCH output file, This property will be silently ignored unless the "output_punch" property is set to "PUNCH" This property accepts the following values, "SORT" - Bulk data will be sorted in alphabetical order when written to the punch output file None - Same as "SORT" except that this field will not be written to the Nastran file for this ECHO command - "SORT" is the Nastran default "BOTH" - Include both sorted and unsorted entries in the punch output "NEWBULK" - In Solution 200, write the entire unsorted bulk data to the punch file with updated design model entries.
- `getUnsorted_entries() -> str` — Gets optional property defining a list of bulk data entries that will NOT be sorted prior to being written to the print file. This list does NOT affect output to the punch file if punch output is requested. This property accepts a list of strings where each string represents a valid Nastran bulk data entry. The bulk data entries contained in this list will not be sorted prior to being written to the print file.
#### `setOutput_punch(output_punch: str) -> None`
Sets optional property that enables/disables output (echo) of bulk data entries to the punch file This property may be assigned the following values, "None" (or omitted) - no bulk data entries will be written to the punch file "PUNCH" - bulk data entries will be written to the punch file/ This property must be set to "PUNCH" to activate the "sort_punch" options.

- `output_punch` — Set the output_punch of this ECHO

#### `setSort_print(sort_print: str) -> None`
Sets optional property used to control sorting of the bulk data when written to the printed output file, This property accepts the following values, "SORT" - Bulk data will be sorted in alphabetical order when written to the printed output file None - Same as "SORT" except that this field will not be written to the Nastran file for this ECHO command - "SORT" is the Nastran default "UNSORT" - Include unsorted bulk data (entries defined using the "except" property of this class) in the printed output "BOTH" - Include both sorted and unsorted entries in the printed output "NONE" - Do not print bulk data to the printed output.

- `sort_print` — Set the sort_print of this ECHO

#### `setSort_punch(sort_punch: str) -> None`
Sets optional property used to control sorting of the bulk data when written to the PUNCH output file, This property will be silently ignored unless the "output_punch" property is set to "PUNCH" This property accepts the following values, "SORT" - Bulk data will be sorted in alphabetical order when written to the punch output file None - Same as "SORT" except that this field will not be written to the Nastran file for this ECHO command - "SORT" is the Nastran default "BOTH" - Include both sorted and unsorted entries in the punch output "NEWBULK" - In Solution 200, write the entire unsorted bulk data to the punch file with updated design model entries.

- `sort_punch` — Set the sort_punch of this ECHO

#### `setUnsorted_entries(unsorted_entries: str) -> None`
Sets optional property defining a list of bulk data entries that will NOT be sorted prior to being written to the print file. This list does NOT affect output to the punch file if punch output is requested. This property accepts a list of strings where each string represents a valid Nastran bulk data entry. The bulk data entries contained in this list will not be sorted prior to being written to the print file.

- `unsorted_entries` — Set the unsorted_entries of this ECHO


## `apex.studies.Event`  (extends `Entity`, `IName`, `IUserAttributes`)
An Event defines a combination of constraints and LoadReps that are applied during the simulation of a Step. The combination of LoadReps and Constraints in an Event is intended to represent some design operating condition that the Design will experience. The state of the Mechanical System at the end of a Step is caused by the application of the LoadReps and Constraints to the MechanicalSystem during the Step, causing the initial state of the system to change.
Properties: `constraints`, `loads`, `resultsDataAvailable`

Methods:

#### `addConstraint(constraint: apex.Entity) -> None`
Add a Constraint to this Event.

- `constraint` — The constraint will be added to the Event

#### `addLoad(load: apex.Entity, loadRep: apex.Entity = None) -> None`
Add a Load to an Event.

- `load` — The load will be added to the Event
- `loadRep` — The load representation will be added to the Event. This argument is optional since load may not have a loadRep

- `getConstraints() -> apex.EntityCollection` — Return a collection of Constraint objects that are associated with this event.
- `getLoads() -> apex.EntityCollection` — Return a collection of LoadRep or Load objects that don't have LoadReps that are associated with this event.
- `getResultsDataAvailable() -> bool` — True if any ResultsData is available for this Event, otherwise False.
#### `importResultData(resultFilename: str, resultFileType: apex.post.ResultFileType) -> None`
Imports results data to this Scenario from an external results file. Currently this method only supports import of Adams/Car results data and for this case the Event must be composed by a MultiBody Dynamics Step.

- `resultFilename` — The fully qualified filename of the result file.
- `resultFileType` — The type of result file to import as an apex.post.ResultFileType enumeration. Currently, only Adams/Car result file types are supported.

#### `removeConstraint(constraint: apex.Entity) -> None`
Removes a Constraint from an Event.

- `constraint` — The constraint to be removed from the Event

#### `removeLoad(load: apex.Entity) -> None`
Removes a Load from this Event.

- `load` — The load to be removed from the Event

#### `update(name: str) -> None`
Update this Scenario Event.

- `name` — the name of this Scenario Event to be updated


## `apex.studies.EventCollection`  (extends `EntityCollection`)

Methods:

- `EventCollection() -> None` — Construct a new EventCollection.

## `apex.studies.ExecutedScenario`  (extends `Scenario`)
a executed version of a Scenario
Properties: `steps`

Methods:

#### `getAssembly(pathName: str) -> apex.Assembly`
Get the AsseAssembly that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getBeamSpan(pathName: str) -> apex.attribute.BeamSpan`
Get the beam span that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

- `getBucklingStep() -> apex.studies.Step` — Get the buckling step if the executed scenario is buckling.
#### `getConnector(pathName: str) -> apex.attribute.Connector`
Get the connector that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getConstraint(pathName: str) -> apex.environment.DisplacementConstraint`
Get the constraint that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getCoordinateSystem(pathName: str) -> apex.construct.CoordinateSystem`
Get the coordinate system that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getCrossSectionSensor(pathName: str) -> apex.instrument.XSectionForceSensor`
Get the cross section sensor that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getElement(pathName: str, id: int) -> apex.mesh.Element`
Get the element that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name
- `id` — the id of element

#### `getElements(pathName: str, ids: str) -> apex.mesh.ElementCollection`
Get the element collection that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name
- `ids` — the ids of elements which was ranged with "-" and separated with ","., e.g "9-9,50-52"

#### `getEvent(pathName: str) -> apex.studies.Event`
Get the event given the executed scenario's relative pathName.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getForceMoment(pathName: str) -> apex.environment.ForceMoment`
Get the forceMoment that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getInterfacePoint(pathName: str) -> apex.attribute.InterfacePoint`
Get the interface point that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

- `getLinearStep() -> apex.studies.Step` — Get the linear step if the executed scenario is linear static.
#### `getLoadCase(pathName: str) -> apex.studies.LoadCase`
Get the loadcase given the executed scenario's relative name.

- `pathName` — the path to the object to be retrieved including the object's path name

#### `getMesh(pathName: str) -> apex.mesh.MeshBody`
Get the node that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getName() -> str`
Read-only string representing the name of this object.

Returns: this entity name (string)

getName() may also be accessed as an Entity property 'name'. For example:

#### `getNode(pathName: str, id: int) -> apex.mesh.Node`
Get the node that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name
- `id` — the id of node

#### `getNodes(pathName: str, ids: str) -> apex.mesh.NodeCollection`
Get the node collection that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name
- `ids` — the ids of nodes which was ranged with "-" and separated with ","., e.g "9-9,50-52"

#### `getPart(pathName: str) -> apex.Part`
Get the part that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/

- `getPreLoadStep() -> apex.studies.Step` — Get the preload step if the executed scenario is buckling.
- `getScenarioModelRep() -> apex.ModelRep` — Get the model rep that is associated with the executed scenario.
#### `getStep(pathName: str) -> apex.studies.Step`
Get the step given the executed scenario's relative pathName.

- `pathName` — the path to the object to be retrieved including the object's name

#### `getSteps() -> apex.studies.StepCollection`
returns an ordered collection of the Steps in an ExecutedScenario

Returns: an ordered collection of the Steps in an ExecutedScenario

#### `getXSectionForceSensorArray(pathName: str) -> apex.instrument.XSectionForceSensorArray`
Get the XSection force sensor array that is associated with an ExecutedScenario.

- `pathName` — the path to the object to be retrieved including the object's name


## `apex.studies.FEMCHECK`  (extends `ScenarioCommand`)
Class representing a Nastran FEMCHECK case control command The FEMCHECK command is used to specify model checking options that will be carried out at the start of a Nastran run.
Properties: `user_checks`, `value`

Methods:

- `getUser_checks() -> str` — Gets defines the subset of model checks that will be carried out at the start of the Nastran run This property must be defined if "value" is set to "USER" This property may be assigned the following values A list of strings containing any combination of the following values RBE2 - provides a warning for each dependent grid on an RBE2 entry that is not attaches to an element, PLOTEL or DMIG RBE3 - checks that every independent grid on an RBE3 entry is attache to an element, PLOTEL or DMIG DLOAD - Checks if a DLOAD command is present in a frequency analysis. Checks that DLOAD or IC is is defined for transient analysis. Checks that each DLOAD case control command references a valid bulk data entry (DLOAD, RLOAD1, RLOAD2, TLOAD1, TLOAD2, ACSRCE, ACLOAD) FREQ - Checks that a FREQUENCY case control command is defined for frequency analyses and that it refers to a valid FREQ, FREQ1, FREQ2, FREQ3, FREQ4 or FREQ5 entry SDAMP - Checks that any SDMAPING commands reference valid TABLED1, TABLED2, TABLED3, TABLED4, TABLED5 or TABDMP1 entries TSTEP - For solution sequences 108, 109, 1111 and 112 checks that TSTEP case control commands reference a TSTEP bulk entry. For solution sequences 129 and 150, checks that the TSTEP case control command references a valid TSTEPNL entry.
- `getValue() -> str` — Gets property used to define the scope of model checking that will be carried out at the start of the Nastran run This property may be assigned any of the following values, "NONE" - No model checking will be carried out None - same as "NONE" wit the exception that this field will not be written to the Nastran file for this FEMCHECK command. ("NONE" is the Nastran default) "ALL" - All model checks will be carried out "USER" - A set of user defined checks will be carried out. Setting this option requires values also be assigned to the "user_checks" property.
#### `setUser_checks(user_checks: str) -> None`
Sets defines the subset of model checks that will be carried out at the start of the Nastran run This property must be defined if "value" is set to "USER" This property may be assigned the following values A list of strings containing any combination of the following values RBE2 - provides a warning for each dependent grid on an RBE2 entry that is not attaches to an element, PLOTEL or DMIG RBE3 - checks that every independent grid on an RBE3 entry is attache to an element, PLOTEL or DMIG DLOAD - Checks if a DLOAD command is present in a frequency analysis. Checks that DLOAD or IC is is defined for transient analysis. Checks that each DLOAD case control command references a valid bulk data entry (DLOAD, RLOAD1, RLOAD2, TLOAD1, TLOAD2, ACSRCE, ACLOAD) FREQ - Checks that a FREQUENCY case control command is defined for frequency analyses and that it refers to a valid FREQ, FREQ1, FREQ2, FREQ3, FREQ4 or FREQ5 entry SDAMP - Checks that any SDMAPING commands reference valid TABLED1, TABLED2, TABLED3, TABLED4, TABLED5 or TABDMP1 entries TSTEP - For solution sequences 108, 109, 1111 and 112 checks that TSTEP case control commands reference a TSTEP bulk entry. For solution sequences 129 and 150, checks that the TSTEP case control command references a valid TSTEPNL entry.

- `user_checks` — Set the user_checks of this FEMCHECK

#### `setValue(value: str) -> None`
Sets property used to define the scope of model checking that will be carried out at the start of the Nastran run This property may be assigned any of the following values, "NONE" - No model checking will be carried out None - same as "NONE" wit the exception that this field will not be written to the Nastran file for this FEMCHECK command. ("NONE" is the Nastran default) "ALL" - All model checks will be carried out "USER" - A set of user defined checks will be carried out. Setting this option requires values also be assigned to the "user_checks" property.

- `value` — Set the value of this FEMCHECK


## `apex.studies.FREQUENCY`  (extends `ScenarioCommand`)
Class representing a Nastran FREQUENCY case control command. FREQUENCY commands are used to select the forcing frequencies to be solved in frequency response problems, for inclusion in a frequency response Subcase or Step. Forcing frequencies can be define using FREQ, FREQ1, FREQ2, FREQ3, FREQ4 and FREQ5 entries, each of which has an ID and each of these entries may share the same ID. The ID set here will cause all of entries that share the ID to be used to define the forcing frequencies for the analysis.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of FREQ, FREQ1, FREQ2, FREQ3, FREQ4 and FREQ5 entries assigned to the model referenced by the Scenario that this command is composed by Use this command to assign one or more of the above entries to a Subcase or Step.
#### `setValue(value: int) -> None`
Sets the ID of FREQ, FREQ1, FREQ2, FREQ3, FREQ4 and FREQ5 entries assigned to the model referenced by the Scenario that this command is composed by Use this command to assign one or more of the above entries to a Subcase or Step.

- `value` — Set the value of this FREQUENCY


## `apex.studies.FRF`  (extends `ScenarioCommand`)
Class representing a Nastran FRF case control command The FRF command is used to provide information required for the generation of frequency response functions (FRF) and/or for use in frequency base assembly (FBA) proceses.
Properties: `asmout`, `compid`, `compname`, `connpts`, `frf_generation`, `frf_store`, `icf_op2_unit`, `icf_store`, `icfauto`, `icfgen`, `icfuse`, `loadlbl`, `op2_unit`, `xitout`

Methods:

- `getAsmout() -> str` — Gets options for the frequency based assembly process This property may be assigned any one of the following values, "COMP" None "ALL" "ASSEMBLY" "CONNINFO" n - cname -.
- `getCompid() -> int` — Gets the id of the component whose FRFs are to be generated This property may be assigned either of the following values, n - a positive integer used to select an existing component wit the same ID None - this field will not be written to the Nastran file for this FRF command.
- `getCompname() -> str` — Gets the name of the component whose FRFs are to be generated This property may be assigned either of the following values, a string value used to select an existing component with the same name None - this field will not be written to the Nastran file for this FRF command.
- `getConnpts() -> int` — Gets the ID of an existing Scenario SET that defines the points at which the FRF component specified by the "compid"/"compname" properties are to be connected during a subsequent FRF assembly (FBA) process This property may be assigned either of the following values, n - a positive integer used to select an existing Scenario SET that defines the IDs of the connection grids None - this filed will not be written to the Nastran file for this FRF command.
- `getFrf_generation() -> str` — Gets property used to control which FRFs are generated This property may be assigned any of the following values, "GEN" - generate FRFs for the specified component None - same as "GEN" with the exception that this field will not be written to the Nastran file for this BCPARA ("GEN" is the Nastran default value for this field) "ASM" - generate FRFs from an assembly of components from the FRFs of the individual components "GENASM"- generate FRFs for the specified component and then compute the FRFs of an assembly of components from the FRFs of the individual components.
- `getFrf_store() -> str` — Gets an optional property used to define whether the FRF matrices are stored on the Nastran database or on a .op2 file. This property may be assigned any one of the following values, "DB" - the FRF matrices will be stored on the current Nastran database None - same as "DB" with the exception that this field will not be written to the Nastran file for this FRF command (the Nastran default for this field is "DB") "OP2" - the FRF matrices will be stored on an external /op2 file Note: If this property is assigned the value "OP2", the associated "op2_unit" property must also be provided.
- `getIcf_op2_unit() -> int` — Gets a positive integer identifying the Nastran Fortran unit number associated with the .op2 file where the ICF data is stored This property MUST be provided if the icf_store property is set to "ICFOP2", otherwise it will be silently ignored.
- `getIcf_store() -> str` — Gets an optional property used to define whether the ICF data is stored on the Nastran database or on a .op2 file. This property may be assigned any one of the following values, "ICFDB" - the ICF data will be stored on the current Nastran database None - same as "ICFDB" with the exception that this field will not be written to the Nastran file for this FRF command (the Nastran default for this field is "ICFDB") "ICFOP2" - the ICF data will be stored on an external /op2 file Note: If this property is assigned the value "ICFOP2", the associated "icf_op2_unit" property must also be provided.
- `getIcfauto() -> str` — Gets a property the defines how Nastran will GENERATE and USE use ICF information in the FBA process. This property may be assigned any one of the following values, +n - (a POSITIVE integer value) First generate and then use ICF information in the FBA process only for those FRF components whose IDs are specified by SET ID n. -n - (a NEGATIVE integer value) First generate and then use ICF information only for the single FRF component whose ID is given by |n|. compname - (a string value) First generate and then use ICF information for the single FRF component whose name is given by here.
- `getIcfgen() -> str` — Gets a property the defines how Nastran will Generate ICF information for the FRF component whose name is defined on the "compname" property . This property may be assigned any one of the following values, "ALL" - Generate ICF information in the FBA process for all of the FRF components of the assembly +n - (a POSITIVE integer value) Generate ICF information in the FBA process only for those FRF components of the assembly whose IDs are included in SET n -n - (a NEGATIVE integer value) Generate ICF information in the FBA process only for that single FRF component of the assembly whose ID is given by |n| compname - (a string value) Generate ICF information for the FRF component whose name is provided here.
- `getIcfuse() -> str` — Gets a property the defines how Nastran will use ICF information in the FBA process. This property may be assigned any one of the following values, +n - (a POSITIVE integer value) Use ICF information in the FBA process a configuration that consists of only those FRF components whose IDs are specified by SET ID n. -n - (a NEGATIVE integer value) Use ICF information in the FBA process a configuration that consists of only that single FRF component whose ID is given by |n|. compname - (a string value) Use ICF information in the FBA process a configuration that consists of only that single FRF component whose name is given here.
- `getLoadlbl() -> str` — Gets options for defining load lables in the output of FRF and FBA jobs This property may be assigned any one of the following values, "STD" None "ALT" "ALTX".
- `getOp2_unit() -> int` — Gets a positive integer identifying the Nastran Fortran unit number associated with the .op2 file where the FRF matrices and other information are stored This property MUST be provided if the frf_store property is set to "OP2", otherwise it will be silently ignored.
- `getXitout() -> str` — Gets which FRFs will be output This property may be assigned any one of the following values, "UNIT" - Output the FRF results only for those unit excitations that are specified explicitly via FRFXIT / FRFXIT1 Bulk Data entries or implicitly via the DLOAD Case Control request "UNITALL" - Output FRF results not only for unit excitations specified explicitly via FRFXIT / FRFXIT1 Bulk Data entries or implicitly via the DLOAD Case Control command, but also for unit excitations that are internally applied automatically by Nastran at the connection points of the FRF component(s) "USER" - Output the FRF results for the following excitations implied by the DLOAD Case Control request: A separate excitation for each individual DOF that has a nonzero load value specified for it An excitation representing the total load Thus, if a DLOAD Case Control request involves non-zero load values on N DOFs, then this request gives results for (N+1) excitations, with the first N such excitations representing individual and separate loads on the N DOFs and the (N+1)th excitation representing the total load "USERTOITL" - Output the FRF results for the single excitation representing the total load implied the DLOAD Case Control request. This corresponds to the (N+1)th excitation mentioned earlier. The output for this single excitation representing the total load is identified by the coded subcase ID of the form xxxx9999 where xxxx is the user subcase ID corresponding to the DLOAD under consideration. Because of the above coded numbering scheme, when XITOUT = USERTOTL is specified, the program will not allow any user subcase ID to exceed 9999. If it does, the program terminates the job with an appropriate fatal message.
#### `setAsmout(asmout: str) -> None`
Sets options for the frequency based assembly process This property may be assigned any one of the following values, "COMP" None "ALL" "ASSEMBLY" "CONNINFO" n - cname -.

- `asmout` — Set the asmout of this FRF

#### `setCompid(compid: int) -> None`
Sets the id of the component whose FRFs are to be generated This property may be assigned either of the following values, n - a positive integer used to select an existing component wit the same ID None - this field will not be written to the Nastran file for this FRF command.

- `compid` — Set the compid of this FRF

#### `setCompname(compname: str) -> None`
Sets the name of the component whose FRFs are to be generated This property may be assigned either of the following values, a string value used to select an existing component with the same name None - this field will not be written to the Nastran file for this FRF command.

- `compname` — Set the compname of this FRF

#### `setConnpts(connpts: int) -> None`
Sets the ID of an existing Scenario SET that defines the points at which the FRF component specified by the "compid"/"compname" properties are to be connected during a subsequent FRF assembly (FBA) process This property may be assigned either of the following values, n - a positive integer used to select an existing Scenario SET that defines the IDs of the connection grids None - this filed will not be written to the Nastran file for this FRF command.

- `connpts` — Set the connpts of this FRF

#### `setFrf_generation(frf_generation: str) -> None`
Sets property used to control which FRFs are generated This property may be assigned any of the following values, "GEN" - generate FRFs for the specified component None - same as "GEN" with the exception that this field will not be written to the Nastran file for this BCPARA ("GEN" is the Nastran default value for this field) "ASM" - generate FRFs from an assembly of components from the FRFs of the individual components "GENASM"- generate FRFs for the specified component and then compute the FRFs of an assembly of components from the FRFs of the individual components.

- `frf_generation` — Set the frf_generation of this FRF

#### `setFrf_store(frf_store: str) -> None`
Sets an optional property used to define whether the FRF matrices are stored on the Nastran database or on a .op2 file. This property may be assigned any one of the following values, "DB" - the FRF matrices will be stored on the current Nastran database None - same as "DB" with the exception that this field will not be written to the Nastran file for this FRF command (the Nastran default for this field is "DB") "OP2" - the FRF matrices will be stored on an external /op2 file Note: If this property is assigned the value "OP2", the associated "op2_unit" property must also be provided.

- `frf_store` — Set the frf_store of this FRF

#### `setIcf_op2_unit(icf_op2_unit: int) -> None`
Sets a positive integer identifying the Nastran Fortran unit number associated with the .op2 file where the ICF data is stored This property MUST be provided if the icf_store property is set to "ICFOP2", otherwise it will be silently ignored.

- `icf_op2_unit` — Set the icf_op2_unit of this FRF

#### `setIcf_store(icf_store: str) -> None`
Sets an optional property used to define whether the ICF data is stored on the Nastran database or on a .op2 file. This property may be assigned any one of the following values, "ICFDB" - the ICF data will be stored on the current Nastran database None - same as "ICFDB" with the exception that this field will not be written to the Nastran file for this FRF command (the Nastran default for this field is "ICFDB") "ICFOP2" - the ICF data will be stored on an external /op2 file Note: If this property is assigned the value "ICFOP2", the associated "icf_op2_unit" property must also be provided.

- `icf_store` — Set the icf_store of this FRF

#### `setIcfauto(icfauto: str) -> None`
Sets a property the defines how Nastran will GENERATE and USE use ICF information in the FBA process. This property may be assigned any one of the following values, +n - (a POSITIVE integer value) First generate and then use ICF information in the FBA process only for those FRF components whose IDs are specified by SET ID n. -n - (a NEGATIVE integer value) First generate and then use ICF information only for the single FRF component whose ID is given by |n|. compname - (a string value) First generate and then use ICF information for the single FRF component whose name is given by here.

- `icfauto` — Set the icfauto of this FRF

#### `setIcfgen(icfgen: str) -> None`
Sets a property the defines how Nastran will Generate ICF information for the FRF component whose name is defined on the "compname" property . This property may be assigned any one of the following values, "ALL" - Generate ICF information in the FBA process for all of the FRF components of the assembly +n - (a POSITIVE integer value) Generate ICF information in the FBA process only for those FRF components of the assembly whose IDs are included in SET n -n - (a NEGATIVE integer value) Generate ICF information in the FBA process only for that single FRF component of the assembly whose ID is given by |n| compname - (a string value) Generate ICF information for the FRF component whose name is provided here.

- `icfgen` — Set the icfgen of this FRF

#### `setIcfuse(icfuse: str) -> None`
Sets a property the defines how Nastran will use ICF information in the FBA process. This property may be assigned any one of the following values, +n - (a POSITIVE integer value) Use ICF information in the FBA process a configuration that consists of only those FRF components whose IDs are specified by SET ID n. -n - (a NEGATIVE integer value) Use ICF information in the FBA process a configuration that consists of only that single FRF component whose ID is given by |n|. compname - (a string value) Use ICF information in the FBA process a configuration that consists of only that single FRF component whose name is given here.

- `icfuse` — Set the icfuse of this FRF

#### `setLoadlbl(loadlbl: str) -> None`
Sets options for defining load lables in the output of FRF and FBA jobs This property may be assigned any one of the following values, "STD" None "ALT" "ALTX".

- `loadlbl` — Set the loadlbl of this FRF

#### `setOp2_unit(op2_unit: int) -> None`
Sets a positive integer identifying the Nastran Fortran unit number associated with the .op2 file where the FRF matrices and other information are stored This property MUST be provided if the frf_store property is set to "OP2", otherwise it will be silently ignored.

- `op2_unit` — Set the op2_unit of this FRF

#### `setXitout(xitout: str) -> None`
Sets which FRFs will be output This property may be assigned any one of the following values, "UNIT" - Output the FRF results only for those unit excitations that are specified explicitly via FRFXIT / FRFXIT1 Bulk Data entries or implicitly via the DLOAD Case Control request "UNITALL" - Output FRF results not only for unit excitations specified explicitly via FRFXIT / FRFXIT1 Bulk Data entries or implicitly via the DLOAD Case Control command, but also for unit excitations that are internally applied automatically by Nastran at the connection points of the FRF component(s) "USER" - Output the FRF results for the following excitations implied by the DLOAD Case Control request: A separate excitation for each individual DOF that has a nonzero load value specified for it An excitation representing the total load Thus, if a DLOAD Case Control request involves non-zero load values on N DOFs, then this request gives results for (N+1) excitations, with the first N such excitations representing individual and separate loads on the N DOFs and the (N+1)th excitation representing the total load "USERTOITL" - Output the FRF results for the single excitation representing the total load implied the DLOAD Case Control request. This corresponds to the (N+1)th excitation mentioned earlier. The output for this single excitation representing the total load is identified by the coded subcase ID of the form xxxx9999 where xxxx is the user subcase ID corresponding to the DLOAD under consideration. Because of the above coded numbering scheme, when XITOUT = USERTOTL is specified, the program will not allow any user subcase ID to exceed 9999. If it does, the program terminates the job with an appropriate fatal message.

- `xitout` — Set the xitout of this FRF


## `apex.studies.FailureSetting3DOrth`  (extends `FailureSettings`)
Define the failure Settings for the current scenario setting And each failure settings depends on the materials used in the current scenario. if the material type is 3D orthotropic material, then the FailureSetting3DOrth should be used to instantiate an object.
Properties: `axisCompScale`, `axisTenScale`, `inPlaneCompScale`, `inPlaneTenScale`, `shearScale`

Methods:

- `getAxisCompScale() -> float` — Define the axis Compression Scale in Build Direction(%)
- `getAxisTenScale() -> float` — Define the axis tension Scale in Build Direction(%)
- `getInPlaneCompScale() -> float` — Define the inplane Compression Scale in Build Direction(%)
- `getInPlaneTenScale() -> float` — Define the inPlane tension Scale in Build Direction(%)
- `getShearScale() -> float` — Define the shear Scale in Build Direction(%)
- `setAxisCompScale(axisCompScale: float) -> None` — Define the axis Compression Scale in Build Direction(%)
- `setAxisTenScale(axisTenScale: float) -> None` — Define the axis tension Scale in Build Direction(%)
- `setInPlaneCompScale(inPlaneCompScale: float) -> None` — Define the inplane Compression Scale in Build Direction(%)
- `setInPlaneTenScale(inPlaneTenScale: float) -> None` — Define the inPlane tension Scale in Build Direction(%)
- `setShearScale(shearScale: float) -> None` — Define the shear Scale in Build Direction(%)
#### `update(failureCriteria: apex.studies.FailureCriteria, assessMethod: apex.studies.FailureAssessMethod, safetyFactorGlobal: float, stressGoalGlobal: float, safetyFactorEvent: {str:float}, stressGoalEvent: {str:float}, axisTenScale: float, axisCompScale: float, inPlaneTenScale: float, inPlaneCompScale: float, shearScale: float) -> None`
update the Failure Setting for current scenario

- `failureCriteria` — Define a failure Criteria for current scenario
- `assessMethod` — Defined a Failure Assess Method for current scenario. it can be safetyFactor or stressGoal
- `safetyFactorGlobal` — Define a safety factor for global
- `stressGoalGlobal` — Define a stress Goal for global
- `safetyFactorEvent` — Define a safety factor for events
- `stressGoalEvent` — Define a stress Goal for events
- `axisTenScale` — Define the axis tension Scale in Build Direction(%)
- `axisCompScale` — Define the axis compression Scale in Build Direction(%)
- `inPlaneTenScale` — Define the inplane tension Scale in Build Direction(%)
- `inPlaneCompScale` — Define the in plane Compression Scale in Build Direction(%)
- `shearScale` — Define the shear Scale in Build Direction(%)


## `apex.studies.FailureSetting3DTranseIso`  (extends `FailureSettings`)
Define the failure Settings for the current scenario setting And each failure settings depends on the materials used in the current scenario. if the material type is 3D Transverse isotropic material, then the FailureSetting3DTranseIso should be used to instantiate an object.
Properties: `axisCompScale`, `axisTenScale`, `inPlaneCompScale`, `inPlaneTenScale`, `shearScale`

Methods:

- `getAxisCompScale() -> float` — Define the axis Compression Scale in Build Direction(%)
- `getAxisTenScale() -> float` — Define the axis tension Scale in Build Direction(%)
- `getInPlaneCompScale() -> float` — Define the inplane Compression Scale in Build Direction(%)
- `getInPlaneTenScale() -> float` — Define the inPlane tension Scale in Build Direction(%)
- `getShearScale() -> float` — Define the shear Scale in Build Direction(%)
- `setAxisCompScale(axisCompScale: float) -> None` — Define the axis Compression Scale in Build Direction(%)
- `setAxisTenScale(axisTenScale: float) -> None` — Define the axis tension Scale in Build Direction(%)
- `setInPlaneCompScale(inPlaneCompScale: float) -> None` — Define the inplane Compression Scale in Build Direction(%)
- `setInPlaneTenScale(inPlaneTenScale: float) -> None` — Define the inPlane tension Scale in Build Direction(%)
- `setShearScale(shearScale: float) -> None` — Define the shear Scale in Build Direction(%)
#### `update(failureCriteria: apex.studies.FailureCriteria, assessMethod: apex.studies.FailureAssessMethod, safetyFactorGlobal: float, stressGoalGlobal: float, safetyFactorEvent: {str:float}, stressGoalEvent: {str:float}, axisTenScale: float, axisCompScale: float, inPlaneTenScale: float, inPlaneCompScale: float, shearScale: float) -> None`
update the Failure Setting for current scenario

- `failureCriteria` — Define a failure Criteria for current scenario
- `assessMethod` — Defined a Failure Assess Method for current scenario. it can be safetyFactor or stressGoal
- `safetyFactorGlobal` — Define a safety factor for global
- `stressGoalGlobal` — Define a stress Goal for global
- `safetyFactorEvent` — Define a safety factor for events
- `stressGoalEvent` — Define a stress Goal for events
- `axisTenScale` — Define the axis tension Scale in Build Direction(%)
- `axisCompScale` — Define the axis compression Scale in Build Direction(%)
- `inPlaneTenScale` — Define the inplane tension Scale in Build Direction(%)
- `inPlaneCompScale` — Define the in plane Compression Scale in Build Direction(%)
- `shearScale` — Define the shear Scale in Build Direction(%)


## `apex.studies.FailureSettingIso`  (extends `FailureSettings`)
Define the failure Settings for the current scenario setting And each failure settings depends on the materials used in the current scenario. if the material type is isotropic material, then the FailureSettingIso should be used to instantiate an object.
Properties: `tensionScale`

Methods:

- `getTensionScale() -> float` — Define the tension Scale in Build Direction(%)
- `setTensionScale(tensionScale: float) -> None` — Define the tension Scale in Build Direction(%)
#### `update(failureCriteria: apex.studies.FailureCriteria, assessMethod: apex.studies.FailureAssessMethod, safetyFactorGlobal: float, stressGoalGlobal: float, safetyFactorEvent: {str:float}, stressGoalEvent: {str:float}, tensionScale: float) -> None`
used to update the Failure Setting for current scenario

- `failureCriteria` — Define a failure Criteria for current scenario
- `assessMethod` — Defined a Failure Assess Method for current scenario. it can be safetyFactor or stressGoal
- `safetyFactorGlobal` — Define a safety factor for global
- `stressGoalGlobal` — Define a stress Goal for global
- `safetyFactorEvent` — Define a safety factor for events
- `stressGoalEvent` — Define a stress Goal for events
- `tensionScale` — Define the tension Scale in Build Direction(%)


## `apex.studies.FailureSettings`
Define the failure Settings for the current scenario setting And each failure settings depends on the materials used in the current scenario. An example as below: gdSimSetting = simSettings[0].asSimulationSettingsGenerativeDesign() myfailureSetting = gdSimSetting.failureSettings.asFailureSetting3DTranseIso() myfailureSettings.update( failureCri = TsaiWu assessMethod = safetyFactor failureValueGlobal =2.0 failureValueEvent ={Event1 : 1.8, Event2 : 2.6, Event4 : 0.8, Event7 : 2.8, } axisTenScale = 0.3 axisCompScale = 0.3 inPlaneTenScale = 0.3 inPlaneCompScale = 0.3 shearScale =0.3 ) # -------------------------------------------------------------------------------------- # update the failureSettings myfailureSettings.update(failureCri = TsaiWu assessMethod = safetyFactor failureValueGlobal =2.0 ) # -------------------------------------------------------------------------------------- # create the simulationSettings simSetting1 = scenario1.simulationSettings() simSetting1.manufacturing = apex.studies.FDM simSetting1.failureSettings = myfailureSettings simSetting1.buildDirection = apex.construct.createOrientation(alpha=270., beta=90., gamma=0.0) simSetting1.strutDensity = xx simSetting1.shapeQuality = xx simSetting1.complexity = xx simSetting1.keepNonDesignRegions = xx # the attributes must following the below table, If there is a conflict between user-defined member variables, an error message should be displayed.
Properties: `assessMethod`, `failureCriteria`, `safetyFactorEvent`, `safetyFactorGlobal`, `stressGoalEvent`, `stressGoalGlobal`

Methods:

- `getAssessMethod() -> apex.studies.FailureAssessMethod` — Defined a Failure Assess Method for current scenario. it can be safetyFactor or stressGoal.
- `getFailureCriteria() -> apex.studies.FailureCriteria` — Define a failure Criteria for current scenario.
- `getSafetyFactorEvent() -> {str:float}` — Define a safety factor for events.
- `getSafetyFactorGlobal() -> float` — Define a safety factor for global.
- `getStressGoalEvent() -> {str:float}` — Define a stress Goal for events.
- `getStressGoalGlobal() -> float` — Define a stress Goal for global.
- `setAssessMethod(assessMethod: apex.studies.FailureAssessMethod) -> None` — Defined a Failure Assess Method for current scenario. it can be safetyFactor or stressGoal.
- `setFailureCriteria(failureCriteria: apex.studies.FailureCriteria) -> None` — Define a failure Criteria for current scenario.
- `setSafetyFactorEvent(safetyFactorEvent: {str:float}) -> None` — Define a safety factor for events.
- `setSafetyFactorGlobal(safetyFactorGlobal: float) -> None` — Define a safety factor for global.
- `setStressGoalEvent(stressGoalEvent: {str:float}) -> None` — Define a stress Goal for events.
- `setStressGoalGlobal(stressGoalGlobal: float) -> None` — Define a stress Goal for global.

## `apex.studies.FrequencyResponseSimulationSettings`  (extends `SimulationSettings`)
This class manages the simulation settings for Frequency Response Steps. An instance of this class is created and populated with default values whenever a Frequency Response Step is created.
Properties: `freqRangeLower`, `freqRangeUpper`, `maxModes`, `mechanismCheck`, `numBucklingModes`

Methods:

- `getFreqRangeLower() -> float`
- `getFreqRangeUpper() -> float`
- `getMaxModes() -> int`
- `getMechanismCheck() -> bool`
- `getNumBucklingModes() -> int`
- `getStopCalculation() -> bool`
#### `update(enableMechanismCheck: apex.ApexBool, frequencyBoundLower: float, frequencyBoundUpper: float, maxNumModes: int, numBucklingModes: int) -> None`
Update this SimulationSettings.

- `enableMechanismCheck` — Boolean flag to indicate whether the solver should produce diagnostic results if a mechanism is detected during solution. If True (default) and a mechanism is detected during solution, Apex will produce diagnostic results (displacements) that can be viewed in post-processing to help diagnose the mechanism.
- `frequencyBoundLower` — The lower bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies lower than this value will be ignored. If undefined (default), no lower bound will be applied and all modes will be recovered including modes with negative frequencies
- `frequencyBoundUpper` — The upper bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies higher than this value will be ignored. If undefined (default), no upper bound will be applied and all modes will be recovered.
- `maxNumModes` — The maximum number of modes (default = 10) to recover during solution.
- `numBucklingModes` — The number of buckling modes (default = 10) to recover during the simulation.


## `apex.studies.GROUNDCHECK`  (extends `ScenarioCommand`)
Class representing a Nastran "GROUNDCHECK" case control command The GROUNDCHECK command is used to carry out grounding check analysis on the stiffness matrix to identify unintentional constraints by moving the model rigidly.
Properties: `dof_set`, `force_print_threshold`, `grounding_data_recovery`, `print_output`, `punch_output`, `refgrid`, `strain_energy_thresh`, `value`

Methods:

- `getDof_set() -> str` — Gets defines which set of stiffness degrees of freedom will be used for the ground checks This property may be assigned any one of the following values, "ALL" - uses all degree of freedom sets a list of any combination of the following strings, "G" - "N" "N+AUTOSPC" "F" "A" None - same as "G" with the exception that this field will not be written to the Nastran file for this GROUNDCHECK command.
- `getForce_print_threshold() -> float` — Gets defines a threshold for printing of grounding forces This property will be silently ignored unless "grounding_data_recovery" is set to "YES" This property defines a grounding force force threshold as a percentage of the largest calculated grounding force All forces with values greater than this threshold will be written to the printed output (Assuming "grounding_data_recovery" is set to "YES") This property may be assigned either of the following values, r - floating point value between 0 and 1.0 defining the threshold percentage None - has the same effect as setting a value of 0.1 (10%) with the exception that his field will not be written to the Nastran file for this GROUNDCHECK command.
- `getGrounding_data_recovery() -> str` — Gets property used to specify whether grounding forces will be recovered or not This property may be assigned any one of the following values, "NO" - grounding forces will NOT be recovered None - same as "NO" with the exception that this field will not be written to the Nastran file for this GROUNDCHECK command. ("NO" is the Nastran default value for this field) "YES" - grounding forces WILL be recovered.
- `getPrint_output() -> str` — Gets specifies whether ground check data will be written to the print file or not This property may be assigned one of the following values, "PRINT" - writes ground check output to the print file None - same as "PRINT" with the exception that this field will not be written to the Nastran file for this GROUNDCECK command ("PRINT" is the Nastran default value for this field) "NOPRINT" - ground check output will NOT be written to the print file.
- `getPunch_output() -> str` — Gets controls output of ground check data to the punch file This property may be assigned any one of the following values, "PUNCH" - cause ground check output to be written to the punch file None (Default) - ground check data will NOT be written to the punch file.
- `getRefgrid() -> int` — Gets optional ID of a Grid used for the calculation of the rigid body motion The property may be assigned either of the following values, n - positive integer ID identify an existing Grid in the model None - The reference grid will be left undefined and this field will not be exported to the Nastran file. (Nastran will use the global origin as the basis for rigid boy motions calculations)
- `getStrain_energy_thresh() -> float` — Gets defines a maximum threshold strain energy value used to determine if grounding is present. Calculated strain energy values great than this value are considered to be caused by grounding This property may be assigned either of the following values, e - any positive floating point value that defines the maximum strain energy threshold None (Default) - Nastran will use a maximum strain energy threshold value calculated by dividing the largest term on the stiffness matrix diagonal by 1.0E10.
- `getValue() -> str` — Gets optional property specifying whether or not GROUNDCHECKS will be performed. This property may be assigned any one of the following values, "YES" - grounding checks will be performed "NO" - grounding checks will NOT be performed None - same is "NO" with the exception that this field will not be written to the Nastran file ("NO" is the Nastran default value for this field)
#### `setDof_set(dof_set: str) -> None`
Sets defines which set of stiffness degrees of freedom will be used for the ground checks This property may be assigned any one of the following values, "ALL" - uses all degree of freedom sets a list of any combination of the following strings, "G" - "N" "N+AUTOSPC" "F" "A" None - same as "G" with the exception that this field will not be written to the Nastran file for this GROUNDCHECK command.

- `dof_set` — Set the dof_set of this GROUNDCHECK

#### `setForce_print_threshold(force_print_threshold: float) -> None`
Sets defines a threshold for printing of grounding forces This property will be silently ignored unless "grounding_data_recovery" is set to "YES" This property defines a grounding force force threshold as a percentage of the largest calculated grounding force All forces with values greater than this threshold will be written to the printed output (Assuming "grounding_data_recovery" is set to "YES") This property may be assigned either of the following values, r - floating point value between 0 and 1.0 defining the threshold percentage None - has the same effect as setting a value of 0.1 (10%) with the exception that his field will not be written to the Nastran file for this GROUNDCHECK command.

- `force_print_threshold` — Set the force_print_threshold of this GROUNDCHECK

#### `setGrounding_data_recovery(grounding_data_recovery: str) -> None`
Sets property used to specify whether grounding forces will be recovered or not This property may be assigned any one of the following values, "NO" - grounding forces will NOT be recovered None - same as "NO" with the exception that this field will not be written to the Nastran file for this GROUNDCHECK command. ("NO" is the Nastran default value for this field) "YES" - grounding forces WILL be recovered.

- `grounding_data_recovery` — Set the grounding_data_recovery of this GROUNDCHECK

#### `setPrint_output(print_output: str) -> None`
Sets specifies whether ground check data will be written to the print file or not This property may be assigned one of the following values, "PRINT" - writes ground check output to the print file None - same as "PRINT" with the exception that this field will not be written to the Nastran file for this GROUNDCECK command ("PRINT" is the Nastran default value for this field) "NOPRINT" - ground check output will NOT be written to the print file.

- `print_output` — Set the print_output of this GROUNDCHECK

#### `setPunch_output(punch_output: str) -> None`
Sets controls output of ground check data to the punch file This property may be assigned any one of the following values, "PUNCH" - cause ground check output to be written to the punch file None (Default) - ground check data will NOT be written to the punch file.

- `punch_output` — Set the punch_output of this GROUNDCHECK

#### `setRefgrid(refgrid: int) -> None`
Sets optional ID of a Grid used for the calculation of the rigid body motion The property may be assigned either of the following values, n - positive integer ID identify an existing Grid in the model None - The reference grid will be left undefined and this field will not be exported to the Nastran file. (Nastran will use the global origin as the basis for rigid boy motions calculations)

- `refgrid` — Set the refgrid of this GROUNDCHECK

#### `setStrain_energy_thresh(strain_energy_thresh: float) -> None`
Sets defines a maximum threshold strain energy value used to determine if grounding is present. Calculated strain energy values great than this value are considered to be caused by grounding This property may be assigned either of the following values, e - any positive floating point value that defines the maximum strain energy threshold None (Default) - Nastran will use a maximum strain energy threshold value calculated by dividing the largest term on the stiffness matrix diagonal by 1.0E10.

- `strain_energy_thresh` — Set the strain_energy_thresh of this GROUNDCHECK

#### `setValue(value: str) -> None`
Sets optional property specifying whether or not GROUNDCHECKS will be performed. This property may be assigned any one of the following values, "YES" - grounding checks will be performed "NO" - grounding checks will NOT be performed None - same is "NO" with the exception that this field will not be written to the Nastran file ("NO" is the Nastran default value for this field)

- `value` — Set the value of this GROUNDCHECK


## `apex.studies.GenerativeDesignStaticStep`  (extends `Step`)
GenerativeDesignStaticStep GenerativeDesignStaticStep.

## `apex.studies.IC`  (extends `ScenarioCommand`)
Class representing a Nastran "IC" case control command The IC command is used to select initial conditions for transient analysis.
Properties: `diffk`, `ic_type`, `value`

Methods:

- `getDiffk() -> str` — Gets defines whether or not differential stiffness effects will be included in the solution. This property is silently ignored unless "ic_type" is set to "STATSUB" This property may be assigned either of the following values, "DIFFK" - Nastran will include the effects of differential stiffness in the solutions None - differential stiffness effects will NOT be included in the solution This property is silently ignored unless "ic_type" is set to "STATSUB".
- `getIc_type() -> str` — Gets property used to specify the type of initial condition that is being selected. This property may be assigned any one of the following values, "PHYSICAL" - The initial conditions selected by this IC command define initial conditions on physical degrees of freedom (grid, scalar or extra points) None - same as "PHYSICAL" with the exception that this field will not be written to the Nastran file for this IC command ("PHYSICAL" is the Nastran default value for this field "MODAL") - the initial conditions selected by this IC command define initial conditions for modal coordinates and extra points "STATSUB" - the "value" property of this IC selects a static Subcase (instead of a TIC entry) and that Subcase is used to define the initial condition values. If this option is used, the optional "diffk" property may also defined.
- `getValue() -> int` — Gets positive integer property used to specify the ID of either a transient initial condition entry (TIC) or the ID of a static subcase as the source of the initial conditions. If "ic_type" is set to "PHYSICAL", None or "MODAL" the value of this property is used to select an existing "TIC" load which defines the initial transient conditions If "ic_type" is set to "STATSUB", the value of this property is used to select an existing static Subcase with the same ID as the source of the transient initial conditions.
#### `setDiffk(diffk: str) -> None`
Sets defines whether or not differential stiffness effects will be included in the solution. This property is silently ignored unless "ic_type" is set to "STATSUB" This property may be assigned either of the following values, "DIFFK" - Nastran will include the effects of differential stiffness in the solutions None - differential stiffness effects will NOT be included in the solution This property is silently ignored unless "ic_type" is set to "STATSUB".

- `diffk` — Set the diffk of this IC

#### `setIc_type(ic_type: str) -> None`
Sets property used to specify the type of initial condition that is being selected. This property may be assigned any one of the following values, "PHYSICAL" - The initial conditions selected by this IC command define initial conditions on physical degrees of freedom (grid, scalar or extra points) None - same as "PHYSICAL" with the exception that this field will not be written to the Nastran file for this IC command ("PHYSICAL" is the Nastran default value for this field "MODAL") - the initial conditions selected by this IC command define initial conditions for modal coordinates and extra points "STATSUB" - the "value" property of this IC selects a static Subcase (instead of a TIC entry) and that Subcase is used to define the initial condition values. If this option is used, the optional "diffk" property may also defined.

- `ic_type` — Set the ic_type of this IC

#### `setValue(value: int) -> None`
Sets positive integer property used to specify the ID of either a transient initial condition entry (TIC) or the ID of a static subcase as the source of the initial conditions. If "ic_type" is set to "PHYSICAL", None or "MODAL" the value of this property is used to select an existing "TIC" load which defines the initial transient conditions If "ic_type" is set to "STATSUB", the value of this property is used to select an existing static Subcase with the same ID as the source of the transient initial conditions.

- `value` — Set the value of this IC


## `apex.studies.IRLOAD`  (extends `ScenarioCommand`)
Class used to represent a Nastran "IRLOAD" case control command. The IRLOAD command is used to specify nonlinear inertia relief in Solution 400.
Properties: `value`

Methods:

- `getValue() -> str` — Gets property used to specify how Nastran will apply nonlinear inertial relief in Solution 400 This property may be assigned any of the following values, "QLINEAR" - inertia loads will be calculated using small (quasi-linear)displacements "NONE" - inertia relief will not be applied None - same as "NONE" wit the exception that this field will not be written to the Nastran file for this IRLOAD command ("NONE" is the Nastran default for this field)
#### `setValue(value: str) -> None`
Sets property used to specify how Nastran will apply nonlinear inertial relief in Solution 400 This property may be assigned any of the following values, "QLINEAR" - inertia loads will be calculated using small (quasi-linear)displacements "NONE" - inertia relief will not be applied None - same as "NONE" wit the exception that this field will not be written to the Nastran file for this IRLOAD command ("NONE" is the Nastran default for this field)

- `value` — Set the value of this IRLOAD


## `apex.studies.IncrementalSchemeAdaptive`
A class to define the properties of Incremental Scheme = Adaptive.
Properties: `artificialDamping`, `dampingRatio`, `incrementGrowthFactor`, `initialLoadIncrement`, `maximumLoadIncrement`, `maxIncrements`, `minimumLoadIncrement`, `outputIncrements`, `stepLength`, `stepOutput`

Methods:

#### `IncrementalSchemeAdaptive(stepLength: float, initialLoadIncrement: float, minimumLoadIncrement: float, maximumLoadIncrement: float, incrementGrowthFactor: float, maxIncrements: int, artificialDamping: apex.studies.ArtificialDamping, dampingRatio: float, stepOutput: apex.studies.StepOutput, outputIncrements: int) -> None`
Constructor for "IncrementalSchemeAdaptive".

- `stepLength` — Step length to be used in the analysis.
- `initialLoadIncrement` — Optional-Initial time step defined as fraction of total load step time
- `minimumLoadIncrement` — Minimum time step defined as fraction of total load step time
- `maximumLoadIncrement` — Maximum time step defined as fraction of total load step time
- `incrementGrowthFactor` — Factor for increasing time steps due to number of iterations
- `maxIncrements` — Maximum number of increments in the current load case
- `artificialDamping` — Artificial damping for static analysis
- `dampingRatio` — The damping ration to use if artificial damping is set to Always, Damping energy or Minimum
- `stepOutput` — Optional-Step output setting
- `outputIncrements` — The number of equal length increments for which output will be generated

- `getArtificialDamping() -> apex.studies.ArtificialDamping` — Artificial damping for static analysis.
- `getDampingRatio() -> float` — The damping ration to use if artificial damping is set to Always, Damping energy or Minimum.
- `getIncrementGrowthFactor() -> float` — Factor for increasing time steps due to number of iterations.
- `getInitialLoadIncrement() -> float` — Initial time step defined as fraction of total load step time.
- `getMaxIncrements() -> int` — Maximum number of increments in the current load case.
- `getMaximumLoadIncrement() -> float` — Maximum time step defined as fraction of total load step time.
- `getMinimumLoadIncrement() -> float` — Minimum time step defined as fraction of total load step time.
- `getOutputIncrements() -> int` — The number of equal length increments for which output will be generated.
- `getStepLength() -> float` — Step length is used to define the period over which the increment of the load applies. The Step length is frequently referred to as "Time" however since the Step type is Static this is incorrect.
- `getStepOutput() -> apex.studies.StepOutput` — Optional-Step output setting.
#### `update(stepLength: float, initialLoadIncrement: float, minimumLoadIncrement: float, maximumLoadIncrement: float, incrementGrowthFactor: float, maxIncrements: int, artificialDamping: apex.studies.ArtificialDamping, dampingRatio: float, stepOutput: apex.studies.StepOutput, outputIncrements: int) -> None`
Update properties of "IncrementalSchemeAdaptive".

- `stepLength` — Step length to be used in the analysis.
- `initialLoadIncrement` — Optional-Initial time step defined as fraction of total load step time
- `minimumLoadIncrement` — Minimum time step defined as fraction of total load step time
- `maximumLoadIncrement` — Maximum time step defined as fraction of total load step time
- `incrementGrowthFactor` — Factor for increasing time steps due to number of iterations
- `maxIncrements` — Maximum number of increments in the current load case
- `artificialDamping` — Artificial damping for static analysis
- `dampingRatio` — The damping ration to use if artificial damping is set to Always, Damping energy or Minimum
- `stepOutput` — Optional-Step output setting
- `outputIncrements` — The number of equal length increments for which output will be generated


## `apex.studies.IncrementalSchemeArcLength`
A class to define the properties of Incremental Scheme = ArcLength.
Properties: `arcLengthMethod`, `initialLoadFraction`, `maximumAdjustmentRatio`, `maxIncrements`, `minimumAdjustmentRatio`, `stepLength`

Methods:

#### `IncrementalSchemeArcLength(stepLength: float, arcLengthMethod: apex.studies.ArcLengthMethod, initialLoadFraction: float, minimumAdjustmentRatio: float, maximumAdjustmentRatio: float, maxIncrements: int) -> None`
Constructor for "IncrementalSchemeArcLength".

- `stepLength` — Step length to be used in the analysis.
- `arcLengthMethod` — Arc length method
- `initialLoadFraction` — Initial time step defined as a fraction of the load step time for the arc-length procedure.
- `minimumAdjustmentRatio` — Minimum allowable arc-length adjustment ratio.
- `maximumAdjustmentRatio` — Maximum time step defined as fraction of total load step time
- `maxIncrements` — Maximum number of increments in the current load case

- `getArcLengthMethod() -> apex.studies.ArcLengthMethod` — Arc length method.
- `getInitialLoadFraction() -> float` — Initial time step defined as a fraction of the load step time for the arc-length procedure.
- `getMaxIncrements() -> int` — Maximum number of increments in the current load case.
- `getMaximumAdjustmentRatio() -> float` — Maximum time step defined as fraction of total load step time.
- `getMinimumAdjustmentRatio() -> float` — Minimum allowable arc-length adjustment ratio.
- `getStepLength() -> float` — Step length is used to define the period over which the increment of the load applies. The Step length is frequently referred to as "Time" however since the Step type is Static this is incorrect.
#### `update(stepLength: float, arcLengthMethod: apex.studies.ArcLengthMethod, initialLoadFraction: float, minimumAdjustmentRatio: float, maximumAdjustmentRatio: float, maxIncrements: int) -> None`
Update properties of "IncrementalSchemeArcLength".

- `stepLength` — Step length to be used in the analysis.
- `arcLengthMethod` — Arc length method
- `initialLoadFraction` — Initial time step defined as a fraction of the load step time for the arc-length procedure.
- `minimumAdjustmentRatio` — Minimum allowable arc-length adjustment ratio.
- `maximumAdjustmentRatio` — Maximum time step defined as fraction of total load step time
- `maxIncrements` — Maximum number of increments in the current load case


## `apex.studies.IncrementalSchemeFixed`
A class to define the properties of Incremental Scheme = Fixed.
Properties: `increments`, `outputInterval`, `stepLength`

Methods:

#### `IncrementalSchemeFixed(stepLength: float, increments: int, outputInterval: int) -> None`
"IncrementalSchemeFixed" constructor

- `stepLength` — Step length is used to define the period over which the increment of the load applies. The Step length is frequently referred to as "Time" however since the Step type is Static this is incorrect.
- `increments` — Number of increments for fixed time stepping
- `outputInterval` — Interval for output.

- `getIncrements() -> int` — Number of increments for fixed time stepping.
- `getOutputInterval() -> float` — Interval for output.
- `getStepLength() -> float` — Step length is used to define the period over which the increment of the load applies. The Step length is frequently referred to as "Time" however since the Step type is Static this is incorrect.
#### `update(stepLength: float, increments: int, outputInterval: int) -> None`
Update properties of "IncrementalSchemeFixed".

- `stepLength` — Step length is used to define the period over which the increment of the load applies. The Step length is frequently referred to as "Time" however since the Step type is Static this is incorrect.
- `increments` — Number of increments for fixed time stepping
- `outputInterval` — Interval for output.


## `apex.studies.InteractionControl`
Interaction control setting for a simulation setting.
Properties: `biasFactor`, `contactMethod`, `contactTolerance`, `enablePermanentGlue`, `frictionType`, `ignoreShellThickness`, `linearContact`, `linearContactLargeDisplacement`, `maximumSeparations`, `maxSlidingDistance`, `nonSymmetricFrictionMatrix`, `normalAugmentationMethod`, `normalPenaltyFactor`, `normalScaleFactor`, `normalVectorAngle`, `notAllowedSeparateNewlyContactedNode`, `penetrationDistance`, `separationForce`, `separationIn`, `separationMethod`, `separationStress`, `slipDistance`, `tangentAugmentationMethod`, `tangentPenaltyFactor`, `tangentScaleFactor`

Methods:

#### `InteractionControl(contactMethod: apex.studies.ContactMethod = apex.studies.ContactMethod.NodeToSegment, normalAugmentationMethod: apex.studies.AugmentationMethod = apex.studies.AugmentationMethod.NotUse, penetrationDistance: float, normalPenaltyFactor: float, normalScaleFactor: float = 1.0, normalVectorAngle: float, tangentAugmentationMethod: apex.studies.AugmentationMethod = apex.studies.AugmentationMethod.NotUse, tangentPenaltyFactor: float, tangentScaleFactor: float = 1.0, slipDistance: float, frictionType: apex.studies.FrictionType = apex.studies.FrictionType.Frictionless, nonSymmetricFrictionMatrix: apex.ApexBool = True, maxSlidingDistance: float, linearContact: apex.ApexBool = False, linearContactLargeDisplacement: apex.ApexBool = False, enablePermanentGlue: apex.ApexBool = False, contactTolerance: float, biasFactor: float, ignoreShellThickness: apex.ApexBool = False, separationMethod: apex.studies.SeparationMethod = apex.studies.SeparationMethod.Force, separationForce: float, separationStress: float, separationIn: apex.studies.SeparationIn = apex.studies.SeparationIn.Current, notAllowedSeparateNewlyContactedNode: apex.ApexBool = False, maximumSeparations: float) -> None`
InteractionControl constructor.

- `contactMethod` — Contact method for the interaction control in a scenario.
- `normalAugmentationMethod` — Optional - Augmentation method in normal direction. It is only available for segment to segment method, omits in node to segment method.
- `penetrationDistance` — Optional - Penetration distance beyond which an augmentation will be applied The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `normalPenaltyFactor` — Optional - Augmented Lagrange penalty factor in normal direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `normalScaleFactor` — Scale factor of augmented Lagrange penalty factor along contact normal direction
- `normalVectorAngle` — Optional - Minimum angle between segment normal vectors allowing the segments to come into contact
- `tangentAugmentationMethod` — Optional - Augmentation method in tangent direction. It is only available for segment to segment method, omits in node to segment method.
- `tangentPenaltyFactor` — Optional - Augmented Lagrange penalty factor in tangent direction The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `tangentScaleFactor` — Scale factor of augmented Lagrange penalty factor along contact tangent direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `slipDistance` — Optional - Maximum allowable slip distance for sticking, beyond it there is no sticking, only sliding exists
- `frictionType` — Optional - Friction type of contact pair.
- `nonSymmetricFrictionMatrix` — Optional- Specify symmetric or non-symmetric friction matrix. If it is false,use symmetric friction matrix. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `maxSlidingDistance` — Optional - Maximum allowed sliding distance, beyond it the contact segments are redefined The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `linearContact` — Optional - if enable, the contact force is distributed based upon undeformed geometry.
- `linearContactLargeDisplacement` — Optional - Force Linear Contact with Large Displacement of it is true
- `enablePermanentGlue` — Optional - Force all glues with Permanent Glue without separation if it is true. It is only available for interaction type is Glue, which will be skipped in contact.
- `contactTolerance` — An optional distance tolerance value (default =0.005m) used to determine the subset of elements specified in targetSide1 and targetSide2 that will actually be glued/contact during the simulations.
- `biasFactor` — Optional - Contact tolerance bias factor
- `ignoreShellThickness` — Optional-Ignore shell thickness from the tolerance during detection if it is true.
- `separationMethod` — Optional - Separation based on stresses or forces.
- `separationForce` — Optional - max force of separation, which is only available when separation method define in scenario is based on "Force". Otherwise,it will be skipped.
- `separationStress` — Optional - max stress of separation, which is only available when separation method define in scenario is based on "Stress". Otherwise,it will be skipped.
- `separationIn` — Optional - control separation in which increment
- `notAllowedSeparateNewlyContactedNode` — Optional - A node which comes into contact may not separate again in the same increment if it is on
- `maximumSeparations` — Optional - Maximum number of separations allowed in each increment

- `getBiasFactor() -> float` — Gets Optional - Contact tolerance bias factor.
- `getContactMethod() -> apex.studies.ContactMethod` — Gets Contact method for the interaction control in a scenario.
- `getContactTolerance() -> float` — Gets An optional distance tolerance value (default =0.005m) used to determine the subset of elements specified in targetSide1 and targetSide2 that will actually be glued/contact during the simulations.
- `getEnablePermanentGlue() -> apex.ApexBool` — Gets Optional - Force all glues with Permanent Glue without separation if it is true. It is only available for interaction type is Glue, which will be skipped in contact.
- `getFrictionType() -> apex.studies.FrictionType` — Gets Optional - Friction type of contact pair.
- `getIgnoreShellThickness() -> apex.ApexBool` — Gets Optional-Ignore shell thickness from the tolerance during detection if it is true.
- `getLinearContact() -> apex.ApexBool` — Gets Optional - if enable, the contact force is distributed based upon undeformed geometry.
- `getLinearContactLargeDisplacement() -> apex.ApexBool` — Gets Optional - Force Linear Contact with Large Displacement of it is true.
- `getMaxSlidingDistance() -> float` — Gets Optional - Maximum allowed sliding distance, beyond it the contact segments are redefined The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getMaximumSeparations() -> float` — Gets Optional - Maximum number of separations allowed in each increment.
- `getNonSymmetricFrictionMatrix() -> apex.ApexBool` — Gets Optional- Specify symmetric or non-symmetric friction matrix. If it is false,use symmetric friction matrix. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getNormalAugmentationMethod() -> apex.studies.AugmentationMethod` — Gets Optional - Augmentation method in normal direction. It is only available for segment to segment method, omits in node to segment method.
- `getNormalPenaltyFactor() -> float` — Gets Optional - Augmented Lagrange penalty factor in normal direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getNormalScaleFactor() -> float` — Gets Scale factor of augmented Lagrange penalty factor along contact normal direction.
- `getNormalVectorAngle() -> float` — Gets Optional - Minimum angle between segment normal vectors allowing the segments to come into contact.
- `getNotAllowedSeparateNewlyContactedNode() -> apex.ApexBool` — Gets Optional - A node which comes into contact may not separate again in the same increment if it is on.
- `getPenetrationDistance() -> float` — Gets Optional - Penetration distance beyond which an augmentation will be applied The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getSeparationForce() -> float` — Gets Optional - max force of separation, which is only available when separation method define in scenario is based on "Force". Otherwise,it will be skipped.
- `getSeparationIn() -> apex.studies.SeparationIn` — Gets Optional - control separation in which increment.
- `getSeparationMethod() -> apex.studies.SeparationMethod` — Gets Optional - Separation based on stresses or forces.
- `getSeparationStress() -> float` — Gets Optional - max stress of separation, which is only available when separation method define in scenario is based on "Stress". Otherwise,it will be skipped.
- `getSlipDistance() -> float` — Gets Optional - Maximum allowable slip distance for sticking, beyond it there is no sticking, only sliding exists.
- `getTangentAugmentationMethod() -> apex.studies.AugmentationMethod` — Gets Optional - Augmentation method in tangent direction. It is only available for segment to segment method, omits in node to segment method.
- `getTangentPenaltyFactor() -> float` — Gets Optional - Augmented Lagrange penalty factor in tangent direction The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getTangentScaleFactor() -> float` — Gets Scale factor of augmented Lagrange penalty factor along contact tangent direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
#### `update(contactMethod: apex.studies.ContactMethod, normalAugmentationMethod: apex.studies.AugmentationMethod, penetrationDistance: float, normalPenaltyFactor: float, normalScaleFactor: float, normalVectorAngle: float, tangentAugmentationMethod: apex.studies.AugmentationMethod, tangentPenaltyFactor: float, tangentScaleFactor: float, slipDistance: float, frictionType: apex.studies.FrictionType, nonSymmetricFrictionMatrix: apex.ApexBool, maxSlidingDistance: float, linearContact: apex.ApexBool, linearContactLargeDisplacement: apex.ApexBool, enablePermanentGlue: apex.ApexBool, contactTolerance: float, biasFactor: float, ignoreShellThickness: apex.ApexBool, separationMethod: apex.studies.SeparationMethod, separationForce: float, separationStress: float, separationIn: apex.studies.SeparationIn, notAllowedSeparateNewlyContactedNode: apex.ApexBool, maximumSeparations: float) -> None`
update InteractionControl

- `contactMethod` — Contact method for the interaction control in a scenario.
- `normalAugmentationMethod` — Optional - Augmentation method in normal direction. It is only available for segment to segment method, omits in node to segment method.
- `penetrationDistance` — Optional - Penetration distance beyond which an augmentation will be applied The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `normalPenaltyFactor` — Optional - Augmented Lagrange penalty factor in normal direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `normalScaleFactor` — Scale factor of augmented Lagrange penalty factor along contact normal direction
- `normalVectorAngle` — Optional - Minimum angle between segment normal vectors allowing the segments to come into contact
- `tangentAugmentationMethod` — Optional - Augmentation method in tangent direction. It is only available for segment to segment method, omits in node to segment method.
- `tangentPenaltyFactor` — Optional - Augmented Lagrange penalty factor in tangent direction The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `tangentScaleFactor` — Scale factor of augmented Lagrange penalty factor along contact tangent direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `slipDistance` — Optional - Maximum allowable slip distance for sticking, beyond it there is no sticking, only sliding exists
- `frictionType` — Optional - Friction type of contact pair.
- `nonSymmetricFrictionMatrix` — Optional- Specify symmetric or non-symmetric friction matrix. If it is false,use symmetric friction matrix. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `maxSlidingDistance` — Optional - Maximum allowed sliding distance, beyond it the contact segments are redefined The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `linearContact` — Optional - if enable, the contact force is distributed based upon undeformed geometry.
- `linearContactLargeDisplacement` — Optional - Force Linear Contact with Large Displacement of it is true
- `enablePermanentGlue` — Optional - Force all glues with Permanent Glue without separation if it is true. It is only available for interaction type is Glue, which will be skipped in contact.
- `contactTolerance` — An optional distance tolerance value (default =0.005m) used to determine the subset of elements specified in targetSide1 and targetSide2 that will actually be glued/contact during the simulations.
- `biasFactor` — Optional - Contact tolerance bias factor
- `ignoreShellThickness` — Optional-Ignore shell thickness from the tolerance during detection if it is true.
- `separationMethod` — Optional - Separation based on stresses or forces.
- `separationForce` — Optional - max force of separation, which is only available when separation method define in scenario is based on "Force". Otherwise,it will be skipped.
- `separationStress` — Optional - max stress of separation, which is only available when separation method define in scenario is based on "Stress". Otherwise,it will be skipped.
- `separationIn` — Optional - control separation in which increment
- `notAllowedSeparateNewlyContactedNode` — Optional - A node which comes into contact may not separate again in the same increment if it is on
- `maximumSeparations` — Optional - Maximum number of separations allowed in each increment


## `apex.studies.IterationAndConvergence`
Class to use for linear contact setting for static scenario.
Properties: `autoAdjustConvergenceCriteria`, `displacementCriteria`, `displacementTolerance`, `effectiveStressFraction`, `includeDisplacementLoadVectorLength`, `includeMaximumDisplacementLoadComponent`, `includeMoments`, `includeRotations`, `iterationProcedure`, `lineSearchTolerance`, `maxCorrectionVectors`, `maxIterationsPerIncrement`, `maxLineSearchesPerIteration`, `minIterationsPerIncrement`, `numberOfCutbacks`, `numberOfIterationsBeforeStiffnessUpdate`, `residualLoadCriteria`, `residualLoadTolerance`, `workCriteria`, `workTolerance`

Methods:

#### `IterationAndConvergence(displacementCriteria: bool, displacementTolerance: float, includeRotations: bool, residualLoadCriteria: bool, residualLoadTolerance: float, includeMoments: bool, workCriteria: bool, workTolerance: float, includeMaximumDisplacementLoadComponent: bool, includeDisplacementLoadVectorLength: bool, autoAdjustConvergenceCriteria: bool, effectiveStressFraction: float, iterationProcedure: apex.studies.IterationProcedure, numberOfIterationsBeforeStiffnessUpdate: int, maxCorrectionVectors: int, maxLineSearchesPerIteration: int, lineSearchTolerance: float, maxIterationsPerIncrement: int, minIterationsPerIncrement: int, numberOfCutbacks: int) -> None`
Constructor of "IterationAndConvergence".

- `displacementCriteria` — Optional- Boolean to control Displacement convergence criteria.
- `displacementTolerance` — Optional- tolerance for displacement criterion. It is only available when displacementCriteria = True.
- `includeRotations` — Optional- Boolean to control include rotations as well as translations in the displacement convergence checks. It is only available when displacementCriteria = True.
- `residualLoadCriteria` — Optional- Boolean to control residual Load criteria.
- `residualLoadTolerance` — Optional- tolerance for residual load criterion. It is only available when residualLoadCriteria = True.
- `includeMoments` — Optional- Boolean to control Include moments as well as forces in the load convergence checks. It is only available when residualLoadCriteria = True.
- `workCriteria` — Optional- Boolean to control Work criteria.
- `workTolerance` — Optional- tolerance for work criterion. It is only available when workCriteria = True.
- `includeMaximumDisplacementLoadComponent` — Optional- Boolean to extend convergence checks to include the maximum component of displacement/load. It is only available when displacementCriteria or residualLoadCriteria = True.
- `includeDisplacementLoadVectorLength` — Optional- Boolean to extend convergence checks to include the length of the displacement/load vector. It is only available when displacementCriteria or residualLoadCriteria = True.
- `autoAdjustConvergenceCriteria` — Optional- Boolean to control automatically adjust convergence criteria if need
- `effectiveStressFraction` — Optional-Fraction of effective stress used to limit the sub increment size in material routines
- `iterationProcedure` — Optional-Iteration strategies to be used
- `numberOfIterationsBeforeStiffnessUpdate` — Optional-Defines the frequency ( in terms of the number of iterations between updates) with which the stiffness is updated. It is only available when IterationProcedure = ControlledIterations
- `maxCorrectionVectors` — Optional - Maximum number of quasi-Newton correction vectors to be saved on the database. It is only available when IterationProcedure = ControlledIterations
- `maxLineSearchesPerIteration` — Optional - Maximum number of line searches allowed for each iteration. It is only available when IterationProcedure = ControlledIterations
- `lineSearchTolerance` — Optional - Line Search tolerance. It is only available when IterationProcedure = ControlledIterations
- `maxIterationsPerIncrement` — Optional- Maximum number of iterations allowed for each increment.
- `minIterationsPerIncrement` — Optional- Minimum number of iterations needed for each increment.
- `numberOfCutbacks` — Optional- Limits the number of times a load increment will be cut-back within a Step

- `getAutoAdjustConvergenceCriteria() -> bool` — Boolean to control automatically adjust convergence criteria if need.
- `getDisplacementCriteria() -> bool` — Boolean to control Displacement convergence criteria.
- `getDisplacementTolerance() -> float` — tolerance for displacement criterion. It is only available when displacementCriteria = True.
- `getEffectiveStressFraction() -> float` — Fraction of effective stress used to limit the sub increment size in material routines.
- `getIncludeDisplacementLoadVectorLength() -> bool` — oolean to extend convergence checks to include the length of the displacement/load vector. It is only available when displacementCriteria or residualLoadCriteria = True.
- `getIncludeMaximumDisplacementLoadComponent() -> bool` — Boolean to extend convergence checks to include the maximum component of displacement/load. It is only available when displacementCriteria or residualLoadCriteria = True.
- `getIncludeMoments() -> bool` — Boolean to control Include moments as well as forces in the load convergence checks. It is only available when residualLoadCriteria = True.
- `getIncludeRotations() -> bool` — Boolean to control include rotations as well as translations in the displacement convergence checks . It is only available when displacementCriteria = True.
- `getIterationProcedure() -> apex.studies.IterationProcedure` — Iteration strategies to be used.
- `getLineSearchTolerance() -> float` — Line Search tolerance. It is only available when IterationProcedure = ControlledIterations.
- `getMaxCorrectionVectors() -> int` — Maximum number of quasi-Newton correction vectors to be saved on the database. It is only available when IterationProcedure = ControlledIterations.
- `getMaxIterationsPerIncrement() -> int` — Maximum number of iterations allowed for each increment.
- `getMaxLineSearchesPerIteration() -> int` — Maximum number of line searches allowed for each iteration. It is only available when IterationProcedure = ControlledIterations.
- `getMinIterationsPerIncrement() -> int` — Minimum number of iterations needed for each increment.
- `getNumberOfCutbacks() -> int` — Limits the number of times a load increment will be cut-back within a Step.
- `getNumberOfIterationsBeforeStiffnessUpdate() -> int` — Defines the frequency ( in terms of the number of iterations between updates) with which the stiffness is updated. It is only available when IterationProcedure = ControlledIterations.
- `getResidualLoadCriteria() -> bool` — Boolean to control residual Load criteria.
- `getResidualLoadTolerance() -> float` — tolerance for residual load criterion. It is only available when residualLoadCriteria = True.
- `getWorkCriteria() -> bool` — Boolean to control Work criteria.
- `getWorkTolerance() -> float` — tolerance for work criterion. It is only available when workCriteria = True.
#### `update(displacementCriteria: apex.ApexBool, displacementTolerance: float, includeRotations: apex.ApexBool, residualLoadCriteria: apex.ApexBool, residualLoadTolerance: float, includeMoments: apex.ApexBool, workCriteria: apex.ApexBool, workTolerance: float, includeMaximumDisplacementLoadComponent: apex.ApexBool, includeDisplacementLoadVectorLength: apex.ApexBool, autoAdjustConvergenceCriteria: apex.ApexBool, effectiveStressFraction: float, iterationProcedure: apex.studies.IterationProcedure, numberOfIterationsBeforeStiffnessUpdate: int, maxCorrectionVectors: int, maxLineSearchesPerIteration: int, lineSearchTolerance: float, maxIterationsPerIncrement: int, minIterationsPerIncrement: int, numberOfCutbacks: int) -> None`
Update properties of "IterationAndConvergence".

- `displacementCriteria` — Optional- Boolean to control Displacement convergence criteria.
- `displacementTolerance` — Optional- tolerance for displacement criterion. It is only available when displacementCriteria = True.
- `includeRotations` — Optional- Boolean to control include rotations as well as translations in the displacement convergence checks. It is only available when displacementCriteria = True.
- `residualLoadCriteria` — Optional- Boolean to control residual Load criteria.
- `residualLoadTolerance` — Optional- tolerance for residual load criterion. It is only available when residualLoadCriteria = True.
- `includeMoments` — Optional- Boolean to control Include moments as well as forces in the load convergence checks. It is only available when residualLoadCriteria = True.
- `workCriteria` — Optional- Boolean to control Work criteria.
- `workTolerance` — Optional- tolerance for work criterion. It is only available when workCriteria = True.
- `includeMaximumDisplacementLoadComponent` — Optional- Boolean to extend convergence checks to include the maximum component of displacement/load. It is only available when displacementCriteria or residualLoadCriteria = True.
- `includeDisplacementLoadVectorLength` — Optional- Boolean to extend convergence checks to include the length of the displacement/load vector. It is only available when displacementCriteria or residualLoadCriteria = True.
- `autoAdjustConvergenceCriteria` — Optional- Boolean to control automatically adjust convergence criteria if need
- `effectiveStressFraction` — Optional-Fraction of effective stress used to limit the sub increment size in material routines
- `iterationProcedure` — Optional-Iteration strategies to be used
- `numberOfIterationsBeforeStiffnessUpdate` — Optional-Defines the frequency ( in terms of the number of iterations between updates) with which the stiffness is updated. It is only available when IterationProcedure = ControlledIterations
- `maxCorrectionVectors` — Optional - Maximum number of quasi-Newton correction vectors to be saved on the database. It is only available when IterationProcedure = ControlledIterations
- `maxLineSearchesPerIteration` — Optional - Maximum number of line searches allowed for each iteration. It is only available when IterationProcedure = ControlledIterations
- `lineSearchTolerance` — Optional - Line Search tolerance. It is only available when IterationProcedure = ControlledIterations
- `maxIterationsPerIncrement` — Optional- Maximum number of iterations allowed for each increment.
- `minIterationsPerIncrement` — Optional- Minimum number of iterations needed for each increment.
- `numberOfCutbacks` — Optional- Limits the number of times a load increment will be cut-back within a Step


## `apex.studies.KeyResult`  (extends `Entity`, `IName`)
Key result of a target entity.
Properties: `event`, `independentValue`, `resultDataSetIndex`, `resultDerivation`, `resultQuantity`, `target`

Methods:

- `getEvent() -> apex.studies.Event` — Return the Event of this KeyResult.
- `getIndependentValue() -> float` — An optional value used when the Event from which the key result is being extracted from is not atomic. For example when the Event represents a transient, frequency or incremental load/response. IndependentValue is ignored if the Event does not represent a variable quantity.
- `getResultDataSetIndex() -> int` — Return the ResultDataSetIndex of this KeyResult.
- `getResultDerivation() -> apex.post.ResultDerivation` — An enumeration of supported ResultDerivations in Apex. In createKeyReult method,this argument currently only accept apex.post.ResultDerivation.Magnitude, apex.post.ResultDerivation.Component1, apex.post.ResultDerivation.Component2 and apex.post.ResultDerivation.Component3,.
- `getResultQuantity() -> apex.post.ResultQuantity` — An enumeration of all supported ResultQuantities in Apex. In createKeyReult method, this argument currently only accept apex.post.ResultQuantity.ForceInterface and apex.post.ResultQuantity.MomentInterface, as Apex only supports load mapping of Force and Moment for now.
- `getTarget() -> apex.EntityCollection` — Return the Target of this KeyResult.
- `setDescription(description: str) -> None` — set description of this KeyResult

## `apex.studies.LINE`  (extends `ScenarioCommand`)
Class representing a Nastran "LINE" case control command. The LINE command is used to control the maximum number of lines on each printed output.
Properties: `value`

Methods:

- `getValue() -> int` — Gets optional property used to limit the number of lines that Nastran will write to each printed output. If omitted, Nastran will write a maximum of 50 lines to each page Setting this property to any positive integer will cause Nastran to limit the number of lines of printed to each page to the value provided here.
#### `setValue(value: int) -> None`
Sets optional property used to limit the number of lines that Nastran will write to each printed output. If omitted, Nastran will write a maximum of 50 lines to each page Setting this property to any positive integer will cause Nastran to limit the number of lines of printed to each page to the value provided here.

- `value` — Set the value of this LINE


## `apex.studies.LOAD`  (extends `ScenarioCommand`)
Class representing a Nastran LOAD case control command. LOAD commands are used to select one or more Loads, applied to the model, for inclusion in a LoadCaseItem. Loads are identified by their ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of at least one load assigned to the model referenced by the Scenario that this command is composed by Use this command to assign a Loads to a Scenario, Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets the ID of at least one load assigned to the model referenced by the Scenario that this command is composed by Use this command to assign a Loads to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this LOAD


## `apex.studies.LoadCase`  (extends `Entity`, `IName`, `IUserAttributes`)
Load case of a scenario.
Properties: `id`, `steps`

Methods:

#### `addStep(name: str, description: str, stepType: apex.studies.StepType, initialStepState: apex.studies.InitialStepState, loadCase: apex.studies.LoadCase, step: apex.studies.Step, loadFactor: float, id: int) -> apex.studies.Step`
adds (and returns) a new step to this loadCase.

- `name` — An optional name for the Step. If omitted the system will supply a default name.
- `description` — An optional description for the Step.
- `stepType` — Step type to be create for each load case. In current release, only static step type is available. Return error if the step type is not "Static".
- `initialStepState` — Initial Step State for the new step.
- `loadCase` — Optional-Load Case for the initial step state of the step to be created. The option is only available when initialStepState = StepInAnotherLoadCase.
- `step` — Optional-Step for the initial step state of the step to be created. The option is only available when initialStepState = StepInAnotherLoadCase or StepInThisLoadCase.
- `loadFactor` — Optional-Load factor for the initial step state.
- `id` — Optional-ID of the step

Returns: Step object

#### `getId() -> int`
ID for this LoadCase.

Returns: the id of this LoadCase.

#### `getStep(name: str) -> apex.studies.Step`
Retrieves a single Step from the LoadCase using the supplied name. If a Step with a matching name does not exist within the LoadCase the method will throw an exception.

- `name` — of a Step

Returns: returns a single Step in this LoadCase

#### `getSteps() -> apex.studies.StepCollection`
returns a collection of all Steps composed by this LoadCase

Returns: a collection of all Steps composed by this LoadCase

#### `update(name: str, description: str, id: int) -> None`
Update the load case.

- `name` — Optional- Name for this LoadCase.
- `description` — Optional-Description for this LoadCase .
- `id` — Optional-id of the load case


## `apex.studies.LoadCaseCollection`  (extends `EntityCollection`)

Methods:

- `LoadCaseCollection() -> None` — Construct a new LoadCaseCollection.

## `apex.studies.LoadCaseItem`  (extends `Entity`, `IName`, `IUserAttributes`)
Class LoadCaseItem A base class for ScenarioNastran SubcaseNastran, StepNastran and SubstepNastran.
Properties: `applicableCommandNames`, `label`, `subtitle`, `title`

Methods:

#### `activateCommands(activeCommands: [str]) -> [ScenarioCommand]`
Activates the case control commands identified using the activeCommands argument.

- `activeCommands` — a list of command names to activate in this load case item. Commands included in this list that are not applicable to this load case item will be silently ignored

Returns: ScenarioCommandCollection ScenarioCommand collection had be activated

#### `deactivateCommands(inactiveCommands: [str]) -> [ScenarioCommand]`
Deactivates the case control commands identified using the inactiveCommands argument.

- `inactiveCommands` — a list of command names to deactivate in this load case item. Commands included in this list that are not applicable to this load case item will be silently ignored

Returns: ScenarioCommandCollection ScenarioCommand collection had be not activated

- `getApplicableCommandNames() -> [str]` — Gets a list of the names of all ScenarioCommands that are applicable to this LoadCaseItem.
#### `getCommand(commandName: str) -> ScenarioCommand`
Retrieves the command identified by the argument from this LoadCaseItem.

- `commandName` — Identifies the name of the command to retrieve

Returns: the command identified

- `getLabel() -> str` — Gets a Label for this LoadCaseItem. The string provided here will be exported as a LABEL case command associated with this LoadCaseItem.
- `getSubtitle() -> str` — Gets a Subtitle for this LoadCaseItem. The string provided here will be exported as a SUBTITLE case command associated with this LoadCaseItem.
- `getTitle() -> str` — Gets a Title for this LoadCaseItem. The string provided here will be exported as a TITLE case command associated with this LoadCaseItem.
#### `setCommand(commandName: str, activate: bool) -> None`
Sets the command provided in the argument on this LoadCaseItem. If the command is not applicable to this LoadCase Item the method will raise an exception.

- `commandName` — The name of the command to set
- `activate` — An optional boolean value to indicate whether the command should be activated when set. The default value of True indicates that the command will be activated after being set Set this value to False to de-activate the command after setting the value

- `setLabel(label: str) -> None` — Sets a Label for this LoadCaseItem. The string provided here will be exported as a LABEL case command associated with this LoadCaseItem.
- `setSubtitle(subtitle: str) -> None` — Sets a Subtitle for this LoadCaseItem. The string provided here will be exported as a SUBTITLE case command associated with this LoadCaseItem.
- `setTitle(title: str) -> None` — Sets a Title for this LoadCaseItem. The string provided here will be exported as a TITLE case command associated with this LoadCaseItem.

## `apex.studies.MAPMODES`  (extends `ScenarioCommand`)
Class representing a Nastran "MAPMODES" case control command The MAPMODES command is used to choose between writing the modes from the current Nastran run to a .op2 file or map the modes from the current run to those from a prior run.
Properties: `baseline_or_mapping`, `value`

Methods:

- `getBaseline_or_mapping() -> str` — Gets property used to define whether this MAPMODES command is a baseline run and cause the modes to be written to the .op2 file or a mapping run which will map modes from a previous run to this run. This property may be assigned one the following values, "BASELINE" - indicate this run is a baseline run and modes will be written to the .op2 file "MAPPING" - indicates this run is a mapping run and modes will be mapped from an .op2 file from a previous run to the modes calcuated by this run.
- `getValue() -> int` — Gets property defining the unit number (as a positive integer) associated wit the .op2 file that contains the modes from the initial run and into which the modes from this run will be matched.
#### `setBaseline_or_mapping(baseline_or_mapping: str) -> None`
Sets property used to define whether this MAPMODES command is a baseline run and cause the modes to be written to the .op2 file or a mapping run which will map modes from a previous run to this run. This property may be assigned one the following values, "BASELINE" - indicate this run is a baseline run and modes will be written to the .op2 file "MAPPING" - indicates this run is a mapping run and modes will be mapped from an .op2 file from a previous run to the modes calcuated by this run.

- `baseline_or_mapping` — Set the baseline_or_mapping of this MAPMODES

#### `setValue(value: int) -> None`
Sets property defining the unit number (as a positive integer) associated wit the .op2 file that contains the modes from the initial run and into which the modes from this run will be matched.

- `value` — Set the value of this MAPMODES


## `apex.studies.MASTER`  (extends `ScenarioCommand`)
Class used to represent a Nastran "MASTER" case control command The MASTER command is used to indicate that all commands within the same Subcase as this MASTER command will be applied to all following subcases (until another NASTER command is encountered)

## `apex.studies.MAXLINES`  (extends `ScenarioCommand`)
Class representing a Nastran "MAXLINES" case control command. MAXLINES commands are used to control the maximum number of lines in the printed output.
Properties: `value`

Methods:

- `getValue() -> int` — Gets optional property used to limit the number of lines that Nastran will write to the printed output. If omitted, Nastran will write a maximum of 999,999,999 lines to the printed output Setting this property to any positive integer will cause Nastran to limit the number of lines of printed output to the value provided here.
#### `setValue(value: int) -> None`
Sets optional property used to limit the number of lines that Nastran will write to the printed output. If omitted, Nastran will write a maximum of 999,999,999 lines to the printed output Setting this property to any positive integer will cause Nastran to limit the number of lines of printed output to the value provided here.

- `value` — Set the value of this MAXLINES


## `apex.studies.MAXMINDEF`  (extends `ScenarioCommand`)
Class representing the Nastran "MAXMIN(DEF)" case control command The "MAXMIN(DEF)" command is used to define parameters that control the monitoring of maximum and minimum values during data recovery.
Properties: `all_output_options`, `brief_or_full`, `coordinate_system_grid`, `element_types_components`, `grid_or_element`, `result_component_grid`, `result_quantity_element`, `result_quantity_grid`, `rms_values`, `user_output_options`

Methods:

- `getAll_output_options() -> ( str,int )` — Gets the number of maximum and minimum values to be printed. The property controls how many max/min value are printed using all three Nastran supported ordering algorithms (Absolute, Min, Max) To define different numbers of values for each ordering algorithm or to selectively omit printing based on one or more of these algorithms use the user_output_options property instead. This property expects a List type (or None) although any type of iterable can be provided, not just List If a list is provided, the first item in the list must be "ALL" and the second item must be either an integer defining the number of max/min values to print or None. If None is provided, Nastran will print a default number of values (Default = 5) Setting this property to None will clear any previously set values and will omit this field from the exported Nastran file for this MAXMINDEF command Setting this property to ['ALL', 6]will cause a MAXMINDEF to be written to the Nastran file that includes the following options - 'ALL=6' This property will REPLACE any previous properties defined using "user_output_options".
- `getBrief_or_full() -> str` — Gets property used to control whether only the max/min data will be printed or if additional standard data recovery will also be provided This property accepts the following values, "BRIEF" - output is limited to the max/min values only None - same as "BRIEF" except this field will not be written to the Nastran file for the is MAXMIN(DEF) command ("BRIEF" is the Nastran default) "FULL" - extended data is output.
- `getCoordinate_system_grid() -> str` — Gets property used to define the coordinate system used for grid based output max.min monitoring. This property may be assigned any of the following values, "BASIC" - the max/min values will be determined using the Nastran BASIC coordinate system None - the same as "BASIC", except this field will not be written to the Nastran file for this MONITOR command (BASIC is the Nastran default for thsi command) "GLOBAL" - the max/min values will be determined using the Nastran GLOBAL coordinate system n - positive integer identifying an existing local coordinate system that will be used for to the determination of max/min values.
- `getElement_types_components() -> [str]` — Gets an optional property used to identify the element types and result components that will be monitored by this MAXMINDEF command This property may be omitted (assigned a None value) or assigned a list of strings, (minimum one) where each string identifies an element type and list of result components to be monitored by this MONITOR command. Each string in the list is composed of two parts. The first part identifies the Nastran element type to be monitored and uses the Nastran element type entry ("CQUAD", "CHEXA" etc) but with the initial "C" character removed - for example "QUAD4", HEXA8". Exceptions to the rule to remove the initial "C" character are the "CONROD" and "CONV" elements which must be specified with the initial character intact - for example "CONROD", "CONV" etc. The second part of the string identifies element based result quantity components and options. Multiple components and options can be associated with each element type. The following example shows the types of values that can be assigned to this property ["HEXA P1/ALL P2/ALL P3/ALL OCT/ALL", "BEAM SXC SXD SXE SXF SMAX SMIN"].
- `getGrid_or_element() -> str` — Gets property defining whether this MAXMIN(DEF) command will define max.min data recovery for Grid or Elements based output data This property may be set to any of the values shown below, "GRID" - indicates that the data on this command is Grid based data "ELEMENT" indicates that the data on this command is Element based data.
- `getResult_component_grid() -> str` — Gets property identifying the type of GRID based result COMPONENT for which max/min values should be monitored. This property is only used when the value assigned to the "grid_or_element" property is "GRID" - when this MAXMIN(DEF) command is associated with Grid based output data. This property may be assigned the following values, "T1" - Grid point translational component 1 "T2" - Grid point translational component 2 "T3" - Grid point translational component 3 "R1" - Grid point rotational component 1 "R2" - Grid point rotational component 2 "R3" - Grid point rotational component 3 "MAGT" - Magnitude of the grid point translational components "MAGR" - Magnitude of the grid point rotational components If this property is set when grid_or_element" property is set to "ELEMENT" it will be silently ignored.
- `getResult_quantity_element() -> str` — Gets property identifying the type of ELEMENT based result quantity for which max/min values should be monitored. This property is only used when the value assigned to the "grid_or_element" property is "ELEMENT" - when this MAXMIN(DEF) command is associated with Grid based output data. This property may be assigned the following values, "STRESS" - Stresses "STRAIN" - Strains "FORCE" - Element forces If this property is set when grid_or_element" property is set to "GRID" it will be silently ignored.
- `getResult_quantity_grid() -> str` — Gets property identifying the type of GRID based result quantity for which max/min values should be monitored. This property is only used when the value assigned to the "grid_or_element" property is "GRID" - when this MAXMIN(DEF) command is associated with Grid based output data. This property may be assigned the following values, "DISP" - Displacements "VELO" - Velocities "ACCE" - Accelerations "MPCF" - Multi-point constraint forces "SPCF" - Single point constraint forces "OLOAD" - Applied loads If this property is set when grid_or_element" property is set to "ELEMENT" it will be silently ignored.
- `getRms_values() -> str` — Gets property to enable/disable root mean square values of each max/min requested by the ABSOLUTE, MIN and MAX properties This property may be assigned the following values, "RMS" - enables output of RMS values None - RMS values will not be output.
- `getUser_output_options() -> [( str,int )]` — Gets the ordering type and associated number of values based on that ordering type to print This property controls how many value are printed by choosing a value ordering algorithm (Absolute, Min, Max) and defining the number of values for that algorithm to print. This property uses a "List of List" design although any type of iterable can be provided, not just List Each internal list must consist of two entries : the ordering type followed by the number of values to print based on this ordering. The ordering type must be one the following values "ABSOLUTE" - Orders values based absolute values and then selects the top defined number of values to print (Default =5) "MINALG" - Orders values algebraically and then selects the bottom defined number of values to print (Default =5) "MAXALG" - Orders values algebraically and then selects the top defined number of values to print (Default =5) The number of values for each is defined using an integer, or None. Using None will cause the field to be written with out a value and Nastran will user he default value for this field. Any combination of ordering types can be defined although duplicates are no allowed and will cause Apex to raise an exception If an ordering method is not included, no values will be printed based on that ordering method Setting this property to [['ABSOLUTE', 6], ['MINALG, 10], ['MAXALG', None]] will cause a MAXMINDEF to be written to the Nastran file tha includes the following options - 'ABSOLUTE=6 MINALG=10 MAXALG' This property will REPLACE any previous properties defined using "all_output_options".
#### `setAll_output_options(all_output_options: ( str,int )) -> None`
Sets the number of maximum and minimum values to be printed. The property controls how many max/min value are printed using all three Nastran supported ordering algorithms (Absolute, Min, Max) To define different numbers of values for each ordering algorithm or to selectively omit printing based on one or more of these algorithms use the user_output_options property instead. This property expects a List type (or None) although any type of iterable can be provided, not just List If a list is provided, the first item in the list must be "ALL" and the second item must be either an integer defining the number of max/min values to print or None. If None is provided, Nastran will print a default number of values (Default = 5) Setting this property to None will clear any previously set values and will omit this field from the exported Nastran file for this MAXMINDEF command Setting this property to ['ALL', 6]will cause a MAXMINDEF to be written to the Nastran file that includes the following options - 'ALL=6' This property will REPLACE any previous properties defined using "user_output_options".

- `all_output_options` — Set the all_output_options of this MAXMINDEF

#### `setBrief_or_full(brief_or_full: str) -> None`
Sets property used to control whether only the max/min data will be printed or if additional standard data recovery will also be provided This property accepts the following values, "BRIEF" - output is limited to the max/min values only None - same as "BRIEF" except this field will not be written to the Nastran file for the is MAXMIN(DEF) command ("BRIEF" is the Nastran default) "FULL" - extended data is output.

- `brief_or_full` — Set the brief_or_full of this MAXMINDEF

#### `setCoordinate_system_grid(coordinate_system_grid: str) -> None`
Sets property used to define the coordinate system used for grid based output max.min monitoring. This property may be assigned any of the following values, "BASIC" - the max/min values will be determined using the Nastran BASIC coordinate system None - the same as "BASIC", except this field will not be written to the Nastran file for this MONITOR command (BASIC is the Nastran default for thsi command) "GLOBAL" - the max/min values will be determined using the Nastran GLOBAL coordinate system n - positive integer identifying an existing local coordinate system that will be used for to the determination of max/min values.

- `coordinate_system_grid` — Set the coordinate_system_grid of this MAXMINDEF

#### `setElement_types_components(element_types_components: [str]) -> None`
Sets an optional property used to identify the element types and result components that will be monitored by this MAXMINDEF command This property may be omitted (assigned a None value) or assigned a list of strings, (minimum one) where each string identifies an element type and list of result components to be monitored by this MONITOR command. Each string in the list is composed of two parts. The first part identifies the Nastran element type to be monitored and uses the Nastran element type entry ("CQUAD", "CHEXA" etc) but with the initial "C" character removed - for example "QUAD4", HEXA8". Exceptions to the rule to remove the initial "C" character are the "CONROD" and "CONV" elements which must be specified with the initial character intact - for example "CONROD", "CONV" etc. The second part of the string identifies element based result quantity components and options. Multiple components and options can be associated with each element type. The following example shows the types of values that can be assigned to this property ["HEXA P1/ALL P2/ALL P3/ALL OCT/ALL", "BEAM SXC SXD SXE SXF SMAX SMIN"].

- `element_types_components` — Set the element_types_components of this MAXMINDEF

#### `setGrid_or_element(grid_or_element: str) -> None`
Sets property defining whether this MAXMIN(DEF) command will define max.min data recovery for Grid or Elements based output data This property may be set to any of the values shown below, "GRID" - indicates that the data on this command is Grid based data "ELEMENT" indicates that the data on this command is Element based data.

- `grid_or_element` — Set the grid_or_element of this MAXMINDEF

#### `setResult_component_grid(result_component_grid: str) -> None`
Sets property identifying the type of GRID based result COMPONENT for which max/min values should be monitored. This property is only used when the value assigned to the "grid_or_element" property is "GRID" - when this MAXMIN(DEF) command is associated with Grid based output data. This property may be assigned the following values, "T1" - Grid point translational component 1 "T2" - Grid point translational component 2 "T3" - Grid point translational component 3 "R1" - Grid point rotational component 1 "R2" - Grid point rotational component 2 "R3" - Grid point rotational component 3 "MAGT" - Magnitude of the grid point translational components "MAGR" - Magnitude of the grid point rotational components If this property is set when grid_or_element" property is set to "ELEMENT" it will be silently ignored.

- `result_component_grid` — Set the result_component_grid of this MAXMINDEF

#### `setResult_quantity_element(result_quantity_element: str) -> None`
Sets property identifying the type of ELEMENT based result quantity for which max/min values should be monitored. This property is only used when the value assigned to the "grid_or_element" property is "ELEMENT" - when this MAXMIN(DEF) command is associated with Grid based output data. This property may be assigned the following values, "STRESS" - Stresses "STRAIN" - Strains "FORCE" - Element forces If this property is set when grid_or_element" property is set to "GRID" it will be silently ignored.

- `result_quantity_element` — Set the result_quantity_element of this MAXMINDEF

#### `setResult_quantity_grid(result_quantity_grid: str) -> None`
Sets property identifying the type of GRID based result quantity for which max/min values should be monitored. This property is only used when the value assigned to the "grid_or_element" property is "GRID" - when this MAXMIN(DEF) command is associated with Grid based output data. This property may be assigned the following values, "DISP" - Displacements "VELO" - Velocities "ACCE" - Accelerations "MPCF" - Multi-point constraint forces "SPCF" - Single point constraint forces "OLOAD" - Applied loads If this property is set when grid_or_element" property is set to "ELEMENT" it will be silently ignored.

- `result_quantity_grid` — Set the result_quantity_grid of this MAXMINDEF

#### `setRms_values(rms_values: str) -> None`
Sets property to enable/disable root mean square values of each max/min requested by the ABSOLUTE, MIN and MAX properties This property may be assigned the following values, "RMS" - enables output of RMS values None - RMS values will not be output.

- `rms_values` — Set the rms_values of this MAXMINDEF

#### `setUser_output_options(user_output_options: [( str,int )]) -> None`
Sets the ordering type and associated number of values based on that ordering type to print This property controls how many value are printed by choosing a value ordering algorithm (Absolute, Min, Max) and defining the number of values for that algorithm to print. This property uses a "List of List" design although any type of iterable can be provided, not just List Each internal list must consist of two entries : the ordering type followed by the number of values to print based on this ordering. The ordering type must be one the following values "ABSOLUTE" - Orders values based absolute values and then selects the top defined number of values to print (Default =5) "MINALG" - Orders values algebraically and then selects the bottom defined number of values to print (Default =5) "MAXALG" - Orders values algebraically and then selects the top defined number of values to print (Default =5) The number of values for each is defined using an integer, or None. Using None will cause the field to be written with out a value and Nastran will user he default value for this field. Any combination of ordering types can be defined although duplicates are no allowed and will cause Apex to raise an exception If an ordering method is not included, no values will be printed based on that ordering method Setting this property to [['ABSOLUTE', 6], ['MINALG, 10], ['MAXALG', None]] will cause a MAXMINDEF to be written to the Nastran file tha includes the following options - 'ABSOLUTE=6 MINALG=10 MAXALG' This property will REPLACE any previous properties defined using "all_output_options".

- `user_output_options` — Set the user_output_options of this MAXMINDEF


## `apex.studies.METHOD`  (extends `ScenarioCommand`)
Class representing a Nastran METHOD case control command The METHOD command is used to select real eigenvalue extraction parameters that have been defined in an existing EIGRL, EIGR or EIGB entity and to control how/if the eigenvalues will be extracted on fluid and structural regions of the model.
Properties: `scope`, `value`

Methods:

- `getScope() -> str` — Gets optional property used to define how the eigenvalue extraction parameters defined in the referenced EIGRL, EIGR or EIGB entity impact any fluid and structural regions of the model this property supports the following values, 'BOTH' - Causes the referenced eigenvalue extraction parameters to be applied to both the structural and the fluid regions of the model None - has the same effect as 'BOTH', but omits this field from the exported Nastran file which causes NASTRAN to use the logic defined above for 'BOTH' 'STRUCTURE' - Causes the referenced eigenvalue extraction parameters to be applied only to the structural region of the model 'FLUID' - Causes the referenced eigenvalue extraction parameters to be applied only to the fluid region of the model 'COUPLED' - Causes the referenced eigenvalue extraction parameters to be applied to the coupled system of the model using a subspace iteration method 'SYMCOUP' - Causes the referenced eigenvalue extraction parameters to be applied to the coupled system of the model using a the Lanczos method.
- `getValue() -> int` — Gets a positive integer used to select a set of eigenvalue extraction parameters defined in an existing EIGRL, EIGR or EIGB (Buckling only) entry with the corresponding ID.
#### `setScope(scope: str) -> None`
Sets optional property used to define how the eigenvalue extraction parameters defined in the referenced EIGRL, EIGR or EIGB entity impact any fluid and structural regions of the model this property supports the following values, 'BOTH' - Causes the referenced eigenvalue extraction parameters to be applied to both the structural and the fluid regions of the model None - has the same effect as 'BOTH', but omits this field from the exported Nastran file which causes NASTRAN to use the logic defined above for 'BOTH' 'STRUCTURE' - Causes the referenced eigenvalue extraction parameters to be applied only to the structural region of the model 'FLUID' - Causes the referenced eigenvalue extraction parameters to be applied only to the fluid region of the model 'COUPLED' - Causes the referenced eigenvalue extraction parameters to be applied to the coupled system of the model using a subspace iteration method 'SYMCOUP' - Causes the referenced eigenvalue extraction parameters to be applied to the coupled system of the model using a the Lanczos method.

- `scope` — Set the scope of this METHOD

#### `setValue(value: int) -> None`
Sets a positive integer used to select a set of eigenvalue extraction parameters defined in an existing EIGRL, EIGR or EIGB (Buckling only) entry with the corresponding ID.

- `value` — Set the value of this METHOD


## `apex.studies.MFREQUENCY`  (extends `ScenarioCommand`)
Class used to represent a Nastran MFREQUENCY case control command The MFREQUENCY command is used to define the set of of forcing frequencies that will be used in a frequency response analysis as the master frequencies for matrix generation Properties of this class enable different methods to be used to define the frequency list.
Properties: `interpolation_type`, `tolerance`, `value`

Methods:

- `getInterpolation_type() -> str` — Gets enables selection of either linear or logarithmic interpolation between the frequencies defined by this MFREQUENCY command This property may be assign one of the values shown below, 'Linear' - selects linear interpolation between master frequencies 'Log10' - selects logarithmic interpolation between master frequencies Assigning values other than the ones defined here will cause Ape to raise an exception when this MFREQUENCY command is assigned to a Load case item.
- `getTolerance() -> float` — Gets an optional frequency value threshold used to control when frequency interpolation is used in frequency dependent materials, springs and bushes. This property may be assigned any floating point value greater than or equal to 0.0 or None. If None is assigned, Nastran will use a default frequency threshold tolerance of 0.1 but this field will not be written to the Nastran file.
- `getValue() -> str` — Gets optional property used to select how this MFREQUENCY command will define its set of master frequencies This property may be assigned one of the following values, 'AUTO' - causes Nastran to determine a set of master frequencies automatically None - has the same effect as 'AUTO' with the exception that 'AUTO' will not be written to the Nastran file for this command 'NOAUTO' - prevents Nastran from automatically calculating a set of master frequencies. The frequencies defined using the 'FREQUENCY' case control command will be use as master frequencies n - a positive integer used to select one or more existing FREQ, FREQ1 or FREQ2 entities by their corresponding ID. The frequencies defined on these entries will be used as the master frequencies.
#### `setInterpolation_type(interpolation_type: str) -> None`
Sets enables selection of either linear or logarithmic interpolation between the frequencies defined by this MFREQUENCY command This property may be assign one of the values shown below, 'Linear' - selects linear interpolation between master frequencies 'Log10' - selects logarithmic interpolation between master frequencies Assigning values other than the ones defined here will cause Ape to raise an exception when this MFREQUENCY command is assigned to a Load case item.

- `interpolation_type` — Set the interpolation_type of this MFREQUENCY

#### `setTolerance(tolerance: float) -> None`
Sets an optional frequency value threshold used to control when frequency interpolation is used in frequency dependent materials, springs and bushes. This property may be assigned any floating point value greater than or equal to 0.0 or None. If None is assigned, Nastran will use a default frequency threshold tolerance of 0.1 but this field will not be written to the Nastran file.

- `tolerance` — Set the tolerance of this MFREQUENCY

#### `setValue(value: str) -> None`
Sets optional property used to select how this MFREQUENCY command will define its set of master frequencies This property may be assigned one of the following values, 'AUTO' - causes Nastran to determine a set of master frequencies automatically None - has the same effect as 'AUTO' with the exception that 'AUTO' will not be written to the Nastran file for this command 'NOAUTO' - prevents Nastran from automatically calculating a set of master frequencies. The frequencies defined using the 'FREQUENCY' case control command will be use as master frequencies n - a positive integer used to select one or more existing FREQ, FREQ1 or FREQ2 entities by their corresponding ID. The frequencies defined on these entries will be used as the master frequencies.

- `value` — Set the value of this MFREQUENCY


## `apex.studies.MNFGenerationProperty`
Container class used to define parameters that affect the generation and content of a Modal Neutral File (MNF). If an MNFGeneratiopnProperty instance is present in a ModesStep when that Step is executed an MNF file will be generated when the Scenario is executed. Several options can be defined to control how the MNF is generated and what output it contains and these are defined using the properties of this class.
Properties: `generateGridPointStrains`, `generateGridPointStresses`, `generateMNF`, `massInvariantOptions`, `mnfFilename`

Methods:

- `MNFGenerationProperty() -> None` — Default constructor for MNFGenerationProperty.
#### `MNFGenerationProperty(mnfFilename: str) -> None`
Constructor for MNFGenerationProperty enabling the mnfFilename to be specified during construction.

- `mnfFilename` — The modal neutral file name that will be used when the MNF is generated

- `getGenerateGridPointStrains() -> bool` — Gets a Boolean value used to control output of grid point strains to the MNF. Set this property to true to output grid point strains or false to suppress them.
- `getGenerateGridPointStresses() -> bool` — Gets a Boolean value used to control output of grid point stresses to the MNF. Set this property to true to output grid point stresses or false to suppress them.
- `getGenerateMNF() -> bool` — Gets a Boolean value that controls whether or not a modal neutral file will be generated. The default value of true will cause the MNF to be generated after the normal modes calculations are complete. If this value is false, no MNF will be generated.
- `getMassInvariantOptions() -> MNFMassInvariantOptions` — Gets an Enumeration property that controls which mass invariants are written to the MNF.
- `getMnfFilename() -> str` — Gets the name of the exported modal neutral files.
- `setGenerateGridPointStrains(generateGridPointStrains: bool) -> None` — Sets a Boolean value used to control output of grid point strains to the MNF. Set this property to true to output grid point strains or false to suppress them.
- `setGenerateGridPointStresses(generateGridPointStresses: bool) -> None` — Sets a Boolean value used to control output of grid point stresses to the MNF. Set this property to true to output grid point stresses or false to suppress them.
- `setGenerateMNF(generateMNF: bool) -> None` — Sets a Boolean value that controls whether or not a modal neutral file will be generated. The default value of true will cause the MNF to be generated after the normal modes calculations are complete. If this value is false, no MNF will be generated.
- `setMassInvariantOptions(massInvariantOptions: MNFMassInvariantOptions) -> None` — Sets an Enumeration property that controls which mass invariants are written to the MNF.
- `setMnfFilename(mnfFilename: str) -> None` — Sets the name of the exported modal neutral files.

## `apex.studies.MODES`  (extends `ScenarioCommand`)
Class representing a Nastran "MODES" case control command The MODES command is used to repeat output for a normal modes subcase.
Properties: `value`

Methods:

- `getValue() -> int` — Gets a positive integer specifying the number of times the subcase with which this MODES command is associated will be repeated.
#### `setValue(value: int) -> None`
Sets a positive integer specifying the number of times the subcase with which this MODES command is associated will be repeated.

- `value` — Set the value of this MODES


## `apex.studies.MODESELECT`  (extends `ScenarioCommand`)
Class representing a Nastran "MODESLECT" case control command The MODESLECT command is used to select a subset of the calculated modes for inclusion in modal dynamic analyses.
Properties: `domain_type`, `force_include_exclude`, `force_mode_inclusion_exclusion`, `force_mode_set_inclusion_exclusion`, `frequency_range`, `include_exclude_modes`, `lowest`, `mod_eff_mass_frac`, `mode_range`, `selected_mode_include_exclude`, `selected_mode_set_include_excldue`, `selection_method`, `threshold_method`

Methods:

- `getDomain_type() -> str` — Gets specifies whether the modes selected by this MODESELECT command will be used in the calculation of the dynamic response of the structure or the fluid region of the model This property may be assigned any one of the following values, "STRUCTURE" - selected modes will be applied to the dynamic response of the structure None - same as "STRUCTURE" with the exception that this field will not be written to the Nastran file for this command. ("STRUCTURE" is the Nastran default value for this field) "FLUID" - selected modes will be applied to the dynamic response of the fluid region.
- `getForce_include_exclude() -> int` — Gets a property used to define whether modes defined on the "force_mode_inclusion_exclusion" or "force_mode_set_inclusion_exclusion" properties will be forcefully INCLUDED or EXCLUDED from the simulation This property may be assigned either one of the following values, 1 - The modes will be unconditionally INCLUDED -1 - The modes will be unconditionally EXCLUDED.
- `getForce_mode_inclusion_exclusion() -> int` — Gets specifies the ID of a single mode that will be unconditionally INCLUDED or EXCLUDED from the simulation base on the value of the "force_include_exclude" property.
- `getForce_mode_set_inclusion_exclusion() -> int` — Gets specifies the ID of a ScenarioSetModeId that defines the IDs one or more modes that will be unconditionally INCLUDED or EXCLUDED from the simulation based on the value of the "force_include_exclude" property. Any modes defined here will be included/excluded irrespective of other settings on this command The option is only valid if the "selection_method" property is set to "FREQRANGE" or "MODEFFMASS" and will be silently ignored in all other cases.
- `getFrequency_range() -> [float]` — Gets specifies, using a list of two floating point values, the lower and upper limits of a range of modal frequencies that will be used in the calculation of the dynamic response. All modes with frequencies between and including the first and second values in this list will be selected and used in the dynamic response calculation. This property will be silently ignored unless "selection_method" = "FREQRANGE".
- `getInclude_exclude_modes() -> int` — Gets a property used to define whether the modes defined on the "selected_mode" or "selected_mode_set" properties will be forcefully INCLUDED or EXCLUDED from the simulation This property may be assigned either one of the following values, 1 - The modes will be unconditionally INCLUDED -1 - The modes will be unconditionally EXCLUDED.
- `getLowest() -> int` — Gets specifies, using a positive integer) the number of modes that will be used in the calculation of the dynamic response. The value specified here will select all modes sequentially from the lowest available mode up to the mode number specified here. This property will be silently ignored unless "selection_method" = "LOWEST".
- `getMod_eff_mass_frac() -> [( str,float )]` — Gets specifies which modes will be used in the dynamic response calculation using threshold values of modal effective mass fraction. Different threshold values may be assigned to each of the three translational and three rotational degrees of freedom. Any modes with effective mass fractions greater than the specified values will be selected and included in the dynamic response. Each component and it's optional associated threshold value is defined using a heterogeneous list which may contain one or two items. The first item in the list identifies a degree of freedom using one of the following strings, "T1FR" - translation degree of freedom 1 "T2FR" - translation degree of freedom 2 "T3FR" - translation degree of freedom 3 "R1FR" - rotational degree of freedom 1 "R2FR" - rotational degree of freedom 2 "R3FR" - rotational degree of freedom 3 "ALLFR" - all degrees of freedom not explicitly defined above The second item in the list is an optional value that defines the threshold mass fraction for the associated degree of freedom. The mass fraction must be assigned a floating point value greater than 0.0 and less than or equal to 1.0 If the second value (mass fraction) is omitted (or set to None) Nastran will assign a default mass fraction value Multiple degrees of freedom, each with potentially different mass fraction thresholds may be assigned this property using a list of lists where each internal list represents a single degree of freedom with an optional mass fraction value. If a degree of freedom is provided more than once in this property, the second value will be used and any preceding values will be silently ignored. An example of a valid input for this property is shown below, [["T1FR", 0.9],["T2FR",], ["T3FR", None], ["R3FR", 0.85]] This example will cause the following output to the Nastran file for this command MODESELECT (T1FR = 0.90 T2FR T3FR R3FR = 0.85) This property will be silently ignored unless "selection_method" = "MODEFFMASS".
- `getMode_range() -> [int]` — Gets specifies, using a list of two positive integers, the lower and upper limits of a range of mode numbers that will be used in the calculation of the dynamic response. All modes with numbers between and including the first and second values in this list will be selected and used in the dynamic response calculation. This property will be silently ignored unless "selection_method" = "MODERANGE".
- `getSelected_mode_include_exclude() -> int` — Gets specifies the ID of a single mode that will be INCLUDED or EXCLUDED from the simulation base on the value of the "include_exclude_modes" property.
- `getSelected_mode_set_include_excldue() -> int` — Gets specifies the ID of a ScenarioSetModeId that defines the IDs of one or more modes selected for inclusion or exclusion from the simulation. The modes selected here will either be INCLUDED or EXCLUDED based on the value of the include_exclude_modes property This property is only valid when the "selection"method" property is set to "USER".
- `getSelection_method() -> str` — Gets specifies which one of five different methods will be used to select modes This property may be assigned any one of the following values, "USER" - user defined mode numbers will selected "LOWEST" - the specified number of lowest modes will be selected "MODERANGE" - modes will be selected based on mode number range "FREQRANGE" - modes will be selected based on frequency range "MODEFFMASS" - modes will be selected based on modal effective mass fraction.
- `getThreshold_method() -> str` — Gets specifies how the model effective mass fraction thresholds specified using the "mod_eff_mass_fraction" property are used to select modes This property may be assigned any one of the following values, "SUM" - modes will be selected by first sorting them in descending order of the corresponding modal effective mass fraction values. Then, starting from the first mode in this sorted list, the modes are selected until the sum of corresponding MEFFMFRA values equals or just exceeds the threshold value for that component None - same as "SUM" with the exception that this field will not be written to the Nastran file for this MODESELECT command. ("SUM" is the Nastran default value for this field) "ANYMIN" - Any mode whose modal effective mass fraction for any specified component equals or exceeds the threshold value for that component will be selected. "ALLMIN" - Any mode whose modal effective mass fraction for all of the specified components equals or exceeds the corresponding threshold values for those components will be selected. This property will be silently ignored unless "selection_method" = "MODEFFMASS".
#### `setDomain_type(domain_type: str) -> None`
Sets specifies whether the modes selected by this MODESELECT command will be used in the calculation of the dynamic response of the structure or the fluid region of the model This property may be assigned any one of the following values, "STRUCTURE" - selected modes will be applied to the dynamic response of the structure None - same as "STRUCTURE" with the exception that this field will not be written to the Nastran file for this command. ("STRUCTURE" is the Nastran default value for this field) "FLUID" - selected modes will be applied to the dynamic response of the fluid region.

- `domain_type` — Set the domain_type of this MODESELECT

#### `setForce_include_exclude(force_include_exclude: int) -> None`
Sets a property used to define whether modes defined on the "force_mode_inclusion_exclusion" or "force_mode_set_inclusion_exclusion" properties will be forcefully INCLUDED or EXCLUDED from the simulation This property may be assigned either one of the following values, 1 - The modes will be unconditionally INCLUDED -1 - The modes will be unconditionally EXCLUDED.

- `force_include_exclude` — Set the force_include_exclude of this MODESELECT

#### `setForce_mode_inclusion_exclusion(force_mode_inclusion_exclusion: int) -> None`
Sets specifies the ID of a single mode that will be unconditionally INCLUDED or EXCLUDED from the simulation base on the value of the "force_include_exclude" property.

- `force_mode_inclusion_exclusion` — Set the force_mode_inclusion_exclusion of this MODESELECT

#### `setForce_mode_set_inclusion_exclusion(force_mode_set_inclusion_exclusion: int) -> None`
Sets specifies the ID of a ScenarioSetModeId that defines the IDs one or more modes that will be unconditionally INCLUDED or EXCLUDED from the simulation based on the value of the "force_include_exclude" property. Any modes defined here will be included/excluded irrespective of other settings on this command The option is only valid if the "selection_method" property is set to "FREQRANGE" or "MODEFFMASS" and will be silently ignored in all other cases.

- `force_mode_set_inclusion_exclusion` — Set the force_mode_set_inclusion_exclusion of this MODESELECT

#### `setFrequency_range(frequency_range: [float]) -> None`
Sets specifies, using a list of two floating point values, the lower and upper limits of a range of modal frequencies that will be used in the calculation of the dynamic response. All modes with frequencies between and including the first and second values in this list will be selected and used in the dynamic response calculation. This property will be silently ignored unless "selection_method" = "FREQRANGE".

- `frequency_range` — Set the frequency_range of this MODESELECT

#### `setInclude_exclude_modes(include_exclude_modes: int) -> None`
Sets a property used to define whether the modes defined on the "selected_mode" or "selected_mode_set" properties will be forcefully INCLUDED or EXCLUDED from the simulation This property may be assigned either one of the following values, 1 - The modes will be unconditionally INCLUDED -1 - The modes will be unconditionally EXCLUDED.

- `include_exclude_modes` — Set the include_exclude_modes of this MODESELECT

#### `setLowest(lowest: int) -> None`
Sets specifies, using a positive integer) the number of modes that will be used in the calculation of the dynamic response. The value specified here will select all modes sequentially from the lowest available mode up to the mode number specified here. This property will be silently ignored unless "selection_method" = "LOWEST".

- `lowest` — Set the lowest of this MODESELECT

#### `setMod_eff_mass_frac(mod_eff_mass_frac: [( str,float )]) -> None`
Sets specifies which modes will be used in the dynamic response calculation using threshold values of modal effective mass fraction. Different threshold values may be assigned to each of the three translational and three rotational degrees of freedom. Any modes with effective mass fractions greater than the specified values will be selected and included in the dynamic response. Each component and it's optional associated threshold value is defined using a heterogeneous list which may contain one or two items. The first item in the list identifies a degree of freedom using one of the following strings, "T1FR" - translation degree of freedom 1 "T2FR" - translation degree of freedom 2 "T3FR" - translation degree of freedom 3 "R1FR" - rotational degree of freedom 1 "R2FR" - rotational degree of freedom 2 "R3FR" - rotational degree of freedom 3 "ALLFR" - all degrees of freedom not explicitly defined above The second item in the list is an optional value that defines the threshold mass fraction for the associated degree of freedom. The mass fraction must be assigned a floating point value greater than 0.0 and less than or equal to 1.0 If the second value (mass fraction) is omitted (or set to None) Nastran will assign a default mass fraction value Multiple degrees of freedom, each with potentially different mass fraction thresholds may be assigned this property using a list of lists where each internal list represents a single degree of freedom with an optional mass fraction value. If a degree of freedom is provided more than once in this property, the second value will be used and any preceding values will be silently ignored. An example of a valid input for this property is shown below, [["T1FR", 0.9],["T2FR",], ["T3FR", None], ["R3FR", 0.85]] This example will cause the following output to the Nastran file for this command MODESELECT (T1FR = 0.90 T2FR T3FR R3FR = 0.85) This property will be silently ignored unless "selection_method" = "MODEFFMASS".

- `mod_eff_mass_frac` — Set the mod_eff_mass_frac of this MODESELECT

#### `setMode_range(mode_range: [int]) -> None`
Sets specifies, using a list of two positive integers, the lower and upper limits of a range of mode numbers that will be used in the calculation of the dynamic response. All modes with numbers between and including the first and second values in this list will be selected and used in the dynamic response calculation. This property will be silently ignored unless "selection_method" = "MODERANGE".

- `mode_range` — Set the mode_range of this MODESELECT

#### `setSelected_mode_include_exclude(selected_mode_include_exclude: int) -> None`
Sets specifies the ID of a single mode that will be INCLUDED or EXCLUDED from the simulation base on the value of the "include_exclude_modes" property.

- `selected_mode_include_exclude` — Set the selected_mode_include_exclude of this MODESELECT

#### `setSelected_mode_set_include_excldue(selected_mode_set_include_excldue: int) -> None`
Sets specifies the ID of a ScenarioSetModeId that defines the IDs of one or more modes selected for inclusion or exclusion from the simulation. The modes selected here will either be INCLUDED or EXCLUDED based on the value of the include_exclude_modes property This property is only valid when the "selection"method" property is set to "USER".

- `selected_mode_set_include_excldue` — Set the selected_mode_set_include_excldue of this MODESELECT

#### `setSelection_method(selection_method: str) -> None`
Sets specifies which one of five different methods will be used to select modes This property may be assigned any one of the following values, "USER" - user defined mode numbers will selected "LOWEST" - the specified number of lowest modes will be selected "MODERANGE" - modes will be selected based on mode number range "FREQRANGE" - modes will be selected based on frequency range "MODEFFMASS" - modes will be selected based on modal effective mass fraction.

- `selection_method` — Set the selection_method of this MODESELECT

#### `setThreshold_method(threshold_method: str) -> None`
Sets specifies how the model effective mass fraction thresholds specified using the "mod_eff_mass_fraction" property are used to select modes This property may be assigned any one of the following values, "SUM" - modes will be selected by first sorting them in descending order of the corresponding modal effective mass fraction values. Then, starting from the first mode in this sorted list, the modes are selected until the sum of corresponding MEFFMFRA values equals or just exceeds the threshold value for that component None - same as "SUM" with the exception that this field will not be written to the Nastran file for this MODESELECT command. ("SUM" is the Nastran default value for this field) "ANYMIN" - Any mode whose modal effective mass fraction for any specified component equals or exceeds the threshold value for that component will be selected. "ALLMIN" - Any mode whose modal effective mass fraction for all of the specified components equals or exceeds the corresponding threshold values for those components will be selected. This property will be silently ignored unless "selection_method" = "MODEFFMASS".

- `threshold_method` — Set the threshold_method of this MODESELECT


## `apex.studies.MONITOR`  (extends `ScenarioCommand`)
Class representing a Nastran MONITOR case control command. MONITOR commands are to define options for printing of monitor point data. Properties on this class enable selection of the desired format of complex data and inclusion/exclusion of monitor point data by monitor point type.
Properties: `complex_form`, `noprint_mondsp1`, `noprint_monpnt1`, `noprint_monpnt2`, `noprint_monpnt3`, `value`

Methods:

- `getComplex_form() -> str` — Gets optional property defining the form of complex output from monitor point data. This property may be set to "REAL" or "IMAGINARY" and both values cause the complex monitor point data to be exported in rectangular format "REAL" - complex data will be written in rectangular (real, imaginary) format "IMAG" - same as "REAL" "PHASE" - complex data will be written in polar format (magnitude, phase) format None - same as "REAL" with the exception that this field of the MONITOR command will NOT be written to the Nastran file - Nastran by default will write complex monitor point data in rectangular format. Assigning any values other than the ones described above will cause Apex to raise an exception when this object is assigned to a load case item.
- `getNoprint_mondsp1() -> str` — Gets optional property to enable/disable printing of monitor point data from MONDSP1 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONDSP1 monitor points Setting this property to "NODSP1" will disable output of data from MONDSP1 monitor points.
- `getNoprint_monpnt1() -> str` — Gets optional property to enable/disable printing of monitor point data from MONPNT1 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONPNT1 monitor points Setting this property to "NOPNT1" will disable output of data from MONPNT1 monitor points.
- `getNoprint_monpnt2() -> str` — Gets optional property to enable/disable printing of monitor point data from MONPNT2 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONPNT2 monitor points Setting this property to "NOPNT2" will disable output of data from MONPNT2 monitor points.
- `getNoprint_monpnt3() -> str` — Gets optional property to enable/disable printing of monitor point data from MONPNT3 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONPNT3 monitor points Setting this property to "NOPNT3" will disable output of data from MONPNT3 monitor points.
- `getValue() -> str` — Gets property to enable or disable output of monitor point data This property supports the following value assignment, 'ALL' (Default) - enables output of all monitor points according to the options set for other properties of this MIONTOR command 'NONE' - disables output of all monitor point data.
#### `setComplex_form(complex_form: str) -> None`
Sets optional property defining the form of complex output from monitor point data. This property may be set to "REAL" or "IMAGINARY" and both values cause the complex monitor point data to be exported in rectangular format "REAL" - complex data will be written in rectangular (real, imaginary) format "IMAG" - same as "REAL" "PHASE" - complex data will be written in polar format (magnitude, phase) format None - same as "REAL" with the exception that this field of the MONITOR command will NOT be written to the Nastran file - Nastran by default will write complex monitor point data in rectangular format. Assigning any values other than the ones described above will cause Apex to raise an exception when this object is assigned to a load case item.

- `complex_form` — Set the complex_form of this MONITOR

#### `setNoprint_mondsp1(noprint_mondsp1: str) -> None`
Sets optional property to enable/disable printing of monitor point data from MONDSP1 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONDSP1 monitor points Setting this property to "NODSP1" will disable output of data from MONDSP1 monitor points.

- `noprint_mondsp1` — Set the noprint_mondsp1 of this MONITOR

#### `setNoprint_monpnt1(noprint_monpnt1: str) -> None`
Sets optional property to enable/disable printing of monitor point data from MONPNT1 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONPNT1 monitor points Setting this property to "NOPNT1" will disable output of data from MONPNT1 monitor points.

- `noprint_monpnt1` — Set the noprint_monpnt1 of this MONITOR

#### `setNoprint_monpnt2(noprint_monpnt2: str) -> None`
Sets optional property to enable/disable printing of monitor point data from MONPNT2 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONPNT2 monitor points Setting this property to "NOPNT2" will disable output of data from MONPNT2 monitor points.

- `noprint_monpnt2` — Set the noprint_monpnt2 of this MONITOR

#### `setNoprint_monpnt3(noprint_monpnt3: str) -> None`
Sets optional property to enable/disable printing of monitor point data from MONPNT3 monitor points. Omitting this property (setting to None) will cause Nastran to output data from MONPNT3 monitor points Setting this property to "NOPNT3" will disable output of data from MONPNT3 monitor points.

- `noprint_monpnt3` — Set the noprint_monpnt3 of this MONITOR

#### `setValue(value: str) -> None`
Sets property to enable or disable output of monitor point data This property supports the following value assignment, 'ALL' (Default) - enables output of all monitor points according to the options set for other properties of this MIONTOR command 'NONE' - disables output of all monitor point data.

- `value` — Set the value of this MONITOR


## `apex.studies.MeshlessGenerativeDesignStep`  (extends `Step`)
MeshlessGenerativeDesignStep is used to define the calculation of the linear buckling modes of a system.

Methods:

#### `addEvent(name: str = "") -> apex.studies.Event`
Adds an Event to this Step using the supplied name and returns the Event. The Event name must be unique within the Step. If an Event with the same name already exists within the Step the system will automatically modify the supplied name to make it unique.

- `name` — The name that will be assigned to the Event created by this method

Returns: Event object

#### `duplicateEvent(event: Event) -> apex.studies.Event`
duplicate a new Event from the given one.

- `event` — The given child event of current Step

Returns: returns an single Event in a Step

#### `getSimulationSettings() -> apex.studies.SimulationSettingsGenerativeDesign`
returns the simulation settings from this scenario

Returns: the simulationSettings object


## `apex.studies.ModalFrequencyStep`  (extends `DynamicsStep`)
ModalFrequencyStep is used to calculate the frequency response of a system. This Step must be preceded by a ModesStep.

## `apex.studies.ModesSimulationSettings`  (extends `SimulationSettings`)
This class manages the simulation settings for Normal Modes Simulation Steps. An instance of this class is created and populated with default values whenever a Normal Modes Step is created.
Properties: `freqRangeLower`, `freqRangeUpper`, `interactionControl`, `maxModes`

Methods:

- `getFreqRangeLower() -> float`
- `getFreqRangeUpper() -> float`
- `getInteractionControl() -> apex.studies.InteractionControl`
- `getMaxModes() -> int`
- `setFreqRangeLower(freqRangeLower: float) -> None`
- `setFreqRangeUpper(freqRangeUpper: float) -> None`
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None`
- `setMaxModes(maxModes: int) -> None`

## `apex.studies.ModesStep`  (extends `Step`)
ModesStep is used to define calculation of the normal modes of a system.

Methods:

#### `getSimulationSettings() -> apex.studies.ModesSimulationSettings`
returns the ModesSimulationSettings from this apex.studie.Scenario

Returns: the ModesSimulationSettings object

#### `setMNFOptions(mnfGenerationProperties: apex.studies.MNFGenerationProperty) -> None`
Configures the Step to include calculation and export of a Modal Neutral File for use in Adams multi-body dynamics simulations. Parameter to control the modal neutral file calculation and export are supplied as arguments.

- `mnfGenerationProperties` — An MNFGenerationProperties object describing the options that will be used to generate and output the MNF. See the documentation for MNFGenerationProperties for further details


## `apex.studies.MultiBodyTransientStep`  (extends `DynamicsStep`)
MultiBodyTransientStep is used to define the calculation of the Multi-Body Transient of a system.

Methods:

#### `addEvent(name: str = "") -> apex.studies.Event`
Adds an Event to this Step using the supplied name and returns the Event. The Event name must be unique within the Step. If an Event with the same name already exists within the Step the system will automatically modify the supplied name to make it unique.

- `name` — The name that will be assigned to the Event created by this method

Returns: Event object

#### `duplicateEvent(event: Event) -> apex.studies.Event`
duplicate a new Event from the given one.

- `event` — The given child event of current Step

Returns: returns an single Event in a Step

- `getEndTime() -> float` — Get the end time duration of the simulation.
- `getOutputFrequency() -> float` — Get the output frequency in the simulation.
- `getOutputStepSize() -> float` — Get the output step size in the simulation.
- `getOutputSteps() -> int` — Get the number of output steps in the simulation.
#### `getSimulationSettings() -> apex.studies.SimulationSettings`
returns the simulation settings from this scenario

Returns: the simulationSettings object

#### `update(simulationType: int = 0, endTime: float = NAN, outputSteps: int = 0, outputStepSize: float = NAN, outputFrequency: float = NAN) -> None`
Modifies one or more parameters of the Scenario.

- `simulationType` — Simulation type of the simulation, Dynamic or QuasiStatic.
- `endTime` — End time duration of the simulation .
- `outputSteps` — Number of output steps in the simulation.
- `outputStepSize` — Output step size in the simulation.
- `outputFrequency` — Output frequency in the simulation.


## `apex.studies.NLBUCK`  (extends `ScenarioCommand`)
Class representing a Nastran "NLBUCK" case control command The NLBUCK command is used to request a nonlinear buckling analysis in Solution 400.
Properties: `value`

Methods:

- `getValue() -> str` — Gets property used to control when nonlinear buckling analyses will be carried out during a Solution 400 analysis This property may be assigned any one of the following values, "END" - requests a buckling analysis at the end of the STEP with which this NLBUCK command is associated None - same as "END" wit the exception that this field will not be written to the Nastran file as part of the NLBUCK command ("END" is the Nastran default value for this field) "ALL" - a buckling analysis will be carried out at the end of each converged load increment within the STEP with which this NLBUCK command is associated r - any positive integer. A buckling analysis will be carried out every "rth" converged load increment AND at the final converged load increment.
#### `setValue(value: str) -> None`
Sets property used to control when nonlinear buckling analyses will be carried out during a Solution 400 analysis This property may be assigned any one of the following values, "END" - requests a buckling analysis at the end of the STEP with which this NLBUCK command is associated None - same as "END" wit the exception that this field will not be written to the Nastran file as part of the NLBUCK command ("END" is the Nastran default value for this field) "ALL" - a buckling analysis will be carried out at the end of each converged load increment within the STEP with which this NLBUCK command is associated r - any positive integer. A buckling analysis will be carried out every "rth" converged load increment AND at the final converged load increment.

- `value` — Set the value of this NLBUCK


## `apex.studies.NLIC`  (extends `ScenarioCommand`)
Class representing a Nastran "NLIC" case control command The NLIC command is used to select a previously executed load increment as the initial state for a nonlinear or perturbation STEP in Solution 400.
Properties: `loadfact`, `step`, `subcase`, `time`, `usage_tolerance`

Methods:

- `getLoadfact() -> float` — Gets specifies the load factor (or time) within the previously selected Subcase or Step at which the initial state was calculated.
- `getStep() -> int` — Gets specifies the positive integer ID of an existing STEP in which the initial state is calculated This property may be assigned either of the following values, n - positive integer ID of an existing Step within the Subcase identified by the "subcase" property. None - has the same behavior as setting this property to the ID of the last Step in the selected subcase with the exception that this field will not be written to the Nastran file for this NLIC command. (By default Nastran will use the last Step in the selected Subcase)
- `getSubcase() -> int` — Gets specify the positive integer ID of the existing Subcase in which the initial state is calculated This property may be assigned either of the following values, n - positive integer ID of an existing Subcase. The referenced Subcase must appear before the Subcase with which this NLIC command is associated None - has the same behavior as setting this property to the ID of the Subcase with which this NLIC command is associated with the exception that this field will not be written to the Nastran file for this NLIC command. (By default Nastran will use the Subcase with which the NLIC command is associated)
- `getTime() -> float` — Gets specifies the time (or load factor) within the previously selected Subcase or Step at which the initial state was calculated.
- `getUsage_tolerance() -> str` — Gets specify whether the nearest time/load factor to the specified value should be used irrespective of how far it is from an available value or if it should only be used if it's within a defined tolerance This property may be assigned any one of the following values, "NEAR" - Use the state at the load factor or time nearest to the value specified by "loadfact" no matter how far away it is from the specified value 'tol' - a floating point value that defines a tolerance about the specific loadfact. An available value will be used only if it is within this tolerance of loadfact None - has the same effect as setting tol=1.0E-6 with the exception that this field will not be written to the Nastran file for this NLIC command. (1.0E-6 is the Nastran default value for this field)
#### `setLoadfact(loadfact: float) -> None`
Sets specifies the load factor (or time) within the previously selected Subcase or Step at which the initial state was calculated.

- `loadfact` — Set the loadfact of this NLIC

#### `setStep(step: int) -> None`
Sets specifies the positive integer ID of an existing STEP in which the initial state is calculated This property may be assigned either of the following values, n - positive integer ID of an existing Step within the Subcase identified by the "subcase" property. None - has the same behavior as setting this property to the ID of the last Step in the selected subcase with the exception that this field will not be written to the Nastran file for this NLIC command. (By default Nastran will use the last Step in the selected Subcase)

- `step` — Set the step of this NLIC

#### `setSubcase(subcase: int) -> None`
Sets specify the positive integer ID of the existing Subcase in which the initial state is calculated This property may be assigned either of the following values, n - positive integer ID of an existing Subcase. The referenced Subcase must appear before the Subcase with which this NLIC command is associated None - has the same behavior as setting this property to the ID of the Subcase with which this NLIC command is associated with the exception that this field will not be written to the Nastran file for this NLIC command. (By default Nastran will use the Subcase with which the NLIC command is associated)

- `subcase` — Set the subcase of this NLIC

#### `setTime(time: float) -> None`
Sets specifies the time (or load factor) within the previously selected Subcase or Step at which the initial state was calculated.

- `time` — Set the time of this NLIC

#### `setUsage_tolerance(usage_tolerance: str) -> None`
Sets specify whether the nearest time/load factor to the specified value should be used irrespective of how far it is from an available value or if it should only be used if it's within a defined tolerance This property may be assigned any one of the following values, "NEAR" - Use the state at the load factor or time nearest to the value specified by "loadfact" no matter how far away it is from the specified value 'tol' - a floating point value that defines a tolerance about the specific loadfact. An available value will be used only if it is within this tolerance of loadfact None - has the same effect as setting tol=1.0E-6 with the exception that this field will not be written to the Nastran file for this NLIC command. (1.0E-6 is the Nastran default value for this field)

- `usage_tolerance` — Set the usage_tolerance of this NLIC


## `apex.studies.NLOPRM`  (extends `ScenarioCommand`)
Class representing a Nastran "NLOPRM" case control command The NLOPRM command is used to control nonlinear solution output.
Properties: `contact_punch`, `debug_control`, `debug_post`, `delimit`, `grid_output`, `output_control`

Methods:

- `getContact_punch() -> str` — Gets property used to select which contact constraint output options are written to the punch file This property may be assigned any on of the following values, "NONE" - No MPC or MPCY output will be written to the punch file None - same as "NONE" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NONE" is the Nastran default value for this field) any combination of the following values as a list of strings, "BEGN" - MPC data will be written to the punch file at the start of the first iteration "OTIME" - MPC data will be written to the punch file at every user requested output STEP "STEP" - MPC data will be written to the punch file at the end of every SUBCASE, STEP and SUBSTEP any combination of the following values as a list of strings, "YBEGN" - MPCY data will be written to the punch file at the start of the first iteration "YOTIME" - MPCY data will be written to the punch file at every user requested output STEP "YSTEP" - MPCY data will be written to the punch file at the end of every SUBCASE, STEP and SUBSTEP.
- `getDebug_control() -> str` — Gets property used to specify printed output of debug data. This property may be assigned any one of the following values, "NONE" - No debug output will be printed None - same as "NONE" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NONE" is the Nastran default value for this field) any combination of the following values as list of strings "NLBASIC" - Basic nonlinear infromation will be printed "NRDBG" - Newton-Raphson iteration information will be printed "ADVDBG" - Advanced nonlinear information will be printed Any one of the following "N3DBASE" - Contact error tolerance will be printed "N3DMED" - A summary table of all contact information including the output produced using "N3DBASE" "N3DADV" - All contact body information plus the output produced using "N3DBASE" and "N3DMED" "N3DSUM" - Simplified contact data (w.r.t. the output produced using "N3DADV")
- `getDebug_post() -> str` — Gets property used to specify debug POST output options This property may be assigned any one of the following values, "NONE" - No post output None - same as "NONE" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NONE" is the Nastran default value for this field) "LTIME" - output will be written for all iterations in the last load/time increment "LSTEP" - output will be written for all iterations in the last STEP "LSUBC" - output will be written for all iterations in the last SUBCASE "ALL" - output will be written for all iterations.
- `getDelimit() -> str` — Gets specifies whether or not DELIMIT output is written to the punch file Ths property may be assigned any one of the following values, "NO" - no delimiters will be output None - same as "NO" wit the exception that this field will not be written to the Nastran file for this NLOPRM command ("NO" is the Nastran default value for this field "YES" - delimiters will be output.
- `getGrid_output() -> str` — Gets specifies which grid point information will be written to the punch file This property may be assigned any one of the following values, "NO" - No grid point infromation will be written None - same as "NO" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NO" is the Nastran default value for this field) "MAXGRID" - grid point information will be written only for the Grid with the maximum displacement n - the positive integer ID of an exiting GRID. grid point information will be written only for the Grid with ID=n.
- `getOutput_control() -> str` — Gets property used to specify nonlinear solution output options This property may be assigned either of the following values, any combination of the following values as a list of strings, "STD" - Standard nastran output "SOLUTION" - Solution set output which does include superelement output "INTERM" - intermediate nonlinear solution output None - Same a "STD" with the exception that this command field will not be written to the Nastran file for this NLOPRM command ("STD is the Nastran default value for this field)
#### `setContact_punch(contact_punch: str) -> None`
Sets property used to select which contact constraint output options are written to the punch file This property may be assigned any on of the following values, "NONE" - No MPC or MPCY output will be written to the punch file None - same as "NONE" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NONE" is the Nastran default value for this field) any combination of the following values as a list of strings, "BEGN" - MPC data will be written to the punch file at the start of the first iteration "OTIME" - MPC data will be written to the punch file at every user requested output STEP "STEP" - MPC data will be written to the punch file at the end of every SUBCASE, STEP and SUBSTEP any combination of the following values as a list of strings, "YBEGN" - MPCY data will be written to the punch file at the start of the first iteration "YOTIME" - MPCY data will be written to the punch file at every user requested output STEP "YSTEP" - MPCY data will be written to the punch file at the end of every SUBCASE, STEP and SUBSTEP.

- `contact_punch` — Set the contact_punch of this NLOPRM

#### `setDebug_control(debug_control: str) -> None`
Sets property used to specify printed output of debug data. This property may be assigned any one of the following values, "NONE" - No debug output will be printed None - same as "NONE" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NONE" is the Nastran default value for this field) any combination of the following values as list of strings "NLBASIC" - Basic nonlinear infromation will be printed "NRDBG" - Newton-Raphson iteration information will be printed "ADVDBG" - Advanced nonlinear information will be printed Any one of the following "N3DBASE" - Contact error tolerance will be printed "N3DMED" - A summary table of all contact information including the output produced using "N3DBASE" "N3DADV" - All contact body information plus the output produced using "N3DBASE" and "N3DMED" "N3DSUM" - Simplified contact data (w.r.t. the output produced using "N3DADV")

- `debug_control` — Set the debug_control of this NLOPRM

#### `setDebug_post(debug_post: str) -> None`
Sets property used to specify debug POST output options This property may be assigned any one of the following values, "NONE" - No post output None - same as "NONE" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NONE" is the Nastran default value for this field) "LTIME" - output will be written for all iterations in the last load/time increment "LSTEP" - output will be written for all iterations in the last STEP "LSUBC" - output will be written for all iterations in the last SUBCASE "ALL" - output will be written for all iterations.

- `debug_post` — Set the debug_post of this NLOPRM

#### `setDelimit(delimit: str) -> None`
Sets specifies whether or not DELIMIT output is written to the punch file Ths property may be assigned any one of the following values, "NO" - no delimiters will be output None - same as "NO" wit the exception that this field will not be written to the Nastran file for this NLOPRM command ("NO" is the Nastran default value for this field "YES" - delimiters will be output.

- `delimit` — Set the delimit of this NLOPRM

#### `setGrid_output(grid_output: str) -> None`
Sets specifies which grid point information will be written to the punch file This property may be assigned any one of the following values, "NO" - No grid point infromation will be written None - same as "NO" with the exception that this field will not be written to the Nastran file for this NLOPRM command ("NO" is the Nastran default value for this field) "MAXGRID" - grid point information will be written only for the Grid with the maximum displacement n - the positive integer ID of an exiting GRID. grid point information will be written only for the Grid with ID=n.

- `grid_output` — Set the grid_output of this NLOPRM

#### `setOutput_control(output_control: str) -> None`
Sets property used to specify nonlinear solution output options This property may be assigned either of the following values, any combination of the following values as a list of strings, "STD" - Standard nastran output "SOLUTION" - Solution set output which does include superelement output "INTERM" - intermediate nonlinear solution output None - Same a "STD" with the exception that this command field will not be written to the Nastran file for this NLOPRM command ("STD is the Nastran default value for this field)

- `output_control` — Set the output_control of this NLOPRM


## `apex.studies.NLSTEP`  (extends `ScenarioCommand`)
Class representing a Nastran NLSTEP case control command. The NLSTEP command is used to select integration and output time steps for static and transient nonlinear analyses in Solution 400. The actual integration and time step data is defined on an NLSTEP bulk antry and the ID of that entry is defined here.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of NLSTEP bulk entry Use this command to assign integration and time step data to a nonlinear static and transient Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets the ID of NLSTEP bulk entry Use this command to assign integration and time step data to a nonlinear static and transient Subcase, Step or Substep.

- `value` — Set the value of this NLSTEP


## `apex.studies.NSM`  (extends `ScenarioCommand`)
Class representing a Nastran NSM case control command. NSM commands are used to select one or more non-structural masses defined using NMS, NSML, NSM1, NSML1 or NSMADD entries, assigned to the model, for inclusion in a LoadCaseItem. Non structural masses are identified by their ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of one or more NMS, NSML, NSM1, NSML1 or NSMADD entries assigned to the model referenced by the Scenario that this command is composed by Use this command to assign a non-structural masses to a Scenario, Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets the ID of one or more NMS, NSML, NSM1, NSML1 or NSMADD entries assigned to the model referenced by the Scenario that this command is composed by Use this command to assign a non-structural masses to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this NSM


## `apex.studies.NastranSol400StepSettings`
A base class for Nastran 400 step setting.

## `apex.studies.NastranSol400StepSettingsStatic`  (extends `NastranSol400StepSettings`)
A class to define static step setting for nastran Sol400.
Properties: `id`, `incrementalScheme`, `incrementalSchemeAdaptive`, `incrementalSchemeArcLength`, `incrementalSchemeFixed`, `iterationsAndConvergence`, `predefinedOption`, `stepSettingMethod`

Methods:

#### `NastranSol400StepSettingsStatic(id: int, stepSettingMethod: apex.studies.StepSettingMethod, predefinedOption: apex.studies.PredefinedOption, incrementalScheme: apex.studies.IncrementalScheme, incrementalSchemeFixed: apex.studies.IncrementalSchemeFixed, incrementalSchemeAdaptive: apex.studies.IncrementalSchemeAdaptive, incrementalSchemeArcLength: apex.studies.IncrementalSchemeArcLength, iterationsAndConvergence: apex.studies.IterationAndConvergence) -> None`
Constructor for Nastran s400 static step simulation setting.

- `id` — Optional-id of the step setting.
- `stepSettingMethod` — Optional-Step setting using "Smart' or "Advanced" to define increment, iteration and convergence settings. If "Smart" is used, two arguments are available : "incrementalScheme" and "predefinedOption". If "Advanced" is used, the following arguments are available : "incrementalScheme" and "incrementalSchemeFixed","incrementalSchemeAdaptive", incrementalSchemeArcLength" and "iterationsAndConvergence".
- `predefinedOption` — Optional-The severity of the nonlinear present in this Step.
- `incrementalScheme` — Optional-Incremental Scheme to be used for this step.
- `incrementalSchemeFixed` — Optional-The step properties of Incremental Scheme = Fixed.
- `incrementalSchemeAdaptive` — Optional-The step properties of Incremental Scheme = Adaptive.
- `incrementalSchemeArcLength` — Optional-The step properties of Incremental Scheme = ArcLength.
- `iterationsAndConvergence` — Optional-Iteration and convergence setting for the step.

- `getId() -> int` — id of the step setting.
- `getIncrementalScheme() -> apex.studies.IncrementalScheme` — Incremental Scheme to be used for this step.
- `getIncrementalSchemeAdaptive() -> apex.studies.IncrementalSchemeAdaptive` — The step properties of Incremental Scheme = Adaptive.
- `getIncrementalSchemeArcLength() -> apex.studies.IncrementalSchemeArcLength` — The step properties of Incremental Scheme = ArcLength.
- `getIncrementalSchemeFixed() -> apex.studies.IncrementalSchemeFixed` — The step properties of Incremental Scheme = Fixed.
- `getIterationsAndConvergence() -> apex.studies.IterationAndConvergence` — Iteration and convergence setting for the step.
- `getPredefinedOption() -> apex.studies.PredefinedOption` — The severity of the nonlinear present in this Step.
- `getStepSettingMethod() -> apex.studies.StepSettingMethod` — Step setting using "Smart' or "Advanced" to define increment, iteration and convergence settings. If "Smart" is used, two arguments are available : "incrementalScheme" and "predefinedOption". If "Advanced" is used, the following arguments are available : "incrementalScheme" and "incrementalSchemeFixed","incrementalSchemeAdaptive", incrementalSchemeArcLength" and "iterationsAndConvergence".
#### `update(id: int, stepSettingMethod: apex.studies.StepSettingMethod, predefinedOption: apex.studies.PredefinedOption, incrementalScheme: apex.studies.IncrementalScheme, incrementalSchemeFixed: apex.studies.IncrementalSchemeFixed, incrementalSchemeAdaptive: apex.studies.IncrementalSchemeAdaptive, incrementalSchemeArcLength: apex.studies.IncrementalSchemeArcLength, iterationsAndConvergence: apex.studies.IterationAndConvergence) -> None`
Update Nastran s400 static step simulation setting.

- `id` — Optional-id of the step setting.
- `stepSettingMethod` — Optional-Step setting using "Smart' or "Advanced" to define increment, iteration and convergence settings. If "Smart" is used, two arguments are available : "incrementalScheme" and "predefinedOption". If "Advanced" is used, the following arguments are available : "incrementalScheme" and "incrementalSchemeFixed","incrementalSchemeAdaptive", incrementalSchemeArcLength" and "iterationsAndConvergence".
- `predefinedOption` — Optional-The severity of the nonlinear present in this Step.
- `incrementalScheme` — Optional-Incremental Scheme to be used for this step.
- `incrementalSchemeFixed` — Optional-The step properties of Incremental Scheme = Fixed.
- `incrementalSchemeAdaptive` — Optional-The step properties of Incremental Scheme = Adaptive.
- `incrementalSchemeArcLength` — Optional-The step properties of Incremental Scheme = ArcLength.
- `iterationsAndConvergence` — Optional-Iteration and convergence setting for the step.


## `apex.studies.ODSFREQ`  (extends `ScenarioCommand`)
Class representing the Nastran "ODSFREQ" case control command The ODSFREQ command is used to select excitation frequencies for Operational Deformed Shape output.
Properties: `value`

Methods:

- `getValue() -> str` — Gets a property used to identify the ScenarioSetFrequency containing frequency values that will be used to generate ODS output This property may be assigned the ID of any existing ScenarioSetFrequency.
#### `setValue(value: str) -> None`
Sets a property used to identify the ScenarioSetFrequency containing frequency values that will be used to generate ODS output This property may be assigned the ID of any existing ScenarioSetFrequency.

- `value` — Set the value of this ODSFREQ


## `apex.studies.OFREQUENCY`  (extends `ScenarioCommand`)
Class representing a Nastran "OFREQUENCY" case control command The OFREQUENCY command is used to select a set of frequencies for output requests.
Properties: `value`

Methods:

- `getValue() -> str` — Gets a property used to identify the ScenarioSetFrequency containing frequency values that will be used to generate output requests This property may be assigned the ID of any existing ScenarioSetFrequency.
#### `setValue(value: str) -> None`
Sets a property used to identify the ScenarioSetFrequency containing frequency values that will be used to generate output requests This property may be assigned the ID of any existing ScenarioSetFrequency.

- `value` — Set the value of this OFREQUENCY


## `apex.studies.OMODES`  (extends `ScenarioCommand`)
Class representing a Nastran "OMODES" case control command The OMODES command is used to select a set of Modes for output requests.
Properties: `value`

Methods:

- `getValue() -> str` — Gets a property used to identify the ScenarioSetModeId containing IDs of the Modes that will be used to generate output requests This property may be assigned the ID of any existing ScenarioSetModeId.
#### `setValue(value: str) -> None`
Sets a property used to identify the ScenarioSetModeId containing IDs of the Modes that will be used to generate output requests This property may be assigned the ID of any existing ScenarioSetModeId.

- `value` — Set the value of this OMODES


## `apex.studies.OTIME`  (extends `ScenarioCommand`)
Class representing the Nastran "OTIME" case control command The OTIME command is used to specify the set of time points at which output requests will be written during transient analysis.
Properties: `value`

Methods:

- `getValue() -> str` — Gets a property used to identify the ScenarioSetTime containing the time values that will be used to generate output data This property may be assigned the ID of any existing ScenarioSetTime.
#### `setValue(value: str) -> None`
Sets a property used to identify the ScenarioSetTime containing the time values that will be used to generate output data This property may be assigned the ID of any existing ScenarioSetTime.

- `value` — Set the value of this OTIME


## `apex.studies.PAGE`  (extends `ScenarioCommand`)
Class representing a Nastran "PAGE" case control command. The PAGE command is used to force subsequent case control commands to be written on a new page in the echo of the Nastran case control section.

## `apex.studies.PARTN`  (extends `ScenarioCommand`)
Class representing a Nastran PARTN case control command. Defines the ID of a ScenarioSetNastranGrid that in turn defines a list of grid point IDs that will be partitioned with the DMAP module MATMOD to generate a partitioning vector for use in DMAP modules such as PARTN and MERGE.
Properties: `value`

Methods:

- `getValue() -> int` — Gets a property used to identify the ScenarioSetGridId containing IDs of the Nodes that will be used to generate the partitioning vector This property may be assigned the ID of any existing ScenarioSetGridId.
#### `setValue(value: int) -> None`
Sets a property used to identify the ScenarioSetGridId containing IDs of the Nodes that will be used to generate the partitioning vector This property may be assigned the ID of any existing ScenarioSetGridId.

- `value` — Set the value of this PARTN


## `apex.studies.PEAKOUT`  (extends `ScenarioCommand`)
Class representing a Nastran "PEAKOUT" case control command The PEAKOUT command is used to control peak identification in frequency response analysis.
Properties: `acoustic_dofs`, `min_peak_separation`, `number_of_peaks`, `peak_highest`, `peak_lowest`, `peak_quantity`, `peak_scale_method`, `structural_dofs`

Methods:

- `getAcoustic_dofs() -> int` — Gets a positive integer identifying the ID of a an existing ScenarioSetGridId that defines a set of acoustic degrees of freedom from which the peaks are extracted. If this property is omitted (set to None) no search for acoustic peaks will be carried out.
- `getMin_peak_separation() -> float` — Gets optional property (Default None) used to define the minimum allowed frequency between two peaks. This property may be assigned the following values, any positive real number. This value represents the minimum frequency allowed between extracted peaks None - defines a minimum peak separation frequency of 0.01Hz. Setting this value to None will disable writing of this field/value to the Nastran file for this command - 0.01Hz is the Nastran default for minimum peak separation frequency.
- `getNumber_of_peaks() -> int` — Gets optional property used to specify the number of peaks to extract.
- `getPeak_highest() -> float` — Gets defines the highest frequency used in peak identification. This property may be assigned the following values, any positive real number. This value will be used to define the highest frequency peak that will be extracted None - Causes Nastran to use the higher of 1.0E10Hz OR the highest forcing frequency value as the maximum frequency used for peak identification.
- `getPeak_lowest() -> float` — Gets defines the lowest frequency used in peak identification. This property may be assigned the following values, any positive real number. This value will be used to define the lowest frequency peak that will be extracted None - Causes Nastran to use the lower of 0.0Hz OR the lowest forcing frequency value as the minimum frequency used for peak identification.
- `getPeak_quantity() -> str` — Gets optional property (Default None)used to identify the result quantity that will be used to identify response peaks This property may be assigned any one of the following values, "DISP" - peaks will be identified using displacements None - same as "DISP", with the exception that his field will not be written to the Nastran file for this PEAKOUT command - "DISP" is the Nastran default value "VELO" - peaks will be identified using velocities "ACCE" - peaks will be identified using accelerations.
- `getPeak_scale_method() -> str` — Gets property used to define the scaling method for peak acoustic pressure identification in the fluid domain This property may be assigned any one of the following values, "NONE" - No scaling of acoustic pressures will be performed None - same as "NONE" with the exception that this field will not be written to the Nastran file for this command - "NONE" is the Nastran default value "DB" - Decibel scale "DBA" - "A" weighted decibel scale.
- `getStructural_dofs() -> int` — Gets a positive integer identify an existing ScenarioSetGridComponent that defines a set of structural degrees of freedom from which the peaks are extracted. If this property is omitted (set to None) no search for structural peaks will be carried out.
#### `setAcoustic_dofs(acoustic_dofs: int) -> None`
Sets a positive integer identifying the ID of a an existing ScenarioSetGridId that defines a set of acoustic degrees of freedom from which the peaks are extracted. If this property is omitted (set to None) no search for acoustic peaks will be carried out.

- `acoustic_dofs` — Set the acoustic_dofs of this PEAKOUT

#### `setMin_peak_separation(min_peak_separation: float) -> None`
Sets optional property (Default None) used to define the minimum allowed frequency between two peaks. This property may be assigned the following values, any positive real number. This value represents the minimum frequency allowed between extracted peaks None - defines a minimum peak separation frequency of 0.01Hz. Setting this value to None will disable writing of this field/value to the Nastran file for this command - 0.01Hz is the Nastran default for minimum peak separation frequency.

- `min_peak_separation` — Set the min_peak_separation of this PEAKOUT

#### `setNumber_of_peaks(number_of_peaks: int) -> None`
Sets optional property used to specify the number of peaks to extract.

- `number_of_peaks` — Set the number_of_peaks of this PEAKOUT

#### `setPeak_highest(peak_highest: float) -> None`
Sets defines the highest frequency used in peak identification. This property may be assigned the following values, any positive real number. This value will be used to define the highest frequency peak that will be extracted None - Causes Nastran to use the higher of 1.0E10Hz OR the highest forcing frequency value as the maximum frequency used for peak identification.

- `peak_highest` — Set the peak_highest of this PEAKOUT

#### `setPeak_lowest(peak_lowest: float) -> None`
Sets defines the lowest frequency used in peak identification. This property may be assigned the following values, any positive real number. This value will be used to define the lowest frequency peak that will be extracted None - Causes Nastran to use the lower of 0.0Hz OR the lowest forcing frequency value as the minimum frequency used for peak identification.

- `peak_lowest` — Set the peak_lowest of this PEAKOUT

#### `setPeak_quantity(peak_quantity: str) -> None`
Sets optional property (Default None)used to identify the result quantity that will be used to identify response peaks This property may be assigned any one of the following values, "DISP" - peaks will be identified using displacements None - same as "DISP", with the exception that his field will not be written to the Nastran file for this PEAKOUT command - "DISP" is the Nastran default value "VELO" - peaks will be identified using velocities "ACCE" - peaks will be identified using accelerations.

- `peak_quantity` — Set the peak_quantity of this PEAKOUT

#### `setPeak_scale_method(peak_scale_method: str) -> None`
Sets property used to define the scaling method for peak acoustic pressure identification in the fluid domain This property may be assigned any one of the following values, "NONE" - No scaling of acoustic pressures will be performed None - same as "NONE" with the exception that this field will not be written to the Nastran file for this command - "NONE" is the Nastran default value "DB" - Decibel scale "DBA" - "A" weighted decibel scale.

- `peak_scale_method` — Set the peak_scale_method of this PEAKOUT

#### `setStructural_dofs(structural_dofs: int) -> None`
Sets a positive integer identify an existing ScenarioSetGridComponent that defines a set of structural degrees of freedom from which the peaks are extracted. If this property is omitted (set to None) no search for structural peaks will be carried out.

- `structural_dofs` — Set the structural_dofs of this PEAKOUT


## `apex.studies.POST`  (extends `ScenarioCommand`)
Class used to represent a Nastran "POST" case control command. The POST command is used to control selection of data for output to the Nastran .op2 file for different post-processing products.
Properties: `enhanced_op2`, `post_processor`

Methods:

- `getEnhanced_op2() -> str` — Gets parameter used to control whether to export standard or enhanced .op2 formats to the .op2 file This property will be silently ignored unless "post_processor" is set to "PATRAN" This property accepts the following values, None (or omitted) the standard Nastran .op2 file format will be written "ENHOP2" - Enhanced .op2 file formats will be used.
- `getPost_processor() -> str` — Gets optional property used to identify which post-processor this command will target This property accepts any one of the following values, "PATRAN" - Patran None - Same as "PATRAN" except this field will not be written to the Nastran file for this command (PATRAN is the default post output) "SDRC" - Siemens IDEAS "NF" - LMS NF "FEMTOOLS" - DDS/FemTools "UNIGRAPHICS" - Siemens Unigraphics.
#### `setEnhanced_op2(enhanced_op2: str) -> None`
Sets parameter used to control whether to export standard or enhanced .op2 formats to the .op2 file This property will be silently ignored unless "post_processor" is set to "PATRAN" This property accepts the following values, None (or omitted) the standard Nastran .op2 file format will be written "ENHOP2" - Enhanced .op2 file formats will be used.

- `enhanced_op2` — Set the enhanced_op2 of this POST

#### `setPost_processor(post_processor: str) -> None`
Sets optional property used to identify which post-processor this command will target This property accepts any one of the following values, "PATRAN" - Patran None - Same as "PATRAN" except this field will not be written to the Nastran file for this command (PATRAN is the default post output) "SDRC" - Siemens IDEAS "NF" - LMS NF "FEMTOOLS" - DDS/FemTools "UNIGRAPHICS" - Siemens Unigraphics.

- `post_processor` — Set the post_processor of this POST


## `apex.studies.RANDOM`  (extends `ScenarioCommand`)
Class representing a Nastran RANDOM case control command The RANDOM command is used to select and assign power spectral density and time lag distribution for use in Random response analyses.
Properties: `value`

Methods:

- `getValue() -> int` — Gets required property used to select one or more RANDPS and/or RANDT1 entities that respectively define the power spectral density and time lag functions that will be used by the random analysis load case item that this RANDOM command is assigned to. This property may be assigned the following values, n - a single positive integer. This integer is used to select either, One or more RANDPS/RANDT1 entities with ID=n An existing Scenario SET with ID=n.
#### `setValue(value: int) -> None`
Sets required property used to select one or more RANDPS and/or RANDT1 entities that respectively define the power spectral density and time lag functions that will be used by the random analysis load case item that this RANDOM command is assigned to. This property may be assigned the following values, n - a single positive integer. This integer is used to select either, One or more RANDPS/RANDT1 entities with ID=n An existing Scenario SET with ID=n.

- `value` — Set the value of this RANDOM


## `apex.studies.RCROSS`  (extends `ScenarioCommand`)
Class representing a Nastran RCROSS case control command. The RCROSS command is used to activate computation and output of cross power spectral density and cross correlation functions in random analysis Properties of this class enable control of the random output and selection of the response quantities that will be used in the cross PSD and cross correlation function calculations.
Properties: `output_cross_corr`, `output_cross_psd`, `output_cross_psd_corr`, `output_format`, `output_print`, `output_punch`, `value`

Methods:

- `getOutput_cross_corr() -> str` — Gets property used to request calculation and output of the cross correlation function This property may be assigned the following values, 'CORF' - activates calculation and output of cross correlation function data None - DO NOT activate calculation and output of cross correlation function data.
- `getOutput_cross_psd() -> str` — Gets property used to request calculation and output of the cross power spectra; density function This property may be assigned the following values, 'PSDF' - requests calculation and output of cross power spectral density function data None - inhibits calculation and output of cross power spectral density function data.
- `getOutput_cross_psd_corr() -> str` — Gets property used to request calculation and output of both the cross power spectral density and cross correlation function This property may be assigned the following values, 'RALL' - activates calculation and output of both the cross power spectral density and cross correlation function None - DO NOT activate calculation and output of both the cross power spectral density and cross correlation function.
- `getOutput_format() -> str` — Gets optional property used to control the format of the complex output generated by this RCROSS command This property may be assigned the following values, 'REAL' - requests output of complex data in rectangular (real, imaginary)format 'IMAG' - same as 'REAL' None - equivalent to 'REAL' or 'IMAG' with the exception that this filed will not be written to the Nastran file. Omission of this field causes Nastran to output the complex data in rectangular format 'PHASE' - requests output of complex data in polar (magnitude, phase)format Assigning values to this property other than those defined above will cause Apex to raise an exception when the command is assigned to a load case ietm.
- `getOutput_print() -> str` — Gets property used to control output of the cross PSD and cross correlation data to the Nastran print file This property may be assigned the following values, 'PRINT' - causes the output to be written to the Nastran print file None - same a 'PRINT' with the exception that this field will not be written to the Nastran output field for this command . Omitting this field from the command causes Nastran to write the output to the print file 'NOPRINT' - no output to be written to the Nastran print file.
- `getOutput_punch() -> str` — Gets property used to control output of the cross PSD and cross correlation data to the Nastran punch file This property may be assigned the following values, 'PUNCH' - causes the output to be written to the Nastran punch file None - no output is written to the Nastran punch file.
- `getValue() -> int` — Gets The positive integer ID of an RCROSS entity that defines the pair of response quantities used to compute the cross power spectral density and cross correlation functions requested by this command.
#### `setOutput_cross_corr(output_cross_corr: str) -> None`
Sets property used to request calculation and output of the cross correlation function This property may be assigned the following values, 'CORF' - activates calculation and output of cross correlation function data None - DO NOT activate calculation and output of cross correlation function data.

- `output_cross_corr` — Set the output_cross_corr of this RCROSS

#### `setOutput_cross_psd(output_cross_psd: str) -> None`
Sets property used to request calculation and output of the cross power spectra; density function This property may be assigned the following values, 'PSDF' - requests calculation and output of cross power spectral density function data None - inhibits calculation and output of cross power spectral density function data.

- `output_cross_psd` — Set the output_cross_psd of this RCROSS

#### `setOutput_cross_psd_corr(output_cross_psd_corr: str) -> None`
Sets property used to request calculation and output of both the cross power spectral density and cross correlation function This property may be assigned the following values, 'RALL' - activates calculation and output of both the cross power spectral density and cross correlation function None - DO NOT activate calculation and output of both the cross power spectral density and cross correlation function.

- `output_cross_psd_corr` — Set the output_cross_psd_corr of this RCROSS

#### `setOutput_format(output_format: str) -> None`
Sets optional property used to control the format of the complex output generated by this RCROSS command This property may be assigned the following values, 'REAL' - requests output of complex data in rectangular (real, imaginary)format 'IMAG' - same as 'REAL' None - equivalent to 'REAL' or 'IMAG' with the exception that this filed will not be written to the Nastran file. Omission of this field causes Nastran to output the complex data in rectangular format 'PHASE' - requests output of complex data in polar (magnitude, phase)format Assigning values to this property other than those defined above will cause Apex to raise an exception when the command is assigned to a load case ietm.

- `output_format` — Set the output_format of this RCROSS

#### `setOutput_print(output_print: str) -> None`
Sets property used to control output of the cross PSD and cross correlation data to the Nastran print file This property may be assigned the following values, 'PRINT' - causes the output to be written to the Nastran print file None - same a 'PRINT' with the exception that this field will not be written to the Nastran output field for this command . Omitting this field from the command causes Nastran to write the output to the print file 'NOPRINT' - no output to be written to the Nastran print file.

- `output_print` — Set the output_print of this RCROSS

#### `setOutput_punch(output_punch: str) -> None`
Sets property used to control output of the cross PSD and cross correlation data to the Nastran punch file This property may be assigned the following values, 'PUNCH' - causes the output to be written to the Nastran punch file None - no output is written to the Nastran punch file.

- `output_punch` — Set the output_punch of this RCROSS

#### `setValue(value: int) -> None`
Sets The positive integer ID of an RCROSS entity that defines the pair of response quantities used to compute the cross power spectral density and cross correlation functions requested by this command.

- `value` — Set the value of this RCROSS


## `apex.studies.RESVEC`  (extends `ScenarioCommand`)
Class representing a Nastran "RESVEC" case control command The RESVEC command is used to specify options for calculation and output of residual vectors.
Properties: `adjoint_load_residuals`, `applied_load_residuals`, `dynamically_responding_residuals`, `inertial_force_residuals`, `rvdof_residuals`, `value`, `viscous_damping_residuals`

Methods:

- `getAdjoint_load_residuals() -> str` — Gets property used to specify whether or not residual vectors based on adjoint loads will be calculated This property may be assigned any one of the following values, "ADHLOD" - enables calculation of residual vectors based on adjoint loads None - same as "ADJLOD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("ADJLOD" is the default value for this field) "NOADJLOD" - disables calculation of residual vectors based on adjoint loads.
- `getApplied_load_residuals() -> str` — Gets property used to specify whether or not residual vectors based on applied loads will be calculated This property may be assigned any one of the following values, "APPLOD" - enables calculation of residual vectors based on applied loads None - same as "APPLOD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("APPLOD" is the default value for this field) "NOAPPL" - disables calculation of residual vectors based on applied loads.
- `getDynamically_responding_residuals() -> str` — Gets property used to specify whether or not residual vectors are allowed to respond dynamically during modal frequency/transient analysis This property may be assigned any one of the following values, "DYNRESP" - allows residual vectors to vary dynamically None - same as "DYNRESP" with the exception that this field will not be written to the Nastran file for this RESVEC command ("DYNRESP" is the default value for this field) "NODYNRSP" - dynamic variation of residual vectors is not allowed.
- `getInertial_force_residuals() -> str` — Gets property used to specify whether or not residual vectors based on inertial forces from rigid body motions will be calculated This property may be assigned any one of the following values, "INRLOAD" - enables calculation of residual vectors based on rigid body inertia forces None - same as "INRLOAD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("INRLOAD" is the default value for this field) "NOINRL" - disables calculation of residual vectors based on rigid body inertia forces.
- `getRvdof_residuals() -> str` — Gets property used to specify whether or not residual vectors based on specified residual vector degrees of freedom will be calculated This property may be assigned any one of the following values, "RVDOF" - enables calculation of residual vectors based on specified residual vector degrees of freedom None - same as "RVDOF" with the exception that this field will not be written to the Nastran file for this RESVEC command ("RVDOF" is the default value for this field) "NORVDO" - disables calculation of residual vectors based on specified residual vector degrees of freedom.
- `getValue() -> str` — Gets property used to specify whether residual vectors will be calculated or not This property may be assigned any one of the following values, "SYSTEM" - "NOSYSTEM" - "COMPONENT" - "NOCOMPONENT" - "YES" - Calculate residual vectors for both system and component modes "BOTH" - Same as Yes "NO" - Do NOT calculate residual vectors.
- `getViscous_damping_residuals() -> str` — Gets property used to specify whether or not residual vectors based on viscous damping will be calculated This property may be assigned any one of the following values, "DAMPLOD" - enables calculation of residual vectors based on viscous damping None - same as "DAMPLOD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("DAMPLOD" is the default value for this field) "NODAMP" - disables calculation of residual vectors based on viscous damping.
#### `setAdjoint_load_residuals(adjoint_load_residuals: str) -> None`
Sets property used to specify whether or not residual vectors based on adjoint loads will be calculated This property may be assigned any one of the following values, "ADHLOD" - enables calculation of residual vectors based on adjoint loads None - same as "ADJLOD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("ADJLOD" is the default value for this field) "NOADJLOD" - disables calculation of residual vectors based on adjoint loads.

- `adjoint_load_residuals` — Set the adjoint_load_residuals of this RESVEC

#### `setApplied_load_residuals(applied_load_residuals: str) -> None`
Sets property used to specify whether or not residual vectors based on applied loads will be calculated This property may be assigned any one of the following values, "APPLOD" - enables calculation of residual vectors based on applied loads None - same as "APPLOD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("APPLOD" is the default value for this field) "NOAPPL" - disables calculation of residual vectors based on applied loads.

- `applied_load_residuals` — Set the applied_load_residuals of this RESVEC

#### `setDynamically_responding_residuals(dynamically_responding_residuals: str) -> None`
Sets property used to specify whether or not residual vectors are allowed to respond dynamically during modal frequency/transient analysis This property may be assigned any one of the following values, "DYNRESP" - allows residual vectors to vary dynamically None - same as "DYNRESP" with the exception that this field will not be written to the Nastran file for this RESVEC command ("DYNRESP" is the default value for this field) "NODYNRSP" - dynamic variation of residual vectors is not allowed.

- `dynamically_responding_residuals` — Set the dynamically_responding_residuals of this RESVEC

#### `setInertial_force_residuals(inertial_force_residuals: str) -> None`
Sets property used to specify whether or not residual vectors based on inertial forces from rigid body motions will be calculated This property may be assigned any one of the following values, "INRLOAD" - enables calculation of residual vectors based on rigid body inertia forces None - same as "INRLOAD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("INRLOAD" is the default value for this field) "NOINRL" - disables calculation of residual vectors based on rigid body inertia forces.

- `inertial_force_residuals` — Set the inertial_force_residuals of this RESVEC

#### `setRvdof_residuals(rvdof_residuals: str) -> None`
Sets property used to specify whether or not residual vectors based on specified residual vector degrees of freedom will be calculated This property may be assigned any one of the following values, "RVDOF" - enables calculation of residual vectors based on specified residual vector degrees of freedom None - same as "RVDOF" with the exception that this field will not be written to the Nastran file for this RESVEC command ("RVDOF" is the default value for this field) "NORVDO" - disables calculation of residual vectors based on specified residual vector degrees of freedom.

- `rvdof_residuals` — Set the rvdof_residuals of this RESVEC

#### `setValue(value: str) -> None`
Sets property used to specify whether residual vectors will be calculated or not This property may be assigned any one of the following values, "SYSTEM" - "NOSYSTEM" - "COMPONENT" - "NOCOMPONENT" - "YES" - Calculate residual vectors for both system and component modes "BOTH" - Same as Yes "NO" - Do NOT calculate residual vectors.

- `value` — Set the value of this RESVEC

#### `setViscous_damping_residuals(viscous_damping_residuals: str) -> None`
Sets property used to specify whether or not residual vectors based on viscous damping will be calculated This property may be assigned any one of the following values, "DAMPLOD" - enables calculation of residual vectors based on viscous damping None - same as "DAMPLOD" with the exception that this field will not be written to the Nastran file for this RESVEC command ("DAMPLOD" is the default value for this field) "NODAMP" - disables calculation of residual vectors based on viscous damping.

- `viscous_damping_residuals` — Set the viscous_damping_residuals of this RESVEC


## `apex.studies.RIGID`  (extends `ScenarioCommand`)
Class representing a Nastran "RIGID" case control command The RIGID command is used to which of three possible methods will be used to process rigid elements.
Properties: `value`

Methods:

- `getValue() -> str` — Gets property used to specify which of three possible methods will be used by Nastran to process rigid elements This property may be assigned any one of the following values, "LINEAR" - rigid elements will be processed using the linear elimination method "LAGRAN" - rigid elements will be processed using the Lagrange multiplier method "LGELIM" - rigid elements will be processed using the Lagrange multiplier method with elimination None - rigid elements will be processed using the linear elimination method for all solution sequences EXCEPT Solution 400 where Nastran will use the Lagrange multiplier method.
#### `setValue(value: str) -> None`
Sets property used to specify which of three possible methods will be used by Nastran to process rigid elements This property may be assigned any one of the following values, "LINEAR" - rigid elements will be processed using the linear elimination method "LAGRAN" - rigid elements will be processed using the Lagrange multiplier method "LGELIM" - rigid elements will be processed using the Lagrange multiplier method with elimination None - rigid elements will be processed using the linear elimination method for all solution sequences EXCEPT Solution 400 where Nastran will use the Lagrange multiplier method.

- `value` — Set the value of this RIGID


## `apex.studies.RSDAMP`  (extends `ScenarioCommand`)
Class used to represent a Nastran RSDAMP case control command The RSDAMP command is used to activate residual structure damping and to select the damping parameters.
Properties: `scope`, `value`

Methods:

- `getScope() -> str` — Gets an optional property used to define how this residual structure damping command is applied to the structural and fluid regions of the residual. This property may be assigned the following values, 'STRUCTURE' - causes damping to be applied to the structural regions of the residual only None - causes the same behavior as 'STRUCTURE' but does not write 'STRUCTURE' to the Nastran file for this command 'FLUID' - causes damping to be applied to the fluid regions of the residual only 'BOTH' - causes damping to be applied to both the structural and fluid region of the residual Values other than those defined above will cause Apex to raise an exception when this command is assigned to a load case item.
- `getValue() -> int` — Gets a positive integer identifying an existing DAMPING entity. The referenced DAMPING entity defines the damping parameters that will be used during solutio of the load case item that this RSDMAP command is assigned to.
#### `setScope(scope: str) -> None`
Sets an optional property used to define how this residual structure damping command is applied to the structural and fluid regions of the residual. This property may be assigned the following values, 'STRUCTURE' - causes damping to be applied to the structural regions of the residual only None - causes the same behavior as 'STRUCTURE' but does not write 'STRUCTURE' to the Nastran file for this command 'FLUID' - causes damping to be applied to the fluid regions of the residual only 'BOTH' - causes damping to be applied to both the structural and fluid region of the residual Values other than those defined above will cause Apex to raise an exception when this command is assigned to a load case item.

- `scope` — Set the scope of this RSDAMP

#### `setValue(value: int) -> None`
Sets a positive integer identifying an existing DAMPING entity. The referenced DAMPING entity defines the damping parameters that will be used during solutio of the load case item that this RSDMAP command is assigned to.

- `value` — Set the value of this RSDAMP


## `apex.studies.SDAMPING`  (extends `ScenarioCommand`)
Class used to represent a Nastran SDAMPING case control command The SDAMPING command is used to activate modal damping as a function of natural frequency in modal solutions and to select the modal damping parameters.
Properties: `scope`, `value`

Methods:

- `getScope() -> str` — Gets an optional property used to define how this modal damping command is applied to the structural and fluid regions of the model. This property may be assigned the following values, 'STRUCTURE' - causes modal damping to be applied to the structural regions of the model only None - causes the same behavior as 'STRUCTURE' but does not write 'STRUCTURE' to the Nastran file for this command 'FLUID' - causes modal damping to be applied to the fluid regions of the model only 'BOTH' - causes modal damping to be applied to both the structural and fluid regions of the model Values other than those defined above will cause Apex to raise an exception when this command is assigned to a load case item.
- `getValue() -> int` — Gets a positive integer identifying an existing TABDMP1, TABLED1, TABLED2, TABLED3 or, TABLED4 entity. The referenced entity defines the damping parameters that will be used during solution of the load case item that this SDMAPING command is assigned to.
#### `setScope(scope: str) -> None`
Sets an optional property used to define how this modal damping command is applied to the structural and fluid regions of the model. This property may be assigned the following values, 'STRUCTURE' - causes modal damping to be applied to the structural regions of the model only None - causes the same behavior as 'STRUCTURE' but does not write 'STRUCTURE' to the Nastran file for this command 'FLUID' - causes modal damping to be applied to the fluid regions of the model only 'BOTH' - causes modal damping to be applied to both the structural and fluid regions of the model Values other than those defined above will cause Apex to raise an exception when this command is assigned to a load case item.

- `scope` — Set the scope of this SDAMPING

#### `setValue(value: int) -> None`
Sets a positive integer identifying an existing TABDMP1, TABLED1, TABLED2, TABLED3 or, TABLED4 entity. The referenced entity defines the damping parameters that will be used during solution of the load case item that this SDMAPING command is assigned to.

- `value` — Set the value of this SDAMPING


## `apex.studies.SLDSKIN`  (extends `ScenarioCommand`)
Class representing a Nastran SLDSKIN case control command. SLDSKIN commands are used to modify the behavior selected PSHELL element properties by disbaling any materials defined on the MID2, MID3 and MID4 fields of these properties and effectively causing the element property to define membrane only behavior. Note that the material references are not actually removed from the referenced PSHELL properties - this is basically an instruction for Nastran to ignore these fields. The class provides properties to identify the target PSHELL entries and to exclude targeted PSHEL entries based on their individual thickness.
Properties: `thickness_tol`, `value`

Methods:

- `getThickness_tol() -> float` — Gets optional property (Default = 1.0E-3) defining a thickness. Any of the PSHELL properties selected by this command will be ignored (the MID2, ID3 and MID4 fields will remain active) if their thickness value is less than or equal to this value this property represents a LENGTH quantity and is specified in the unit of Length that is active in the current Apex scripting unit system.
- `getValue() -> str` — Gets optional property (default = "NONE") used to identify the PSHELL entries that will be modified by this command. value may be set as follows, "NONE" - The command will be applied NO PSHELL element properties 'ALL" - The command will be applied ALL PSHELL element properties in the model <br>"n" - a single positive integer defining the ID of an ModelSet3 entity that defines the IDs of one or more PSHELL element properties that this command will be applied to.
#### `setThickness_tol(thickness_tol: float) -> None`
Sets optional property (Default = 1.0E-3) defining a thickness. Any of the PSHELL properties selected by this command will be ignored (the MID2, ID3 and MID4 fields will remain active) if their thickness value is less than or equal to this value this property represents a LENGTH quantity and is specified in the unit of Length that is active in the current Apex scripting unit system.

- `thickness_tol` — Set the thickness_tol of this SLDSKIN

#### `setValue(value: str) -> None`
Sets optional property (default = "NONE") used to identify the PSHELL entries that will be modified by this command. value may be set as follows, "NONE" - The command will be applied NO PSHELL element properties 'ALL" - The command will be applied ALL PSHELL element properties in the model <br>"n" - a single positive integer defining the ID of an ModelSet3 entity that defines the IDs of one or more PSHELL element properties that this command will be applied to.

- `value` — Set the value of this SLDSKIN


## `apex.studies.SMETHOD`  (extends `ScenarioCommand`)
Class representing a Nastran SMETHOD case control command The SMETHOD command is used to define iterative solver parameters.
Properties: `solver_controls`

Methods:

- `getSolver_controls() -> str` — Gets required property used to define iterative solver controls this property may be assigned any of the values shown below, 'ELEMENT' - This is the default value for this property and selects the element based iterative solver with default control values 'MATRIX' - Selects the matrix based iterative solver with default control values n - a positive integer value that selects the an existing ITER entity by its ID. The referenced ITER entity specifies user defined iterative solver control values.
#### `setSolver_controls(solver_controls: str) -> None`
Sets required property used to define iterative solver controls this property may be assigned any of the values shown below, 'ELEMENT' - This is the default value for this property and selects the element based iterative solver with default control values 'MATRIX' - Selects the matrix based iterative solver with default control values n - a positive integer value that selects the an existing ITER entity by its ID. The referenced ITER entity specifies user defined iterative solver control values.

- `solver_controls` — Set the solver_controls of this SMETHOD


## `apex.studies.SPC`  (extends `ScenarioCommand`)
Class representing a Nastran SPC case control command. SPC commands are used to select one or more Constraints, applied to the model, for inclusion in a LoadCaseItem. Constraints are identified by their ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of one or more constraints assigned to the model referenced by the Scenario that this command is composed by Use this command to assign Constraints to a Scenario, Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets the ID of one or more constraints assigned to the model referenced by the Scenario that this command is composed by Use this command to assign Constraints to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this SPC


## `apex.studies.STATSUB_BUCKLING`  (extends `ScenarioCommand`)
Class representing as Nastran "STATSUB (BUCKLING)" case control command The STATSUB (BUCKLING) command is used to select a static analysis subcase that will be used to define the static buckling load for use in linear buckling subcases.
Properties: `value`, `write_buckling_field`

Methods:

- `getValue() -> int` — Gets specifies the ID of an existing static analysis Subcase that will be used to define the static buckling load for use in linear buckling analysis This property may be assigned either of the following values, n - positive integer ID of an existing static analysis Subcase None -.
- `getWrite_buckling_field() -> str` — Gets a property that controls whether or not the "(BUCKLING)" string is written as part of this STATSUB command or not This property may be assigned any one of the following values, "BUCKLING" - when written to the Nastran file this command will include the optional "BUCKLING" string. For example "STATSUB (BUCKLING) = n" None - when written to the Nastran file this command will omit the optional "BUCKLING" string. For example "STATSUB = n".
#### `setValue(value: int) -> None`
Sets specifies the ID of an existing static analysis Subcase that will be used to define the static buckling load for use in linear buckling analysis This property may be assigned either of the following values, n - positive integer ID of an existing static analysis Subcase None -.

- `value` — Set the value of this STATSUB_BUCKLING

#### `setWrite_buckling_field(write_buckling_field: str) -> None`
Sets a property that controls whether or not the "(BUCKLING)" string is written as part of this STATSUB command or not This property may be assigned any one of the following values, "BUCKLING" - when written to the Nastran file this command will include the optional "BUCKLING" string. For example "STATSUB (BUCKLING) = n" None - when written to the Nastran file this command will omit the optional "BUCKLING" string. For example "STATSUB = n".

- `write_buckling_field` — Set the write_buckling_field of this STATSUB_BUCKLING


## `apex.studies.STATSUB_PRELOAD`  (extends `ScenarioCommand`)
Class representing a Nastran "STATSUB (PRELOAD)" case control command The STATSUB (PRELOAD) command is used to select a static analysis subcase that will be used to form the differential stiffness for use in static, normal modes, frequency and transient response, complex eigenvalue and linear buckling subcases.
Properties: `value`, `write_preload_field`

Methods:

- `getValue() -> int` — Gets specifies the ID of an existing static analysis Subcase that will be used to form the differential stiffness that will be used by the Subcase with which this STATSUB command is associated This property may be assigned either of the following values, n - positive integer ID of an existing static analysis Subcase None -.
- `getWrite_preload_field() -> str` — Gets a property that controls whether or not the "(PRELOAD)" string is written as part of this STATSUB command or not This property may be assigned any one of the following values, "PRELOAD" - when written to the Nastran file this command will include the optional "PRELOAD" string. For example "STATSUB (PRELOAD) = n" None - when written to the Nastran file this command will omit the optional "PRELOAD" string. For example "STATSUB = n".
#### `setValue(value: int) -> None`
Sets specifies the ID of an existing static analysis Subcase that will be used to form the differential stiffness that will be used by the Subcase with which this STATSUB command is associated This property may be assigned either of the following values, n - positive integer ID of an existing static analysis Subcase None -.

- `value` — Set the value of this STATSUB_PRELOAD

#### `setWrite_preload_field(write_preload_field: str) -> None`
Sets a property that controls whether or not the "(PRELOAD)" string is written as part of this STATSUB command or not This property may be assigned any one of the following values, "PRELOAD" - when written to the Nastran file this command will include the optional "PRELOAD" string. For example "STATSUB (PRELOAD) = n" None - when written to the Nastran file this command will omit the optional "PRELOAD" string. For example "STATSUB = n".

- `write_preload_field` — Set the write_preload_field of this STATSUB_PRELOAD


## `apex.studies.STOCHASTICS`  (extends `ScenarioCommand`)
Class representing a Nastran STOCHASTICS case control command. The STOCHASTIC command is used to request randomization of all or selected subsets of model parameters The command can be configured to RANDOMIIZE ALL model parameters (all parameters supported by Nastran) or a subset of model parameters defined on a referenced STOCHAS entry. NOTE : Currently Apex supports randomization of ALL model parameters only. Support for defined sets of model parameters will be added in a future release.
Properties: `value`

Methods:

- `getValue() -> str` — Gets optional value used to identify which model parameters will be randomized by this STOCHASTICS command. Currently, Apex supports randomization of ALL model parameters. Setting this property to 'ALL', or leaving it unset, will cause Nastran to randomize all model paramartes.
#### `setValue(value: str) -> None`
Sets optional value used to identify which model parameters will be randomized by this STOCHASTICS command. Currently, Apex supports randomization of ALL model parameters. Setting this property to 'ALL', or leaving it unset, will cause Nastran to randomize all model paramartes.

- `value` — Set the value of this STOCHASTICS


## `apex.studies.SUBSEQ`  (extends `ScenarioCommand`)
Class representing a Nastran "SUBSEQ" case control command The SUBSEQ command is used to specify coefficients for forming linear combinations of previous subcases.
Properties: `value`

Methods:

- `getValue() -> [float]` — Gets the coefficients applied to previously occurring Subcases. The result quantities from the preceding subcases are first multiplied by these coefficients and then these scaled results are summed to generate results quantities for the Subcase that references this SUBSEQ command. The coefficients are assigned as a list of floating point values. The first value in the list applies to the first subcase in the Scenario, the second to the second Subcase in the Scenario and so until the last value in the list which refers to the Subcase immediately preceding the Subcase that references this SUBSEQ command.
#### `setValue(value: [float]) -> None`
Sets the coefficients applied to previously occurring Subcases. The result quantities from the preceding subcases are first multiplied by these coefficients and then these scaled results are summed to generate results quantities for the Subcase that references this SUBSEQ command. The coefficients are assigned as a list of floating point values. The first value in the list applies to the first subcase in the Scenario, the second to the second Subcase in the Scenario and so until the last value in the list which refers to the Subcase immediately preceding the Subcase that references this SUBSEQ command.

- `value` — Set the value of this SUBSEQ


## `apex.studies.SUBSEQ1`  (extends `ScenarioCommand`)
Class representing a Nastran SUBSEQ1 case control command.
Properties: `global_scale_factpr`, `value`

Methods:

- `getGlobal_scale_factpr() -> float` — Gets the global scale factor for this subcase combination.
- `getValue() -> [RealInt]` — Gets the coefficients and associated Subcase IDs of previously occurring Subcases as a list of lists. Each inner list must contain two values, the first value is the coefficient, as float value, that will be used to scale Subcase results the second value is the ID of a previously occurring Subcase whose results will be scaled Multiple sets of coefficient and Subcase IDs can be defined by adding to the uter list. Results are calculated for the SUBCOM subcase that references this SUBSEQ1 command by first multiplying the results for each Subcase referenced here list by its associated coefficients and then summing all of the scaled results. Given a job with four Subcases as shown below, SUBCASE 1 SUBCASE 2 SUBCASE 3 SUBCASE 4 SUBCASE 5 SUBCASE 6 and a desire to generate results by subtracting the results of Subcase 4 from Subcase 2 this value would be set to, [[1.0, 2], [-1.0, 4]] which in turn will cause the following command to be written to the Nastran file, SUBCOM 8 SUBSEQ1 = 1.0, 1.0, 2, -1.0, 4 Note that the first "1.0" shown above is actually defined by the "global_scale_factor" property of this class (which defaults to 1.0)
#### `setGlobal_scale_factpr(global_scale_factpr: float) -> None`
Sets the global scale factor for this subcase combination.

- `global_scale_factpr` — Set the global_scale_factpr of this SUBSEQ1

#### `setValue(value: [RealInt]) -> None`
Sets the coefficients and associated Subcase IDs of previously occurring Subcases as a list of lists. Each inner list must contain two values, the first value is the coefficient, as float value, that will be used to scale Subcase results the second value is the ID of a previously occurring Subcase whose results will be scaled Multiple sets of coefficient and Subcase IDs can be defined by adding to the uter list. Results are calculated for the SUBCOM subcase that references this SUBSEQ1 command by first multiplying the results for each Subcase referenced here list by its associated coefficients and then summing all of the scaled results. Given a job with four Subcases as shown below, SUBCASE 1 SUBCASE 2 SUBCASE 3 SUBCASE 4 SUBCASE 5 SUBCASE 6 and a desire to generate results by subtracting the results of Subcase 4 from Subcase 2 this value would be set to, [[1.0, 2], [-1.0, 4]] which in turn will cause the following command to be written to the Nastran file, SUBCOM 8 SUBSEQ1 = 1.0, 1.0, 2, -1.0, 4 Note that the first "1.0" shown above is actually defined by the "global_scale_factor" property of this class (which defaults to 1.0)

- `value` — Set the value of this SUBSEQ1


## `apex.studies.SUPORT1`  (extends `ScenarioCommand`)
Class representing a Nastran SUPORT case control command. This command is used to select one or more fictitious support (SUPORT1) entries applied to the model, for inclusion in a LoadCaseItem. Fictitious supports are identified by their ID.
Properties: `value`

Methods:

- `getValue() -> int` — Gets The ID of one or more SUPORT1 entries assigned to the model referenced by the Scenario that this command is composed by Use this command to assign a fictitious support to a Scenario, Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets The ID of one or more SUPORT1 entries assigned to the model referenced by the Scenario that this command is composed by Use this command to assign a fictitious support to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this SUPORT1


## `apex.studies.SYMSEQ`  (extends `ScenarioCommand`)
Class representing a Nastran "SYMSEQ" case control command The SYMSEQ command is used to specify coefficients for forming linear combinations of previous SYM subcases.
Properties: `value`

Methods:

- `getValue() -> [float]` — Gets the coefficients used to scale and subsequently sum results generated by previously occurring SYM Subcases. The result quantities from the preceding subcases are first multiplied by these coefficients and then these scaled results are summed to generate results quantities for the Subcase that references this SUBSEQ command. The coefficients are assigned as a list of floating point values. The first value in the list applies to the first SYM subcase in the Scenario, the second to the second SYM Subcase in the Scenario and so until the last value in the list which refers to the SYM Subcase immediately preceding the Subcase that references this SUBSEQ command.
#### `setValue(value: [float]) -> None`
Sets the coefficients used to scale and subsequently sum results generated by previously occurring SYM Subcases. The result quantities from the preceding subcases are first multiplied by these coefficients and then these scaled results are summed to generate results quantities for the Subcase that references this SUBSEQ command. The coefficients are assigned as a list of floating point values. The first value in the list applies to the first SYM subcase in the Scenario, the second to the second SYM Subcase in the Scenario and so until the last value in the list which refers to the SYM Subcase immediately preceding the Subcase that references this SUBSEQ command.

- `value` — Set the value of this SYMSEQ


## `apex.studies.Scenario`  (extends `Entity`, `IName`, `IUserAttributes`)
A Scenario combines all of the objects that are required to compose a valid simulation.
Properties: `constraints`, `directTextInput`, `executionStatus`, `initialConditions`, `lastExecutedScenario`, `loadCases`, `nonStructuralMassSets`, `parameters`, `parametersBulkData`, `parametersByEvent`, `parametersByLoadCase`, `parametersByStep`, `scenarioConfiguration`, `scenarioModelRep`, `simulationSettings`, `steps`, `systemCells`

Methods:

#### `addConstraint(constraint: apex.Entity) -> None`
Add a Constraint to this Scenario (only for standalone Modes Scenario)

- `constraint` — The constraint will be added to the Scenario

#### `addLoadCase(name: str, description: str, stepType: apex.studies.StepType, stepNumber: int) -> apex.studies.LoadCase`
adds (and returns) a new LoadCase to this Scenario.

- `name` — An optional name for the Load case. If omitted the system will supply a default name.
- `description` — An optional description for the Load case.
- `stepType` — Step type to be create for each load case. In current release, only static step type is available. Return error if the step type is not "Static".
- `stepNumber` — Number of steps to be created for the load case.

Returns: the created LoadCase to this Scenario

#### `associateModelAssociation(modelAssociation: apex.ModelAssociation) -> None`
Associates an ModelAssociation with the Scenario.

- `modelAssociation` — The ModelAssociation to be analyzed.

#### `associateModelRep(modelRep: apex.Entity) -> None`
Associates an AssemblyRep or PartRep with the Scenario.

- `modelRep` — The AssemblyRep, PartRep, Assembly or Part to be analyzed. If an Assembly or Part is supplied here a default AssemblyRep or PartRep will be created at the time the Scenario is executed and this AssemblyRep/PartRep will be used as the basis of the Scenario execution. If the Scenario already references a ModelRep when this method is executed the existing reference will be replaced by the ModelRep provided here If 'None' value is used in the place of ModelRep, this API will cause the ModelRep that is associated with the Scenario to be cleared

#### `attachNastranResults(resultsFilename: str, unitSystenName: str) -> None`
Attaches results from the supplied Nastran .hdf5 file into this Scenario. The units used for values in the .hdf5 file must be supplied as an input argument. Only the results are read from the results file (any model data is silently ignored) and these results must match the ModelRep associated with this Scenario as follows, All nodes and elements associated with results data in the selected results file must exist in the ModelRep referenced by this Scenario if the results file contains results from any unsupported analysis type the method will throw an exception.

- `resultsFilename` — The fully qualified name of the FE results file containing the results data that is being read.
- `unitSystenName` — The name of the Apex unit system that contains the units in which the imported files are be assumed to be, for example "m-kg-s-N-K".

#### `createDynamicStep(name: str, description: str, simulationType: int, endTime: float, outputSteps: int, outputStepSize: float, outputFrequency: float) -> apex.studies.MultiBodyTransientStep`
Create Dynamic Step.

- `name` — Name of the Dynamic Step.
- `description` — Description of the Static Step.
- `simulationType` — Enumeration defining the Multi Body Scenario Dynamic Step Simulation Type. Options are: Dynamic; QuasiStatic.
- `endTime` — End time duration of the simulation .
- `outputSteps` — Number of output steps in the simulation.
- `outputStepSize` — Output step size in the simulation.
- `outputFrequency` — Output frequency in the simulation.

#### `createStaticStep(name: str, description: str) -> apex.studies.StaticStep`
Create Static Step.

- `name` — Name of the Static Step.
- `description` — Description of the Static Step.

- `detachNastranResults() -> None` — Detach Nastran results from a scenario.
- `execute() -> bool` — Executes the Scenario on the local workstation. The amount of memory and location of the scratch files for the solver is determined by default from Apex Application Settings.
#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, resultOutputType: apex.attribute.NastranResultOutputType = apex.attribute.NastranResultOutputType.Hdf5, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports the Scenario to a Nastran file. All objects composed or referenced by the Scenario that can be mapped to Nastran keywords will be exported including the Scenario Model Rep, Events (Loads, Constraints, Initial Conditions), Simulation Settings and Output Requests. Method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the export) to be written.
- `resultOutputType` — An enumeration to define which Nastran results file format will be requested in the exported file. The default is HDF5 results output.
- `renumberMethod` — Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

#### `exportGenerativeDesignSolverInput(jobName: str, jobFolder: str, unitSystem: str) -> None`
Exports the Scenario in Generative Design file format. All objects in the Scenario will be exported. The method arguments provide control over export options.

- `jobName` — The qualified name of the folder to be exported for the scenario.
- `jobFolder` — The path of the folder to be exported for generate design scenario.
- `unitSystem` — The name of a consistent unit system to use when exporting Generative design scenario, for example "mm-kg-s-N", "in-slinch-s-lbf"

#### `exportMarc(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, inputType: apex.attribute.MarcInputType = apex.attribute.MarcInputType.Dat, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False) -> None`
Exports the contents of the Scenario to a Marc file. Scenario objects such as Events, Simulation Settings and Output Requests that map to Marc Case, Executive and File Management sections are exported. All contents of the Scenario Model Representation that map to Marc bulk data keywords are exported.

- `filename` — The path qualified name of the file that will be exported
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf"
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field)
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hiearchical include files that mirrors the Assmbly/Part product structure, or as a singel Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the xport) to be written.
- `inputType` — An enumeration to define which Marc input file format will be requested in the exported file. The default is DAT input file
- `renumberMethod` — Nastran jobs require these ID's to be unique within the scope of the Marc run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Marc files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — A Boolean quantity to control whether the exported data contains Apex Engineering Abstractions.

- `getAcfCommands() -> str` — Get the series of ACF Commands to control a scenario.
- `getConstraints() -> apex.EntityCollection` — Return a collection of apex.EntityCollection objects that are associated with this (Modes) Scenario.
- `getDirectTextInput() -> apex.studies.DirectTextInput`
#### `getDynamicStep(name: str) -> apex.studies.MultiBodyTransientStep`
Get a Dynamic Step in a Scenario.

- `name` — Name of the Dynamic Step.

#### `getExecutionStatus() -> apex.studies.ExecutionStatus`
returns the ExecutionStatus of the Scenario

Returns: Read only attribute enumerating the ExecutionStatus of the Scenario.

- `getInitialConditions() -> apex.EntityCollection` — The collection of InitialConditions that are associated with the scenario. Note that it only contains initialTemperature in this release. The collection does not include the default initial temperature or other unsupported types of initialConditions.
- `getLastExecutedScenario() -> ExecutedScenario` — return the last previously executed version of the Scenario. Use this attribute (or associated method)to access the Results data and other solution generated data related to the Scenario. This version will provide access to the ModelRep, Loads, Boundary Conditions, Simulation Settings, Simulation Status etc. of the last executed version of the Scenario. The ModelRep, Boundary Conditions, Simulation Settings, Simulation Status etc.
#### `getLoadCase(name: str) -> apex.studies.LoadCase`
Retrieves a single LoadCase from the Scenario using the supplied name. If a LoadCase with a matching name does not exist within the Scenario the method will throw an exception.

- `name` — name of load case

Returns: returns a single LoadCase in this Scenario

#### `getLoadCases() -> apex.studies.LoadCaseCollection`
Retrieves a collection of all LoadCases composed by this Scenario.

Returns: returns a collection of all LoadCases composed by this Scenario

#### `getNonStructuralMassSets() -> apex.attribute.NonstructuralMassCollection`
The collection of NonStructuralMasses that is active in this Scenario. If the collection is empty, no NonStructuralMass is active in this Scenario.

Returns: The collection of NonStructuralMasses that is active in this Scenario

- `getParameters() -> apex.catalog.ParametersSet` — Parameters set of the scenario, all PARAMs of the parameter set will be added above sub case within Nastran input file. Omits it if the ParametersType = BulkData.
- `getParametersBulkData() -> apex.catalog.ParametersSet` — Parameters set of the scenario, all PARAMs of the parameter set will be added to bulk data within Nastran input file. Omits it if the ParametersType = CaseControl.
- `getParametersByEvent() -> {str:apex.catalog.ParametersSet}` — The string keys of the dictionary is the name of the event. The value is the ParametersSet in this event. All PARAMs of the parameter set will be added to Subcase within Nastran input file. Omits it if the ParametersType = BulkData.
- `getParametersByLoadCase() -> {str:apex.catalog.ParametersSet}` — The string keys of the dictionary is the name of the load case. The value is the ParametersSet in this event. All PARAMs of the parameter set will be added to Subcase within Nastran input file. Omits it if the ParametersType = BulkData.
- `getParametersByStep() -> {str:apex.catalog.ParametersSet}` — The string keys of the dictionary is the path name of the step. The value is the ParametersSet in this step. All PARAMs of the parameter set will be added to Step within Nastran input file. Omits it if the ParametersType = BulkData.
- `getScenarioConfiguration() -> apex.studies.ScenarioConfiguration` — returns the ScenarioConfiguration of this scenario
- `getScenarioModelRep() -> apex.ModelRep` — returns the ModelRep that is associated with this scenario
#### `getSimulationSettings() -> apex.studies.SimulationSettings`
returns the SimulationSettings from this Scenario

Returns: the SimulationSettings objects

#### `getSimulationStatusMessages() -> [str]`
returns the Simulation Status messages of the Scenario

Returns: Read only attribute enumerating the Simulation Status messages of the Scenario.

#### `getStaticStep(name: str) -> apex.studies.StaticStep`
Get a Static Step in a Scenario.

- `name` — Name of the Static Step.

#### `getStep(name: str) -> apex.studies.Step`
Retrieves a single Step from the Scenario using the supplied name. If a Step with a matching name does not exist within the Scenario the method will throw an exception.

- `name` — the name of a step

Returns: a single Step by name in a Scenario

#### `getSteps() -> apex.studies.StepCollection`
returns an ordered collection of the Steps in a Scenario

Returns: an ordered collection of the Steps in a Scenario

- `getSystemCells() -> apex.catalog.SystemCellsSet` — System cells set of the scenario.
#### `importMarc(filename: str, unitSystem: str, importHierarchicalFiles: bool = False, inputType: apex.attribute.MarcInputType = apex.attribute.MarcInputType.Dat, renumberMethod: apex.attribute.ImportRenumberMethod = apex.attribute.ImportRenumberMethod.Internal, importAbstractions: bool = False) -> None`
Imports the contents of the Scenario to a Marc file. Scenario objects such as Events, Simulation Settings and Output Requests that map to Marc Case, Executive and File Management sections are imported. All contents of the Scenario Model Representation that map to Marc bulk data keywords are imported.

- `filename` — The path qualified name of the file that will be imported
- `unitSystem` — The name of a consistent unit system to use when importing Marc files, for example "mm-kg-s-N", "in-slinch-s-lbf"
- `importHierarchicalFiles` — A Boolean quantity to control whether the imported data is written as a series of hiearchical include files that mirrors the Assmbly/Part product structure, or as a singel Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the xport) to be written.
- `inputType` — An enumeration to define which Marc input file format will be requested in the imported file. The default is DAT input file
- `renumberMethod` — Marc jobs require these ID's to be unique within the scope of the Marc run. This enumeration is used to control how Apex resolves duplicate ID's when models are being imported as Marc files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "import" causes the renumbering operation to be applied ONLY to the imported Marc file and has no impact on the ID's within Apex.
- `importAbstractions` — A Boolean quantity to control whether the imported data contains Apex Engineering Abstractions.

#### `importNastranResults(resultsFilename: str, unitSystenName: str) -> None`
Imports results from the supplied Nastran .hdf5 file into this Scenario. The units used for values in the .hdf5 file must be supplied as an input argument. Only HDF5 files containing results from Linear static, normal modes or linear buckling analyses are supported. If the .hdf5 file contains results from any other analysis type the method will throw an exception. Only the results are read from the .hdf5 file (any model data is silently ignored) and these results must match the ModelRe associated with this Scenario as follows, All nodes and elements associated with results data in the .hdf5 file must exist in the ModelRep referenced by this Scenario The hd5 file must contain results from a linear static, normal modes or linear buckling analysis only If either of these conditions are not me, the method will throw an exception. If the number of Events in the .hdf5 file is different from the number of Events in this Scenario and the above model compatibility rules are satisfied , the method will create a copy of this Scenario (minus the Events) and will create new Events on the copied Scenario to match the Events found in the .hdf5 file.

- `resultsFilename` — The path qualified name of the file that will be imported.
- `unitSystenName` — The name of the Apex unit system that contains the units in which the imported files are be assumed to be.

#### `removeConstraint(constraint: apex.Entity) -> None`
Removes a Constraint from an Scenario (only for standalone Modes Scenario)

- `constraint` — The constraint to be removed from the Scenario

- `setInitialConditions(initialConditions: apex.EntityCollection) -> None` — Defines InitialConditions that are associated with the scenario. Note that it only contains initialTemperature in this release. The collection does not include the default initial temperature or other unsupported types of initialConditions.
#### `setNonStructuralMassSets(nonStructuralMasses: apex.attribute.NonstructuralMassCollection) -> None`
Defines the set of NonStructuralMasses that will be active in this Scenario. The set of NonStructuralMasses to activate is provided as a NonstructuralMassCollection argument.

- `nonStructuralMasses` — the NonstructuralMassCollection to activate of this Scenario

#### `setParameters(parameters: apex.catalog.ParametersSet) -> None`
set a Parameters set to this Scenario

- `parameters` — Parameters set of the scenario, all PARAMs of the parameter set will be added above sub case within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersBulkData(parametersBulkData: apex.catalog.ParametersSet) -> None`
set a Parameters set to this Scenario

- `parametersBulkData` — Parameters set of the scenario, all PARAMs of the parameter set will be added above sub case within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersByEvent(parametersByEvent: {str:apex.catalog.ParametersSet}) -> None`
set Parameters set to this Scenario

- `parametersByEvent` — The string keys of the dictionary is the name of the event. The value is the ParametersSet in this event. All PARAMs of the parameter set will be added to Subcase within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersByLoadCase(parametersByLoadCase: {str:apex.catalog.ParametersSet}) -> None`
set Parameters set to this Scenario

- `parametersByLoadCase` — The string keys of the dictionary is the name of the load case. The value is the ParametersSet in this event. All PARAMs of the parameter set will be added to Subcase within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersByStep(parametersByStep: {str:apex.catalog.ParametersSet}) -> None`
set Parameters set to this Scenario

- `parametersByStep` — The string keys of the dictionary is the path name of the step. The value is the ParametersSet in this step. All PARAMs of the parameter set will be added to Step within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setSimulationSettings(simulationSettings: apex.studies.SimulationSettings) -> None`
set a SimulationSettings to this Scenario

- `simulationSettings` — the SimulationSettings to be set into this Scenario

#### `setSystemCells(systemCells: apex.catalog.SystemCellsSet) -> None`
set a System cells set to this Scenario

- `systemCells` — System cells set of the scenario.

#### `update(name: str, description: str, modelRep: apex.ModelRep) -> None`
Update this Scenario.

- `name` — the name of this Scenario to be updated
- `description` — the description of this Scenario to be updated
- `modelRep` — the model rep of this Scenario to be updated


## `apex.studies.ScenarioCollection`  (extends `EntityCollection`)

Methods:

- `ScenarioCollection() -> None` — Construct a new ScenarioCollection.

## `apex.studies.ScenarioCommand`
A base class for all Nastran ScenarioCommands. ScenarioCommands map mostly to Nastran case control commands although there are some exceptions where bulk data entries such as BCPARA and a few others are mapped to ScenaioCommands.
Properties: `activeState`, `description`, `name`

Methods:

- `getActiveState() -> bool` — Gets the active state of this ScenarioCommand. True indicates that the command is active within the LoadCaseItem within which it is composed. False indicates that it is inactive.
- `getDescription() -> str` — Gets the read only a description of this ScenarioCommand.
- `getName() -> str` — Gets the read only Name of this ScenarioCommand.
#### `setActiveState(activeState: bool) -> None`
Sets the active state of this ScenarioCommand. True indicates that the command is active within the LoadCaseItem within which it is composed. False indicates that it is inactive.

- `activeState` — Set the activeState of this ScenarioCommand


## `apex.studies.ScenarioNastran`  (extends `LoadCaseItem`)
Class ScenarioNastran A Scenario combines all of the data required to fully define a simulation - model, loading environment, solution controls and output requests.
Properties: `analysis`, `directTextInput`, `executionStatus`, `resultFiles`, `scenario_sets`, `solutionType`, `subcases`

Methods:

#### `associateModelRep(modelRep: apex.Entity) -> None`
Associates an AssemblyRep or PartRep with the Scenario.

- `modelRep` — The AssemblyRep, PartRep, Assembly or Part to be analyzed. If an Assembly or Part is supplied here a default AssemblyRep or PartRep will be created at the time the Scenario is executed and this AssemblyRep/PartRep will be used as the basis of the Scenario execution. If the Scenario already references a ModelRep when this method is executed the existing reference will be replaced by the ModelRep provided here If 'None' value is used in the place of ModelRep, this API will cause the ModelRep that is associated with the Scenario to be cleared

#### `attachNastranResults(result_file_names: [str], unit_system_name: str) -> None`
Attaches results from the supplied ScenarioNastran .hdf5 file into this Scenario. The units used for values in the .hdf5 file must be supplied as an input argument. Only the results are read from the results file (any model data is silently ignored) and these results must match the ModelRep associated with this Scenario as follows, All nodes and elements associated with results data in the selected results file must exist in the ModelRep referenced by this Scenario if the results file contains results from any unsupported analysis type the method will throw an exception.

- `result_file_names` — A list of fully qualified pathnames identifying the results files to attach Apex currently supports attachment of Nastran .h5 or .op2 result files types NOTE : Apex currently supports attachment of a single result file per ScenarioNastran. If multiple h5 file names are provided only the first will be processed and all others will be silently ignored A future release of Apex will support attachment of multiple files per ScenaioNastran
- `unit_system_name` — The name of the Apex unit system in which the results data is provided.

#### `createScenarioSetFrequency(id: int, name: str, frequencies: [float]) -> apex.studies.ScenarioSetFrequency`
Creates and returns a ScenarioSetFrequency The ScenarioSetElementId may be optionally be initialized with an id, name and iterable of frequency values.

- `id` — An id for this ScenarioSetGridId. If omitted, Apex will provide a default id that is unique among all other ScenarioSetNastrans in this Scenario
- `name` — An optional name for this ScenarioSet. If omitted, Apex will provide a default name that is unique within this Scenario. The default name will be generated from the concatenation of the root string "ScenarioSetFrequency" and the lowest available integer to ensure name uniqueness of this ScenarioSetFrequency within this Scenario for example "ScenarioSetFrequency 4" If a non-unique name is provided, Apex will silently ignore the input and generate a unique name as described above
- `frequencies` — An iterable (list, array etc) containing the frequencies that this ScenarioSetFrequency will reference The values defined here represent a Frequency quantity and must be defined using the units of Frequency from the active script unit system

#### `createScenarioSetFrfcompId(id: int, name: str, rand_ids: [int]) -> apex.studies.ScenarioSetFrfcompId`
Creates and returns a ScenarioSetFrfcompId The ScenarioSetFrfcompId may optionally be initialized with an id, name and iterable of FRFCOMP bulk entry IDs.

- `id` — An id for this ScenarioSetGridId. If omitted, Apex will provide a default id that is unique among all other ScenarioSetNastrans in this Scenario
- `name` — An optional name for this ScenarioSet. If omitted, Apex will provide a default name that is unique within this Scenario. The default name will be generated from the concatenation of the root string "ScenarioSetFrfcompId" and the lowest available integer to ensure name uniqueness of this ScenarioSetFrfcompId within this Scenario for example "ScenarioSetFrfcompId 4" If a non-unique name is provided, Apex will silently ignore the input and generate a unique name as described above
- `rand_ids` — An iterable (list, array etc) containing the ids of one or more RANDPS and/or RANDT1 entries that this ScenarioSetRandIds will reference

#### `createScenarioSetGridComponent(id: int, name: str, grid_components: [str]) -> apex.studies.ScenarioSetGridComponent`
Creates and returns a ScenarioSetGridComponent The ScenarioSetGridComponent may optionally be initialized with an id, name and iterable of grid component values.

- `id` — An id for this ScenarioSetGridId. If omitted, Apex will provide a default id that is unique among all other ScenarioSetNastrans in this Scenario
- `name` — An optional name for this ScenarioSet. If omitted, Apex will provide a default name that is unique within this Scenario. The default name will be generated from the concatenation of the root string "ScenarioSetGridComponent" and the lowest available integer to ensure name uniqueness of this ScenarioSetGridComponent within this Scenario for example "ScenarioSetGridComponent 4" If a non-unique name is provided, Apex will silently ignore the input and generate a unique name as described above
- `grid_components` — An iterable (list, array etc) containing the grid components that this ScenarioSetGridComponent will reference Each grid component in the list is represented by the combination of the grid ID and a component code Valid component codes are "T1", "T2", "T3", "R1", "R2", "R3" An example of a list of grid components is shown below ["101/T1", "501/T3", "991/R3"]

#### `createScenarioSetGridId(id: int, name: str, group: apex.Group) -> apex.studies.ScenarioSetGridId`
Creates and returns a ScenarioSetGridId The ScenarioSetGridId may be optionally be initialized with an id, name and Group.

- `id` — An id for this ScenarioSetGridId. If omitted, Apex will provide a default id that is unique among all other ScenarioSetNastrans in this Scenario
- `name` — An optional name for this ScenarioSet. If omitted, Apex will provide a default name that is unique within this Scenario. The default name will be generated from the concatenation of the root string "ScenarioSetGridId" and the lowest available integer to ensure name uniqueness of this ScenarioSetGridId within this Scenario for example "ScenarioSetGridId 4" If a non-unique name is provided, Apex will silently ignore the input and generate a unique name as described above
- `group` — optional Group that contains the Grids (or elements from which Grids will be extracted) that this ScenarioSetGridId will reference

- `createScenarioSetModeId(id: int, name: str, mode_ids: [int]) -> apex.studies.ScenarioSetModeId`
#### `createScenarioSetRandId(id: int, name: str, rand_ids: [int]) -> apex.studies.ScenarioSetRandId`
Creates and returns a ScenarioSetRandId The ScenarioSetRandId may optionally be initialized with an id, name and iterable of IDs.

- `id` — An id for this ScenarioSetGridId. If omitted, Apex will provide a default id that is unique among all other ScenarioSetNastrans in this Scenario
- `name` — An optional name for this ScenarioSet. If omitted, Apex will provide a default name that is unique within this Scenario. The default name will be generated from the concatenation of the root string "ScenarioSetGridRandId" and the lowest available integer to ensure name uniqueness of this ScenarioSetRandId within this Scenario for example "ScenarioSetRandId 4" If a non-unique name is provided, Apex will silently ignore the input and generate a unique name as described above
- `rand_ids` — An iterable (list, array etc) containing the ids of one or more RANDPS and/or RANDT1 entries that this ScenarioSetRandIds will reference

#### `createScenarioSetTime(id: int, name: str, times: [float]) -> apex.studies.ScenarioSetTime`
Creates and returns a ScenarioSetTime The ScenarioSetTime may be optionally be initialized with an id, name and iterable of time values.

- `id` — An id for this ScenarioSetGridId. If omitted, Apex will provide a default id that is unique among all other ScenarioSetNastrans in this Scenario
- `name` — An optional name for this ScenarioSet. If omitted, Apex will provide a default name that is unique within this Scenario. The default name will be generated from the concatenation of the root string "ScenarioSetTime" and the lowest available integer to ensure name uniqueness of this ScenarioSetTime within this Scenario for example "ScenarioSetTime 4" If a non-unique name is provided, Apex will silently ignore the input and generate a unique name as described above
- `times` — An iterable (list, array etc) containing the times that this ScenarioSetFrequency will reference The values defined here represent a Time quantity and must be defined using the units of Time from the active script unit system

#### `createSubcase(analysisType: apex.studies.NastranAnalysisType, numberOfSubcases: int, name: str, description: str) -> apex.studies.SubcaseNastranCollection`
Creates one or more Subcases of the specified type and adds them to this Scenario.

- `analysisType` — An optional argument defining the analysis type of the Subcase. If omitted a Subcase with the default analysis type for the current Scenario solution type will be created
- `numberOfSubcases` — An optional argument specifying the the number of Subcases to create. If omitted, a single Subcase will be created
- `name` — A name for the Scenario. If omitted Apex will generate a default name dependent on the type of Subcase that is being created If a Subcase with the same name already exists within this Scenario Apex will append an integer to ensure Subcase name uniqueness within this Scenario
- `description` — An optional description for the new Subcase

Returns: Creates one or more Subcases of the specified type

#### `deleteSubcase(name: str = "#####") -> None`
Deletes a SubcaseNastran from this Study.

- `name` — The name of the SubcaseNastran to be removed from the ScenarioNastran

- `detachNastranResults() -> None` — Detach ScenarioNastran results from a scenario.
#### `execute(compute_environment: ComputeEnvironmentNastranExternal) -> bool`
Executes the Scenario on the local workstation.

- `compute_environment` — An optional ComputeEnvironmentNastranExternal on which the Scenario will be executed. If omitted, the Scenario will be executed on the default ComputeEnvironment. The ComputeEnvironment identifies the solver instance that will be used plus all memory, disk and CPU options.

#### `exportFEModel(filename: str, unitSystem: str, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, resultOutputType: apex.attribute.NastranResultOutputType = apex.attribute.NastranResultOutputType.Hdf5, renumberMethod: apex.attribute.ExportRenumberMethod = apex.attribute.ExportRenumberMethod.Internal, exportAbstractions: bool = False, writePropertyOnElement: bool = True, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Exports the ScenarioNastran to a Nastran file. All objects composed or referenced by the Scenario that can be mapped to Nastran keywords will be exported including the Scenario Model Rep, Events (Loads, Constraints, Initial Conditions), Simulation Settings and Output Requests. Method arguments provide control over export options.

- `filename` — The path qualified name of the file that will be exported.
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the export) to be written.
- `resultOutputType` — An enumeration to define which Nastran results file format will be requested in the exported file. The default is HDF5 results output.
- `renumberMethod` — Nastran jobs require these ID's to be unique within the scope of the Nastran run. This enumeration is used to control how Apex resolves duplicate ID's when models are being exported as Nastran files. Two options are provided, "internal" causes the renumbering operation to carried out and persisted in the Apex Model. "export" causes the renumbering operation to be applied ONLY to the exported Nastran file and has no impact on the ID's within Apex.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `writePropertyOnElement` — Optional boolean argument (Default = True) that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `exportProperty` — Optional argument to control the way how the property is exported, the default value is "AsDefined", unless one of other two values are given : "Inline" or "External". If "AsDefined" is given, then the property will be exported according to the defined way in Apex, for example : one spring is defined with "Embedded" property, then this spring is exported as CLEAS2; one spring is referring a existed property through "Use property" method, then this spring is exported as CELAS1 and PELAS. If "Inline" is given, the property will be written in the element entry If "External" is given, the property will be written as a separated nastran entry Damper has the same behavior during exporting with different setting for this argument.

- `getAnalysis() -> apex.studies.NastranAnalysisType` — Gets enumeration used to define the default ANALYSIS type for this ScenarioNastran. This property is only valid for Scenarios types associated with Nastran Solution 400 or Solution 200 and is used to set the value of the ANALYSIS command ABOVE all subcases.Although the ANALYSIS value can be set within each load case item(SUBCASE, STEP, SUBSTEP), setting it above all SUBCASES removes the need to set it within each load case item The property may be set to either of the values shown below Any value of the apex.studies.NastranAnalysisType.See the documentation for this Enum to determine the range of analysis types supported None - No ANALYSIS entry will be defined above the Subcases Attempting to set this property on a ScenarioNastran that is not associated with Solution 400 or Solution 200 will cause an exception to be raised. NOTE: Not all analysis types defined by the apex.studies.NastranAnalysisType enumeration are supported by Solution 200 or Solution 400. Refer to the table below for valid combinations.Setting an unsupported value will cause this method to raise an exception. Statics 200, 400 Modes 200, 400 Buckling 200, 400 ModalTransient 200,400 ModalFrequency 200, 400 DirectFrequency 200, 400 ModalComplexEigenvalue 200, 400 DirectComplexEigenvalue 200, 400 StaticAeroelasticity 200, 400 StaticAeroelasticDivergence 200, 400 Flutter 200, 400 NonlinearStatics 400 NonlinearTransient 400 NonlinearSteadyStateHeat 400 NonlinearTransientHeat 400.
- `getDirectTextInput() -> apex.studies.DirectTextInput` — get export new scenario settings.
- `getExecutionStatus() -> apex.studies.ExecutionStatus` — Gets the execution status of this ScenarioNastran.
- `getParameters() -> apex.catalog.ParametersSet` — Parameters set of the ScenarioNastran, all PARAMs of the parameter set will be added above sub case within Nastran input file. Omits it if the ParametersType = BulkData.
- `getParametersBulkData() -> apex.catalog.ParametersSet` — Parameters set of the ScenarioNastran, all PARAMs of the parameter set will be added to bulk data within Nastran input file. Omits it if the ParametersType = CaseControl.
- `getParametersByLoadCase() -> {str:apex.catalog.ParametersSet}` — The string keys of the dictionary is the name of the load case. The value is the ParametersSet in this load case. All PARAMs of the parameter set will be added to load case within ScenarioNastran input file. Omits it if the ParametersType = BulkData.
- `getParametersByStep() -> {str:apex.catalog.ParametersSet}` — The string keys of the dictionary is the path name of the step. The value is the ParametersSet in this step. All PARAMs of the parameter set will be added to Step within ScenarioNastran input file. Omits it if the ParametersType = BulkData.
- `getParametersBySubStep() -> {str:apex.catalog.ParametersSet}` — The string keys of the dictionary is the path name of the sub step. The value is the ParametersSet in this sub step. All PARAMs of the parameter set will be added to Step within ScenarioNastran input file. Omits it if the ParametersType = BulkData.
- `getResultFiles() -> [str]` — Gets A List of the fully qualified pathnames of all currently attached result files.
#### `getScenarioSetNastran(id: int) -> apex.studies.ScenarioSetNastran`
gets a ScenarioSetNastran from this ScenarioNastran using the ID provided in the argument The ScenarioSetNastran is returned as an instance of the actual type of the Set and not as the base class ScenarioSetNastran types

- `id` — The ID of the ScenarioSet to retrieve, If a ScenarioSet with this ID cannot be found this method will raise an exception

- `getScenarioSets() -> [apex.studies.ScenarioSetNastran]` — Gets a list of all ScenarioSetNastran items in this ScenarioNastran.
- `getSolutionType() -> apex.studies.NastranSolutionType` — Gets Enumeration used to identify the type of solution that will be carried out by a Scenario.
#### `getSubcaseNastran(name: str) -> apex.studies.SubcaseNastran`
Returns the SubcaseNastran identified by the name defined in the argument. If no SubcaseNastran entities can be found with a matching name the method will return None.

- `name` — The name of the SubcaseNastran to return

#### `getSubcases(analysisTypes: [apex.studies.NastranAnalysisType]) -> apex.studies.SubcaseNastranCollection`
Returns a list of Subcases in this Scenario. An optional argument allows the method to return only the subcases of the specific types defined in the optional analysisTypes argument.

- `analysisTypes` — An optional list of analysis types defining the types of Subcases that this method should return If omitted, all Subcases will be returned

- `getSystemCells() -> apex.catalog.SystemCellsSet` — System cells set of the ScenarioNastran.
- `setAnalysis(analysis: apex.studies.NastranAnalysisType) -> None` — Sets enumeration used to define the default ANALYSIS type for this ScenarioNastran. This property is only valid for Scenarios types associated with Nastran Solution 400 or Solution 200 and is used to set the value of the ANALYSIS command ABOVE all subcases.Although the ANALYSIS value can be set within each load case item(SUBCASE, STEP, SUBSTEP), setting it above all SUBCASES removes the need to set it within each load case item The property may be set to either of the values shown below Any value of the apex.studies.NastranAnalysisType.See the documentation for this Enum to determine the range of analysis types supported None - No ANALYSIS entry will be defined above the Subcases Attempting to set this property on a ScenarioNastran that is not associated with Solution 400 or Solution 200 will cause an exception to be raised. NOTE: Not all analysis types defined by the apex.studies.NastranAnalysisType enumeration are supported by Solution 200 or Solution 400. Refer to the table below for valid combinations.Setting an unsupported value will cause this method to raise an exception. Statics 200, 400 Modes 200, 400 Buckling 200, 400 ModalTransient 200,400 ModalFrequency 200, 400 DirectFrequency 200, 400 ModalComplexEigenvalue 200, 400 DirectComplexEigenvalue 200, 400 StaticAeroelasticity 200, 400 StaticAeroelasticDivergence 200, 400 Flutter 200, 400 NonlinearStatics 400 NonlinearTransient 400 NonlinearSteadyStateHeat 400 NonlinearTransientHeat 400.
#### `setParameters(parameters: apex.catalog.ParametersSet) -> None`
set a Parameters set to this ScenarioNastran

- `parameters` — Parameters set of the ScenarioNastran, all PARAMs of the parameter set will be added above sub case within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersBulkData(parametersBulkData: apex.catalog.ParametersSet) -> None`
set a Parameters set to this ScenarioNastran

- `parametersBulkData` — Parameters set of the ScenarioNastran, all PARAMs of the parameter set will be added above sub case within Nastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersByLoadCase(parametersByLoadCase: {str:apex.catalog.ParametersSet}) -> None`
set Parameters set to this ScenarioNastran

- `parametersByLoadCase` — The string keys of the dictionary is the name of the load case. The value is the ParametersSet in this load case. All PARAMs of the parameter set will be added to Load case within ScenarioNastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersByStep(parametersByStep: {str:apex.catalog.ParametersSet}) -> None`
set Parameters set to this ScenarioNastran

- `parametersByStep` — The string keys of the dictionary is the path name of the step. The value is the ParametersSet in this sub step. All PARAMs of the parameter set will be added to Step within ScenarioNastran input file. Omits it if the ParametersType = BulkData.

#### `setParametersBySubStep(parametersBySubStep: {str:apex.catalog.ParametersSet}) -> None`
set Parameters set to this ScenarioNastran

- `parametersBySubStep` — The string keys of the dictionary is the path name of the sub step. The value is the ParametersSet in this sub step. All PARAMs of the parameter set will be added to Step within ScenarioNastran input file. Omits it if the ParametersType = BulkData.

#### `setSystemCells(systemCells: apex.catalog.SystemCellsSet) -> None`
set a System cells set to this ScenarioNastran

- `systemCells` — System cells set of the ScenarioNastran.


## `apex.studies.ScenarioNastranCollection`  (extends `EntityCollection`)

Methods:

- `ScenarioNastranCollection() -> None` — Construct a new ScenarioNastranCollection.

## `apex.studies.ScenarioSetFrequency`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to define a list of Frequency values.
Properties: `values`

Methods:

- `getValues() -> [float]` — Gets a property defining the list of Frequencies that this set represents.
- `setValues(values: [float]) -> None` — Sets a property defining the list of Frequencies that this set represents.

## `apex.studies.ScenarioSetFrfcompId`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to defines a list of IDs of FRFCOMP bulk data entries entries.
Properties: `values`

Methods:

- `getValues() -> [int]` — Gets a property defining the list of IDs of FRFCOMP bulk entries that this set represents.
- `setValues(values: [int]) -> None` — Sets a property defining the list of IDs of FRFCOMP bulk entries that this set represents.

## `apex.studies.ScenarioSetGridComponent`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to define a list Grid components.
Properties: `values`

Methods:

- `getValues() -> [str]` — Gets a property defining the list of Grid components that this set represents Each grid component in the list is represented by the combination of the grid ID and a component code Valid component codes are "T1", "T2", "T3", "R1", "R2", "R3" An example of a list of grid components is shown below ["101/T1", "501/T3", "991/R3"].
- `setValues(values: [str]) -> None` — Sets a property defining the list of Grid components that this set represents Each grid component in the list is represented by the combination of the grid ID and a component code Valid component codes are "T1", "T2", "T3", "R1", "R2", "R3" An example of a list of grid components is shown below ["101/T1", "501/T3", "991/R3"].

## `apex.studies.ScenarioSetGridId`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to define lists of Grid IDs.
Properties: `group`

Methods:

- `clone() -> ScenarioSetNastran` — Creates a copy of this ScenarioSetNastran. The copy will be created by default in the same scenario as the original, however if the optional "scenario_nastran" argument is provided, the copy will be created in the ScenarioNastran that it references All properties of the original ScenarioSetNastran will be copied with the exception of the id which will be replaced by a new unique ID.
- `getGroup() -> apex.Group` — Gets a property defining the list of Grid IDs that this set represents.
- `setGroup(group: apex.Group) -> None` — Sets the Apex Group from which this set extracts its Grids.

## `apex.studies.ScenarioSetModeId`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to define a list of Mode IDs.
Properties: `values`

Methods:

- `getValues() -> [int]` — Gets a property defining the list of Mode IDs that this set represents.
- `setValues(values: [int]) -> None` — Sets a property defining the list of Mode IDs that this set represents.

## `apex.studies.ScenarioSetNastran`  (extends `Entity`)
Base class representing a Nastran case control SET. The Nastran SET case control command is used to define lists of inputs to other commands SETS can be used to define lists of the following types, ID numbers(Grids, Elements, Superelements, Surface, Volume etc.) Frequencies Times Grid point ID plus component type code Specializations of this base class are used to represent each of these list types.
Properties: `id`, `name`

Methods:

- `clone() -> ScenarioSetNastran` — Creates a copy of this ScenarioSetNastran. The copy will be created by default in the same scenario as the original, however if the optional "scenario_nastran" argument is provided, the copy will be created in the ScenarioNastran that it references All properties of the original ScenarioSetNastran will be copied with the exception of the id which will be replaced by a new unique ID.
- `getId() -> int` — Gets an ID for this SET. ScenarioSetNastran ID's must be unique within a Scenario.
- `getName() -> str` — Gets an optional name for this ScenarioSet ScenarioSet names must be unique within a Scenario.
- `setId(id: int) -> None` — Sets an ID for this SET. ScenarioSetNastran ID's must be unique within a Scenario.
- `setName(name: str) -> None` — Sets an optional name for this ScenarioSet ScenarioSet names must be unique within a Scenario.

## `apex.studies.ScenarioSetRandId`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to defines a list of IDs of RANDPS and /or RANDT1 entries.
Properties: `values`

Methods:

- `getValues() -> [int]` — Gets a property defining the list of IDs of RANDPS and/or RANDT1 that this set represents.
- `setValues(values: [int]) -> None` — Sets a property defining the list of IDs of RANDPS and/or RANDT1 that this set represents.

## `apex.studies.ScenarioSetTime`  (extends `ScenarioSetNastran`)
Class representing a Nastran SET case control command to define a list of times.
Properties: `values`

Methods:

- `getValues() -> [float]` — Gets a property defining the list of times that this set represents This property represents a Time quantity and must be defined using the units of Time from the active script unit system.
- `setValues(values: [float]) -> None` — Sets a property defining the list of times that this set represents This property represents a Time quantity and must be defined using the units of Time from the active script unit system.

## `apex.studies.SimulationSettings`
Contains simulation settings that are applical to static, normal modes and buckling scenarios.

Methods:

- `asBucklingSimulationSettings() -> BucklingSimulationSettings`
- `asFrequencyResponseSimulationSettings() -> apex.studies.FrequencyResponseSimulationSettings`
- `asModesSimulationSettings() -> ModesSimulationSettings`
- `asNastranSol400SimulationSettings() -> SimulationSettingsNastranSol400`
- `asSimulationSettingsBucklingNastran() -> apex.studies.SimulationSettingsBucklingNastran`
- `asSimulationSettingsGenerativeDesign() -> SimulationSettingsGenerativeDesign`
- `asSimulationSettingsModesNastran() -> apex.studies.SimulationSettingsModesNastran`
- `asSimulationSettingsStaticNastran() -> apex.studies.SimulationSettingsStaticNastran`
- `asStaticSimulationSettings() -> StaticSimulationSettings`

## `apex.studies.SimulationSettingsBucklingNastran`  (extends `SimulationSettings`)
This class manages the simulation settings for Buckling Simulation Steps. An instance of this class is created and populated with default values whenever a Buckling Step is created.
Properties: `interactionControl`, `numBucklingModes`, `solverControlSettings`

Methods:

#### `SimulationSettingsBucklingNastran(interactionControl: apex.studies.InteractionControl, solverControlSettings: apex.studies.SolverControlSettingsNastran, numBucklingModes: int) -> None`
This class manages the simulation settings for Buckling Simulation Steps. An instance of this class is created and populated with default values whenever a Buckling Step is created.

- `interactionControl` — Optional - Interaction control setting for the scenario
- `solverControlSettings` — Solver control settings for the scenario.
- `numBucklingModes` — The number of buckling modes (default = 10) to recover during the simulation.

- `getInteractionControl() -> apex.studies.InteractionControl` — Interaction control settings for the scenario.
- `getNumBucklingModes() -> int` — The number of buckling modes (default = 10) to recover during the simulation.
- `getSolverControlSettings() -> apex.studies.SolverControlSettingsNastran` — Solver control settings for the scenario.
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None` — Interaction control settings for the scenario.
- `setNumBucklingModes(numBucklingModes: int) -> None` — The number of buckling modes (default = 10) to recover during the simulation.
- `setSolverControlSettings(solverControlSettings: apex.studies.SolverControlSettingsNastran) -> None` — Solver control settings for the scenario.
#### `update(interactionControl: apex.studies.InteractionControl, solverControlSettings: apex.studies.SolverControlSettingsNastran, numBucklingModes: int) -> None`
Update the simulation settings.

- `interactionControl` — Optional - Interaction control setting for the scenario
- `solverControlSettings` — Solver control settings for the scenario.
- `numBucklingModes` — The number of buckling modes (default = 10) to recover during the simulation.


## `apex.studies.SimulationSettingsGenerativeDesign`  (extends `SimulationSettings`)
class representing settings used by the generative design solver during simulation of the Scenario.
Properties: `advancedSettingGenerativeDesign`, `buildDirection`, `complexity`, `designRules`, `failureSettings`, `frequencyConstraintEvent`, `frequencyConstraintGlobal`, `keepConstraintRegions`, `keepInterfaceRegions`, `keepLoadRegions`, `keepNonDesignRegions`, `manufacturingMethod`, `shapeQuality`, `strutDensity`

Methods:

- `getAdvancedSettings() -> AdvancedSettingGenerativeDesign` — returns the AdvancedSettingGenerativeDesign object from this Scenario. If a AdvancedSettingGenerativeDesign object does not exits for this Scenario the method will return None
- `getBuildDirection() -> apex.IOrientation` — Get the build direction of the SimulationSettings.
- `getComplexity() -> float` — indirectly controls the initial complexity of the model during simulation by specifying the amount of memory to use for the simulation. Higher values for complexity will cause the solution to generated a very fine grained simulation model which generally leads to "better" final shapes, but at the expense of compute time.
- `getDesignRules() -> DesignRules` — The argument defines how the current scenario take the design rules.
- `getFailureSettings() -> FailureSettings` — The argument defines how the current scenario take the failure settings.
- `getFrequencyConstraintEvent() -> {str:float}` — a dictionary to define the frequency constraint for each event in this scenario. The key is the event name and the value is a float value, for example frequencyConstraintEvent = {"Event 1": 100.0, "Event 2": 126.00}. The events applied with frequencyConstraintEvent will ignore the value from frequencyConstraintGlobal since the latter is a default settings. The frequency constraint only makes sense for the events with at least one displacement constraint and without any loads. The frequency constraint sets a minimum frequency target for the 1st normal mode frequency of the design target.
- `getFrequencyConstraintGlobal() -> float` — a float value to define the frequency constraint applied to the scenario - all events in this scenario will have the same frequency constraint if the frequency constraint of the event is not set. The frequency constraint only makes sense for the events with at least one displacement constraint and without any loads. The frequency constraint sets a minimum frequency target for the 1st normal mode frequency of the design target.
- `getKeepConstraintRegions() -> [str]` — The argument defines a list constraint objects which application regions to be kept during optimization by name. If it is empty, the constraint application regions may be removed during optimization. If constraint objects are set through the argument, the solver will keep the constraint application regions during optimization. If the constraint objects setting through the argument are not associated to environment of the scenario, the system will give an error.
- `getKeepInterfaceRegions() -> [str]` — The argument defines a list interfaces objects to be kept during optimization by name. If it is empty or undefined, the interface regions may be removed during optimization. If the interface objects are set through the argument, the solver will keep the interface regions during optimization. If the interface setting through the argument are not associated to the model rep, the system will give an error.
- `getKeepLoadRegions() -> [str]` — The argument defines a list load objects which application regions to be kept during optimization by name. If it is empty, the load's application regions may be removed during optimization. If load objects are set through the argument, the solver will keep the load application regions during optimization. If the loads setting through the argument are not associated to environment of the scenario, the system will give an error.
- `getKeepNonDesignRegions() -> [str]` — The argument defines a list non-design regions objects to be kept during optimization by name. If it is empty or undefined, the Non-Design regions may be removed during optimization. If Non-Design regions objects are set through the argument, the solver will keep the Non-Design regions during optimization. If the Non-Design regions setting through the argument are not associated to the model rep, the system will give an error.
- `getManufacturingMethod() -> ManufacturingMethod` — Enumeration argument to guide the type of manufacturing method that will be generated by the solver.
- `getShapeQuality() -> ShapeQuality` — Enumeration argument to control the quality of the shape that will be generated. Use apex.gendes.ShapeQuality.Preview for a rapid, coarse grained simulation that will provide a non-optimal, but representative shape. This setting is normally used when first setting up a new simulation to ensure that all other settings are valid, prior to re-running the simulation with a better shapeQuality setting. Use apex.gendes.ShapeQuality.Balanced (Default) for a simulation that balances compute time with quality of the computed shape. Use apex.gendes.ShapeQuality.FineTune for a simulation that generates the best quality of the computed shape.
- `getStrutDensity() -> StrutDensity` — Enumeration argument to guide the type of shape that will be generated by the solver. In order to meet different end user manufacturing, functional or aesthetic considerations the generative design solver can be directed to generated different types of shapes. Setting this argument to "Sparse" will cause the solver to preferentially generate shapes that may include many fine or narrow regions whereas setting the value to "Dense" will cause the final shape to have fewer but larger regions.
- `setAdvancedSettings(advancedSetting: AdvancedSettingGenerativeDesign) -> None` — returns the AdvancedSettingGenerativeDesign object from this Scenario. If a AdvancedSettingGenerativeDesign object does not exits for this Scenario the method will return None
- `setBuildDirection(buildDirection: apex.IOrientation) -> None` — Define the build direction using an orientation object. Please Note: So the default value should be got from the associated material. (we provide a private member for the related material of the current analysis scenario. From the material we can get the materialType and the material coverageRegions. From the coverageRegions object,we can get the material orientation.) If buildDirection is set to None, switch to use the material orientation. If buildDirection is set to an IOrientation object, switch to use the defined orientation.
- `setComplexity(complexity: float) -> None` — indirectly controls the initial complexity of the model during simulation by specifying the amount of memory to use for the simulation. Higher values for complexity will cause the solution to generated a very fine grained simulation model which generally leads to "better" final shapes, but at the expense of compute time.
- `setDesignRules(designRules: DesignRules) -> None` — The argument defines how the current scenario take the design rules.
- `setFailureSettings(failureSettings: FailureSettings) -> None` — The argument defines how the current scenario take the failure settings.
- `setFrequencyConstraintEvent(frequencyConstraintEvent: {str:float}) -> None` — a dictionary to define the frequency constraint for each event in this scenario. The key is the event name and the value is a float value, for example frequencyConstraintEvent = {"Event 1": 100.0, "Event 2": 126.00}. The events applied with frequencyConstraintEvent will ignore the value from frequencyConstraintGlobal since the latter is a default settings. The frequency constraint only makes sense for the events with at least one displacement constraint and without any loads. The frequency constraint sets a minimum frequency target for the 1st normal mode frequency of the design target.
- `setFrequencyConstraintGlobal(frequencyConstraintGlobal: float) -> None` — a float value to define the frequency constraint applied to the scenario - all events in this scenario will have the same frequency constraint if the frequency constraint of the event is not set. The frequency constraint only makes sense for the events with at least one displacement constraint and without any loads. The frequency constraint sets a minimum frequency target for the 1st normal mode frequency of the design target.
- `setKeepConstraintRegions(keepConstraintRegions: [str]) -> None` — The argument defines a list constraint objects which application regions to be kept during optimization by name. If it is empty, the constraint application regions may be removed during optimization. If constraint objects are set through the argument, the solver will keep the constraint application regions during optimization. If the constraint objects setting through the argument are not associated to environment of the scenario, the system will give an error.
- `setKeepInterfaceRegions(keepInterfaceRegions: [str]) -> None` — The argument defines a list interfaces objects to be kept during optimization by name. If it is empty or undefined, the interface regions may be removed during optimization. If the interface objects are set through the argument, the solver will keep the interface regions during optimization. If the interface setting through the argument are not associated to the model rep, the system will give an error.
- `setKeepLoadRegions(keepLoadRegions: [str]) -> None` — The argument defines a list load objects which application regions to be kept during optimization by name. If it is empty, the load's application regions may be removed during optimization. If load objects are set through the argument, the solver will keep the load application regions during optimization. If the loads setting through the argument are not associated to environment of the scenario, the system will give an error.
- `setKeepNonDesignRegions(keepNonDesignRegions: [str]) -> None` — The argument defines a list non-design regions objects to be kept during optimization by name. If it is empty or undefined, the Non-Design regions may be removed during optimization. If Non-Design regions objects are set through the argument, the solver will keep the Non-Design regions during optimization. If the Non-Design regions setting through the argument are not associated to the model rep, the system will give an error.
- `setManufacturingMethod(manufacturingMethod: ManufacturingMethod) -> None` — Enumeration argument to guide the type of manufacturing method that will be generated by the solver. used to define the manufacturing Method
- `setShapeQuality(shapeQuality: ShapeQuality) -> None` — Enumeration argument to control the quality of the shape that will be generated. Use apex.gendes.ShapeQuality.Preview for a rapid, coarse grained simulation that will provide a non-optimal, but representative shape. This setting is normally used when first setting up a new simulation to ensure that all other settings are valid, prior to re-running the simulation with a better shapeQuality setting. Use apex.gendes.ShapeQuality.Balanced (Default) for a simulation that balances compute time with quality of the computed shape. Use apex.gendes.ShapeQuality.FineTune for a simulation that generates the best quality of the computed shape.
- `setStrutDensity(strutDensity: StrutDensity) -> None` — Enumeration argument to guide the type of shape that will be generated by the solver. In order to meet different end user manufacturing, functional or aesthetic considerations the generative design solver can be directed to generated different types of shapes. Setting this argument to "Sparse" will cause the solver to preferentially generate shapes that may include many fine or narrow regions whereas setting the value to "Dense" will cause the final shape to have fewer but larger regions. Use the default "Medium" value to generate a balanced shape.

## `apex.studies.SimulationSettingsModesNastran`  (extends `SimulationSettings`)
This class manages the simulation settings for Normal Modes Simulation Steps. An instance of this class is created and populated with default values whenever a Normal Modes Step is created.
Properties: `frequencyBoundLower`, `frequencyBoundUpper`, `interactionControl`, `maxNumModes`, `solverControlSettings`, `stopCalculation`

Methods:

#### `SimulationSettingsModesNastran(frequencyBoundLower: float, frequencyBoundUpper: float, interactionControl: apex.studies.InteractionControl, solverControlSettings: apex.studies.SolverControlSettingsNastran, stopCalculation: bool, maxNumModes: int) -> None`
Constructor of the simulation settings.

- `frequencyBoundLower` — The lower bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies lower than this value will be ignored. If undefined (default), no lower bound will be applied and all modes will be recovered including modes with negative frequencies
- `frequencyBoundUpper` — The upper bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies higher than this value will be ignored. If undefined (default), no upper bound will be applied and all modes will be recovered.
- `interactionControl` — Optional - Interaction control setting for the scenario
- `solverControlSettings` — Solver control settings for the scenario.
- `stopCalculation` — Stop calculation based on maximum number of modes
- `maxNumModes` — The maximum number of modes (default = 10) to recover during solution

- `getFrequencyBoundLower() -> float` — The lower bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies lower than this value will be ignored. If undefined (default), no lower bound will be applied and all modes will be recovered including modes with negative frequencies.
- `getFrequencyBoundUpper() -> float` — The upper bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies higher than this value will be ignored. If undefined (default), no upper bound will be applied and all modes will be recovered.
- `getInteractionControl() -> apex.studies.InteractionControl` — Interaction control settings for the scenario.
- `getMaxNumModes() -> int` — The maximum number of modes (default = 10) to recover during solution.
- `getSolverControlSettings() -> apex.studies.SolverControlSettingsNastran` — Solver control settings for the scenario.
- `getStopCalculation() -> bool` — Stop calculation based on maximum number of modes.
- `setFrequencyBoundLower(freqRangeLower: float) -> None` — The lower bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies lower than this value will be ignored. If undefined (default), no lower bound will be applied and all modes will be recovered including modes with negative frequencies.
- `setFrequencyBoundUpper(freqRangeUpper: float) -> None` — The upper bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies higher than this value will be ignored. If undefined (default), no upper bound will be applied and all modes will be recovered.
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None` — Interaction control settings for the scenario.
- `setMaxNumModes(maxModes: int) -> None` — The maximum number of modes (default = 10) to recover during solution.
- `setSolverControlSettings(solverControlSettings: apex.studies.SolverControlSettingsNastran) -> None` — Solver control settings for the scenario.
- `setStopCalculation(stopCalculation: bool) -> None` — Stop calculation based on maximum number of modes.
#### `update(frequencyBoundLower: float, frequencyBoundUpper: float, interactionControl: apex.studies.InteractionControl, solverControlSettings: apex.studies.SolverControlSettingsNastran, stopCalculation: apex.ApexBool, maxNumModes: int) -> None`
Updates all properties of the this settings.

- `frequencyBoundLower` — The lower bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies lower than this value will be ignored. If undefined (default), no lower bound will be applied and all modes will be recovered including modes with negative frequencies
- `frequencyBoundUpper` — The upper bound value of modal frequencies that will be recovered by the normal modes solutions. Modal frequencies higher than this value will be ignored. If undefined (default), no upper bound will be applied and all modes will be recovered.
- `interactionControl` — Optional - Interaction control setting for the scenario
- `solverControlSettings` — Solver control settings for the scenario.
- `stopCalculation` — Stop calculation based on maximum number of modes
- `maxNumModes` — The maximum number of modes (default = 10) to recover during solution


## `apex.studies.SimulationSettingsNastranSol400`  (extends `SimulationSettings`)
This class manages the simulation settings for nonlinear scenario of Nastran Sol400.
Properties: `interactionControl`, `solverControlSettings`, `stepSettings`

Methods:

#### `SimulationSettingsNastranSol400(interactionControl: apex.studies.InteractionControl, stepSettings: {str:apex.studies.NastranSol400StepSettings}, solverControlSettings: apex.studies.SolverControlSettingsNastran) -> None`
Constructor of the simulation setting for nonlinear scenario(Sol400).

- `interactionControl` — Optional - Interaction control setting for the scenario
- `stepSettings` — A dictionary to define Step setting for nonlinear scenario steps. The key is a string of the path name of the step, the value is the class of NastranSol400StepSettings.
- `solverControlSettings` — Optional-Solver control settings for the scenario.

- `getInteractionControl() -> apex.studies.InteractionControl`
- `getSolverControlSettings() -> apex.studies.SolverControlSettingsNastran` — Solver control settings for the scenario.
- `getStepSettings() -> {str:apex.studies.NastranSol400StepSettings}`
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None`
- `setSolverControlSettings(solverControlSettings: apex.studies.SolverControlSettingsNastran) -> None` — Solver control settings for the scenario.
- `setStepSettings(stepSettings: {str:apex.studies.NastranSol400StepSettings}) -> None`
#### `update(interactionControl: apex.studies.InteractionControl, stepSettings: {str:apex.studies.NastranSol400StepSettings}, solverControlSettings: apex.studies.SolverControlSettingsNastran) -> None`
Update the simulation setting for nonlinear scenario(Sol400).

- `interactionControl` — Optional - Interaction control setting for the scenario
- `stepSettings` — A dictionary to define Step setting for nonlinear scenario steps. The key is a string of the path name of the step, the value is the class of NastranSol400StepSettings.
- `solverControlSettings` — Optional-Solver control settings for the scenario.


## `apex.studies.SimulationSettingsStaticNastran`  (extends `SimulationSettings`)
This class manages the simulation settings for Static Simulation Steps.
Properties: `enableMechanismCheck`, `interactionControl`, `solverControlSettings`

Methods:

#### `SimulationSettingsStaticNastran(interactionControl: apex.studies.InteractionControl, solverControlSettings: apex.studies.SolverControlSettingsNastran, enableMechanismCheck: bool) -> None`
SimulationSettingsStaticNastran Constructor.

- `interactionControl` — Optional - Interaction control setting for the scenario
- `solverControlSettings` — Solver control settings for the scenario.
- `enableMechanismCheck` — Boolean flag to indicate whether the solver should produce diagnostic results if a mechanism is detected during solution. If True (default) and a mechanism is detected during solution, Apex will produce diagnostic results (displacements) that can be viewed in post-processing to help diagnose the mechanism. If False and a mechanism is detected during solution, Apex will immediatly terminate the solution report a mechanism error

- `getEnableMechanismCheck() -> bool` — Boolean flag to indicate whether the solver should produce diagnostic results if a mechanism is detected during solution. If True (default) and a mechanism is detected during solution, Apex will produce diagnostic results (displacements) that can be viewed in post-processing to help diagnose the mechanism. If False and a mechanism is detected during solution, Apex will immediatly terminate the solution report a mechanism error.
- `getInteractionControl() -> apex.studies.InteractionControl` — Interaction control settings for the scenario.
- `getSolverControlSettings() -> apex.studies.SolverControlSettingsNastran` — Solver control settings for the scenario.
- `setEnableMechanismCheck(mechanismCheck: bool) -> None` — Boolean flag to indicate whether the solver should produce diagnostic results if a mechanism is detected during solution. If True (default) and a mechanism is detected during solution, Apex will produce diagnostic results (displacements) that can be viewed in post-processing to help diagnose the mechanism. If False and a mechanism is detected during solution, Apex will immediatly terminate the solution report a mechanism error.
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None` — Interaction control settings for the scenario.
- `setSolverControlSettings(solverControlSettings: apex.studies.SolverControlSettingsNastran) -> None` — Solver control settings for the scenario.
#### `update(interactionControl: apex.studies.InteractionControl, solverControlSettings: apex.studies.SolverControlSettingsNastran, enableMechanismCheck: apex.ApexBool) -> None`
Update the SimulationSettingsStaticNastran.

- `interactionControl` — Optional - Interaction control setting for the scenario
- `solverControlSettings` — Solver control settings for the scenario.
- `enableMechanismCheck` — Boolean flag to indicate whether the solver should produce diagnostic results if a mechanism is detected during solution. If True (default) and a mechanism is detected during solution, Apex will produce diagnostic results (displacements) that can be viewed in post-processing to help diagnose the mechanism. If False and a mechanism is detected during solution, Apex will immediatly terminate the solution report a mechanism error


## `apex.studies.SolverControlSettingsNastran`
This class provides access to a Nastran solver control settings that are applicable to most Nastran simulation types (Solution sequences). Solution specific simulation settings are provided in other classes.
Properties: `automaticConstraints`, `dataDeckEcho`, `exportAbstractions`, `exportHierarchicalFiles`, `exportProperty`, `exportWideFormat`, `massCalcuationMethod`, `maxPrintLines`, `maxRunTime`, `nodeForWeightGeneration`, `plateStiffnessFactor`, `resultOutputType`, `shellNormalTolerance`, `unitSystem`, `wtmass`

Methods:

#### `SolverControlSettingsNastran(nodeForWeightGeneration: int, maxRunTime: float, maxPrintLines: int, unitSystem: str, automaticConstraints: bool = True, shellNormalTolerance: float = 20.0f, plateStiffnessFactor: float = 100.0f, wtmass: float = 1.0f, exportAbstractions: bool = False, exportWideFormat: bool = False, exportHierarchicalFiles: bool = False, massCalcuationMethod: apex.studies.MassCalculationMethod = apex.studies.MassCalculationMethod.Lumped, dataDeckEcho: apex.studies.DataDeckEcho = apex.studies.DataDeckEcho.Unset, resultOutputType: apex.attribute.NastranResultOutputType = apex.attribute.NastranResultOutputType.Hdf5, exportProperty: apex.ExportProperty = apex.ExportProperty.AsDefined) -> None`
Constructor of nastran solver control settings.

- `nodeForWeightGeneration` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. Specify the node weight generator to be executed. if undefined, no node weight generator will be executed if it is 0, the reference point is taken as the origin of the basic coordinate system it is Node ID, the node weight generator will be executed
- `maxRunTime` — the maximum CPU time.maxRunTime represents an Time quantity and must be defined using the units of Time from the active script unit system
- `maxPrintLines` — the maximum number of output lines
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `automaticConstraints` — boolean property that controls whether Nastran will automatically constrain singular degrees of freedom. Setting automaticConstraints = True will cause Nastran to automatically constrain any singular degrees of freedom in the stiffness matrix. Setting the value to False will allow the singular degrees of freedom to remain
- `shellNormalTolerance` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. requests the generation of unique grid point normals for adjacent shell elements. shellNormalTolerance represents an Angle quantity and must be defined using the units of Angle from the active script unit system
- `plateStiffnessFactor` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. specifies the scaling factor of the penalty stiffness to be added to the normal rotation for CQUAD4 and CTRIA3 elements
- `wtmass` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. Scale factor that will be used to scale all structural mass and density values in the exported file. If omitted, density and mass values in the exported file will be scaled by the value of 1.0.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the export) to be written.
- `massCalcuationMethod` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. mass calculation method to be used. 1.Lumped, generation of lumped mass matrices 2.Coupled, generation of Coupled mass matrices
- `dataDeckEcho` — Controls echo (i.e., printout) of the Bulk Data
- `resultOutputType` — An enumeration to define which Nastran results file format will be requested in the exported file. The default is HDF5 results output.
- `exportProperty` — Optional boolean argument that controls whether the property is written on element entry or it is written as a separated entry in the exported file.

- `getAutomaticConstraints() -> bool` — boolean property that controls whether Nastran will automatically constrain singular degrees of freedom. Setting automaticConstraints = True will cause Nastran to automatically constrain any singular degrees of freedom in the stiffness matrix. Setting the value to False will allow the singular degrees of freedom to remain
- `getDataDeckEcho() -> apex.studies.DataDeckEcho` — Controls echo (i.e., printout) of the Bulk Data.
- `getExportAbstractions() -> bool` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `getExportHierarchicalFiles() -> bool` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the export) to be written.
- `getExportProperty() -> apex.ExportProperty` — Optional boolean argument that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `getExportWideFormat() -> bool` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `getMassCalcuationMethod() -> apex.studies.MassCalculationMethod` — mass calculation method to be used. 1.Lumped, generation of lumped mass matrices 2.Coupled, generation of Coupled mass matrices
- `getMaxPrintLines() -> int` — the maximum number of output lines
- `getMaxRunTime() -> float` — the maximum CPU time. maxRunTime represents an Time quantity and must be defined using the units of Time from the active script unit system
- `getNodeForWeightGeneration() -> int` — Specify the node weight generator to be executed.
- `getPlateStiffnessFactor() -> float` — specifies the scaling factor of the penalty stiffness to be added to the normal rotation for CQUAD4 and CTRIA3 elements
- `getResultOutputType() -> apex.attribute.NastranResultOutputType` — An enumeration to define which Nastran results file format will be requested in the exported file. The default is HDF5 results output.
- `getShellNormalTolerance() -> float` — requests the generation of unique grid point normals for adjacent shell elements. shellNormalTolerance represents an Angle quantity and must be defined using the units of Angle from the active script unit system
- `getUnitSystem() -> str` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `getWtmass() -> float` — Scale factor that will be used to scale all structural mass and density values in the exported file. If omitted, density and mass values in the exported file will be scaled by the value of 1.0.
- `setAutomaticConstraints(automaticConstraints: bool) -> None` — boolean property that controls whether Nastran will automatically constrain singular degrees of freedom. Setting automaticConstraints = True will cause Nastran to automatically constrain any singular degrees of freedom in the stiffness matrix. Setting the value to False will allow the singular degrees of freedom to remain
- `setDataDeckEcho(dataDeckEcho: apex.studies.DataDeckEcho) -> None` — Controls echo (i.e., printout) of the Bulk Data.
- `setExportAbstractions(exportAbstractions: bool) -> None` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `setExportHierarchicalFiles(exportHierarchicalFiles: bool) -> None` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the export) to be written.
- `setExportProperty(exportProperty: apex.ExportProperty) -> None` — Optional boolean argument that controls whether the property is written on element entry or it is written as a separated entry in the exported file.
- `setExportWideFormat(exportWideFormat: bool) -> None` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `setMassCalcuationMethod(massCalcuationMethod: apex.studies.MassCalculationMethod) -> None` — mass calculation method to be used. 1.Lumped, generation of lumped mass matrices 2.Coupled, generation of Coupled mass matrices
- `setMaxPrintLines(maxPrintLines: int) -> None` — the maximum number of output lines
- `setMaxRunTime(maxRunTime: float) -> None` — the maximum CPU time. maxRunTime represents an Time quantity and must be defined using the units of Time from the active script unit system
- `setNodeForWeightGeneration(nodeForWeightGeneration: int) -> None` — Specify the node weight generator to be executed.
- `setPlateStiffnessFactor(plateStiffnessFactor: float) -> None` — specifies the scaling factor of the penalty stiffness to be added to the normal rotation for CQUAD4 and CTRIA3 elements
- `setResultOutputType(resultOutputType: apex.attribute.NastranResultOutputType) -> None` — An enumeration to define which Nastran results file format will be requested in the exported file. The default is HDF5 results output.
- `setShellNormalTolerance(shellNormalTolerance: float) -> None` — requests the generation of unique grid point normals for adjacent shell elements. shellNormalTolerance represents an Angle quantity and must be defined using the units of Angle from the active script unit system
- `setUnitSystem(unitSystem: str) -> None` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `setWtmass(wtmass: float) -> None` — Scale factor that will be used to scale all structural mass and density values in the exported file. If omitted, density and mass values in the exported file will be scaled by the value of 1.0.
#### `update(nodeForWeightGeneration: int, maxRunTime: float, maxPrintLines: int, unitSystem: str, automaticConstraints: apex.ApexBool, shellNormalTolerance: float, plateStiffnessFactor: float, wtmass: float, exportAbstractions: apex.ApexBool, exportWideFormat: apex.ApexBool, exportHierarchicalFiles: apex.ApexBool, massCalcuationMethod: apex.studies.MassCalculationMethod, dataDeckEcho: apex.studies.DataDeckEcho, resultOutputType: apex.attribute.NastranResultOutputType, exportProperty: apex.ExportProperty) -> None`
Update the nastran solver control settings.

- `nodeForWeightGeneration` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. Specify the node weight generator to be executed. if undefined, no node weight generator will be executed if it is 0, the reference point is taken as the origin of the basic coordinate system it is Node ID, the node weight generator will be executed
- `maxRunTime` — the maximum CPU time.maxRunTime represents an Time quantity and must be defined using the units of Time from the active script unit system
- `maxPrintLines` — the maximum number of output lines
- `unitSystem` — The name of a consistent unit system to use when exporting Nastran files, for example "mm-kg-s-N", "in-slinch-s-lbf".
- `automaticConstraints` — boolean property that controls whether Nastran will automatically constrain singular degrees of freedom. Setting automaticConstraints = True will cause Nastran to automatically constrain any singular degrees of freedom in the stiffness matrix. Setting the value to False will allow the singular degrees of freedom to remain
- `shellNormalTolerance` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. requests the generation of unique grid point normals for adjacent shell elements. shellNormalTolerance represents an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `plateStiffnessFactor` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. specifies the scaling factor of the penalty stiffness to be added to the normal rotation for CQUAD4 and CTRIA3 elements
- `wtmass` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. Scale factor that will be used to scale all structural mass and density values in the exported file. If omitted, density and mass values in the exported file will be scaled by the value of 1.0.
- `exportAbstractions` — Optional boolean argument (Default = False) that controls whether the exported file will include Nastran ABSTRCT and/or NAMVAL keywords that preserve Apex specific data, not directly support by Nastran, within the Nastran file. This data passes through the solver to the output .h5 file without otherwise impacting the solution and can be used during a subsequent import of the Nastran model to Apex to reconstruct "rich" Apex objects from the "raw" Nastran keywords.
- `exportWideFormat` — A boolean value that controls whether the exported data is written using Nastran Wide format (16 characters per keyword field) or not. The default value is "False" - causing the data to be written in narrow format (8 characters per field).
- `exportHierarchicalFiles` — A Boolean quantity to control whether the exported data is written as a series of hierarchical include files that mirrors the Assembly/Part product structure, or as a single Flat file. The default for this argument is "False" - causing a single Flat file containing the entire model (matching the scope of the export) to be written.
- `massCalcuationMethod` — THIS ARGUMENT WILL BE DEPRECATED AND WILL BE RMOVED IN A FUTURE RELEASE. mass calculation method to be used. 1.Lumped, generation of lumped mass matrices 2.Coupled, generation of Coupled mass matrices
- `dataDeckEcho` — Controls echo (i.e., printout) of the Bulk Data
- `resultOutputType` — An enumeration to define which Nastran results file format will be requested in the exported file. The default is HDF5 results output.
- `exportProperty` — Optional boolean argument that controls whether the property is written on element entry or it is written as a separated entry in the exported file.


## `apex.studies.StaticSimulationSettings`  (extends `SimulationSettings`)
This class manages the StaticSimulationSettings for Static Simulation Steps. An instance of this class is created and populated with default values whenever a StaticStep is created StaticStep is a type of Step used to define and analyze load environments where the loads do not vary with time or frequency and dynamic effects need not be considered. <NOTE TO DEVELOPER - DO NOT INCLUDE IN IL IMPLEMENTATION - THIS IS FOR NONLINEAR STATIC STEPS IN JAGUAR> The StaticStep is used to represent both linear and nonlinear static behavior. For nonlinear cases the Step (including application of the loads) is defined to take place over a user defined period of "pseudo time".
Properties: `interactionControl`, `mechanismCheck`

Methods:

- `getInteractionControl() -> apex.studies.InteractionControl`
- `getMechanismCheck() -> bool`
- `setInteractionControl(interactionControl: apex.studies.InteractionControl) -> None`
- `setMechanismCheck(mechanismCheck: bool) -> None`

## `apex.studies.StaticStep`  (extends `Step`)
StaticStep is a type of Step used to define and analyze load environments where the loads do not vary with time or frequency and dynamic effects need not be considered. The Static Step will be used to represent both linear and nonlinear static behavior.

Methods:

- `activateInertiaRelief() -> None` — Activates Inertia Relief for this StaticStep.
- `deactivateInertiaRelief() -> None` — De-activates Inertia Relief for this StaticStep.
#### `getSimulationSettings() -> apex.studies.StaticSimulationSettings`
returns the StaticSimulationSettings from this Scenario

Returns: the StaticSimulationSettings object


## `apex.studies.StaticStepNastranSol400`  (extends `StaticStep`)
Static step of Nastran sol400.

Methods:

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/

#### `update(name: str, description: str, initialStepState: apex.studies.InitialStepState, loadCase: apex.studies.LoadCase, step: apex.studies.Step, loadFactor: float, id: int) -> None`
update the step.

- `name` — Optional-Name of the step
- `description` — Optional-description of the Step.
- `initialStepState` — Initial Step State for the new step.
- `loadCase` — Optional-Load Case for the initial step state of the step to be created. The option is only available when initialStepState = StepInAnotherLoadCase.
- `step` — Optional-Step for the initial step state of the step to be created. The option is only available when initialStepState = StepInAnotherLoadCase or StepInThisLoadCase.
- `loadFactor` — Optional-Load factor for the initial step state.
- `id` — Optional-Id of the step.


## `apex.studies.Step`  (extends `Entity`, `IName`, `IUserAttributes`)
A Step defines a collection of Loads, Constraints and Simulation Settings that will cause the state of the mechanical system to be changed. Steps are typed,.
Properties: `constraints`, `events`, `loads`, `outputRequests`

Methods:

#### `addConstraints(constraints: apex.EntityCollection) -> None`
Add one or more constraints to the step.

- `constraints` — A List of constraints to be added to the steps.

#### `addEvent(name: str = "") -> apex.studies.Event`
Adds an Event to this Step using the supplied name and returns the Event. The Event name must be unique within the Step. If an Event with the same name already exists within the Step the system will automatically modify the supplied name to make it unique.

- `name` — The name that will be assigned to the Event created by this method

Returns: Event object

#### `addLoads(loads: apex.EntityCollection, loadReps: apex.EntityCollection) -> None`
Add one or more loads to the step.

- `loads` — A List of loads to be added to the steps. If a load has multiple loadReps, omits the load.
- `loadReps` — A List of LoadReps to be added to the steps.

#### `duplicateEvent(event: Event) -> apex.studies.Event`
duplicate a new Event from the given one.

- `event` — The given child event of current Step

Returns: returns an single Event in a Step

- `getConstraints() -> apex.EntityCollection` — Return a collection of Constraint objects that are associated with this Step.
#### `getEvent(name: str) -> apex.studies.Event`
Retrieves a single Event from the Step using the supplied name. If an Event with a matching name does not exist within the Step the method will throw an exception.

- `name` — The name of the Event

Returns: returns an single Event in a Step

#### `getEvents() -> apex.studies.EventCollection`
retrieves an ordered collection of the Steps in a Scenario

Returns: an ordered collection of the Steps in a Scenario

- `getLoads() -> apex.EntityCollection` — Return a collection of LoadRep or Load objects that don't have LoadReps that are associated with this event.
- `getOutputRequests() -> [apex.studies.OutputRequestQuantities]` — A list of output requests of the step. If it is undefined, the system will provide default output request for each step type.
#### `removeConstraints(constraints: apex.EntityCollection) -> None`
Remove one or more constraints to the step.

- `constraints` — A List of constraints to be removed from the steps.

#### `removeEvent(name: str = "#####") -> None`
Removes an Event from the Step. The Event to be deleted may be supplied by name or by object.

- `name` — The name of the Event to be removed from the Step. If the name does not exist in the Step the method will return False. If the name argument is supplied the 'event' argument must be omitted or the method will throw an exception

#### `removeLoads(loads: apex.EntityCollection, loadReps: apex.EntityCollection) -> None`
Remove one or more loads from the step.

- `loads` — A List of loads to be removed from the step. If a load has multiple loadReps, omits the load.
- `loadReps` — A List of LoadReps to be removed from the step.

- `setOutputRequests(outputRequests: [apex.studies.OutputRequestQuantities]) -> None` — A list of output requests of the step. If it is undefined, the system will provide default output request for each step type.
#### `update(name: str, simulationSettings: apex.studies.SimulationSettings) -> None`
Update this Step.

- `name` — the name that will be set to this Step
- `simulationSettings` — the SimulationSettings that will be assoicated with this Step


## `apex.studies.StepCollection`  (extends `EntityCollection`)

Methods:

- `StepCollection() -> None` — Construct a new StepCollection.

## `apex.studies.StepNastran`  (extends `LoadCaseItem`)
Properties: `stepID`, `substeps`

Methods:

#### `createSubsteps(substep_analysis_types: [apex.studies.NastranAnalysisTypeNS.value], name: str, description: str) -> apex.studies.SubstepNastranCollection`
Creates and returns a pair of Substeps and adds them to this Step. The analysis types of the Substep must be defined using the analysisTypes argument. Steps and Substeps are only available in Scenarios with solution type NONLINEAR_400 Steps composing Substeps must compose two Substeps and the analysis types of those Substeps must match the following, order dependent, analysis type pairs,.

- `substep_analysis_types` — A list of two NastranAnalysis type enumerations defining the analysis types of the Substeps to be created.
- `name` — an optional name (prefix) for the Subteps that will be created. If omitted, Apex will assign unique default Substep names
- `description` — an optional description for the Substeps that are being created. The same description will be assigned to both of the new Substeps

Returns: returns a list of Steps composed by this Subcase.

First Substep = NonlinearSteadyStateHeat, Second Substep = NonlinearStatics First Substep = NonlinearTransientHeat, Second Substep = NonlinearTransient First Substep = NonlinearTransientHeat, Second Substep = NonlinearStatics First Substep = NonlinearSteadyStateHeat, Second Substep = NonlinearTransient This method will raise an exception if used to attempt creation of invalid analysis type pairs

- `getAnalysisType() -> apex.studies.NastranAnalysisType` — Gets Enumeration used to identify the type of Analysis that will be carried out by a Subcase.
- `getStepID() -> int` — Gets an ID for this StepNastran Step IDs must be unique and monotonically increasing (with Step order) within a SubcaseNastran.
#### `getSubstepNastran(name: str) -> apex.studies.SubstepNastran`
Returns the SubstepNastran identified by the name defined in the argument. If no SubstepNastran entities can be found with a matching name the method will return None.

- `name` — The name of the SubstepNastran to return

#### `getSubsteps(analysisTypes: [apex.studies.NastranAnalysisType]) -> apex.studies.SubstepNastranCollection`
Returns a list of Substeps in this Scenario. An optional argument allows the method to return only the substeps of the specific types defined in the optional analysisTypes argument.

- `analysisTypes` — An optional list of analysis types defining the types of Substep that this method should return If omitted, all Substeps will be returned

- `setStepID(stepID: int) -> None` — Sets an ID for this StepNastran Step IDs must be unique and monotonically increasing (with Step order) within a SubcaseNastran.

## `apex.studies.StepNastranCollection`  (extends `EntityCollection`)

Methods:

- `StepNastranCollection() -> None` — Construct a new StepNastranCollection.

## `apex.studies.Study`  (extends `Entity`, `IName`, `IUserAttributes`)
Studies are container classes for other Studies, Scenarios, Key Result Values, Targets and Assessments. (Key Result, Targets and Assessments are not implemented in current Apex versions and are described here only for context) Studies are typed - current Apex implementations support just two types of Study - Design Validation studies and Optimization Studies. The primary purpose of a Study is to contain Scenarios (simulations) that have some common purpose.
Properties: `scenarios`, `scenariosNastran`

Methods:

#### `MNFGenerationProperty(mnfFilename: str = "", generateMNF: bool = True, generateGridPointStresses: bool = True, generateGridPointStrains: bool = True, massInvariantOptions: apex.studies.MNFMassInvariantOptions = apex.studies.MNFMassInvariantOptions.partial) -> apex.studies.MNFGenerationProperty`
Creates a MNFGenerationProperty. The MNFGenerationProperty that is created will include all of properties.

- `mnfFilename` — name of the exported modal neutral files.
- `generateMNF` — a Boolean value that controls whether or not a modal neutral file will be generated. The default value of true will cause the MNF to be generated after the normal modes calculations are complete. If this value is false, no MNF will be generated.
- `generateGridPointStresses` — a Boolean value used to control output of grid point stresses to the MNF. Set this property to true to output grid point stresses or false to suppress them.
- `generateGridPointStrains` — a Boolean value used to control output of grid point strains to the MNF. Set this property to true to output grid point strains or false to suppress them.
- `massInvariantOptions` — an Enumeration property that controls which mass invariants are written to the MNF.

#### `createScenario(name: str, description: str, scenarioConfiguration: apex.studies.ScenarioConfiguration, events: [str] = [], loadCases: [str] = []) -> apex.studies.Scenario`
Creates a Scenario within this Study object. The Study type is determined by the scenarioConfiguration enumeration argument. Enumerations are provided for all supported Scenarios types. The Scenario that is created will include all of default objects and properties contained by a Scenario including default output requests for each Step etc.

- `name` — an optional name for the Scenario. If omitted the system will assign a default name
- `description` — an optional description for the Scenario.
- `scenarioConfiguration` — defines the configuration of the Scenario. Enumerations are provided for currently supported Scenario configurations
- `events` — an optional List of ordered Event names. Each name in the list must be unique within the Scenario. The Events will be added to the last Step in the Scenario (Current version of Apex only support multiple Events in the last Step). For Scenario configurations that do not support multiple Events this argument will be ignored
- `loadCases` — an optional List of ordered Load case names. Each name in the list must be unique within the Scenario. A single step with the type defined in scenarioConfiguration will be added to each load case. For Scenario that do not support multiple Load cases this argument will be ignored. Currently, it is only supported in nonlinear scenario.

#### `createScenarioByModelRep(context: apex.Entity, simulationType: apex.studies.SimulationType) -> apex.studies.Scenario`
Creates a Scenario within this Study object. Generate a scenario using the ModelRep entity and set every thing of the context into the Scenario.

- `context` — ModelRep entity.
- `simulationType` — Scenario type (Static, NormalModes, LinearBuckling, ModalFrequency).

#### `createScenarioMBDScripted(name: str, description: str, acfCommands: str) -> apex.studies.Scenario`
Create scripted scenario with the specified attributes.

- `name` — Name of the Scenario.
- `description` — Description of the Scenario.
- `acfCommands` — Series of ACF commands to control a scenario.

#### `createScenarioMBDStandard(name: str, description: str) -> apex.studies.Scenario`
Create standard scenario with the specified attributes.

- `name` — Name of the Scenario.
- `description` — Description of the Scenario.

#### `createScenarioNastran(scenarioNastranType: apex.studies.NastranSolutionType, numberOfSubcases: int, subcaseType: apex.studies.NastranAnalysisType, name: str, description: std.strinng) -> apex.studies.ScenarioNastran`
Creates and returns a ScenarioNastran entity and adds it to this Study. The type of ScenarioNastran created and the number and type of Subcases that are included in the Scenario can be defined using the optional arguments.

- `scenarioNastranType` — The solution type of ScenarioNastran to create specified as a SolutionType enumeration literal If omitted, this method will create a linear statics Scenario
- `numberOfSubcases` — The number of Subcases that will be created and included in the Scenario. The type of these Subcases can be defined using the subcaseType argument
- `subcaseType` — optional argument specifying the type of any Subcases that may be created during Scenario creation. If omitted, the system will determine the type of any Subcases that are created during Scenario creation based on the type of the Scenario according to the following table, Linear static - linear static Normal modes (103) - Normal modes etc.
- `name` — An optional name for the Scenario. If the provided name is not unique within the Study, Apex will append an integer to ensure name uniqueness. If omitted Apex will provide a default name
- `description` — An optional description for the new Scenario

#### `createStudyGenerativeDesign(name: str = "", description: str = "", studyModelRep: apex.Entity = None) -> apex.studies.StudyGenerativeDesign`
Creates and returns a StudyGenerativeDesign object. The study will include a Generative Design Scenario populated with default properties. The Model that forms the basis of Study can be provided as an optional input argument.

- `name` — An optional name for the generative design Study. If omitted the system will supply a default unique name. If provided, the name must be unique within the root Study for the current Project. If a non-unique name is provided Apex will silently modify the name to ensure uniqueness within the scope of the root Study.
- `description` — An optional description for the generative design Study.
- `studyModelRep` — An optional ModelRep for the generative design Study. For current releases of Apex this must be a PartRep (The PartRep must reference a GenerativeDesignProperty) although future releases will also support AssemblyReps. If omitted during creation of the Study, the study model rep can be added later.

#### `deleteScenario(scenario: apex.studies.Scenario) -> None`
Deletes a Scenario from this Study.

- `scenario` — the Scenario to be deleted

#### `deleteScenarioNastran(scenarioNastran: apex.studies.ScenarioNastran) -> None`
Deletes a ScenarioNastran from this Study.

- `scenarioNastran` — the ScenarioNastran to be deleted

#### `getGenerativeDesignStudy(name: str) -> apex.studies.StudyGenerativeDesign`
Retrieves a Generative Study from the primary Study using the input Generative Design study name. If Generative Design study does not exist with the provided name the method will throw an exception.

- `name` — name of the Scenario.

#### `getScenario(name: str) -> apex.studies.Scenario`
Retrieves a Scenario from the Study using the input Scenario name. If a Scenario does not exist with the provided name the method will throw an exception.

- `name` — name of the Scenario.

#### `getScenarioNastran(name: str) -> apex.studies.ScenarioNastran`
Returns the ScenarioNastran identified by the name defined in the argument. If no ScenarioNastran entities can be found with a matching name the method will return None.

- `name` — The name of the ScenarioNastran to return

#### `getScenarios(recursive: bool = False) -> apex.studies.ScenarioCollection`
returns a collection of all Scenarios in the Study. Use the "recursive = True" argument to return all Scenarios within all Studies using a recursive approach

- `recursive` — Set recursive = True to return all Scenarios within a Study by descending each Study recursively. The default re3cursive = False will return only the Scenarios that are directly composed by the Study

#### `getScenariosNastran(nastranSolutionTypes: [apex.studies.NastranSolutionType]) -> apex.studies.ScenarioNastranCollection`
Returns a list of ScenarioNastran entities composed by this Study. The optional scenarioTypes argument enables the method to return only ScenarioNastran entities of specific types.

- `nastranSolutionTypes` — A List of NastranSolutionTypes identifying the types of Scenarios that will be returned. If omitted, all ScenarioNastrans will be returned


## `apex.studies.StudyGenerativeDesign`  (extends `Study`)
Class representing a Study for generative design simulations Generative design studies compose, a single ModelRep (a single Part in current Apex releases) that defines the model for all of the Scenarios in this Study one or more Scenarios that in turn compose Steps and Events that define Generative Design simulations
Properties: `scenarios`, `studyModelRep`

Methods:

#### `associateStudyModelRep(modelRep: apex.Entity) -> None`
Sets the ModelRep for this Study. All Scenarios in a generative design Study reference this single ModelRep. For current releases the ModelRep must be a Part however future releases will add support for Assemblies. If a ModelRep is already associate with this Study it will be silently replaced.

- `modelRep` — The AssemblyRep, PartRep, Assembly or Part to be analyzed. The ModelRep associated with this Study. In current Apex releases this must be a single Part (Rep), however future releases will also support Assemblies.

#### `createScenario(name: str, description: str, events: [str] = []) -> apex.studies.Scenario`
creates and returns a Scenario for use in generative design simulations. The Scenario will include a single Step plus default instances of all object types that it composes including Simulation Settings, Simulation Status composed by composed. An optional argument allows the Scenario to be created with a list of named Events.

- `name` — an optional name for the Scenario. If omitted the system will assign a default name
- `description` — an optional description for the Scenario.
- `events` — an optional List of ordered Event names. Each name in the list must be unique within the Scenario. The Events will be added to the last Step in the Scenario (Current version of Apex only support multiple Events in the last Step). For Scenario configurations that do not support multiple Events this argument will be ignored

#### `deleteScenario(scenario: apex.studies.Scenario) -> None`
Deletes a Scenario from this Study.

- `scenario` — the Scenario to be deleted

#### `getScenario(name: str) -> apex.studies.Scenario`
Retrieves a Scenario from the Study using the input Scenario name. If a Scenario does not exist with the provided name the method will throw an exception.

- `name` — name of the Scenario.

- `getScenarios() -> apex.studies.ScenarioCollection` — returns a collection of all Scenarios in the StudyGenerativeDesign.
- `getStudyModelRep() -> apex.ModelRep` — The ModelRep associated with this Study. In current Apex releases this must be a single Part (Rep), however future releases will also support Assemblies.
#### `update(name: str, description: str) -> None`
Update the StudyGenerativeDesign.

- `name` — updates the name of this StudyGenerativeDesign
- `description` — updates the description of this StudyGenerativeDesign


## `apex.studies.SubcaseNastran`  (extends `LoadCaseItem`)
Class SubcaseNastran Subcase is the top level load case structure.
Properties: `steps`, `subcaseID`

Methods:

#### `createSteps(analysisType: apex.studies.NastranAnalysisType, numberOfSteps: int, name: str, description: str) -> apex.studies.StepNastranCollection`
Creates and returns one or more Steps and adds them to this Subcase. The type of Step created can be specified using the optional argument. Steps can only be added to Subcases that are composed by a Scenario with a solution type of NONLINEAR_400. Attempting to add a Step to Subcases composed by any other Scenario type will cause this method to raise an exception.

- `analysisType` — optional argument specifying the analysis type of the Step that will be created. If omitted the method will create a nonlinear static Step
- `numberOfSteps` — optional argument specifying the number of Steps to create. If omitted, a single Step will be created
- `name` — An optional name for the new Step
- `description` — An optional description for the new Step

Returns: returns a list of Steps composed by this Subcase.

#### `createSubcase(analysisType: apex.studies.NastranAnalysisType, numberOfSubcases: int, name: str, description: str) -> apex.studies.SubcaseNastranCollection`
Creates one or more Subcases of the specified type and adds them to this Subcase.

- `analysisType` — An optional argument defining the analysis type of the Subcase. If omitted a Subcase with the default analysis type for the current Subcase solution type will be created
- `numberOfSubcases` — An optional argument specifying the the number of Subcases to create. If omitted, a single Subcase will be created
- `name` — A name for the Subcase. If omitted Apex will generate a default name dependent on the type of Subcase that is being created If a Subcase with the same name already exists within this Scenario Apex will append an integer to ensure Subcase name uniqueness within this Scenario
- `description` — An optional description for the new Subcase

Returns: Creates one or more Subcases of the specified type

- `getAnalysisType() -> apex.studies.NastranAnalysisType` — Gets Enumeration used to identify the type of Analysis that will be carried out by a Subcase.
#### `getStepNastran(name: str) -> apex.studies.StepNastran`
Returns the StepNastran identified by the name defined in the argument. If no StepNastran entities can be found with a matching name the method will return None.

- `name` — The name of the StepNastran to return

#### `getSteps(analysisTypes: [apex.studies.NastranAnalysisType]) -> apex.studies.StepNastranCollection`
returns a list of Steps composed by this Subcase. An optional argument enables the method to return a filtered list of Steps of specific analysis types

- `analysisTypes` — List of analysis types defining an analysis type filter. Only Steps in this Subcase with analysis types matching the analysis types in this list will be returned. If omitted, all Steps in this Subcase will be returned

Returns: returns a list of Steps composed by this Subcase.

- `getSubcaseID() -> int` — Gets an ID for this SubcaseNastran Subcase IDs must be unique and monotonically increasing (with Subcase order) within a ScenarioNastran.
#### `getSubcaseNastran(name: str) -> apex.studies.SubcaseNastran`
Returns the SubcaseNastran identified by the name defined in the argument. If no SubcaseNastran entities can be found with a matching name the method will return None.

- `name` — The name of the SubcaseNastran to return

#### `getSubcases(analysisTypes: [apex.studies.NastranAnalysisType]) -> apex.studies.SubcaseNastranCollection`
Returns a list of Subcases in this Scenario. An optional argument allows the method to return only the subcases of the specific types defined in the optional analysisTypes argument.

- `analysisTypes` — An optional list of analysis types defining the types of Subcases that this method should return If omitted, all Subcases will be returned

- `setSubcaseID(subcaseID: int) -> None` — Sets an ID for this SubcaseNastran Subcase IDs must be unique and monotonically increasing (with Subcase order) within a ScenarioNastran.

## `apex.studies.SubcaseNastranCollection`  (extends `EntityCollection`)

Methods:

- `SubcaseNastranCollection() -> None` — Construct a new SubcaseNastranCollection.

## `apex.studies.SubstepNastran`  (extends `LoadCaseItem`)
Properties: `substepID`

Methods:

- `getAnalysisType() -> apex.studies.NastranAnalysisType` — Gets Enumeration used to identify the type of Analysis that will be carried out by a Subcase.
- `getSubstepID() -> int` — Gets an ID for this SubstepNastran Substep IDs must be unique and monotonically increasing (with Substep order) within a StepNastran.
- `setSubstepID(substepID: int) -> None` — Sets an ID for this SubstepNastran Substep IDs must be unique and monotonically increasing (with Substep order) within a StepNastran.

## `apex.studies.SubstepNastranCollection`  (extends `EntityCollection`)

Methods:

- `SubstepNastranCollection() -> None` — Construct a new SubstepNastranCollection.

## `apex.studies.TEMPERATURE`  (extends `ScenarioCommand`)
Class representing a Nastran TEMPERATURE case control command. TEMPERATURE commands are used to select and configure Temperature load definitions using the ID of the temperature load.
Properties: `outputVerification`, `temperaturePurpose`, `value`

Methods:

- `getOutputVerification() -> str` — Gets an optional property specifying the type of temperature verification data (if any) to output This property may be assigned any one of the following values, "NONE" - no temperature verification data will be output None - same as "NONE" with the exception that this field will not be written to the Nastran file for this command ("NONE" is the Nastran default value for this field) "GRID" - verification of Grid data will be output "ELEMENT" - verification of Element data will be output "BOTH" - verification of both Grid and Element data will be output.
- `getTemperaturePurpose() -> str` — Gets an optional property identifying how the temperature load selected by this TEMPERATURE command will be used This property may be assigned any one of the following values, "BOTH" - the selected Temperature will be used for both Load calculations and to define temperature dependent material property value None - same as "BOTH" with the exception that this field will not be written to the Nastran file for this command. ("BOTH" is the Nastran default value for this field) "INITIAL" - the selected Temperature will be used to identify the initial temperature distribution in a nonlinear static analysis "MATERIAL" - the selected Temperature will be used to determine temperature dependent material properties "LOAD" - the selected Temperature will be used to determine an equivalent static load and to update material properties in a nonlinear analysis.
- `getValue() -> int` — Gets the ID of one or more temperatures (TEMP, TEMPD, TEMPP1, TEMPB3, TEMPRB or TEMPAX) assigned to the model referenced by the Scenario that this command is composed by. Use this command to assign temperatures to a Scenario, Subcase, Step or Substep.
#### `setOutputVerification(outputVerification: str) -> None`
Sets an optional property specifying the type of temperature verification data (if any) to output This property may be assigned any one of the following values, "NONE" - no temperature verification data will be output None - same as "NONE" with the exception that this field will not be written to the Nastran file for this command ("NONE" is the Nastran default value for this field) "GRID" - verification of Grid data will be output "ELEMENT" - verification of Element data will be output "BOTH" - verification of both Grid and Element data will be output.

- `outputVerification` — Set the outputVerification of this TEMPERATURE

#### `setTemperaturePurpose(temperaturePurpose: str) -> None`
Sets an optional property identifying how the temperature load selected by this TEMPERATURE command will be used This property may be assigned any one of the following values, "BOTH" - the selected Temperature will be used for both Load calculations and to define temperature dependent material property value None - same as "BOTH" with the exception that this field will not be written to the Nastran file for this command. ("BOTH" is the Nastran default value for this field) "INITIAL" - the selected Temperature will be used to identify the initial temperature distribution in a nonlinear static analysis "MATERIAL" - the selected Temperature will be used to determine temperature dependent material properties "LOAD" - the selected Temperature will be used to determine an equivalent static load and to update material properties in a nonlinear analysis.

- `temperaturePurpose` — Set the temperaturePurpose of this TEMPERATURE

#### `setValue(value: int) -> None`
Sets the ID of one or more temperatures (TEMP, TEMPD, TEMPP1, TEMPB3, TEMPRB or TEMPAX) assigned to the model referenced by the Scenario that this command is composed by. Use this command to assign temperatures to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this TEMPERATURE


## `apex.studies.TSTEP`  (extends `ScenarioCommand`)
Class representing a Nastran TSTEP case control command. TSTEP is used to select integration and time step specifications for a LoadCaseItem.This information is defined on a TSEP bulk entry and the ID of this bulk entry is entered here.
Properties: `value`

Methods:

- `getValue() -> int` — Gets the ID of a TSTEP entry assigned to the model referenced by the Scenario that this command is composed by Use this command to assign integration and time step data to a Scenario, Subcase, Step or Substep.
#### `setValue(value: int) -> None`
Sets the ID of a TSTEP entry assigned to the model referenced by the Scenario that this command is composed by Use this command to assign integration and time step data to a Scenario, Subcase, Step or Substep.

- `value` — Set the value of this TSTEP


## `apex.studies.WEIGHTCHECK`  (extends `ScenarioCommand`)
Class representing the Nastran "WEIGHTCHECK" case control command The WEIGHTCHECK command is used to compute the rigid body mass of the model at each stage of mass matrix reduction and compare with the rigid body mass of the g-set.
Properties: `cgi`, `dof_set`, `print_output`, `punch_out`, `refgrid`, `value`, `weight_mass`

Methods:

- `getCgi() -> str` — Gets property used to request output of the center of gravity and mass moments of inertia of the model This property may be assigned the following values, "NO" - center of mass and mass moment of inertia will NOT be output None - same as "NO" with the exception that this field will not be written to the Nastran file for this WEIGHTCECK command ("NO" is the Nastran default value for this field) "YES" - center of mass and mass moment of inertia will be calculated and output.
- `getDof_set() -> str` — Gets defines which set of stiffness degrees of freedom will be used for the weight checks This property may be assigned any one of the following values, "ALL" - uses all degree of freedom sets a list of any combination of the following strings, "G" - "N" "N+AUTOSPC" "F" "A" None - same as "G" with the exception that this field will not be written to the Nastran file for this WEIGHTCHECK command.
- `getPrint_output() -> str` — Gets specifies whether weight check data will be written to the print file or not This property may be assigned one of the following values, "PRINT" - writes weight check output to the print file None - same as "PRINT" with the exception that this field will not be written to the Nastran file for this WEIGHTCHECK command ("PRINT" is the Nastran default value for this field) "NOPRINT" - weight check output will NOT be written to the print file.
- `getPunch_out() -> str` — Gets controls output of weight check data to the punch file This property may be assigned any one of the following values, "PUNCH" - cause weight check output to be written to the punch file None (Default) - weight check data will NOT be written to the punch file.
- `getRefgrid() -> int` — Gets optional ID of a Grid used for the calculation of the rigid body motion The property may be assigned either of the following values, n - positive integer ID identify an existing Grid in the model None -.
- `getValue() -> str` — Gets optional property specifying whether or not WEIGHTCHECKs will be performed. This property may be assigned any one of the following values, "YES" - weight checks will be performed "NO" - weight checks will NOT be performed None - same is "NO" with the exception that this field will not be written to the Nastran file ("NO" is the Nastran default value for this field)
- `getWeight_mass() -> str` — Gets property used to control whether the weight check output is produced in units of mass or weight This property may be assigned any one of the following values, "WEIGHT" - weight check output will be produced using units of WEIGHT None - same as "WEIGHT" with the exception that this field will not be written to the Nastran file for this WEIGHTCHECK command ("WEIGHT" is the Nastran default value for this field) "MASS" - weight check output will be produced using units of MASS.
#### `setCgi(cgi: str) -> None`
Sets property used to request output of the center of gravity and mass moments of inertia of the model This property may be assigned the following values, "NO" - center of mass and mass moment of inertia will NOT be output None - same as "NO" with the exception that this field will not be written to the Nastran file for this WEIGHTCECK command ("NO" is the Nastran default value for this field) "YES" - center of mass and mass moment of inertia will be calculated and output.

- `cgi` — Set the cgi of this WEIGHTCHECK

#### `setDof_set(dof_set: str) -> None`
Sets defines which set of stiffness degrees of freedom will be used for the weight checks This property may be assigned any one of the following values, "ALL" - uses all degree of freedom sets a list of any combination of the following strings, "G" - "N" "N+AUTOSPC" "F" "A" None - same as "G" with the exception that this field will not be written to the Nastran file for this WEIGHTCHECK command.

- `dof_set` — Set the dof_set of this WEIGHTCHECK

#### `setPrint_output(print_output: str) -> None`
Sets specifies whether weight check data will be written to the print file or not This property may be assigned one of the following values, "PRINT" - writes weight check output to the print file None - same as "PRINT" with the exception that this field will not be written to the Nastran file for this WEIGHTCHECK command ("PRINT" is the Nastran default value for this field) "NOPRINT" - weight check output will NOT be written to the print file.

- `print_output` — Set the print_output of this WEIGHTCHECK

#### `setPunch_out(punch_out: str) -> None`
Sets controls output of weight check data to the punch file This property may be assigned any one of the following values, "PUNCH" - cause weight check output to be written to the punch file None (Default) - weight check data will NOT be written to the punch file.

- `punch_out` — Set the punch_out of this WEIGHTCHECK

#### `setRefgrid(refgrid: int) -> None`
Sets optional ID of a Grid used for the calculation of the rigid body motion The property may be assigned either of the following values, n - positive integer ID identify an existing Grid in the model None -.

- `refgrid` — Set the refgrid of this WEIGHTCHECK

#### `setValue(value: str) -> None`
Sets optional property specifying whether or not WEIGHTCHECKs will be performed. This property may be assigned any one of the following values, "YES" - weight checks will be performed "NO" - weight checks will NOT be performed None - same is "NO" with the exception that this field will not be written to the Nastran file ("NO" is the Nastran default value for this field)

- `value` — Set the value of this WEIGHTCHECK

#### `setWeight_mass(weight_mass: str) -> None`
Sets property used to control whether the weight check output is produced in units of mass or weight This property may be assigned any one of the following values, "WEIGHT" - weight check output will be produced using units of WEIGHT None - same as "WEIGHT" with the exception that this field will not be written to the Nastran file for this WEIGHTCHECK command ("WEIGHT" is the Nastran default value for this field) "MASS" - weight check output will be produced using units of MASS.

- `weight_mass` — Set the weight_mass of this WEIGHTCHECK


