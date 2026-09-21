# apex.chart

(apex.chart module) Charting functions used to visualize XY-Chart data.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.chart.Interpolation`: `Linear`, `Log`
  - Of a linear or logarithmic interpolation

## Module functions

### `apex.chart.createChartPlotXY(name: str, description: str = "") -> ChartPlotXY`
Creates and returns an empty ChartPlotXY object. The returned ChartPlotXY is empty on creation and must be populated with DataSeries before it can display anything useful.

- `name` — The Scenario Event will be initially used to create ChartPlotXY.
- `description` — The Scenario Event will be initially used to create ChartPlotXY.

### `apex.chart.createTABLED1(name: str, description: str, id: int, xInterpolation: apex.chart.Interpolation, yInterpolation: apex.chart.Interpolation, xdata: [float], ydata: [float]) -> TABLED1`
create TABLED1

- `name` — The name of this TABLED1
- `description` — The description of this TABLED1
- `id` — id of the table
- `xInterpolation` — Specifies a linear or logarithmic interpolation for the x-axis
- `yInterpolation` — Specifies a linear or logarithmic interpolation for the y-axis
- `xdata` — List of scalar values representing the x-axis data.
- `ydata` — List of scalar values representing the y-axis data.

### `apex.chart.createTABLED2(name: str, description: str, id: int, x1: float, xdata: [float], ydata: [float]) -> TABLED2`
create TABLED2

- `name` — The name of this TABLED2
- `description` — The description of this TABLED2
- `id` — id of the table
- `x1` — Table parameter
- `xdata` — List of scalar values representing the x-axis data.
- `ydata` — List of scalar values representing the y-axis data.

### `apex.chart.createTABLED3(name: str, description: str, id: int, x1: float, x2: float, xdata: [float], ydata: [float]) -> TABLED3`
create TABLED3

- `name` — The name of this TABLED3
- `description` — The description of this TABLED3
- `id` — id of the table
- `x1` — Table parameter
- `x2` — Table parameter
- `xdata` — List of scalar values representing the x-axis data.
- `ydata` — List of scalar values representing the y-axis data.

### `apex.chart.createTABLED4(name: str, description: str, id: int, x1: float, x2: float, x3: float, x4: float, coefficients: [float]) -> TABLED4`
create TABLED4

- `name` — The name of this TABLED4
- `description` — The description of this TABLED4
- `id` — id of the table
- `x1` — Table parameter
- `x2` — Table parameter
- `x3` — Table parameter
- `x4` — Table parameter
- `coefficients` — List of scalar values representing the coefficients data.

### `apex.chart.getChartPlotXY(name: str) -> ChartPlotXY`
returns ChartPlotXY object by the input ChartPlotXY name.

- `name` — the name of the ChartPlotXY.

### `apex.chart.getCurrentChartPlotXY() -> ChartPlotXY`
returns current ChartPlotXY object.

### `apex.chart.getTABLED1(name: str = "#####") -> TABLED1`

- `name` — The name of the TABLED1

### `apex.chart.getTABLED1s() -> apex.EntityCollection`

### `apex.chart.getTABLED2(name: str = "#####") -> TABLED2`

- `name` — The name of the TABLED2

### `apex.chart.getTABLED2s() -> apex.EntityCollection`

### `apex.chart.getTABLED3(name: str = "#####") -> TABLED3`

- `name` — The name of the TABLED3

### `apex.chart.getTABLED3s() -> apex.EntityCollection`

### `apex.chart.getTABLED4(name: str = "#####") -> TABLED4`

- `name` — The name of the TABLED4

### `apex.chart.getTABLED4s() -> apex.EntityCollection`

### `apex.chart.getTable(name: str) -> apex.chart.Table`
Get a specified Table by name.

- `name` — The name of the table.

### `apex.chart.getTables() -> apex.EntityCollection`
Get all Tables.

### `apex.chart.getTables(type: str) -> apex.EntityCollection`

## Classes in this module

Full method signatures are in `api/classes/apex.chart.md`.

`ChartPlotXY`, `DataSeries`, `DataSeriesCollection`, `DataTable`, `MatrixMN`, `TABLED1`, `TABLED2`, `TABLED3`, `TABLED4`, `Table`

