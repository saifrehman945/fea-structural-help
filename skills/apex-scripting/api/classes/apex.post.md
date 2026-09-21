# apex.post — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.post.ChartPlot`  (extends `Entity`)
The ChartPlot class is used to create and display XYChart Visualizations. ChartPlot is a container class that generates and manages one or more XYChart Visualizations. When the ChartPlot is created, the event attribute defines the results data displayed when XYChart Visualizations are created. The ChartPlot can be updated to display results associated to more than one event using the ChartPlot::update() method.

Methods:

- `activate() -> None` — Activate the ChartPlot.
- `clearAllDataSeries() -> None` — Clear all curves on the ChartPlot.
#### `createSBMTChart(target: apex.EntityCollection, yResultQuantity: apex.post.ResultQuantity, yResultDerivation: apex.post.ResultDerivation) -> apex.post.SBMTChart`
Creates SBMTChart and adds it to the ChartPlot. Use this method to add one or more SBMTChart curves to the ChartPlot.

- `target` — Entities on which the SBMTChart curves are defined; arc length will be calculated in target entity order
- `yResultQuantity` — The ResultQuantity (e.g. ForceBeam) for the Y values that will be used to draw the curve.
- `yResultDerivation` — The ResultDerivation for the Y values that will be used to draw the curve.

- `deactivate() -> None` — Deactivate the ChartPlot.
#### `update(event: apex.studies.Event, bAddEvent: apex.ApexBool, showDataSeriesMarkers: apex.ApexBool, showLegend: apex.ApexBool, maxminMarkerVisibility: apex.ApexBool, annotations: apex.ApexBool, bReplaceMode: apex.ApexBool) -> None`
Updates one or more properties of the ChartPlot. This method allow multiple properties of the ChartPlot to be updated using a single method call. Arguments are optional and the values of all ChartPlot properties associated with the omitted arguments are left unchanged. This method allows the CharPlot to be associated to morethan one event. It allows an event to be added to the ChartPlot by setting the bAddEvent to true. It can also be used to remove an event by seeting the bAddEvent to false.

- `event` — The Scenario Event for the results data that will be used to update the ChartPlot.
- `bAddEvent` — If true, add the previous specified event to the ChartPlot. Otherwise, remove it.
- `showDataSeriesMarkers` — If true display markers on curves.
- `showLegend` — If true, display legend.
- `maxminMarkerVisibility` — If true, show max/min markers.
- `annotations` — If true, display annotation at each point.
- `bReplaceMode` — If true, use Replace mode; If false, use Accumulate mode.


## `apex.post.ColorMap`  (extends `Entity`)
ColorMap - apex.post module class. Create using apex.post.createColorMap() method. This class is used to control how (scalar) data, usually associated to a mesh, is mapped to colors. It is used in both Contour (Fringe, Fill) and Vector Visualizations and will be eventually be used to support all color coded displays throughout Apex. ColorMap creation uses a default range of colors from "Cold" to "Hot". Colors can be manually mapped to specific colors using the TableValue and RGB colors. In future releases default color ranges will be supported. ColorMap currently provides two different approaches to define the number of colors and the scalar data ranges that map to each color using the "colorMapSegmentMethod" attribute. This attribute is an enumeration of type apex.post.ColorMapSegmentMethod that currently supports two values - "Linear" and "Manual" If the "Linear" method is active,.
Properties: `colorMapSegmentMethod`, `displayContinuousColors`, `end`, `isLocked`, `name`, `start`, `tableValues`, `useOutOfRangeColors`

Methods:

- `getColorMapSegmentMethod() -> apex.post.ColorMapSegmentMethod` — Returns the ColorMapSegmentMethod.
- `getDisplayContinuousColors() -> apex.ApexBool` — Returns a boolean indicating if the ColorMap uses continous varying colors for color .
- `getEnd() -> float` — Returns the ending value of ColorMap.
- `getName() -> str` — Returns the ColorMap name.
- `getStart() -> float` — Returns the starting value of ColorMap.
- `getTableValues() -> [apex.post.TableValue]` — Returns a list of TableValue - pair of (value, color).
- `getUseOutOfRangeColors() -> apex.ApexBool` — Returns a boolean indicating if out of range colors are used.
- `getisLocked() -> apex.ApexBool` — Returns a boolean indicating if the ColorMap is locked.
#### `update(name: str, colorMapSegmentMethod: apex.post.ColorMapSegmentMethod, start: float, end: float, tableValues: [apex.post.TableValue], isLocked: apex.ApexBool, useOutOfRangeColors: apex.ApexBool, displayContinuousColors: apex.ApexBool) -> None`
Updates one or more properties of the ColorMap. This method allows multiple properties of the object to be updated using a single method call. All arguments are optional and the values of all properties associated with the omitted arguments are left unchanged.

- `name` — ColorMap name.
- `colorMapSegmentMethod` — Optional parameter that sets the colorMapSegmentMethod used by the ColorMap.
- `start` — Optional argument that sets the starting value of the scalar data that is being color mapped.
- `end` — Optional argument that sets the ending value of the scalar data that is being color mapped.
- `tableValues` — Used if colorMapSegmentMethod = Manual, List of TableValue (double value, apex::ColorRGB) pairs that define the color segments.
- `isLocked` — If true, ColorMap definition can't be changed.
- `useOutOfRangeColors` — Optional argument that sets how scalar data that is "out of range" (above or below the start and end values) is color mapped. If "False" data that is outside the range defined by the "start" and "end" values will be colored with the "start" or "end" values. If "True", data that is out of the range of "start" and "end" values will be colored with the out of range colors.
- `displayContinuousColors` — Optional argument that sets whether the ColorMap will use continuous colors (True) or not (False).


