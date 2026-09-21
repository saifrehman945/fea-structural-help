# apex.attribute — classes

Properties are read via `obj.prop` or `obj.getProp()`. Entity-derived
classes have no setters: change them with `obj.update(...)`.

## `apex.attribute.BeamShape`  (extends `Entity`, `IDisplayable`, `IUserAttributes`, `IName`)
Class BeamShape.
Properties: `beamShapeArea`, `beamShapeAreaMomentAxis1`, `beamShapeAreaMomentAxis2`, `beamShapeProductAreaMoment`, `beamShapeTorsionalConstant`, `principalAxes`

Methods:

- `asBeamShape1DProfile() -> BeamShape1DProfile` — cast to BeamShape1DProfile type
- `asBeamShapeC() -> BeamShapeC` — cast to BeamShapeC type
- `asBeamShapeCAlternate() -> BeamShapeCAlternate` — cast to BeamShapeCAlternate type
- `asBeamShapeCruciform() -> BeamShapeCruciform` — cast to BeamShapeCruciform type
- `asBeamShapeH() -> BeamShapeH` — cast to BeamShapeH type
- `asBeamShapeHat() -> apex.attribute.BeamShapeHat` — cast to BeamShapeHat type
- `asBeamShapeHatClosed() -> BeamShapeHatClosed` — cast to BeamShapeHatClosed type
- `asBeamShapeHollowDoubleRectangular() -> apex.attribute.BeamShapeHollowDoubleRectangular` — cast to BeamShapeHollowDoubleRectangular type
- `asBeamShapeHollowRectangularAsymmetric() -> apex.attribute.BeamShapeHollowRectangularAsymmetric` — cast to BeamShapeHollowRectangularAsymmetric type
- `asBeamShapeHollowRectangularSymmetric() -> apex.attribute.BeamShapeHollowRectangularSymmetric` — cast to BeamShapeHollowRectangularSymmetric type
- `asBeamShapeHollowRound() -> apex.attribute.BeamShapeHollowRound` — cast to BeamShapeHollowRound type
- `asBeamShapeHollowRoundByThickness() -> apex.attribute.BeamShapeHollowRoundByThickness` — cast to BeamShapeHollowRoundByThickness type
- `asBeamShapeIAsymmetric() -> BeamShapeIAsymmetric` — cast to BeamShapeIAsymmetric type
- `asBeamShapeISymmetric() -> BeamShapeISymmetric` — cast to BeamShapeISymmetric type
- `asBeamShapeL() -> BeamShapeL` — cast to BeamShapeL type
- `asBeamShapeNumeric() -> BeamShapeNumeric` — cast to BeamShapeNumeric type
- `asBeamShapeSolidHexagon() -> apex.attribute.BeamShapeSolidHexagon` — cast to BeamShapeSolidHexagon type
- `asBeamShapeSolidRectangle() -> apex.attribute.BeamShapeSolidRectangle` — cast to BeamShapeSolidRectangle type
- `asBeamShapeSolidRound() -> apex.attribute.BeamShapeSolidRound` — cast to BeamShapeSolidRound type
- `asBeamShapeT() -> BeamShapeT` — cast to BeamShapeT type
- `asBeamShapeTInverted() -> BeamShapeTInverted` — cast to BeamShapeTInverted type
- `asBeamShapeTSideways() -> BeamShapeTSideways` — cast to BeamShapeTSideways type
- `asBeamShapeU() -> BeamShapeU` — cast to BeamShapeU type
- `asBeamShapeZ() -> BeamShapeZ` — cast to BeamShapeZ type
- `getBeamShapeArea() -> float`
- `getBeamShapeAreaMomentAxis1() -> float`
- `getBeamShapeAreaMomentAxis2() -> float`
- `getBeamShapeProductAreaMoment() -> float`
- `getBeamShapeTorsionalConstant() -> float`
- `getCentroid() -> apex.construct.Point2D`
- `getPrincipalAxes() -> float`
- `getShearCenter() -> apex.construct.Point2D`
#### `update(name: str, description: str) -> None`
Update this Beam Shape properties.

- `name` — of this Beam Shape
- `description` — of this Beam Shape

One or more properties may be updated in each call to update().


## `apex.attribute.BeamShape1DProfile`  (extends `BeamShape`)
Properties: `profile`, `segmentThicknesses`

Methods:

- `getProfile() -> apex.construct.Profile1D`
- `getSegmentThicknesses() -> [float]`
- `update(name: str, profile: apex.construct.Profile1D, segmentThicknesses: {int:float}) -> None`

## `apex.attribute.BeamShapeC`  (extends `BeamShape`)
Properties: `flangeThickness`, `overallHeight`, `overallWidth`, `webThickness`

Methods:

- `getFlangeThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, webThickness: float, flangeThickness: float) -> None`

## `apex.attribute.BeamShapeCAlternate`  (extends `BeamShape`)
Properties: `flangeLength`, `flangeSeparation`, `overallHeight`, `webThickness`

Methods:

- `getFlangeLength() -> float`
- `getFlangeSeparation() -> float`
- `getOverallHeight() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, flangeLength: float, webThickness: float, flangeSeparation: float, overallHeight: float) -> None`

## `apex.attribute.BeamShapeCollection`  (extends `EntityCollection`)

Methods:

- `BeamShapeCollection() -> None` — Construct a new BeamShapeCollection.

## `apex.attribute.BeamShapeCruciform`  (extends `BeamShape`)
Properties: `horizontalSparExtension`, `horizontalSparWidth`, `overallHeight`, `verticalSparExtension`

Methods:

- `getHorizontalSparExtension() -> float`
- `getHorizontalSparWidth() -> float`
- `getOverallHeight() -> float`
- `getVerticalSparExtension() -> float`
- `update(name: str, description: str, horizontalSparExtension: float, verticalSparExtension: float, overallHeight: float, horizontalSparWidth: float) -> None`

## `apex.attribute.BeamShapeFactory`

## `apex.attribute.BeamShapeH`  (extends `BeamShape`)
Properties: `flangeSeparation`, `flangeThickness`, `overallHeight`, `webThickness`

Methods:

- `getFlangeSeparation() -> float`
- `getFlangeThickness() -> float`
- `getOverallHeight() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, flangeSeparation: float, flangeThickness: float, overallHeight: float, webThickness: float) -> None`

## `apex.attribute.BeamShapeHat`  (extends `BeamShape`)
Properties: `flangeWidth`, `hatWidth`, `height`, `thickness`

Methods:

- `getFlangeWidth() -> float`
- `getHatWidth() -> float`
- `getHeight() -> float`
- `getThickness() -> float`
- `update(name: str, description: str, height: float, thickness: float, hatWidth: float, flangeWidth: float) -> None`

## `apex.attribute.BeamShapeHatClosed`  (extends `BeamShape`)
Properties: `hatThickness`, `hatWidth`, `headThickness`, `overallHeight`, `overallWidth`

Methods:

- `getHatThickness() -> float`
- `getHatWidth() -> float`
- `getHeadThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, hatWidth: float, hatThickness: float, headThickness: float) -> None`

## `apex.attribute.BeamShapeHollowDoubleRectangular`  (extends `BeamShape`)
Properties: `bottomLeftWallThickness`, `bottomRightWallThickness`, `leftWallThickness`, `overallHeight`, `overallWidth`, `rightWallThickness`, `topLeftWallThickness`, `topRightWallThickness`, `webOffset`, `webThickness`

Methods:

- `getBottomLeftWallThickness() -> float`
- `getBottomRightWallThickness() -> float`
- `getLeftWallThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getRightWallThickness() -> float`
- `getTopLeftWallThickness() -> float`
- `getTopRightWallThickness() -> float`
- `getWebOffset() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, webOffset: float, leftWallThickness: float, webThickness: float, rightWallThickness: float, topLeftWallThickness: float, bottomLeftWallThickness: float, topRightWallThickness: float, bottomRightWallThickness: float) -> None`

## `apex.attribute.BeamShapeHollowRectangularAsymmetric`  (extends `BeamShape`)
Properties: `ceilingThickness`, `floorThickness`, `leftSideThickness`, `overallHeight`, `overallWidth`, `rightSideThickness`

Methods:

- `getCeilingThickness() -> float`
- `getFloorThickness() -> float`
- `getLeftSideThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getRightSideThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, ceilingThickness: float, floorThickness: float, rightSideThickness: float, leftSideThickness: float) -> None`

## `apex.attribute.BeamShapeHollowRectangularSymmetric`  (extends `BeamShape`)
Properties: `floorCeilingThickness`, `overallHeight`, `overallWidth`, `sideWallThickness`

Methods:

- `getFloorCeilingThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getSideWallThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, floorCeilingThickness: float, sideWallThickness: float) -> None`

## `apex.attribute.BeamShapeHollowRound`  (extends `BeamShape`)
Properties: `innerRadius`, `outerRadius`

Methods:

- `getInnerRadius() -> float`
- `getOuterRadius() -> float`
- `update(name: str, description: str, outerRadius: float, innerRadius: float) -> None`

## `apex.attribute.BeamShapeHollowRoundByThickness`  (extends `BeamShape`)
Properties: `outerRadius`, `thickness`

Methods:

- `getOuterRadius() -> float`
- `getThickness() -> float`
- `update(name: str, description: str, outerRadius: float, thickness: float) -> None`

## `apex.attribute.BeamShapeIAsymmetric`  (extends `BeamShape`)
Properties: `bottomFlangeThickness`, `bottomFlangeWidth`, `overallHeight`, `topFlangeThickness`, `topFlangeWidth`, `webThickness`

Methods:

- `getBottomFlangeThickness() -> float`
- `getBottomFlangeWidth() -> float`
- `getOverallHeight() -> float`
- `getTopFlangeThickness() -> float`
- `getTopFlangeWidth() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, overallHeight: float, bottomFlangeWidth: float, topFlangeWidth: float, webThickness: float, bottomFlangeThickness: float, topFlangeThickness: float) -> None`

## `apex.attribute.BeamShapeISymmetric`  (extends `BeamShape`)
Properties: `flangeExtension`, `flangeSeparation`, `overallHeight`, `webThickness`

Methods:

- `getFlangeExtension() -> float`
- `getFlangeSeparation() -> float`
- `getOverallHeight() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, flangeExtension: float, webThickness: float, flangeSeparation: float, overallHeight: float) -> None`

## `apex.attribute.BeamShapeL`  (extends `BeamShape`)
Properties: `horizontalLegThickness`, `overallHeight`, `overallWidth`, `verticalLegThickness`

Methods:

- `getHorizontalLegThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getVerticalLegThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, horizontalLegThickness: float, verticalLegThickness: float) -> None`

## `apex.attribute.BeamShapeNumeric`  (extends `BeamShape`)
Properties: `areaCrossSection`, `areaMomentOfInertia_I11`, `areaMomentOfInertia_I22`, `areaProductOfInertia_I12`, `beamBehaviorType`, `shearCenterLocation`, `shearStiffnessFactor_K1`, `shearStiffnessFactor_K2`, `stressRecoveryPoints`, `torsionalStiffness`, `torsionalStressCoefficient`

Methods:

- `getAreaCrossSection() -> float`
- `getAreaMomentOfInertia_I11() -> float`
- `getAreaMomentOfInertia_I22() -> float`
- `getAreaProductOfInertia_I12() -> float`
- `getBeamBehaviorType() -> apex.attribute.BeamBehaviorType`
- `getShearCenterLocation() -> apex.construct.Point2D`
- `getShearStiffnessFactor_K1() -> float`
- `getShearStiffnessFactor_K2() -> float`
- `getStressRecoveryPoints() -> [apex.construct.Point2D]`
- `getTorsionalStiffness() -> float`
- `getTorsionalStressCoefficient() -> float`
- `update(name: str, beamBehaviorType: apex.attribute.BeamBehaviorType, areaCrossSection: float, areaMomentOfInertia_I11: float, areaMomentOfInertia_I22: float, areaProductOfInertia_I12: float, torsionalStiffness: float, torsionalStressCoefficient: float, shearCenterLocation: apex.construct.Point2D, neutralAxisOffset_1: float, neutralAxisOffset_2: float, shearStiffnessFactor_K1: float, shearStiffnessFactor_K2: float, stressRecoveryLocations: [apex.construct.Point2D]) -> None`

## `apex.attribute.BeamShapeProperty`  (extends `Entity`)

Methods:

- `add(propName: str, propValue: float) -> None`
- `get(properties: [( str,float )]) -> None`

## `apex.attribute.BeamShapeSolidHexagon`  (extends `BeamShape`)
Properties: `height`, `offset`, `width`

Methods:

- `getHeight() -> float`
- `getOffset() -> float`
- `getWidth() -> float`
- `update(name: str, description: str, offset: float, width: float, height: float) -> None`

## `apex.attribute.BeamShapeSolidRectangle`  (extends `BeamShape`)
Properties: `height`, `width`

Methods:

- `getHeight() -> float`
- `getWidth() -> float`
- `update(name: str, description: str, width: float, height: float) -> None`

## `apex.attribute.BeamShapeSolidRound`  (extends `BeamShape`)
Properties: `radius`

Methods:

- `getRadius() -> float`
- `update(name: str, description: str, radius: float) -> None`

## `apex.attribute.BeamShapeT`  (extends `BeamShape`)
Properties: `baseThickness`, `overallHeight`, `overallWidth`, `sparThickness`

Methods:

- `getBaseThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getSparThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, baseThickness: float, sparThickness: float) -> None`

## `apex.attribute.BeamShapeTInverted`  (extends `BeamShape`)
Properties: `baseThickness`, `overallHeight`, `overallWidth`, `sparThickness`

Methods:

- `getBaseThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getSparThickness() -> float`
- `update(name: str, description: str, overallWidth: float, overallHeight: float, baseThickness: float, sparThickness: float) -> None`

## `apex.attribute.BeamShapeTSideways`  (extends `BeamShape`)
Properties: `baseThickness`, `overallHeight`, `sparLength`, `sparThickness`

Methods:

- `getBaseThickness() -> float`
- `getOverallHeight() -> float`
- `getSparLength() -> float`
- `getSparThickness() -> float`
- `update(name: str, description: str, overallHeight: float, sparLength: float, baseThickness: float, sparThickness: float) -> None`

## `apex.attribute.BeamShapeU`  (extends `BeamShape`)
Properties: `flangeThickness`, `overallHeight`, `overallWidth`, `webThickness`

Methods:

- `getFlangeThickness() -> float`
- `getOverallHeight() -> float`
- `getOverallWidth() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, flangeThickness: float, webThickness: float, overallHeight: float, overallWidth: float) -> None`

## `apex.attribute.BeamShapeZ`  (extends `BeamShape`)
Properties: `flangeExtension`, `flangeSeparation`, `overallHeight`, `webThickness`

Methods:

- `getFlangeExtension() -> float`
- `getFlangeSeparation() -> float`
- `getOverallHeight() -> float`
- `getWebThickness() -> float`
- `update(name: str, description: str, flangeExtension: float, webThickness: float, flangeSeparation: float, overallHeight: float) -> None`

## `apex.attribute.BeamSpan`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class BeamSpan.
Properties: `beamSpanType`, `beamTarget`, `distributionType`, `fieldOffset1`, `fieldOffset2`, `fieldVector`, `material`, `plateSide`, `plateTarget`, `references`, `shapeBoundaryDistanceA`, `shapeBoundaryDistanceB`, `shapeEndADirection1`, `shapeEndADirection2`, `shapeEndAOffsetGlobal`, `shapeEndAShearCenterOffsetGlobal`, `shapeEndBDirection1`, `shapeEndBDirection2`, `shapeEndBOffsetGlobal`, `shapeEndBShearCenterOffsetGlobal`, `shapeMatingDirection`, `spanOrientationA`, `spanOrientationB`, `stationAOrientation`, `stationAShape`, `stationAXoffset`, `stationAYOffset`, `stationBOrientation`, `stationBShape`, `stationBXoffset`, `stationBYOffset`

Methods:

- `getBeamShapeSide() -> apex.attribute.ShapeMatingSide` — Returns the BeamShape side that touches the stiffened plate.
- `getBeamSpanType() -> apex.attribute.BeamSpanType` — Returns BeamSpanType of the BeamSpan.
- `getBeamTarget() -> apex.geometry.EdgeCollection` — Read only property that returns the apex.geometry.EdgeCollection that the BeamSpan is assigned to.
- `getDistributionType() -> str`
- `getFieldOffset1() -> {str:[]}` — Field of offset from end A to end B in the "1" direction, the data type is one dictionary.
- `getFieldOffset2() -> {str:[]}` — Field of offset from end A to end B in the "2" direction, the data type is one dictionary.
- `getFieldVector() -> {str:[]}` — Field of vectors is used to define the orientation, the data type is one dictionary.
- `getMaterial() -> apex.attribute.Material` — Returns the referenced Material object by the BeamSpan.
- `getPathEdge() -> apex.geometry.EdgeCollection` — DEPRECATED: THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. This method has been superseded by the equivalent "BeamSpan.getBeamTarget()/beamTarget method/property Returns the apex.geometry.EdgeCollection that the BeamSpan is assigned to.
- `getPlateFace() -> apex.geometry.FaceCollection` — DEPRECATED: THIS METHOD IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. This method has been superseded by the equivalent "BeamSpan.getPlatTarget()/platTarget method/property Returns the apex.geometry.FaceCollection of the stiffened plates of the BeamSpan.
- `getPlateSide() -> apex.attribute.TopBottom` — Returns the side of the stiffened plate that is touched by the beam span.
- `getPlateTarget() -> apex.geometry.FaceCollection` — Read only property that returns the apex.geometry.FaceCollection that the BeamSpan is associated with.
- `getReferences() -> apex.EntityCollection` — returns a collection of all entities that this BeamSpan directly references
- `getShapeBoundaryDistanceA() -> float` — Returns boundary distance of shape A of the BeamSpan.
- `getShapeBoundaryDistanceB() -> float` — Returns boundary distance of shape B of the BeamSpan.
- `getShapeEndADirection1() -> apex.construct.Vector3D` — Returns the direction of the "1" axis of the "End A" BeamShape as a Vector3D.
- `getShapeEndADirection2() -> apex.construct.Vector3D` — Returns the direction of the "2" axis of the "End A" BeamShape as a Vector3D.
- `getShapeEndAOffsetGlobal() -> apex.construct.Vector3D` — Returns the offset, in 3D space, of the origin of the BeamShape relative to the BeamSpan at end 'A' of the span. The offset is returned in a vector3D object with respect to the global coordinate system and represents a distance therefore units of length must be used when defining or interpreting this value.
- `getShapeEndAShearCenterOffsetGlobal() -> apex.construct.Vector3D` — Returnsthe offset, in 3D space, of the shear center of the BeamShape relative to the BeamSpan at end 'A' of the span. This offset is not available if the BeamSpan is defined using BeamShapeProfile1D beam shapes The offset is returned in a vector3D object and represents a distance therefore units of length must be used when defining or interpreting this value.
- `getShapeEndBDirection1() -> apex.construct.Vector3D` — Returns the direction of the "1" axis of the "End B" BeamShape as a Vector3D.
- `getShapeEndBDirection2() -> apex.construct.Vector3D` — Returns the direction of the "2" axis of the "End B" BeamShape as a Vector3D.
- `getShapeEndBOffsetGlobal() -> apex.construct.Vector3D` — Returns the offset, in 3D space, of the origin of the BeamShape relative to the BeamSpan at end 'B' of the span. The offset is returned in a vector3D object with respect to the global coordinate system and represents a distance therefore units of length must be used when defining or interpreting this value.
- `getShapeEndBShearCenterOffsetGlobal() -> apex.construct.Vector3D` — Returnsthe offset, in 3D space, of the shear center of the BeamShape relative to the BeamSpan at end 'B' of the span. This offset is not available if the BeamSpan is defined using BeamShapeProfile1D beam shapes The offset is returned in a vector3D object and represents a distance therefore units of length must be used when defining or interpreting this value.
- `getSpanOrientationA() -> apex.construct.Orientation`
- `getSpanOrientationB() -> apex.construct.Orientation`
- `getStationAOrientation() -> float` — Returns Station A shape orientation of the BeamSpan.
- `getStationAShape() -> BeamShape` — Returns the referenced BeamShape object at station A by the BeamSpan.
- `getStationAXoffset() -> float` — Returns Station A Xoffset of the BeamSpan.
- `getStationAYOffset() -> float` — Returns Station A Yoffset of the BeamSpan.
- `getStationBOrientation() -> float` — Returns Station B shape orientation of the BeamSpan.
- `getStationBShape() -> BeamShape` — Returns the referenced BeamShape object at station B by the BeamSpan.
- `getStationBXoffset() -> float` — Returns Station B Xoffset of the BeamSpan.
- `getStationBYOffset() -> float` — Returns Station B Yoffset of the BeamSpan.
- `isTaperSection() -> bool` — check if the BeamSpan is tapered. The BeamSpan is tapered if the return value is True, otherwise, it is constant
- `reverse() -> None` — Reverses the orientation of the BeamSpan.
#### `update(name: str, description: str, shapeEndA: BeamShape, shapeEndB: BeamShape, shapeEndA_orientation: float, shapeEndB_orientation: float, shapeEndA_offset1: float, shapeEndA_offset2: float, shapeEndB_offset1: float, shapeEndB_offset2: float, spanType: apex.attribute.BeamSpanType, beamTarget: apex.geometry.EdgeCollection, plateTarget: apex.geometry.FaceCollection, shapeMatingDirection: apex.attribute.ShapeMatingSide, plateSide: apex.attribute.TopBottom, shapeBoundaryDistanceA: float, shapeBoundaryDistanceB: float, shapeEndA_direction1: apex.construct.Vector3D, shapeEndA_direction2: apex.construct.Vector3D, shapeEndB_direction1: apex.construct.Vector3D, shapeEndB_direction2: apex.construct.Vector3D, beamSpanOrientationType: apex.attribute.BeamSpanOrientationType, field_vector: {string:[]}, field_offset1: {string:[]}, field_offset2: {string:[]}, color: [int], renderStyle: apex.session.DisplayRenderStyle, material: apex.attribute.Material) -> None`
updates one or more of the BeamSpan properties. All arguments are optional. If an argument is omitted the value of the corresponding property will be unchanged by this method.

- `name` — updates the name of the BeamSpan. The BeamSpan name must be unique for all BeamSpans within the scope of the Part that composes this BeamSpan otherwise the system will modify the provided name to enforce uniqueness by appending an integer to this name.
- `description` — updates the Description of this BeamSpan
- `shapeEndA` — replaces the existing BeamShape at end A of the BeamSpan with the BeamSpan provided here
- `shapeEndB` — replaces the existing BeamShape at end B of the BeamSpan with the BeamSpan provided here
- `shapeEndA_orientation` — Updates the beam shape orientation at end A of this BeamSpan. The orientation of the shape is defined by an angle measured between the BeamShape 2 axis and the BeamSpan normal at End A. This argument represents an angle quantity and must be defined in the units of angle in the active script units system
- `shapeEndB_orientation` — Updates the beam shape orientation at end B of this BeamSpan. The orientation of the shape is defined by an angle measured between the BeamShape 2 axis and the BeamSpan normal at End B. This argument represents an angle quantity and must be defined in the units of angle in the active script units system
- `shapeEndA_offset1` — updates the offset of the centroid of the BeamShape from the BeamSpan support Edge in the 1 direction at end A of the BeamSpan. This argument represents a Length quantity and must be defined in the units of Length in the active script units system
- `shapeEndA_offset2` — updates the offset of the centroid of the BeamShape from the BeamSpan support Edge in the 2 direction at end A of the BeamSpan. This argument represents a Length quantity and must be defined in the units of Length in the active script units system
- `shapeEndB_offset1` — updates the offset of the centroid of the BeamShape from the BeamSpan support Edge in the 1 direction at end B of the BeamSpan. This argument represents a Length quantity and must be defined in the units of Length in the active script units system
- `shapeEndB_offset2` — updates the offset of the centroid of the BeamShape from the BeamSpan support Edge in the 2 direction at end B of the BeamSpan. This argument represents a Length quantity and must be defined in the units of Length in the active script units system
- `spanType` — defines whether the Span is Free-standing or a Stiffener
- `beamTarget` — replaces the Edge that this BeamSpan is associated to. Effectively moves the Span from the existing Edge to the Edge supplied here.
- `plateTarget` — replaces the Face that this BeamSpan references for stiffener orientation. This argument is only meaningful if the BeamSpan is a stiffener BeamSan and will be silently ignored otherwise.
- `shapeMatingDirection` — updates the orientation of the BeamShape w.r.t. the plate for stiffener BeamSpans. This argument will be silently ignored of the BeamSpan is a free standing BeamSpan
- `plateSide` — updates the side (Top/Bottom) of the plate (Surface/Face) that the BeamSpan will be located on. This argument is only meaningful if the BeamSpan is a stiffener BeamSpan, otherwise it will be silently ignored.
- `shapeBoundaryDistanceA` — updates the shape Boundary distance at end A of the Span for stiffener BeamSpans. In a stiffener BeamSpan the Beam butts directly against the free face of the plate. For BeamShape defined using Standard shapes or 1D profiles the offset of the BeamShape centroid from the support Edge is easily calculated form the geometry of the BeamShape however for Numeric beams that do not have a physical profile the offset of the beam centroid from the plate must be provided directly. This argument represents a Length quantity and must be entered using the units of Length that are active in the script unit system.
- `shapeBoundaryDistanceB` — updates the shape Boundary distance at end B of the Span for stiffener BeamSpans. In a stiffener BeamSpan the Beam butts directly against the free face of the plate. For BeamShape defined using Standard shapes or 1D profiles the offset of the BeamShape centroid from the support Edge is easily calculated form the geometry of the BeamShape however for Numeric beams that do not have a physical profile the offset of the beam centroid from the plate must be provided directly. This argument represents a Length quantity and must be entered using the units of Length that are active in the script unit system.
- `shapeEndA_direction1` — updates the vector defining the desired orientation of the "1" axis of the "End A" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End A, it will be projected onto that plane and the projected vector will be used. If omitted, but shapeEndA_direction2 is provided, the system will orient the shape using shapeEndA_direction2. If this argument is updated AND shapeEndA_orientation is updated in the same call, shapeEndA_orientation will be silently ignored
- `shapeEndA_direction2` — updates the vector defining the desired orientation of the "2" axis of the "End A" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End A, it will be projected onto that plane and the projected vector will be used. If omitted, but shapeEndA_direction1 is provided, the system will orient the shape using shapeEndA_direction1. If this argument is updated AND shapeEndA_orientation is updated in the same call, shapeEndA_orientation will be silently ignored .
- `shapeEndB_direction1` — updates the vector defining the desired orientation of the "1" axis of the "End B" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End B, it will be projected onto that plane and the projected vector will be used. If omitted, but shapeEndB_direction2 is provided, the system will orient the shape using shapeEndA_direction2. If this argument is updated AND shapeEndB_orientation is updated in the same call, shapeEndB_orientation will be silently ignored .
- `shapeEndB_direction2` — updates the vector defining the desired orientation of the "2" axis of the "End B" BeamShape. If this vector does not lie in a plane that is perpendicular to the tangent of the support Edge at End B, it will be projected onto that plane and the projected vector will be used. If omitted, but shapeEndB_direction1 is provided, the system will orient the shape using shapeEndB_direction1. If this argument is updated AND shapeEndB_orientation is updated in the same call, shapeEndB_orientation will be silently ignored .
- `beamSpanOrientationType` — defines the orientation type used for beam spans.
- `field_vector` — FEM Field of vectors are used to define the orientation. If a vector3D is defined for either direction 1 or direction 2 in end A or B, this argument is ignored.
- `field_offset1` — FEM Field of offset from end A to end B in the "1" direction, If the offset1 of shape end A or B is provided, this argument is ignored.
- `field_offset2` — FEM Field of offset from end A to end B in the "2" direction. If the offset2 of shape end A or B is provided, this argument is ignored.
- `color` — of this BeamSpan - optional
- `renderStyle` — of this BeamSpan - optional
- `material` — the material to be updated


## `apex.attribute.BeamSpanCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `BeamSpanCollection() -> None` — Construct a new BeamSpanCollection.

## `apex.attribute.Bolt`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)

## `apex.attribute.Bolt3D`  (extends `Bolt`)
Class Bolt3D. A class represents 3D bolt objects.
Properties: `boltAxisOrientation`, `boltBody`, `boltPreloads`, `controlNode`, `controlNodeDefinitionMethod`, `crossSectionElements`, `crossSectionFaces`, `crossSectionMethod`, `crossSectionNodes`, `crossSectionOffset`, `id`, `scaleOfOffset`

Methods:

- `getBoltAxisOrientation() -> apex.construct.Vector3D` — Get the Bolt axis orientation with a 3D vector.
- `getBoltBody() -> apex.EntityCollection` — Get body of the 3D bolt object.
- `getBoltPreloads() -> apex.environment.PreloadBoltCollection` — Get A collection of bolt preload object applying to the bolt object.If bolt preload is not existing, returns None.
- `getControlNode() -> apex.mesh.Node` — Get the Control node of the bolt.
- `getControlNodeDefinitionMethod() -> apex.attribute.ControlNodeDefinitionMethod` — Get the control node definition method of bolt.
- `getCrossSectionElements() -> apex.EntityCollection` — Get the Cross section elements opposites to bolt axis orientation. It can be elements or a group of elements.
- `getCrossSectionFaces() -> apex.EntityCollection` — Get the Cross section Faces to detect cross section elements and nodes. If it is not existing, returns None.
- `getCrossSectionMethod() -> apex.attribute.CrossSectionMethod` — Get the Cross section definition method of the 3D bolt object.
- `getCrossSectionNodes() -> apex.EntityCollection` — Get the Nodes of the cross section of bolt. It can be nodes or a group of nodes.
- `getCrossSectionOffset() -> float` — Get the Cross section offset of the bolt. It is only available when crossSectionMethod = Automatic.
- `getId() -> int` — Get the id of the bolt object.
- `getScaleOfOffset() -> float` — Get the scale which used to determine the offset value from top or bottom. The offset = scale*Bolt Length. It is only available when controlNodeDefinitionMethod = OffsetFromTop or OffsetFromBottom.
#### `update(name: str, description: str, id: int, crossSectionMethod: apex.attribute.CrossSectionMethod, boltBody: apex.Entity, crossSectionOffset: float, crossSectionElements: apex.EntityCollection, crossSectionNodes: apex.EntityCollection, boltAxisOrientation: apex.construct.Vector3D, crossSectionFaces: apex.EntityCollection, controlNodeDefinitionMethod: apex.attribute.ControlNodeDefinitionMethod, controlNode: apex.mesh.Node, scaleOfOffset: float, controlNodeLocation: apex.ILocation) -> None`
Used to Update the 3D bolt object.

- `name` — Optional- name prefox of the bolt
- `description` — Optional- description of the bolt
- `id` — Optional- id of the bolt
- `crossSectionMethod` — Cross section definition method of the 3D bolt object.
- `boltBody` — Body to represent the 3D bolt. It can be a geometry body, mesh body, a collection of 3D elements of the body, or a group of geometry body, mesh body or a collection of 3D elements. Omits it when crossSectonMethod = Manual.
- `crossSectionOffset` — Cross section offset of the bolt. It is only available when crossSectionMethod = Automatic.
- `crossSectionElements` — Cross section elements opposites to bolt axis orientation. It can be elements or a group of elements. it is only available when crossSectionMethod = Manual, omits it if crossSectionMethod = Automatic or if argument crossSectionFaces is defined.
- `crossSectionNodes` — Nodes of the cross section of bolt. It can be elements or a group of nodes, if the cross section elements are defined by group, cross section nodes should be a group of node. It is only available when crossSectionMethod = Manual, omits it if crossSectionMethod = Automatic or if argument crossSectionFaces is defined.
- `boltAxisOrientation` — Bolt axis orientation with a 3D vector. Omits it if crossSectionMethod = Automatic
- `crossSectionFaces` — Cross section Faces to detect cross section elements and nodes. It is only available when crossSectionMethod = Manual, omits it if crossSectionMethod = Automatic
- `controlNodeDefinitionMethod` — Control node definition method
- `controlNode` — Control node of the bolt. It is only available when controlNodeDefinitionMethod = User.
- `scaleOfOffset` — The scale used to determine the offset value from top or bottom. The offset = scale*Bolt Length. It is only available when controlNodeDefinitionMethod = OffsetFromTop or OffsetFromBottom.
- `controlNodeLocation` — Optional- Use ILocation to define Control node of the bolt. It is only available when controlNodeDefinitionMethod = User. Omits it of controlNode argument is defined.


## `apex.attribute.Bolt3DCollection`  (extends `EntityCollection`)
Iterable collection of Bolt3D, based on EntityCollection.

Methods:

- `Bolt3DCollection() -> None` — Construct a new Bolt3DCollection.

