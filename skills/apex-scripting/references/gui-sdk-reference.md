# GUI SDK reference (`apex_sdk`)

The API available to a custom tool's `*_ui.py` file. This code runs as
**IronPython inside the Apex UI process**, so the panel is built from .NET WPF
controls, not from a Python toolkit.

## Table of contents

1. Standard imports
2. `getUIContent` — the required entry point
3. `ToolPropertyContainer`
4. `ActionCommand`
5. `PickFilterTypes` and `PickFilterRegistration`
6. `@apex_sdk.errorhandler`
7. `runScript` and `runScriptFunction`
8. `DataDescriptor`

## 1. Standard imports

```python
import sys
import os
import apex_sdk
import clr

import System
import System.Windows.Controls as WPFControls
from System.Windows.Automation import AutomationProperties
from Microsoft.Win32 import OpenFileDialog
```

Do **not** `import apex` here. Model work belongs in the worker script.

## 2. `getUIContent` — the required entry point

Every UI tool script must define `getUIContent()`, returning a
`ToolPropertyContainer`. Apex calls it when the tool is opened.

```python
def getUIContent():
    my_toolProperty = apex_sdk.ToolPropertyContainer()
    my_toolProperty.TitleText = "My Tool"
    my_toolProperty.ToolPropertyContent = getCustomToolPropertyContent()
    return my_toolProperty
```

The smallest legal tool is a bare container with nothing set.

## 3. `ToolPropertyContainer`

Derives from `System.Windows.Controls.UserControl`.

| Member | Type | Purpose |
|---|---|---|
| `ToolPropertyContent` | `FrameworkElement` | the panel body. Must be a `Panel` subclass such as `Grid` or `StackPanel` |
| `TitleText` | `string` | title bar text |
| `TitleImageUriString` | `string` | tool icon, e.g. `"file:///C:/path/icon.png"` |
| `IsCustomTool` | `bool` | always set `True` |
| `IsObjectPropertyControl` | `bool` | always set `False` |
| `AppliedCommand` | `ICommand` | `ActionCommand` run by the Apply button (green check) |
| `ExitCommand` | `ICommand` | `ActionCommand` run by the Exit button |
| `IsAppliedVisible` | `bool` | show/hide the Apply button |
| `IsAppliedEnabled` | `bool` | enable/disable the Apply button |
| `IsAutoAppliedVisible` | `bool` | show/hide the Auto button (lightning bolt) |
| `IsAutoApplied` | `bool` | `True` = automatic mode, `False` = manual |
| `ShowPickChoice` | `bool` | show the pick filter |
| `PickFilterList` | `List[String]` | pick filter contents |
| `IsHeaderExpanderVisible` | `bool` | show the Advanced Properties expander |
| `WorkFlowInstructions` | `string` | HTML-encoded workflow instructions |
| `WorkFlowInstructionsVisibility` | `Visibility` | show/hide those instructions |
| `ToolPropBorderVerticalAlignment` | `string` | `"Top"` (default), `"Center"`, `"Bottom"`, `"Stretch"` |

Documented as **do not use**: `PickFilterContent`,
`PickFilterVisibilityPickingContent`, `ShowBorderEffect`,
`UseDefaultExitBehavior`, `IsRoundCornerContainer`.

## 4. `ActionCommand`

Wraps a zero-argument Python function as a WPF command, for Apply and Exit.

```python
my_toolProperty.AppliedCommand = apex_sdk.ActionCommand(
    System.Action(HandleApplyButton))
```

The wrapped function **must take no parameters**. Ordinary control events are
different — a `Button.Click` handler takes `(sender, args)`:

```python
importBtn.Click += HandleImportButton     # def HandleImportButton(sender, args)
```

## 5. `PickFilterTypes` and `PickFilterRegistration`

Set which entity types the user is allowed to pick. Build a .NET string list:

```python
def setPickFilterList():
    pickChoices = System.Collections.Generic.List[System.String]()
    pickChoices.Add(apex_sdk.PickFilterTypes.ExclusivePicking)
    pickChoices.Add(apex_sdk.PickFilterTypes.VisibilityPicking)
    pickChoices.Add(apex_sdk.PickFilterTypes.Part)
    pickChoices.Add(apex_sdk.PickFilterTypes.Solid)
    pickChoices.Add(apex_sdk.PickFilterTypes.Surface)
    return pickChoices
```

