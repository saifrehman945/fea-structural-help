# Custom tool UI file.
#
# Runs as IronPython inside the Apex UI process, so the panel is built from .NET
# WPF controls. This file must NOT import apex and must NOT do modelling work --
# both stall the Apex user interface. It collects user input and hands it to the
# worker script through apex_sdk.runScriptFunction().

import sys
import os
import apex_sdk
import clr

# .NET references
import System
import System.Windows.Controls as WPFControls
from System.Windows.Automation import AutomationProperties
from Microsoft.Win32 import OpenFileDialog

current_file_path = os.path.dirname(os.path.abspath(__file__))

# Controls the Apply handler needs to read are module-level so both functions
# can reach them.
meshSizeTextBox = None
meshTypeComboBox = None


# --- required entry point ----------------------------------------------------

def getUIContent():
    """Apex calls this when the tool is opened. Must return a ToolPropertyContainer."""
    my_toolProperty = apex_sdk.ToolPropertyContainer()

    my_toolProperty.TitleText = "Example Tool"
    my_toolProperty.TitleImageUriString = os.path.join(
        os.path.dirname(current_file_path), r"res\exampleTool.png")

    my_toolProperty.IsCustomTool = True
    my_toolProperty.IsObjectPropertyControl = False

    my_toolProperty.ToolPropertyContent = getCustomToolPropertyContent()

    # Green check mark.
    my_toolProperty.AppliedCommand = apex_sdk.ActionCommand(
        System.Action(HandleApplyButton))

    # Let the user pick targets in the viewport.
    my_toolProperty.ShowPickChoice = True
    my_toolProperty.PickFilterList = setPickFilterList()

    return my_toolProperty


# --- layout ------------------------------------------------------------------

def getCustomToolPropertyContent():
    """Build the panel. Must return a Panel subclass once there is >1 control."""
    my_Grid = WPFControls.Grid()

    my_Grid.RowDefinitions.Add(WPFControls.RowDefinition())
    my_Grid.RowDefinitions.Add(WPFControls.RowDefinition())
    my_Grid.ColumnDefinitions.Add(WPFControls.ColumnDefinition())
    my_Grid.ColumnDefinitions.Add(WPFControls.ColumnDefinition())

    # Row 0 -- mesh size
    meshSizeLabel = WPFControls.TextBlock()
    meshSizeLabel.Text = "Mesh Size:"
    WPFControls.Grid.SetRow(meshSizeLabel, 0)
    WPFControls.Grid.SetColumn(meshSizeLabel, 0)

    global meshSizeTextBox
    meshSizeTextBox = WPFControls.TextBox()
    meshSizeTextBox.Text = "5.0"
    WPFControls.Grid.SetRow(meshSizeTextBox, 0)
    WPFControls.Grid.SetColumn(meshSizeTextBox, 1)

    my_Grid.Children.Add(meshSizeLabel)
    my_Grid.Children.Add(meshSizeTextBox)

    # Row 1 -- mesh type
    meshTypeLabel = WPFControls.TextBlock()
    meshTypeLabel.Text = "Mesh Type:"
    WPFControls.Grid.SetRow(meshTypeLabel, 1)
    WPFControls.Grid.SetColumn(meshTypeLabel, 0)

    global meshTypeComboBox
    meshTypeComboBox = WPFControls.ComboBox()
    # These strings are the keys the worker looks up -- keep them in step.
    for label in ("Mixed", "Quadrilateral", "Triangle"):
        item = WPFControls.ComboBoxItem()
        item.Content = label
        meshTypeComboBox.Items.Add(item)
    meshTypeComboBox.SelectedIndex = 0
    WPFControls.Grid.SetRow(meshTypeComboBox, 1)
    WPFControls.Grid.SetColumn(meshTypeComboBox, 1)

    my_Grid.Children.Add(meshTypeLabel)
    my_Grid.Children.Add(meshTypeComboBox)

    return my_Grid


# --- pick filter -------------------------------------------------------------

def setPickFilterList():
    """Restrict what the user can pick. Must be a .NET List[String]."""
    pickChoices = System.Collections.Generic.List[System.String]()

    pickChoices.Add(apex_sdk.PickFilterTypes.ExclusivePicking)
    pickChoices.Add(apex_sdk.PickFilterTypes.VisibilityPicking)

    pickChoices.Add(apex_sdk.PickFilterTypes.Part)
    pickChoices.Add(apex_sdk.PickFilterTypes.Solid)
    pickChoices.Add(apex_sdk.PickFilterTypes.Surface)

    return pickChoices


# --- handlers ----------------------------------------------------------------

# The decorator is mandatory: without it an uncaught exception terminates Apex.
@apex_sdk.errorhandler
def HandleApplyButton():
    """Called on every Apply click. Read controls, build the dict, hand off."""
    dictionary = {}
    dictionary["MeshSize"] = meshSizeTextBox.Text
    dictionary["MeshType"] = meshTypeComboBox.Text

    # runScriptFunction is the only supported way to reach the Apex API from
    # here. Arguments: worker path, function name in it, dictionary of inputs.
    # Every key and value is converted to a string on the way across.
    apex_sdk.runScriptFunction(
        os.path.join(current_file_path, r"example_tool.py"),
        "example_tool",
        dictionary)
