# The Apex scripting model

Rules that hold across the whole `apex` API. Read this before writing any Apex
code — most generated-code failures come from violating one of these, not from
picking the wrong function.

## Table of contents

1. Package and imports
2. Units
3. Keyword arguments only
4. Object construction
5. Reading properties
6. Changing properties: `update()`
7. Return types and ZResult
8. Collections
9. Errors
10. Bulk APIs

## 1. Package and imports

The API ships as a single Python package, `apex`, containing 22 modules.
Importing any one module imports all of them, so `import apex` is always enough.

```python
import apex
```

Use the fully qualified path, or import a name directly when it is used often:

```python
import apex
from apex.construct import Point3D

my_point = apex.geometry.createPointXYZ(x=0.0, y=0.0, z=0.0)
```

All Apex classes and functions are uniquely named across modules, so direct
imports are safe within the API. They are not safe against third-party packages —
prefer qualified names when mixing in other libraries.

## 2. Units

Set the unit system before creating or measuring anything. Values in the script
are interpreted in this system.

```python
apex.setScriptUnitSystem(unitSystemName=r"m-kg-s-N")
```

## 3. Keyword arguments only

**The Apex API does not support positional arguments.** Every argument must be
passed as a name-value pair. This is the single most common cause of broken
generated scripts.

```python
# correct
apex.mesh.createSurfaceMesh(target=bodies, meshSize=5.0)

# raises — positional arguments are not supported
apex.mesh.createSurfaceMesh(bodies, 5.0)
```

Most arguments are optional. Pass only the ones that matter; the rest take
documented defaults. These two calls are equivalent:

```python
model.importGeometry(geometryFileNames=files, importSolids=True,
                     importSurfaces=True, cleanOnImport=True)

model.importGeometry(geometryFileNames=files)
```

## 4. Object construction

Three patterns, chosen by what the object is:

**Module free function** — the general case for entities. Usually `create*`, and
usually able to create many objects at once from a collection.

```python
meshes = apex.mesh.createSolidMesh(target=solid_collection, meshSize=5.0)
```

**Factory method on the parent** — for objects whose position in the hierarchy
must be specified. Parts and Assemblies always belong to a Model or Assembly.

```python
my_part = my_assembly.createPart(name="My New Part")
```

**Native Python constructor** — only for classes that do *not* derive from
`Entity`, such as `Point3D`, `Vector3D` and `ColorRGB`.

```python
p = apex.construct.Point3D(x=0.0, y=1.0, z=1.0)
c = apex.ColorRGB(214, 255, 0)
```

## 5. Reading properties

Properties are `lowerCamelCase` and readable two equivalent ways:

```python
size = my_mesh.meshSize
size = my_mesh.getMeshSize()
```

## 6. Changing properties: `update()`

**Classes derived from `Entity` have no property setters and no `set*` methods.**
Assigning to a property does not change the model. Use `update()`, which accepts
any valid combination of that class's properties in one call.

```python
# correct
my_mesh.update(meshSize=8.0, elementMinEdgeLengthRatio=0.2)

# does NOT modify the model
my_mesh.meshSize = 8.0
```

## 7. Return types and ZResult

Apex methods return exactly **one** value and never return tuples.

| What is returned | Type |
|---|---|
| Several Apex objects sharing a base class | an Apex Collection |
| Several values of a Python intrinsic type | a Python `list` |
| Several values of mixed types | a `ZResult*` object |
| Anything else | a Python intrinsic or a single Apex object |

`ZResult` classes are named `ZResult` + the method name with its first letter
capitalized, so `createSurfaceMesh()` returns `ZResultCreateSurfaceMesh`. Read
the individual values from its properties:

```python
result = apex.mesh.createSurfaceMesh(target=bodies, meshSize=5.0)
meshes = result.meshes
```

Check the module's entry in `api/modules/` for the exact ZResult property names —
never guess them.

## 8. Collections

Collections are typed, iterable containers, scoped to the same module as the type
they hold (`apex.geometry.Solid` -> `apex.geometry.SolidCollection`). They follow
collection inheritance, so a method returning mixed `Surface` and `Face` objects
returns a `GeometryCollection`.

**Collections are not Python lists**, but as of Iberian Lynx they cover most of
what scripts need:

| Call | Does |
|---|---|
| `append(entity=...)` | add one entity |
| `appendList(entityList=[...])` | add from a Python list |
| `extend(collection=...)` | add another collection |
| `fromList(entityList=[...])` | insert a Python list, in place |
| `toList()` | return the members as a Python list |
| `len()` | number of members |
| `clear()` | empty the collection |

Also supported: iteration, slicing, copying, `[]` indexing, and combining with
`+`.

Note `len()` is a **method**, not the `len()` builtin:

```python
count = targets.len()      # correct
count = len(targets)       # not supported
```

Drop to a Python list with `toList()` when you need real list behaviour such as
`sorted()` or `sum()`. Build a collection from a comprehension via `appendList`:

```python
bodies = apex.EntityCollection()
bodies.appendList([body
                   for part in apex.currentModel().getParts(recursive=True)
                   for body in part.geometryBodies])
```

## 9. Errors

The API signals failure by **raising exceptions**, never by returning an error
code. A returned value can be trusted; wrap operations that can legitimately
fail (file I/O, meshing, geometry repair) in `try`/`except`.

In custom tool UI code this is not optional — see
[gui-sdk-reference.md](gui-sdk-reference.md) for `@apex_sdk.errorhandler`.

## 10. Bulk APIs

Where an operation applies to many objects, a bulk form usually exists as a
module free function alongside the single-object method. Prefer it: it avoids a
Python loop and its implementation is faster.

```python
# single object
my_solid.assignMaterial(material=my_material)

# bulk — preferred for more than one target
apex.attribute.assignMaterial(target=solid_collection, material=my_material)
```
