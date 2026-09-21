# apex.datavis — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.datavis.LoadSummationPlot`  (extends `Entity`)
LoadSummationPlot is used to display the summation of forces and moments about a point in space. Finite element simulations frequently generate fields of forces and moments at the nodes and/or elements of the meshes that are used to represent the mechanical system that is being studied. In many cases, this distribution of forces and moments (as well as stresses, strains and other quantities of interest) can be used to assess how a proposed design transmits the applied loads throughout the structure. However, there are other engineering cases where this field of forces and moments is inappropriate and the engineer needs to know the total force and/or moment that is being transmitted by or applied to the structure. The LoadSummationPlot presents both the field distribution of forces and moments and the results force/moment arising from this field at a user defined location and orientation in space. The LoadSummationPlot can be used to display free body diagram information - the equivalent force and moment that would need to be applied at a location in space to bring a partial structure into equilibrium. It can also be used to display cross section force sensor output.
Properties: `applyFitlerEnabled`, `arrowDisplayFilter`, `colorMap`, `coordinateSystemMethod`, `displayDiscreteSummed`, `displayForcesMoments`, `summationOrientations`, `unitSystem`, `vectorComponentColors`, `vectorDisplayAnchorStyle`, `vectorDisplayColorMethod`, `vectorDisplayScalingFactor`, `vectorDisplayScalingMethod`, `vectorDisplayStyle`, `vectorDisplayZoomEnabled`

Methods:

- `getApplyFilterEnabled() -> apex.ApexBool` — Returns the apply filter boolean that controls whether vectors should be filtered.
- `getArrowDisplayFilter() -> float` — Returns arrow display filter value.
- `getColorMap() -> apex.post.ColorMap` — Returns the ColorMap for this LoadSummationPlot. If the color by components, returns None.
- `getCoordinateSystemMethod() -> apex.datavis.CoordinateSystemMethod` — Returns the System Type that the cross section force and/or moment data will be transformed to prior to display.
- `getDiscreteSummedVectorDisplay() -> apex.datavis.DiscreteSummedVectorDisplay` — Returns Discrete Summed Vector Display that controls the display of discrete and summed vectors.
- `getForceMomentVectorDisplay() -> apex.datavis.ForceMomentVectorDisplay` — Returns Force Moment Vector Display that controls the display of force and/or moment vectors.
- `getSummationOrientations() -> [apex.IOrientation]` — Returns the orientations used to display the cross section force and/or moment data.
- `getUnitSystem() -> str` — Returns the name Unit System that will be used to display the forces and moments on this plot.
- `getVectorComponentColors() -> {apex.datavis.VectorComponent:apex.ColorRGB}` — Gets the Vector Components that are displayed and their Colors.
- `getVectorDisplayAnchorStyle() -> apex.datavis.VectorDisplayAnchorStyle` — Returns the Vector Display Anchor Style that controls whether the vector display arrows are anchored by their tips or tails to the locations where the quantities are evaluated.
- `getVectorDisplayColorMethod() -> apex.datavis.VectorDisplayColorMethod` — Returns the Vector Display Color Method that defines how the vectors will be color coded.
- `getVectorDisplayScalingFactor() -> float` — Returns the Vector Display scaling factor that controls the size of the arrows used to display the vectors.
- `getVectorDisplayScalingMethod() -> apex.datavis.VectorDisplayScalingMethod` — Returns the Vector Display Scaling Method that controls whether the arrows will be drawn at a constant size or scaled based on the value of the vector.
- `getVectorDisplayStyle() -> apex.datavis.VectorDisplayStyle` — Returns the Vector Display Style that controls the style of the arrows used to display the vectors. The default apex.datavis.VectorDisplayStyle.ArrowShaded renders the arrows in full 3D and is useful for plots with a few vectors.
- `getVectorDisplayZoomEnabled() -> apex.ApexBool` — Returns the Vector Zoom boolean that controls whether the arrows used to display the vectors will change size as the view scale changes.
- `setApplyFilterEnabled(applyFilterEnabled: apex.ApexBool) -> None` — Sets the apply filter boolean that controls whether vectors should be filtered.
- `setArrowDisplayFilter(arrowDisplayFilter: float) -> None` — Sets arrow display filter value.
- `setColorMap(colorMap: apex.post.ColorMap) -> None` — Sets the ColorMap for this LoadSummationPlot.
- `setCoordinateSystemMethod(coordinateSystemMethod: apex.datavis.CoordinateSystemMethod) -> None` — Sets the System Type that the cross section force and/or moment data will be transformed to prior to display.
- `setDiscreteSummedVectorDisplay(displayDiscreteSummed: apex.datavis.DiscreteSummedVectorDisplay) -> None` — Sets the Discrete Summed Vector Display that controls the display of discrete and summed vectors.
- `setForceMomentVectorDisplay(displayForcesMoments: apex.datavis.ForceMomentVectorDisplay) -> None` — Sets the Force Moment Vector Display that controls the display of force and/or moment vectors.
- `setSummationOrientations(summationOrientations: [apex.IOrientation]) -> None` — Sets the display orientations that the cross section force and/or moment data will be transformed to prior to display as an apex.Construct.CoordinateSystem.
- `setUnitSystem(unitSystem: str) -> None` — Sets the name of Unit System that will be used to display the forces and moments on this plot.
- `setVectorComponentColors(vectorComponentColors: {apex.datavis.VectorComponent:apex.ColorRGB}) -> None` — Sets which Vector Components will be displayed and their Colors.
- `setVectorDisplayAnchorStyle(vectorDisplayAnchorStyle: apex.datavis.VectorDisplayAnchorStyle) -> None` — Sets the Vector Display Anchor Style that controls whether the vector display arrows are anchored by their tips or tails to the locations where the quantities are evaluated.
- `setVectorDisplayColorMethod(vectorDisplayColorMethod: apex.datavis.VectorDisplayColorMethod) -> None` — Sets the Vector Display Color Method that defines how the vectors will be color coded. apex.datavis.VectorColorMethod.VectorValue should only be used if Discrete Summed Vector Display is set to apex.datavis.DiscreteSummedVectorDisplay.Discrete.
- `setVectorDisplayScalingFactor(vectorDisplayScalingFactor: float) -> None` — Sets the Vector Display scaling factor that controls the size of the arrows used to display the vectors.
- `setVectorDisplayScalingMethod(vectorDisplayScalingMethod: apex.datavis.VectorDisplayScalingMethod) -> None` — Sets the Vector Display Scaling Method that controls whether the arrows will be drawn at a constant size or scaled based on the value of the vector.
- `setVectorDisplayStyle(vectorDisplayStyle: apex.datavis.VectorDisplayStyle) -> None` — Sets the Vector Display Style that controls the style of the arrows used to display the vectors. The default apex.datavis.VectorDisplayStyle.ArrowShaded renders the arrows in full 3D and is useful for plots with a few vectors.
- `setVectorDisplayZoomEnabled(vectorDisplayZoomEnabled: apex.ApexBool) -> None` — Sets the Vector Zoom boolean that controls whether the arrows used to display the vectors will change size as the view scale changes.