## `apex.attribute.Bushing`  (extends `Connector`)

## `apex.attribute.BushingCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `BushingCollection() -> None` — Construct a new BushingCollection.

## `apex.attribute.BushingRepProperties`  (extends `ConnectorDiscreteProperty`)
Class BushingRepProperties. The class BushingRepProperties holds the properties of Bushing connector.
Properties: `embedded`, `id`, `lengthOfCoincidentGrids`, `mass`, `referenceTemperature`, `rotationalDampingX`, `rotationalDampingY`, `rotationalDampingZ`, `rotationalStiffnessX`, `rotationalStiffnessY`, `rotationalStiffnessZ`, `rotationalStrainRecovery`, `rotationalStressRecovery`, `rotationalStructuralDampingX`, `rotationalStructuralDampingY`, `rotationalStructuralDampingZ`, `thermalExpansionCoefficient`, `translationalDampingX`, `translationalDampingY`, `translationalDampingZ`, `translationalStiffnessX`, `translationalStiffnessY`, `translationalStiffnessZ`, `translationalStrainRecovery`, `translationalStressRecovery`, `translationalStructuralDampingX`, `translationalStructuralDampingY`, `translationalStructuralDampingZ`

Methods:

- `getEmbedded() -> bool` — Returns embedded of the bushing.
- `getId() -> int` — Returns id of the bushing.
- `getLengthOfCoincidentGrids() -> float` — The coincidentGridsLengthof bushing.
- `getMass() -> float` — The lumped mass of bushing.
- `getReferenceTemperature() -> float` — The reference temperature of bushing.
- `getRotationalDampingX() -> float` — The rotationalDamping in X direction.
- `getRotationalDampingY() -> float` — The rotationalDamping in Y direction.
- `getRotationalDampingZ() -> float` — The rotationalDamping in Z direction.
- `getRotationalStiffnessX() -> float` — The rotationalStiffness in X direction.
- `getRotationalStiffnessY() -> float` — The rotationalStiffness in Y direction.
- `getRotationalStiffnessZ() -> float` — The rotationalStiffness in Z direction.
- `getRotationalStrainRecovery() -> float` — The rotationalStrainRecovery of bushing.
- `getRotationalStressRecovery() -> float` — The rotationalStressRecovery of bushing.
- `getRotationalStructuralDampingX() -> float` — The structuralDampingRotation in X direction.
- `getRotationalStructuralDampingY() -> float` — The structuralDampingRotation in Y direction.
- `getRotationalStructuralDampingZ() -> float` — The structuralDampingRotation in Z direction.
- `getThermalExpansionCoefficient() -> float` — The thermal expansion coefficient of bushing.
- `getTranslationalDampingX() -> float` — The translationalDamping in X direction.
- `getTranslationalDampingY() -> float` — The translationalDamping in Y direction.
- `getTranslationalDampingZ() -> float` — The translationalDamping in Z direction.
- `getTranslationalStiffnessX() -> float` — The translationalStiffness in X direction.
- `getTranslationalStiffnessY() -> float` — The translationalStiffness in Y direction.
- `getTranslationalStiffnessZ() -> float` — The translationalStiffness in Z direction.
- `getTranslationalStrainRecovery() -> float` — The translationalStrainRecovery of bushing.
- `getTranslationalStressRecovery() -> float` — The translationalStressRecovery of bushing.
- `getTranslationalStructuralDampingX() -> float` — The structuralDampingDirection in X direction.
- `getTranslationalStructuralDampingY() -> float` — The structuralDampingDirection in Y direction.
- `getTranslationalStructuralDampingZ() -> float` — The structuralDampingDirection in Z direction.
#### `update(translationalStiffnessX: float, translationalStiffnessY: float, translationalStiffnessZ: float, rotationalStiffnessX: float, rotationalStiffnessY: float, rotationalStiffnessZ: float, translationalDampingX: float, translationalDampingY: float, translationalDampingZ: float, rotationalDampingX: float, rotationalDampingY: float, rotationalDampingZ: float, translationalStructuralDampingX: float, translationalStructuralDampingY: float, translationalStructuralDampingZ: float, rotationalStructuralDampingX: float, rotationalStructuralDampingY: float, rotationalStructuralDampingZ: float, translationalStressRecovery: float, rotationalStressRecovery: float, translationalStrainRecovery: float, rotationalStrainRecovery: float, mass: float, thermalExpansionCoefficient: float, referenceTemperature: float, lengthOfCoincidentGrids: float, name: str, description: str, id: int) -> None`
Update this connector properties.

- `translationalStiffnessX` — Update the translationalStiffnessX of this connectorProperty.
- `translationalStiffnessY` — Update the translationalStiffnessY of this connectorProperty.
- `translationalStiffnessZ` — Update the translationalStiffnessZ of this connectorProperty.
- `rotationalStiffnessX` — Update the rotationalStiffnessX of this connectorProperty.
- `rotationalStiffnessY` — Update the rotationalStiffnessY of this connectorProperty.
- `rotationalStiffnessZ` — Update the rotationalStiffnessZ of this connectorProperty.
- `translationalDampingX` — Update the translationalDampingX of this connectorProperty.
- `translationalDampingY` — Update the translationalDampingY of this connectorProperty.
- `translationalDampingZ` — Update the translationalDampingZ of this connectorProperty.
- `rotationalDampingX` — Update the rotationalDampingX of this connectorProperty.
- `rotationalDampingY` — Update the rotationalDampingY of this connectorProperty.
- `rotationalDampingZ` — Update the rotationalDampingZ of this connectorProperty.
- `translationalStructuralDampingX` — update structural damping along X axis
- `translationalStructuralDampingY` — update structural damping along X axis
- `translationalStructuralDampingZ` — update structural damping along Z axis
- `rotationalStructuralDampingX` — update structural damping about X axis
- `rotationalStructuralDampingY` — update structural damping about Y axis
- `rotationalStructuralDampingZ` — update structural damping about Z axis
- `translationalStressRecovery` — update translational stress recovery coefficient
- `rotationalStressRecovery` — update rotational stress recovery coefficient
- `translationalStrainRecovery` — update translational strain recovery
- `rotationalStrainRecovery` — update rotational strain recovery coefficient
- `mass` — update mass of the bushing
- `thermalExpansionCoefficient` — update thermal expansion coefficient
- `referenceTemperature` — update reference temperature
- `lengthOfCoincidentGrids` — update length if two grids are coincident
- `name` — update the name of this connector property.
- `description` — update the description of this connector property.
- `id` — update the id of this connector property.

One or more properties may be updated in each call to update().


## `apex.attribute.BushingRepPropertiesCollection`  (extends `EntityCollection`)

Methods:

- `BushingRepPropertiesCollection() -> None` — Construct a new BushingRepPropertiesCollection.

## `apex.attribute.Connector`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class Connector. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Instead use ConnectorDiscrete
Properties: `applicationMethod1`, `applicationMethod2`, `closedStiffness`, `colorRGB`, `connectorProperties`, `connectorType`, `damping`, `diameter`, `edgeWeight`, `end1AttachmentRegion`, `end1DistributionMethod`, `end1InterfacePoint`, `end2AttachmentRegion`, `end2DistributionMethod`, `end2InterfacePoint`, `highlighted`, `initialOpening`, `kineticFriction`, `linkMaterial`, `openStiffness`, `orientation`, `pointSize`, `preload`, `rotationalDampingX`, `rotationalDampingY`, `rotationalDampingZ`, `rotationalStiffnessX`, `rotationalStiffnessY`, `rotationalStiffnessZ`, `staticFriction`, `stiffness`, `translationalDampingX`, `translationalDampingY`, `translationalDampingZ`, `translationalStiffnessX`, `translationalStiffnessY`, `translationalStiffnessZ`, `transverseStiffness`

Methods:

- `getApplicationMethod1() -> ApplicationMethod` — Returns ApplicationMethod1 of the Connector.
- `getApplicationMethod2() -> ApplicationMethod` — Returns ApplicationMethod2 of the Connector.
- `getClosedStiffness() -> float` — Returns closedStiffness of the Connector.
- `getConnectorProperties() -> ConnectorProperty` — Returns ConnectorProperty of the Connector.
- `getConnectorType() -> ConnectorType` — Returns connectorType of the Connector.
- `getDamping() -> float` — Returns Damping of the Connector.
- `getDiameter() -> float` — Returns diameter of the Connector.
- `getEnd1AttachmentRegion() -> apex.EntityCollection` — Returns end1AttachmentRegion of the Connector.
- `getEnd1DistributionMethod() -> DistributionType` — Returns end1DistributionMethod of the Connector.
- `getEnd1InterfacePoint() -> apex.Coordinate` — Returns End1InterfacePoint of the Connector.
- `getEnd2AttachmentRegion() -> apex.EntityCollection` — Returns end2AttachmentRegion of the Connector.
- `getEnd2DistributionMethod() -> DistributionType` — Returns end2DistributionMethod of the Connector.
- `getEnd2InterfacePoint() -> apex.Coordinate` — Returns End2InterfacePoint of the Connector.
- `getInitialOpening() -> float` — Returns initialOpening of the Connector.
- `getKineticFriction() -> float` — Returns kineticFriction of the Connector.
- `getLinkMaterial() -> Material` — Returns the Referenced Material of the Connector.
- `getOpenStiffness() -> float` — Returns openStiffness of the Connector.
- `getOrientation() -> apex.construct.Orientation` — Returns apex.construct.Orientation of the Connector.
- `getPreload() -> float` — Returns preload of the Connector.
- `getRotationalDampingX() -> float` — Returns rotationalDampingX of the Connector.
- `getRotationalDampingY() -> float` — Returns rotationalDampingY of the Connector.
- `getRotationalDampingZ() -> float` — Returns rotationalDampingZ of the Connector.
- `getRotationalStiffnessX() -> float` — Returns rotationalStiffnessX of the Connector.
- `getRotationalStiffnessY() -> float` — Returns rotationalStiffnessY of the Connector.
- `getRotationalStiffnessZ() -> float` — Returns rotationalStiffnessZ of the Connector.
- `getStaticFriction() -> float` — Returns staticFriction of the Connector.
- `getStiffness() -> float` — Returns stiffness of the Connector.
- `getTranslationalDampingX() -> float` — Returns translationalDampingX of the Connector.
- `getTranslationalDampingY() -> float` — Returns translationalDampingY of the Connector.
- `getTranslationalDampingZ() -> float` — Returns translationalDampingZ of the Connector.
- `getTranslationalStiffnessX() -> float` — Returns translationalStiffnessX of the Connector.
- `getTranslationalStiffnessY() -> float` — Returns translationalStiffnessY of the Connector.
- `getTranslationalStiffnessZ() -> float` — Returns translationalStiffnessZ of the Connector.
- `getTransverseStiffness() -> float` — Returns transverseStiffness of the Connector.
#### `update(name: str, connectorProperties: ConnectorProperty, applicationMethod1: apex.attribute.ApplicationMethod, applicationMethod2: apex.attribute.ApplicationMethod, end1InterfacePoint: apex.Coordinate, end2InterfacePoint: apex.Coordinate, end1AttachmentRegion: EntityCollection, end1DistributionMethod: apex.attribute.DistributionType, end2AttachmentRegion: EntityCollection, end2DistributionMethod: apex.attribute.DistributionType, orientation: apex.construct.Orientation, description: str, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this Connector properties.

- `name` — of this Connector
- `connectorProperties` — of this Connector
- `applicationMethod1` — of this Connector
- `applicationMethod2` — of this Connector
- `end1InterfacePoint` — of this Connector
- `end2InterfacePoint` — of this Connector
- `end1AttachmentRegion` — of this Connector
- `end1DistributionMethod` — of this Connector
- `end2AttachmentRegion` — of this Connector
- `end2DistributionMethod` — of this Connector
- `orientation` — of this Connector
- `description` — of this Connector
- `color` — of this Connector
- `renderStyle` — of this Connector
- `enableTransparency` — of this Connector
- `transparencyLevel` — of this Connector

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.ConnectorCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `ConnectorCollection() -> None` — Construct a new ConnectorCollection.

## `apex.attribute.ConnectorDiscrete`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
The class ConnectorDiscrete.
Properties: `applicationMethod1`, `applicationMethod2`, `colorRGB`, `connectorProperties`, `connectorType`, `createTypeForFastener`, `edgeWeight`, `end1AttachmentRegion`, `end1DependentDOF`, `end1DistributionMethod`, `end1DOF`, `end1IndependentDOF`, `end1InterfacePoint`, `end2AttachmentRegion`, `end2DependentDOF`, `end2DistributionMethod`, `end2DOF`, `end2IndependentDOF`, `end2InterfacePoint`, `highlighted`, `id`, `locationOffsetCoordinates`, `locationOffsetCoordinateSystem`, `locationParametric`, `masterLocationForPatches`, `masterNodeForPatches`, `orientation`, `orientationByLocation`, `orientationByVector`, `piercingNodeForPatchA`, `piercingNodeForPatchB`, `pointSize`

Methods:

- `getApplicationMethod1() -> ApplicationMethod` — The application method for the 1st end of the connector.
- `getApplicationMethod2() -> ApplicationMethod` — The application method for the 2nd end of the connector.
- `getConnectorDiscreteProperties() -> ConnectorDiscreteProperty` — The connectorProperties of the connector.
- `getConnectorType() -> ConnectorType` — The connectorType of ConnectorDiscrete.
- `getCreateTypeForFastener() -> apex.attribute.createTypeForFastener` — Returns indicate the creation type as one of the enumerations : "ByElement" or "ByProperty".
- `getEnd1AttachmentRegion() -> apex.EntityCollection` — The attachment region of the 1st end. THIS ATTRIBUTE WILL BE DEPRECATED BECASUE NOW ONE CONNECTOR CREATED BY APEX WILL ONLY CONNECTS TWO NODES.
- `getEnd1DOF() -> str` — Returns end1DOF of the ConnectorDiscrete.
- `getEnd1DependentDOF() -> str` — Returns end1DependentDOF of the ConnectorDiscrete.
- `getEnd1DistributionMethod() -> DistributionType` — The distribution type of the 1st end.
- `getEnd1IndependentDOF() -> str` — Returns end1IndependentDOF of the ConnectorDiscrete.
- `getEnd1InterfacePoint() -> apex.Coordinate` — The location of the 1st end.
- `getEnd2AttachmentRegion() -> apex.EntityCollection` — The attachment region of the 2nd end. THIS ATTRIBUTE WILL BE DEPRECATED BECASUE NOW ONE CONNECTOR CREATED BY APEX WILL ONLY CONNECTS TWO NODES.
- `getEnd2DOF() -> str` — Returns end2DOFof the ConnectorDiscrete.
- `getEnd2DependentDOF() -> str` — Returns end2DependentDOF of the ConnectorDiscrete.
- `getEnd2DistributionMethod() -> DistributionType` — The distribution type of the 2nd end.
- `getEnd2IndependentDOF() -> str` — Returns end2IndependentDOF of the ConnectorDiscrete.
- `getEnd2InterfacePoint() -> apex.Coordinate` — The location of the 2nd end.
- `getId() -> int` — Returns id of the ConnectorDiscrete.
- `getLocationOffsetCoordinateSystem() -> apex.construct.CoordinateSystem` — Returns locationOffsetCoordinateSystem of the ConnectorDiscrete.
- `getLocationOffsetCoordinates() -> apex.Coordinate` — Returns locationOffsetCoordinates of the ConnectorDiscrete.
- `getLocationParametric() -> float` — Returns locationParametric of the ConnectorDiscrete.
- `getMasterLocationForPatches() -> apex.Coordinate` — Returns master location for patches.
- `getMasterNodeForPatches() -> apex.Coordinate` — Returns location of master node for two patches.
- `getOrientation() -> apex.construct.Orientation` — Returns apex.construct.Orientation of the ConnectorDiscrete.
- `getOrientationByLocation() -> apex.Coordinate` — Returns orientationByLocation of the ConnectorDiscrete.
- `getOrientationByVector() -> apex.construct.Vector3D` — Returns orientationByVector of the ConnectorDiscrete.
- `getPiercingNodeForPatchA() -> apex.Coordinate` — Returns piercing point for patch A.
- `getPiercingNodeForPatchB() -> apex.Coordinate` — Returns piercing location for patch B.
#### `update(name: str, connectorProperties: ConnectorDiscreteProperty, applicationMethod1: apex.attribute.ApplicationMethod, applicationMethod2: apex.attribute.ApplicationMethod, end1InterfacePoint: apex.Coordinate, end2InterfacePoint: apex.Coordinate, end1AttachmentRegion: EntityCollection, end1DistributionMethod: apex.attribute.DistributionType, end2AttachmentRegion: EntityCollection, end2DistributionMethod: apex.attribute.DistributionType, orientation: apex.construct.Orientation, orientationByLocation: apex.ILocation, orientationByVector: apex.construct.Vector3D, locationParametric: float, locationOffsetCoordinateSystem: apex.construct.CoordinateSystem, locationOffsetCoordinates: apex.ILocation, description: str, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int, end1DOF: str, end2DOF: str, end1IndependentDOF: str, end1DependentDOF: str, end2IndependentDOF: str, end2DependentDOF: str, piercingNodeForPatchA: apex.Coordinate, piercingNodeForPatchB: apex.Coordinate, masterNodeForPatches: apex.Coordinate, masterLocationForPatches: apex.ILocation, id: int, deleteUnreferencedNodeAndNodeTie: bool) -> None`
Update this ConnectorDiscrete.

- `name` — Update the name of this connector.
- `connectorProperties` — Update the connectorProperty of this connector.
- `applicationMethod1` — Update the application method for the 1st end.
- `applicationMethod2` — Update the application method for the 2nd end.
- `end1InterfacePoint` — Update the location of the 1st end.
- `end2InterfacePoint` — Update the location of the 2nd end.
- `end1AttachmentRegion` — Update the attachment region of 1st end.
- `end1DistributionMethod` — Update the distribution type for the 1st end.
- `end2AttachmentRegion` — Update the attachment region of 2nd end.
- `end2DistributionMethod` — Update the distribution type for the 2nd end.
- `orientation` — Update the orientation of the connector. If orientation is provided, other 2 arguments "orientationByLocation" and "orientationByVector" will be silently ignored. If all 3 types of orientation methods are provided, the priority is: orientation>orientationByVector>orientationByLocation.
- `orientationByLocation` — Update the orientationByLocation of the connector.
- `orientationByVector` — Update the orientationByVector of the connector.
- `locationParametric` — Update the locationParametric of the connector.
- `locationOffsetCoordinateSystem` — Update the locationOffsetCoordinateSystem of the connector.
- `locationOffsetCoordinates` — Update the locationOffsetCoordinates of the connector.
- `description` — Update the description of the connector
- `color` — Update the color of this connector.
- `renderStyle` — Update the render style of this connector.
- `enableTransparency` — Enable or disable the transparency of this connector.
- `transparencyLevel` — Update the transparency level of this connector.
- `end1DOF` — Optional - degree of freedom for the first end of spring or damper, it could be one of "1,2,3,4,5,6". It is also used for grounded spring or damper.
- `end2DOF` — Optional - degree of freedom for the second end of spring or damper, it could be one of "1,2,3,4,5,6".
- `end1IndependentDOF` — Optional - independent DOF at end 1 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `end1DependentDOF` — Optional - Dependent DOF at end 1 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `end2IndependentDOF` — Optional - independent DOF at end 2 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `end2DependentDOF` — Optional - dependent DOF at end 2 for rigid link, it can be any combination of "1,2,3,4,5,6", or blank.
- `piercingNodeForPatchA` — Argument of piercing point for patch A.
- `piercingNodeForPatchB` — Argument of piercing location for patch B.
- `masterNodeForPatches` — Argument of location of master node for two patches.
- `masterLocationForPatches` — Argument of master location for patches.
- `id` — Optional - id of the created connector.
- `deleteUnreferencedNodeAndNodeTie` — Optional argument to control if un-referenced node and node tie will be deleted, the value is set as false by default if value is not given.

One or more properties may be updated in each call to update().


## `apex.attribute.ConnectorDiscreteCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `ConnectorDiscreteCollection() -> None` — Construct a new ConnectorDiscreteCollection.

## `apex.attribute.ConnectorDiscreteProperty`  (extends `Entity`, `IName`)
The base class ConnectorDiscreteProperty.

## `apex.attribute.ConnectorProperty`
Properties: `damping`, `diameter`, `linkMaterial`, `rotationalDampingX`, `rotationalDampingY`, `rotationalDampingZ`, `rotationalStiffnessX`, `rotationalStiffnessY`, `rotationalStiffnessZ`, `stiffness`, `translationalDampingX`, `translationalDampingY`, `translationalDampingZ`, `translationalStiffnessX`, `translationalStiffnessY`, `translationalStiffnessZ`

## `apex.attribute.ConstitutiveModel`  (extends `Entity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.

## `apex.attribute.ContactBody`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IName`)
A class to represent Contact Body.
Properties: `bodyProperty`, `bodyType`, `contactResultCalculation`, `id`, `target`

Methods:

- `getBodyProperty() -> apex.attribute.ContactBodyProperty` — Contact body properties.
- `getBodyType() -> apex.attribute.ContactBodyType` — Defines if the body is rigid or deformable. By default, it is deformable.
- `getContactResultCalculation() -> apex.attribute.ContactResultCalculation` — Calculate the global resultant contact force/moment in Origin or Estimated centroid. Omits it if body type is not deform.
- `getId() -> int` — ID of the contact body. If omits, the system will automatically assign an ID.
- `getTarget() -> apex.EntityCollection` — An entity collection for contact body.
#### `update(name: str, description: str, id: int, bodyType: apex.attribute.ContactBodyType, target: apex.EntityCollection, bodyProperty: apex.attribute.ContactBodyProperty, contactResultCalculation: apex.attribute.ContactResultCalculation) -> ContactBody`
update the contact body.

- `name` — Optional name for the contact body.
- `description` — Optional string providing a description for the contact body.
- `id` — ID of the contact body. If omits, the system will automatically assign an ID.
- `bodyType` — Defines if the body is rigid or deformable. By default, it is deformable.
- `target` — An entity collection for contact body. For deform body, the target entities can be solid body, solid cell, sheet body, solid mesh body, shell mesh body, 3D elements, 2D elements, face, element face and 2D/3D element property. For rigid body, the target entities can be solid body, sheet body, curve body, face, edge, shell mesh body, curve mesh body, 2D element, 1D element.
- `bodyProperty` — Contact body properties. If omits, the default contact body properties will be used.
- `contactResultCalculation` — Optional-calculate the global resultant contact force/moment in Origin or Estimated centroid. Omits it if body type is not deform.


## `apex.attribute.ContactBodyCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of ContactBody, based on EntityCollection.

Methods:

- `ContactBodyCollection() -> None` — Construct a new ContactBodyCollection.

## `apex.attribute.ContactBodyProperty`  (extends `Entity`)
A contact body property of each side contact pair.
Properties: `discontinuityDefinition`, `discontinuityTarget`, `ignoreShellThickness`, `projectMidNode`, `shellLayer`, `smoothingFeatureAngle`, `smoothingState`

Methods:

- `getDiscontinuityDefinition() -> apex.attribute.DiscontinuityDefinition` — Discontinuity Definition for smoothing. It is used when smoothingStage is true.
- `getDiscontinuityTarget() -> apex.EntityCollection` — the target discontinuities entities for smoothing. It can be geometry edge or element edge. It is used when DiscontinuityDefinition = Manual and smoothingStage is true.
- `getIgnoreShellThickness() -> bool` — Consider or ignore shell thickness during detection of contact.
- `getProjectMidNode() -> bool` — Optional - The mid-side grid of quadratic elements are projected onto the selected spline surfaces. Ignored if smoothing is false.
- `getShellLayer() -> apex.attribute.ShellLayer` — Shell layer to be used for contact detection.
- `getSmoothingFeatureAngle() -> float` — Optional - Angle to detect feature edges. Edges between Elements with face normal deviation equal to or larger will be detected as an edge feature, and not be smoothed. It is used when DiscontinuityDefinition = Auto and smoothinStage is true.
- `getSmoothingState() -> bool` — Optional - enable to control geometric smoothing of boundary of deformable body. Omits it if it is not a deform body.
#### `update(smoothingState: apex.ApexBool, smoothingFeatureAngle: float, projectMidNode: apex.ApexBool, shellLayer: apex.attribute.ShellLayer, ignoreShellThickness: apex.ApexBool, discontinuityDefinition: apex.attribute.DiscontinuityDefinition, discontinuityTarget: apex.EntityCollection) -> None`
update contact body property.

- `smoothingState` — Optional - enable to control geometric smoothing of boundary of deformable body.
- `smoothingFeatureAngle` — Optional - Angle to detect feature edges. Edges between Elements with face normal deviation equal to or larger will be detected as an edge feature, and not be smoothed. It is used when DiscontinuityDefinition = Auto and smoothinStage is true.
- `projectMidNode` — Optional - The mid-side grid of quadratic elements are projected onto the selected spline surfaces. Ignored if smoothing is false.
- `shellLayer` — Optional-Shell layer to be used for contact detection.
- `ignoreShellThickness` — Optional- Consider or ignore shell thickness during detection of contact.
- `discontinuityDefinition` — Optional- Discontinuity Definition for smoothing. It is used when smoothingStage is true.
- `discontinuityTarget` — Optional- the target discontinuities entities for smoothing. It can be geometry edge or element edge. It is used when DiscontinuityDefinition = Manual and smoothingStage is true.


## `apex.attribute.ContactTable`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
A class to represent ContactTable.
Properties: `id`, `interactions`

Methods:

- `getId() -> int` — Returns ID of the ContactTable. If omits, the system will automatically assign an ID.
- `getInteractions() -> apex.attribute.InteractionCollection` — Returns A collection of Interaction for the ContactTable.
#### `update(name: str, description: str, id: int, interactions: InteractionCollection) -> apex.attribute.ContactTable`
Creates and returns a ContactTable.

- `name` — Optional name for the ContactTablen.
- `description` — Optional string providing a description for the ContactTable.
- `id` — ID of the ContactTable. If omits, the system will automatically assign an ID.
- `interactions` — A collection of interactions for the contact table(BCTABL1).


## `apex.attribute.ContactTableCollection`  (extends `EntityCollection`)
Iterable collection of ContactTable, based on EntityCollection.

Methods:

- `ContactTableCollection() -> None` — Construct a new ContactTableCollection.

## `apex.attribute.CylindricalJoint`  (extends `Joint`)
Contains CylindricalJoint and methods for editing/getting CylindricalJoint attributes.

Methods:

#### `update(name: str, description: str, jointAxis: apex.attribute.JointAxis, side1: apex.EntityCollection, side1DistributionType: apex.attribute.DistributionType, side2: apex.EntityCollection, side2DistributionType: apex.attribute.DistributionType, jointOrigin: apex.Entity, jointOrientation: apex.construct.Orientation, axisLocationMode: apex.attribute.AxisLocationMode, jointRenderType: apex.attribute.JointRenderType) -> None`
Update this CylindricalJoint properties.

- `name` — of this CylindricalJoint
- `description` — of this CylindricalJoint
- `jointAxis` — of this CylindricalJoint
- `side1` — of this CylindricalJoint
- `side1DistributionType` — of this CylindricalJoint
- `side2` — of this CylindricalJoint
- `side2DistributionType` — of this CylindricalJoint
- `jointOrigin` — of this CylindricalJoint
- `jointOrientation` — of this CylindricalJoint
- `axisLocationMode` — of this CylindricalJoint
- `jointRenderType` — of this CylindricalJoint - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.Damper1D`  (extends `Connector`)

## `apex.attribute.Damper1DCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `Damper1DCollection() -> None` — Construct a new Damper1DCollection.

## `apex.attribute.Damper1DRepProperties`  (extends `ConnectorDiscreteProperty`)
Class Damper1DRepProperties. The class Damper1DRepProperties holds the properties of Damper1D connector.
Properties: `damping`, `embedded`, `id`

Methods:

- `getDamping() -> float` — The damping of the Damper1D connector.
- `getEmbedded() -> bool` — Returns embedded of the Damper1D connector.
- `getId() -> int` — Returns id of the Damper1D connector.
#### `update(damping: float, name: str, description: str, id: int) -> None`
Update this connector properties.

- `damping` — Update the damping of this connectorProperty.
- `name` — update the name of this connector property.
- `description` — update the description of this connector property.
- `id` — update the id of this connector property.

One or more properties may be updated in each call to update().


## `apex.attribute.Damper1DRepPropertiesCollection`  (extends `EntityCollection`)

Methods:

- `Damper1DRepPropertiesCollection() -> None` — Construct a new Damper1DRepPropertiesCollection.

## `apex.attribute.DiscreteDataTable`
class DiscreteDataTable.

Methods:

#### `getRegions() -> [DiscreteRegion]`
get the discrete region list.

Returns: the list of discrete region

#### `removeValueByElementFaceID(elemId: int int int, faceId: int int int) -> bool`
remove element if DiscreteRegionType is ElementFace.

- `elemId` — storing in this DiscreteDataTable
- `faceId` — storing in this DiscreteDataTable

Returns: true if the row is removed successfully

#### `removeValueByElementID(elemId: int int int) -> bool`
remove element if DiscreteRegionType is Element.

- `elemId` — storing in this DiscreteDataTable

Returns: true if the row is removed successfully

#### `removeValueByElementNodeID(elemId: int int int, nodeId: int int int) -> bool`
remove element if DiscreteRegionType is ElementNode.

- `elemId` — storing in this DiscreteDataTable
- `nodeId` — storing in this DiscreteDataTable

Returns: true if the row is removed successfully

#### `removeValueByFaceNodeID(elemId: int int int, faceId: int int int, nodeId: int int int) -> bool`
remove element if DiscreteRegionType is FaceNode.

- `elemId` — storing in this DiscreteDataTable
- `faceId` — storing in this DiscreteDataTable
- `nodeId` — storing in this DiscreteDataTable

Returns: true if the row is removed successfully

#### `updateValueByElementFaceID(elemId: int int int, faceId: int int int, value: float) -> bool`
Update the value field if DiscreteRegionType is ElementFace.

- `elemId` — storing in this DiscreteDataTable
- `faceId` — storing in this DiscreteDataTable
- `value` — storing in this DiscreteDataTable

Returns: true if the value is updated successfully

#### `updateValueByElementID(elemId: int int int, value: float) -> bool`
Update the value field if DiscreteRegionType is Element.

- `elemId` — storing in this DiscreteDataTable
- `value` — storing in this DiscreteDataTable

Returns: true if the value is updated successfully

#### `updateValueByElementNodeID(elemId: int int int, nodeId: int int int, value: float) -> bool`
Update the value field if DiscreteRegionType is ElementNode.

- `elemId` — storing in this DiscreteDataTable
- `nodeId` — storing in this DiscreteDataTable
- `value` — storing in this DiscreteDataTable

Returns: true if the value is updated successfully

#### `updateValueByFaceNodeID(elemId: int int int, faceId: int int int, nodeId: int int int, value: float) -> bool`
Update the value field if DiscreteRegionType is FaceNode.

- `elemId` — storing in this DiscreteDataTable
- `faceId` — storing in this DiscreteDataTable
- `nodeId` — storing in this DiscreteDataTable
- `value` — storing in this DiscreteDataTable

Returns: true if the value is updated successfully

#### `updateValueByNodeID(nodeId: int int int, value: float) -> bool`
Update the value field if DiscreteRegionType is Node.

- `nodeId` — storing in this DiscreteDataTable
- `value` — storing in this DiscreteDataTable

Returns: true if the value is updated successfully

#### `updateVectorByElementID(elemId: int int int, vector: apex.construct.Vector3D) -> bool`
Update the vector in Field if DiscreteRegionType is Element.

- `elemId` — storing in this DiscreteDataTable
- `vector` — storing in this DiscreteDataTable.

Returns: true if the value is updated successfully

#### `updateVectorByElementNodeID(elemId: int int int, nodeId: int int int, vector: apex.construct.Vector3D) -> bool`
update the vector field if DiscreteRegionType is ElementNode.

- `elemId` — storing in this DiscreteDataTable
- `nodeId` — storing in this DiscreteDataTable.
- `vector` — storing in this DiscreteDataTable.

Returns: true if the value is updated successfully


## `apex.attribute.DiscreteFEMField`  (extends `Entity`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class DiscreteFEMField. This class describes the property of DiscreteFEMField. This is the base class for Field. including: ThicknessOffsetField,.MaterialOrientationField2D.
Properties: `discreteFEMFieldType`, `discreteValue`

Methods:

- `getDiscreteFEMFieldType() -> apex.attribute.DiscreteFEMFieldType` — Get the DiscreteFEMFieldType of DiscreteFEMField.
#### `getDiscreteValue(type: apex.attribute.DiscreteFEMFieldType) -> {str:{dict}}`
Get the discrete value that this DiscreteFEMField has.

