---
name: apex-scripting
description: Write, review, debug or generate MSC Apex Python code. Use for requests to produce a script, utility, macro, custom tool or plugin, to fix or improve existing Apex Python, or to find the right apex module, function signature, enum member or entity property before writing code — covering model and part traversal, geometry, meshing, materials and attribution, loads and constraints, studies and scenarios, results, session and viewport control, import and export, and tool panels built with the apex_sdk GUI SDK. Carries the generated Apex API reference (989 functions, 237 enums, 733 classes) with per-argument documentation. For how to do something in the Apex GUI rather than in code, use apex-docs. For Nastran deck keywords use nastran-reference, and for solver messages use nastran-diagnostics.
---

# Apex scripting

## Overview

MSC Apex is scripted with a single Python package, `apex`, spanning 22 modules.
Plugins ("custom tools") add a native-looking tool panel on top of that API
using a separate .NET/WPF GUI SDK, `apex_sdk`.

This skill bundles a generated, authoritative API reference. **Look the call up
before writing it.** Apex signatures are large, keyword-only, and full of
near-miss enum names, so recalled code is usually wrong in a way that only
fails at runtime.

## Required workflow

1. **Classify the deliverable.** Decide which of these the user needs, because
   the architecture differs completely:
   - a **batch script** — runs start to finish, no user input
   - a **custom tool (`ui_tool`)** — a panel with inputs and/or entity picking
   - a **custom tool (`batch_tool`)** — a palette button over a batch script
   - a **remote script** — drives Apex from an external interpreter
   - a **fix** to existing code
2. **Read the conventions.** [references/scripting-model.md](references/scripting-model.md)
   before writing any Apex code. Keyword-only arguments, `update()` instead of
   setters, and `ZResult` returns account for most broken generated scripts.
3. **Locate the functionality.** Follow the lookup order below. Do not write a
   call you have not found in `api/`.
4. **Generate only once the API is grounded.** Confirm the module, function
   signature, enum members and entity properties first, then write code.
5. **Validate before finishing.** Run
   [references/script-quality-checklist.md](references/script-quality-checklist.md).

## Documentation lookup order

1. [references/documentation-index.md](references/documentation-index.md) — the
   full doc surface and navigation rules.
2. [references/module-selection.md](references/module-selection.md) — map the
   task to one of the 22 modules.
3. `api/functions-index.md` — grep for a verb or noun to find the function and
   its module.
4. `api/modules/<module>.md` — exact signature, argument names, defaults.
5. `api/enums.md` — confirm every enum member. Never invent one.
6. `api/classes/<module>.md` — entity properties and methods. Members shown are
   those declared on the class; inherited ones are under the base classes named
   in its `(extends ...)` header.
7. Per-parameter documentation is inline in `api/modules/` and `api/classes/`
   under each signature — there is no separate source to drill into.

Grep the flat indexes before opening a module file. `apex.environment` and
`apex.studies` class files are large — grep those rather than reading them.

All documentation is inside this skill folder. The original 1.76 GB
documentation set is not bundled and must not be searched.

## Script generation rules

1. `import apex` at the top; it makes every module available.
2. Set `apex.setScriptUnitSystem(...)` before creating or measuring geometry.
3. Pass **every** argument by keyword. Apex supports no positional arguments.
4. Change entity properties with `update()`. Assignment silently does nothing.
5. Build targets as an `apex.EntityCollection` via `appendList`, not as a Python
   list. Use `.len()`, not `len()`.
6. Treat returns as single values; read multi-value results off the `ZResult*`
   object's properties.
7. Prefer bulk module functions over per-entity loops.
8. Use `recursive=True` when nested assemblies are in scope.
9. Separate lookup, filtering, mutation and reporting into clear blocks.
10. Report progress with `apex.session.displayStatusMessage` for slow work.
11. Guard operations that can genuinely fail; let everything else raise.

Start from [assets/template_batch_script.py](assets/template_batch_script.py).

## Custom tool rules

