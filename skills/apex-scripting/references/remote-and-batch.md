# Remote control, macros, and batch scripts

Three ways to run Apex Python outside a custom tool panel.

## Table of contents

1. Choosing a delivery mode
2. Macro record and play
3. Batch scripts
4. Remote control from an external interpreter
5. Python environment

## 1. Choosing a delivery mode

| The user wants | Use |
|---|---|
| To capture steps they just performed | Macro record |
| A repeatable job with no input | a batch script, or a `batch_tool` custom tool |
| Input, picking, or a panel | a `ui_tool` custom tool |
| To drive Apex from PyCharm or a console | remote control via `remoting` |

## 2. Macro record and play

Record from the Macro menu or the Record Macro button; stop with Stop
Recording. The result is an ordinary Python script that can be edited by hand
and replayed with Play Macro.

Recording is the fastest way to discover the correct call for an unfamiliar
operation: perform it once, then read the generated script.

It does not capture everything. Documented gaps include geometry cleanup,
incremental meshing, feature mesh settings, import and export operations,
application settings, auto-thickness midsurface attribution, interface point
definition for `.MNF` export, cross-section force sensors, duplicating beam
shapes, behaviour specification, system damping, and study and scenario
definitions.

When a recorded macro comes out empty for one of these, look the operation up in
`api/` and write the call by hand.

## 3. Batch scripts

A standalone script run inside Apex. Same API as everything else:

```python
import apex

apex.setScriptUnitSystem(unitSystemName=r"m-kg-s-N")

model = apex.currentModel()
```

A `batch_tool` custom tool is the same thing with a palette button in front of
it: `tool.xml` sets `<tooltype>batch_tool</tooltype>` and `<runfile>` names the
script directly. There is no `_ui.py` and no `getUIContent()`.

## 4. Remote control from an external interpreter

The `remoting` package launches and drives Apex from an outside Python process,
which makes an IDE debugger and a REPL available.

```python
import remoting

remoting.launchApplication(appName='Apex')

import apex
from apex.construct import Point3D

apex.setScriptUnitSystem(unitSystemName=r"m-kg-s-N")

model = apex.currentModel()
model = model.close()

model.importGeometry(geometryFileNames=[r"C:\Demo\Front_Suspension_CAD.X_T"])

for part in model.getParts(recursive=True):
    for solid in part.solids:
        print(solid.name, solid.volume)

remoting.shutdownApplication()
```

Rules:

1. `import remoting` and `launchApplication()` come **before** `import apex`.
2. After launch, the API behaves exactly as it does inside Apex.
3. Always `shutdownApplication()` at the end, or the Apex process is left
   running.
4. Entered interactively, each call takes effect immediately and the model can
   be inspected between statements.

Use the interpreter that ships with Apex. Its environment must be able to see:

```
<installation_directory>\CL#\python3
<installation_directory>\CL#\python3\DLLs
<installation_directory>\CL#\python3\lib
<installation_directory>\CL#\python3\Lib\site-packages
```

## 5. Python environment

Apex embeds its interpreter in its own process, so `python.exe` never appears in
Task Manager while a script runs.

Bundled packages include numpy, scipy, pandas, h5py, tables, matplotlib and vtk.
Prefer them.

Anything else must match Apex's Python version and be built against the VC++
14.x runtime, because a single Windows process cannot mix runtimes. With write
access to the installation:

```
<apex_installation>\python3\python3.8.exe -m pip install <package_name>
```

Otherwise point at a compatible external distribution **before** importing apex:

```python
import sys
import os

os.environ['PATH'] = r'E:\Anaconda3\Library\bin' + ';' + os.environ['PATH']
sys.path.insert(0, r'E:\Anaconda3\Lib\site-packages')

import apex
```

The Apex 2021.4 documentation records Python 3.8.2 and VC++ 14.x. Confirm the
version against the user's installation before relying on it — the API reference
in `api/` is from the later Iberian Lynx FP2 release.
