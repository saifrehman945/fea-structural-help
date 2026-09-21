# Patterns and recipes

Verified building blocks for Apex batch scripts and custom tool worker scripts.
Every signature here was checked against `api/`. Confirm any function you add
beyond these the same way.

## Table of contents

1. Script skeleton
2. Model access
3. Traversing the hierarchy
4. Building collections
5. Acting on the user's selection
6. Importing and exporting
7. Meshing
8. Materials and attribution
9. Reporting progress
10. Measuring and querying
11. Safe mutation

## 1. Script skeleton

```python
import apex

apex.setScriptUnitSystem(unitSystemName=r"m-kg-s-N")

model = apex.currentModel()
```

For a script invoked from a custom tool, suppress the trailing output dialog:

```python
apex.disableShowOutput()
```

Re-enable it with `apex.enableShowOutput()` if a later step should report.

## 2. Model access

```python
model = apex.currentModel()          # the session's single current model
model = model.close()                # close and start an empty model
model = apex.createModel(name="New Model")
```

`close()` returns the *new* empty model — rebind the name, do not keep using the
old handle.

## 3. Traversing the hierarchy

`Model` -> `Assembly` -> `Part` -> geometry and mesh entities.

```python
parts = model.getParts(recursive=True)

for part in parts:
    for solid in part.solids:
        print(part.name, solid.name, solid.volume)
```

Useful `Part` properties: `solids`, `surfaces`, `curves`, `points`,
`geometryBodies`, `meshes`, `nodes`, `elements`, `beamSpans`, `partProperties`.

`getParts(recursive=True)` flattens nested assemblies; without it you get only
direct children.

## 4. Building collections

Most bulk functions take an `apex.EntityCollection`. Build one with
`appendList`, because a Python list is not accepted:

```python
bodies = apex.EntityCollection()
bodies.appendList([body
                   for part in model.getParts(recursive=True)
                   for body in part.geometryBodies])
```

Filter first, then append, so the collection holds only real targets:

```python
large = apex.EntityCollection()
large.appendList([s
                  for part in model.getParts(recursive=True)
                  for s in part.solids
                  if s.volume >= 1.0e-4])
```

## 5. Acting on the user's selection

The natural input for a custom tool: operate on what the user picked.

```python
targets = apex.selection.getCurrentSelection()
```

It returns an `EntityCollection`. Constrain *what* can be picked through the
tool's pick filter rather than by filtering afterwards — see
[gui-sdk-reference.md](gui-sdk-reference.md).

## 6. Importing and exporting

```python
model.importGeometry(geometryFileNames=[r"C:\data\part.x_t"])
```

Optional flags (all default `True` unless noted): `importSolids`,
`importSurfaces`, `importCurves`, `importPoints`, `importGeneralBodies`,
`cleanOnImport`; `importHiddenGeometry` and `sewOnImport` default `False`.

```python
model.exportFEModel(filename=r"C:\out\model.bdf", unitSystem="m")

model.exportGeometry(filename=r"C:\out\model.x_t",
                     cadFormat=apex.geometry.CADFormat.ParasolidText)
```

`CADFormat` members are exactly: `ParasolidText`, `ParasolidBinary`, `STLText`,
`STLBinary`, `ACISText`, `IGES_5_3`, `STP_AP214`. There is no plain `Parasolid`
or `STL` member — this is a typical place to guess wrong, so check `api/enums.md`
for any enum before using it.

## 7. Meshing

```python
result = apex.mesh.createSurfaceMesh(
    target=bodies,
    meshSize=5.0,
    meshType=apex.mesh.SurfaceMeshElementShape.Mixed,
    meshMethod=apex.mesh.SurfaceMeshMethod.Auto,
    elementOrder=apex.mesh.ElementOrder.Linear)
```

`createSolidMesh`, `createHexMesh`, `createHybridMesh` and `createCurveMesh`
follow the same shape. Each returns a `ZResult*` object, not the mesh itself —
read the meshes from its properties.

Element counts come from the entity, via `.len()` on the collection:

```python
for entity in apex.selection.getCurrentSelection():
    print(entity.nodes.len(), entity.elements.len())
```

## 8. Materials and attribution

Create or fetch the material in `apex.catalog`, assign it in `apex.attribute`:

```python
material = apex.catalog.getMaterial(name="Steel")
apex.attribute.assignMaterial(target=solid_collection, material=material)
```

Prefer the bulk assignment above to calling `solid.assignMaterial(...)` in a
loop.

## 9. Reporting progress

```python
apex.session.displayStatusMessage("Meshing started ...")
# ... work ...
apex.session.displayStatusMessage("Meshing completed.")
```

Use this for anything slow — it is the only feedback the user gets while a
worker script runs.

## 10. Measuring and querying

Measure and transform helpers live directly on `apex`. Proximity search is in
`apex.utility`. Grep `api/functions-index.md` for `measure` or `distance` to
find the exact call rather than computing geometry by hand.

Highlighting is useful for review tools:

```python
color = apex.ColorRGB(214, 255, 0)
solid.highlight(colorRGB=color, lineWidth=2, pointSize=3)
```

## 11. Safe mutation

Entity-derived objects change only through `update()`:

```python
mesh_body.update(meshSize=8.0, elementOrder=apex.mesh.ElementOrder.Quadratic)
```

Guard operations that can genuinely fail, and let everything else raise:

```python
try:
    model.importGeometry(geometryFileNames=[path])
except Exception as exc:
    apex.session.displayStatusMessage("Import failed: %s" % exc)
    raise
```

Collect the entities you intend to change before changing them. Mutating while
iterating a live collection gives unpredictable results.
