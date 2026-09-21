# apex.chart — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.chart.ChartPlotXY`  (extends `Entity`, `IName`)
ChartPlotXY supports creation, modification and display of one or more XY charts within a single ChartPlot container. The class manages one or more individual XY charts automatically, however this convenience also reduces control over the individual charts.
Properties: `dataSeriesLabelVisibility`, `dataSeriesList`, `legendVisibility`, `markerVisibility`, `maxMinMarkerVisibility`

Methods:

- `activate() -> None` — Activates the ChartPlotXY.
- `addDataSeries(dataSeries: apex.chart.DataSeries) -> None` — Adds a DataSeries to this Chart. If the DataSeries is already included in this Chart it will be silently ignored.
- `addDataSeriesList(dataSeriesList: [apex.chart.DataSeries]) -> None` — Adds a list of DataSeries to this Chart. If the DataSeries is already included in this Chart it will be silently ignored.
- `clearAllDataSeries() -> None` — Removes all DataSeries from this Chart.
- `deactivate() -> None` — Deactivates the ChartPlotXY.
- `getDataSeriesLabelVisibility() -> bool` — Returns a Boolean value indicating the visibility of the DataSeries labels on this chart. A value of True indicates that the labels are visible and a value of False indicates that they are hidden.
- `getDataSeriesList() -> [apex.chart.DataSeries]` — Returns the List of all DataSeries in this Chart.
#### `getDescription() -> str`
Read-only string representing the description of this object. The description field usually appears the Object Property panel in the interactive UI and in some cases will appear in the Tool property panel of the tool that creates the object.

Returns: this entity description (string)

getDescription() may also be accessed as an Entity property 'description'. For example:

- `getLegendVisibility() -> bool` — Returns a Boolean value indicating the visibility of this Chart Legend. A value of True indicates that the legend is visible and a value of False indicates that it is hidden.
- `getMarkerVisibility() -> bool` — Returns a Boolean value indicating the visibility of the DataSeries markers on this Chart. A value of True indicates that the markers are visible and a value of False indicates that they are hidden.
- `getMaxMinMarkerVisibility() -> bool` — Boolean property indicating the visibility of Max/Min markers on this ChartPlotXY. A value of True indicates that the markers are displayed, False that they are hidden.
#### `getName() -> str`
Read-only string representing the name of this object.

Returns: this entity name (string)

getName() may also be accessed as an Entity property 'name'. For example:

#### `getPath() -> str`
return this Entity path string.

Returns: this entity path (string)

The Path string includes the parent name Hierarchy, including model name For example a Part path: MyModel/TopAssembly/LeftAssembly/

- `hideDataSeriesLabels() -> None` — Hides the labels on the DataSeries points. This method is silently ignored if the labels are already hidden.
- `hideDataSeriesMarkers() -> None` — Hides markers at each data point on every visible DataSeries. This method is silently ignored if the markers are already hidden.
- `hideLegend() -> None` — Hides the Legend for this Chart. This method is silently ignored if the Legend is already hidden.
- `hideMaxMinMarkers() -> None` — Hides the Max Min markers for this Chart. This method is silently ignored if the markers are already hidden.
- `removeDataSeries(dataSeries: apex.chart.DataSeries) -> None` — Removes a DataSeries from this Chart. If the DataSeries is does not exist in this Chart it will be silently ignored.
- `removeDataSeriesList(dataSeriesList: [apex.chart.DataSeries]) -> None` — Removes one ore more DataSeries from this chart. If any of the input DataSeries do not already exist within this Chart they will be silently ignored.Duplicate DataSeries within the input will be silently ignored.
- `setDataSeriesBehaviorAccumulate() -> None` — Causes all new DataSeries that are added to this Chart to be accumulated alongside any existing DataSeries. This method is silently ignored if the behavior is already set to accumulate. An alternative behavior can be invoked using setDataSeriesBehaviorReplace() method that causes all new DataSeries that are added to the Chart to replace any existing DataSeries. This method only affects the interactive behavior of the Chart. For scripting use cases use the <add/remove/toggle>DataSerires methods to achieve the desired behavior.
- `setDataSeriesBehaviorReplace() -> None` — Causes all new DataSeries that are added to this Chart to replace any existing DataSeries. This method is silently ignored if the behavior is already set to replace.
- `showDataSeriesLabels() -> None` — Displays the labels on the DataSeries points. This method is silently ignored if the labels are already visible.
- `showDataSeriesMarkers() -> None` — Displays markers at each data point on every visible DataSeries. This method is silently ignored if the markers are already visible.
- `showLegend() -> None` — Displays the Legend for this Chart. This method is silently ignored if the Legend is already visible.
- `showMaxMinMarkers() -> None` — Displays the Max Min markers for this Chart. This method is silently ignored if the markers are already visible.