- `type` — the type of discrete value, include DiscreteThicknessField, DiscreteOffsetField, DiscreteAngleField, DiscreteCoordinateSystemField, Undefined. When the field is ThicknessOffsetFieldMidsurface and don't set the type(use the default of type Undefined), This method return the thickness values. Example : fieldValues_= { "Model/Part 1/Mesh 1": { 'element_ids' : [1,2,3,4,5], 'values' : [-55.,22.,2.,3.,4.]} }

#### `updateDiscreteValue(name: str, type: apex.attribute.DiscreteFEMFieldType, fieldValues: {str:{dict}}) -> None`
Used to update the attribute for DiscreteFEMField. In the scripting we will allow user update the discrete value.

- `name` — the name of this object as a string
- `type` — the type of discrete value, include DiscreteThicknessField, DiscreteOffsetField, DiscreteAngleField, DiscreteCoordinateSystemField, Undefined If the discrete value is no ambiguity , this parameter can be left unset.
- `fieldValues` — the value of discrete. Example : fieldValues_= { "Model/Part 1/Mesh 1": { 'element_ids' : [1,2,3,4,5], 'values' : [-55.,22.,2.,3.,4.]} }


## `apex.attribute.DiscreteFEMFieldCollection`  (extends `EntityCollection`)
Iterable collection of DiscreteFEMField, based on EntityCollection.

Methods:

- `DiscreteFEMFieldCollection() -> None` — Construct a new DiscreteFEMFieldCollection.

## `apex.attribute.DiscreteRegion`
class DiscreteRegion. THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: LoadPressure, LoadPressurePropertyStaticConstant and LoadPressurePropertyStaticVariable.
Properties: `discreteIDs1a`, `discreteIDs1b`, `discreteIDs2`, `discreteRegionType`, `values`

Methods:

- `getDiscreteIDs1a() -> [int int int]`
- `getDiscreteIDs1b() -> [int int int]`
- `getDiscreteIDs2() -> [int int int]`
- `getDiscreteRegionType() -> apex.attribute.DiscreteRegionType`
- `getMeshBodyIndices() -> [int int]`
- `getValues() -> [float]`

## `apex.attribute.DiscreteTie`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Contains NodeTies and methods for adding/deleting/getting NodeTie objects.
Properties: `count`, `dependentDof`, `distributionMode`, `distributionType`

Methods:

#### `deleteNodeTies(nodeTies: apex.attribute.NodeTieCollection) -> bool`
Remove NodeTies from this DiscreteTie.

- `nodeTies` — is A collection of NodeTies. The NodeTies in this collection will be added to the NodeTies that are already composed by the target DiscreteTie and they will be removed from the DiscreteTie that currently composes them. If the NodeTie that is being added does not share the same nearest common ancestor as the DiscreteTie to which it is being added the method will return false, otherwise it will return True

- `getCount() -> int` — Returns Count (of NodeTies in) of the DiscreteTie.
- `getDependentDof() -> str` — Returns dependentDoF of the DiscreteTie.
- `getDistributionMode() -> str` — Returns distributionMode of the DiscreteTie.
- `getDistributionType() -> str` — Returns distributionType of the DiscreteTie.
- `getNodeTieByID(id: int) -> NodeTie` — get an existing NodeTie under Discrete Tie by ID
#### `update(name: str, dependentDoF: str) -> None`
Update this DiscreteTie properties.

- `name` — of this DiscreteTie
- `dependentDoF` — of this DiscreteTie

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.DiscreteTieCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of DiscreteTie, based on EntityCollection.

Methods:

- `DiscreteTieCollection() -> None` — Construct a new DiscreteTieCollection.

## `apex.attribute.DisplacementConstraintProperty`
Struct DisplacementConstraintProperty. THIS STRUCT IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Users should be working with classes: ConstraintDisplacement.
Properties: `constrainRotationX`, `constrainRotationY`, `constrainRotationZ`, `constrainTranslationX`, `constrainTranslationY`, `constrainTranslationZ`

Methods:

- `getConstrainRotationX() -> bool`
- `getConstrainRotationY() -> bool`
- `getConstrainRotationZ() -> bool`
- `getConstrainTranslationX() -> bool`
- `getConstrainTranslationY() -> bool`
- `getConstrainTranslationZ() -> bool`
- `setConstrainRotationX(constrainRotationX: bool) -> None`
- `setConstrainRotationY(constrainRotationY: bool) -> None`
- `setConstrainRotationZ(constrainRotationZ: bool) -> None`
- `setConstrainTranslationX(constrainTranslationX: bool) -> None`
- `setConstrainTranslationY(constrainTranslationY: bool) -> None`
- `setConstrainTranslationZ(constrainTranslationZ: bool) -> None`

## `apex.attribute.Elasticity`  (extends `ConstitutiveModel`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.

## `apex.attribute.ElasticityLinear2DAniso`  (extends `Elasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `materialMatrix11`, `materialMatrix12`, `materialMatrix13`, `materialMatrix22`, `materialMatrix23`, `materialMatrix33`

Methods:

- `ElasticityLinear2DAniso(materialMatrix11: float, materialMatrix12: float, materialMatrix13: float, materialMatrix22: float, materialMatrix23: float, materialMatrix33: float) -> None`
- `getMaterialMatrix11() -> float` — Returns Matrix11 of the constitutive model.
- `getMaterialMatrix12() -> float` — Returns Matrix12 of the constitutive model.
- `getMaterialMatrix13() -> float` — Returns Matrix13 of the constitutive model.
- `getMaterialMatrix22() -> float` — Returns Matrix22 of the constitutive model.
- `getMaterialMatrix23() -> float` — Returns Matrix23 of the constitutive model.
- `getMaterialMatrix33() -> float` — Returns Matrix33 of the constitutive model.
#### `update(materialMatrix11: float, materialMatrix12: float, materialMatrix13: float, materialMatrix22: float, materialMatrix23: float, materialMatrix33: float) -> None`
Update properties of this ElasticityLinear2DAniso constitutive model.

- `materialMatrix11` — of this constitutive model
- `materialMatrix12` — of this constitutive model
- `materialMatrix13` — of this constitutive model
- `materialMatrix22` — of this constitutive model
- `materialMatrix23` — of this constitutive model
- `materialMatrix33` — of this constitutive model


## `apex.attribute.ElasticityLinear2DOrtho`  (extends `Elasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `elasticModulus11`, `elasticModulus22`, `poissonRatio`, `shearModulus12`, `shearModulus13`, `shearModulus23`

Methods:

#### `ElasticityLinear2DOrtho(elasticModulus11: float, elasticModulus22: float, shearModulus12: float, shearModulus23: float, shearModulus13: float, poissonRatio: float) -> None`
Create ElasticityLinear2DOrtho constitutive model.

- `elasticModulus11` — of this constitutive model
- `elasticModulus22` — of this constitutive model
- `shearModulus12` — of this constitutive model
- `shearModulus23` — of this constitutive model
- `shearModulus13` — of this constitutive model
- `poissonRatio` — of this constitutive model

- `getElasticModulus11() -> float` — Returns Elastic Modulus 11 of the constitutive model.
- `getElasticModulus22() -> float` — Returns Shear Modulus 22 of the constitutive model.
- `getPoissonRatio() -> float` — Returns Poisson Ratio of the constitutive model.
- `getShearModulus12() -> float` — Returns Shear Modulus 12 of the constitutive model.
- `getShearModulus13() -> float` — Returns Shear Modulus 13 of the constitutive model.
- `getShearModulus23() -> float` — Returns Shear Modulus 23 of the constitutive model.
#### `update(elasticModulus11: float, elasticModulus22: float, shearModulus12: float, shearModulus23: float, shearModulus13: float, poissonRatio: float) -> None`
Update properties of this ElasticityLinear2DOrtho constitutive model.

- `elasticModulus11` — of this constitutive model
- `elasticModulus22` — of this constitutive model
- `shearModulus12` — of this constitutive model
- `shearModulus23` — of this constitutive model
- `shearModulus13` — of this constitutive model
- `poissonRatio` — of this constitutive model


## `apex.attribute.ElasticityLinear3DAniso`  (extends `Elasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `materialMatrix11`, `materialMatrix12`, `materialMatrix13`, `materialMatrix14`, `materialMatrix15`, `materialMatrix16`, `materialMatrix22`, `materialMatrix23`, `materialMatrix24`, `materialMatrix25`, `materialMatrix26`, `materialMatrix33`, `materialMatrix34`, `materialMatrix35`, `materialMatrix36`, `materialMatrix44`, `materialMatrix45`, `materialMatrix46`, `materialMatrix55`, `materialMatrix56`, `materialMatrix66`

Methods:

#### `ElasticityLinear3DAniso(materialMatrix11: float, materialMatrix12: float, materialMatrix13: float, materialMatrix14: float, materialMatrix15: float, materialMatrix16: float, materialMatrix22: float, materialMatrix23: float, materialMatrix24: float, materialMatrix25: float, materialMatrix26: float, materialMatrix33: float, materialMatrix34: float, materialMatrix35: float, materialMatrix36: float, materialMatrix44: float, materialMatrix45: float, materialMatrix46: float, materialMatrix55: float, materialMatrix56: float, materialMatrix66: float) -> None`
Create ElasticityLinear2DOrtho constitutive model.

- `materialMatrix11` — of this constitutive model
- `materialMatrix12` — of this constitutive model
- `materialMatrix13` — of this constitutive model
- `materialMatrix14` — of this constitutive model
- `materialMatrix15` — of this constitutive model
- `materialMatrix16` — of this constitutive model
- `materialMatrix22` — of this constitutive model
- `materialMatrix23` — of this constitutive model
- `materialMatrix24` — of this constitutive model
- `materialMatrix25` — of this constitutive model
- `materialMatrix26` — of this constitutive model
- `materialMatrix33` — of this constitutive model
- `materialMatrix34` — of this constitutive model
- `materialMatrix35` — of this constitutive model
- `materialMatrix36` — of this constitutive model
- `materialMatrix44` — of this constitutive model
- `materialMatrix45` — of this constitutive model
- `materialMatrix46` — of this constitutive model
- `materialMatrix55` — of this constitutive model
- `materialMatrix56` — of this constitutive model
- `materialMatrix66` — of this constitutive model

- `getMaterialMatrix11() -> float` — Returns Matrix11 of the constitutive model.
- `getMaterialMatrix12() -> float` — Returns Matrix12 of the constitutive model.
- `getMaterialMatrix13() -> float` — Returns Matrix13 of the constitutive model.
- `getMaterialMatrix14() -> float` — Returns Matrix14 of the constitutive model.
- `getMaterialMatrix15() -> float` — Returns Matrix15 of the constitutive model.
- `getMaterialMatrix16() -> float` — Returns Matrix16 of the constitutive model.
- `getMaterialMatrix22() -> float` — Returns Matrix22 of the constitutive model.
- `getMaterialMatrix23() -> float` — Returns Matrix23 of the constitutive model.
- `getMaterialMatrix24() -> float` — Returns Matrix24 of the constitutive model.
- `getMaterialMatrix25() -> float` — Returns Matrix25 of the constitutive model.
- `getMaterialMatrix26() -> float` — Returns Matrix26 of the constitutive model.
- `getMaterialMatrix33() -> float` — Returns Matrix33 of the constitutive model.
- `getMaterialMatrix34() -> float` — Returns Matrix34 of the constitutive model.
- `getMaterialMatrix35() -> float` — Returns Matrix35 of the constitutive model.
- `getMaterialMatrix36() -> float` — Returns Matrix36 of the constitutive model.
- `getMaterialMatrix44() -> float` — Returns Matrix44 of the constitutive model.
- `getMaterialMatrix45() -> float` — Returns Matrix45 of the constitutive model.
- `getMaterialMatrix46() -> float` — Returns Matrix46 of the constitutive model.
- `getMaterialMatrix55() -> float` — Returns Matrix55 of the constitutive model.
- `getMaterialMatrix56() -> float` — Returns Matrix56 of the constitutive model.
- `getMaterialMatrix66() -> float` — Returns Matrix66 of the constitutive model.
#### `update(materialMatrix11: float, materialMatrix12: float, materialMatrix13: float, materialMatrix14: float, materialMatrix15: float, materialMatrix16: float, materialMatrix22: float, materialMatrix23: float, materialMatrix24: float, materialMatrix25: float, materialMatrix26: float, materialMatrix33: float, materialMatrix34: float, materialMatrix35: float, materialMatrix36: float, materialMatrix44: float, materialMatrix45: float, materialMatrix46: float, materialMatrix55: float, materialMatrix56: float, materialMatrix66: float) -> None`
Update properties of this ElasticityLinear2DOrtho constitutive model.

- `materialMatrix11` — of this constitutive model
- `materialMatrix12` — of this constitutive model
- `materialMatrix13` — of this constitutive model
- `materialMatrix14` — of this constitutive model
- `materialMatrix15` — of this constitutive model
- `materialMatrix16` — of this constitutive model
- `materialMatrix22` — of this constitutive model
- `materialMatrix23` — of this constitutive model
- `materialMatrix24` — of this constitutive model
- `materialMatrix25` — of this constitutive model
- `materialMatrix26` — of this constitutive model
- `materialMatrix33` — of this constitutive model
- `materialMatrix34` — of this constitutive model
- `materialMatrix35` — of this constitutive model
- `materialMatrix36` — of this constitutive model
- `materialMatrix44` — of this constitutive model
- `materialMatrix45` — of this constitutive model
- `materialMatrix46` — of this constitutive model
- `materialMatrix55` — of this constitutive model
- `materialMatrix56` — of this constitutive model
- `materialMatrix66` — of this constitutive model


## `apex.attribute.ElasticityLinear3DOrtho`  (extends `Elasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `elasticModulus11`, `elasticModulus22`, `elasticModulus33`, `poissonRatio12`, `poissonRatio13`, `poissonRatio23`, `shearModulus12`, `shearModulus13`, `shearModulus23`

Methods:

#### `ElasticityLinear3DOrtho(elasticModulus11: float, elasticModulus22: float, elasticModulus33: float, shearModulus12: float, shearModulus23: float, shearModulus13: float, poissonRatio12: float, poissonRatio23: float, poissonRatio13: float) -> None`
Create ElasticityLinear3DOrtho constitutive model.

- `elasticModulus11` — This define the x direction elastic Modulus
- `elasticModulus22` — This define the Y direction elastic Modulus
- `elasticModulus33` — This define the Z direction elastic Modulus
- `shearModulus12` — This define the xy direction shear Modulus
- `shearModulus23` — This define the yz direction shear Modulus
- `shearModulus13` — This define the xz direction shear Modulus
- `poissonRatio12` — This define the xy direction poisson ratio
- `poissonRatio23` — This define the yz direction poisson ratio
- `poissonRatio13` — This define the xz direction poisson ratio

- `getElasticModulus11() -> float` — Returns ElasticModulus11 of the constitutive model.
- `getElasticModulus22() -> float` — Returns ElasticModulus22 of the constitutive model.
- `getElasticModulus33() -> float` — Returns ElasticModulus33 of the constitutive model.
- `getPoissonRatio12() -> float` — Returns PoissonRatio12 of the constitutive model.
- `getPoissonRatio13() -> float` — Returns PoissonRatio13 of the constitutive model.
- `getPoissonRatio23() -> float` — Returns PoissonRatio23 of the constitutive model.
- `getShearModulus12() -> float` — Returns ShearModulus12 of the constitutive model.
- `getShearModulus13() -> float` — Returns ShearModulus13 of the constitutive model.
- `getShearModulus23() -> float` — Returns ShearModulusc23 of the constitutive model.
#### `update(elasticModulus11: float, elasticModulus22: float, elasticModulus33: float, shearModulus12: float, shearModulus23: float, shearModulus13: float, poissonRatio12: float, poissonRatio23: float, poissonRatio13: float) -> None`
Update properties of this ElasticityLinear3DOrtho constitutive model.

- `elasticModulus11` — This define the x direction elastic Modulus
- `elasticModulus22` — This define the Y direction elastic Modulus
- `elasticModulus33` — This define the Z direction elastic Modulus
- `shearModulus12` — This define the xy direction shear Modulus
- `shearModulus23` — This define the yz direction shear Modulus
- `shearModulus13` — This define the xz direction shear Modulus
- `poissonRatio12` — This define the xy direction poisson ratio
- `poissonRatio23` — This define the yz direction poisson ratio
- `poissonRatio13` — This define the xz direction poisson ratio


## `apex.attribute.ElasticityLinear3DTransvIso`  (extends `Elasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `elasticModulusAxial`, `elasticModulusPlan`, `poissonRatioxy`, `poissonRatioyz`, `shearModulusxy`

Methods:

#### `ElasticityLinear3DTransvIso(elasticModulusAxial: float, elasticModulusPlan: float, shearModulusxy: float, poissonRatioxy: float, poissonRatioyz: float) -> None`
Create ElasticityLinear3DTransvIso constitutive model.

- `elasticModulusAxial` — The Axis Direction elastic Modulus. Used axial for x Orientation.
- `elasticModulusPlan` — The in Plane elastic Modulus. Used in plane for y and z Orientation.
- `shearModulusxy` — The shear Modulus in XY direction. Used axial for x Orientation. Used in plane for y and z Orientation.
- `poissonRatioxy` — Defiend the poisson Ratio in xy direction. Used axial for x Orientation. Used in plane for y and z Orientation.
- `poissonRatioyz` — Defiend the poisson Ratio in yz direction. Used axial for x Orientation. Used in plane for y and z Orientation.

- `getElasticModulusAxial() -> float` — Returns ElasticModulus11 of the constitutive model.
- `getElasticModulusPlan() -> float` — Returns ElasticModulus22 of the constitutive model.
- `getPoissonRatioxy() -> float` — Returns ShearModulus12 of the constitutive model.
- `getPoissonRatioyz() -> float` — Returns ShearModulusc23 of the constitutive model.
- `getShearModulusxy() -> float` — Returns ElasticModulus33 of the constitutive model.
#### `update(elasticModulusAxial: float, elasticModulusPlan: float, shearModulusxy: float, poissonRatioxy: float, poissonRatioyz: float) -> None`
Update properties of this ElasticityLinear3DTransvIso constitutive model.

- `elasticModulusAxial` — The Axis Direction elastic Modulus. Used axial for x Orientation.
- `elasticModulusPlan` — The in Plane elastic Modulus. Used in plane for y and z Orientation.
- `shearModulusxy` — The shear Modulus in XY direction. Used axial for x Orientation. Used in plane for y and z Orientation.
- `poissonRatioxy` — Defiend the poisson Ratio in xy direction. Used axial for x Orientation. Used in plane for y and z Orientation.
- `poissonRatioyz` — Defiend the poisson Ratio in yz direction. Used axial for x Orientation. Used in plane for y and z Orientation.


## `apex.attribute.ElasticityLinearIso`  (extends `Elasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `elasticModulus`, `poissonRatio`, `shearModulus`

Methods:

#### `ElasticityLinearIso(elasticModulus: float, shearModulus: float, poissonRatio: float) -> None`
Create ElasticityLinearIso constitutive model.

- `elasticModulus` — of this constitutive model
- `shearModulus` — of this constitutive model
- `poissonRatio` — of this constitutive model

- `getElasticModulus() -> float` — Returns Elastic Modulus of the material.
- `getPoissonRatio() -> float` — Returns Poisson Ratio of the material.
- `getShearModulus() -> float` — Returns Shear Modulus of the material.
#### `update(elasticModulus: float, shearModulus: float, poissonRatio: float) -> None`
Update properties of this ElasticityLinearIso constitutive model.

- `elasticModulus` — of this constitutive model
- `shearModulus` — of this constitutive model
- `poissonRatio` — of this constitutive model


## `apex.attribute.Failure`  (extends `ConstitutiveModel`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.

## `apex.attribute.Failure2DAniso`  (extends `Failure`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `compression`, `shear`, `tension`

Methods:

- `Failure2DAniso(tension: float, compression: float, shear: float) -> None`
- `getCompression() -> float` — Returns The compression Strength of the material.
- `getShear() -> float` — Returns The shear Strength of the material.
- `getTension() -> float` — Returns The Tensile Strength of the material.
#### `update(tension: float, compression: float, shear: float) -> None`
Used to update a Failure2DAniso object.

- `tension` — The Tensile Strength of the material
- `compression` — The compression Strength of the material
- `shear` — The shear Strength of the material


## `apex.attribute.Failure2DOrth`  (extends `Failure`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `compressionX`, `compressionY`, `inPlaneShear`, `tensionX`, `tensionY`

Methods:

- `Failure2DOrth(tensionX: float, tensionY: float, compressionX: float, compressionY: float, inPlaneShear: float) -> None`
- `getCompressionX() -> float` — Returns The X-axial compression Strength of the material.
- `getCompressionY() -> float` — Returns The Y-axial compression Strength of the material.
- `getInPlaneShear() -> float` — Returns The inPlane Shear Strength of the material.
- `getTensionX() -> float` — Returns The X-axial Tensile Strength of the material.
- `getTensionY() -> float` — Returns The Y-axial Tensile Strength of the material.
#### `update(tensionX: float, tensionY: float, compressionX: float, compressionY: float, inPlaneShear: float) -> None`
Used to update a Failure2DOrth object.

- `tensionX` — The X-axial Tensile Strength of the material
- `tensionY` — The Y-axial Tensile Strength of the material
- `compressionX` — The X-axial compression Strength of the material
- `compressionY` — The Y-axial compression Strength of the material
- `inPlaneShear` — The inPlane Shear Strength of the material


## `apex.attribute.Failure3DOrth`  (extends `Failure`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `axisCompressive`, `axisTension`, `inPlaneCompressive`, `inPlaneTension`, `transverseShear`

Methods:

- `Failure3DOrth(axisTension: float, axisCompressive: float, inPlaneTension: float, inPlaneCompressive: float, transverseShear: float) -> None`
- `getAxisCompressive() -> float` — Returns the axis Compressive Strength of the material.
- `getAxisTension() -> float` — Returns the axial Tensile Strength of the material.
- `getInPlaneCompressive() -> float` — Returns the in Plane compressive Strength of the material.
- `getInPlaneTension() -> float` — Returns the in Plane Tensile Strength of the material.
- `getTransverseShear() -> float` — Returns the transverse Shear Strength of the material.
#### `update(axisTension: float, axisCompressive: float, inPlaneTension: float, inPlaneCompressive: float, transverseShear: float) -> None`
Used to update a Failure3DOrth object.

- `axisTension` — The axial Tensile Strength of the material
- `axisCompressive` — The axis Compressive Strength of the material
- `inPlaneTension` — The in Plane Tensile Strength of the material
- `inPlaneCompressive` — The in Plane compressive Strength of the material
- `transverseShear` — The transverse Shear Strength of the material


## `apex.attribute.Failure3DTransvIso`  (extends `Failure`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `axisCompressive`, `axisTension`, `inPlaneCompressive`, `inPlaneTension`, `transverseShear`

Methods:

- `Failure3DTransvIso(axisTension: float, axisCompressive: float, inPlaneTension: float, inPlaneCompressive: float, transverseShear: float) -> None`
- `getAxisCompressive() -> float` — Returns the axis Compressive Strength of the material.
- `getAxisTension() -> float` — Returns the axial Tensile Strength of the material.
- `getInPlaneCompressive() -> float` — Returns the in Plane compressive Strength of the material.
- `getInPlaneTension() -> float` — Returns the in Plane Tensile Strength of the material.
- `getTransverseShear() -> float` — Returns the transverse Shear Strength of the material.
#### `update(axisTension: float, axisCompressive: float, inPlaneTension: float, inPlaneCompressive: float, transverseShear: float) -> None`
Used to update a Failure3DTransvIso object.

- `axisTension` — The axial Tensile Strength of the material
- `axisCompressive` — The axis Compressive Strength of the material
- `inPlaneTension` — The in Plane Tensile Strength of the material
- `inPlaneCompressive` — The in Plane compressive Strength of the material
- `transverseShear` — The transverse Shear Strength of the material


## `apex.attribute.FailureIso`  (extends `Failure`)
the base Class Used to define material failure behavior and parameters.
Properties: `compression`, `shear`, `tension`

Methods:

- `FailureIso(tension: float, compression: float, shear: float) -> None`
- `getCompression() -> float` — Returns The compression Strength of the material.
- `getShear() -> float` — Returns The shear Strength of the material.
- `getTension() -> float` — Returns The Tensile Strength of the material.
#### `update(tension: float, compression: float, shear: float) -> None`
Used to update a FailureIso object.

- `tension` — The Tensile Strength of the material
- `compression` — The compression Strength of the material
- `shear` — The shear Strength of the material


## `apex.attribute.Fastener`  (extends `Connector`)

## `apex.attribute.FastenerCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `FastenerCollection() -> None` — Construct a newFastenerCollection.

## `apex.attribute.FastenerRepProperties`  (extends `ConnectorDiscreteProperty`)
Class FastenerRepProperties. The FastenerRepProperties class holds the properties for Fastener.
Properties: `diameter`, `embedded`, `flagOfCoordinateSystem`, `id`, `lengthWithCoincidentGrids`, `mass`, `referenceTemperature`, `rotationalStiffnessX`, `rotationalStiffnessY`, `rotationalStiffnessZ`, `stiffnessCoordinateSystem`, `structuralDamping`, `thermalExpansionCoefficient`, `transverseStiffnessX`, `transverseStiffnessY`, `transverseStiffnessZ`, `userDefinedStiffnessCoordinateSystem`

Methods:

- `getDiameter() -> float` — Gets the diameter of fastener.
- `getEmbedded() -> bool` — Returns embedded of the fastener.
- `getFlagOfCoordinateSystem() -> apex.attribute.FlagOfCoordinateSystem` — Gets the flag of coordinate system either in "Relative" or "Absolute".
- `getId() -> int` — Returns id of the fastener.
- `getLengthWithCoincidentGrids() -> float` — Gets the length with coincident grids.
- `getMass() -> float` — Gets the mass of fastener.
- `getReferenceTemperature() -> float` — Gets the reference temperature of Gets the fastener.
- `getRotationalStiffnessX() -> float` — Gets the rotational stiffness about x axis.
- `getRotationalStiffnessY() -> float` — Gets the rotational stiffness about y axis.
- `getRotationalStiffnessZ() -> float` — Gets the rotational stiffness about z axis.
- `getStiffnessCoordinateSystem() -> apex.attribute.FastenerStiffnessCoordinateSystem` — Gets the element stiffness coordinate system type. Optional numeric argument indicate the element stiffness coordinate system, which could be one of values: Global, UserDefined, MinusOne, Unset,.
- `getStructuralDamping() -> float` — Gets the structural damping of fastener.
- `getThermalExpansionCoefficient() -> float` — Gets the thermal expansion coefficient for Gets the fastener.
- `getTransverseStiffnessX() -> float` — Gets the transverse stiffness along x axis.
- `getTransverseStiffnessY() -> float` — Gets the transverse stiffness along y axis.
- `getTransverseStiffnessZ() -> float` — Gets the transverse stiffness along z axis.
- `getUserDefinedStiffnessCoordinateSystem() -> apex.construct.CoordinateSystem` — Gets user defined element stiffness coordinate system, which takes effect only when the argument"stiffnessCoordinateSystem" is set as "userDefined.
#### `update(id: int, diameter: float, transverseStiffnessX: float, transverseStiffnessY: float, transverseStiffnessZ: float, rotationalStiffnessX: float, rotationalStiffnessY: float, rotationalStiffnessZ: float, mass: float, structuralDamping: float, thermalExpansionCoefficient: float, referenceTemperature: float, lengthWithCoincidentGrids: float, flagOfCoordinateSystem: apex.attributes.FlagOfCoordinateSystem, userDefinedStiffnessCoordinateSystem: apex.construct.CoordinateSystem, stiffnessCoordinateSystem: apex.attributes.FastenerStiffnessCoordinateSystem, name: str, description: str) -> None`
Update the property of fastener.

- `id` — update the id of this connector property.
- `diameter` — Update the diameter of fastener.
- `transverseStiffnessX` — Update the transverse stiffness along x axis.
- `transverseStiffnessY` — Update the transverse stiffness along y axis.
- `transverseStiffnessZ` — Update the transverse stiffness along z axis.
- `rotationalStiffnessX` — Update the rotational stiffness about x axis.
- `rotationalStiffnessY` — Update The rotational stiffness about y axis.
- `rotationalStiffnessZ` — Update The rotational stiffness about z axis.
- `mass` — Update the mass of fastener.
- `structuralDamping` — Update the structural damping of fastener.
- `thermalExpansionCoefficient` — Update the thermal expansion coefficient for the fastener.
- `referenceTemperature` — Update the reference temperature of the fastener.
- `lengthWithCoincidentGrids` — Update the length with coincident grids.
- `flagOfCoordinateSystem` — Update the flag of coordinate system either in "Relative" or "Absolute".
- `userDefinedStiffnessCoordinateSystem` — Update user defined element stiffness coordinate system, which takes effect only when the argument"stiffnessCoordinateSystem" is set as "userDefined.
- `stiffnessCoordinateSystem` — Update optional numeric argument indicate the element stiffness coordinate system, which could be one of values: Global, UserDefined, MinusOne, Unset.
- `name` — update the name of this connector property.
- `description` — update the description of this connector property.

One or more properties may be updated in each call to update().


## `apex.attribute.FastenerRepPropertiesCollection`  (extends `EntityCollection`)
Iterable collection of FastenerRepProperties, based on EntityCollection.

Methods:

- `FastenerRepPropertiesCollection() -> None` — Construct a new FastenerRepPropertiesCollection.

## `apex.attribute.FlexibleLink`  (extends `Connector`)

## `apex.attribute.FlexibleLinkCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `FlexibleLinkCollection() -> None` — Construct a new FlexibleLinkCollection.

## `apex.attribute.FlexibleLinkRepProperties`  (extends `ConnectorDiscreteProperty`)
Class FlexibleLinkRepProperties. The class FlexibleLinkRepProperties holds the properties of FlexibleLink connector.
Properties: `diameter`, `linkMaterial`

Methods:

- `getDiameter() -> float` — The diameter of the FlexibleLink connector.
- `getLinkMaterial() -> Material` — The material assigned to the FlexibleLink connector.
#### `update(diameter: float, linkMaterial: Material) -> None`
Update this connector properties.

- `diameter` — Update the diameter of this connectorProperty.
- `linkMaterial` — Update the linkMaterial of this connectorProperty.

One or more properties may be updated in each call to update().


## `apex.attribute.Gap`  (extends `Connector`)

## `apex.attribute.GapCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `GapCollection() -> None` — Construct a new GapCollection.

## `apex.attribute.GapRepProperties`  (extends `ConnectorDiscreteProperty`)
Class GapRepProperties. The class GapRepProperties holds the properties of Gap connector.
Properties: `closedStiffness`, `initialOpening`, `kineticFriction`, `openStiffness`, `preload`, `staticFriction`, `transverseStiffness`

Methods:

- `getClosedStiffness() -> float` — Axial stiffness for the closed gap.
- `getInitialOpening() -> float` — The initial gap opening.
- `getKineticFriction() -> float` — Coefficient of kinetic friction.
- `getOpenStiffness() -> float` — Axial stiffness for the open gap.
- `getPreload() -> float` — The preload applied on the gap.
- `getStaticFriction() -> float` — Coefficient of static friction.
- `getTransverseStiffness() -> float` — Transverse stiffness when the gap is closed.
#### `update(initialOpening: float, preload: float, closedStiffness: float, openStiffness: float, transverseStiffness: float, staticFriction: float, kineticFriction: float) -> None`
Update this connector properties.

- `initialOpening` — Update the initialOpening of this connectorProperty.
- `preload` — Update the preload of this connectorProperty.
- `closedStiffness` — Update the closedStiffness of this connectorProperty.
- `openStiffness` — Update the openStiffness of this connectorProperty.
- `transverseStiffness` — Update the transverseStiffness of this connectorProperty.
- `staticFriction` — Update the staticFriction of this connectorProperty.
- `kineticFriction` — Update the kineticFriction of this connectorProperty.

One or more properties may be updated in each call to update().


## `apex.attribute.Interaction`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
An interaction, is the pair of bodies, plus the Geometric attributes of the interaction, which covers rules for how these bodies can become in contact, and the Physical properties, which covers how they behave once they are in contact.
Properties: `activeRep`, `body1Property`, `body2Property`, `contactBody1`, `contactBody2`, `targetSide1`, `targetSide2`

Methods:

#### `createInteractionRep(name: str, description: str, id: int, interactionType: apex.attribute.InteractionType, interactionPropertyGeometric: apex.attribute.InteractionPropertyGeometric, interactionPropertyPhysical: apex.attribute.InteractionPropertyPhysical, allowSelfContactSide1: bool, allowSelfContactSide2: bool) -> apex.attribute.InteractionRep`
Create an interaction rep.