## `apex.post.ContourVisualization`  (extends `DataVisualization`)
ContourVisualization is a class that represents contours, fringes and fill displays. When a ContourVisualization is added to a StatePlot (and is also Active in the StatePlot), the entities that are referenced in the target will be displayed using color coded line contours, fringes or element fill regions. This class provides methods and attributes to control the display, result quantity, result derivation, transformation, layers and all other aspects of the contour visualization. If the StatePlot also contains an active DeformVisualization and any of the entities in the ContourVisualization are also referenced by the ContourVisualization, the contours or fringes will be displayed in the deformed position.
Properties: `colorMap`, `compositeFailure`, `contourStyle`, `coordinateSystem`, `coordinateSystemMethod`, `elementNodalProcessing`, `layerEnvelopingMethod`, `layerIdentificationMethod`, `layers`, `resultDerivation`, `resultQuantity`

Methods:

- `getColorMap() -> apex.post.ColorMap` — Returns the Color Map.
- `getCompositeFailure() -> apex.post.CompositeFailure` — Returns the Composite Failure method. This is only applicable for Composite data.
- `getContourStyle() -> apex.post.ContourStyle` — Returns Contour Style.
- `getCoordinateSystem() -> apex.construct.CoordinateSystem` — Returns the CoordinateSystem information, if defined.
- `getCoordinateSystemMethod() -> apex.post.CoordinateSystemMethod` — Returns the System Type that the direction scalar data such as X-Component of Stress will be transformed to prior to display.
- `getCurrentResultQuantity() -> apex.post.ResultQuantity` — Returns the Result Quantity such as Stress.
- `getCurrentReusltDerivation() -> apex.post.ResultDerivation` — Returns the Result Derivation such as vonMises.
- `getElementNodalProcessing() -> apex.post.ElementNodalProcessing` — Returns the Element Nodal Processing method.
- `getLayerEnvelopingMethod() -> apex.post.LayerEnvelopingMethod` — Returns the Layer Enveloping Methods which is applicable when multiple layers are specified.
- `getLayerIdentificationMethod() -> apex.post.LayerIdentificationMethod` — Returns the Layer Identification Method.
- `getLayers() -> [str]` — Returns a list of layers, if applicable. Specific layers are usually used for 2D elements.
#### `update(contourStyle: apex.post.ContourStyle, target: apex.EntityCollection, resultQuantity: apex.post.ResultQuantity, resultDerivation: apex.post.ResultDerivation, layerIdentificationMethod: apex.post.LayerIdentificationMethod, layers: [str], layerEnvelopingMethod: apex.post.LayerEnvelopingMethod, elementNodalProcessing: apex.post.ElementNodalProcessing, coordinateSystemMethod: apex.post.CoordinateSystemMethod, compositeFailure: apex.post.CompositeFailure, colorMap: apex.post.ColorMap, coordinateSystem: apex.construct.CoordinateSystem = None, displayUnit: str) -> None`
Update ContourVisualization.

- `contourStyle` — Fringe or Fill style contours.
- `target` — An optional collection of entities that defines which regions of the Scenario ModelRep will be displayed using contour visualization. If omitted, the ContourVisualization will be applied to the entire Scenario ModelRep. Must contain only Parts and Assemblies - all other objects types will be silently ignored. Only Parts and Assemblies that are contained by the Scenario Model Rep associated with the Scenario and Event that generated the results data that this ContourVisualization are allowed otherwise the method will throw an exception.
- `resultQuantity` — The resultQuantity (e.g. Stress, Strain, Displacement etc.) that will be contoured by the contourVisualization. If no data is available for this resultQuantity for ANY of the target entities, the method will throw an exception.
- `resultDerivation` — The resultDerivation (e.g. VonMises) that will be applied to corresponding resultQuantity (e.g. Stress). If the resultDerivation is not valid for the corresponding resultQuantity the method will throw an exception.
- `layerIdentificationMethod` — Enumeration to define the approach used to identify layers in ContourVisualizations. For some result quantities, beam and shell elements generate results data at multiple "layers" - for example the top, bottom and middle surfaces of homogeneous shells, the "output points" in beams and the plies in composite shell elements. Different layer identification methods are supported across all elements that support layers and this argument defines how to interpret the data in the associated "layers" argument.
- `layers` — For some result quantities, beam and shell elements generate results data at multiple "layers" - for example the top, bottom and middle surfaces of homogeneous shells, the "output points" in beams and the plies in composite shell elements. This argument defines which layers will be used during calculation of the contour values. Apex supports multiple layer identification methods and the method used in this List is defined in the associated layerIdentificationMethod argument. If the List contains just a single layer, the results data for that layer will be processed directly. If the List contains more than one layer an enveloping operation such as "Min", "Max", "Average" etc. must be applied to reduce the multiple data values to a single value. In this case the "layerEnvelopingMethod" is used to choose which enveloping operation to use.
- `layerEnvelopingMethod` — Defines the enveloping method that will be applied when multiple layers are passed to the ContourVisualization. For some result quantities, beam and shell elements generate results data at multiple "layers" - for example the top, bottom and middle surfaces of homogeneous shells, the "output points" in Beams and the plies in composite shell elements. ContourVisualization supports processing of a single or multiple layers via the "layers" argument and each layer has an associated set of result data values - one per layer per element. Contouring must be performed on a single scalar value so when more than one layer is provided the data must be reduced to a single scalar value. The ContourVisualization class uses layer enveloping to perform this reduction and this argument defines, using an apex.post.LayerEnvelopingMethod enumeration, the enveloping algorithm will be used. See the documentation for apex.post.LayerEnvelopingMethod for a description of the supported layer enveloping methods. If this argument is omitted and multiple layers are supplied the default "Max" enveloping method will be used.
- `elementNodalProcessing` — Enumeration defining the element nodal processing approach that will used to calculate the contour. Details of the supported element nodal processing approaches are described in the apex.post.
- `coordinateSystemMethod` — Enumeration that defines how the contour coordinate system will be defined. When processing vector data ContourVisualization can transform the raw results data into a different coordinate system before displaying it. Different methods are supported to define the contour coordinate system and this argument defines which method will be used using an apex.post.CoordinateSystemMethod enumerations. The supported methods for defining coordinate system transformations are described in the apex.post.CoordinateSystemMethod documentation.
- `compositeFailure` — Composite failure criteria - Failure Index or Strength ratio..
- `colorMap` — The ColorMap that the ContourVisualization will use to assign colors to the target based on the result data values at each target location.
- `coordinateSystem` — Results output coordinate system that the results will be displayed in when the coordinateSystemMethod is apex.post.CoordinateSystemMethod.User.
- `displayUnit` — The display unit of the results data of the visualization.


