# apex.display

(apex.display module) for adding 3dViewport annotation.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Enumerations

`apex.display.CaptureRegionType`: `Viewport`, `ViewCollection`
  - For the support display regions for graphics capture methods

`apex.display.GraphicsFontStyle`: `Normal`, `Bold`, `Italic`, `BoldItalic`
  - For the support font styles for graphics fonts

`apex.display.GraphicsFontUnderlineStyle`: `NoUnderline`, `Single`, `Double`, `SingleBold`, `Dotted`, `Dashed`
  - For the support font undeline styles

`apex.display.ImageType`: `jpg`, `png`, `bmp`, `tiff`, `gif`
  - For the support Image Types for graphics capture methods

`apex.display.VideoType`: `gif`, `mp4`, `avi`
  - For the support display regions for graphics capture methods

## Module functions

### `apex.display.cancelRecord() -> None`
cancel Record the current movie

### `apex.display.captureImage(path: str, imageNamePrefix: str = "Image", imageCaptureRegion: apex.display.CaptureRegionType = apex.display.CaptureRegionType.Viewport, imageFormat: apex.display.ImageType = apex.display.ImageType.jpg) -> str`
Captures an image of a region of the Apex application (either the current Viewport or the current ViewCollection) and saves it to disk in one of the supported image file formats, The method returns the fully path qualified name of the saved image file.

- `path` — The full path name for the saved image file
- `imageNamePrefix` — String which will become the prefix part of the recorded output image file name. (default = "Image")
- `imageCaptureRegion` — The region of the Apex application (default = REGION_CURRENT_VIEWPORT)
- `imageFormat` — The image file format (default = jpg)

### `apex.display.captureMovie(path: str, imageNamePrefix: str = "Video", imageCaptureRegion: apex.display.CaptureRegionType = apex.display.CaptureRegionType.Viewport, movieFormat: apex.display.VideoType = apex.display.VideoType.mp4, frameRate: int = 30, captureCursor: bool = True) -> bool`
Captures a movie of a region of the Apex application (either the current Viewport or the current ViewCollection) and saves it to disk in one of the supported movie file formats.

- `path` — The full path name for the saved video file
- `imageNamePrefix` — String which will become the prefix part of the recorded output video file name. (default = "Video")
- `imageCaptureRegion` — The region of the Apex application (default = apex::display::CaptureRegionType::Viewport)
- `movieFormat` — The movie file format (default = apex::display::VideoType::mp4)
- `frameRate` — The video frame rate (default = 30)
- `captureCursor` — Boolean flag specifying whether to show Mouse Cursor (default = True)

### `apex.display.clearAllGraphicsText() -> None`
Clears all graphics text that is currently displayed on the graphics view.

### `apex.display.clearExternalVTKElements(isClearRenderers: bool = False) -> None`
clearup exernal vtk elements.

- `isClearRenderers` — - false : does not clear VTK renderers, but just sets the vtkRenderWindow pointer in GEN to null. true : clearup VTK renderers, so the VTK elements cannot be restored.

### `apex.display.clearText(graphicsText: apex.display.GraphicsText) -> None`
Clears the supplied graphics text from the graphics view.

### `apex.display.createCutView(location: apex.ILocation = None, orientation: apex.IOrientation = None, bSlideMode: bool = False) -> apex.display.CutView`
causes the cut view created in the specific 3D view.

- `location` — - optional argument which specify the location of the cut plane, if omitted, the center of bounding box formed by model will be the location.
- `orientation` — - optional argument which specifies the orientation of cut plane, normal of plane aligns with Z axis, if omitted, system will assign X, Y, Z axis recurrently.
- `bSlideMode` — - optional boolean argument which specifies the type of cut view as either clip or slice, if omitted, Clip is set by default.

### `apex.display.displayCutViews(display: bool = True, boundingBoxVisibility: bool = False) -> None`
causes displaying model cut by one plane or several planes.

- `display` — - Optional argument to control the visibility of cuting view for the structural model. It is set as false if omitted.
- `boundingBoxVisibility` — - Optional argument to control the visibility of wireframe bounding box for the structural model. It is set as false if omitted.

### `apex.display.displayExplodedView(display: bool) -> None`
ODM control for the display of exploded view.

