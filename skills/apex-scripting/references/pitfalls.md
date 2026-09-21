# Apex pitfalls

Mistakes that produce plausible-looking Apex code that does not run, ordered by
how often they appear in generated scripts.

## 1. Positional arguments

The Apex API accepts **no positional arguments**. Every call needs name-value
pairs. This breaks more generated scripts than anything else.

```python
apex.mesh.createSurfaceMesh(target=bodies, meshSize=5.0)   # correct
apex.mesh.createSurfaceMesh(bodies, 5.0)                   # fails
```

Non-`Entity` value types are the exception, because they use normal Python
construction: `apex.ColorRGB(214, 255, 0)` is fine.

## 2. Assigning to a property instead of calling `update()`

`Entity`-derived classes have no setters. Assignment silently fails to change
the model rather than raising.

```python
my_mesh.update(meshSize=8.0)   # correct
my_mesh.meshSize = 8.0         # does nothing to the model
```

## 3. Invented enum members

Enum names read naturally, which makes them easy to guess and easy to get
wrong. `apex.geometry.CADFormat` has no `Parasolid` member — it has
`ParasolidText` and `ParasolidBinary`. Check `api/enums.md` every time.

The API also contains genuine misspellings that must be reproduced exactly:
`apex.mesh.FeatureMeshType.ArbirtaryHole`, `apex_sdk.PickFilterTypes.ExcludDof`.

## 4. Treating a Collection as a list

Passing a Python list where a collection is expected fails.

```python
bodies = apex.EntityCollection()
bodies.appendList([...])       # correct
bodies = [...]                 # not a collection
```

`len()` is a method on the collection, not the Python builtin:

```python
count = entity.nodes.len()     # correct
count = len(entity.nodes)      # not supported
```

Use `toList()` when you genuinely need list behaviour like `sorted()`.

## 5. Concluding a member does not exist because it is inherited

`api/classes/<module>.md` lists only the members declared on each class.
`apex.Part` shows no `name` property, yet `part.name` is valid — it comes from
`apex.IName`, one of the interfaces in that class's `(extends ...)` header.
Walk the base classes before deciding something is missing.

## 6. Expecting a tuple

Apex methods return exactly one value. Multiple heterogeneous results come back
as a `ZResult*` object whose properties hold the values.

```python
result = apex.mesh.createSurfaceMesh(...)   # ZResultCreateSurfaceMesh
meshes, ok = apex.mesh.createSurfaceMesh(...)   # fails
```

## 7. Reusing a model handle after `close()`

`Model.close()` returns a new empty model. The old handle is stale.

```python
model = model.close()   # correct
model.close()           # `model` is now stale
```

## 8. Importing `apex` in a tool's UI file

`*_ui.py` runs as IronPython in the UI process and must import only `apex_sdk`,
`clr` and `System.*`. `import apex` belongs in the worker script.

## 9. Doing model work in a click handler

Calling worker code directly — or importing the worker module and invoking its
function — stalls the Apex UI. Always go through `apex_sdk.runScript()` or
`apex_sdk.runScriptFunction()`.

## 10. Omitting `@apex_sdk.errorhandler`

An uncaught exception in an event handler terminates Apex. The decorator is
mandatory on every handler, not a nicety.

## 11. Forgetting that dictionary values are strings

`runScriptFunction` converts every key and value to a string. The worker must
cast:

```python
mesh_size = float(dictionary["MeshSize"])
include = dictionary["IncludeHidden"] == "True"
```

## 12. Skipping the unit system

Without `apex.setScriptUnitSystem(...)` the script runs in whatever units the
application currently has active, so the same script gives different geometry on
different machines. Set it explicitly.

## 13. Assuming `getParts()` is recursive

It is not. Nested assemblies need `getParts(recursive=True)`.

## 14. Documentation version skew

The API reference in `api/` is **Iberian Lynx FP2** (2024). The concept and
custom-tool documentation it was built alongside describes **Apex 2021.4**
with **Python 3.8.2**.

Treat `api/` as authoritative for what exists and what its signature is. Treat
the older material as authoritative for tool authoring structure and GUI SDK
behaviour, which have been stable. If the user names a specific Apex release,
say that the signature came from Iberian Lynx FP2 and may differ on theirs.

## 15. Third-party packages

Apex runs Python in its own process with its own interpreter and a modified
`PATH`/`PYTHONPATH`. Compiled packages must match Apex's Python version and its
VC++ 14.x runtime. Apex already ships numpy, scipy, pandas, h5py, tables,
matplotlib and vtk — prefer those. Any `sys.path` or `os.environ` manipulation
for an external distribution must happen **before** `import apex`.

## 16. Macro Record does not cover everything

Recorded macros are a good starting point but several areas are not captured,
including geometry cleanup, incremental meshing, feature mesh settings, import
and export, application settings, auto-thickness attribution, interface points,
cross-section force sensors, and study/scenario definitions. A user reporting
"the macro is empty" for one of these is hitting a documented limitation, not a
bug.