## `apex.post.DataSeriesOverSteps`  (extends `DataSeries`)
Common post-processing/result analysis requires the ability to view the specific results through the simulation time or load increments, referred to general response charting.
Properties: `resultDerivation`, `resultQuantity`, `steps`, `targets`, `unitXaxis`, `unitYaxis`

Methods:

- `getResultDerivation() -> ResultDerivation` — Returns The Result Derivation that user want to check and plot.
- `getResultQuantity() -> ResultQuantity` — Returns the results quantity that user want to check and plot.
- `getSteps() -> apex.studies.StepCollection` — Returns the steps collection from which the results extracted.
- `getTargets() -> apex.EntityCollection` — Return the Plot target from which the results data extracted.
- `getUnitXaxis() -> str` — Returns the unit used in the Plot X.
- `getUnitYaxis() -> str` — Returns the unit used in the Plot in Y.

## `apex.post.DataSeriesOverStepsCollection`  (extends `DataSeriesCollection`)

Methods:

- `DataSeriesOverStepsCollection() -> None` — Construct a new DataSeriesOverStepsCollection.

## `apex.post.DataSeriesTransient`  (extends `DataSeries`)
Class representing the variation of a quantity over time Specifically intended to return quantities from transient dynamic/kinematic simulations and , since this class inherits apex.chart.DataSeries, enable display of such data in Apex XY charts. The X data in this class is expected to represent Time (the xunitquantiy property from apex.chart.DataSeries is overwritten with a read only "Time" value in this class) and the values are expected to be monotonically increasing across the domain.
Properties: `event`, `resultDerivation`, `resultQuantity`, `target`

Methods:

- `getEvent() -> apex.studies.Event` — Gets An event from which the transient data is extracted.
- `getResultDerivation() -> ResultDerivation` — Returns the ResultDerivation for which the data in this DataSeries was extracted.
- `getResultQuantity() -> ResultQuantity` — Returns the ResultQuantity for which the data in this DataSeries was extracted.
- `getTarget() -> apex.Entity` — Gets Optional target, as an apex.Entity for this DataSeriesTime. The target typically defines the object with which the data is associated..

## `apex.post.DataSeriesVMTBeamSpan`  (extends `DataSeries`)
Class holding pairs of data extracted from a BeamSpan. Primarily intended for use in the display of Shear, Bending Moment and Torsion diagrams. The class inherits from DataSeries. The X-data represents the distance from the start of the BeamSpan (End A) to each element node. The Y-data represents the Axial Force, Bending Moment, etc. data evaluated at the X-location.
Properties: `beamSpan`, `elementNodePositions`, `event`, `resultDerivation`, `resultQuantity`

Methods:

- `getBeamSpan() -> apex.attribute.BeamSpan` — Returns the BeamSpan from which the data in this DataSeries was extracted.
- `getElementNodePositions() -> [str]` — Returns a list of string defining the element nodes from which the underlying data was extracted The data used to display VMT diagrams from BeamSpans is associated with the Element Nodes from the BeamSpan. Because connected elements within a BeamSpan will share a common node and give rise to two VMT values for each shared node, it is not feasible to use either element ids or node ids, therefore we use element node positions. The topology of each Beam element is defined by two nodes - position 1 (the start node) and position 2 (the end node). The notation used to identify element nodes is a concatenation of the element ID, a "." separator and the Node position as an integer - "<ELEMENT_ID>.<NODE_POSITION>" For example the start node of element 123 would be identified as "123.1" A BeamSpan consisting of three connected and similarly aligned elements in sequence will be identified as, "123.1, 123.2, 124.1, 124.2, 125.1, 125.2".
- `getEvent() -> apex.studies.Event` — Returns the Event from which the data in this DataSeries was extracted.
- `getResultDerivation() -> ResultDerivation` — Returns the ResultDerivation for which the data in this DataSeries was extracted.
- `getResultQuantity() -> ResultQuantity` — Returns the ResultQuantity for which the data in this DataSeries was extracted.

## `apex.post.DataSeriesVMTSensorArray`  (extends `DataSeries`)
Class holding pairs of data extracted from a XSectionForceSensorArray. Primarily intended for use in the display of Shear, Bending Moment and Torsion diagrams. The class inherits from DataSeries. The X-data represents the distance from the first XSectionForceSensor to the last XSectionForceSensor in XSectionForceSensorArray. The Y-data represents the Cross Section Forces and Moments evaluated at the summation location.
Properties: `event`, `resultQuantity`, `vectorComponent`, `xSensorArray`

Methods:

- `getEvent() -> apex.studies.Event` — Returns the Event from which the data in this DataSeries was extracted.
- `getResultQuantity() -> ResultQuantity` — Returns the ResultQuantity for which the data in this DataSeries was extracted.
- `getVectorComponent() -> VectorComponent` — Returns the VectorComponent for which the data in this DataSeries is displayed.
- `getXSensorArray() -> apex.instrument.XSectionForceSensorArray` — Returns the XSectionForceSensorArray from which the data in this DataSeries was extracted.

