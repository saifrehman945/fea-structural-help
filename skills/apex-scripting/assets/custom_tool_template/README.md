# Custom tool template

A complete, minimal Apex plugin. Copy the tree, rename the folders, and edit.

```
custom_tool_template/          <- your tool palettes folder
  palette.xml
  res/
    myUtilities.png            <- 36x36, add your own
  Example Group/
    group.xml
    Example Tool/
      tool.xml
      src/
        example_tool_ui.py     <- WPF panel, IronPython, imports apex_sdk
        example_tool.py        <- modelling worker, imports apex
      res/
        exampleTool.png        <- 36x36, add your own
```

The example tool meshes whatever the user picks, at a size and element shape
they choose.

## Renaming checklist

Three names must agree in three places, or the tool silently fails to appear:

1. `palette.xml` `<group Name="...">` == `group.xml` `<name>`
2. `group.xml` `<tool Name="...">` == `tool.xml` `<name>`
3. `tool.xml` `<runfile>` == the UI file in `src/`

And inside the UI file:

4. The path in `runScriptFunction(...)` == the worker file in `src/`
5. The function name in `runScriptFunction(...)` == the function in the worker

## Icons

Both `res/` folders need a 36x36 image matching the `<icon>` element. The
template references `myUtilities.png` and `exampleTool.png`; they are not
included.

## Installing

Register the top folder through **Options / Application Settings / Custom
Tools** in Apex.

## Turning it into a batch tool

For a tool with no panel: set `<tooltype>batch_tool</tooltype>`, point
`<runfile>` at a single script, and delete the `_ui.py`. Start from
`../template_batch_script.py` instead.
