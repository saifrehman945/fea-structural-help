# Module selection

Map the task to a module before searching for a function. All 22 modules live in
the `apex` package; `import apex` makes every one of them available.

## The 22 modules

| Module | Covers |
|---|---|
| `apex` | Model, Assembly, Part, Collections; Transform and Measure; unit system; session-level entry points |
| `apex.attribute` | Materials in use, sections, beam shapes/spans, point masses, ties, offsets, composite zones — creation, assignment, editing |
| `apex.catalog` | Creating and fetching `attribute.Material` and `attribute.ShellSection` objects from catalogs |
| `apex.chart` | XY-chart data visualization |
| `apex.compute` | Remote/compute solver configuration |
| `apex.construct` | Construction geometry: `Sketch`, `Point3D`, `Vector3D`, `Orientation`, `CoordinateSystem` |
| `apex.datavis` | Data visualization |
| `apex.display` | 3D viewport annotation |
| `apex.environment` | Loads, constraints, forces, gravity, pressures, temperatures, enforced motion |
| `apex.expression` | Parametric expressions |
| `apex.gendes` | Generative design |
| `apex.geometry` | Geometry and topology: solids, surfaces, curves, points, faces, edges, vertices; drag, push/pull, defeature, stitch, midsurface |
| `apex.globals` | Global constants |
| `apex.instrument` | Point sensors, cross-section force sensors, clearance sensors |
| `apex.license` | License queries |
| `apex.mesh` | `SurfaceMesh`, `SolidMesh`, `CurveMesh`, `HexMesh`; nodes, elements, seeds; FE model import/export |
| `apex.post` | Post-processing and results visualization |
| `apex.selection` | The user's current viewport/tree selection |
| `apex.session` | Viewport visibility: show/hide, `displayStatusMessage`, topology line display |
| `apex.setting` | Application Settings access |
| `apex.studies` | Studies, scenarios, simulation setup and execution |
| `apex.utility` | General utilities, including proximity search |

## Choosing by task

| The user wants to... | Start in |
|---|---|
| Open, close, import, export, or traverse a model | `apex` |
| Walk assemblies and parts, or create them | `apex` (`Model.getParts`, `Assembly.createPart`) |
| Import CAD geometry | `apex` (`Model.importGeometry`) |
| Clean, defeature, stitch, or midsurface geometry | `apex.geometry` |
| Create or query solids, surfaces, edges, vertices | `apex.geometry` |
| Sketch, or build points/vectors/coordinate systems | `apex.construct` |
| Mesh anything, or edit nodes and elements | `apex.mesh` |
| Import or export a Nastran FE model | `apex.mesh` |
| Assign a material or a thickness/section | `apex.attribute`, sourcing from `apex.catalog` |
| Add point masses, ties, offsets, beam spans | `apex.attribute` |
| Apply loads, constraints, pressures, gravity | `apex.environment` |
| Add sensors or instrumentation | `apex.instrument` |
| Set up or run a simulation | `apex.studies` |
| Read results or build plots | `apex.post`, `apex.chart` |
| Show, hide, or change the viewport | `apex.session`, `apex.display` |
| Act on whatever the user has selected | `apex.selection` |
| Change an application preference | `apex.setting` |
| Find nearby entities | `apex.utility` |

## When the module is not obvious

1. Grep `api/functions-index.md` for a verb (`create`, `assign`, `import`,
   `delete`, `measure`) or a noun from the request. It lists all 989 module
   functions as `module.function — brief`.
2. Grep `api/classes.md` for the entity type the user named. The class's module
   prefix tells you where its operations live.
3. Only then open `api/modules/<module>.md` for exact signatures.

Entities and their operations usually share a module: `apex.geometry.Solid` is
operated on by `apex.geometry` functions, `apex.mesh.Node` by `apex.mesh`
functions. Attribution is the main exception — you create a material with
`apex.catalog` and assign it with `apex.attribute`.