## `apex.post.DataVisualization`  (extends `Entity`)
DataVisualization - A base class for the specific DataVisualization classes.
Properties: `displayUnit`, `target`

Methods:

- `asContourVisualization() -> apex.post.ContourVisualization`
- `asDeformVisualization() -> apex.post.DeformVisualization`
- `asVectorVisualization() -> apex.post.VectorVisualization`
- `getDisplayUnit() -> str` — Return the display unit of the data the visualization is showing.
- `getTarget() -> apex.EntityCollection` — Return the Target entities used for this DataVisualization.

## `apex.post.DeformVisualization`  (extends `DataVisualization`)
Represents the deformed shape visualization aspects of a StatePlot.
Properties: `absoluteScalingFactor`, `deformScalingMethod`, `relativeScalingFactor`

Methods:

- `getAbsoluteScalingFactor() -> float` — Returns the Absolute Scaling Factor.
- `getDeformScalingMethod() -> apex.post.DeformScalingMethod` — Returns the Deform Scaling Method.
- `getRelativeScalingFactor() -> float` — Returns the Relative Scaling Factor.
#### `update(target: apex.EntityCollection, deformScalingMethod: apex.post.DeformScalingMethod, relativeScalingFactor: float, absoluteScalingFactor: float) -> None`
Updates one or more properties of the DeformVisualization. This method allows multiple properties of the DeformVisualization to be updated using a single method call. All arguments are optional and the values of all DeformVisualization properties associated with the omitted arguments are left unchanged. If the DeformVisualization is active and the parent StatePlot is displayed when this method is called it will remain unchanged until all updates have been completed and then be replaced by the completely updated visualization.

- `target` — An optional collection of entities that defines which regions of the Scenario ModelRep will be displayed in their deformed state. If omitted, the DeformVisualization will be applied to the entire Scenario ModelRep. Must contain only Parts and Assemblies - all other objects types will be silently ignored. Only Parts and Assemblies that are contained by the Scenario Model Rep associated with the Scenario and Event that generated the results data that this DeformVisualization are allowed otherwise the method will throw an exception.
- `deformScalingMethod` — Optional parameter that defines whether the DeformationVisualization object will use Absolute or Relative (Default) deformation scaling. A valid value for the chosen scale factor (relativeScaleFactor or absoluteScalefactor)must already exist in the object or be supplied in the same update call, otherwise the method will throw an exception.
- `relativeScalingFactor` — Deformation scale factor that will be used when Relative deformation scaling is active. This factor defines the ratio between the offset associated with the location of maximum deformation and the size of the viewport. Relative Scale factors are useful when true displacements are very small and it is required to exaggerate the deformation to identify the deformed shape. This value is only used if the deformScalingStyle for this visualization is set to Relative scaling.
- `absoluteScalingFactor` — Deformation scale factor that will be used when Absolute deformation scaling is active. This factor defines the ratio between the offset associated with the location of maximum deformation and the calculated offset (deformation). This value is only used if the deformScalingStyle for this visualization is set to Absolute scaling.


## `apex.post.ResultProbe0D`  (extends `Entity`)
ResultProbe0D - apex.post module class. Create using apex.post.createResultProbe0D() method. This class respresents the Apex 0D Results Probe. It can be used within post-processing to display digital values of results data in the graphics viewport. The probe extracts data from a single supplied DataVisualization object at a set of supplied target Entities. Methods are provided to modify the set of target entities and to update the DataVisualization. Configure the DataVisualization with the Result Quantity and Derivation you wish to probe.
Properties: `probeTargetEntities`, `units`

Methods:

#### `addProbeTargetEntities(probeTarget: apex.EntityCollection, probeTargetUpdateMode: apex.post.ProbeTargetUpdateMode) -> None`
Modifies the set of target Entities at which the Probe will evaluate the results data, display on the viewport and add to the data grid. The behavior of this method can be controlled by the optional probetargetUpdateMode argument to Add or Remove the supplied Entities to the Probe.

- `probeTarget` — : The Entities to Add or Remove.
- `probeTargetUpdateMode` — : An optional argument that controls how the method operates on the supplied Entities. The default apex::post::ProbeTargetUpdateMode.Add will add all supplied Entities to any Entities that are already in the Probe target. The method will ensure that the Probe target does not contain duplicate entities. Setting to apex.post.ProbeTargetUpdateMode.Remove will remove all supplied Entities from the set of Entities that are already in the Probe target. Any supplied entities that are NOT already in the Probe target will be silently ignored.

#### `addProbeTargetEntity(probeTarget: apex.Entity, probeTargetUpdateMode: apex.post.ProbeTargetUpdateMode) -> None`
Modifies the set of target Entities at which the Probe will evaluate the results data, display on the viewport and add to the data grid. The behavior of this method can be controlled by the optional probetargetUpdateMode argument to Add or Remove the supplied Entity to the Probe.

- `probeTarget` — : The Entity to Add or Remove.
- `probeTargetUpdateMode` — : An optional argument that controls how the method operates on the supplied Entity. The default apex::post::ProbeTargetUpdateMode.Add will add all supplied Entities to any Entities that are already in the Probe target. The method will ensure that the Probe target does not contain duplicate entities. Setting to apex.post.ProbeTargetUpdateMode.Remove will remove all supplied Entities from the set of Entities that are already in the Probe target. Any supplied entities that are NOT already in the Probe target will be silently ignored.

- `clearProbe() -> None` — Clears all Entities from this Probe causing all of its labels and the data grid to be cleared.
- `deleteProbe() -> None` — When "exit probe tool" occurs.
#### `exportDataCSV(filename: str) -> None`
Exports the contents of the probe (Data Grid) to a named .csv file.

- `filename` — : The path qualified name of the .csv file that the 0D probe data will be written to.