- `display` — - defines if Exploded View should appear or not by using True or False.

### `apex.display.displayText(text: str, textLocation: apex.ILocation, graphicsFont: str = "", graphicsFontColor: apex.ColorRGB = apex.ColorRGB(0, 0, 0), graphicsFontSize: int = 12, graphicsFontStyle: apex.display.GraphicsFontStyle = apex.display.GraphicsFontStyle.Normal, graphicsFontUnderlineStyle: apex.display.GraphicsFontUnderlineStyle = apex.display.GraphicsFontUnderlineStyle.NoUnderline) -> apex.display.GraphicsText`
DEPRECATED: In releases of Apex prior to Iberian Lynx this argument was of type apex.construct.Point3D. In the Iberian Lynx release the argument type has been changed to apex.ILocation. For the Iberian Lynx release, users may continue to pass Point3D objects however this capability may be deprecated in a future release therefore users are advised to transition their code to use apex.ILocation as quickly as possible to avoid future problems. Displays text on the graphics view at the specified location. The graphics text will rotate and translate with the model but will remain front facing.

- `text` — The text that will be rendered into the graphics view
- `textLocation` — The location in global space where the text will be drawn
- `graphicsFont` — The font used to render the graphics text. The default font is TimesNewRoman
- `graphicsFontColor` — The font used to render the graphics text
- `graphicsFontSize` — The font size used to render the graphics text
- `graphicsFontStyle` — The font style used to render the graphics text. The default font style is 'Normal'
- `graphicsFontUnderlineStyle` — The font underline style used to render the graphics text. The default font underline style is 'None'

### `apex.display.enableGraphicRefresh(bEnable: bool) -> None`
enable/disable graphic refresh, Before using this scripting, must ensure that there are no transaction start. If transaction has been started, DDM will clean this transaction.

- `bEnable` — enable/disable graphic refresh.

### `apex.display.getCamera() -> apex.display.Camera`
Returns a virtual camera from the input 3D graphics view. The camera settings will reflect the current setting of the camera in the view.

### `apex.display.getCutView(name: str = "") -> apex.display.CutView`
Return a cut view by specifying the name. Will return the current cut view if omit.

- `name` — - optional argument to indicate the returned cut view with the specified name.

### `apex.display.getExternalVTKWidget() -> ExternalVTKWidget`
a virtual camera for 3D graphics views. It provides methods to position and orient the view point and focal point. Convenience methods for moving about the focal point also are provided.

Returns: An ExternalVTKWidget VTK object pointer.

Camera Class Object.Get the ExternalVTKWidget object which is created by C++ in the ddm module and is used to embed VTKRenderer.

### `apex.display.getSysFontFamilyList() -> [str]`
get the current system supports all font family.

### `apex.display.hideRotationCenter() -> None`
hide the location of the rotation center on the input View3D.

### `apex.display.isEnableGraphicRefresh(bEnable: bool) -> None`
query graphic refresh status.

- `bEnable` — whether to enable/disable.

### `apex.display.render() -> None`
Notify the Gen to update the view after adding or updating some elements by scripting.

### `apex.display.restoreExternalVTKElements() -> None`
restore exernal vtk elements. the premise is that VTK renderers have not been cleared.

### `apex.display.setRotationCenterAutomatic() -> None`
Causes the location of the rotation center used for graphical view manipulation for the input View3D to be calculated automatically based on the displayed object and their proximity.

### `apex.display.setRotationCenterManual(rotationCenter: apex.ILocation) -> None`
Causes the location of the rotation center used for graphical view manipulation for the input View3D to be fixed at the input rotationCenter location.

- `rotationCenter` — - Optional argument defining the location of the rotation center used for view manipulation. If omitted, the current rotation center will be used.

### `apex.display.showRotationCenter() -> None`
Show the location of the rotation center on the input View3D.

### `apex.display.stopMovie() -> str`
stop record and save the movie according with setting from captureMovie The method returns the fully path qualified name of the saved movie file.

## Classes in this module

Full method signatures are in `api/classes/apex.display.md`.

`Camera`, `CutView`, `GraphicsText`, `Tessellation`, `Tessellation0D`, `Tessellation1D`, `Tessellation2D`

