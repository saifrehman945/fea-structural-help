# Configuration

## Documentation bundles

MSC Nastran documentation is split across releases, and the best source differs
per book. Each index records the release it was built from, and every citation
states it.

    qrg: MSC_Nastran_2025.2
    reference: MSC_Nastran_2025.2

- **`qrg`** — Quick Reference Guide: bulk data entries, case control commands,
  executive control and file management statements, the NASTRAN statement.
- **`reference`** — Reference Guide: element theory, solution sequences, grid
  points and coordinate systems, data recovery.

Error messages are **not** in these bundles. They live in the `MSC_Nastran_2025.1`
Combined Book and are handled by the `nastran-diagnostics` skill.

Verified available: `MSC_Nastran_2025.2`, `MSC_Nastran_2025.1`,
`MSC_Nastran_2024.2`, `MSC_Nastran_2024.1`, `MSC_Nastran_2023.4`.

## Matching your solver

Set these to the Nastran release your Apex install actually runs, if you know it.
Bulk data entries gain and lose fields between releases, so a field described here
may not exist in an older solver. When a user names a release and it differs from
the bundle, say which release the answer came from.

## Rebuilding

Changing a bundle means rebuilding the indexes, which needs network access:

    python tools/build_index.py
    python tools/validate.py