- `getProbeTargetEntities() -> apex.EntityCollection` — Returns the target entitites associated with this ResultProbe0D..
- `getUnits() -> str` — Returns the units associated with this ResultProbe0D.
#### `setProbeDataVisualization(dataVisualization: apex.post.DataVisualization) -> None`
Sets the DataVisualization that the probe will use to evaluate results data values. The supplied DataVisualization will replace any existing DataVisualization that exist in the Probe and will update all existing result data values to reflect the Result Quantity and Derivation that are set in the Probe.

- `dataVisualization` — : DataVisualization that the probe will use.


## `apex.post.StatePlot`  (extends `Entity`)
The StatePlot class is used to create and display plots of deformed shape, color coded contours (fringe, fill) and vectors. StatePlot is a container class that generates and manages one or more DataVisualizations. Specific DataVisualizations are provided to display deformed shape (DeformVisualization), contours (ContourVisualization) and vectors (VectorVisualization). Any combination of DataVisualizations (subject to a maximum of one of each type) can be created to generate different types of StatePlot. For example,.
Properties: `event`, `resultDataSetIndex`, `visualizations`

Methods:

- `activate() -> None` — activate the StatePlot.
#### `activateVisualization(dataVis: apex.post.DataVisualization) -> None`
Unmasks an existing DataVisualization within a StatePlot if it is currently masked.

- `dataVis` — The DataVisualization to activate.

- `active() -> None`
#### `createContourVisualization(contourStyle: apex.post.ContourStyle = apex.post.ContourStyle.Fringe, target: apex.EntityCollection = None, resultQuantity: apex.post.ResultQuantity = apex.post.ResultQuantity.Stress, resultDerivation: apex.post.ResultDerivation = apex.post.ResultDerivation.VonMises, layerIdentificationMethod: apex.post.LayerIdentificationMethod = apex.post.LayerIdentificationMethod.Position, layers: [str] = std.vector< std.string >(1,"Z2"), layerEnvelopingMethod: apex.post.LayerEnvelopingMethod = apex.post.LayerEnvelopingMethod.Max, elementNodalProcessing: apex.post.ElementNodalProcessing = apex.post.ElementNodalProcessing.Averaged, coordinateSystemMethod: apex.post.CoordinateSystemMethod = apex.post.CoordinateSystemMethod.Global, compositeFailure: apex.post.CompositeFailure = apex.post.CompositeFailure.StrengthRatio, colorMap: apex.post.ColorMap = None, coordinateSystem: apex.construct.CoordinateSystem = None, displayUnit: str = "MPa") -> apex.post.ContourVisualization`
Creates a ContourVisualization and adds it to the StatePlot. If a ContourVisualization already exists in the StatePlot it will be replaced by the new one. Use this method to create a fringe or fill contour visualization or add fringe/fill ContourVisualization to an existing deformation or VectorVisualization. The scope of the contour visualization (Parts, Assemblies) can be defined using the "target" argument. Other arguments enable initialization of the ContourVisualization parameters during construction.

- `contourStyle` — Fringe or Fill style contours.
- `target` — An optional collection of entities that defines which regions of the Scenario ModelRep will be displayed using contour visualization. If omitted, the ContourVisualization will be applied to the entire Scenario ModelRep. Must contain only Parts and Assemblies - all other objects types will be silently ignored. Only Parts and Assemblies that are contained by the Scenario Model Rep associated with the Scenario and Event that generated the results data that this ContourVisualization are allowed otherwise the method will throw an exception.
- `resultQuantity` — The resultQuantity (e.g. Stress, Strain, Displacement etc.) that will be contoured by the ContourVisualization. If no data is available for this resultQuantity for ANY of the target entities, the method will throw an exception.
- `resultDerivation` — The resultDerivation (e.g. VonMises) that will be applied to corresponding resultQuantity (e.g. Stress). If the resultDerivation is not valid for the corresponding resultQuantity the method will throw an exception.
- `layerIdentificationMethod` — Enumeration to define the approach used to identify layers in ContourVisualization. For some result quantities, beam and shell elements generate results data at multiple "layers" - for example the top, bottom and middle surfaces of homogeneous shells, the "output points" in beams and the plies in composite shell elements. Different layer identification methods are supported across all elements that support layers and this argument defines how to interpret the data in the associated "layers" argument.
- `layers` — For some result quantities, beam and shell elements generate results data at multiple "layers" - for example the top, bottom and middle surfaces of homogeneous shells, the "output points" in beams and the plies in composite shell elements. This argument defines which layers will be used during calculation of the contour values. Apex supports multiple layer identification methods and the method used in this List is defined in the associated layerIdentificationMethod argument. If the List contains just a single layer, the results data for that layer will be processed directly. If the List contains more than one layer an enveloping operation such as "Min", "Max", "Average" etc. must be applied to reduce the multiple data values to a single value. In this case the "layerEnvelopingMethod" is used to choose which enveloping operation to use.
- `layerEnvelopingMethod` — Defines the enveloping method that will be applied when multiple layers are passed to the ContourVisualization. For some result quantities, beam and shell elements generate results data at multiple "layers" - for example the top, bottom and middle surfaces of homogeneous shells, the "output points" in Beams and the plies in composite shell elements. ContourVisualization supports processing of a single or multiple layers via the "layers" argument and each layer has an associated set of result data values - one per layer per element. Contouring must be performed on a single scalar value so when more than one layer is provided the data must be reduced to a single scalar value. The ContourVisualization class uses layer enveloping to perform this reduction and this argument defines, using an apex.post.LayerEnvelopingMethod enumeration, the enveloping algorithm will be used. See the documentation for apex.post.LayerEnvelopingMethod for a description of the supported layer enveloping methods. If this argument is omitted and multiple layers are supplied the default "Max" enveloping method will be used. If the List contains just a single layer, the results data for that layer will be processed directly and the value of this argument is ignored.
- `elementNodalProcessing` — Enumeration defining the element nodal processing approach that will used to calculate the contour. Details of the supported element nodal processing approaches are described in apex.post.
- `coordinateSystemMethod` — Enumeration that defines how the contour coordinate system will be defined. When processing vector data ContourVisualization can transform the raw results data into a different coordinate system before displaying it. Different methods are supported to define the contour coordinate system and this argument defines which method will be used in an apex.post.CoordinateSystemMethod enumerations. The supported methods for defining coordinate system transformations are described in the apex.post.CoordinateSystemMethod documentation.
- `compositeFailure` — Composite failure criteria - Failure Index or Strength ratio.
- `colorMap` — The ColorMap that the ContourVisualization will use to assign colors to the target based on the result data values at each target location.
- `coordinateSystem` — Results output coordinate system that the results will be displayed in when the coordinateSystemMethod is apex.post.CoordinateSystemMethod.User.
- `displayUnit` — The display unit of the results data of the visualization.

