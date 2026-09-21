# Apex remote control template.
#
# Drives Apex from an EXTERNAL Python interpreter or IDE, so you get a debugger
# and a REPL. Use the interpreter that ships with Apex.
#
# Order matters: remoting is imported and the application launched BEFORE apex.

import remoting

remoting.launchApplication(appName='Apex')

import apex
from apex.construct import Point3D

# --- configuration -----------------------------------------------------------

UNIT_SYSTEM = r"m-kg-s-N"
GEOMETRY_FILES = [r"C:\Demo\Front_Suspension_CAD.X_T"]

try:
    # --- setup ---------------------------------------------------------------

    apex.setScriptUnitSystem(unitSystemName=UNIT_SYSTEM)

    model = apex.currentModel()
    # close() returns the NEW empty model -- rebind, do not reuse the old handle.
    model = model.close()

    # --- work ----------------------------------------------------------------

    model.importGeometry(geometryFileNames=GEOMETRY_FILES)

    for part in model.getParts(recursive=True):
        for solid in part.solids:
            print("%s / %s : %s" % (part.name, solid.name, solid.volume))

finally:
    # Always shut down, or the Apex process is left running.
    remoting.shutdownApplication()
