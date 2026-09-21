# apex.datavis

(apex.datavis module) Functions used to visualize data.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.datavis.CoordinateSystemMethod`: `Global`, `Local`, `User`
  - Which method is used to define coordinate system transformations to the result quantity data if it is vector or tensor type. Specify CoordinateSystemMethod by using the syntax apex.datavis.CoordinateSystemMethod."<enum_value>" For example: apex.datavis.CoordinateSystemMethod.Global Global - Display data is presented in the Gloabl coordinate system. Local - Display data is presented in aLlocal coordinate system. User - Display data is presented in user defined coordinate system

`apex.datavis.DiscreteSummedVectorDisplay`: `Summed`, `Discrete`
  - In LoadSummationPlots to control the display of discrete and summed vectors. Specify DiscreteSummedVectorDisplay by using the syntax apex.datavis.DiscreteSummedVectorDisplay."<enum_value>" For example: apex.datavis.DiscreteSummedVectorDisplay.Summed Summed selects display of summed vectors only. Discrete selects display of discrete vectors only

`apex.datavis.ForceMomentVectorDisplay`: `Both`, `Force`, `Moment`
  - In LoadSummationPlots to control the display of Force and Moment vectors. Specify ForceMomentVectorDisplay by using the syntax apex.datavis.ForceMomentVectorDisplay."<enum_value>" For example: apex.datavis.ForceMomentVectorDisplay.Both Both selects display of both Force and Moment vectors. Force selects display of Force vectors only. Moment selects display of Moment vectors only

`apex.datavis.VectorComponent`: `Resultant`, `Component1`, `Component2`, `Component3`, `Resultant12`, `Resultant23`, `Resultant13`
  - Supported vector components in Apex. Specify VectorComponent by using the syntax apex.datavis.VectorComponent."<enum_value>" For example: apex.datavis.VectorComponent.Resultant For example: apex.datavis.VectorComponent.Component1 is used to specify the 1st component of the vector data. The enumeration provides values for each of the three orthogonal vector components of a vector in three dimensions, plus three "2D resultants" and one "3D resultant"

`apex.datavis.VectorDisplayAnchorStyle`: `Tip`, `Tail`
  - To select how the vector display arrows are displayed relative to their associated locations. Arrows can be positioned with either their tips or tails coincident with the location. Specify VectorDisplayAnchorStyle by using the syntax apex.datavis.VectorDisplayAnchorStyle."<enum_value>" For example: apex.datavis.VectorDisplayAnchorStyle.Tip Tip displays the arrow tip coincident with the location. Tail displays the arrow tail coincident with the location

`apex.datavis.VectorDisplayColorMethod`: `VectorValue`, `Component`
  - How displayed vectors will be colored. Specify VectorDisplayColorMethod by using the syntax apex.datavis.VectorDisplayColorMethod."<enum_value>" For example: apex.datavis.VectorDisplayColorMethod.VectorValue VectorValue option causes individual vectors to be color coded according to the ColorMap color that maps to the vector value. This displays a plot where every vector is color coded according to its value. Component option causes individual vectors to be color coded according to their component color. Colors can be specified independently for each component however all occurrences of that vector component will have the same color, regardless of its value

`apex.datavis.VectorDisplayScalingMethod`: `Scaled`, `Constant`
  - Whether the vector display arrows are displayed proportionally to the magnitude of the vector or all vectors are displayed with an equal length, irrespective of the underlying vector value. Specify VectorDisplayScalingMethod by using the syntax apex.datavis.VectorDisplayScalingMethod."<enum_value>" For example: apex.datavis.VectorDisplayScalingMethod.Constant Constant display all vectors with the same constant length, irrespective of the underlying vector value. Scaled displays all vectors with a length proportional to the value of the underlying vector value

`apex.datavis.VectorDisplayStyle`: `ArrowShaded`, `ArrowWireFrame`, `Line`
  - To identify how vectors are displayed in plots. Specify VectorDisplayStyle by using the syntax apex.datavis.VectorDisplayStyle."<enum_value>" For example: apex.datavis.VectorDisplayStyle.ArrowShaded ArrowShaded - Vectors can be displayed using high fidelity 3D solid shaded arrows, 3D wireframe arrows or simple line segments. 3D solid shaded arrows provide the best visual appearance and are recommended when only a few vectors are being displayed since they can be computationally expensive to draw and can lead to clutter if many vectors are being displayed. ArrowWireFrame - 3D wireframe arrows offer a mid range option and are moderatedly pleasing to view and relatively computationally cheap to draw. Line - Simple line displays are computationally cheap to display and work well when a large number of vectors are displayed

## Module functions

### `apex.datavis.createVectorComponentColor() -> {apex.datavis.VectorComponent:apex.ColorRGB}`
Creates a VectorComponentColor empty map used for XSectionForceSensorPlot.

This can be populated with std::map syntax vectorComponentColor[apex::datavis::VectorComponent key] = ColorRGB() value

## Classes in this module

Full method signatures are in `api/classes/apex.datavis.md`.

`LoadSummationPlot`, `XSectionForceSensorPlot`

