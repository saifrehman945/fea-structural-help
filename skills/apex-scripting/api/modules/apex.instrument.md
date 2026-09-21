# apex.instrument

(apex.instrument module) model Attribute attribute.PointSensor creation functions.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.instrument.SensorLocationMethod`: `AtCentroid`, `OnPath`
  - Possible SensorLocationMethod options in Apex. Specify SensorLocationMethod by using the syntax apex.instrument.SensorLocationMethod."<enum_value>" For example: apex.instrument.SensorLocationMethod.AtCentroid

## Module functions

### `apex.instrument.createClearanceSensors(name: str, description: str, useModelAssociation: bool, modelAssociation: apex.ModelAssociation, maxDistance: float, parts: apex.PartCollection) -> apex.instrument.ClearanceSensorCollection`
create clearance sensor objects between the selected parts.

- `name` — Optional name for the clearance sensor.
- `description` — Optional description of clearance sensor.
- `useModelAssociation` — optional argument to indicate if Model association is used.
- `modelAssociation` — optional argument to indicate the Model Association is used, it is needed ONLY when the argument of "useModelAssociation" is set as true.
- `maxDistance` — maximum distance of clearance sensor.
- `parts` — a list contains parts between which the clearance sensors are created.

### `apex.instrument.createPointSensor(name: str, target: apex.EntityCollection, activateChannelMask: [bool], orientation: apex.construct.Orientation = None, description: str = "") -> apex.attribute.PointSensor`
Create a new PointSensor.

- `name` — of the PointSensor. default = "" (auto-named)
- `target` — entities.
- `activateChannelMask` — of the PointSensor.
- `orientation` — Optional - the orientation relative to the global coordinate system.
- `description` — Optional - the description.

Returns: the created Point Sensor

### `apex.instrument.createXSectionForceSensor(name: str, description: str = "", targetAll: bool = False, target: apex.EntityCollection = None, sensorCentroidLocation: apex.instrument.SensorLocationMethod = apex.instrument.SensorLocationMethod.AtCentroid, location: apex.ILocation = None, orientation: apex.construct.Orientation = None) -> apex.instrument.XSectionForceSensor`
Creates a Cross Section Force Sensor.

- `name` — Optional name for the Cross Section Force Sensor. If omitted a default name will be provided by the system using the prefix "X-Section Force Sensor" followed by the lowest integer required to ensure Cross Section Force Sensor name uniquenes within the Model. If a name is provided it must be unique across all Cross Section Force Sensors in the Model. If a non-unique name is provided it will be silently modified to ensure uniqueness.
- `description` — Optional description for the Cross Section Force Sensor. If omitted, the description will be left blank.
- `targetAll` — If True: all objects intersected by the section plane will be used to create the Cross Section Force Sensor. If false: the target argument must be specified.
- `target` — Collection of entities selected for the creation of the Cross Section Force Sensor.
- `sensorCentroidLocation` — Enumeration defining where the origins of the sensors created by this method will be. The default apex.instrumentation.SensorLocationMethod.AtCentroid will cause the sensors to be created with their origins at the centroid of the shape definied by the intersection of the sensor plane and the target entities. The optional apex.instrumentation.SensorLocationMethod.OnPath will cause the sensors to be created with their origins located on the straight line between the two end points.
- `location` — The location of the Cross Section Force Sensor as an ILocation. The location is used as the point about which moments are summed.
- `orientation` — The orientation of the Cross Section Force Sensor relative to the global coordinate system.

Returns: the created XSectionForceSensor

### `apex.instrument.createXSectionForceSensorArrayBetweenEndpoints(name: str, description: str = "", targetAll: bool = False, target: apex.EntityCollection = None, startLocation: apex.ILocation = None, endLocation: apex.ILocation = None, numberOfSensors: int = 5, sensorCentroidLocation: apex.instrument.SensorLocationMethod = apex.instrument.SensorLocationMethod.AtCentroid, sensorXAxis: apex.construct.Vector3D = apex.construct.Vector3D(), sensorYAxis: apex.construct.Vector3D = apex.construct.Vector3D()) -> apex.instrument.XSectionForceSensorArray`
Creates a Cross Section Force Sensor Array, two or more XSectionForceSensors evenly spaced between the two end points and adds the sensors to the array.

- `name` — The name of this XSectionForceSensorArray
- `description` — Optional description for this XSectionForceSensorArray. If omitted, the description will be left blank.
- `targetAll` — If True: all object intersected by the section plane will be used to create the Cross Section Force Sensor. If false: the targe arument must be specified.
- `target` — Collection of entitites selected for the creation of the Cross Section Force Sensor.
- `startLocation` — The start location of the Cross Section Force Sensor Array
- `endLocation` — The end location of the Cross Section Force Sensor Array
- `numberOfSensors` — The total number of sensors to be created at each end point. Values higher that 2 will cause additional sensors to be created, evenly spaced between the two end point sensors.
- `sensorCentroidLocation` — Enumeration defining where the origins of the sensors created by this method will be. The default apex.instrumentation.SensorLocationMethod.AtCentroid will cause the sensors to be created with their origins at the centroid of the shape definied by the intersection of the sensor plane and the target entities. The optional apex.instrumentation.SensorLocationMethod.OnPath will cause the sensors to be created with their origins located on the straight line between the two end points.
- `sensorXAxis` — The direction of the X axis of the sensors as a Vector 3D. All sensors created by this method will be created with their Z axes aligned parallel to a vector defined by the end points of the path. This argument defines the direction of the sensor X axis. If the vector provided here is not orthogonal to the vector defined by the two end points of the path, it will be projected onto a plane that is perpendicular to the path and the projeted vector will define the X axes of all sensors created by this method. sensorXAxis is an optional argument and maybe omitted if sensorYAxis is defined, however at least one of the X or Y axes must be provided or the method will raise an exception. If both sensorXAxis and sensorYAxis are defined, only sensorXAxis will be used since the sensorYAxis can be uniquely determined for the X and Z axes.
- `sensorYAxis` — The direction of the Y axis of the sensors as a Vector 3D. All sensors created by this method will be created with their Z axes aligned parallel to a vector defined by the end points of the path. This argument defines the direction of the sensor Y axis. If the vector provided here is not orthogonal to the vector defined by the two end points of the path, it will be projected onto a plane that is perpendicular to the path and the projeted vector will define the Y axes of all sensors created by this method. sensorYAxis is an optional argument and maybe omitted if sensorXAxis is defined, however at least one of the X or Y axes must be provided or the method will raise an exception. If both sensorXAxis and sensorYAxis are defined, only sensorXAxis will be used since the sensorYAxis can be uniquely determined for the X and Z axes.

Returns: the created XSectionForceSensorArray

### `apex.instrument.getClearanceSensor(name: str) -> apex.instrument.ClearanceSensor`
retrieve the clearance sensor by name.

- `name` — The name of clearance sensor.

### `apex.instrument.getClearanceSensors() -> apex.instrument.ClearanceSensorCollection`
retrieve all clearance sensors in the model.

Returns: a ClearanceSensorCollection

### `apex.instrument.getPointSensor(pathName: str) -> apex.attribute.PointSensor`
Get a PointSensor.

- `pathName` — of the PointSensor.

### `apex.instrument.getPointSensors(target: [{str:str}]) -> apex.attribute.PointSensorCollection`
Get a collection of PointSensors, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the sensors to retrieve. Valid keys are 'path' and 'name'.

Returns: a PointSensorCollection of the requested PointSensors

### `apex.instrument.getSensors() -> apex.EntityCollection`
Get all sensors including X Section Sensor and Sensor Array.

### `apex.instrument.getXSectionForceSensor(name: str) -> apex.instrument.XSectionForceSensor`
Get a XSectionForceSensor.

- `name` — of XSectionForceSensor.

### `apex.instrument.getXSectionForceSensorArray(name: str) -> apex.instrument.XSectionForceSensorArray`
Get a XSectionForceSensorArray.

- `name` — of XSectionForceSensorArray.

### `apex.instrument.getXSectionForceSensorArrays(target: [{str:str}]) -> apex.instrument.XSectionForceSensorArrayCollection`
Get a collection of XSectionForceSensors, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the sensors to retrieve. Valid keys are 'path' and 'name'.

Returns: a XSectionForceSensorCollection of the requested XSectionForceSensors

### `apex.instrument.getXSectionForceSensors(target: [{str:str}]) -> apex.instrument.XSectionForceSensorCollection`
Get a collection of XSectionForceSensors, specified by target of key:value string dictionaries.

- `target` — of dictionaries (string:string) specifying the sensors to retrieve. Valid keys are 'path' and 'name'.

Returns: a XSectionForceSensorCollection of the requested XSectionForceSensors

## Classes in this module

Full method signatures are in `api/classes/apex.instrument.md`.

`ClearanceSensor`, `ClearanceSensorCollection`, `XSectionForceSensor`, `XSectionForceSensorArray`, `XSectionForceSensorArrayCollection`, `XSectionForceSensorCollection`