- `name` — Optional-name of interaction rep
- `description` — Optional - description of interaction rep.
- `id` — Optional-id of interaction rep. If omits, the system will automatically assign the ID.
- `interactionType` — Interaction type of the interaction object: Glue, General Contact or Self Contact.
- `interactionPropertyGeometric` — Interaction Geometric Properties.
- `interactionPropertyPhysical` — Interaction Physical Properties.
- `allowSelfContactSide1` — Optional - Boolean to choose self Contact for primary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.
- `allowSelfContactSide2` — Optional - Boolean to choose self Contact for secondary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.

- `getActiveRep() -> apex.attribute.InteractionRep` — Gets The active interaction rep of current interaction.
- `getBody1Property() -> apex.attribute.ContactBodyProperty` — Gets Interaction body property of side1.
- `getBody2Property() -> apex.attribute.ContactBodyProperty` — Gets Interaction body property of side2.
- `getContactBodies1() -> apex.attribute.ContactBodyCollection` — Gets Primary Side Contact Bodies of an interaction pair.
- `getContactBodies2() -> apex.attribute.ContactBodyCollection` — Gets Secondary side Contact Bodies of an interaction pair.
- `getTargetSide1() -> apex.EntityCollection` — Gets Primary side of an interaction pair.
- `getTargetSide2() -> apex.EntityCollection` — Gets Secondary side of an interaction pair.
#### `update(name: str, description: str, targetSide1: apex.EntityCollection, targetSide2: apex.EntityCollection, body1Property: apex.attribute.ContactBodyProperty, body2Property: apex.attribute.ContactBodyProperty) -> Interaction`
update the interaction object.

- `name` — Optional name for the interaction. If omitted, Apex will provide a default name by concatenating the prefix 'Interaction' with the lowest possible integer required to ensure name uniqueness within the scope of the Model.
- `description` — Optional string providing a description for the Interaction. If omitted, the description will be blank
- `targetSide1` — A collection of entities that represent the first side (Side 1) of the Interaction. The collection may contain, - geometry Solids, Surfaces, Cells and Faces - Solid and Surface MeshBodies - arbitrary sets of solid elements/faces and shell elements
- `targetSide2` — A collection of entities that represent the second side (Side 2) of the Interaction. The collection may contain, - geometry Solids, Surfaces, Cells and Faces - Solid and Surface MeshBodies - arbitrary sets of solid elements/faces and shell elements
- `body1Property` — Optional - Contact body property of side 1 side of interaction pair. If omits, the default contact body properties will be used.
- `body2Property` — Optional - Contact body property of side 1 side of interaction pair. If omits, the default contact body properties will be used.


## `apex.attribute.InteractionCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `InteractionCollection() -> None` — Construct a new InteractionCollection.

## `apex.attribute.InteractionPropertyGeometric`  (extends `Entity`)
Interaction Geometric Properties, it is various properties for Interaction Pairs.
Properties: `adjustedMagnitude`, `adjustedSecondaryBodyClearance`, `adjustedSecondaryBodyInterferenceFit`, `allowSeparation`, `biasFactor`, `breakingGlueCriteria`, `clearanceSearchTolerance`, `contactSearchOrder`, `contactTolerance`, `contactToleranceCalculationMethod`, `coordinateSystemWithVector`, `cosinesVector`, `delayedSlideOff`, `flexibleGlue`, `hardSoftRatio`, `id`, `ignoreShellThicknessSide1`, `ignoreShellThicknessSide2`, `initialClearance`, `interferenceClosure`, `interferenceFit`, `interferenceFitMethod`, `name`, `normalPenaltyFactor`, `normalStiffness`, `penetrationDistance`, `penetrationSearchTolerance`, `retainMoment`, `scaleCenter`, `scaleFactorVector`, `shellLayerSide1`, `shellLayerSide2`, `slideOffDistance`, `slipDistance`, `stepGlue`, `stressFreeInitialContact`, `tangentPenaltyFactor`, `tangentStiffness`

Methods:

- `getAdjustedMagnitude() -> float` — Gets Optional - adjusted magnitude. It is only available when initialClearance is true.
- `getAdjustedSecondaryBodyClearance() -> bool` — Gets Optional to define which Contact body to be adjust for Initial gap/overlap. True: Secondary body False: Primary body It is only available when initialClearance is true.
- `getAdjustedSecondaryBodyInterferenceFit() -> bool` — Gets Optional to define which Contact body to be adjust for interference fit. True: Secondary body False: Primary body.
- `getAllowSeparation() -> bool` — Gets Optional - enable to allow glue separation during simulation. Omits it if the interaction type is contact.
- `getBiasFactor() -> float` — Gets Optional - Contact tolerance bias factor.
- `getBreakingGlueCriteria() -> bool` — Gets Optional - enable to use breaking blue parameters to define separation when allowSeparation = True. Omits it if the interaction type is contact.
- `getClearanceSearchTolerance() -> float` — Gets Optional - Search tolerance of initial gap or overlap. It is only available when initialClearance is true.
- `getContactSearchOrder() -> apex.attribute.ContactSearchOrder` — Gets Optional - contact search order for node to segment contact method.
- `getContactTolerance() -> float` — Gets An optional distance tolerance value (default =0.005m) used to determine the subset of elements specified in targetSide1 and targetSide2 that will actually be glued/contact during the simulations.
- `getContactToleranceCalculationMethod() -> apex.AutoManual` — Gets An optional argument (default True) that controls whether the ContactTolerance should be calculated automatically by the system or defined manually via this method. The Automatic option works well in most cases and should only be replaced with a manual value for complex geometry where the automatic value is observed to produce unwanted results.
- `getCoordinateSystemWithVector() -> apex.construct.CoordinateSystem` — Gets Optional - Coordinate system to define the interference fit vector. The option will be available when InterferenceFitMethod = UserDirection or ScaleFactor.
- `getCosinesVector() -> [float]` — Gets Optional - Cosines Vector[a1,a2,a3] of the interference fit direction. a1 will be the angle of x axis; a2 will be the angle of y axis; a3 will be the angle of z axis. The option will be available when InterferenceFitMethod = UserDirection.
- `getDelayedSlideOff() -> bool` — Gets Optional - Activate/Deactivate delay-slide off.
- `getFlexibleGlue() -> bool` — Gets Optional - Activate/Deactivate Flexible Glue. Omits it if the interaction type is contact.
- `getHardSoftRatio() -> float` — Gets Optional - Hard soft ratio of the contact pair. This argument is only available for node to segment contact method, which will be skipped in segment to segment method.
- `getId() -> int` — Gets ID of Interaction geometric properties.
- `getIgnoreShellThicknessSide1() -> bool` — Gets Consider or ignore shell thickness during detection of contact side 1.
- `getIgnoreShellThicknessSide2() -> bool` — Gets Consider or ignore shell thickness during detection of contact side 2.
- `getInitialClearance() -> bool` — Gets Optional - active to Adjust Initial gap or overlap.
- `getInterferenceClosure() -> float` — Gets Optional - Adjust gap(>0.0) or overlap(<0.0) based on the value The option will be available when InterferenceFitMethod = NormalDirection or UserDireaction.
- `getInterferenceFit() -> bool` — Gets Optional - active to Adjust Interference Fit.
- `getInterferenceFitMethod() -> apex.attribute.InterferenceFitMethod` — Gets Optional - Method to define Interference Fit.
- `getName() -> str` — Gets Name of Interaction geometric properties.
- `getNormalPenaltyFactor() -> float` — Gets Optional - Augmented Lagrange penalty factor in normal direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getNormalStiffness() -> float` — Gets Optional - Normal Stiffness for flexible glue. Omits it if the interaction type is contact.
- `getPenetrationDistance() -> float` — Gets Optional - Penetration distance beyond which an augmentation will be applied The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getPenetrationSearchTolerance() -> float` — Gets Optional - Penetration Search Tolerance. The option will be available when InterferenceFitMethod = Automatic.
- `getRetainMoment() -> bool` — Gets Optional - enable to retain moment for shell glue. Omits it if the interaction type is contact.
- `getScaleCenter() -> [float]` — Gets Optional - Scale Center[x,y,z] with interference fit. The option will be available when InterferenceFitMethod = ScaleCenter.
- `getScaleFactorVector() -> [float]` — Gets Optional - Scale Factor Vector [a1,a2,a3] of the interference fit. The option will be available when InterferenceFitMethod = ScaleFactor.
- `getShellLayerSide1() -> apex.attribute.ShellLayer` — Gets Shell layer to be used for contact detection in side 1. In segment to segment contact method, it only supports "ShellLayer = TopAndButtom", skip other shell layer method. In node to segment contact method, it supports all 3 options.
- `getShellLayerSide2() -> apex.attribute.ShellLayer` — Gets Shell layer to be used for contact detection in side 2. In segment to segment contact method, it only supports "ShellLayer = TopAndButtom", skip other shell layer method. In node to segment contact method, it supports all 3 options.
- `getSlideOffDistance() -> float` — Gets Optional - Slide Off Distance which is only available when "delayedSlideOff = True". Otherwise,it will be skipped.
- `getSlipDistance() -> float` — Gets Optional - Maximum allowable slip distance for sticking, beyond it there is no sticking, only sliding exists The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getStepGlue() -> bool` — Gets Optional- Step Glue for Large Displacement and Rotation. Omits it if the interaction type is contact.
- `getStressFreeInitialContact() -> bool` — Gets Optional - Activate/Deactivate stress-free initial contact can be obtained.
- `getTangentPenaltyFactor() -> float` — Gets Optional - Augmented Lagrange penalty factor in tangent direction The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `getTangentStiffness() -> float` — Gets Optional - Tangent Stiffness for flexible glue. Omits it if the interaction type is contact.
#### `update(contactToleranceCalculationMethod: apex.AutoManual, contactTolerance: float, biasFactor: float, shellLayerSide1: apex.attribute.ShellLayer, shellLayerSide2: apex.attribute.ShellLayer, ignoreShellThicknessSide1: bool, ignoreShellThicknessSide2: bool, normalPenaltyFactor: float, tangentPenaltyFactor: float, penetrationDistance: float, slipDistance: float, contactSearchOrder: apex.attribute.ContactSearchOrder, hardSoftRatio: float, stressFreeInitialContact: bool, delayedSlideOff: bool, slideOffDistance: float, retainMoment: bool, allowSeparation: bool, breakingGlueCriteria: bool, stepGlue: bool, flexibleGlue: bool, normalStiffness: float, tangentStiffness: float, interferenceFit: bool, interferenceFitMethod: apex.attribute.InterferenceFitMethod, interferenceClosure: float, cosinesVector: [float], scaleCenter: [float], scaleFactorVector: [float], penetrationSearchTolerance: float, coordinateSystemWithVector: apex.construct.CoordinateSystem, adjustedSecondaryBodyInterferenceFit: bool, initialClearance: bool, clearanceSearchTolerance: float, adjustedMagnitude: float, adjustedSecondaryBodyClearance: bool, id: int, name: str) -> None`
Update interaction geometric properties.

- `contactToleranceCalculationMethod` — An optional argument (default True) that controls whether the ContactTolerance should be calculated automatically by the system or defined manually via this method. The Automatic option works well in most cases and should only be replaced with a manual value for complex geometry where the automatic value is observed to produce unwanted results.
- `contactTolerance` — An optional distance tolerance value (default =0.005m) used to determine the subset of elements specified in targetSide1 and targetSide2 that will actually be glued/contact during the simulations.
- `biasFactor` — Optional - Contact tolerance bias factor
- `shellLayerSide1` — Shell layer to be used for contact detection in side 1. In segment to segment contact method, it only supports "ShellLayer = TopAndButtom", skip other shell layer method. In node to segment contact method, it supports all 3 options.
- `shellLayerSide2` — Shell layer to be used for contact detection in side 2. In segment to segment contact method, it only supports "ShellLayer = TopAndButtom", skip other shell layer method. In node to segment contact method, it supports all 3 options.
- `ignoreShellThicknessSide1` — Consider or ignore shell thickness during detection of contact side 1
- `ignoreShellThicknessSide2` — Consider or ignore shell thickness during detection of contact side 2
- `normalPenaltyFactor` — Optional - Augmented Lagrange penalty factor in normal direction. The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `tangentPenaltyFactor` — Optional - Augmented Lagrange penalty factor in tangent direction The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `penetrationDistance` — Optional - Penetration distance beyond which an augmentation will be applied The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `slipDistance` — Optional - Maximum allowable slip distance for sticking, beyond it there is no sticking, only sliding exists The argument is only available for segment to segment method, which will be skipped in node to segment method.
- `contactSearchOrder` — Optional - contact search order for node to segment contact method.
- `hardSoftRatio` — Optional - Hard soft ratio of the contact pair. This argument is not available for node to segment contact method, which will be skipped in segment to segment method.
- `stressFreeInitialContact` — Optional - Activate/Deactivate stress-free initial contact can be obtained
- `delayedSlideOff` — Optional - Activate/Deactivate delay-slide off
- `slideOffDistance` — Optional - Slide Off Distance which is only available when "delayedSlideOff = True". Otherwise,it will be skipped.
- `retainMoment` — Optional - enable to retain moment for shell glue. Omits it if the interaction type is contact.
- `allowSeparation` — Optional - enable to allow glue separation during simulation. Omits it if the interaction type is contact.
- `breakingGlueCriteria` — Optional - enable to use breaking blue parameters to define separation when allowSeparation = True. the system will use the breaking glue separation criteria defined in physical property. If it is false when allowSeparation = True, the system will use standard separation criteria defined in physical property. Omits it if the interaction type is contact.
- `stepGlue` — Optional- Step Glue for Large Displacement and Rotation. Omits it if the interaction type is contact.
- `flexibleGlue` — Optional - Activate/Deactivate Flexible Glue. Omits it if the interaction type is contact.
- `normalStiffness` — Optional - Normal Stiffness for flexible glue. Omits it if the interaction type is contact.
- `tangentStiffness` — Optional - Tangent Stiffness for flexible glue. Omits it if the interaction type is contact.
- `interferenceFit` — Optional - active to Adjust Interference Fit
- `interferenceFitMethod` — Optional - Method to define Interference Fit.
- `interferenceClosure` — Optional - Adjust gap(>0.0) or overlap(<0.0) based on the value The option will be available when InterferenceFitMethod = NormalDirection or UserDireaction. If both interferenceClosure and interferenceClosureVariable are defined, the interferenceClosureVariable will be used in priority.
- `cosinesVector` — Optional - Cosines Vector[a1,a2,a3] of the interference fit direction. a1 will be the angle of x axis; a2 will be the angle of y axis; a3 will be the angle of z axis. The option will be available when InterferenceFitMethod = UserDirection.
- `scaleCenter` — Optional - Scale Center[x,y,z] with interference fit. The option will be available when InterferenceFitMethod = ScaleCenter.
- `scaleFactorVector` — Optional - Scale Factor Vector [a1,a2,a3] of the interference fit. The option will be available when InterferenceFitMethod = ScaleFactor.
- `penetrationSearchTolerance` — Optional - Penetration Search Tolerance. The option will be available when InterferenceFitMethod = Automatic.
- `coordinateSystemWithVector` — Optional - Coordinate system to define the interference fit vector. The option will be available when InterferenceFitMethod = UserDirection or ScaleFactor
- `adjustedSecondaryBodyInterferenceFit` — Optional to define which Contact body to be adjust for interference fit. True: Secondary body False: Primary body
- `initialClearance` — Optional - active to Adjust Initial gap or overlap
- `clearanceSearchTolerance` — Optional - Search tolerance of initial gap or overlap. It is only available when initialClearance is true.
- `adjustedMagnitude` — Optional - adjusted magnitude. It is only available when initialClearance is true.
- `adjustedSecondaryBodyClearance` — Optional to define which Contact body to be adjust for Initial gap/overlap. True: Secondary body False: Primary body It is only available when initialClearance is true.
- `id` — ID of Interaction geometric properties.
- `name` — Optional-name of interaction geometric properties.


## `apex.attribute.InteractionPropertyPhysical`  (extends `Entity`)
Interaction Physical Properties, it is various properties for Interaction Pairs.
Properties: `exponent1`, `exponent2`, `frictionCoefficient`, `frictionStressLimit`, `id`, `maxNormalStress`, `maxTangentStress`, `name`, `separationForce`, `separationStress`

Methods:

- `getExponent1() -> float` — Gets Optional - Exponent of Max Normal Stress. It is only available when breakingGlueCriteria = True in InteractionPropertyGeometric. Omits it if the interaction type is contact.
- `getExponent2() -> float` — Gets Optional - Exponent of Max Tangent Stress. It is only available when breakingGlueCriteria = True in InteractionPropertyGeometric. Omits it if the interaction type is contact.
- `getFrictionCoefficient() -> float` — Gets Optional - Friction Coefficient of the contact pair.
- `getFrictionStressLimit() -> float` — Gets Optional - Friction stress limit of the contact pair.
- `getId() -> int` — Gets ID of interaction physical properties.
- `getMaxNormalStress() -> float` — Gets Optional - it is only available when breakingGlueCriteria = True in InteractionPropertyGeometric. Omits it if the interaction type is contact.
- `getMaxTangentStress() -> float` — Gets Optional - it is only available when breakingGlueCriteria = True in InteractionPropertyGeometric. Omits it if the interaction type is contact.
- `getName() -> str` — Gets Name of interaction physical properties.
- `getSeparationForce() -> float` — Gets Optional - max force of separation, which is only available when separation method define in scenario is based on "Force". Otherwise,it will be skipped.
- `getSeparationStress() -> float` — Gets Optional - max stress of separation, which is only available when separation method define in scenario is based on "Stress". Otherwise,it will be skipped.
#### `update(frictionCoefficient: float, frictionStressLimit: float, maxNormalStress: float, maxTangentStress: float, exponent1: float, exponent2: float, separationForce: float, separationStress: float, id: int, name: str) -> None`
Update interaction physical properties.

- `frictionCoefficient` — Optional - Friction Coefficient of the contact pair
- `frictionStressLimit` — Optional - Friction stress limit of the contact pair
- `maxNormalStress` — Optional - it is only available when breakingGlueCriteria = True in InteractionPropertyGeometric. Omits it if the interaction type is contact.
- `maxTangentStress` — Optional - it is only available when breakingGlueCriteria = True in InteractionPropertyGeometric. Omits it if the interaction type is contact.
- `exponent1` — Optional - Exponent of Max Normal Stress. It is only available when maxNormalStress is defined. Omits it if the interaction type is contact.
- `exponent2` — Optional - Exponent of Max Tangent Stress. It is only available when maxTangentStress is defined. Omits it if the interaction type is contact.
- `separationForce` — Optional - max force of separation, which is only available when separation method define in scenario is based on "Force". Otherwise,it will be skipped.
- `separationStress` — Optional - max stress of separation, which is only available when separation method define in scenario is based on "Stress". Otherwise,it will be skipped.
- `id` — ID of interaction physical properties
- `name` — Optional - name of interaction physical properties.


## `apex.attribute.InteractionRep`  (extends `Entity`, `IName`)
A class to represent Interaction Rep. In current release, only single interaction rep is available for an interaction.
Properties: `allowSelfContactSide1`, `allowSelfContactSide2`, `id`, `interactionPropertyGeometric`, `interactionPropertyPhysical`, `interactionType`

Methods:

- `getAllowSelfContactSide1() -> bool` — Optional - Boolean to choose self Contact for primary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.
- `getAllowSelfContactSide2() -> bool` — Optional - Boolean to choose self Contact for secondary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.
- `getId() -> int` — Gets ID of this interaction rep.
- `getInteractionPropertyGeometric() -> apex.attribute.InteractionPropertyGeometric` — Gets Interaction Geometric Properties.
- `getInteractionPropertyPhysical() -> apex.attribute.InteractionPropertyPhysical` — Gets Interaction Physical Properties.
- `getInteractionType() -> apex.attribute.InteractionType` — Gets Interaction type of the interaction object: Glue, General Contact or Self Contact.
#### `update(name: str, description: str, id: int, interactionType: apex.attribute.InteractionType, interactionPropertyGeometric: InteractionPropertyGeometric, interactionPropertyPhysical: InteractionPropertyPhysical, allowSelfContactSide1: apex.ApexBool, allowSelfContactSide2: apex.ApexBool) -> InteractionRep`
Update an interaction rep.

- `name` — Optional-name of interaction rep
- `description` — Optional - description of interaction rep.
- `id` — Optional-id of interaction rep. If omits, the system will automatically assign the ID.
- `interactionType` — Interaction type of the interaction object: Glue, General Contact or Self Contact.
- `interactionPropertyGeometric` — Interaction Geometric Properties.
- `interactionPropertyPhysical` — Interaction Physical Properties.
- `allowSelfContactSide1` — Optional - Boolean to choose self Contact for primary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.
- `allowSelfContactSide2` — Optional - Boolean to choose self Contact for secondary side of interaction pair. It is only available if interactionType = Glue or General contact. Omits it if interactionType = Self contact.


## `apex.attribute.InterfacePoint`  (extends `Entity`, `IName`, `IPhysical`, `IDisplayable`, `IUserAttributes`, `IActivatable`, `IOrientation`)
Properties: `activeDofs`, `applicationMethod`, `description`, `distributionType`, `generateASET`, `name`, `orientation`, `target`

Methods:

- `getActiveDofs() -> str` — Returns active DOFs of the Interface Point. A string defining the degrees of freedom that are active on this InterfacePoint. Each degrees of freedom is represented by an integer between 1 and 6. Translational DOFs are denoted by the values 1, 2 and 3 (corresponding to translation along x, y and z axes). Rotational DOFs are denoted by the values 4, 5 and 6 (corresponding to rotation about the x, y and z axes). If the interface point is created by "Free" Method, return "None".
- `getApplicationMethod() -> apex.attribute.ApplicationMethod` — Returns application method of the Interface Point. The application method, options are: 1. ApplicationMethod.Direct 2. ApplicationMethod.Remote 3. ApplicationMethod.Free, the method is only available in Adams Mission.
- `getDistributionType() -> apex.attribute.DistributionType` — Returns distribution type of the Interface Point. Enumeration property defining how loads will be distributed between the InterfacePoint and the attachment region. The default "Compliant" option causes the motion of the reference point to be calculated as the average of the motions of the points in the attachment region. It adds no stiffness to the regions that it attaches to and will distribute load according to the relative stiffness distributions across the attachment region. The optional "Rigid" option will cause the entire attachment region to be considered as a rigid body. If the attachment region is already part of a rigid body, the options are equivalent. If the interface point is created by "Free" Method, return "None".
- `getGenerateASET() -> bool` — Returns Boolean of generateASET of the Interface Point. Optional Boolean property to control if ASET creates for the Interface Point. If true, the ASET will be created to generate MNF. If false, No ASET will be created. If ApplicationMethod.Free is used, it will be omitted.
- `getLocation() -> apex.Coordinate` — Returns location of the Interface Point as an ILocation. The location of the InterfacePoint will be at the global x, y, z coordinate locations defined by ILocation.
- `getOrientation() -> apex.Orientation` — Returns orientation of the Interface Point as an IOrientation object.
- `getTarget() -> apex.EntityCollection` — Returns target of the Interface Point. A collection of entities that define regions of the MechanicalSystem to which this InterfacePoint connects. Valid entity types are Parts, geometry bodies, geometry topologies or nodes.
#### `update(name: str, description: str, applicationMethod: apex.attribute.ApplicationMethod, location: apex.ILocation, target: apex.EntityCollection, distributionType: apex.attribute.DistributionType, orientation: apex.IOrientation, activeDofs: str, generateASET: bool, useLocalValue: bool) -> None`
Updates one or more properties of this InterfacePoint. This method allows multiple properties of the InterfacePoint to be updated using a single method call. All arguments are optional and the values of all InterfacePoint properties associated with the omitted arguments are left unchanged.

- `name` — Updates the name of this InterfacePoint. InterfacePoint names must be unique within the scope of their parent Part or Assembly. If a non-unique name is provided here it will be silently modified to ensure uniqueness.
- `description` — Updates the description of this InterfacePoint.
- `applicationMethod` — Update the application method. Options are: 1. ApplicationMethod.Direct 2. ApplicationMethod.Remote 3. ApplicationMethod.Free, the method is only available in Adams Mission.
- `location` — Updates the location of this InterfacePoint with an ILocation. The location of the InterfacePoint will be at the global x, y, z coordinate locations defined by location. While application method is "Direct", skip the location definition and the system will automatically calculation the location. While application method is "Remote" or "Free", the location is required.
- `target` — A collection of entities as an ILocationCollection that define regions of the MechanicalSystem to which this InterfacePoint connects. Valid entity types are Parts, geometry bodies, geometry topologies or nodes.
- `distributionType` — Updates the distributionType for this InterfacePoint to define how loads will be distributed between the InterfacePoint and the attachment region. A value of "apex.attributes.DistributionType.Compliant" causes the motion of the reference point to be calculated as the average of the motions of the points in the attachment region. It adds no stiffness to the regions that it attaches to and will distribute load according to the relative stiffness distributions across the attachment region. A value of "apex.attributes.DistributionType.Rigid" causes the entire attachment region to be considered as a rigid body. If the attachment region is already part of a rigid body, the options are equivalent. If applicationMethod is "ApplicationMethod.Free", distribution type will be skipped.
- `orientation` — Update orientation for the InterfacePoint as an IOrientation object.
- `activeDofs` — Updates the active degrees of freedom for this InterfacePoint using a string defining the degrees of freedom that are active on this InterfacePoint. Each degrees of freedom is represented by an integer between 1 and 6. Translational degrees of freedom are denoted by the values 1, 2 and 3 (corresponding the x, y and z axes) with rotational degrees of freedom represented by the values 4, 5 and 6 representing rotations about the x, y and z axes. The active degrees of freedom may be defined in any order. Duplicate values will be silently removed. Providing more than six characters is considered an error wan will cause the method to raise an exception. If omitted, all six degrees of freedom will be active. The argument of "activeDofs" is not required in "ApplicationMethod.Free".
- `generateASET` — Optional Boolean argument to control if ASET creates for the interface point. If true, the ASET will be created to generate MNF. If false, No ASET will be created. If ApplicationMethod.Free is used, it will be omitted.
- `useLocalValue` — Optional-Boolean argument(default = True) to use local location and orientation value to define "origin" and "orientation". The local location and orientation value is referencing to its parent part. If it is false, the location and orientation value is referencing to global.


## `apex.attribute.InterfacePointCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `InterfacePointCollection() -> None` — Construct a new InterfacePointCollection.

## `apex.attribute.Joint`  (extends `Entity`, `IDisplayable`, `IIdentifier`, `IPhysical`, `IUserAttributes`, `IName`)
Contains Joint and methods for editing/getting Joint attributes.
Properties: `axisLocationMode`, `jointAxis`, `jointOrientation`, `jointOrigin`, `jointRenderType`, `jointType`, `side1`, `side1DistributionType`, `side2`, `side2DistributionType`

Methods:

- `getAxisLocationMode() -> str` — Returns AxisLocationMode of the Joint.
- `getJointAxis() -> apex.construct.CoordinateSystemAxis` — *Returns orientation of the Joint.
- `getJointOrientation() -> apex.construct.Orientation` — Returns orientation of the Joint.
- `getJointOrigin() -> apex.Entity` — Returns Origin of the Joint.
- `getJointRenderType() -> apex.attribute.JointRenderType` — Returns JointRenderType of the Joint.
- `getJointType() -> int` — Returns the joint Type of joint.
- `getSide1() -> apex.EntityCollection` — Returns side 1 attachment region of the Joint.
- `getSide1DistributionType() -> str` — Returns Side 1 Distribution Type of the Joint.
- `getSide2() -> apex.EntityCollection` — Returns side 2 attachment region of the Joint.
- `getSide2DistributionType() -> str` — Returns Sidde 2 Distribution Type of the Joint.

## `apex.attribute.JointCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of Joint, based on EntityCollection.

Methods:

- `JointCollection() -> None` — Construct a new JointCollection.

## `apex.attribute.LayeredPanel`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IName`)
Class LayeredPanel.
Properties: `alignmentType`, `allowableInterLaminarBondStress`, `failureCriteria`, `panelCoordinateSystem`, `panelMaterialOrientation`, `panelMaterialOrientations`, `panelOffset`, `plies`, `plyBehavior`, `plyIdBehavior`, `referenceTemperature`, `structuralDampingCoefficient`, `target`, `zones`

Methods:

- `addPanelMaterialOrientations(panelMaterialOrientations: {str:[{dict}]}) -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `clearAllPanelMaterialOrientations() -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Clears all material orientations defined in this layeredPanel.
#### `createAddPlyUsingProjectedVector(material: apex.attribute.Material, thickness: float, angle: float, coverageRegion: apex.EntityCollection) -> apex.attribute.Ply`
Creates a Ply and adds it to the LayeredPanel using a projected vector approach to define the Ply Material orientation.

- `material` — The Ply Material
- `thickness` — The ply thickness, Thickness is a Length quantity and must be entered in the units of Length from the active ScriptUnitSystem
- `angle` — The ply angle. This angle is used to define the orientation of the material relative to the LayeredPanel material reference direction. The Material X-axis will be oriented at this angle relative to the LayeredPanel material reference angle
- `coverageRegion` — The region of this layeredPanel that the Ply will cover as an EntityCollection. The coverage Region may contain, The single Surface that defines the extent of the LayeredPanelAny combination of the Faces of the LayeredPanel SurfaceAny existing Zone within this layeredPanel Zones and Faces may be mixed to define the desired CoverageRegion. Duplicate Faces or overlapping Zones/Faces will be silently resolved.

The Ply Material, Thickness and Angle are provided as inputs to the method The Material properties will be aligned such that the X-axis properties of the Material are aligned with the projection of a Vector

#### `createPliesFromSheetStackUsingProjectedVector(materialSheetStack: apex.attribute.MaterialSheetStack, angle: float, coverageRegion: apex.EntityCollection) -> apex.attribute.PlyCollection`
Creates and returns a sequence of plies within this LayeredPanel using an input MaterialSheetStack and orients the sheet stack relative to the panel axis using the input angle.

- `materialSheetStack` — The MaterialSheetStack (from the material Catalog) to add to this LayeredPanel
- `angle` — the angle of the MaterialSheetStack axis relative to the layered panel material reference axis. angle represents a unit of rotation and is defined using the rotation unit from the active script unit system.
- `coverageRegion` — The region of this layeredPanel that the Ply will cover as an EntityCollection. The coverage Region may contain, The single Surface that defines the extent of the LayeredPanelAny combination of the Faces of the LayeredPanel SurfaceAny existing Zone within this layeredPanel Zones and Faces may be mixed to define the desired CoverageRegion. Duplicate Faces or overlapping Zones/Faces will be silently resolved.

Each sheet within the MaterialSheetStack retains its original orientation relative to other sheets in the stack.The orientation of each sheet in the stack relative to the panel axis is determined from the cumulative rotation of the stack relative to the panel plus the angle of the individual sheet relative to the SheetStack.

#### `createPlyFromSheetUsingProjectedVector(materialSheet: apex.attribute.MaterialSheet, angle: float, coverageRegion: apex.EntityCollection) -> apex.attribute.Ply`
Creates a ply within this LayeredPanel using an input MaterialSheet and orients the sheet relative to the panel axis using the input angle.

- `materialSheet` — a MaterialSheet from the Material catalog
- `angle` — the angle of this ply relative to the layered panel material reference axis. angle represents a unit of rotation and is defined using the rotation unit from the active script unit system.
- `coverageRegion` — The region of this layeredPanel that the Ply will cover as an EntityCollection. The coverage Region may contain, The single Surface that defines the extent of the LayeredPanelAny combination of the Faces of the LayeredPanel SurfaceAny existing Zone within this layeredPanel Zones and Faces may be mixed to define the desired CoverageRegion. Duplicate Faces or overlapping Zones/Faces will be silently resolved.

#### `deletePlies(plies: apex.attribute.PlyCollection) -> None`
Deletes Plies from this Layered Panel.

- `plies` — of this LayeredPanel

#### `deletePly(ply: apex.attribute.Ply) -> None`
Deletes a Ply.

- `ply` — of this LayeredPanel

- `flip() -> None` — Flips the build direction of the layeredPanel, if the input target is a general surface, then flip will not perform as there is no uniform build direction for a general surface.
- `getAlignmentType() -> apex.attribute.AlignmentType` — Gets an optional enum defining the default alignment type for the panel.If omitted, the offsetType is "apex.attribute.AlignmentType..Offset".
- `getAllowableInterLaminarBondStress() -> float` — Gets the allowable shear stress of the bonding material.
- `getFailureCriteria() -> apex.attribute.FailureCriteriaComposite` — Gets the optional enum defining the failureCriteria of the panel.
- `getPanelCoordinateSystem() -> apex.construct.CoordinateSystem` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `getPanelMaterialOrientation() -> apex.construct.Orientation` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `getPanelMaterialOrientations() -> {str:[{dict}]}` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `getPanelOffset() -> float` — Gets the panel offset distance from the bottom plane. If omitted, the reference location of the panel is on the bottom plane.
- `getPlies() -> apex.attribute.PlyCollection` — Gets Plies of the LayeredPanel.
#### `getPly(name: str) -> apex.attribute.Ply`
Gets the ply of the LayeredPanel.

