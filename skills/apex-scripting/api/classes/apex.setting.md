# apex.setting — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.setting.ApplicationSettingsGeometry`
A Class representing the Apex Application Settings related to Geometry.
Properties: `createGeometryInNewPart`, `geometryEdgeTesselationTolerance`, `geometryFaceTesselationTolerance`, `geometryTessellationIsWatertight`

Methods:

#### `update(createGeometryInNewPart: apex.setting.CreateGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart, geometryTessellationIsWatertight: bool = False, geometryFaceTesselationTolerance: apex.setting.GeometryTessellationTolerance = apex.setting.GeometryTessellationTolerance.Medium, geometryEdgeTesselationTolerance: apex.setting.GeometryTessellationTolerance = apex.setting.GeometryTessellationTolerance.Medium) -> None`
Updates the properties of this ApplicationSettingsGeometry object. All modifiable properties of the ApplicationSettingsGeometry object are supported as optional arguments. Multiple properties may be updated in a single call. Any properties not included in the argument list are unchanged by this method.

Returns: array of points


## `apex.setting.ApplicationSettingsStudy`
Class to represent settings of study in application settings.
Properties: `displayPrereleaseScenario`, `displayUnsupportedCommand`, `useNewScenario`

Methods:

- `ApplicationSettingsStudy(useNewScenario: bool = True, displayPrereleaseScenario: bool = False, displayUnsupportedCommand: bool = True) -> None` — Constructor of ApplicationSettingsStudy.
- `getDisplayPrereleaseScenario() -> bool` — Gets If true, display pre-release scenario,subcase, step in study tab; if false, the pre-release scenario,subcase, step are hidden.
- `getDisplayUnsupportedCommand() -> bool` — Gets If true, display unsupported command of a scenario; if false, unsupported command is hidden in a scenario.
- `getUseNewScenario() -> bool` — Gets If true, use new scenarios; if false, use legacy scenarios.
- `setDisplayPrereleaseScenario(displayPrereleaseScenario: bool) -> None` — Sets If true, display pre-release scenario,subcase, step in study tab; if false, the pre-release scenario,subcase, step are hidden.
- `setDisplayUnsupportedCommand(displayUnsupportedCommand: bool) -> None` — Sets If true, display unsupported command of a scenario; if false, unsupported command is hidden in a scenario.
- `setUseNewScenario(useNewScenario: bool) -> None` — Sets If true, use new scenarios; if false, use legacy scenarios.

## `apex.setting.IntegratedSolverExecutionSettings`
This class defines application wide settings related to the integrated solver.
Properties: `scratchFolder`, `solverMemory`

Methods:

- `getScratchFolder() -> str` — The location where the integrated solver will create temporary files used during solution. The location must be defined as a path qualified folder and must exist on the current system otherwise the method will throw an exception.
- `getSolverMemory() -> float` — The maximum amount of memory that will be provided to the integrated solver when it executes.
- `setScratchFolder(scratchFolder: str) -> None` — set the location where the integrated solver will create temporary files used during solution.
- `setSolverMemory(solverMemory: float) -> None` — set the maximum amount of memory that will be provided to the integrated solver when it executes.

## `apex.setting.ScriptTriggers`
setting object used to add/remove/enable the automatic execution of scripts.

Methods:

#### `add(trigger: apex.setting.ScriptTriggerType, scriptName: str, methodName: str) -> None`
Add a Script Trigger, Script, and script method to settings. if a script and method already exist for the trigger, it will be replaced.

- `trigger` — the Apex event that will trigger the script execution
- `scriptName` — full path to a Script File containing the method to execute.
- `methodName` — method name to execute (contained in the Script File).

#### `disable(trigger: apex.setting.ScriptTriggerType) -> None`
disable a Script Trigger from settings.

- `trigger` — the Apex trigger to disable

#### `enable(trigger: apex.setting.ScriptTriggerType) -> None`
enable a Script Trigger in settings.

- `trigger` — the Apex trigger to enable

#### `getTriggerMethod(trigger: apex.setting.ScriptTriggerType) -> str`
Return method name associated with a ScriptTriggerType.

- `trigger` — the Apex event(ScriptTriggerType) to get the method name for.

#### `getTriggerScript(trigger: apex.setting.ScriptTriggerType) -> str`
Return script name associated with a ScriptTriggerType.

- `trigger` — the Apex event(ScriptTriggerType) to get the script name for.

#### `remove(trigger: apex.setting.ScriptTriggerType) -> None`
remove a Script Trigger and associated Script and method from settings.

- `trigger` — the Apex trigger to remove