## `apex.chart.DataSeries`  (extends `Entity`)
Class containing XY data pairs for use in Charts.
Properties: `description`, `name`, `xunit`, `xunitquantity`, `xvalues`, `ydata`, `yunit`, `yunitquantity`

Methods:

- `getDescription() -> str` — Returns the description for this DataSeries.
- `getName() -> str` — Returns the name for this DataSeries.
- `getXUnit() -> str` — Returns the string defining the unit (e.g., "m") for the x-axis data.
- `getXUnitQuantity() -> str` — Returns the string defining the type of unit quantity (e.g. "Length") for the x-data.
- `getXValues() -> [float]` — Returns the list of scalar values representing the x-axis data.
- `getYData() -> [float]` — Returns the list of scalar values representing the y-axis data.
- `getYUnit() -> str` — Returns the string defining the unit for the y-axis data.
- `getYUnitQuantity() -> str` — Returns the string defining the type of unit quantity for the y-data.

## `apex.chart.DataSeriesCollection`  (extends `EntityCollection`)

Methods:

- `DataSeriesCollection() -> None` — Construct a new DataSeriesCollection.

## `apex.chart.DataTable`  (extends `Entity`, `IName`)
Class to represent data with multiples independent and dependent variables.
Properties: `dependentVariables`, `independentVariables`

Methods:

#### `DataTable(name: str, description: str, independentVariables: {str:[str,str,float,...]}, dependentVariables: {str:[str,str,MatrixMN]}) -> None`
DataTable constructor.

- `name` — the name of DataTable.
- `description` — the description of DataTable.
- `independentVariables` — Dictionary to represent the independent variables, the max number of the member is 4, which means we allow to define 1-4 Independent variables. In each member, 1. the key is the name of independent variable 2. the values is a list which pack the one description(str), one unit(str) and one or more data(float). [str, str, float, float, etc] For example: {name 1:[str, str, float, float, etc],name 2:[str, str, float, float, etc]}
- `dependentVariables` — Dictionary to represent the dependent variables In each member, 1. the key is the name of dependent variable 2. the values is a list which pack the description, unit and m*n matrix data.

For example, Number of 1st independent variable = m Number of 2nd independent variable = n Number of 3rd independent variable = i Number of 4th independent variable = j matrixMN = [[Len=m], The column Len is m [Len=m], [ … ], [Len=m]] The row Len is n dependentVariables = [str,str,[matrixMN], The column Len is i [matrixMN], [… ], [matrixMN]] The column Len is j

- `getDependentVariables() -> {str:[str,str,MatrixMN]}` — Gets Dictionary to represent the dependent variables In each member, 1. the key is the name of dependent variable 2. the values is a list which pack the description, unit and m*n matrix data.
- `getIndependentVariables() -> {str:[str,str,float,...]}` — Gets Dictionary to represent the independent variables, the max number of the member is 4, which means we allow to define 1-4 Independent variables. In each member, 1. the key is the name of independent variable 2. the values is a list which pack the one description(str), one unit(str) and one or more data(float). [str, str, float, float, etc] For example: {name 1:[str, str, float, float, etc],name 2:[str, str, float, float, etc]}.
#### `update(name: str, description: str, independentVariables: {str:[str,str,float,...]}, dependentVariables: {str:[str,str,MatrixMN]}) -> DataTable`
update DataTable.

