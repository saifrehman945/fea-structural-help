# apex.selection

(apex.selection module) provides access to the current selection.

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Module functions

### `apex.selection.getCurrentSelection(stageIndex: int = -1) -> apex.EntityCollection`
Returns the contents of the current selection list.

Returns: EntityCollection of objects in the current selection list

### `apex.selection.setBoxPickingEnabled(bEnable: bool) -> None`
Enable/Disable the Box picking status to display box in 3d-View;.

### `apex.selection.setRetainSelectionOrder(bEnable: bool) -> None`
set the order status for selection list, the default is order.