#### `createDeformVisualization(target: apex.EntityCollection = None, deformScalingMethod: apex.post.DeformScalingMethod = apex.post.DeformScalingMethod.Relative, relativeScalingFactor: float = 10.0, absoluteScalingFactor: float = 1.0, displayUnit: str = "mm") -> apex.post.DeformVisualization`
Creates a DeformVisualization and adds it to the StatePlot. If a DeformVisualization already exists in the StatePlot it will be replaced by the new one. Use this method to create a deformed shape or add deformation to an existing contour or vector visualization. The scope of the deformation visualization (Parts, Assemblies) can be defined using the "target" argument. Other arguments enable initialization of the deformation visualization parameters during construction.

- `target` — An optional collection of entities that defines which regions of the Scenario ModelRep will be displayed in their deformed state. If omitted, the DeformVisualization will be applied to the entire Scenario ModelRep. Must contain only Parts and Assemblies - all other objects types will be silently ignored. Only Parts and Assemblies that are contained by the Scenario Model Rep associated with the Scenario and Event that generated the results data that this DeformVisualization are allowed otherwise the method will throw an exception.
- `deformScalingMethod` — Optional parameter that defines whether to use Absolute or Relative (Default) deformation scaling
- `relativeScalingFactor` — Deformation scale factor that will be used when Relative deformation scaling is active. This factor defines the ratio between the offset associated with the location of maximum deformation and the size of the viewport. Relative Scale factors are useful when true displacements are very small and it is required to exaggerate the deformation to identify the deformed shape. This value is only used if the deformScalingStyle for this visualization is set to Relative scaling.
- `absoluteScalingFactor` — Deformation scale factor that will be used when Absolute deformation scaling is active. This factor defines the ratio between the offset associated with the location of maximum deformation and the calculated offset (deformation). This value is only used if the deformScalingStyle for this visualization is set to Absolute scaling.
- `displayUnit` — The display unit of the results data of the visualization.

#### `createVectorVisualization(vectorColorMethod: apex.post.VectorColorMethod = apex.post.VectorColorMethod.VectorValue, targetEntityType: apex.post.TargetEntityType = apex.post.TargetEntityType.Node, target: apex.EntityCollection = None, resultQuantity: apex.post.ResultQuantity = apex.post.ResultQuantity.DisplacementTranslational, vectorComponentColors: {apex.post.VectorComponent:apex.ColorRGB} = {{apex.post.VectorComponent.Resultant, apex.ColorRGB(224, 224, 224)}}, coordinateSystemMethod: apex.post.CoordinateSystemMethod = apex.post.CoordinateSystemMethod.Global, vectorScalingMethod: apex.post.VectorScalingMethod = apex.post.VectorScalingMethod.Scaled, vectorDisplayScalingFactor: float = 30., enableVectorZoom: apex.ApexBool = ApexBoolTrue, originLocation: apex.post.VectorOriginLocation = apex.post.VectorOriginLocation.Tip, vectorDisplayStyle: apex.post.VectorDisplayStyle = apex.post.VectorDisplayStyle.Vector3D, enableApplyFilter: apex.ApexBool = ApexBoolFalse, arrowDisplayFilter: float = 0.01, colorMap: apex.post.ColorMap = None, coordinateSystem: apex.construct.CoordinateSystem = None, displayUnit: str = "mm") -> apex.post.VectorVisualization`
Creates a VectorVisualization and adds it to the StatePlot.