- `name` — the name of DataTable.
- `description` — the description of DataTable.
- `independentVariables` — Dictionary to represent the independent variables, the max number of the member is 4, which means we allow to define 1-4 Independent variables. In each member, 1. the key is the name of independent variable 2. the values is a list which pack the one description(str), one unit(str) and one or more data(float). [str, str, float, float, etc] For example: {name 1:[str, str, float, float, etc],name 2:[str, str, float, float, etc]}
- `dependentVariables` — Dictionary to represent the dependent variables In each member, 1. the key is the name of dependent variable 2. the values is a list which pack the description, unit and m*n matrix data.

For example, Number of 1st independent variable = m Number of 2nd independent variable = n Number of 3rd independent variable = i Number of 4th independent variable = j matrixMN = [[Len=m], The column Len is m [Len=m], [ … ], [Len=m]] The row Len is n dependentVariables = [str,str,[matrixMN], The column Len is i [matrixMN], [… ], [matrixMN]] The column Len is j


## `apex.chart.MatrixMN`  (extends `Entity`, `IName`)
Class to store m*n matrix data.
Properties: `matrix`

Methods:

#### `MatrixMN(matrixMN: [[],[],...,[]]) -> None`
MatrixMN constructor.

- `matrixMN` — List of lists with scalar values representing the m*n matrix data. m is representing the column and n is representing row.For example, Matrix =[[Dm1n1,Dm2n1,...,Dmmn1], [[Dm1n2,Dm2n2,...,Dmmn2], ... [[Dm1nn,Dm2nn,...,Dmmnn]]

- `getMatrix() -> [[],[],...,[]]` — Gets List of lists with scalar values representing the m*n matrix data. m is representing the column and n is representing row.For example, Matrix =[[Dm1n1,Dm2n1,...,Dmmn1], [[Dm1n2,Dm2n2,...,Dmmn2], ... [[Dm1nn,Dm2nn,...,Dmmnn]].
- `setMatrix(matrix: [[],[],...,[]]) -> None` — Sets List of lists with scalar values representing the m*n matrix data. m is representing the column and n is representing row.For example, Matrix =[[Dm1n1,Dm2n1,...,Dmmn1], [[Dm1n2,Dm2n2,...,Dmmn2], ... [[Dm1nn,Dm2nn,...,Dmmnn]].

## `apex.chart.TABLED1`  (extends `Table`)
a tabular function for use in generating frequency-dependent and time-dependent dynamic loads, Form 1
Properties: `xdata`, `xInterpolation`, `ydata`, `yInterpolation`

Methods:

- `getXInterpolation() -> apex.chart.Interpolation` — Specifies a linear or logarithmic interpolation for the x-axis.
- `getXdata() -> [float]` — List of scalar values representing the x-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `getYInterpolation() -> apex.chart.Interpolation` — Specifies a linear or logarithmic interpolation for the y-axis.
- `getYdata() -> [float]` — List of scalar values representing the y-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `setXInterpolation(xInterpolation: apex.chart.Interpolation) -> None` — Specifies a linear or logarithmic interpolation for the x-axis.
- `setXdata(xdata: [float]) -> None` — List of scalar values representing the x-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `setYInterpolation(yInterpolation: apex.chart.Interpolation) -> None` — Specifies a linear or logarithmic interpolation for the y-axis.
- `setYdata(ydata: [float]) -> None` — List of scalar values representing the y-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
#### `update(name: str, description: str, id: int, xInterpolation: apex.chart.Interpolation, yInterpolation: apex.chart.Interpolation, xdata: [float], ydata: [float]) -> None`
update TABLED1

- `name` — Update the name of this TABLED1
- `description` — Update the description of this TABLED1
- `id` — id of the table
- `xInterpolation` — Specifies a linear or logarithmic interpolation for the x-axis
- `yInterpolation` — Specifies a linear or logarithmic interpolation for the y-axis
- `xdata` — List of scalar values representing the x-axis data.
- `ydata` — List of scalar values representing the y-axis data.


## `apex.chart.TABLED2`  (extends `Table`)
a tabular function for use in generating frequency-dependent and time-dependent dynamic loads, Form 2
Properties: `x1`, `xdata`, `ydata`

Methods:

- `getX1() -> float` — Table parameter.
- `getXdata() -> [float]` — List of scalar values representing the x-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `getYdata() -> [float]` — List of scalar values representing the y-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `setX1(x1: float) -> None` — Table parameter.
- `setXdata(xdata: [float]) -> None` — List of scalar values representing the x-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `setYdata(ydata: [float]) -> None` — List of scalar values representing the y-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
#### `update(name: str, description: str, id: int, x1: float, xdata: [float], ydata: [float]) -> None`
update TABLED2

- `name` — Update the name of this TABLED2
- `description` — Update the description of this TABLED2
- `id` — id of the table
- `x1` — Table parameter
- `xdata` — List of scalar values representing the x-axis data.
- `ydata` — List of scalar values representing the y-axis data.


## `apex.chart.TABLED3`  (extends `Table`)
a tabular function for use in generating frequency-dependent and time-dependent dynamic loads, Form 3
Properties: `x1`, `x2`, `xdata`, `ydata`

Methods:

- `getX1() -> float` — Table parameter.
- `getX2() -> float` — Table parameter.
- `getXdata() -> [float]` — List of scalar values representing the x-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `getYdata() -> [float]` — List of scalar values representing the y-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `setX1(x1: float) -> None` — Table parameter.
- `setX2(x2: float) -> None` — Table parameter.
- `setXdata(xdata: [float]) -> None` — List of scalar values representing the x-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
- `setYdata(ydata: [float]) -> None` — List of scalar values representing the y-axis data. The X and Y data for each pair is stored in two separate Lists where the X and Y data for any given pairs shares the same index. xdata must contain the same number of values and be in the same order as ydata. When used in Charts, the data will be plotted in the order that it is found in these lists.
#### `update(name: str, description: str, id: int, x1: float, x2: float, xdata: [float], ydata: [float]) -> None`
update TABLED3

- `name` — Update the name of this TABLED3
- `description` — Update the description of this TABLED3
- `id` — id of the table
- `x1` — Table parameter
- `x2` — Table parameters
- `xdata` — List of scalar values representing the x-axis data.
- `ydata` — List of scalar values representing the y-axis data.


## `apex.chart.TABLED4`  (extends `Table`)
a tabular function for use in generating frequency-dependent and time-dependent dynamic loads, Form 4
Properties: `coefficients`, `x1`, `x2`, `x3`, `x4`

Methods:

- `getCoefficients() -> [float]` — List of scalar values representing the coefficients data.
- `getX1() -> float` — Table parameter.
- `getX2() -> float` — Table parameter.
- `getX3() -> float` — Table parameter.
- `getX4() -> float` — Table parameter.
- `setCoefficients(coefficients: [float]) -> None` — List of scalar values representing the coefficients data.
- `setX1(x1: float) -> None` — Table parameter.
- `setX2(x2: float) -> None` — Table parameter.
- `setX3(x3: float) -> None` — Table parameter.
- `setX4(x4: float) -> None` — Table parameter.
#### `update(name: str, description: str, id: int, x1: float, x2: float, x3: float, x4: float, coefficients: [float]) -> None`
update TABLED4

- `name` — Update the name of this TABLED4
- `description` — Update the description of this TABLED4
- `id` — id of the table
- `x1` — Table parameter
- `x2` — Table parameters
- `x3` — Table parameters
- `x4` — Update the x4 of this TABLED4
- `coefficients` — List of scalar values representing the coefficients data.


## `apex.chart.Table`  (extends `Entity`, `IUserAttributes`, `IName`)
Base Class to represent table data of Nastran.
Properties: `id`

Methods:

- `getId() -> int` — the id of the table.

