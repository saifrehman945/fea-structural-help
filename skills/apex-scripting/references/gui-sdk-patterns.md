# GUI SDK patterns

WPF layout recipes for custom tool panels, taken from the Apex Demo Tools. All
of this belongs in the `*_ui.py` file.

## Table of contents

1. Module preamble
2. Minimal tool
3. Label and input grid
4. Combo box
5. Check box and radio buttons
6. File dialog
7. Apply button to worker
8. Sharing state between functions
9. Layout notes

## 1. Module preamble

```python
import sys
import os
import apex_sdk
import clr

import System
import System.Windows.Controls as WPFControls
from System.Windows.Automation import AutomationProperties
from Microsoft.Win32 import OpenFileDialog

current_file_path = os.path.dirname(os.path.abspath(__file__))
```

`current_file_path` is how the UI file finds its worker script and icons.

## 2. Minimal tool

```python
def getUIContent():
    my_toolProperty = apex_sdk.ToolPropertyContainer()
    return my_toolProperty
```

Add a single label:

```python
def getCustomToolPropertyContent():
    meshTextBlock = WPFControls.TextBlock()
    meshTextBlock.Text = "Hello world!"
    return meshTextBlock
```

A lone `TextBlock` is accepted, but anything with more than one control needs a
`Panel` subclass — normally a `Grid`.

## 3. Label and input grid

Build the grid, declare rows and columns, then place each control by index.

```python
def getCustomToolPropertyContent():
    my_Grid = WPFControls.Grid()

    my_Grid.RowDefinitions.Add(WPFControls.RowDefinition())
    my_Grid.RowDefinitions.Add(WPFControls.RowDefinition())
    my_Grid.ColumnDefinitions.Add(WPFControls.ColumnDefinition())
    my_Grid.ColumnDefinitions.Add(WPFControls.ColumnDefinition())

    meshTextBlock = WPFControls.TextBlock()
    meshTextBlock.Text = "Mesh Size:"
    WPFControls.Grid.SetRow(meshTextBlock, 0)
    WPFControls.Grid.SetColumn(meshTextBlock, 0)

    global meshSizeTextBox
    meshSizeTextBox = WPFControls.TextBox()
    WPFControls.Grid.SetRow(meshSizeTextBox, 0)
    WPFControls.Grid.SetColumn(meshSizeTextBox, 1)

    my_Grid.Children.Add(meshTextBlock)
    my_Grid.Children.Add(meshSizeTextBox)

    return my_Grid
```

`Grid.SetRow` / `Grid.SetColumn` are static calls taking the control — placement
is not a property on the control itself. Adding a control to `Children` is
separate from positioning it; both are required.

## 4. Combo box

```python
    global meshTypeComboBox
    meshTypeComboBox = WPFControls.ComboBox()

    item1 = WPFControls.ComboBoxItem()
    item1.Content = "Mixed"
    meshTypeComboBox.Items.Add(item1)

    item2 = WPFControls.ComboBoxItem()
    item2.Content = "Auto"
    meshTypeComboBox.Items.Add(item2)

    meshTypeComboBox.SelectedIndex = 0
    WPFControls.Grid.SetRow(meshTypeComboBox, 1)
    WPFControls.Grid.SetColumn(meshTypeComboBox, 1)
```

Each entry is a `ComboBoxItem` whose `Content` is the visible text. Read the
selection later with `meshTypeComboBox.Text`.

Keep the item strings identical to the keys of the worker's enum lookup table,
so the worker can map them without guessing.

## 5. Check box and radio buttons

```python
    myCheckBox = WPFControls.CheckBox()
    myCheckBox.Content = "Include hidden bodies"
    myCheckBox.IsChecked = False
```

```python
    optionA = WPFControls.RadioButton()
    optionA.Content = "All bodies"
    optionA.GroupName = "scope"
    optionA.IsChecked = True

    optionB = WPFControls.RadioButton()
    optionB.Content = "Selected bodies"
    optionB.GroupName = "scope"
```

Radio buttons are mutually exclusive only when they share a `GroupName`.

Pass their state as strings: `str(myCheckBox.IsChecked)`, and cast back in the
worker with a comparison such as `dictionary["IncludeHidden"] == "True"`.

## 6. File dialog

```python
@apex_sdk.errorhandler
def HandleImportButton(sender, args):
    dialog = OpenFileDialog()
    dialog.Multiselect = False
    dialog.Filter = "CSV Files|*.csv|All Files|*.*"
    if dialog.ShowDialog():
        fileNameTextBox.Text = dialog.FileName
```

Wire it up with `+=`:

```python
    importBtn = WPFControls.Button()
    importBtn.Content = "Import"
    importBtn.Click += HandleImportButton
```

The `Filter` string alternates description and pattern, separated by `|`.
A control event handler takes `(sender, args)`; an `ActionCommand` target takes
nothing.

## 7. Apply button to worker

```python
def getUIContent():
    my_toolProperty = apex_sdk.ToolPropertyContainer()
    my_toolProperty.TitleImageUriString = os.path.join(
        os.path.dirname(current_file_path), r"Icons\script.png")
    my_toolProperty.TitleText = "Mesh All Bodies"
    my_toolProperty.ToolPropertyContent = getCustomToolPropertyContent()
    my_toolProperty.AppliedCommand = apex_sdk.ActionCommand(
        System.Action(HandleApplyButton))
    return my_toolProperty


@apex_sdk.errorhandler
def HandleApplyButton():
    dictionary = {}
    dictionary["MeshSize"] = meshSizeTextBox.Text
    dictionary["MeshType"] = meshTypeComboBox.Text

    apex_sdk.runScriptFunction(
        os.path.join(current_file_path, r"mesh_all_bodies.py"),
        "mesh_all_bodies",
        dictionary)
```

The handler does three things and nothing more: read controls, build the
dictionary, hand off. It is called again on every Apply click, so it must not
accumulate state.

The matching worker:

```python
def mesh_all_bodies(dictionary={}):
    import apex

    apex.disableShowOutput()

    mesh_size = float(dictionary["MeshSize"])
    mesh_types = {
        "Mixed": apex.mesh.SurfaceMeshElementShape.Mixed,
        "Quadrilateral": apex.mesh.SurfaceMeshElementShape.Quadrilateral,
        "Triangle": apex.mesh.SurfaceMeshElementShape.Triangle,
    }
    mesh_type = mesh_types[dictionary["MeshType"]]
    ...
```

`import apex` sits **inside** the worker function, matching the demo tools.

## 8. Sharing state between functions

`getCustomToolPropertyContent()` builds the controls but the Apply handler must
read them, so controls that carry input are declared `global`:

```python
    global meshSizeTextBox
    meshSizeTextBox = WPFControls.TextBox()
```

Declare `global` only for controls the handler actually reads — labels and
static text do not need it.

## 9. Layout notes

- `ToolPropertyContent` must be a `Panel` subclass (`Grid`, `StackPanel`) once
  there is more than one control.
- Add every control to `Children`, or it will not render.
- Row and column definitions must exist before anything is placed in them.
- A `TreeView` or `DataGrid` is appropriate for reporting per-part results back
  to the user; both are ordinary WPF controls used the same way.