## `apex.datavis.XSectionForceSensorPlot`  (extends `LoadSummationPlot`)
XSectionForceSensorPlot is used to display the summation of forces and moments from one or more XSectionForceSensors or a single XSectionForceSensorArray. This class specializes the generic LoadSummationPlot specifically for use with XSectionForceSensors by defining the input fields of discrete forces and moments in terms of XSectionForceSensors or XSectionForceSensorArrays plus a static loadEvent. A XSectionForceSensor defines a plane in space and a target region of the Mechanical System (which can be the entire Mechanical System or a subset of that system). Each element in the target region that is intersected by the plane contributes a point force/moment derived from the internal forces acting within the cut element. This plot displays the intersected elements and their associated point forces and moments as well as the summation of the forces and moments about a point in space. The summed forces and moments can be calculated (dynamically) at any point in space, resolved into any user supplied axis system and displayed on the plot.
Properties: `loadEvent`, `xSectionForceSensorArray`, `xSectionForceSensors`

Methods:

- `getLoadEvent() -> apex.studies.Event` — Returns the Scenario Event from which the raw force data displayed on this plot is extracted.
- `getXSectionForceSensorArray() -> apex.instrument.XSectionForceSensorArray` — Returns the XSectionForceSensorArray that is displayed by this Plot. If this plot has been configured to display a simple collection of XSectionForceSensors then xSectionForceSensorArray will return a None type.
- `getXSectionForceSensors() -> apex.instrument.XSectionForceSensorCollection` — Returns the XSectionForceSensor collection that is displayed by this Plot. If this plot has been configured to display a XSectionForceSensorArray then xSectionForceSensors will return a None type.
- `setXSectionForceSensorArray(xSectionForceSensorArray: apex.instrument.XSectionForceSensorArray) -> None` — Sets the XSectionForceSensorArray that is displayed by this Plot. If this plot has been configured to display a simple collection of XSectionForceSensors then xSectionForceSensorArray is not used.
- `setXSectionForceSensors(xSectionForceSensors: apex.instrument.XSectionForceSensorCollection) -> None` — Sets the XSectionForceSensor collection that is displayed by this Plot. If this plot has been configured to display a XSectionForceSensorArray then xSectionForceSensors is not used.

