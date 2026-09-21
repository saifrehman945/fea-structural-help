# Authoring custom tools

A custom tool is an Apex plugin: a Python-backed tool that looks and behaves like
a built-in Apex tool, with its own panel, pick filter, and Apply/Exit buttons.

Use a custom tool when the user needs to supply input or pick entities. Use a
plain batch script when the work is fully determined up front.

## Table of contents

1. Architecture
2. Folder structure
3. palette.xml
4. group.xml
5. tool.xml
6. The two-file rule
7. Installing the palette
8. Checklist

## 1. Architecture

A UI tool is always **two Python files**:

| File | Runs as | Imports | Job |
|---|---|---|---|
| `mytool_ui.py` | IronPython, in the Apex UI process | `apex_sdk`, `clr`, `System.Windows.Controls` | build the panel, collect user input |
| `mytool.py` | Apex's CPython interpreter | `apex` | do the modelling work |

The UI file never imports `apex` and never does modelling. It hands a
dictionary of strings to the worker through `apex_sdk.runScriptFunction()`.
Crossing that line — importing the worker and calling it directly, or doing
model work inside the click handler — stalls the Apex user interface.

A tool declared as `batch_tool` has no UI and no `_ui.py`; its single script runs
on invocation.

## 2. Folder structure

The layout *is* the configuration — Apex discovers tools by walking it, so names
like `res`, `src`, `palette.xml`, `group.xml` and `tool.xml` are fixed.

```
<tool palettes folder>/
  <Palette folder>/
    palette.xml
    res/
      palette_icon.png
    <Group folder>/
      group.xml
      <Tool folder>/
        tool.xml
        src/
          mytool_ui.py
          mytool.py
        res/
          tool_icon.png
```

One palettes folder can hold many palettes; a palette holds groups; a group
holds tools.

Keep your tools in a folder of your own rather than extending the installed
`Demo Tools` or `Apex Utilities` folders — an Apex upgrade overwrites those.

## 3. palette.xml

One per palette folder. Groups appear in the order listed here, and each `Name`
must match the `<name>` inside that group's `group.xml`.

```xml
<?xml version="1.0" ?>
<configurations xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <palette>
    <name>My Utilities</name>
    <icon>myUtilities.png</icon>
    <description>In-house modelling utilities</description>
    <tool_groups Version="1.0" LastUpdate="20240101">
      <group Name="Meshing"/>
      <group Name="Query"/>
    </tool_groups>
  </palette>
</configurations>
```

The icon is a 36x36 image in the palette's `res/` folder.

## 4. group.xml

One per group folder. Tools appear in the order listed, and each `Name` must
match the `<name>` inside that tool's `tool.xml`.

```xml
<?xml version="1.0" ?>
<configurations xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <tool_group>
    <name>Meshing</name>
    <description>Meshing helpers</description>
    <tools>
      <tool Name="Mesh Selected Bodies"/>
    </tools>
    <Version>1.0</Version>
  </tool_group>
</configurations>
```

## 5. tool.xml

One per tool folder.

```xml
<?xml version="1.0" ?>
<configurations xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <tool>
    <name>Mesh Selected Bodies</name>
    <icon>meshSelected.png</icon>
    <description>Mesh the picked bodies at a given size</description>
    <tooltype>ui_tool</tooltype>
    <runfile>mesh_selected_bodies_ui.py</runfile>
    <Version>1.0</Version>
  </tool>
</configurations>
```

| Element | Notes |
|---|---|
| `name` | shown on the palette; referenced from `group.xml` |
| `icon` | 36x36 image in this tool's `res/` folder |
| `description` | becomes the tool's advanced tooltip |
| `tooltype` | `ui_tool` or `batch_tool` |
| `runfile` | file in `src/`. For `ui_tool` this is the **UI** file, not the worker |

## 6. The two-file rule

`runfile` points at the UI file. The worker is never registered in XML — the UI
file locates it by path at runtime:

```python
apex_sdk.runScriptFunction(
    os.path.join(current_file_path, r"mesh_selected_bodies.py"),
    "mesh_selected_bodies",
    dictionary)
```

The second argument is the worker **function** name, which need not match the
file name but must exist in that file and accept one dictionary argument.

## 7. Installing the palette

Register the palettes folder through **Options / Application Settings / Custom
Tools**. Apex writes the registration to
`CustomToolPalettesSetting<APEX_VERSION_INFO>.xml` in the user's `MSC_Apex
Workspace` folder. The version suffix means each Apex release keeps its own
custom tool configuration, so several versions can coexist on one machine.

## 8. Checklist

1. Folder names nest palette -> group -> tool, each with its XML file.
2. Every `group Name=` matches a `group.xml` `<name>`; every `tool Name=`
   matches a `tool.xml` `<name>`.
3. `src/` holds the Python; `res/` holds the icons.
4. `runfile` names the UI file for `ui_tool`.
5. The UI file imports `apex_sdk`, never `apex`.
6. The worker file imports `apex`, never `apex_sdk`.
7. Every event handler carries `@apex_sdk.errorhandler`.
8. All model work is reached through `runScript` or `runScriptFunction`.