- `name` — of the ply

- `getPlyBehavior() -> apex.attribute.PlyBehavior` — Gets the plyBehavior of the panel.If omitted, the plyBehavior is "apex.attribute.PlyBehavior.Default".
#### `getPlyById(id: int) -> apex.attribute.Ply`
Gets the ply of the LayeredPanel by id.

- `id` — of the ply

- `getPlyIdBehavior() -> apex.attribute.PlyIdBehavior` — Gets the plyIdBehavior of the panel.If omitted, the plyBehavior is "apex.attribute.PlyIdBehavior.UseGlobal".
- `getReferenceTemperature() -> float` — Gets the optional referenceTemperature of the layeredPanel.
- `getStructuralDampingCoefficient() -> float` — Gets an optional structuralDampingCoefficient of the panel.
- `getTarget() -> apex.Entity` — Gets the target that supports this LayeredPanel. It can be one surface or one 2d mesh.
#### `getZone(index: int) -> apex.attribute.Zone`
Gets the zone of the LayeredPanel.

- `index` — of the zone

#### `getZoneByID(id: int) -> apex.attribute.Zone`
Gets the zone of the LayeredPanel by id.

- `id` — of the zone

- `getZones() -> apex.attribute.ZoneCollection` — Gets Zones of the LayeredPanel.
#### `highlightZone(zone: apex.attribute.Zone) -> None`
Highlight a Zone.

- `zone` — of this LayeredPanel

- `removePanelMaterialOrientations(target: {str:str}) -> None` — THIS FUNCTION IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `setAlignmentType(alignmentType: apex.attribute.AlignmentType) -> None` — Sets an optional enum defining the default alignment type for the panel.If omitted, the offsetType is "apex.attribute.AlignmentType..Offset".
- `setFailureCriteria(failureCriteria: apex.attribute.FailureCriteriaComposite) -> None` — Sets the optional enum defining the failureCriteria of the panel.
- `setPanelOffset(panelOffset: float) -> None` — Sets the panel offset distance from the bottom plane. If omitted, the reference location of the panel is on the bottom plane.
- `setPlyBehavior(plyBehavior: apex.attribute.PlyBehavior) -> None` — Sets the plyBehavior of the panel.If omitted, the plyBehavior is "apex.attribute.PlyBehavior.Default".
- `setPlyIdBehavior(plyIdBehavior: apex.attribute.PlyIdBehavior) -> None` — Sets the plyIdBehavior of the panel.If omitted, the plyBehavior is "apex.attribute.PlyIdBehavior.UseGlobal".
- `setReferenceTemperature(referenceTemperature: float) -> None` — Sets the optional referenceTemperature of the layeredPanel.
- `setStructuralDampingCoefficient(structuralDampingCoefficient: float) -> None` — Sets an optional structuralDampingCoefficient of the panel.
#### `setTarget(target: apex.Entity) -> None`
Sets the Surface that supports this LayeredPanel.

- `target` — target of the LayeredPanel

#### `update(name: str, description: str, offset: float, alignmentType: apex.attribute.AlignmentType, buildSide: apex.attribute.TopBottom, failureCriteria: apex.attribute.FailureCriteriaComposite, plyBehavior: apex.attribute.PlyBehavior, referenceTemperature: float, allowableInterLaminarBondStress: float, structuralDampingCoefficient: float, orientation: apex.construct.Orientation, panelMaterialOrientations: {str:[{dict}]}, plyIdBehavior: apex.attribute.PlyIdBehavior) -> None`
Update this LayeredPanel properties.

- `name` — of this LayeredPanel
- `description` — of this LayeredPanel
- `offset` — of this LayeredPanel
- `alignmentType` — of this LayeredPanel
- `buildSide` — of this LayeredPanel
- `failureCriteria` — of this LayeredPanel
- `plyBehavior` — of this LayeredPanel
- `referenceTemperature` — of this LayeredPanel
- `allowableInterLaminarBondStress` — of this LayeredPanel
- `structuralDampingCoefficient` — of this LayeredPanel
- `orientation` — of this LayeredPanel, THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `panelMaterialOrientations` — of this LayeredPanel, THIS ARGUMENT IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE.
- `plyIdBehavior` — of this LayeredPanel

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.LayeredPanelCollection`  (extends `EntityCollection`)
Iterable collection of LayeredPanel, based on EntityCollection.

Methods:

- `LayeredPanelCollection() -> None` — Construct a new LayeredPanelCollection.

## `apex.attribute.Mass`  (extends `ConstitutiveModel`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `massDensity`

Methods:

#### `Mass(massDensity: float) -> None`
Create ElasticityLinear2DOrtho constitutive model.

- `massDensity` — of this constitutive model

- `getMassDensity() -> float` — Returns Elastic Modulus 11 of the constitutive model.
#### `update(massDensity: float) -> None`
Update properties of this ElasticityLinear2DOrtho constitutive model.

- `massDensity` — of this constitutive model


## `apex.attribute.Material`  (extends `Entity`, `IUserAttributes`, `IName`)
Class representing a Material in Apex.
Properties: `color`, `constitutiveModels`, `coverageRegions`, `dampingCoefficient`, `density`, `elasticityOrthotropic2D`, `elasticModulus`, `id`, `materialType`, `poissonRatio`, `references`, `target`, `thermalExpansionCoeff`, `thermalExpansionCoeffOrthotropic2D`

Methods:

#### `addConstitutiveModel(constitutiveModel: apex.attribute.ConstitutiveModel) -> None`
This Method is no longer supported in Apex. Refer to Material.setPrimaryMaterialModel and Material.addSecondaryMaterialModel to determine how this capability is now supported.

- `constitutiveModel` — to be added

This method used to add constitutive models to material objects. The user can first create a material object and then add the required material constitutive model to this material as needed.An example how user will use:myMaterial = apex.catalog.createMaterial(name=xxx, description = "", etc. )..... create a empty material object.myIsotropicElasticty = apex.attribute.ElasticityLinearIso(elasticModulus = , poissonRatio = , etc.).... create an IsotropicElasticity constitutive modelmyMaterial.addConstitutiveModel(constitutiveModel = myisotropicElasticty) ....... add the IsotropicElasticty constitutive to the material.Since a material can have more than one constitutive model, Then add more constitutive models using the addConstitutiveModel() method.myIsotropicLinearExpansion = apex.attribute.ThermalExpansionLinearIsotropic(expansionCoefficient11 = xxx)myMaterial.addConstitutiveModel(constitutiveModel = myIsotropicLinearExpansion).

#### `addSecondaryMaterialModel(secondaryMaterialModel: apex.attribute.MaterialModel) -> bool`
This method is used to add a secondary material model to a material object.

- `secondaryMaterialModel` — to be added

example: material_1 = apex.catalog.createMaterial(name="Material 1", description = "", primaryMaterialModel = "MAT1") matModel_ = apex.attribute.MaterialModel( keyword = 'MATEP' ) material_1.addSecondaryMaterialModel(secondaryMaterialModel = matModel_)

- `getColor() -> [int]` — Returns Color (RGB Vector) of the material.
#### `getConstitutiveModel(type: ConstitutiveModelType) -> apex.attribute.ConstitutiveModel`
This Method is no longer supported in Apex. Refer to Material.getMaterialModel to determine how this capability is now supported.

- `type` — Defined which type of ConstitutiveModel the method get

This method used to get the ConstitutiveModel via ConstitutiveModelType which assigned to a material.example: myElasticity = material1.getConstitutiveModel(type = Elasticity)myElasticity.update(modulus = xx)Returns some kind of constitutive model added to the material.

- `getConstitutiveModels() -> [apex.attribute.ConstitutiveModel]` — This Method is no longer supported in Apex. Refer to Material.getMaterialModels to determine how this capability is now supported.
- `getCoverageRegions() -> MaterialCoverageRegionCollection` — Returns all MaterialCoverageRegions that this Material is associated with.
- `getDampingCoefficient() -> float` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getDensity() -> float` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getElasticModulus() -> float` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getElasticityOrthotropic2D() -> {str:float}` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getId() -> int` — Returns id of the material.
#### `getMaterialModel(materialModel: str) -> apex.attribute.MaterialModel`
Returns specific material model via material model name which is assigned to a material.

- `materialModel` — Defined the material model name.

example: MAT1_ = material1.getMaterialModel(materialModel = "MAT1") Returns a certain material model added to the material.

- `getMaterialModels() -> [apex.attribute.MaterialModel]` — Returns all material models which are assigned to a material.
- `getMaterialType() -> MaterialType` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getPoissonRatio() -> float` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getReferences() -> apex.EntityCollection` — returns a collection of all entities that this Material directly references
- `getTarget() -> apex.EntityCollection` — Returns a read only collection of the entities that the Material is applied to.
- `getThermalExpansionCoeff() -> float` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
- `getThermalExpansionCoeffOrthotropic2D() -> {str:float}` — This Method is no longer supported in Apex. Refer to MaterialModel and Material.getMaterialModel to determine how this capability is now supported.
#### `removeConstitutiveModel(constitutiveModel: apex.attribute.ConstitutiveModel) -> None`
This method used to remove constitutive models from a material objects.

- `constitutiveModel` — to be removed

An example how user will use:myMaterial = apex.catalog.createMaterial(name=xxx, description = "", etc. )..... create a empty material object.myIsotropicElasticty = apex.attribute.ElasticityLinearIso(elasticModulus = , poissonRatio = , etc.).... create an IsotropicElasticity constitutive modelmyMaterial.addConstitutiveModel(constitutiveModel = myisotropicElasticty) ....... add the IsotropicElasticity constitutive to the material.myMaterial.removeConstitutiveModel(constitutiveModel = myisotropicElasticty) ....... remove the IsotropicElasticity constitutive from the material.Since a material can have more than one constitutive model, Then add more constitutive models using the addConstitutiveModel() method.myIsotropicLinearExpansion = apex.attribute.ThermalExpansionLinearIsotropic(expansionCoefficient11 = xxx)myMaterial.addConstitutiveModel(constitutiveModel = myIsotropicLinearExpansion).myMaterial.removeConstitutiveModel(constitutiveModel = myIsotropicLinearExpansion).This Method is no longer supported in Apex. Refer to Material.removeMaterialModel to determine how this capability is now supported.

#### `removeMaterialModel(materialModel: apex.attribute.MaterialModel) -> None`
This method is used to remove a material model (if exists) from a material object.

- `materialModel` — to be removed

example: material_1 = apex.catalog.createMaterial(name="Material 1", description = "", primaryMaterialModel = "MAT1") matModel_ = apex.attribute.MaterialModel( keyword = 'MATEP' ) material_1.addSecondaryMaterialModel(secondaryMaterialModel = matModel_) material_1.removeMaterialModel(materialModel = matModel_)

#### `setPrimaryMaterialModel(primaryMaterialModel: apex.attribute.MaterialModel) -> None`
This method is used to set the primary material model to a material object.

- `primaryMaterialModel` — to be set

example: material_1 = apex.catalog.createMaterial(name="Material 1", description = "", primaryMaterialModel = "MAT1") matModel_ = apex.attribute.MaterialModel( keyword = 'MAT8' ) material_1.setPrimaryMaterialModel(primaryMaterialModel = matModel_)

#### `update(name: str, description: str, color: [int], id: int) -> None`
Update this Material properties.

- `name` — of this Material
- `description` — of this Material
- `color` — of this material
- `id` — Optional - id of this Material.

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.MaterialCollection`  (extends `EntityCollection`)

Methods:

- `MaterialCollection() -> None` — Construct a new MaterialCollection.

## `apex.attribute.MaterialCoverageRegion`  (extends `Entity`, `IPhysical`, `IUserAttributes`)
DEPRECATION NOTICE: THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Class MaterialCoverageRegion. Can only be constructed using apex.catalog createMaterialCoverageRegion() method.
Properties: `alignmentMethod`, `director`, `material`, `materialCoordinateSystem`, `name`, `target`

Methods:

- `getAlignmentMethod() -> MaterialAlignmentMethod` — An enumeration that indicates which method is used to define the material orientation in this MaterialCoverageRegion..
- `getDirector() -> apex.EntityCollection` — A collection of Curves and/or Edges that define how the Material is oriented across this MaterialCoverageRegion.
- `getMaterial() -> Material` — The Material that is assigned to this coverage region.
- `getMaterialCoordinateSystem() -> apex.construct.CoordinateSystem` — A apex.construct.CoordinateSystem whose X axis defines the Material orientation in this MaterialCoverageRegion.
- `getName() -> str` — The name of this MaterialCoverageRegion.
- `getTarget() -> apex.EntityCollection` — The entities that are included in this MaterialCoverageRegion as an EntityCollection.
#### `update(name: str, target: apex.EntityCollection, materialAxis: apex.EntityCollection, director: apex.EntityCollection, orientation: apex.construct.Orientation, origin: apex.ILocation) -> None`
Update this MaterialCoverageRegion properties.

- `name` — The name of this MaterialCoverageRegion
- `target` — The collection of entities that the Material will be assigned to as an EntityCollection. Target may contain Solids, Surfaces, Faces or 2D elements - all other types will be silently ignored. When Solids are included they are internally expanded to the complete set of free faces of the apex.geometry.Solid. Any duplicate entities in target are ignored
- `materialAxis` — A apex.construct.CoordinateSystem axis that will define the material orientation.
- `director` — A collection of Curves and/or Edges that will be used to define the material orientation. director may include Curves or Edges. NOTE : Current releases of Apex support a single apex.geometry.Curve or apex.geometry.Edge only which must be the first entry in the collection. If the Collection includes more than one entry only the first will be used and all others will be silently ignored.
- `orientation` — The Euler angles defined an orientation which used as the material direction. When user using the Euler angles method to align material, there will input Euler angles.
- `origin` — The origin location of A Coordinate system whose X axis defines the material orientation.

One or more properties may be updated in each call to update(). For example: "materialAxis" and "director" are mutually exclusive and the update method will throw an exception of both are defined in the same invocation. If the the update method defines one of these properties and the other has previously been defined for the Material, the existing property will be replaced by the new one.


## `apex.attribute.MaterialCoverageRegionCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `MaterialCoverageRegionCollection() -> None` — Construct a new MaterialCoverageRegionCollection.

## `apex.attribute.MaterialModel`  (extends `Entity`)
This class manages the Material Models of a material.

Methods:

#### `MaterialModel(materialModel: str) -> None`
Create Generic Constitutive Model.

- `materialModel` — keyword of this generic constitutive model

- `getProperties() -> {str:value}` — This function will return the whole dictionary which stores the Material properties.
- `getProperty(key: str) -> object` — The function is passed with an attribute name (bdf filed name), Returns the corresponding value of the attribute. For example: XXModel_.getProperty('E'), the "E" is the input, will return the elasticity Modulus value. The return Type maybe different depend on the value return.
#### `update(materialProperties: {str:value}) -> None`
Update the Generic Constitutive Model.

- `materialProperties` — A dictionary to define material properties. The key is a string of the property name, the value is of valid types.


## `apex.attribute.MaterialOrientationField2D`  (extends `DiscreteFEMField`)
Class MaterialOrientationField2D. This class describes the property of MaterialOrientationField2D. This is the base class of MaterialOrientationField2DCoordinate and MaterialOrientationField2DAlignCurve.
Properties: `alignmentMethod`, `target`

Methods:

- `convertAlignmentMethod(alignmentMethod: apex.attribute.MaterialAlignmentMethod, alignToEntity: apex.Entity) -> MaterialOrientationField2D` — convert MaterialOrientationField2D
- `getAlignmentMethod() -> apex.attribute.MaterialAlignmentMethod` — An enumeration that indicates which method is used to define the material orientation in this MaterialOrientationField2D..
- `getTarget() -> apex.EntityCollection` — Get a collection of all entities that this field directly references.

## `apex.attribute.MaterialOrientationField2DAlignCurve`  (extends `MaterialOrientationField2D`)
Class MaterialOrientationField2DAlignCurve. This class describes the property of MaterialOrientationField2DAlignCurve.
Properties: `director`

Methods:

- `getDirector() -> apex.Entity` — A entity of Curve and/or Edge that define how the Material is oriented across this MaterialOrientationField2DAlignCurve.
#### `update(name: str, target: apex.EntityCollection, director: apex.Entity) -> None`
Update this MaterialOrientationField2DAlignCurve properties.

- `name` — The name of this MaterialOrientationField2DAlignCurve
- `target` — The collection of entities that the MaterialOrientationField2DCoordinate will be assigned to as an EntityCollection. Target may contain Parts, Surfaces, Faces or 2D meshes or 2D elements - all other types will be silently ignored. When Parts are included they are internally expanded to the complete set of surfaces of the apex.Part. Any duplicate entities in target are ignored
- `director` — A entity of Curve and/or Edge that will be used to define the material orientation. director may include single Curve or Edge.


## `apex.attribute.MaterialOrientationField2DCoordinate`  (extends `MaterialOrientationField2D`)
Class MaterialOrientationField2DCoordinate. This class describes the property of MaterialOrientationField2DCoordinate.
Properties: `coordinateSystem`

Methods:

- `getCoordinateSystem() -> apex.construct.CoordinateSystem` — A apex.construct.CoordinateSystem defines the Material orientation in this MaterialOrientationField2DCoordinate.
#### `update(name: str, target: apex.EntityCollection, coordinateSystem: apex.Entity) -> None`
Update this MaterialOrientationField2DCoordinate properties.

- `name` — The name of this MaterialOrientationField2DCoordinate
- `target` — The collection of entities that the MaterialOrientationField2DCoordinate will be assigned to as an EntityCollection. Target may contain Parts, Surfaces, Faces or 2D meshes or 2D elements - all other types will be silently ignored. When Parts are included they are internally expanded to the complete set of surfaces of the apex.Part. Any duplicate entities in target are ignored
- `coordinateSystem` — A apex.construct.CoordinateSystem axis that will define the material orientation.


## `apex.attribute.MaterialSheet`  (extends `Entity`, `IUserAttributes`, `IName`)
Class representing a material sheet that combines a material reference with a thickness.
Properties: `material`, `thickness`

Methods:

- `getMaterial() -> apex.attribute.Material` — Gets the material from which this sheet is made and which, in conjunction with thickness, defines the mechanical properties of the sheet.
- `getThickness() -> float` — Gets the thickness of this SheetMaterial. thickness represents a Length quantity and is defined using the units of Length from the active script unit system.
#### `setDescription(description: str) -> None`
Set the MaterialSheet description.

- `description` — of the MaterialSheet.

- `setMaterial(material: apex.attribute.Material) -> None` — Sets the material from which this sheet is made and which, in conjunction with thickness, defines the mechanical properties of the sheet.
#### `setName(name: str) -> None`
Set the MaterialSheet name.

- `name` — of the MaterialSheet.

- `setThickness(thickness: float) -> None` — Sets the thickness of this SheetMaterial. thickness represents a Length quantity and is defined using the units of Length from the active script unit system.
#### `update(name: str, description: str, material: apex.attribute.Material, thickness: float) -> None`
Updates one or more properties of this SheetMaterial This method allow multiple properties of the SheetMaterial to be updated using a single method call. All arguments are optional and the values of all SheetMaterial properties associated with the omitted arguments are left unchanged.

- `name` — The name of this SheetMaterial. SheetMaterial names must be unique within the Materials catalog. I a non-unique name is provided, the system will silently modify it by appending an integer to ensure name uniqueness.
- `description` — A description for this SheetMaterial.
- `material` — The base material from which this MaterialSheet is composed.
- `thickness` — The thickness of this MaterialSheet. thickness represents a Length quantity and is defined using the units of Length from the active script unit system.


## `apex.attribute.MaterialSheetCollection`  (extends `EntityCollection`)

Methods:

- `MaterialSheetCollection() -> None` — Iterable collection of MaterialSheets.

## `apex.attribute.MaterialSheetStack`  (extends `Entity`, `IUserAttributes`, `IName`)
Class representing a sequence of ordered and oriented MaterialSheets to enable efficient definition of laminates. Associating the MaterialSheetStack to a region of a LayeredPanel enables rapid definitions of complex laminates.
Properties: `sheetStackDefinition`, `symmetry`

Methods:

- `getSheetStackDefinition() -> [{str:str}]` — Gets sheetStackDefinition defines an ordered List of oriented MaterialSheets. Each entry in the List is a dictionary and each dictionary identifies a MaterialSheet and the orientation of the sheet in the stack. The order of the dictionaries in the list defines the order of the Sheets in the SheetStack. Each Dictionary includes two key value pairs, key = "sheet_name" of type string has an associated string type value identifying the name of the MaterialSheet key = "sheet_orientation" of type string has an associated float value defining the relative orientation of the sheet in the SheetStack The value of sheet_orientation represents an Angle quantity and must be defined using the units of Angle from the active script unit system.
- `getSymmetry() -> apex.attribute.StackSymmetry` — Gets enumeration defining whether the provided sheet stack definition will be reflected to add additional sheets to the stack or not. A value of apex.attributes.StackSymmetry. None indicates that this stack has no symmetry - the stack includes only those sheets explicitly defined in the stack definition A value of apex.attributes.StackSymmetry.Odd indicates that this stack is symmetric about the first sheet. Every sheet apart from the first will be mirrored about the first sheet, adding more sheets to the stack than are explicitly defined in the stack definition. The first sheet occurs just once in the stack - it is the "middle" sheet. A value of apex.attributes.StackSymmetry.Even indicates that this stack is symmetric and every sheet in the stack definition will be mirrored, including the first sheet, to double the number of sheets explicitly defined in the stack definition.
#### `moveSheetDown(sheetIndex: int) -> int`
Moves the sheet identified in the input down one position in the stack.

- `sheetIndex` — The index of the Sheet to move down.

#### `moveSheetUp(sheetIndex: int) -> int`
Moves the sheet identified in the input up one position in the stack.

- `sheetIndex` — The index of the Sheet to move up.

- `reverse() -> None` — Reverses the order of the MaterialSheets in this MaterialSheetStack.
#### `setDescription(description: str) -> None`
Set the MaterialSheetStack description.

- `description` — of the MaterialSheetStack.

#### `setName(name: str) -> None`
Set the MaterialSheetStack name.

- `name` — of the MaterialSheetStack.

#### `setSheetStackDefinition(sheetStackDefinition: [{str:str}]) -> None`
Sets sheetStackDefinition defines an ordered List of oriented MaterialSheets. Each entry in the List is a dictionary and each dictionary identifies a MaterialSheet and the orientation of the sheet in the stack. The order of the dictionaries in the list defines the order of the Sheets in the SheetStack. Each Dictionary includes two key value pairs, key = "sheet_name" of type string has an associated string type value identifying the name of the MaterialSheet key = "sheet_orientation" of type string has an associated float value defining the relative orientation of the sheet in the SheetStack The value of sheet_orientation represents an Angle quantity and must be defined using the units of Angle from the active script unit system.

- `sheetStackDefinition` — A list of dictionaries that define the order and relative orientations of the Sheets that make up this SheetStack.

#### `setSymmetry(symmetry: apex.attribute.StackSymmetry) -> None`
Sets enumeration defining whether the provided sheet stack definition will be reflected to add additional sheets to the stack or not. A value of apex.attributes.StackSymmetry. None indicates that this stack has no symmetry - the stack includes only those sheets explicitly defined in the stack definition A value of apex.attributes.StackSymmetry.Odd indicates that this stack is symmetric about the first sheet. Every sheet apart from the first will be mirrored about the first sheet, adding more sheets to the stack than are explicitly defined in the stack definition. The first sheet occurs just once in the stack - it is the "middle" sheet. A value of apex.attributes.StackSymmetry.Even indicates that this stack is symmetric and every sheet in the stack definition will be mirrored, including the first sheet, to double the number of sheets explicitly defined in the stack definition.

- `symmetry` — enumeration defining whether the provided sheet stack definition will be reflected to add additional sheets to the stack or not. A value of apex.attributes.StackSymmetry.Asymmetric indicates that this stack has no symmetry - the stack includes only those sheets explicitly defined in the stack definition A value of apex.attributes.StackSymmetry.Odd indicates that this stack is symmetric about the first sheet. Every sheet apart from the first will be mirrored about the first sheet, adding more sheets to the stack than are explicitly defined in the stack definition. The first sheet occurs just once in the stack - it is the "middle" sheet. A value of apex.attributes.StackSymmetry.Even indicates that this stack is symmetric and every sheet in the stack definition will be mirrored, including the first sheet, to double the number of sheets explicitly defined in the stack definition

#### `update(name: str, description: str, sheetStackDefinition: [{dict}], symmetry: apex.attribute.StackSymmetry) -> None`
Updates one or more properties of this SheetStack This method allow multiple properties of the SheetStack to be updated using a single method call. All arguments are optional and the values of all SheetStack properties associated with the omitted arguments are left unchanged.

- `name` — The name of this SheetStack. SheetStack names must be unique within the MaterialCatalog. If a non-unique name is provided the system will silently change the input name by appending an integer to the provided name to ensure uniqueness.
- `description` — A description for this SheetStack.
- `sheetStackDefinition` — A list of dictionaries that define the order and relative orientations of the Sheets that make up this SheetStack.
- `symmetry` — A property to indicate if the stack is symmetric.


## `apex.attribute.MaterialSheetStackCollection`  (extends `EntityCollection`)

Methods:

- `MaterialSheetStackCollection() -> None` — Iterable collection of MaterialSheetStacks.

## `apex.attribute.MeshDependentTie`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
class MeshDependentTie.
Properties: `bodies`, `facesEdges`

Methods:

- `asEntity() -> Entity`
#### `getBodies() -> apex.geometry.GeometryBodyCollection`
a collection of all of the Bodies associated with this MeshDependentTie.

Returns: a collection of all of the Bodies associated with this MeshDependentTie.

#### `getFacesEdges() -> apex.geometry.GeometryTopologyCollection`
a collection of all of the Faces and/or Edges associated with this MeshDependentTie.

Returns: a collection of all of the Faces and/or Edges associated with this MeshDependentTie.

#### `removeBodies(bodies: apex.geometry.GeometryBodyCollection) -> apex.geometry.GeometryBodyCollection`
removes Geometry Bodies from the MeshDependentTie.

- `bodies` — a apex.geometry.GeometryBodyCollection that may contain apex.geometry.Solid, apex.geometry.Surface or apex.geometry.Curve bodies only. If the collection includes Points or Geometry bodies that are not currently associated with the tie they will be ignored.

Returns: a collection of all Geometry bodies that remain associated with the tie after the supplied bodies have been removed. If all of the bodies are removed or if only a single body remains after the supplied bodies are removed the Tie will be deleted and the method will return and empty collection

#### `update(name: str, description: str) -> None`
Update this MeshDependentTie.

- `name` — the name of the tie
- `description` — the description of the tie

One or more properties may be updated in each call to update().


## `apex.attribute.MeshDependentTieCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `MeshDependentTieCollection() -> None` — Construct a new MeshDependentTieCollection.

## `apex.attribute.NSMCombination`  (extends `Entity`, `IName`)
A class to represent NSM Combination(NSMADD).
Properties: `id`, `NSM`

Methods:

- `getId() -> int` — Returns ID of the NSM Combination. If omits, the system will automatically assign an ID.
- `getNSM() -> apex.attribute.NonstructuralMassCollection` — Returns A collection of NSM for the NSM Combination.
#### `update(name: str, description: str, id: int, NSM: NonstructuralMassCollection) -> apex.attribute.NSMCombination`
Creates and returns a NSMCombination.

- `name` — Optional name for the NSM Combination.
- `description` — Optional string providing a description for the NSM Combination.
- `id` — ID of the NSM Combination. If omits, the system will automatically assign an ID.
- `NSM` — A collection of interactions for the NSM Combination.


## `apex.attribute.NSMCombinationCollection`  (extends `EntityCollection`)
Iterable collection of NSMCombination, based on EntityCollection.

Methods:

- `NSMCombinationCollection() -> None` — Construct a new NSMCombinationCollection.

## `apex.attribute.NodeTie`  (extends `Entity`, `IDisplayable`, `IIdentifier`, `IPhysical`, `IUserAttributes`, `IName`)
Contains NodeTies and methods for editing/getting NodeTie attributes.
Properties: `attachmentDOFAndWeights`, `attachmentRegions`, `dependentDof`, `distributionMode`, `distributionType`, `dOFDefinitionMode`, `referencePoint`, `thermalExpansionCoeff`

Methods:

- `getAttachmentDOFAndWeights() -> {str:{str:float}}` — Returns a map of NodeIds, attachment DOF and attachment weights of the NodeTie. The parameter DOFAndWeightFactors is a map. The Key is NodeID. The value is a map. In the value map, the key is a sub string of "123456" representing the DOF. And the value is a double weight factor: Example from the user story figure on DoF and eight Factor: 'Individual' Case: { "Assembly 3/Assembly 1/Part 1:1" : {"1" :1.0,"2" :2.0,}, "Assembly 3/Assembly 2/Part 1:1" : {"1" :3.01,}, }
- `getAttachmentRegions() -> apex.EntityCollection` — Returns attachment regions of the NodeTie.
- `getDOFDefinitionMode() -> str` — Returns DOF Definition Mode of the NodeTie.
- `getDependentDof() -> str` — Returns dependent DOF of the NodeTie.
- `getDistributionMode() -> str` — Returns Distribution Mode of the NodeTie.
- `getDistributionType() -> str` — Returns Distribution Type of the NodeTie.
- `getReferencePoint() -> apex.Entity` — Returns reference point of the NodeTie.
- `getThermalExpansionCoeff() -> float` — Returns thermalExpansionCoeff of the NodeTie.
#### `update(attachmentRegions: apex.EntityCollection, dependentDoF: str, dofDefinitionMode: apex.attribute.DOFDefinitionMode, distributionType: apex.attribute.DistributionType, distributionMode: apex.attribute.DistributionMode, referencePoint: Entity, DOFAndWeightFactors: {str:{str:float}}, thermalExpansionCoeff: float, deleteUnreferencedNode: bool) -> None`
Update this NodeTie properties.

- `attachmentRegions` — of this NodeTie
- `dependentDoF` — of this NodeTie
- `dofDefinitionMode` — of this NodeTie
- `distributionType` — of this NodeTie
- `distributionMode` — of this NodeTie
- `referencePoint` — of this NodeTie
- `DOFAndWeightFactors` — of this NodeTie
- `thermalExpansionCoeff` — of this NodeTie
- `deleteUnreferencedNode` — of this NodeTie

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.NodeTieCollection`  (extends `EntityCollection`)
Iterable collection of NodeTie, based on EntityCollection.

Methods:

- `NodeTieCollection() -> None` — Construct a new NodeTieCollection.

## `apex.attribute.NonstructuralMass`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IName`)
Class NonstructuralMass.
Properties: `constantMass`, `id`, `massDistribution`, `nonstructuralMassType`, `target`, `variableMass`

Methods:

- `getConstantMass() -> float` — Returns constant mass of the NonstructuralMass.
- `getID() -> int` — Returns ID of the NonstructuralMass.
- `getMassDistribution() -> apex.attribute.MassDistribution` — Returns MassDistribution of the NonstructuralMass.
- `getNonstructuralMassType() -> apex.attribute.NonstructuralMassType` — Returns NonstructuralMassType of the NonstructuralMass.
- `getTarget() -> apex.EntityCollection` — Returns target of the NonstructuralMass.
- `getVariableMass() -> {float:apex.EntityCollection}` — Returns variable mass of the NonstructuralMass.
#### `update(name: str, description: str, id: int, massDistribution: apex.attribute.MassDistribution, nonstructuralMassType: apex.attribute.NonstructuralMassType, constantMass: float, target: apex.EntityCollection, variableMass: {float:apex.EntityCollection}) -> None`
Update this NonstructuralMass properties.

- `name` — of this NonstructuralMass
- `description` — of this NonstructuralMass
- `id` — of this NonstructuralMass
- `massDistribution` — of this NonstructuralMass
- `nonstructuralMassType` — of this NonstructuralMass
- `constantMass` — of this NonstructuralMass
- `target` — of this NonstructuralMass
- `variableMass` — of this NonstructuralMass

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.NonstructuralMassCollection`  (extends `EntityCollection`, `IUserHighlightable`)
Iterable collection of NonstructuralMass, based on EntityCollection.

Methods:

- `NonstructuralMassCollection() -> None` — Construct a new NonstructuralMassCollection.

## `apex.attribute.PerfectlyPlastic`  (extends `Plasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `initialYieldStress`

Methods:

#### `PerfectlyPlastic(initialYieldStress: float, yieldCriteria: YieldCriteria) -> None`
Constructor.