```python
my_toolProperty.ShowPickChoice = True
my_toolProperty.PickFilterList = setPickFilterList()
```

Available types, by family:

- **Picking behaviours**: `ExclusivePicking`, `VisibilityPicking`
- **Model organization**: `Assembly`, `Part`
- **Geometry**: `Solid`, `Surface`, `Curve`, `Point`, `Cell`, `Face`, `Edge`,
  `Vertex`, `AveragePoint`
- **Mesh**: `SolidMesh`, `SurfaceMesh`, `CurveMesh`, `CellMesh`, `FaceMesh`,
  `EdgeMesh`, `VertexMesh`, `Element1D`, `Element2D`, `Element3D`, `Node`,
  `MeshSeed`, `SeedPoint`, `ElementEdge`, `ElementFace`
- **Interactions and connections**: `DiscreteTie`, `Connector`, `EdgeTie`,
  `Joint`, `Glue`, `Bolt3D`, `ContactBody`
- **Loads and constraints**: `Pressure`, `Gravity`, `Constraint`, `ForceMoment`,
  `EnforcedMotion`, `LoadTemperature`, `InitialTemperature`, `LoadPressure`,
  `Force`, `Moment`, `LoadScaleFactor`, `BeamDistributedLoad`, `DynamicLoad`,
  `Temperature`, `BeamTemperature`, `DeformationAxial1D`, `Acceleration`,
  `LoadCombination`, `Support`, `ExcludDof`, `InitialStress`, `InitialStrain`,
  `InitialDisplacementVelocity`, `InitialBeamTemperature`, `RotationalForce`
- **Attribution**: `CompositeZone`, `InterfacePoint`, `LayeredPanel`, `Offset`,
  `BeamSpan`, `PointMass`
- **Sensors**: `ClearanceSensor`, `CrossSectionSensor`, `MotionEnvelopeSensor`,
  `PointSensor`
- **Adams**: `AdamsJoint`, `AdamsJPrim`, `AdamsPointCurve`, `AdamsCurveCurve`,
  `RigidPartRep`, `FlexiblePartRep`, `AdamsSForce`, `AdamsSTorque`,
  `AdamsContact`, `AdamsVForce`, `AdamsVTorque`, `AdamsRotationalMotion`,
  `AdamsTranslationalMotion`, `AdamsPointMotion`, `AdamsBushing`,
  `AdamsTranslationalSpringDamper`, `AdamsRotationalSpringDamper`
- **Other**: `DatumPlane`, `CoordinateSystem`

`ExcludDof` is spelled that way in the SDK. `ArbirtaryHole` and similar
misspellings appear elsewhere in the API — reproduce them exactly.

An alternative registration entry point exists:

```python
apex_sdk.PickFilterRegistration.RegisterTool(toolName, filterList)
```

The reference states that `PickFilterContent` must not be set directly; use
`PickFilterList` or `RegisterTool`.

## 6. `@apex_sdk.errorhandler`

Catches exceptions raised inside the decorated function and shows them in a
dialog.

**Using it on every event handler is mandatory.** Without it, an uncaught Python
exception terminates the Apex application.

```python
@apex_sdk.errorhandler
def HandleApplyButton():
    ...
```

## 7. `runScript` and `runScriptFunction`

The only supported way to run Apex API code from a tool. Both are mandatory in
the sense that running or importing worker code directly stalls the UI.

```python
apex_sdk.runScript(script)
```

```python
apex_sdk.runScriptFunction(script, function, dictionary)
```

- `script` — full path to the worker `.py`
- `function` — name of a function in it taking one dictionary argument
- `dictionary` — the UI values to pass

**Keys and values are converted to strings.** The worker must cast them back:

```python
mesh_size = float(dictionary["MeshSize"])
```

## 8. `DataDescriptor`

Used with an `ExpandableStageButton`: a collection of `DataDescriptor` instances
supplied as the button's `ExpandableContent` makes the stage button generate a
caption and textbox per descriptor. `ExpressionChanged` fires when an expression
is edited.
