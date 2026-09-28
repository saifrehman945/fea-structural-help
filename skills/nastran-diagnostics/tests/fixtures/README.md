# Test fixtures

Synthetic inputs for `tools/validate.py`. They are not real solver output.

| File | Seeds |
|---|---|
| `faults.bdf` + `faults_mesh.inc` | one of each deck fault: duplicate grid, missing PID, undefined LOAD set, SPC on an RBE2-dependent grid, a loaded part with no SPC, coincident unmerged grids, a floating CONM2, an orphan grid, mixed-unit materials. It also exercises small, large (`GRID*`) and free-field cards, continuations, INCLUDE, and a FORCE in a CORD2C through a LOAD combination (resultant 17.8885, 8.9443, 0) |
| `glue.bdf` | a loaded plate reaching its SPC only through a BCONECT glue pair (BCBODY1 → BSURF, BCTABL1) whose secondary side is coarse |
| `mini.f06` | an f06 with a bulk data echo, duplicated warnings and a fatal, to test message deduplication, first-fatal detection and deck rebuild from the echo |

When you add a check to `tools/deck_checks.py`, seed its fault here and add its
code to `FAULTS_EXPECTED` in `tools/validate.py`.