- `initialYieldStress` — Define the initial Yield Stress for the Plasticity model
- `yieldCriteria` — Define a yield Criteria for the plasticity model

Usage example:$$ New the Plasticity constitutive model with the initial Yield stress and yieldCriteria.myPlasticity = apex.attribute.PlasticityPerfectly(initialYieldStress= 200.0, yieldCriteria= myYieldCriteria2 )

- `getInitialYieldStress() -> float`
- `setInitialYieldStress(initialYieldStress: float) -> None`
#### `update(initialYieldStress: float, yieldCriteria: YieldCriteria) -> None`
the update method used to edit the Plasticity constitutive model

- `initialYieldStress` — optional for update method, Define the initial Yield Stress for the Plasticity model
- `yieldCriteria` — optional for update method, Define a yield Criteria for the plasticity model

Usage example:$$ edit the Plasticity constitutive model with the initial Yield stress and yieldCriteria.myPlasticity.update(initialYieldStress= 200.0, yieldCriteria= myYieldCriteria2 )The parameters in the update method are optional, only the parameters specified in the update method will be edited, others will remain as is.


## `apex.attribute.PlanarJoint`  (extends `Joint`)
Contains PlanarJoint and methods for editing/getting PlanarJoint attributes.

Methods:

#### `update(name: str, description: str, jointAxis: apex.attribute.JointAxis, side1: apex.EntityCollection, side1DistributionType: apex.attribute.DistributionType, side2: apex.EntityCollection, side2DistributionType: apex.attribute.DistributionType, jointOrigin: apex.Entity, jointOrientation: apex.construct.Orientation, axisLocationMode: apex.attribute.AxisLocationMode, jointRenderType: apex.attribute.JointRenderType) -> None`
Update this PlanarJoint properties.

- `name` — of this PlanarJoint
- `description` — of this PlanarJoint
- `jointAxis` — of this PlanarJoint
- `side1` — of this PlanarJoint
- `side1DistributionType` — of this PlanarJoint
- `side2` — of this PlanarJoint
- `side2DistributionType` — of this PlanarJoint
- `jointOrigin` — of this PlanarJoint
- `jointOrientation` — of this PlanarJoint
- `axisLocationMode` — of this PlanarJoint
- `jointRenderType` — of this PlanarJoint - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.Plasticity`  (extends `ConstitutiveModel`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `hardeningRule`, `yieldCriteria`

Methods:

- `getHardeningRule() -> apex.attribute.HardeningRule` — Gets There are 4 types of hardening method, they are Enumerated in HardeningRule, and each Plasticity Constitutive model should contain only one of the 4 hardening methods.
- `getYieldCriteria() -> YieldCriteria` — Gets There are six yield criteria rules, they are derived from the base class YieldCriteria. and each Plasticity Constitutive model should contain only one of the six yield criteria rules.
- `setHardeningRule(hardeningRule: apex.attribute.HardeningRule) -> None` — Sets There are 4 types of hardening method, they are Enumerated in HardeningRule, and each Plasticity Constitutive model should contain only one of the 4 hardening methods.
- `setYieldCriteria(yieldCriteria: YieldCriteria) -> None` — Sets There are six yield criteria rules, they are derived from the base class YieldCriteria. and each Plasticity Constitutive model should contain only one of the six yield criteria rules.

## `apex.attribute.PlasticityHardeningSlope`  (extends `Plasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `hardeningSlope`, `initialYieldStress`

Methods:

#### `PlasticityHardeningSlope(initialYieldStress: float, hardeningSlope: float, yieldCriteria: YieldCriteria, hardeningRule: apex.attribute.HardeningRule) -> None`
Constructor.

- `initialYieldStress` — Define the initial Yield Stress for the Plasticity model
- `hardeningSlope` — Define the hardening Slope for the Plasticity model
- `yieldCriteria` — Define a yield Criteria for the plasticity model
- `hardeningRule` — Define a hardening Rule for the plasticity model

Usage example:$$ New the Plasticity constitutive model with the initial Yield stress,hardening slope, yieldCriteria and hardeningRule.myPlasticity = apex.attribute.PlasticityHardeningSlope(initialYieldStress= 200.0, hardeningSlope= 12.3, yieldCriteria= myYieldCriteria2, hardeningRule= Isotropic )

- `getHardeningSlope() -> float`
- `getInitialYieldStress() -> float`
- `setHardeningSlope(hardeningSlope: float) -> None`
- `setInitialYieldStress(initialYieldStress: float) -> None`
#### `update(initialYieldStress: float, hardeningSlope: float, yieldCriteria: YieldCriteria, hardeningRule: apex.attribute.HardeningRule) -> None`
the update method

- `initialYieldStress` — optional for update method, Define the initial Yield Stress for the Plasticity model
- `hardeningSlope` — optional for update method, Define the hardening Slope for the Plasticity model
- `yieldCriteria` — optional for update method, Define a yield Criteria for the plasticity model
- `hardeningRule` — optional for update method, Define a hardening Rule for the plasticity model

Usage example:$$ Edit the Plasticity constitutive model with the initial Yield stress,hardening slope, yieldCriteria and hardeningRule.myPlasticity.update(initialYieldStress= 200.0, hardeningSlope= 12.3, yieldCriteria= myYieldCriteria2, hardeningRule= Isotropic )The parameters in the update method are optional, only the parameters specified in the update method will be edited, others will remain as is.


## `apex.attribute.PlasticityStressStrain`  (extends `Plasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `stressStrainCurve`

Methods:

#### `PlasticityStressStrain(stressStrainCurve: StressStrainCurve, yieldCriteria: YieldCriteria, hardeningRule: apex.attribute.HardeningRule = apex.attribute.HardeningRule.Isotropic) -> None`
Constructor.

- `stressStrainCurve` — M Used to define a stress-strain curve for the plasticity constitutive model.
- `yieldCriteria` — Define a yield Criteria for the plasticity model
- `hardeningRule` — define which hardening Rule will be used in the plasticity model

Usage example:$$ New the Plasticity constitutive model with the stressStrainCurve, yieldCriteria and hardeningRule.myPlasticity = apex.attribute.PlasticityStressStrain(stressStrainCurve = mystressStrainCurve, yieldCriteria = myYieldCriteria2, hardeningRule = Isotropic )

- `getStressStrainCurve() -> StressStrainCurve` — Gets Used to define the stress-strain curve for Plasticity constitutive model.
- `setStressStrainCurve(stressStrainCurve: StressStrainCurve) -> None` — Sets Used to define the stress-strain curve for Plasticity constitutive model.
#### `update(stressStrainCurve: StressStrainCurve, yieldCriteria: YieldCriteria, hardeningRule: apex.attribute.HardeningRule = apex.attribute.HardeningRule.Isotropic) -> None`
the update method used to edit the Plasticity constitutive model

- `stressStrainCurve` — optional Used to define a stress-strain curve for the plasticity constitutive model.
- `yieldCriteria` — optional Define a yield Criteria for the plasticity model
- `hardeningRule` — optional define which hardening Rule will be used in the plasticity model

Usage example:$$ update the Plasticity constitutive model with the stressStrainCurve, yieldCriteria and hardeningRule.myPlasticity.update(stressStrainCurve = mystressStrainCurve, yieldCriteria = myYieldCriteria2, hardeningRule = Isotropic )The parameters in the update method are optional, only the parameters specified in the update method will be edited, others will remain as is.


## `apex.attribute.Ply`  (extends `Entity`)
Class Ply.
Properties: `angle`, `color`, `coverageArea`, `coverageRegion`, `id`, `material`, `name`, `thickness`

Methods:

- `getAngle() -> float` — Gets the angle of this Ply.
- `getColor() -> apex.ColorRGB` — Gets the color associated with this Ply.
- `getCoverageArea() -> float` — Gets the area of the coverage region that this ply is associated with.
- `getCoverageRegion() -> apex.EntityCollection` — Gets the entities in the LayeredPanel that this Ply is associated with.
- `getId() -> int` — Gets the id of the ply, it's an external ply id that can be used in different zones and panels.
- `getMaterial() -> apex.attribute.Material` — Gets the material associated with this ply. material may be omitted only if materialSheet is provided in which case this property will be set to the Material defined by the MaterialSheet.
- `getName() -> str` — Gets the name of this Ply. name must be unique within a LayeredPanel. If a non-unique name is provided the system will silently modify the provided name to make it unique by appending an integer.
- `getThickness() -> float` — Gets the thickness associated with this Ply thickness may be omitted only if materialSheet is provided in which case this property will be set to the thickness defined by the MaterialSheet thickness represents a Length quantity and is defined using the unit of Length from the active script unit system.
- `setAngle(angle: float) -> None` — Sets the angle of this Ply.
- `setColor(color: apex.ColorRGB) -> None` — Sets the color associated with this Ply.
- `setCoverageRegion(coverageRegion: apex.EntityCollection) -> None` — Sets the entities in the LayeredPanel that this Ply is associated with.
- `setId(id: int) -> None` — Sets the id of the ply, it's an external ply id that can be used in different zones and panels.
- `setMaterial(material: apex.attribute.Material) -> None` — Sets the material associated with this ply. material may be omitted only if materialSheet is provided in which case this property will be set to the Material defined by the MaterialSheet.
- `setName(name: str) -> None` — Sets the name of this Ply. name must be unique within a LayeredPanel. If a non-unique name is provided the system will silently modify the provided name to make it unique by appending an integer.
- `setThickness(thickness: float) -> None` — Sets the material associated with this ply. material may be omitted only if materialSheet is provided in which case this property will be set to the Material defined by the MaterialSheet.
#### `update(id: int, name: str, color: [int], material: apex.attribute.Material, thickness: float, angle: float, coverageRegion: apex.EntityCollection) -> None`
Update this Ply properties.