A `ui_tool` is always **two Python files**, and mixing them is the main failure
mode:

| File | Runs as | Imports | Job |
|---|---|---|---|
| `mytool_ui.py` | IronPython, Apex UI process | `apex_sdk`, `clr`, `System.*` | build the panel, gather input |
| `mytool.py` | Apex CPython | `apex` | do the modelling |

1. `getUIContent()` is mandatory and must return a `ToolPropertyContainer`.
2. The UI file never imports `apex`; the worker never imports `apex_sdk`.
3. `@apex_sdk.errorhandler` on **every** event handler — without it an uncaught
   exception terminates Apex.
4. Reach the API only through `apex_sdk.runScriptFunction()` or
   `runScript()`. Calling worker code directly stalls the UI.
5. Dictionary values arrive as strings; cast them in the worker.
6. Declare controls the Apply handler reads as `global`.
7. Constrain input with a pick filter rather than filtering after the fact.
8. The folder tree *is* the configuration — names in `palette.xml`,
   `group.xml`, `tool.xml` and the folders must agree, and `runfile` names the
   **UI** file for a `ui_tool`.

Use [references/custom-tool-authoring.md](references/custom-tool-authoring.md)
for the structure, [references/gui-sdk-reference.md](references/gui-sdk-reference.md)
for the `apex_sdk` surface, and
[references/gui-sdk-patterns.md](references/gui-sdk-patterns.md) for WPF layout.
Copy [assets/custom_tool_template/](assets/custom_tool_template/) as a starting
point.

## Debugging rules

1. Establish whether the code is a batch script, a worker, or UI code.
2. Verify the call exists and its signature matches before reading logic.
3. A script that runs but changes nothing is usually property assignment
   instead of `update()`, or an empty target collection.
4. A frozen Apex means model work on the UI thread.
5. A terminated Apex means a missing `@apex_sdk.errorhandler`.
6. A tool that never appears is a name mismatch in the palette/group/tool XML.

Use [references/debugging-playbook.md](references/debugging-playbook.md) for
symptom-driven triage and [references/pitfalls.md](references/pitfalls.md) for
the specific traps.

## Version

`api/` is generated from the **Iberian Lynx FP2** (May 2024) API reference and
is authoritative for what exists. The concept and custom tool material derives
from Apex 2021.4 / Python 3.8.2 documentation; tool authoring and the GUI SDK
have been stable across those releases. When a user names a specific Apex
release and a signature could differ, say where the signature came from.

## References

- [references/documentation-index.md](references/documentation-index.md): full navigation and lookup order
- [references/scripting-model.md](references/scripting-model.md): API conventions — keyword arguments, `update()`, ZResult, collections, exceptions
- [references/module-selection.md](references/module-selection.md): task-to-module mapping across the 22 Apex modules
- [references/patterns-and-recipes.md](references/patterns-and-recipes.md): verified Apex code patterns
- [references/custom-tool-authoring.md](references/custom-tool-authoring.md): plugin folder structure and palette/group/tool XML
- [references/gui-sdk-reference.md](references/gui-sdk-reference.md): the `apex_sdk` API surface, including all pick filter types
- [references/gui-sdk-patterns.md](references/gui-sdk-patterns.md): WPF panel layout recipes
- [references/remote-and-batch.md](references/remote-and-batch.md): macros, batch scripts, `remoting`, Python environment
- [references/pitfalls.md](references/pitfalls.md): the mistakes that break generated Apex code
- [references/debugging-playbook.md](references/debugging-playbook.md): symptom-driven debugging flow
- [references/script-quality-checklist.md](references/script-quality-checklist.md): criteria for high-quality Apex scripts
- [api/README.md](api/README.md): how to search the generated API reference
- [assets/template_batch_script.py](assets/template_batch_script.py): starter batch script
- [assets/template_remote_script.py](assets/template_remote_script.py): starter external/remote script
- [assets/custom_tool_template/](assets/custom_tool_template/): complete custom tool skeleton
