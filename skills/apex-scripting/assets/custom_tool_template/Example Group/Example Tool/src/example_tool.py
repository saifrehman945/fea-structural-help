# Custom tool worker script.
#
# Runs in Apex's CPython interpreter, reached from the UI file through
# apex_sdk.runScriptFunction(). This file imports apex and does the modelling
# work. It must NOT import apex_sdk.
#
# The entry function takes exactly one dictionary argument. Every value in it
# arrived as a string, so cast before use.


def example_tool(dictionary={}):
    import apex

    # No trailing output dialog when driven from a tool button.
    apex.disableShowOutput()

    # --- unpack UI input -----------------------------------------------------

    mesh_size = float(dictionary["MeshSize"])

    mesh_types = {
        "Mixed": apex.mesh.SurfaceMeshElementShape.Mixed,
        "Quadrilateral": apex.mesh.SurfaceMeshElementShape.Quadrilateral,
        "Triangle": apex.mesh.SurfaceMeshElementShape.Triangle,
    }
    mesh_type = mesh_types[dictionary["MeshType"]]

    # --- collect targets -----------------------------------------------------

    # What the user picked in the viewport, as an EntityCollection.
    targets = apex.selection.getCurrentSelection()

    if targets.len() == 0:
        apex.session.displayStatusMessage("Nothing selected.")
        return

    # --- work ----------------------------------------------------------------

    apex.session.displayStatusMessage(
        "Meshing %d entities ..." % targets.len())

    apex.mesh.createSurfaceMesh(
        name="",
        target=targets,
        meshSize=mesh_size,
        meshType=mesh_type,
        meshMethod=apex.mesh.SurfaceMeshMethod.Auto,
        elementOrder=apex.mesh.ElementOrder.Linear)

    apex.session.displayStatusMessage("Meshing completed.")
