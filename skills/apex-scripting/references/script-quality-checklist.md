# Script quality checklist

Run through this before delivering any Apex script or custom tool.

## Grounding

1. Every function called was found in `api/functions-index.md` or
   `api/modules/<module>.md` — not recalled from memory.
2. Every enum member was confirmed in `api/enums.md`.
3. Every property and method on an entity was confirmed in
   `api/classes/<module>.md`.
4. Anything that could not be confirmed is flagged to the user rather than
   guessed.

## API conventions

5. All arguments are passed by keyword.
6. Entity properties are changed with `update()`, never by assignment.
7. Return values are treated as single objects; `ZResult*` values are read
   through their properties.
8. Collections are built with `EntityCollection` and `appendList`, not as
   Python lists; `.len()` is used rather than `len()`.
9. `apex.setScriptUnitSystem(...)` is set before geometry is created or
   measured.

## Structure

10. Lookup, filtering, mutation and reporting are separate blocks.
11. Entities are collected before they are modified, not mutated mid-iteration.
12. Collection scope is deliberate — `recursive=True` where nested assemblies
    matter.
13. Bulk module functions are preferred over per-object loops.
14. Hard-coded paths are lifted to named variables at the top.

## Robustness

15. Operations that can genuinely fail (file I/O, meshing, geometry repair) are
    guarded; everything else is allowed to raise.
16. Empty collections are handled — an empty target makes most calls quietly do
    nothing.
17. Long operations report through `apex.session.displayStatusMessage`.

## Custom tools only

18. `*_ui.py` imports `apex_sdk`, `clr` and `System.*` — never `apex`.
19. The worker script imports `apex` — never `apex_sdk`.
20. `getUIContent()` exists and returns the `ToolPropertyContainer`.
21. Every event handler carries `@apex_sdk.errorhandler`.
22. All model work goes through `runScript` or `runScriptFunction`.
23. Dictionary values are cast back from strings in the worker.
24. Controls read by the Apply handler are declared `global`.
25. Pick filter types match what the worker actually expects.
26. `palette.xml`, `group.xml` and `tool.xml` names match the folder tree, and
    `runfile` points at the UI file for a `ui_tool`.

## Communication

27. The target Apex release is stated when a signature could differ between
    versions.
28. Assumptions the user has not confirmed — units, deck, file paths, model
    state — are called out rather than buried in the code.
