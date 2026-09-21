# Apex batch script template.
#
# Runs inside Apex (Macro Play, or a custom tool with <tooltype>batch_tool</tooltype>).
# Replace the marked sections; delete what the task does not need.
#
# Reminders:
#   - every Apex argument is keyword-only
#   - change entity properties with update(), never by assignment
#   - collections are apex.EntityCollection, not Python lists

import apex

# --- configuration -----------------------------------------------------------

UNIT_SYSTEM = r"m-kg-s-N"

# --- setup -------------------------------------------------------------------

apex.setScriptUnitSystem(unitSystemName=UNIT_SYSTEM)

# Suppress the trailing output dialog when driven from a tool button.
apex.disableShowOutput()

model = apex.currentModel()


# --- lookup ------------------------------------------------------------------

def collect_targets():
    """Return the entities this script acts on, as an EntityCollection."""
    targets = apex.EntityCollection()
    targets.appendList([body
                        for part in model.getParts(recursive=True)
                        for body in part.geometryBodies])
    return targets


# --- work --------------------------------------------------------------------

def process(targets):
    """Do the modelling work. Prefer bulk module functions over per-entity loops."""
    # e.g. apex.mesh.createSurfaceMesh(target=targets, meshSize=5.0)
    raise NotImplementedError("replace with the actual operation")


# --- main --------------------------------------------------------------------

def main():
    targets = collect_targets()

    if targets.len() == 0:
        apex.session.displayStatusMessage("Nothing to process.")
        return

    apex.session.displayStatusMessage("Processing %d entities ..." % targets.len())
    process(targets)
    apex.session.displayStatusMessage("Done.")


main()
