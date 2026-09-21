# Configuration

## Documentation bundle

Which published Apex documentation set to fetch live pages from. Set this to
match the Apex release actually installed, so answers describe the right UI.

    bundle: msc_apex_help

Verified available: `msc_apex_help` (rolling/current), `apex_2025.2`,
`apex_2025.1`, `apex_2024.1`, `apex_2023.1`, `apex_2022.1`.

## Archive location

Where the local MSC Apex documentation archive lives. Only the build scripts in
`tools/` need it; everything they generate is committed to this skill, so
answering questions does not require the archive.

    archive:

Leave blank to auto-detect. The build scripts look, in order, at: the path given
on the command line, `$APEX_DOCS_ARCHIVE`, the `archive:` value above, then
`../Archive/Documentation` and `../Documentation` relative to this skill.

The archive is also used at answer time for one optional thing: reading a
documentation screenshot when the text alone is ambiguous. See
`references/fetching.md`.