- `id` — of this Ply
- `name` — of this Ply
- `color` — of this Ply
- `material` — of this Ply
- `thickness` — of this Ply
- `angle` — of this Ply
- `coverageRegion` — of this Ply

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.PlyCollection`  (extends `EntityCollection`)
Iterable collection of Ply, based on EntityCollection.

Methods:

- `PlyCollection() -> None` — Construct a new PlyCollection.

## `apex.attribute.PointMass`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class PointMass.
Properties: `ixx`, `ixy`, `ixz`, `iyy`, `iyz`, `izz`, `location`, `mass`, `massMatrix`, `orientation`, `target`

Methods:

- `getIxx() -> float` — Returns ixx of the PointMass.
- `getIxy() -> float` — Returns ixy of the PointMass.
- `getIxz() -> float` — Returns ixz of the PointMass.
- `getIyy() -> float` — Returns iyy of the PointMass.
- `getIyz() -> float` — Returns iyz of the PointMass.
- `getIzz() -> float` — Returns izz of the PointMass.
- `getLocation() -> apex.Coordinate` — Returns Coordinate of the PointMass.
- `getMass() -> float` — Returns mass of the PointMass.
- `getMassMatrix() -> apex.attribute.PointMassMatrix` — Returns massMatrix of the PointMass. Returns None if the PointMass does not use mass matrix.
- `getOrientation() -> apex.construct.Orientation` — Returns apex.construct.Orientation of the PointMass.
- `getTarget() -> apex.EntityCollection` — Returns a read only collection of the entities that the PointMass is applied to.
- `getUseMassMatrix() -> bool` — Returns a bool value to indicate the PointMass use inertia matrix or not.
#### `update(name: str, mass: float, ixx: float, iyy: float, izz: float, ixy: float, ixz: float, iyz: float, massMatrix: apex.attribute.PointMassMatrix, applicationMethod: apex.attribute.ApplicationMethod, location: apex.Coordinate, target: apex.EntityCollection, orientation: apex.construct.Orientation, description: str, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this PointMass properties.

- `name` — of this PointMass
- `mass` — of this PointMass
- `ixx` — of this PointMass
- `iyy` — of this PointMass
- `izz` — of this PointMass
- `ixy` — of this PointMass
- `ixz` — of this PointMass
- `iyz` — of this PointMass
- `massMatrix` — mass matrix of this PointMass
- `applicationMethod` — of this PointMass
- `location` — of this PointMass
- `target` — of this PointMass
- `orientation` — of this PointMass
- `description` — of this PointMass
- `color` — of this PointMass
- `renderStyle` — of this PointMass
- `enableTransparency` — of this PointMass
- `transparencyLevel` — of this PointMass

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.PointMassCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `PointMassCollection() -> None` — Construct a new PointMassCollection.

## `apex.attribute.PointMassMatrix`
Properties: `M11`, `M21`, `M22`, `M31`, `M32`, `M33`, `M41`, `M42`, `M43`, `M44`, `M51`, `M52`, `M53`, `M54`, `M55`, `M61`, `M62`, `M63`, `M64`, `M65`, `M66`

Methods:

- `getM11() -> float`
- `getM21() -> float`
- `getM22() -> float`
- `getM31() -> float`
- `getM32() -> float`
- `getM33() -> float`
- `getM41() -> float`
- `getM42() -> float`
- `getM43() -> float`
- `getM44() -> float`
- `getM51() -> float`
- `getM52() -> float`
- `getM53() -> float`
- `getM54() -> float`
- `getM55() -> float`
- `getM61() -> float`
- `getM62() -> float`
- `getM63() -> float`
- `getM64() -> float`
- `getM65() -> float`
- `getM66() -> float`
- `setM11(newVal: float) -> None`
- `setM21(newVal: float) -> None`
- `setM22(newVal: float) -> None`
- `setM31(newVal: float) -> None`
- `setM32(newVal: float) -> None`
- `setM33(newVal: float) -> None`
- `setM41(newVal: float) -> None`
- `setM42(newVal: float) -> None`
- `setM43(newVal: float) -> None`
- `setM44(newVal: float) -> None`
- `setM51(newVal: float) -> None`
- `setM52(newVal: float) -> None`
- `setM53(newVal: float) -> None`
- `setM54(newVal: float) -> None`
- `setM55(newVal: float) -> None`
- `setM61(newVal: float) -> None`
- `setM62(newVal: float) -> None`
- `setM63(newVal: float) -> None`
- `setM64(newVal: float) -> None`
- `setM65(newVal: float) -> None`
- `setM66(newVal: float) -> None`

## `apex.attribute.PointSensor`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
Class PointSensor.
Properties: `activateChannelMask`, `orientation`, `target`

Methods:

- `getActivateChannelMask() -> [bool]` — Returns activateChannelMask of the PointSensor.
- `getOrientation() -> apex.construct.Orientation` — Returns apex.construct.Orientation of the PointSensor.
- `getTarget() -> apex.EntityCollection` — "Returns a read only Entity identifying the entity that the PointSensor is associated with.
#### `update(name: str, target: apex.EntityCollection, activateChannelMask: [bool], orientation: apex.construct.Orientation, description: str, color: [int], renderStyle: apex.session.DisplayRenderStyle, enableTransparency: apex.ApexBool, transparencyLevel: int) -> None`
Update this PointSensor properties.

- `name` — of this PointSensor
- `target` — the entity that the PointSensor is associated with
- `activateChannelMask` — of this PointSensor
- `orientation` — of this PointSensor
- `description` — of this PointSensor
- `color` — of this PointSensor
- `renderStyle` — of this PointSensor
- `enableTransparency` — of this PointSensor
- `transparencyLevel` — of this PointSensor

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.PointSensorCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `PointSensorCollection() -> None` — Construct a new PointSensorCollection.

## `apex.attribute.PrismaticJoint`  (extends `Joint`)
Contains PrismaticJoint and methods for editing/getting PrismaticJoint attributes.

Methods:

#### `update(name: str, description: str, jointAxis: apex.attribute.JointAxis, side1: apex.EntityCollection, side1DistributionType: apex.attribute.DistributionType, side2: apex.EntityCollection, side2DistributionType: apex.attribute.DistributionType, jointOrigin: apex.Entity, jointOrientation: apex.construct.Orientation, axisLocationMode: apex.attribute.AxisLocationMode, jointRenderType: apex.attribute.JointRenderType) -> None`
Update this PrismaticJoint properties.

- `name` — of this PrismaticJoint
- `description` — of this PrismaticJoint
- `jointAxis` — of this PrismaticJoint
- `side1` — of this PrismaticJoint
- `side1DistributionType` — of this PrismaticJoint
- `side2` — of this PrismaticJoint
- `side2DistributionType` — of this PrismaticJoint
- `jointOrigin` — of this PrismaticJoint
- `jointOrientation` — of this PrismaticJoint
- `axisLocationMode` — of this PrismaticJoint
- `jointRenderType` — of this PrismaticJoint - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.Properties2DModel`  (extends `Entity`)
This class manages the Properties Models of a PropertiesElement2D.

Methods:

#### `Properties2DModel(properties2DModel: str) -> None`
Create Properties2DModel with Properties2D keyword name. All Properties2D can be: PRIMARY: "PSHELL" , "PSHEAR", “ PCOHE”,“PLPLANE” , SECONDARY: "PSHLN1", "PSHEARN", "PSHLN2". example: property2DModel_1 = apex.attribute.Properties2DModel(properties2DModel = 'PSHELL')

- `properties2DModel` — keyword of this Properties2DModel

- `getProperties() -> {str:value}` — This function will return the whole dictionary which stores the PropertiesElement2D properties.
- `getProperty(key: str) -> object` — The function is passed with an attribute name (bdf filed name), Returns the corresponding value of the attribute. For example: XXModel_.getProperty('T'), the "T" is the input, will return the thickness value. The return Type maybe different depend on the value return.
#### `update(elementProperties2D: {str:value}) -> None`
Update the Properties2DModel.

- `elementProperties2D` — A dictionary to define Properties2DModel properties. The key is a string of the property name, the value is of valid types.


## `apex.attribute.Properties3DModel`  (extends `Entity`)
This class manages the Properties Models of a PropertiesElement3D.

Methods:

- `Properties3DModel(properties3DModel: str) -> None` — Create Properties3DModel with Properties3D keyword name. All Properties3D can be: PRIMARY: "PSOLID", "PLSOLID" SECONDARY: "PSLDN1" example: property3DModel_1 = apex.attribute.Properties3DModel(properties2DModel = 'PSOLID')
- `getProperties() -> {str:value}` — This function will return the whole dictionary which stores the PropertiesElement3D properties.
- `getProperty(key: str) -> object` — The function is passed with an attribute name (bdf filed name), Returns the corresponding value of the attribute. For example: XXModel_.getProperty('T'), the "T" is the input, will return the thickness value. The return Type maybe different depend on the value return.
#### `update(elementProperties3D: {str:value}) -> None`
Update the Properties3DModel.

- `elementProperties3D` — A dictionary to define Properties3DModel properties. The key is a string of the property name, the value is of valid types.


## `apex.attribute.PropertiesElement2D`  (extends `Entity`, `IUserAttributes`, `IName`)
Class PropertiesElement2D. This class describes the property of 2D elements. This is the base class of 2D element property. It will derive 2D property derived classes representing different mechanical models, including: simple shell, shell, shear panel, plan strain, plan stress and Axisymmetric.
Properties: `coverageRegion`, `field`, `id`, `propertyType`, `references`, `target`

Methods:

#### `addSecondaryProperties2DModel(secondaryProperties2DModel: apex.attribute.Properties2DModel) -> bool`
This method is used to add a secondary Properties2D model to a PropertiesElement2D object.

- `secondaryProperties2DModel` — to be added

example: myPropertiesElement2D_1 = apex.catalog.createPropertiesElement2D(name="myPropertiesElement2D 1", description = "", primaryProperties2D = "PSHELL") property2DModel_ = apex.attribute.Properties2DModel( properties2DModel = 'PSHEARN' ) myPropertiesElement2D_1.addSecondaryProperties2DModel(secondaryProperties2DModel = property2DModel_)

- `asShearPanel() -> apex.attribute.ShearPanel` — Get ShearPanel entity when the type of 2D element property is apex.attribute.PropertiesElement2DType.ShearPanel.
- `asShell() -> apex.attribute.Shell` — Get Shell entity when the type of 2D element property is apex.attribute.PropertiesElement2DType.Shell.
- `asSimpleShell() -> apex.attribute.SimpleShell` — Get SimpleShell entity when the type of 2D element property is apex.attribute.PropertiesElement2DType.SimpleShell.
- `getCoverageRegion() -> Property2DCoverageRegion` — Get the Property2DCoverageRegion that this 2D element property is associated with.
- `getField() -> apex.Entity` — Get a field that this 2D element property.
- `getID() -> int` — Get the Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
#### `getProperties2DModel(properties2DModel: str) -> apex.attribute.Properties2DModel`
Returns specific Properties2D model via Properties2D model name which is assigned to a PropertiesElement2D.

- `properties2DModel` — Defined the Properties2D model name.

example: property2DModel_1 = myPropertiesElement2D_1 .getProperties2DModel(properties2DModel = 'PSHELL') Returns a certain Properties2D model added to the PropertiesElement2D.

- `getProperties2DModels() -> [apex.attribute.Properties2DModel]` — Returns all Properties2D models which are assigned to a PropertiesElement2D.
- `getPropertyType() -> apex.attribute.PropertiesElement2DType` — Get the type of 2D element property that will be activated for elements that are associated with this class. The type is indicated by an apex.attributes.PropertiesElement2DType enumeration and defaults to "SimpleShell".
- `getReferenceMaterial() -> apex.attribute.Material` — Get the material referenced in the PropertiesElement2D object.
- `getReferences() -> apex.EntityCollection` — Get a collection of all entities that this 2D element property directly references.
- `getTarget() -> apex.EntityCollection` — Get a collection of the entities that the PropertiesElement2D is applied to.
#### `removeProperties2DModel(properties2DModel: apex.attribute.Properties2DModel) -> None`
This method is used to remove a Properties2DModel model (if exists) from a PropertiesElement2D object.

- `properties2DModel` — to be removed

example: myPropertiesElement2D_1 = apex.catalog.createPropertiesElement2D(name="myPropertiesElement2D 1", description = "", primaryProperties2D = "PSHELL") property2DModel_ = apex.attribute.Properties2DModel( properties2DModel = 'PSHEARN' ) myPropertiesElement2D_1.addSecondaryProperties2DModel(secondaryProperties2DModel = property2DModel_) myPropertiesElement2D_1.removeProperties2DModel(properties2DModel = property2DModel_)

- `setID(id: int) -> None` — Set the Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
#### `setPrimaryProperties2DModel(primaryProperties2DModel: apex.attribute.Properties2DModel) -> None`
This method is used to set the primary Properties2D model to a PropertiesElement2D object.

- `primaryProperties2DModel` — to be set

example: myPropertiesElement2D_1 = apex.catalog.createPropertiesElement2D(name="myPropertiesElement2D 1", description = "", primaryProperties2D = "PSHELL") property2DModel_ = apex.attribute.Properties2DModel( properties2DModel = 'PSHEAR' ) myPropertiesElement2D_1.setPrimaryProperties2DModel(primaryProperties2DModel = property2DModel_)

- `setPropertyType(propertyType: apex.attribute.PropertiesElement2DType) -> None` — Set the type of 2D element property that will be activated for elements that are associated with this class. The type is indicated by an apex.attributes.PropertiesElement2DType enumeration and defaults to "SimpleShell".
- `setReferences(references: apex.EntityCollection) -> None` — Set a collection of all entities that this 2D element property directly references.
#### `update(name: str, description: str, id: int) -> None`
Update properties of this PropertiesElement2D.

- `name` — of this PropertiesElement2D
- `description` — of this PropertiesElement2D
- `id` — Optional - id of this PropertiesElement2D.


## `apex.attribute.PropertiesElement2DCollection`  (extends `EntityCollection`)
Iterable collection of PropertiesElement2D, based on EntityCollection.

Methods:

- `PropertiesElement2DCollection() -> None` — Construct a new PropertiesElement2DCollection.

## `apex.attribute.PropertiesElement3D`  (extends `Entity`, `IUserAttributes`, `IName`)
Class PropertiesElement3D. It's an element property that can be assigned to 3d elements only.
Properties: `id`, `target`

Methods:

#### `addSecondaryProperties3DModel(secondaryProperties3DModel: apex.attribute.Properties3DModel) -> bool`
This method is used to add a secondary Properties3D model to a PropertiesElement3D object.

- `secondaryProperties3DModel` — to be added

example: myPropertiesElement3D_1 = apex.catalog.createPropertiesElement3D(name="myPropertiesElement3D 1", description = "", primaryProperties3D = "PSOLID") property3DModel_ = apex.attribute.Properties3DModel( properties3DModel = 'PSHEARN' ) myPropertiesElement3D_1.addSecondaryProperties3DModel(secondaryProperties3DModel = property3DModel_)

- `getAssociatedElements() -> apex.mesh.ElementCollection` — Gets the elements associated with this PropertiesElement3D.
- `getID() -> int` — Get the ID of the PropertiesElement3D.
#### `getProperties3DModel(properties3DModel: str) -> apex.attribute.Properties3DModel`
Returns specific Properties3D model via Properties3D model name which is assigned to a PropertiesElement3D.

- `properties3DModel` — Defined the Properties3D model name.

example: property3DModel_1 = myPropertiesElement3D_1 .getProperties3DModel(properties3DModel = 'PSOLID') Returns a certain Properties3D model added to the PropertiesElement3D.

- `getProperties3DModels() -> [apex.attribute.Properties3DModel]` — Returns all Properties3D models which are assigned to a PropertiesElement3D.
- `getReferenceMaterial() -> apex.attribute.Material` — Get the material referenced in the PropertiesElement3D object.
- `getTarget() -> apex.EntityCollection` — Get a collection of the entities that the PropertiesElement3D is applied to.
#### `removeProperties3DModel(properties3DModel: apex.attribute.Properties3DModel) -> None`
This method is used to remove a Properties3DModel model (if exists) from a PropertiesElement3D object.

- `properties3DModel` — to be removed

example: myPropertiesElement3D_1 = apex.catalog.createPropertiesElement3D(name="myPropertiesElement3D 1", description = "", primaryProperties3D = "PSOLID") property3DModel_ = apex.attribute.Properties3DModel( properties3DModel = 'PSLDN1' ) myPropertiesElement3D_1.addSecondaryProperties3DModel(secondaryProperties3DModel = property3DModel_) myPropertiesElement3D_1.removeProperties3DModel(properties3DModel = property3DModel_)

#### `setPrimaryProperties3DModel(primaryProperties3DModel: apex.attribute.Properties3DModel) -> None`
This method is used to set the primary Properties3D model to a PropertiesElement3D object.

- `primaryProperties3DModel` — to be set

example: myPropertiesElement3D_1 = apex.catalog.createPropertiesElement3D(name="myPropertiesElement3D 1", description = "", primaryProperties3D = "PSOLID") property3DModel_ = apex.attribute.Properties3DModel( properties3DModel = 'PLSOLID' ) myPropertiesElement3D_1.setPrimaryProperties3DModel(primaryProperties3DModel = property3DModel_)

#### `update(name: str, description: str, id: int) -> None`
Update properties of this PropertiesElement3D.

- `name` — of this PropertiesElement3D
- `description` — of this PropertiesElement3D
- `id` — Optional - id of this PropertiesElement3D.


## `apex.attribute.PropertiesElement3DCollection`  (extends `EntityCollection`)
Iterable collection of PropertiesElement3D, based on EntityCollection.

Methods:

- `PropertiesElement3DCollection() -> None` — Construct a new PropertiesElement3DCollection.

## `apex.attribute.PropertiesElement3DHomogeneous`  (extends `PropertiesElement3D`)
Class PropertiesElement3DHomogeneous. It includes general properties for 3d elements including material, material orientation and several element behaviors.
Properties: `integrationNetwork`, `integrationScheme`, `materialOrientation`, `orientationType`, `outputLocation`, `referenceMaterial`

Methods:

- `getIntegrationNetwork() -> apex.attribute.IntegrationNetwork` — Get the integration network of the elements associated with the PropertiesElement3D.
- `getIntegrationScheme() -> apex.attribute.IntegrationScheme` — Get the integration scheme of the elements associated with the PropertiesElement3D.
- `getMaterialOrientation() -> apex.IOrientation` — Get the material orientation of the PropertiesElement3D when the orientationType is local.
- `getOrientationType() -> apex.attribute.OrientationType3D` — Get the material orientation type of the PropertiesElement3D.
- `getOutputLocation() -> apex.attribute.OutputLocation` — Get the location of the stress output.
- `getReferenceMaterial() -> apex.attribute.Material` — Get the material used in the PropertiesElement3D.
#### `update(name: str, description: str, id: int, target: apex.EntityCollection, referenceMaterial: apex.attribute.Material, orientationType: apex.attribute.OrientationType3D, materialOrientation: apex.IOrientation, integrationNetwork: apex.attribute.IntegrationNetwork, integrationScheme: apex.attribute.IntegrationScheme, outputLocation: apex.attribute.OutputLocation) -> None`
Updates this PropertiesElement3D. One or more properties may be updated in each call to update().

- `name` — Updates the name.
- `description` — Updates the description.
- `id` — Updates the id.
- `target` — Updates the target.
- `referenceMaterial` — Updates the reference material.
- `orientationType` — Updates the orientationType.
- `materialOrientation` — Updates the materialOrientation.
- `integrationNetwork` — Updates the integrationNetwork.
- `integrationScheme` — Updates the integrationScheme.
- `outputLocation` — Updates the outputLocation.


## `apex.attribute.Property2DCoverageRegion`  (extends `Entity`, `IPhysical`, `IUserAttributes`)
DEPRECATION NOTICE: THIS CLASS IS DEPRECATED AND WILL BE REMOVED IN THE FUTURE RELEASE. Class Property2DCoverageRegion. This class defines how the orientation of a 2D property is defined over a region of the model. Apex supports multiple methods to define how 2D property orientation varies across a region. It includes the scope of the region, the method used to define the 2D property orientation distribution and.
Properties: `alignmentMethod`, `coordinateSystem`, `director`, `name`, `Property2D`, `target`

Methods:

- `getAlignmentMethod() -> apex.attribute.Property2DAlignmentMethod` — Get the enumeration that indicates which method is used to define the 2D property orientation in this Property2DCoverageRegion.
- `getCoordinateSystem() -> apex.construct.CoordinateSystem` — Get the coordinate system whose X axis defines the 2D property orientation in this Property2DCoverageRegion. This attribute must be defined if the Property2DAlignmentMethod is of type apex.attribute.Property2DAlignmentMethod.CoordinstSystem. For all other MaterialAlignmentMethod types this attribute is ignored.
- `getDirector() -> apex.EntityCollection` — Get the collection of Curves and/or Edges that define how the Property 2D is oriented across this Property2DCoverageRegion. The director EntityCollection may contain only Curve or Edge entities. This attribute must be defined if the Property2DAlignmentMethod is of type apex.attribute.Property2DAlignmentMethod.Curve. For all other Property2DAlignmentMethod types this attribute is ignored.
- `getName() -> str` — Get the name of this Property2DCoverageRegion.
- `getProperty2D() -> apex.attribute.PropertiesElement2D` — Get the 2D property that is assigned to this coverage region.
- `getTarget() -> apex.EntityCollection` — Get the entities that are included in this Property2DCoverageRegion as an EntityCollection. Target may include Surfaces, Faces or 2D/3D elements. The target should be Surfaces, Faces or 2D elements and all other types will be silently ignored. Solids are internally expanded to the set of all exterior Faces of the Solids Note:if the 2D property created by refer section, the target will be NOT allowed edit, because the target of 2D property is determined by the section's target.
- `setCoordinateSystem(property2DAxis: apex.construct.CoordinateSystem) -> None` — Set the coordinate system whose X axis defines the 2D property orientation in this Property2DCoverageRegion. This attribute must be defined if the Property2DAlignmentMethod is of type apex.attribute.Property2DAlignmentMethod.CoordinstSystem. For all other MaterialAlignmentMethod types this attribute is ignored.
- `setDirector(director: apex.EntityCollection) -> None` — Set the collection of Curves and/or Edges that define how the Property 2D is oriented across this Property2DCoverageRegion. The director EntityCollection may contain only Curve or Edge entities. This attribute must be defined if the Property2DAlignmentMethod is of type apex.attribute.Property2DAlignmentMethod.Curve. For all other Property2DAlignmentMethod types this attribute is ignored.
- `setName(name: str) -> None` — Set the name of this Property2DCoverageRegion.
- `setTarget(target: apex.EntityCollection) -> None` — Set the entities that are included in this Property2DCoverageRegion as an EntityCollection. Target may include Surfaces, Faces or 2D/3D elements. The target should be Surfaces, Faces or 2D elements and all other types will be silently ignored. Solids are internally expanded to the set of all exterior Faces of the Solids Note:if the 2D property created by refer section, the target will be NOT allowed edit, because the target of 2D property is determined by the section's target.
#### `update(name: str, target: apex.EntityCollection, property2DAxis: apex.construct.CoordinateSystem, director: apex.EntityCollection) -> None`
Update the properties of this Property2DCoverageRegion. One or more properties may be updated in each call to update() and Properties that are not provided will be left unchanged.

- `name` — The name of this Property2DCoverageRegion.
- `target` — The collection of entities that the 2D property will be assigned to as an EntityCollection. target may contain Surfaces, Faces or 2D elements - all other types will be silently ignored. When Solids are included they are internally expanded to the complete set of free faces of the Solid. Any duplicate entities in target are ignored Noteif the 2D property created by refer section, the target will be NOT allowed edit, because the target of 2D property is determined by the section's target..
- `property2DAxis` — A Coordinate system whose X axis defines the 2D property orientation.
- `director` — A collection of Curves and/or Edges that will be used to define the orientation. director may include Curves or Edges. NOTE : Current releases of Apex support a single Curve or Edge only which must be the first entry in the collection. If the Collection includes more than one entry only the first will be used and all others will be silently ignored.


## `apex.attribute.Property2DCoverageRegionCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `Property2DCoverageRegionCollection() -> None` — Construct a new Property2DCoverageRegionCollection.

## `apex.attribute.RemotePointEntity`  (extends `Entity`)
RemotePointEntity Class Object.
Properties: `x`, `y`, `z`

Methods:

- `getX() -> float`
- `getY() -> float`
- `getZ() -> float`

## `apex.attribute.RevoluteJoint`  (extends `Joint`)
Contains RevoluteJoint and methods for editing/getting RevoluteJoint attributes.

Methods:

#### `update(name: str, description: str, jointAxis: apex.attribute.JointAxis, side1: apex.EntityCollection, side1DistributionType: apex.attribute.DistributionType, side2: apex.EntityCollection, side2DistributionType: apex.attribute.DistributionType, jointOrigin: apex.Entity, jointOrientation: apex.construct.Orientation, axisLocationMode: apex.attribute.AxisLocationMode, jointRenderType: apex.attribute.JointRenderType) -> None`
Update this RevoluteJoint properties.

- `name` — of this RevoluteJoint
- `description` — of this RevoluteJoint
- `jointAxis` — of this RevoluteJoint
- `side1` — of this RevoluteJoint
- `side1DistributionType` — of this RevoluteJoint
- `side2` — of this RevoluteJoint
- `side2DistributionType` — of this RevoluteJoint
- `jointOrigin` — of this RevoluteJoint
- `jointOrientation` — of this RevoluteJoint
- `axisLocationMode` — of this RevoluteJoint
- `jointRenderType` — of this RevoluteJoint - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.RigidFace`  (extends `Entity`, `IDisplayable`, `IUserHighlightable`, `IUserAttributes`, `IName`)
A class to represent Rigid face.
Properties: `curveSubdivisions`, `id`, `referenceBody`, `rigidFaceType`, `subdivisionsUdirection`, `subdivisionsVdirection`, `trimmingCurvesID`, `trimmingCurvesSubdivisions`

Methods:

- `getCurveSubdivisions() -> int` — Int value to represent curve Subdivision number. This attribute is only used when rigidFacType = BCNURBS2.
- `getId() -> int` — ID of the rigid face. If omits, the system will automatically assign an ID.
- `getReferenceBody() -> apex.Entity` — Return Nurbs geometry body when rigidFacType = BCNURBS/BCNURB2 or patch mesh body when rigidFacType = BCPATCH.
- `getRigidFaceType() -> apex.attribute.RigidFaceType` — Defines the rigid face type.
- `getSubdivisionsUdirection() -> int` — Returns subdivisions in U direction for a Nurbs surface when rigidFacType = BCNURBS.
- `getSubdivisionsVdirection() -> int` — Returns subdivisions in V direction for a Nurbs surface when rigidFacType = BCNURBS.
- `getTrimmingCurvesID() -> {apex.Entity:int}` — A dictionary to represent trimming curves ID for Nurbs body. This attribute is only used when rigidFacType = BCNURBS. The key is apex.Entity of trimming curve; the value is int of ID of trimming curve.
- `getTrimmingCurvesSubdivisions() -> {apex.Entity:int}` — A dictionary to represent trimming curves Subdivision for Nurbs body. This attribute is only used when rigidFacType = BCNURBS. The key is apex.Entity of trimming curve ; the value is int of Subdivision number of trimming curve.
#### `update(name: str, description: str, id: int, subdivisionsUdirection: int, subdivisionsVdirection: int, curveSubdivisions: int, trimmingCurvesID: {apex.Entity:int}, trimmingCurvesSubdivisions: {apex.Entity:int}) -> None`
update the rigid face.

- `name` — Optional name for the rigid face.
- `description` — Optional string providing a description for the rigid face.
- `id` — ID of the rigid face.
- `subdivisionsUdirection` — Optional, Subdivisions in U direction, it is only used when rigidFacType = BCNURBS.
- `subdivisionsVdirection` — Optional, Subdivisions in V direction, it is only used when rigidFacType = BCNURBS.
- `curveSubdivisions` — Optional, Int value to represent curve Subdivision number. This attribute is only used when rigidFacType = BCNURBS2.
- `trimmingCurvesID` — Optional, a dictionary to represent trimming curves ID for Nurbs body. This attribute is only used when rigidFacType = BCNURBS. The key is apex.Entity of trimming curve; the value is int of ID of trimming curve.
- `trimmingCurvesSubdivisions` — Optional, a dictionary to represent trimming curves Subdivision for Nurbs body. This attribute is only used when rigidFacType = BCNURBS. The key is apex.Entity of trimming curve ; the value is int of Subdivision number of trimming curve.


## `apex.attribute.RigidFaceCollection`  (extends `EntityCollection`)
Iterable collection of RigidFace, based on EntityCollection.

Methods:

- `RigidFaceCollection() -> None` — Construct a new RigidFaceCollection.

## `apex.attribute.RigidLink`  (extends `Connector`)

## `apex.attribute.RigidLinkCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `RigidLinkCollection() -> None` — Construct a new RigidLinkCollection.

## `apex.attribute.RigidLinkRepProperties`  (extends `ConnectorDiscreteProperty`)
Class RigidLinkRepProperties. The RigidLinkRepProperties does not have any attributes.
Properties: `referenceTemperature`, `thermalExpansionCoefficient`

Methods:

- `getReferenceTemperature() -> float` — reference temperature of rigid link
- `getThermalExpansionCoefficient() -> float` — thermal expansion coefficient of rigid link
#### `update(thermalExpansionCoefficient: float, referenceTemperature: float) -> None`
Update this connector properties.

- `thermalExpansionCoefficient` — update thermal expansion coefficient.
- `referenceTemperature` — reference Temperature.

One or more properties may be updated in each call to update().


## `apex.attribute.SectionCollection`  (extends `EntityCollection`)
This Class is no longer supported in Apex.

Methods:

- `SectionCollection() -> None` — Construct a new SectionCollection.

## `apex.attribute.ShearPanel`  (extends `PropertiesElement2D`)
Class ShearPanel. This class describes the shear panel behavior of shell elements.
Properties: `effectiveFactor1`, `effectiveFactor2`, `nonStructuralMass`, `shearMaterial`, `thickness`

Methods:

- `getEffectiveFactor1() -> float` — Get the Effectiveness factor for extensional stiffness along edges 1-2 and 3-4.
- `getEffectiveFactor2() -> float` — Get the Effectiveness factor for extensional stiffness along edges 1-2 and 3-4.
- `getNonStructuralMass() -> float` — Get the Nonstructural mass per unit area.
- `getShearMaterial() -> apex.attribute.Material` — Get the Material identification of a MAT1 entry.
- `getThickness() -> float` — Get the Thickness value of shear panel.
- `setEffectiveFactor1(effectiveFactor1: float) -> None` — Set the Effectiveness factor for extensional stiffness along edges 1-2 and 3-4.
- `setEffectiveFactor2(effectiveFactor2: float) -> None` — Set the Effectiveness factor for extensional stiffness along edges 1-2 and 3-4.
- `setNonStructuralMass(nonStructuralMass: float) -> None` — Set the Nonstructural mass per unit area.
- `setShearMaterial(shearMaterial: apex.attribute.Material) -> None` — Set the Material identification of a MAT1 entry.
- `setThickness(thickness: float) -> None` — Set the Thickness value of shear panel.
#### `update(name: str, description: str, id: int, thickness: float, shearMaterial: apex.attribute.Material, nonStructuralMass: float, effectiveFactor1: float, effectiveFactor2: float, references: apex.EntityCollection) -> None`
Used to update the attribute for shear panel.

- `name` — the name of this object as a string
- `description` — the description of this object as a string
- `id` — the Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
- `thickness` — the Thickness value of shear panel
- `shearMaterial` — Material identification of a MAT1 entry
- `nonStructuralMass` — Nonstructural mass per unit area
- `effectiveFactor1` — Effectiveness factor for extensional stiffness along edges 1-2 and 3-4
- `effectiveFactor2` — Effectiveness factor for extensional stiffness along edges 1-2 and 3-4
- `references` — A collection of all entities that this 2D element property directly references


## `apex.attribute.Shell`  (extends `PropertiesElement2D`)
Class Shell. the 2D Element Property with SHELL type can be used to define the material ID for the membrane properties, the bending properties, the transverse shear properties, the bending-membrane coupling properties, and the bending and transverse shear parameters. By choosing the appropriate materials and parameters, virtually any plate configuration may be obtained.
Properties: `bendingMaterial`, `bendingRatio`, `bottomFiberDistance`, `couplingMaterial`, `enableBendingStiffness`, `enableCoupling`, `enableMembraneStiffness`, `enableTransverseShearStiffness`, `membraneMaterial`, `nonStructuralMass`, `offset`, `thickness`, `topFiberDistance`, `transverseShearRatio`, `transversMaterial`

Methods:

- `getBendingMaterial() -> apex.attribute.Material` — Get the Bending Material of this 2D element property. this will allow user create the 2D element property by refer a existing material. this means that the Bending will use the referred material.
- `getBendingRatio() -> float` — Get the bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `getBottomFiberDistance() -> float` — Get the BottomFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `getCouplingMaterial() -> apex.attribute.Material` — Get the CouplingMaterial of this 2D element property. Material identification for membrane-bending coupling.
- `getEnableBendingStiffness() -> bool` — Get the EnableBendingStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `getEnableCoupling() -> bool` — Get the EnableCoupling of this 2D element property. Boolean value (Default = False) that defines whether or not membrane-bending coupling stiffness is activated. This value is only applicable if the 2D element property Type is set to "Shell".
- `getEnableMembraneStiffness() -> bool` — Get the EnableMembraneStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `getEnableTransverseShearStiffness() -> bool` — Get the EnableTransverseShearStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `getMembraneMaterial() -> apex.attribute.Material` — Get the Membrane Material of this 2D element property. this will allow user create the 2D element property by refer a existing material. this means that the Membrane will use the referred material.
- `getNonStructuralMass() -> float` — Get the NonStructuralMass of this 2D element property. Define the Nonstructural mass per unit area.
- `getOffset() -> float` — Get the Offset from the surface of grid points to the element reference plane.
- `getThickness() -> float` — Get the membrane thickness of this 2D element property. Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries.
- `getTopFiberDistance() -> float` — Get the TopFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `getTransversMaterial() -> apex.attribute.Material` — Get the Transvers Material of this 2D element property. this will allow user create the 2D element property by refer a existing material. this means that the Transvers Shear will use the referred material.
- `getTransverseShearRatio() -> float` — Get the transverse shear thickness ratio of this 2D element property. Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
- `setBendingMaterial(bendingMaterial: apex.attribute.Material) -> None` — Set the Bending Material of this 2D element property. this will allow user create the 2D element property by refer a existing material. this means that the Bending will use the referred material.
- `setBendingRatio(bendingRatio: float) -> None` — Set the bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `setBottomFiberDistance(bottomFiberDistance: float) -> None` — Set the BottomFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `setCouplingMaterial(couplingMaterial: apex.attribute.Material) -> None` — Set the CouplingMaterial of this 2D element property. Material identification for membrane-bending coupling.
- `setEnableBendingStiffness(enableBendingStiffness: apex.ApexBool) -> None` — Set the EnableBendingStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `setEnableCoupling(enableCoupling: apex.ApexBool) -> None` — Set the EnableCoupling of this 2D element property. Boolean value (Default = False) that defines whether or not membrane-bending coupling stiffness is activated. This value is only applicable if the 2D element property Type is set to "Shell".
- `setEnableMembraneStiffness(enableMembraneStiffness: apex.ApexBool) -> None` — Set the EnableMembraneStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `setEnableTransverseShearStiffness(enableTransverseShearStiffness: apex.ApexBool) -> None` — Set the EnableTransverseShearStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `setMembraneMaterial(membraneMaterial: apex.attribute.Material) -> None` — Set the Membrane Material of this 2D element property. this will allow user create the 2D element property by refer a existing material. this means that the Membrane will use the referred material.
- `setNonStructuralMass(nonStructuralMass: float) -> None` — Set the NonStructuralMass of this 2D element property. Define the Nonstructural mass per unit area.
- `setOffset(offset: float) -> None` — Set the Offset from the surface of grid points to the element reference plane.
- `setThickness(thickness: float) -> None` — Set the membrane thickness of this 2D element property. Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries.
- `setTopFiberDistance(topFiberDistance: float) -> None` — Set the TopFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `setTransversMaterial(transversMaterial: apex.attribute.Material) -> None` — Set the Transvers Material of this 2D element property. this will allow user create the 2D element property by refer a existing material. this means that the Transvers Shear will use the referred material.
- `setTransverseShearRatio(transverseShearRatio: float) -> None` — Set the transverse shear thickness ratio of this 2D element property. Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
#### `update(name: str, description: str, id: int, overrideSection: apex.ApexBool, thickness: float, offset: float, enableMembraneStiffness: apex.ApexBool, membraneMaterial: apex.attribute.Material, enableBendingStiffness: apex.ApexBool, bendingMaterial: apex.attribute.Material, bendingRatio: float, enableTransverseShearStiffness: apex.ApexBool, transversMaterial: apex.attribute.Material, transverseShearRatio: float, enableCoupling: apex.ApexBool, couplingMaterial: apex.attribute.Material, nonStructuralMass: float, topFiberDistance: float, bottomFiberDistance: float, references: apex.EntityCollection) -> None`
Used to update the attribute for shell. In the scripting we will allow user update the thickness/offset as below: 1. User create the object with a thickness/offset value , then only allow update the thickness/offset value. if user set a reference section, will return a error. since we can not support two thickness/offset definition methods at the same time. 2. User create the object with a reference section, it allowed to update the object with a new section (include the association). if user set a thickness/offset value for this object, will return a error. 3. others parameters should be able to update normally.

- `name` — the name of this object as a string
- `description` — the description for this object
- `id` — the Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
- `overrideSection` — the boolean argument to indicate whether the 2d element property overrides the section property when both of them are assigned to same entities.
- `thickness` — Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries.
- `offset` — Offset from the surface of grid points to the element reference plane.
- `enableMembraneStiffness` — Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `membraneMaterial` — this will allow user create the 2D element property by refer a existing material. This means that the Membrane will use the referred material
- `enableBendingStiffness` — Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `bendingMaterial` — this will allow user create the 2D element property by refer a existing material. this means that the Bending will use the referred material
- `bendingRatio` — Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `enableTransverseShearStiffness` — Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `transversMaterial` — This will allow user create the 2D element property by refer a existing material. This means that the Transvers Shear will use the referred material.
- `transverseShearRatio` — Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
- `enableCoupling` — Boolean value (Default = False) that defines whether or not membrane-bending coupling stiffness is activated. This value is only applicable if the 2D element property Type is set to "Shell".
- `couplingMaterial` — Material identification for membrane-bending coupling
- `nonStructuralMass` — Define the Nonstructural mass per unit area
- `topFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `bottomFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule
- `references` — A collection of all entities that this 2D element property directly references


## `apex.attribute.ShellBehavior`  (extends `Entity`, `IUserAttributes`, `IName`)
This Class is no longer supported in Apex. Refer to PropertiesElement2D to determine how this capability is now supported.
Properties: `bendingRatio`, `enableBendingStiffness`, `enableMembraneStiffness`, `enableTransverseShearStiffness`, `references`, `shellBehaviorType`, `transverseShearRatio`

Methods:

- `getBendingRatio() -> float` — Bending momnet of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `getEnableBendingStiffness() -> bool` — Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the ShellBehaviorType is set to "ThinShell" and is silently ignored for all other ShellBehaviorTypes.
- `getEnableMembraneStiffness() -> bool` — Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the ShellBehaviorType is set to "ThinShell" and is silently ignored for all other ShellBehaviorTypes.
- `getEnableTransverseShearStiffness() -> bool` — Boolean value (Default = True) that defines whether or not tranverse shear stiffness is activated. This value is only applicable if the ShellBehaviorType is set to "ThinShell" and is silently ignored for all other ShellBehaviorTypes.
- `getReferences() -> apex.EntityCollection` — returns a collection of all entities that this ShellBehavior directly references.
- `getShellBehaviorType() -> apex.attribute.ShellBehaviorType` — Selects the type of behavior that will be activated for elements that are associated with this class. The behavior type is indicated by an apex.attributes.ShellBehaviorType enumeration and defaults to "ThinShell".
- `getTransverseShearRatio() -> float` — Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if tranverse shear stiffness is active, otherwise it is silently ignored.
#### `update(name: str, description: str, shellBehaviorType: apex.attribute.ShellBehaviorType = apex.attribute.ShellBehaviorType.Undefined, enableMembraneStiffness: apex.ApexBool = ApexBoolUndefined, enableBendingStiffness: apex.ApexBool = ApexBoolUndefined, enableTransverseShearStiffness: apex.ApexBool = ApexBoolUndefined, bendingRatio: float, transverseShearRatio: float) -> None`
Updates one or more properties of the ShellBehavior. This method allows multiple properties of the ShellBehavior to be updated using a single method call. All arguments are optional and the values of all ShellBehavior properties associated with the omitted arguments are left unchanged.

- `name` — The Name of this ShellBehavior
- `description` — The Description of this ShellBehavior
- `shellBehaviorType` — The type of behavior that will be activated for elements that are associated with this class as an apex.attributes.ShellBehaviorType enumeration.
- `enableMembraneStiffness` — Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the ShellBehaviorType is set to "ThinShell" and is silently ignored for all other ShellBehaviorTypes
- `enableBendingStiffness` — Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the ShellBehaviorType is set to "ThinShell" and is silently ignored for all other ShellBehaviorTypes
- `enableTransverseShearStiffness` — Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the ShellBehaviorType is set to "ThinShell" and is silently ignored for all other ShellBehaviorTypes
- `bendingRatio` — Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `transverseShearRatio` — Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.


## `apex.attribute.ShellBehaviorCollection`  (extends `EntityCollection`)
This Class is no longer supported in Apex.

Methods:

- `ShellBehaviorCollection() -> None` — Construct a new ShellBehaviorCollection.

## `apex.attribute.ShellSection`  (extends `Entity`, `IUserAttributes`, `IName`)
This Class is no longer supported in Apex. Refer to ThicknessOffsetFieldConstant to determine how this capability is now supported.
Properties: `offset`, `references`, `target`, `thickness`

Methods:

- `getOffset() -> float` — Returns Offset of the ShellSection.
- `getReferences() -> apex.EntityCollection` — returns a collection of all entities that this ShellSection directly references
- `getTarget() -> apex.EntityCollection` — Returns a read only collection of the entities that the ShellSection is applied to.
- `getThickness() -> float` — Returns Thickness of the ShellSection.
- `recalculate() -> None` — recalculates the thickness and offset fields/values for this Section using the current locations of the pairs of Faces that were used to create the Section. This method will only affect ShellSections that were created using the automatic thickness tool or automatic mid-surface extraction tool. The method will be silently ignored if called on ShellSections that were not created using these methods.
#### `update(name: str, description: str, thickness: float, offset: float) -> None`
Update this ShellSection properties.

- `name` — of this ShellSection
- `description` — of this ShellSection
- `thickness` — of this ShellSection
- `offset` — of this ShellSection

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.SimpleShell`  (extends `PropertiesElement2D`)
Class SimpleShell. A simple shell is provided for users to quickly create simple thin-plate shell attributes. In most cases, the user only needs to simply fill in the thickness to complete the definition of the attribute, while others use the default settings.
Properties: `bendingRatio`, `bottomFiberDistance`, `enableBendingStiffness`, `enableMembraneStiffness`, `enableTransverseShearStiffness`, `nonStructuralMass`, `offset`, `referMaterial`, `thickness`, `topFiberDistance`, `transverseShearRatio`

Methods:

- `getBendingRatio() -> float` — Get the BendingRatio of this 2D element property. Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `getBottomFiberDistance() -> float` — Get the BottomFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `getEnableBendingStiffness() -> bool` — Get the EnableBendingStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `getEnableMembraneStiffness() -> bool` — Get the EnableMembraneStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `getEnableTransverseShearStiffness() -> bool` — Get the EnableTransverseShearStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `getNonStructuralMass() -> float` — Get the NonStructuralMass of this 2D element property. Define the Nonstructural mass per unit area.
- `getOffset() -> float` — Get the Offset of this 2D element property. Offset from the surface of grid points to the element reference plane.
- `getReferMaterial() -> apex.attribute.Material` — Get the ReferMaterial of this 2D element property. This will allow user create the 2D element property by refer a existing material. This means that all the Membrane, Bending, Transvers Shear will use the referred material.
- `getThickness() -> float` — Get the Thickness of this 2D element property. Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries. (Real or blank) Average thickness if TFLAG = 1 .
- `getTopFiberDistance() -> float` — Get the TopFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `getTransverseShearRatio() -> float` — Get the TransverseShearRatio of this 2D element property. Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
- `setBendingRatio(bendingRatio: float) -> None` — Set the BendingRatio of this 2D element property. Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `setBottomFiberDistance(bottomFiberDistance: float) -> None` — Set the BottomFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `setEnableBendingStiffness(enableBendingStiffness: apex.ApexBool) -> None` — Set the EnableBendingStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `setEnableMembraneStiffness(enableMembraneStiffness: apex.ApexBool) -> None` — Set the EnableMembraneStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `setEnableTransverseShearStiffness(enableTransverseShearStiffness: apex.ApexBool) -> None` — Set the EnableTransverseShearStiffness of this 2D element property. Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. his value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `setNonStructuralMass(nonStructuralMass: float) -> None` — Set the NonStructuralMass of this 2D element property. Define the Nonstructural mass per unit area.
- `setOffset(offset: float) -> None` — Set the Offset of this 2D element property. Offset from the surface of grid points to the element reference plane.
- `setReferMaterial(referMaterial: apex.attribute.Material) -> None` — Set the ReferMaterial of this 2D element property. This will allow user create the 2D element property by refer a existing material. This means that all the Membrane, Bending, Transvers Shear will use the referred material.
- `setThickness(thickness: float) -> None` — Set the Thickness of this 2D element property. Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries. (Real or blank) Average thickness if TFLAG = 1 .
- `setTopFiberDistance(topFiberDistance: float) -> None` — Set the TopFiberDistance of this 2D element property. Fiber distances for stress calculations. The positive direction is determined by the right-hand rule.
- `setTransverseShearRatio(transverseShearRatio: float) -> None` — Set the TransverseShearRatio of this 2D element property. Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
#### `update(name: str, description: str, id: int, overrideSection: apex.ApexBool, thickness: float, offset: float, referMaterial: apex.attribute.Material, enableMembraneStiffness: apex.ApexBool, enableBendingStiffness: apex.ApexBool, enableTransverseShearStiffness: apex.ApexBool, bendingRatio: float, transverseShearRatio: float, nonStructuralMass: float, topFiberDistance: float, bottomFiberDistance: float, references: apex.EntityCollection) -> None`
Used to update the attribute for simple shell. In the scripting we will allow user update the thickness/offset as below: 1. User create the object with a thickness/offset value , then only allow update the thickness/offset value. if user set a reference section, will return a error. since we can not support two thickness/offset definition methods at the same time. 2. User create the object with a reference section, it allowed to update the object with a new section (include the association). if user set a thickness/offset value for this object, will return a error. 3. others parameters should be able to update normally.

- `name` — Define the name for simple shell 2D element property
- `description` — Define the description for a simple 2d element property
- `id` — the Property identification number. (Integer > 0) If omitted, the system will assign a default ID which is the smallest and unique among all existing IDs.
- `overrideSection` — the boolean argument to indicate whether the 2d element property overrides the section property when both of them are assigned to same entities.
- `thickness` — Default membrane thickness for Ti on the connection entry. If T is blank then the thickness must be specified for Ti on the CQUAD4, CTRIA3, CQUAD8, and CTRIA6 entries. (Real or blank) Average thickness if TFLAG = 1 .
- `offset` — Offset from the surface of grid points to the element reference plane
- `referMaterial` — This will allow user create the 2D element property by refer a existing material. This means that all the Membrane, Bending, Transvers Shear will use the referred material
- `enableMembraneStiffness` — Boolean value (Default = True) that defines whether or not membrane stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `enableBendingStiffness` — Boolean value (Default = True) that defines whether or not bending stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `enableTransverseShearStiffness` — Boolean value (Default = True) that defines whether or not transverse shear stiffness is activated. This value is only applicable if the 2D element property Type is set to "simpleShell" or "Shell".
- `bendingRatio` — Bending moment of inertia (12I/T^3) ratio of the actual bending moment inertia of the shell, I, to the bending moment of inertia of a homogeneous shell (T^3/12). The default value is for a homogeneous shell.(1.0) This value is required if bending stiffness is active, otherwise it is silently ignored.
- `transverseShearRatio` — Transverse shear thickness ratio, Ts/T is the ratio of the shear thickness (Ts), to the membrane thickness (T) of the shell. The default value is for a homogeneous shell (0.833333). This value is used if transverse shear stiffness is active, otherwise it is silently ignored.
- `nonStructuralMass` — Define the Nonstructural mass per unit area
- `topFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule
- `bottomFiberDistance` — Fiber distances for stress calculations. The positive direction is determined by the right-hand rule
- `references` — A collection of all entities that this 2D element property directly references


## `apex.attribute.Spans`  (extends `Entity`, `IDisplayable`, `IUserAttributes`)
Class BeamSpan.

## `apex.attribute.SphericalJoint`  (extends `Joint`)
Contains SphericalJoint and methods for editing/getting SphericalJoint attributes.

Methods:

#### `update(name: str, description: str, jointAxis: apex.attribute.JointAxis, side1: apex.EntityCollection, side1DistributionType: apex.attribute.DistributionType, side2: apex.EntityCollection, side2DistributionType: apex.attribute.DistributionType, jointOrigin: apex.Entity, jointOrientation: apex.construct.Orientation, axisLocationMode: apex.attribute.AxisLocationMode, jointRenderType: apex.attribute.JointRenderType) -> None`
Update this SphericalJoint properties.

- `name` — of this SphericalJoint
- `description` — of this SphericalJoint
- `jointAxis` — of this SphericalJoint
- `side1` — of this SphericalJoint
- `side1DistributionType` — of this SphericalJoint
- `side2` — of this SphericalJoint
- `side2DistributionType` — of this SphericalJoint
- `jointOrigin` — of this SphericalJoint
- `jointOrientation` — of this SphericalJoint
- `axisLocationMode` — of this SphericalJoint
- `jointRenderType` — of this SphericalJoint - optional argument to control how the Apex Joint will be represented to Nastran. Use apex.attributes.JointRenderType.RJOINT to cause Apex Joints to be represented using Nastran RJOINT elements or apex.attributes.JointRenderType.RBE2 to cause them to be represented using Nastran RBE2 elements. If omitted, Undefined elemenst will be used by default.

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.Spring1D`  (extends `Connector`)

## `apex.attribute.Spring1DCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `Spring1DCollection() -> None` — Construct a new Spring1DCollection.

## `apex.attribute.Spring1DRepProperties`  (extends `ConnectorDiscreteProperty`)
Class Spring1DRepProperties. The class Spring1DRepProperties holds the properties of spring1D connector.
Properties: `dampingCoefficient`, `embedded`, `id`, `stiffness`, `stressCoefficient`

Methods:

- `getDampingCoefficient() -> float` — The dampingCoefficient of Spring1D connector.
- `getEmbedded() -> bool` — Returns embedded of the Spring1D connector.
- `getId() -> int` — Returns id of the Spring1D connector.
- `getStiffness() -> float` — The stiffness of Spring1D connector.
- `getStressCoefficient() -> float` — The stressCoefficient of Spring1D connector.
#### `update(stiffness: float, dampingCoefficient: float, stressCoefficient: float, name: str, description: str, id: int) -> None`
Update this connector properties.

- `stiffness` — Update the stiffness of this connectorProperty.
- `dampingCoefficient` — Update the damping coefficient of this connector property.
- `stressCoefficient` — update the stress coefficient of this connector property.
- `name` — update the name of this connector property.
- `description` — update the description of this connector property.
- `id` — update the id of this connector property.

One or more properties may be updated in each call to update().


## `apex.attribute.Spring1DRepPropertiesCollection`  (extends `EntityCollection`)

Methods:

- `Spring1DRepPropertiesCollection() -> None` — Construct a new Spring1DRepPropertiesCollection.

## `apex.attribute.SpringDamper1D`  (extends `Connector`)

## `apex.attribute.SpringDamper1DCollection`  (extends `EntityCollection`, `IUserHighlightable`)

Methods:

- `SpringDamper1DCollection() -> None` — Construct a new SpringDamper1DCollection.

## `apex.attribute.SpringDamper1DRepProperties`  (extends `ConnectorDiscreteProperty`)
Class SpringDamper1DRepProperties. The class SprinDamper1DRepProperties holds the properties of SpringDamper1D connector.
Properties: `damping`, `embedded`, `id`, `mass`, `stiffness`, `strainRecoveryCoefficient`, `stressRecoveryCoefficient`

Methods:

- `getDamping() -> float` — The damping of the SpringDamper 1D connector.
- `getEmbedded() -> bool` — Returns embedded of the SpringDamper1D connector.
- `getId() -> int` — Returns id of the SpringDamper1D connector.
- `getMass() -> float` — The mass of the SpringDamper1D connector.
- `getStiffness() -> float` — The stiffness of the SpringDamper1D connector.
- `getStrainRecoveryCoefficient() -> float` — The strainRecoveryCoefficient of the SpringDamper1D connector.
- `getStressRecoveryCoefficient() -> float` — The stressRecoveryCoefficient of the SpringDamper1D connector.
#### `update(stiffness: float, damping: float, mass: float, stressRecoveryCoefficient: float, strainRecoveryCoefficient: float, name: str, description: str, id: int) -> None`
Update this connector properties.

- `stiffness` — Update the stiffness of this connectorProperty.
- `damping` — Update the damping of this connectorProperty.
- `mass` — Update the mass of this connectorProperty.
- `stressRecoveryCoefficient` — Update the stressRecoveryCoefficient of this connectorProperty.
- `strainRecoveryCoefficient` — Update the strainRecoveryCoefficient of this connectorProperty.
- `name` — update the name of this connector property.
- `description` — update the description of this connector property.
- `id` — update the id of this connector property.

One or more properties may be updated in each call to update().


## `apex.attribute.SpringDamper1DRepPropertiesCollection`  (extends `EntityCollection`)

Methods:

- `SpringDamper1DRepPropertiesCollection() -> None` — Construct a new SpringDamper1DRepPropertiesCollection.

## `apex.attribute.StressStrainCurve`  (extends `DataSeries`)
This class used to define the stress-strain curve for Plasticity constitutive model.
Properties: `description`, `name`, `strainType`, `xunit`, `xunitquantity`, `xvalues`, `ydata`, `yunit`, `yunitquantity`

Methods:

- `getDescription() -> str` — Returns the description for this DataSeries.
- `getName() -> str` — Returns the name for this DataSeries.
- `getStrainType() -> apex.attribute.StrainType`
- `getXUnit() -> str` — Returns the string defining the unit (e.g., "m") for the x-axis data.
- `getXUnitQuantity() -> str` — Returns the string defining the type of unit quantity (e.g. "Length") for the x-data.
- `getXValues() -> [float]` — Returns the list of scalar values representing the x-axis data.
- `getYData() -> [float]` — Returns the list of scalar values representing the y-axis data.
- `getYUnit() -> str` — Returns the string defining the unit for the y-axis data.
- `getYUnitQuantity() -> str` — Returns the string defining the type of unit quantity for the y-data.
- `setDescription(description: str) -> None`
- `setName(name: str) -> None`
- `setStrainType(strainType: apex.attribute.StrainType) -> None`
- `setXunit(xunit: str) -> None`
- `setXunitquantity(xunitquantity: str) -> None`
- `setXvalues(xvalues: [float]) -> None`
- `setYdata(ydata: [float]) -> None`
- `setYunit(yunit: str) -> None`
- `setYunitquantity(yunitquantity: str) -> None`
- `update(name: str, description: str, xvalues: [float], ydata: [float], xunitquantity: str, xunit: str, yunitquantity: str, yunit: str, strainType: apex.attribute.StrainType) -> None`

## `apex.attribute.TABDMP1`  (extends `Entity`, `IName`)
Class representing a Nastran TABDMP1 case control command.
Properties: `id`, `type`, `xdata`, `ydata`

Methods:

- `exportdata(filename: str) -> None`
- `getId() -> int` — Gets.
- `getType() -> str` — Gets.
- `getXdata() -> [float]` — Gets.
- `getYdata() -> [float]` — Gets.
- `importdata(filename: str) -> None`
- `update(name: str, description: str, id: int, type: str, xdata: [float], ydata: [float]) -> None`

## `apex.attribute.TABRND1`  (extends `Entity`, `IName`)
Class representing a Nastran TABRND1 case control command.
Properties: `id`, `xdata`, `xInterpolation`, `ydata`, `yInterpolation`

Methods:

- `exportdata(filename: str) -> None`
- `getId() -> int` — Gets.
- `getXInterpolation() -> str` — Gets.
- `getXdata() -> [float]` — Gets.
- `getYInterpolation() -> str` — Gets.
- `getYdata() -> [float]` — Gets.
- `importdata(filename: str) -> None`
- `update(name: str, description: str, id: int, xInterpolation: str, yInterpolation: str, xdata: [float], ydata: [float]) -> None`

## `apex.attribute.ThermalExpansion`  (extends `ConstitutiveModel`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.

## `apex.attribute.ThermalExpansionLinear2DAnisotropic`  (extends `ThermalExpansion`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `expansionCoefficient11`, `expansionCoefficient12`, `expansionCoefficient22`, `referenceTemp`

Methods:

#### `ThermalExpansionLinear2DAnisotropic(expansionCoefficient11: float, expansionCoefficient22: float, expansionCoefficient12: float, referenceTemp: float) -> None`
Create ThermalExpansionLinear2DAnisotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `expansionCoefficient22` — of this constitutive model
- `expansionCoefficient12` — of this constitutive model
- `referenceTemp` — Reference Temp property of the Material

- `getExpansionCoefficient11() -> float` — Returns Expansion Coefficient11 of the constitutive model.
- `getExpansionCoefficient12() -> float` — Returns Expansion Coefficient12 of the constitutive model.
- `getExpansionCoefficient22() -> float` — Returns Expansion Coefficient22 of the constitutive model.
- `getReferenceTemp() -> float` — Gets Reference Temp property of the Material.
#### `update(expansionCoefficient11: float, expansionCoefficient22: float, expansionCoefficient12: float, referenceTemp: float) -> None`
Update properties of this ThermalExpansionLinear2DAnisotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `expansionCoefficient22` — of this constitutive model
- `expansionCoefficient12` — of this constitutive model
- `referenceTemp` — Reference Temp property of the Material


## `apex.attribute.ThermalExpansionLinear2DOrthotropic`  (extends `ThermalExpansion`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `expansionCoefficient11`, `expansionCoefficient22`, `referenceTemp`

Methods:

#### `ThermalExpansionLinear2DOrthotropic(expansionCoefficient11: float, expansionCoefficient22: float, referenceTemp: float) -> None`
Create ThermalExpansionLinear2DOrthotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `expansionCoefficient22` — of this constitutive model
- `referenceTemp` — Reference Temp property of the Material

- `getExpansionCoefficient11() -> float` — Returns Expansion Coefficient11 of the constitutive model.
- `getExpansionCoefficient22() -> float` — Returns Expansion Coefficient22 of the constitutive model.
- `getReferenceTemp() -> float` — Gets Reference Temp property of the Material.
#### `update(expansionCoefficient11: float, expansionCoefficient22: float, referenceTemp: float) -> None`
Update properties of this ThermalExpansionLinear2DOrthotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `expansionCoefficient22` — of this constitutive model
- `referenceTemp` — Reference Temp property of the Material


## `apex.attribute.ThermalExpansionLinear3DAnisotropic`  (extends `ThermalExpansion`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `expansionCoefficient11`, `expansionCoefficient12`, `expansionCoefficient13`, `expansionCoefficient22`, `expansionCoefficient23`, `expansionCoefficient33`, `referenceTemp`

Methods:

#### `ThermalExpansionLinear3DAnisotropic(expansionCoefficient11: float, expansionCoefficient22: float, expansionCoefficient33: float, expansionCoefficient12: float, expansionCoefficient23: float, expansionCoefficient13: float, referenceTemp: float) -> None`
Create ThermalExpansionLinear3DAnisotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `expansionCoefficient22` — of this constitutive model
- `expansionCoefficient33` — of this constitutive model
- `expansionCoefficient12` — of this constitutive model
- `expansionCoefficient23` — of this constitutive model
- `expansionCoefficient13` — of this constitutive model
- `referenceTemp` — Reference Temp property of the Material

- `getExpansionCoefficient11() -> float` — Returns Expansion Coefficient11 of the constitutive model.
- `getExpansionCoefficient12() -> float` — Returns Expansion Coefficient12 of the constitutive model.
- `getExpansionCoefficient13() -> float` — Returns Expansion Coefficient13 of the constitutive model.
- `getExpansionCoefficient22() -> float` — Returns Expansion Coefficient22 of the constitutive model.
- `getExpansionCoefficient23() -> float` — Returns Expansion Coefficient23 of the constitutive model.
- `getExpansionCoefficient33() -> float` — Returns Expansion Coefficient33 of the constitutive model.
- `getReferenceTemp() -> float` — Gets Reference Temp property of the Material.
#### `update(expansionCoefficient11: float, expansionCoefficient22: float, expansionCoefficient33: float, expansionCoefficient12: float, expansionCoefficient23: float, expansionCoefficient13: float, referenceTemp: float) -> None`
Update properties of this ThermalExpansionLinear3DAnisotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `expansionCoefficient22` — of this constitutive model
- `expansionCoefficient33` — of this constitutive model
- `expansionCoefficient12` — of this constitutive model
- `expansionCoefficient23` — of this constitutive model
- `expansionCoefficient13` — of this constitutive model
- `referenceTemp` — Reference Temp property of the Material


## `apex.attribute.ThermalExpansionLinear3DOrthotropic`  (extends `ThermalExpansion`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `expansionCoefficient11`, `expansionCoefficient22`, `expansionCoefficient33`, `referenceTemp`

Methods:

#### `ThermalExpansionLinear3DOrthotropic(expansionCoefficient11: float, expansionCoefficient22: float, expansionCoefficient33: float, referenceTemp: float) -> None`
Create ThermalExpansionLinear3DOrthotropic constitutive model.

- `expansionCoefficient11` — Coefficient of linear thermal expansion in the material 11 direction
- `expansionCoefficient22` — Coefficient of linear thermal expansion in the material 22 direction
- `expansionCoefficient33` — Coefficient of linear thermal expansion in the material 33 direction
- `referenceTemp` — Reference Temp property of the Material

- `getExpansionCoefficient11() -> float` — Returns theCoefficient of linear thermal expansion in the material 11 direction.
- `getExpansionCoefficient22() -> float` — Returns the Coefficient of linear thermal expansion in the material 22 direction.
- `getExpansionCoefficient33() -> float` — Returns the Coefficient of linear thermal expansion in the material 33 direction.
- `getReferenceTemp() -> float` — Gets Reference Temp property of the Material.
#### `update(expansionCoefficient11: float, expansionCoefficient22: float, expansionCoefficient33: float, referenceTemp: float) -> None`
Update properties of this ThermalExpansionLinear3DOrthotropic constitutive model.

- `expansionCoefficient11` — Coefficient of linear thermal expansion in the material 11 direction
- `expansionCoefficient22` — Coefficient of linear thermal expansion in the material 22 direction
- `expansionCoefficient33` — Coefficient of linear thermal expansion in the material 33 direction
- `referenceTemp` — Reference Temp property of the Material


## `apex.attribute.ThermalExpansionLinear3DTransvIso`  (extends `ThermalExpansion`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `expansionCoefficient11`, `expansionCoefficient22`, `referenceTemp`

Methods:

#### `ThermalExpansionLinear3DTransvIso(expansionCoefficient11: float, expansionCoefficient22: float, referenceTemp: float) -> None`
Create ThermalExpansionLinear3DTransvIso constitutive model.

- `expansionCoefficient11` — The Axis Direction Thermal Expansion Coefficient. Used axial for x Orientation.
- `expansionCoefficient22` — The in plan Thermal Expansion Coefficient. Used in plane for y and z Orientation
- `referenceTemp` — Reference Temp property of the Material

- `getExpansionCoefficient11() -> float` — Returns the Axis Direction Thermal Expansion Coefficient. Used axial for x Orientation.
- `getExpansionCoefficient22() -> float` — Returns the in plan Thermal Expansion Coefficient. Used in plane for y and z Orientation.
- `getReferenceTemp() -> float` — Gets Reference Temp property of the Material.
#### `update(expansionCoefficient11: float, expansionCoefficient22: float, referenceTemp: float) -> None`
Update properties of this ThermalExpansionLinear3DTransvIso constitutive model.

- `expansionCoefficient11` — The Axis Direction Thermal Expansion Coefficient. Used axial for x Orientation.
- `expansionCoefficient22` — The in plan Thermal Expansion Coefficient. Used in plane for y and z Orientation.
- `referenceTemp` — Reference Temp property of the Material


## `apex.attribute.ThermalExpansionLinearIsotropic`  (extends `ThermalExpansion`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `expansionCoefficient11`, `referenceTemp`

Methods:

#### `ThermalExpansionLinearIsotropic(expansionCoefficient11: float, referenceTemp: float) -> None`
Create ThermalExpansionLinearIsotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `referenceTemp` — parameter to modify the Reference Temp property of the Material

- `getExpansionCoefficient11() -> float` — Returns Expansion Coefficient11 of the constitutive model.
- `getReferenceTemp() -> float` — Gets Reference Temp property of the Material.
#### `update(expansionCoefficient11: float, referenceTemp: float) -> None`
Update properties of this ThermalExpansionLinearIsotropic constitutive model.

- `expansionCoefficient11` — of this constitutive model
- `referenceTemp` — parameter to modify the Reference Temp property of the Material


## `apex.attribute.ThicknessOffsetField`  (extends `DiscreteFEMField`)
Class ThicknessOffsetField. This class describes the property of ThicknessOffsetField. This is the base class of ThicknessOffsetFieldMidsurface and ThicknessOffsetFieldConstant.
Properties: `target`

Methods:

- `getTarget() -> apex.EntityCollection` — Get a collection of all entities that this field directly references.

## `apex.attribute.ThicknessOffsetFieldConstant`  (extends `ThicknessOffsetField`)
Class ThicknessOffsetFieldConstant. This class describes the property of ThicknessOffsetFieldConstant.
Properties: `constantValue`

Methods:

- `getConstantValue() -> float` — Get the constant value of ThicknessOffsetFieldConstant.
#### `update(name: str, targets: apex.EntityCollection, constantValue: float) -> None`
Used to update the attribute for ThicknessOffsetFieldConstant.

- `name` — the name of this object as a string
- `targets` — the field assigned entity collection
- `constantValue` — the constant value of ThicknessOffsetFieldConstant


## `apex.attribute.ThicknessOffsetFieldMidsurface`  (extends `ThicknessOffsetField`)
Class ThicknessOffsetFieldMidsurface. This class describes the property of ThicknessOffsetFieldMidsurface.
Properties: `offset`, `thickness`

Methods:

- `getOffset() -> float` — Get the offset value of ThicknessOffsetFieldMidsurface.
- `getThickness() -> float` — Get the thickness value of ThicknessOffsetFieldMidsurface.
- `recalculate() -> None` — recalculates the thickness and offset fields/values for this field using the current locations of the pairs of Faces that were used to create the field. This method will only affect ThicknessOffsetFieldMidsurface that were created using the automatic thickness tool or automatic mid-surface extraction tool. The method will be silently ignored if called on ThicknessOffsetFieldMidsurface that were not created using these methods.
#### `update(name: str, targets: apex.EntityCollection, thickness: float, offset: float) -> None`
Used to update the attribute for ThicknessOffsetFieldMidsurface.

- `name` — the name of this object as a string
- `targets` — the field assigned entity collection
- `thickness` — the thickness value of ThicknessOffsetFieldMidsurface
- `offset` — the offset value of ThicknessOffsetFieldMidsurface


## `apex.attribute.ThicknessOffsetFieldMidsurfaceCollection`  (extends `EntityCollection`)
Iterable collection of ThicknessOffsetFieldMidsurface, based on EntityCollection.

Methods:

- `ThicknessOffsetFieldMidsurfaceCollection() -> None` — Construct a new ThicknessOffsetFieldMidsurfaceCollection.

## `apex.attribute.ViscoElasticity`  (extends `ConstitutiveModel`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `strdampingCoefficient`

Methods:

#### `ViscoElasticity(strdampingCoefficient: float) -> None`
Create Structural Damping Coefficient.

- `strdampingCoefficient` — of this constitutive model

example: myViscoElasticityProperty.update(strdampingCoefficient = )

- `getStrdampingCoefficient() -> float` — Returns Elastic Modulus 11 of the constitutive model.
#### `update(strdampingCoefficient: float) -> None`
used to update the Structural Damping Coefficient

- `strdampingCoefficient` — of this constitutive model

example: myViscoElasticityProperty.update(strdampingCoefficient = )


## `apex.attribute.ViscoElasticity2DAniso`  (extends `ViscoElasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `GE11`, `GE12`, `GE13`, `GE22`, `GE23`, `GE33`

Methods:

#### `ViscoElasticity2DAniso(strdampingCoefficient: float, GE11: float, GE12: float, GE13: float, GE22: float, GE23: float, GE33: float) -> None`
Create ViscoElasticity2DAniso constitutive model.

- `strdampingCoefficient` — of this constitutive model
- `GE11` — of this constitutive model
- `GE12` — of this constitutive model
- `GE13` — of this constitutive model
- `GE22` — of this constitutive model
- `GE23` — of this constitutive model
- `GE33` — of this constitutive model

- `getGE11() -> float` — Returns Matrix11 of the constitutive model.
- `getGE12() -> float` — Returns Matrix12 of the constitutive model.
- `getGE13() -> float` — Returns Matrix13 of the constitutive model.
- `getGE22() -> float` — Returns Matrix22 of the constitutive model.
- `getGE23() -> float` — Returns Matrix23 of the constitutive model.
- `getGE33() -> float` — Returns Matrix33 of the constitutive model.
#### `update(strdampingCoefficient: float, GE11: float, GE12: float, GE13: float, GE22: float, GE23: float, GE33: float) -> None`
Update properties of this ViscoElasticity2DAniso constitutive model.

- `strdampingCoefficient` — of this constitutive model
- `GE11` — of this constitutive model
- `GE12` — of this constitutive model
- `GE13` — of this constitutive model
- `GE22` — of this constitutive model
- `GE23` — of this constitutive model
- `GE33` — of this constitutive model


## `apex.attribute.ViscoElasticity3DAniso`  (extends `ViscoElasticity`)
This Class is no longer supported in Apex. Refer to MaterialModel to determine how this capability is now supported.
Properties: `GE11`, `GE12`, `GE13`, `GE14`, `GE15`, `GE16`, `GE22`, `GE23`, `GE24`, `GE25`, `GE26`, `GE33`, `GE34`, `GE35`, `GE36`, `GE44`, `GE45`, `GE46`, `GE55`, `GE56`, `GE66`

Methods:

#### `ViscoElasticity3DAniso(strdampingCoefficient: float, GE11: float, GE12: float, GE13: float, GE14: float, GE15: float, GE16: float, GE22: float, GE23: float, GE24: float, GE25: float, GE26: float, GE33: float, GE34: float, GE35: float, GE36: float, GE44: float, GE45: float, GE46: float, GE55: float, GE56: float, GE66: float) -> None`
Create ViscoElasticity3DAniso constitutive model.

- `strdampingCoefficient` — of this constitutive model
- `GE11` — of this constitutive model
- `GE12` — of this constitutive model
- `GE13` — of this constitutive model
- `GE14` — of this constitutive model
- `GE15` — of this constitutive model
- `GE16` — of this constitutive model
- `GE22` — of this constitutive model
- `GE23` — of this constitutive model
- `GE24` — of this constitutive model
- `GE25` — of this constitutive model
- `GE26` — of this constitutive model
- `GE33` — of this constitutive model
- `GE34` — of this constitutive model
- `GE35` — of this constitutive model
- `GE36` — of this constitutive model
- `GE44` — of this constitutive model
- `GE45` — of this constitutive model
- `GE46` — of this constitutive model
- `GE55` — of this constitutive model
- `GE56` — of this constitutive model
- `GE66` — of this constitutive model

- `getGE11() -> float` — Returns Matrix11 of the constitutive model.
- `getGE12() -> float` — Returns Matrix12 of the constitutive model.
- `getGE13() -> float` — Returns Matrix13 of the constitutive model.
- `getGE14() -> float` — Returns Matrix14 of the constitutive model.
- `getGE15() -> float` — Returns Matrix15 of the constitutive model.
- `getGE16() -> float` — Returns Matrix16 of the constitutive model.
- `getGE22() -> float` — Returns Matrix22 of the constitutive model.
- `getGE23() -> float` — Returns Matrix23 of the constitutive model.
- `getGE24() -> float` — Returns Matrix24 of the constitutive model.
- `getGE25() -> float` — Returns Matrix25 of the constitutive model.
- `getGE26() -> float` — Returns Matrix6 of the constitutive model.
- `getGE33() -> float` — Returns Matrix33 of the constitutive model.
- `getGE34() -> float` — Returns Matrix34 of the constitutive model.
- `getGE35() -> float` — Returns Matrix35 of the constitutive model.
- `getGE36() -> float` — Returns Matrix36 of the constitutive model.
- `getGE44() -> float` — Returns Matrix44 of the constitutive model.
- `getGE45() -> float` — Returns Matrix45 of the constitutive model.
- `getGE46() -> float` — Returns Matrix46 of the constitutive model.
- `getGE55() -> float` — Returns Matrix55 of the constitutive model.
- `getGE56() -> float` — Returns Matrix56 of the constitutive model.
- `getGE66() -> float` — Returns Matrix66 of the constitutive model.
#### `update(strdampingCoefficient: float, GE11: float, GE12: float, GE13: float, GE14: float, GE15: float, GE16: float, GE22: float, GE23: float, GE24: float, GE25: float, GE26: float, GE33: float, GE34: float, GE35: float, GE36: float, GE44: float, GE45: float, GE46: float, GE55: float, GE56: float, GE66: float) -> None`
Update properties of this ViscoElasticity3DAniso constitutive model.

- `strdampingCoefficient` — of this constitutive model
- `GE11` — of this constitutive model
- `GE12` — of this constitutive model
- `GE13` — of this constitutive model
- `GE14` — of this constitutive model
- `GE15` — of this constitutive model
- `GE16` — of this constitutive model
- `GE22` — of this constitutive model
- `GE23` — of this constitutive model
- `GE24` — of this constitutive model
- `GE25` — of this constitutive model
- `GE26` — of this constitutive model
- `GE33` — of this constitutive model
- `GE34` — of this constitutive model
- `GE35` — of this constitutive model
- `GE36` — of this constitutive model
- `GE44` — of this constitutive model
- `GE45` — of this constitutive model
- `GE46` — of this constitutive model
- `GE55` — of this constitutive model
- `GE56` — of this constitutive model
- `GE66` — of this constitutive model


## `apex.attribute.YieldBarlat`  (extends `YieldCriteria`)
the class for Barlat’s 1991 yield criteria. Barlat’s anisotropic model introduces orthotropic plastic material. This option can only be combined with orthotropic or anisotropic elastic material (i.e., with MAT2, MATORT or MAT9). Barlat’s 1991 yield criteria have 5 parameters required, M Barlat M coefficient C1 Barlat C1 coefficient C2 Barlat C2 coefficient C3 Barlat C3 coefficient C6 Barlat C6 coefficient
Properties: `c1`, `c2`, `c3`, `c6`, `m`

Methods:

- `getC1() -> float` — Gets Barlat C1 coefficient.
- `getC2() -> float` — Gets Barlat C2 coefficient.
- `getC3() -> float` — Gets Barlat C3 coefficient.
- `getC6() -> float` — Gets Barlat C6 coefficient.
- `getM() -> float` — Gets Barlat M coefficient.
- `setC1(c1: float) -> None` — Sets Barlat C1 coefficient.
- `setC2(c2: float) -> None` — Sets Barlat C2 coefficient.
- `setC3(c3: float) -> None` — Sets Barlat C3 coefficient.
- `setC6(c6: float) -> None` — Sets Barlat C6 coefficient.
- `setM(m: float) -> None` — Sets Barlat M coefficient.
#### `update(m: float, c1: float, c2: float, c3: float, c6: float) -> None`
edit method Usage example: $$ Edit a Barlat yield criteria. myYieldCriteria.update(m = 1.0, c1 = 1.0, c2 = 1.0, c3 = 1.0, c6 = 1.0)

- `m` — M Barlat M coefficient
- `c1` — Barlat C1 coefficient
- `c2` — Barlat C2 coefficient
- `c3` — Barlat C3 coefficient
- `c6` — Barlat C6 coefficient


## `apex.attribute.YieldCriteria`

Methods:

- `asYieldBarlat() -> YieldBarlat`
- `asYieldHill() -> YieldHill`
- `asYieldImpCreep() -> YieldImpCreep`
- `asYieldLinearMohr() -> YieldLinearMohr`
- `asYieldParabolicMohr() -> YieldParabolicMohr`
- `asYieldVonMises() -> YieldVonMises`

## `apex.attribute.YieldHill`  (extends `YieldCriteria`)
the class for Hill’s 1948 yield criteria. Hill’s anisotropic model introduces orthotropic plastic material. This option can only be combined with orthotropic or anisotropic elastic material (i.e., with MAT2, MATORT or MAT9).
Properties: `R11`, `R12`, `R13`, `R22`, `R23`, `R33`

Methods:

- `getR11() -> float` — Gets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `getR12() -> float` — Gets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `getR13() -> float` — Gets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `getR22() -> float` — Gets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `getR23() -> float` — Gets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `getR33() -> float` — Gets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `setR11(R11: float) -> None` — Sets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `setR12(R12: float) -> None` — Sets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `setR13(R13: float) -> None` — Sets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `setR22(R22: float) -> None` — Sets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `setR23(R23: float) -> None` — Sets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
- `setR33(R33: float) -> None` — Sets Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field. (Real > 0; R11, R22, R33, R12, R23, R31, respectively for Hill)
#### `update(r11: float, r22: float, r33: float, r12: float, r23: float, r13: float) -> None`
edit method. Usage example: $$ edit a Hill’s 1948 yield criteria yield criteria myYieldCriteria.update(r11 = 1.0, r22 = 1.0, r33 = 1.0, r12 = 1.0, r23 = 1.0, r13 = 1.0 )

- `r11` — Optional,Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r22` — Optional,Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r33` — Optional,Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r12` — Optional,Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r23` — Optional,Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.
- `r13` — Optional,Stress ratios of initial yield stresses in various material directions to the reference yield stress from FID/Y0 field.


## `apex.attribute.YieldImpCreep`  (extends `YieldCriteria`)
the class for Implicit creep model combining both plasticity and creep,von Mises yield criteria.
Properties: `eqVonMises`

Methods:

- `getEqVonMises() -> float` — Gets Equivalent (von Mises) tensile yield stress. (Real, no Default)
- `setEqVonMises(eqVonMises: float) -> None` — Sets Equivalent (von Mises) tensile yield stress. (Real, no Default)
#### `update(eqVonMises: float) -> None`
edit method Usage example: $$ Edit a Barlat yield criteria. myYieldCriteria.update(m = 1.0, c1 = 1.0, c2 = 1.0, c3 = 1.0, c6 = 1.0)

- `eqVonMises` — Optional, Equivalent (von Mises) tensile yield stress. (Real, no Default)


## `apex.attribute.YieldLinearMohr`  (extends `YieldCriteria`)
The class for Linear Mohr-Coulomb yield criteria. The user needs to instantiate a yield criterion object and set it to the plastic constitutive model.
Properties: `Alpha`

Methods:

- `getAlpha() -> float` — Gets Specifies the parameter alpha for linear Mohr-Coulomb model.
- `setAlpha(Alpha: float) -> None` — Sets Specifies the parameter alpha for linear Mohr-Coulomb model.
#### `update(alpha: float) -> None`
update method Usage example: $$ edit a Linear Mohr-Coulomb yield criteria myYieldCriteria.update(alpha = 1.0)

- `alpha` — optional,Specifies the parameter alpha for linear Mohr-Coulomb model.


## `apex.attribute.YieldParabolicMohr`  (extends `YieldCriteria`)
The Class for Parabolic Mohr-Coulomb yield criteria The user needs to instantiate a yield criterion object and set it to the plastic constitutive model.
Properties: `Alpha`, `Beta`

Methods:

- `getAlpha() -> float` — Gets Specifies the parameter alpha for linear Mohr-Coulomb model. Real > 0.
- `getBeta() -> float` — Gets Specifies the parameter beta for parabolic Mohr-Coulomb model. (Real > 0.
- `setAlpha(Alpha: float) -> None` — Sets Specifies the parameter alpha for linear Mohr-Coulomb model. Real > 0.
- `setBeta(Beta: float) -> None` — Sets Specifies the parameter beta for parabolic Mohr-Coulomb model. (Real > 0.
#### `update(alpha: float, beta: float) -> None`
Edit method Usage example: $$ edit a Parabolic Mohr-Coulomb model yield criteria myYieldCriteria.update(alpha = 1.0,beta = 1.0 )

- `alpha` — Optional,Specifies the parameter alpha for linear Mohr-Coulomb model.
- `beta` — Optional,Specifies the parameter beta for parabolic Mohr-Coulomb model.


## `apex.attribute.YieldVonMises`  (extends `YieldCriteria`)
The class for von Mises yield criteria. The user needs to instantiate a von Mises yield criterion object and set it to the plastic constitutive model, if user want to use the von Mises yield criterion. For von Mises yield criteria, no need any parameters to define the von Mises yield criteria, So there is no related attributes and no update method.

## `apex.attribute.Zone`  (extends `Entity`)
Class Zone.
Properties: `alignmentType`, `allowableInterLaminarBondStress`, `failureCriteria`, `id`, `nonStructuralMass`, `plies`, `plyBehavior`, `plyIdBehavior`, `referenceTemperature`, `regions`, `structuralDampingCoefficient`, `thickness`, `zoneOffset`

Methods:

- `getAlignmentType() -> apex.attribute.AlignmentType` — Gets the optional alignmentType of the zone offset.
- `getAllowableInterLaminarBondStress() -> float` — Gets the optional allowableInterlaminarBondStress of the zone. If set, it will override the allowableInterlaminarBondStress defined by the panel. If unset, this zone will use the allowableInterlaminarBondStress defined by the panel.
- `getFailureCriteria() -> apex.attribute.FailureCriteriaComposite` — Gets the optional failureCriteria of the zone. If set, it will override the failureCriteria defined by the panel. If unset, this zone will use the failureCriteria defined by the panel.
- `getId() -> int` — Gets the id of the zone. If unset, system will automatically assign a valid id to the zone by default.
- `getNonStructuralMass() -> float` — Gets the nonstructural mass per unit area on the zone region.
- `getPlies() -> apex.attribute.PlyCollection` — Gets Plies of the Zone.
- `getPlyBehavior() -> apex.attribute.PlyBehavior` — Gets the optional plyBehavior in zone. If set, it will override the plyBehavior defined by the panel. If unset, this zone will use the plyBehavior defined by the panel. If both plyBehaviors in zone and panel are omitted, then system assumes "apex.attribute.PlyBehavior.Default" is used.
- `getPlyIdBehavior() -> apex.attribute.PlyIdBehavior` — Gets the optional plyIdBehavior in zone. If set, it will override the plyIdBehavior defined by the panel. If unset, this zone will use the plyIdBehavior defined by the panel. If both plyIdBehaviors in zone and panel are omitted, then system assumes "apex.attribute.PlyIdBehavior.UseGlobal" is used.
- `getReferenceTemperature() -> float` — Gets the optional reference temperature of the zone. If set, the reference temperature of the zone will override the reference temperature specified in the panel. If unset, this zone will use the panel referenceTemperature by default.
- `getRegions() -> apex.EntityCollection` — Gets regions of the zone.
- `getStructuralDampingCoefficient() -> float` — Gets the optional structuralDampingCoefficient of the zone. If set, the structuralDampingCoefficient of the zone will override the reference temperature specified in the panel. If unset, this zone will use the panel structuralDampingCoefficient by default.
- `getThickness() -> float` — Gets the total thickness of the zone.This thickness is derived from the total plies thickness within the zone.
- `getZoneOffset() -> float` — Gets the optional offset distance of the zone. The zoneOffset only makes sense when offsetType is defined to "apex.attribute.AlignmentType.Offset". If zoneOffset is set, it will override the panelOffset. If zoneOffset is unset, this zone will use the panelOffset by default.
#### `moveDownPly(ply: apex.attribute.Ply) -> None`
Move down the ply.

- `ply` — of the LayeredPanel

#### `moveUpPly(ply: apex.attribute.Ply) -> None`
Move up the ply.

- `ply` — of the LayeredPanel

- `setAlignmentType(alignmentType: apex.attribute.AlignmentType) -> None` — Sets the optional alignmentType of the zone offset.
- `setAllowableInterLaminarBondStress(allowableInterlaminarBondStress: float) -> None` — Sets the optional allowableInterlaminarBondStress of the zone. If set, it will override the allowableInterlaminarBondStress defined by the panel. If unset, this zone will use the allowableInterlaminarBondStress defined by the panel.
- `setFailureCriteria(failureCriteria: apex.attribute.FailureCriteriaComposite) -> None` — Sets the optional failureCriteria of the zone. If set, it will override the failureCriteria defined by the panel. If unset, this zone will use the failureCriteria defined by the panel.
- `setId(id: int) -> None` — Sets the id of the zone. If unset, system will automatically assign a valid id to the zone by default.
- `setNonStructuralMass(nonStructuralMass: float) -> None` — Sets the nonstructural mass per unit area on the zone region.
- `setPlyBehavior(plyBehavior: apex.attribute.PlyBehavior) -> None` — Sets the optional plyBehavior in zone. If set, it will override the plyBehavior defined by the panel. If unset, this zone will use the plyBehavior defined by the panel. If both plyBehaviors in zone and panel are omitted, then system assumes "apex.attribute.PlyBehavior.Default" is used.
- `setPlyIdBehavior(plyIdBehavior: apex.attribute.PlyIdBehavior) -> None` — Sets the optional plyIdBehavior in zone. If set, it will override the plyIdBehavior defined by the panel. If unset, this zone will use the plyIdBehavior defined by the panel. If both plyIdBehaviors in zone and panel are omitted, then system assumes "apex.attribute.PlyIdBehavior.UseGlobal" is used.
- `setReferenceTemperature(referenceTemperature: float) -> None` — Sets the optional reference temperature of the zone. If set, the reference temperature of the zone will override the reference temperature specified in the panel. If unset, this zone will use the panel referenceTemperature by default.
- `setStructuralDampingCoefficient(structuralDampingCoefficient: float) -> None` — Sets the optional structuralDampingCoefficient of the zone. If set, the structuralDampingCoefficient of the zone will override the reference temperature specified in the panel. If unset, this zone will use the panel structuralDampingCoefficient by default.
- `setZoneOffset(zoneOffset: float) -> None` — Sets the optional offset distance of the zone. The zoneOffset only makes sense when offsetType is defined to "apex.attribute.AlignmentType.Offset". If zoneOffset is set, it will override the panelOffset. If zoneOffset is unset, this zone will use the panelOffset by default.
#### `update(id: int, alignmentType: apex.attribute.AlignmentType, zoneOffset: float, failureCriteria: apex.attribute.FailureCriteriaComposite, plyBehavior: apex.attribute.PlyBehavior, structuralDampingCoefficient: float, referenceTemperature: float, allowableInterLaminarBondStress: float, nonStructuralMass: float, plyIdBehavior: apex.attribute.PlyIdBehavior) -> None`
Update the Zone properties.

- `id` — of this Zone
- `alignmentType` — of this Zone
- `zoneOffset` — of this Zone
- `failureCriteria` — of this Zone
- `plyBehavior` — of this Zone
- `structuralDampingCoefficient` — of this Zone
- `referenceTemperature` — of this Zone
- `allowableInterLaminarBondStress` — of this Zone
- `nonStructuralMass` — of this Zone
- `plyIdBehavior` — of this Zone

One or more properties may be updated in each call to update(). For example:


## `apex.attribute.ZoneCollection`  (extends `EntityCollection`)
Iterable collection of Zone, based on EntityCollection.

Methods:

- `ZoneCollection() -> None` — Construct a new ZoneCollection.