- `vectorColorMethod` — An enumeration that defines whether the vectors displayed by this visualization will be color coded according to the underlying vector value (in conjunction with the active ColorMap) or by component.
- `targetEntityType` — Entity type that the vectors for this visualization will be displayed on. The default entity type is nodes. When VectorVisualization is targeted on connector objects the target entity type can be object end points or object middle point.
- `target` — An optional collection of entities that defines which regions of the Scenario ModelRep will be displayed using vector visualization. If omitted, the VectorVisualization will be applied to the entire Scenario ModelRep. Must contain only Parts and Assemblies - all other objects types will be silently ignored. Only Parts and Assemblies that are contained by the Scenario Model Rep associated with the Scenario and Event that generated the results data that this VectorVisualization are allowed otherwise the method will throw an exception.
- `resultQuantity` — An enumeration of the vector data that will be displayed.
- `vectorComponentColors` — Pairs of vector components as apex.post.VectorComponent and their associated colors as apex.RGBColor to include in the VectorVisualization.
- `coordinateSystemMethod` — Enumeration that defines how the contour coordinate system will be defined. When processing vector or tensor data VectorVisualization can transform the raw results data into a different coordinate system before displaying it. Different methods are supported to define the vector coordinate system and this argument defines which method will be used using an apex.post.CoordinateSystemMethod enumerations. The supported methods for defining coordinate system transformations are described in the apex.post.CoordinateSystemMethod documentation.
- `vectorScalingMethod` — An enumeration that controls the scaling of vectors proportional to their vector value. The default value of "Scaled" causes vectors to be drawn using a length proportional to the underlying vector value. Setting the value to "Constant" causes all vectors to be drawn with the same length, regardless of the underlying vector value.
- `vectorDisplayScalingFactor` — A scale factor (default 0.3) that adjusts the base length of displayed vectors.
- `enableVectorZoom` — Controls how the vector display scaling changes with respect to viewing distance. Setting to "False" (default) causes the vector display size to remain constant as the view distance increases/decreases during graphical zooming. Setting to "True" causes the vector display size to decrease and increase as the view distance increases/decreases during graphical zooming.
- `originLocation` — An enumeration that controls how the vector display is anchored to the location.
- `vectorDisplayStyle` — An enumeration that defines how the system render the vector. The default "Vector3D" renders each vector as a solid shaded arrow. This option is graphically rich and works well for plots with a modest number of vectors. For plots with large numbers of vectors, options are provided for lower fidelity rendering of arrows which can be both more aesthetically pleasing and performant.
- `enableApplyFilter` — Apply Filter
- `arrowDisplayFilter` — Controls how to filter vector arrows (default is 0.01)
- `colorMap` — The ColorMap that defines the spectrum of colors that each vector value will be mapped to, if the vectorColorMethod is set to VectorValue.
- `coordinateSystem` — The coordinate system that the vector data will be transformed to prior to display as an apex.Construct.CoordinateSystem. Vector data is always displayed relative to a coordinate system. The coordinate system may be rectangular, cylindrical or spherical and the raw vector data will be transformed from its original coordinate system into this coordinate system before it is displayed.
- `displayUnit` — The display unit of the results data of the visualization.

If a VectorVisualization already exists in the StatePlot it will be replaced by the new one. Use this method to create a vector visualization or add vector visualization to an existing deformation or contour visualization. The scope of the vector visualization (Parts, Assemblies) can be defined using the "target" argument. Other arguments enable initialization of the vector visualization parameters during construction.

- `deactivate() -> None` — deactivate the StatePlot.
#### `deactivateVisualization(dataVis: apex.post.DataVisualization) -> None`
Temporarily masks a DataVisualization within the StatePlot.

- `dataVis` — The DataVisualization to temporarily deactivate.

- `getEvent() -> apex.studies.Event` — Returns the Scenario Event associated with this StatePlot.
- `getResultDataSetIndex() -> [int]` — Returns the Result Data Set Index for Scenario Events that have multiple data sets such as Modes or Buckling events.
- `getVisualization(entityType: apex.EntityType) -> apex.post.DataVisualization` — Returns DataVisualization in the StatePlot for the given entityType. If the DataVisualization for the given entityType doesn't exist then a null pointer will be returned.
- `getVisualizations() -> {apex.post.DataVisualization:bool}` — Returns a Dictionary of all DataVisualizations that are present in the StatePlot. The Dictionary key type is DataVisualization and the value type is boolean. For each DataVisualization key in the Dictionary the value indicates wheter it is Active (True) or Inactive(False). If no DataVisualizations are present the Dictionary will be empty.
- `hide() -> None` — Hides the StatePlot.
- `removeAllVisualizations() -> None` — Removes all DataVisualizations from the StatePlot.
#### `removeVisualization(dataVis: apex.post.DataVisualization) -> None`
Removes a visualization from the StatePlot.

- `dataVis` — The DataVisualization to remove from the StatePlot.

- `show() -> None` — Displays the StatePlot.
#### `update(event: apex.studies.Event, resultDataSetIndex: [int]) -> None`
Updates one or more properties of the StatePlot. This method allows multiple properties of the StatePlot to be updated using a single method call. All arguments are optional and the values of all StatePlot properties associated with the omitted arguments are left unchanged. If the StatePlot is visible when this method is called it will remain unchanged until all updates have completed and then be replaced by the completely updated plot.

- `event` — The Scenario Event that created the results data that will be used in the created StatePlot.
- `resultDataSetIndex` — If the Scenario Scenario Event associated with this State Plot generates multiple sets of results data, for example, Normal Modes or Buckling, this argument defines which set of results data will be used. The index is 1 based. In the case of an Event associated with a Normal Modes analysis this index identifies the specific mode that will be plotted. In the case of an Event associated with a Buckling analysis this index identifies the specific buckling mode that will be plotted.


## `apex.post.TableValue`
TableValue defines a pair of (dataValues, colorRGB). A list of TableValue pairs are used to specify the color segment for a ColorMap.
Properties: `color`, `value`

Methods:

- `TableValue(value: float = NAN, color: apex.ColorRGB = apex.ColorRGB(0, 0, 0)) -> None`
- `getColor(: None) -> apex.ColorRGB`
- `getValue(: None) -> float`
- `setColor(color: apex.ColorRGB) -> None`
- `setValue(value: float) -> None`

## `apex.post.VectorVisualization`  (extends `DataVisualization`)
VectorVisualization is a class that represents vector displays. When a VectorVisualization is added to a StatePlot (and is also Active in the StatePlot), the entities that are referenced in the target will be displayed using color coded arrows (vectors). This class provides methods and attributes to control the display, result quantity, result derivation, transformation and all other aspects of the vector visualization. If the StatePlot contains an active DeformVisualization and any of the entities in the VectorVisualization are also referenced by the DeformVisualization, the vectors will be displayed in the deformed position.
Properties: `arrowDisplayFilter`, `colorMap`, `coordinateSystem`, `coordinateSystemMethod`, `enableApplyFilter`, `enableVectorZoom`, `originLocation`, `resultQuantity`, `targetEntityType`, `vectorColorMethod`, `vectorComponentColors`, `vectorDisplayScalingFactor`, `vectorDisplayStyle`, `vectorScalingMethod`

