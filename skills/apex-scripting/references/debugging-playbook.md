# Debugging playbook

Symptom-driven triage for existing Apex scripts and custom tools. Identify the
symptom, then work the listed checks in order before reading the script line by
line.

## Table of contents

1. Triage order
2. Script fails immediately
3. Script runs but the model is unchanged
4. Wrong or empty results
5. Apex freezes
6. Apex terminates
7. The tool does not appear
8. Import errors

## 1. Triage order

1. Is this a batch script, a custom tool worker, or custom tool UI code? The
   rules differ sharply between them.
2. Does the failing call exist? Grep `api/functions-index.md`.
3. Does the signature match? Open `api/modules/<module>.md`.
4. Are the enum members real? Check `api/enums.md`.
5. Only then read the logic.

## 2. Script fails immediately

| Check | Why |
|---|---|
| Positional arguments anywhere | the API accepts none |
| Enum member spelling | invented members are common |
| Function actually exists in that module | the module prefix is easy to get wrong |
| `import apex` present | nothing resolves without it |
| A Python list passed where a collection is expected | not interchangeable |

## 3. Script runs but the model is unchanged

The usual cause is property assignment instead of `update()`. Search for
`.someProperty =` on an Apex object; each one is a silent no-op.

Next, confirm the target collection was not empty — an empty collection makes
most bulk calls succeed and do nothing. Print the count before acting:

```python
apex.session.displayStatusMessage("targets: %d" % targets.len())
```

Then confirm scope: `getParts()` without `recursive=True` misses everything in
nested assemblies.

## 4. Wrong or empty results

| Symptom | Check |
|---|---|
| Nothing is found | collection scope, and `recursive=True` |
| Geometry is the wrong size | `apex.setScriptUnitSystem` is missing |
| Only part of the model is affected | selection vs whole model; visibility picking |
| Values look like strings | dictionary values from `runScriptFunction` need casting |
| Unpacking error | the method returned a single `ZResult*`, not a tuple |

## 5. Apex freezes

Almost always a custom tool running model code on the UI thread. Look for:

1. A worker imported into the UI file and called directly.
2. `apex` API calls inside an event handler.
3. Long loops in `*_ui.py`.

The fix is to move that work into a worker script reached through
`apex_sdk.runScriptFunction()`.

## 6. Apex terminates

An uncaught exception in an event handler shuts the application down. Confirm
every handler carries `@apex_sdk.errorhandler`. Once it does, the same failure
surfaces as a dialog with the traceback instead of a crash.

## 7. The tool does not appear

Work down the folder structure, since discovery is purely structural:

1. The palettes folder is registered in Options / Application Settings /
   Custom Tools.
2. `palette.xml`, `group.xml` and `tool.xml` each exist at the right level.
3. Each `<group Name=...>` matches a `group.xml` `<name>`, and each
   `<tool Name=...>` matches a `tool.xml` `<name>`. A mismatch hides the entry
   silently.
4. `runfile` names a file that exists in `src/`.
5. For `ui_tool`, `runfile` is the **UI** file, not the worker.
6. Icons are in `res/`.
7. The registration file is version-specific — a tool set configured for
   another Apex release will not show up.

If the tool appears but the panel is blank, `getUIContent()` is missing, is
misspelled, or does not return the `ToolPropertyContainer`.

## 8. Import errors

A third-party package that works outside Apex may fail inside it. Apex uses its
own interpreter and rewrites `PATH` and `PYTHONPATH` for its process, so
external installations are not visible by default and compiled extensions must
match Apex's Python and VC++ 14.x runtime.

Prefer the packages Apex already ships (numpy, scipy, pandas, h5py, tables,
matplotlib, vtk). If an external distribution is genuinely required, its
`sys.path` and `os.environ` setup must run **before** `import apex`.

## Narrowing an unclear failure

Reduce to the smallest script that still fails, and report progress at each
step so the failing stage is visible:

```python
import apex

apex.setScriptUnitSystem(unitSystemName=r"m-kg-s-N")
model = apex.currentModel()

parts = model.getParts(recursive=True)
apex.session.displayStatusMessage("parts: %d" % parts.len())
```

For interactive exploration, drive Apex from an external interpreter with the
`remoting` package — see [remote-and-batch.md](remote-and-batch.md). Typing
calls one at a time and watching the model respond localises a failure faster
than re-running a whole script.
