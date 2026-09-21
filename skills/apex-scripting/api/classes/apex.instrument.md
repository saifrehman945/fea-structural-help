# apex.instrument — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.instrument.ClearanceSensor`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IName`)
Class ClearanceSensor.
Properties: `maxDistance`, `modelAssociation`, `parts`, `useModelAssociation`

Methods:

- `getMaxDistance() -> float` — Gets maximum distance of clearance sensor. It is a read only value.
- `getModelAssociation() -> apex.ModelAssociation` — Gets optional argument to indicate the Model Association is used, it is needed ONLY when the argument of "useModelAssociation" is set as true.
- `getParts() -> apex.PartCollection` — Gets a list contains 2 parts between which the clearance sensor is created.
- `getUseModelAssociation() -> bool` — Gets optional argument to indicate if Model association is used.
#### `update(name: str, description: str) -> None`
update clearance sensor object.

- `name` — Optional name for the clearance sensor.
- `description` — Optional string providing a description for the clearance sensor.


## `apex.instrument.ClearanceSensorCollection`  (extends `EntityCollection`)
Iterable collection of ClearanceSensor, based on EntityCollection.

Methods:

- `ClearanceSensorCollection() -> None` — Construct a new ClearanceSensorCollection.

## `apex.instrument.XSectionForceSensor`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class XSectionForceSensor.
Properties: `location`, `orientation`, `sensorCentroidLocation`, `target`

Methods:

- `getLocation() -> apex.Coordinate` — Returns location of the XSectionForceSensor.
- `getOrientation() -> apex.Orientation` — Returns glef.Orientation of the XSectionForceSensor.
- `getSensorCentroidLocation() -> apex.instrument.SensorLocationMethod` — Returns apex.instrument.SensorLocationMethod of the XSectionForceSensor.
- `getTarget() -> apex.EntityCollection` — Returns select entities that the XSectionForceSensor is associated with.
#### `update(name: str, description: str, targetAll: bool, target: apex.EntityCollection, sensorCentroidLocation: apex.instrument.SensorLocationMethod, location: apex.ILocation, orientation: apex.construct.Orientation) -> None`
Update X-Section Force Sensor properties.

- `name` — Optional name for the Cross Section Force Sensor. If omitted a defaul name will be provided by the system using the prefix "X-Section Force Sensor" followed by the lowest integer required to ensure Cross Section Force Sensor name uniquenes within the Model. If a name is provided it must be unique across all Cross Section Force Sensors in the Model. If a non-unique name is provided it will be silently modified to ensure uniqueness.
- `description` — Optional description for the Cross Section Force Sensor. If omitted, the description will be left blank.
- `targetAll` — If True: all object intersected by the section plane will be used to create the Cross Section Force Sensor. If false: the targe arument must be specified.
- `target` — Collection of entitites selected for the creation of the Cross Section Force Sensor.
- `sensorCentroidLocation` — Enumeration defining where the origins of the sensors created by this method will be. The default apex.instrumentation.SensorLocationMethod.AtCentroid will cause the sensors to be created with their origins at the centroid of the shape definied by the intersection of the sensor plane and the target entities. The optional apex.instrumentation.SensorLocationMethod.OnPath will cause the sensors to be created with their origins located on the straight line between the two end points.
- `location` — The location of the Cross Section Force Sensor as an ILocation. The location is used as the point about which moments are summed.
- `orientation` — The orientation of the Cross Section Force Sensor relative to the global coordinate system.

Returns: the created XSectionForceSensor

Update one or more properties of XSectionForceSensor. Thie method allows multiple properties of the object to be pdated usin a single method call. All arguments are optional and the values of all object properties associated with the omitted arguments are left unchanged.


## `apex.instrument.XSectionForceSensorArray`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class XSectionForceSensorArray.
Properties: `sensors`

Methods:

#### `appendSensors(sensors: [apex.instrument.XSectionForceSensor]) -> [apex.instrument.XSectionForceSensor]`
Appends a List of XSectionForceSensors to this XSectionForceSensorArray.

- `sensors` — List of XSectionForceSensors to append to this XSectionForceSensorArray.

Returns: the ordered list of XSectionForceSensor in this XSectionForceSensorArray

Appends a List XSectionForceSensors to this XSectionForceSensorArray and returns an ordered List of all sensors in the array. If any of the input XSectionForceSensors are already included in this array they will be silently ignored.

- `getSensors() -> [apex.instrument.XSectionForceSensor]` — Returns sensors that the XSectionForceSensorArray contains.
#### `insertSensors(sensors: [apex.instrument.XSectionForceSensor], index: int) -> [apex.instrument.XSectionForceSensor]`
Inserts a List of XSectionForceSensors into this XSectionForceSensorArray at a specified index.

- `sensors` — List of XSectionForceSensors to be inserted into this XSectionForceSensorArray.
- `index` — Index into the array of XSectionForceSensors in this XSectionForceSensorArray where the input sensors will be inserted. The order of the sensor that are being inserted will be retained after insertion. The first sensor in the inserted list will be positioned at this index with all other inserted sensors being added at sequenctial indices. Any existing sensors that were originally located at or above the index will be shifted toward the end of the array by the number of inserted sensors.

Returns: the ordered list of XSectionForceSensor in this XSectionForceSensorArray

The input XSectionForceSensors will be inserted into this XSectionForceSensorArray at the index provided and will cause any existing sensors at that index and above to be offset. and returns an ordered List of all sensors in the array.

#### `removeSensors(sensors: [apex.instrument.XSectionForceSensor]) -> [apex.instrument.XSectionForceSensor]`
Remove XSectionForceSensors from this XSectionForceSensorArray.

- `sensors` — List of XSectionForceSensors to remove from this XSectionForceSensorArray.

Returns: the ordered list of XSectionForceSensor in this XSectionForceSensorArray

Input XSectionForceSensors that are not referenced by this array will be silently ignored.

#### `update(name: str) -> None`
Update X-Section Force Sensor properties.

- `name` — Optional name for the Cross Section Force Sensor. If omitted a defaul name will be provided by the system using the prefix "X-Section Force Sensor" followed by the lowest integer required to ensure Cross Section Force Sensor name uniquenes within the Model. If a name is provided it must be unique across all Cross Section Force Sensors in the Model. If a non-unique name is provided it will be silently modified to ensure uniqueness.

Returns: the created XSectionForceSensor

Update one or more properties of XSectionForceSensor. Thie method allows multiple properties of the object to be pdated usin a single method call. All arguments are optional and the values of all object properties associated with the omitted arguments are left unchanged.


## `apex.instrument.XSectionForceSensorArrayCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `XSectionForceSensorArrayCollection() -> None` — Construct a new XSectionForceSensorArrayCollection.

## `apex.instrument.XSectionForceSensorCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `XSectionForceSensorCollection() -> None` — Construct a new XSectionForceSensorCollection.

