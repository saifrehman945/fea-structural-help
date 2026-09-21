# apex.setting

(apex.setting module) provides access to the apex Application Settings.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.setting.CreateGeometryInNewPart`: `CurrentPart`, `NewPart`
  - If create geometry in current part in apex

`apex.setting.GeometryTessellationTolerance`: `VeryCoarse`, `Coarse`, `Medium`, `Fine`, `VeryFine`
  - To control the accuracy of geometry tessellation for display purposes

`apex.setting.ScriptTriggerType`: `PreModelClose`, `PostModelDefault`, `PostModelNew`, `PostModelOpen`, `PostFEMImport`, `PostFEMExport`, `PostGeometryImport`
  - Possible Script Triggers in Apex

## Module functions

### `apex.setting.getApplicationSettingsGeometry() -> apex.setting.ApplicationSettingsGeometry`
Returns the current Geometry Application Settings as an apex.geometry.ApplicationSettingsGeometry.

Returns: Returns the current Geometry Application Settings as an apex.geometry.ApplicationSettingsGeometry.

### `apex.setting.getApplicationSettingsStudy() -> apex.setting.ApplicationSettingsStudy`
returns the current study Application Settings

### `apex.setting.getIntegratedSolverExecutionSettings() -> apex.setting.IntegratedSolverExecutionSettings`
Retrieves the IntegratedSolverExecutionSettings from the project.

For example: Methods are provided on the IntegratedSolverExecutionSettings object that is returned to control the execution environment (memory, disk) of the integrated solver.

### `apex.setting.getScriptTriggers() -> apex.setting.ScriptTriggers`

### `apex.setting.getUndoRedoStackSize() -> int`

### `apex.setting.restoreDefaults() -> None`
Restores all application settings to their factory default values.

### `apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry: apex.setting.ApplicationSettingsGeometry) -> None`
Sets the current Geometry Application Settings using the input apex.setting.ApplicationSettingsGeometry.

- `applicationSettingsGeometry` — An instance of apex.setting.ApplicationSettingsGeometry describing all supported Application Settings related to Geometry

### `apex.setting.setApplicationSettingsStudy(applicationSettingsStudy: apex.setting.ApplicationSettingsStudy) -> None`
sets the current study Application Settings

- `applicationSettingsStudy` — study application settings

### `apex.setting.setIntegratedSolverExecutionSettings(integratedSolverExecutionSettings: apex.setting.IntegratedSolverExecutionSettings) -> bool`
change the setting of IntegratedSolverExecutionSettings to the project.

Returns: true if the change is succeed; otherwise returns false.

For example:

### `apex.setting.setUndoRedoStackSize(numCommandsStored: int) -> None`

## Classes in this module

Full method signatures are in `api/classes/apex.setting.md`.

`ApplicationSettingsGeometry`, `ApplicationSettingsStudy`, `IntegratedSolverExecutionSettings`, `ScriptTriggers`

