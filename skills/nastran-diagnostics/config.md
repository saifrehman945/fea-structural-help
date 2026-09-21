# Configuration

## Documentation bundle

    bundle: MSC_Nastran_2025.1

The error message catalogue is published **only** in the 2025.1 "Combined Book".
It is absent from the 2025.2 HTML documentation, which is why this skill pins a
different release from `nastran-reference` (which uses 2025.2 for the Quick
Reference Guide and Reference Guide).

Verified available: `MSC_Nastran_2025.1`. Other releases publish the catalogue as
PDF only, which these tools cannot slice.

## What this means for answers

Always state that a message description came from 2025.1. Message numbers are
stable across releases in practice, but wording and `User action` text are not
guaranteed to match an older or newer solver.

## Rebuilding

Needs network access:

    python tools/build_messages.py            # full rebuild
    python tools/build_messages.py --resume   # only the ranges still missing
    python tools/validate.py

The portal refuses sustained request bursts, and reports it as a DNS or
connection-reset error rather than an HTTP 429. The tools retry with backoff;
if whole ranges still fail, rerun with `--resume` rather than starting over.