Methods:

- `getApplyFilter() -> apex.ApexBool` — Returns enable apply filter boolean.
- `getArrowDisplayFilter() -> float` — Returns the vector arrows display filter.
- `getColorMap() -> apex.post.ColorMap` — Returns the Color Map used to color code vectors if the VectorColorMethod is VectorValue.
- `getCoordinateSystem() -> apex.construct.CoordinateSystem` — Returns the CoordinateSystem information, if defined.
- `getCoordinateSystemMethod() -> apex.post.CoordinateSystemMethod` — Returns the System Type that the vector data will be transformed to prior to display.
- `getResultQuantity() -> apex.post.ResultQuantity` — Returns the Result Quantity.
- `getTargetEntityType() -> apex.post.TargetEntityType` — Returns the Target Entity Type.
- `getVectorColorMethod() -> apex.post.VectorColorMethod` — Returns the Vector Color Method that defines how the vectors will be color coded.
- `getVectorComponentColors() -> {apex.post.VectorComponent:apex.ColorRGB}` — Returns the Vector Components.
- `getVectorDisplayScalingFactor() -> float` — Returns the Vector Display scaling factor.
- `getVectorDisplayStyle() -> apex.post.VectorDisplayStyle` — Returns the Vector Display Style that specifies how the vector will be rendered. For example, if Vector3D is specified then a solid shaded vector is rendered.
- `getVectorOriginLocation() -> apex.post.VectorOriginLocation` — Returns the Vector Origin Location. Origin location can be at the vector Tip or Tail.
- `getVectorScalingMethod() -> apex.post.VectorScalingMethod` — Returns the Vector Scaling Method.
- `getVectorZoom() -> apex.ApexBool` — Returns the Vector Zoom boolean that determines whether or not vectors will scaled with viewing distance.
#### `update(vectorColorMethod: apex.post.VectorColorMethod, targetEntityType: apex.post.TargetEntityType, target: apex.EntityCollection, resultQuantity: apex.post.ResultQuantity, vectorComponentColors: {apex.post.VectorComponent:apex.ColorRGB}, coordinateSystemMethod: apex.post.CoordinateSystemMethod, vectorScalingMethod: apex.post.VectorScalingMethod, vectorDisplayScalingFactor: float, enableVectorZoom: apex.ApexBool, originLocation: apex.post.VectorOriginLocation, vectorDisplayStyle: apex.post.VectorDisplayStyle, enableApplyFilter: apex.ApexBool, arrowDisplayFilter: float, colorMap: apex.post.ColorMap, coordinateSystem: apex.construct.CoordinateSystem, displayUnit: str) -> None`
Update VectorVisualization.

- `vectorColorMethod` — An enumeration that defines whether the vectors displayed by this visualization will be color coded according to the underlying vector value (in conjunction with the active ColorMap) or by component.
- `targetEntityType` — Entity type that the vectors for this visualization will be displayed on. The default entity type is nodes. When VectorVisualization is targeted on connector objects the target entity type can be object end points or object middle point.
- `target` — An optional collection of entities that defines which regions of the Scenario ModelRep will be displayed using vector visualization. If omitted, the VectorVisualization will be applied to the entire Scenario ModelRep. Must contain only Parts and Assemblies - all other objects types will be silently ignored. Only Parts and Assemblies that are contained by the Scenario Model Rep associated with the Scenario and Event that generated the results data that this VectorVisualization are allowed otherwise the method will throw an exception.
- `resultQuantity` — An enumeration of the vector data that will be displayed.
- `vectorComponentColors` — A table of vector components as apex.post.VectorComponent and their associated colors as apex.RGBColor to include in the VectorVisualization.
- `coordinateSystemMethod` — Enumeration that defines how the contour coordinate system will be defined. When processing vector or tensor data VectorVisualization can transform the raw results data into a different coordinate system before displaying it. Different methods are supported to define the vector coordinate system and this argument defines which method will be used using an apex.post.CoordinateSystemMethod enumerations. The supported methods for defining coordinate system transformations are described in the apex.post.CoordinateSystemMethod documentation.
- `vectorScalingMethod` — An enumeration that controls the scaling of vectors proportional to their vector value. The default value of "Scaled" causes vectors to be drawn using a length proportional to the underlying vector value. Setting the value to "Constant" causes all vectors to be drawn with the same length, regardless of the underlying vector value.
- `vectorDisplayScalingFactor` — A scale factor (default 0.3) that adjusts the base length of displayed vectors.
- `enableVectorZoom` — Controls how the vector display scaling changes with respect to viewing distance. Setting to "False" (default) causes the vector display size to remain constant as the view distance increases/decreases during graphical zooming. Setting to "True" causes the vector display size to decrease and increase as the view distance increases/decreases during graphical zooming.
- `originLocation` — An enumeration that controls how the vector display is anchored to the location.
- `vectorDisplayStyle` — An enumeration that defines how the system renders the vector. The default "Vector3D" renders each vector as a solid shaded arrow. This option is graphically rich and works well for plots with a modest number of vectors. For plots with large numbers of vectors, options are provided for lower fidelity rendering of arrows which can be both more aesthetically pleasing and performant.
- `enableApplyFilter` — contorls to trun on/off apply filter
- `arrowDisplayFilter` — Constrols how to filter vector arrows using filter value: default value is 0.01
- `colorMap` — The ColorMap that defines the spectrum of colors that each vector value will be mapped to, if the vectorColorMethod is set to VectorValue.
- `coordinateSystem` — The coordinate system that the vector data will be transformed to prior to display as an apex.Construct.CoordinateSystem. Vector data is always displayed relative to a coordinate system. The coordinate system may be rectangular, cylindrical or spherical and the raw vector data will be transformed from its original coordinate system into this coordinate system before it is displayed.
- `displayUnit` — The display unit of the results data of the visualization.


