# Generated API reference

Apex Python API for **Iberian Lynx FP2**, generated from the Doxygen XML by
`tools/gen_api.py`. This is the authority on what exists and what its signature
is. Do not write an Apex call that is not confirmed here.

Coverage: 22 modules, 989 module functions, 237 enumerations, 733 classes.

## Files

| File | Contents | Use it to |
|---|---|---|
| `functions-index.md` | every module function as `module.name — brief` | find which module owns an operation |
| `enums.md` | every enum with its exact members | confirm an enum member |
| `classes.md` | every class with base classes and brief | find which module owns an entity type |
| `modules/<module>.md` | that module's enums and full function signatures | get argument names, types and defaults |
| `classes/<module>.md` | that module's class properties and methods | find what an entity can do |

## How to search

Start flat, then narrow. Do not open a module file before you know the module.

```
grep -i "mesh"        api/functions-index.md
grep -i "CADFormat"   api/enums.md
grep -i "Solid"       api/classes.md
```

Then open the one relevant file:

```
api/modules/apex.mesh.md
api/classes/apex.geometry.md
```

`apex.environment` and `apex.studies` class files are large. **Grep them rather
than reading them whole**:

```
grep -A15 '^## `apex.studies.Scenario`' api/classes/apex.studies.md
```

## Reading a signature

```
### `apex.mesh.createSurfaceMesh(name: str, target: apex.EntityCollection, meshSize: float, ...) -> apex.mesh.ZResultCreateSurfaceMesh`
```

- Types are shown Python-side: `float`, `str`, `int`, `bool`, `[X]` for a list,
  `{K:V}` for a dict.
- `= value` marks a default; everything else is effectively optional too, since
  Apex supports optional arguments broadly.
- **All arguments are keyword-only.** The order shown is documentation order,
  not a calling order.
- A `ZResult*` return means several values come back on one object — check its
  entry in `classes/<module>.md` for the property names.

## Inherited members are not repeated

Each class entry lists only the members **declared on that class**. Anything it
inherits is listed under its base class, named in the `(extends ...)` header.

So `apex.Part` shows no `name` property, but its header reads
`(extends Entity, IPhysical, IDisplayable, IUserAttributes, IName, IActivatable)`
and `apex.IName` supplies `name`, `description` and `pathName`. `part.name`
is valid.

Before concluding a member does not exist, walk the base classes in the
`extends` list. The common interfaces are:

| Interface | Supplies |
|---|---|
| `apex.IName` | `name`, `description`, `pathName` (all read-only) |
| `apex.IIdentifier` | `id` |
| `apex.IPhysical` | physical/mass properties |
| `apex.IDisplayable` | visibility and display state |
| `apex.Entity` | type introspection and casting |

## Per-parameter documentation

Every argument's documentation is inline, directly under the signature it belongs
to, in `modules/<module>.md` and `classes/<module>.md`:

```
### `apex.mesh.createSurfaceMesh(name: str, target: ..., meshSize: float, ...)`
create surface mesh.

- `target` — Homogeneous List of Geometry objects to be meshed. Only Solids,
  Surfaces and Faces are supported ...
- `meshSize` — Specify the Global Edge Length to use in meshing ...
```

This is where per-argument constraints and deprecation notices live, so read the
argument list before using an unfamiliar call — several parameters are only valid
when another is set, and a few are deprecated in place.

Files are large; grep for the member name with context rather than reading a
whole module.

## Regenerating

Everything in `api/` is generated from the Apex documentation archive's
`ScriptingXML` folder. The generated markdown is what ships; the XML is not
bundled, so regeneration needs that archive:

```
python tools/gen_api.py
```

Paths come from the script's own location. Both are overridable:

```
python tools/gen_api.py [source_xml_dir] [output_package_dir]
```

To move the skill to a **new Apex release**, point the generator at that
release's `ScriptingXML` folder:

```
python tools/gen_api.py <path to that release's ScriptingXML>
python tools/validate_references.py
```

`validate_references.py` re-checks every `apex.*` name used in `SKILL.md`,
`references/` and `assets/` against the regenerated index, and exits non-zero if
a name no longer exists — which is how you find prose that a release has
invalidated.
