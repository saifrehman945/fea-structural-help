# apex.session

(apex.session module) viewport visibility functions (ShowAll(), HideAll(), DisplayTopologyLines(), etc.)

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.session.DisplayRenderStyle`: `Wireframe`, `HiddenLines`, `Filled`, `FilledWithEdges`, `Shaded`, `ShadedWithEdges`, `NoRender`, `Undefined`

`apex.session.DisplayShellThickness`: `Thickness_2D`, `Offset_2D`, `ThicknessAndOffset_3D`, `Display_None`
  - Possible DisplayShellThickness Options in Apex

`apex.session.ElementDimensionMetric`: `MinimumLength_2D`, `MaximumLength_2D`, `LengthDegeneracy_2D`, `AngleDegeneracy_2D`
  - Possible ElementDimensionMetric Options in Apex

`apex.session.ElementQualityMetric`: `QualityIndex_2D`, `AspectRatio_2D`, `WarpageAngle_2D`, `WarpageFactor_2D`, `Skew_2D`, `Taper_2D`, `Jacobian_2D`, `QuadMinInteriorAngle_2D`, `QuadMaxInteriorAngle_2D`, `TriMinInteriorAngle_2D`, `TriMaxInteriorAngle_2D`, `AspectRatio_3D`, `Jacobian_3D`
  - Possible ElementQualityMetric Options in Apex

`apex.session.MarkerSize`: `Small`, `Large`
  - Possible MarkerSize Options in Apex

`apex.session.MaskableEntities`: `All`, `AllFEM`, `Nodes`, `Elements`, `Elements1D`, `Elements1DBeam2`, `Elements2D`, `Elements2DTria3`, `Elements2DTria6`, `Elements2DQuad4`, `Elements2DQuad8`, `Elements3D`, `Elements3DTetra4`, `Elements3DTetra10`, `Elements3DHex8`, `Elements3DPenta6`, `Elements3DHex20`, `Elements3DPenta15`, `Seeds`, `SeedsPointSeeds`, `SeedsEdgeSeeds`, `PointMasses`, `AllGeometry`, `GeometryVertices`, `GeometryPoints`, `GeometryCurves`, `GeometrySurfaces`, `GeometryNonManifoldSurfaces`, `GeometrySolids`
  - Possible Maskable Entities in Apex

`apex.session.MaskableEntities_Apex`: `AllInteractions`, `InteractionsGluePairs`, `InteractionsGluePatches`, `InteractionsTies`, `AllConnections`, `ConnectionsSprings`, `ConnectionsSpringDampers`, `ConnectionsDampers`, `ConnectionsBushings`, `ConnectionsRigidLinks`, `ConnectionsFlexibleLinks`, `AllLBCs`, `LBCsForceMoments`, `LBCsGeneralConstraints`, `LBCsClampedConstraints`, `LBCsAxialConstraints`, `LBCsSphericalConstraints`, `LBCsSymmetryConstraints`, `LBCsPressures`, `LBCsGravities`, `LBCsEnforcedMotions`, `AllSensors`, `SensorsPointSensors`, `SensorsCrossSectionSensors`, `Spans_2D`, `Spans_3D`
  - Possible Maskable Entities in Apex

`apex.session.SuppressableEntities`: `AllEntities`, `EdgesAndCurves`, `Vertices`
  - Possible Suppressable Entities in Apex

`apex.session.Visibility`: `Hidden`, `Visible`, `NotSet`

## Module functions

### `apex.session.clearHighlights() -> None`
Clears the highlight color on all Entities.

### `apex.session.display2DSpans(display: bool) -> bool`
ODM control for the display of 2D Spans.

- `display` — defines if 2D Spans should appear or not.

### `apex.session.display3DSpans(display: bool) -> bool`
ODM control for the display of 3D Spans.

- `display` — defines if 3D Spans should appear or not.

### `apex.session.displayConnectionMarkers(display: bool) -> bool`
ODM control for the display of Connection Markers.

- `display` — defines if Connection Markers should appear or not.

### `apex.session.displayInteractionMarkers(display: bool) -> bool`
ODM control for the display of Interaction Markers.

- `display` — defines if Interaction Markers should appear or not.

### `apex.session.displayLoadsAndBCMarkers(display: bool) -> bool`
ODM control for the display of Loads And BC Markers.

- `display` — defines if Loads And BC Markers should appear or not.

### `apex.session.displayMeshCracks(displayCracks: bool) -> bool`
ODM control for the display of Mesh Cracks.

- `displayCracks` — defines if mesh cracks should appear or not.

### `apex.session.displayMeshTopologyEdges(displayEdges: bool) -> bool`
ODM control for the display of Mesh Topology Edges.

- `displayEdges` — defines if mesh edges should appear or not.

### `apex.session.displayNodeMarkerSize(markerSize: apex.session.MarkerSize = apex.session.MarkerSize.Small) -> bool`
ODM control for the display size of Node Markers.

- `markerSize` — defines marker size (Small or Large).

### `apex.session.displaySensorMarkers(display: bool) -> bool`
ODM control for the display of Sensor Markers.

- `display` — defines if Sensor Markers should appear or not.

### `apex.session.displayShellElementCoordinateSystems(displayCoordinateSystem: bool) -> bool`
ODM control for the display of Shell Element Coordinate Systems.

- `displayCoordinateSystem` — defines if Coordinate System should appear or not.

### `apex.session.displayShellNormalDualColors(displayDualColors: bool) -> bool`
ODM control for the display of Shell Normal Dual Colors.

- `displayDualColors` — defines if dual colors should appear or not.

### `apex.session.displayShellNormalVectors(displayVectors: bool) -> bool`
ODM control for the display of Shell Normal Vectors.

- `displayVectors` — defines if normal vectors should appear or not.

### `apex.session.displayShellThickness(shellThickness: apex.session.DisplayShellThickness) -> bool`
ODM control for the display of Shell Thickness.

- `shellThickness` — defines if shell thickness should appear or not.

### `apex.session.displayStatusMessage(message: str) -> None`
Displays the text provided in the input argument "message" in the application status bar.

- `message` — The text that will be displayed in the status bar

### `apex.session.displaySuppressedEntities(suppressedEntities: apex.session.SuppressableEntities) -> bool`
ODM control for the display of Suppressed Entities.

- `suppressedEntities` — defines if topology lines should appear or not.

### `apex.session.displayTopologyLines(displayState: bool) -> bool`
ODM control for the display of Topology Lines.

- `displayState` — defines if topology lines should appear or not.

### `apex.session.growShellMesh() -> bool`
ODM control for the display of Grow Shell Meshes.

### `apex.session.hideAll() -> None`
Sets the visibility status of all objects in the current scene to "Hidden".

### `apex.session.maskEntityTypes(maskedEntities: apex.session.MaskableEntities) -> bool`
ODM control for the display of Vertices.

- `maskedEntities` — .

### `apex.session.reverseEntityMask() -> bool`
reverses the Entity Masking

### `apex.session.showAll() -> None`
Sets the visibility status of all objects in the current scene to "Visible".

### `apex.session.showReverse() -> None`
Reverses the visibility status of all objects in the current scene. Objects that have a vsiblity status of "Visible" are modified to "Hidden" and objects that have a visiblity status of "Hidden" are modified to "Visible".

