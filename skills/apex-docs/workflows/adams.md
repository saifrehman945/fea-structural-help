# Adams multibody entities — tool procedures

Numbered procedures from the MSC Apex in-product workflow database (`docSearchData_Apex_1.0_en.xml`). **This content is not published on the web** — it ships with the installation, so it cannot be fetched and has no online equivalent.

Read `references/interaction-conventions.md` first: MMB ends a selection stage in most tools, and Auto vs Manual variants differ by exactly that click.

## Contents

- [Bushing](#bushing-node-adams-bushing)
- [Contact](#contact-node-adams-contact)
- [Contact Properties](#contact-properties-node-adams-contact-properties)
- [Coupler](#coupler-node-adams-coupler-constraint)
- [Curve-Curve Constraint](#curve-curve-constraint-node-adams)
- [Gear](#gear-node-adams-gear-constraint)
- [Joint Motion](#joint-motion-node-adams-joint-motion)
- [Joints and Joint Primitives](#joints-and-joint-primitives-node-adams-joint-and-jprims)
- [Point-Curve Constraint](#point-curve-constraint-node-adams-point-curve-constraint)
- [Scripted Simulation](#scripted-simulation-node-adams-scripted-simulation)
- [Single Component Force](#single-component-force-node-adams-single-component-force)
- [Translational SpringDamper](#translational-springdamper-node-adams-translational-springdamper)

---

## Bushing (node Adams_Bushing)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Creation method - 2 Bodies, 1 Location - Automatic Mode**

1. Select the entities to associate with Part 1
2. Select the entities to associate with Part 2

**Creation method - 2 Bodies, 1 Location - Manual Mode**

1. Select the entities to associate with Part 1
2. Click MMB
3. Select the entities to associate with Part 2
4. Click MMB
5. Select the entities to specify the location
6. Click MMB
7. Select the entities to specify the orientation
8. Click MMB

**Creation method - 2 Bodies, 2 Locations - Automatic Mode**

1. Select the entities to associate with Part 1
2. Select the entities to associate with Part 2

**Creation method - 2 Bodies, 2 Locations - Manual Mode**

1. Select the entities to associate with Part 1
2. Click MMB
3. Select the entities to specify the location on Part 1
4. Click MMB
5. Select the entities to specify the orientation on Part 1
6. Click MMB
7. Select the entities to associate with Part 2
8. Click MMB
9. Select the entities to specify the location on Part 2
10. Click MMB
11. Select the entities to specify the orientation on Part 2
12. Click MMB

**Creation method - 2 Interfaces - Automatic Mode**

1. Select the Interface associated with Part 1
2. Select the Interface associated with Part 2

**Creation method - 2 Interfaces - Manual Mode**

1. Select the Interface associated with Part 1
2. Select the Interface associated with Part 2

Tips:

- To multi select in either end, hold down the CTRL or SHIFT key and select the entities

---

## Contact (node Adams_Contact)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Solid to Solid Contact - Manual mode**

1. Select the solid bodies for the First Set
2. Click MMB
3. Select the solid bodies for the Second Set
4. Click MMB

**Solid to Solid Contact - Auto mode**

1. Select the solid bodies for the First Set
2. Select the solid bodies for the Second Set

Tips:

- To multi select, hold down the CTRL or SHIFT key and select the entities

---

## Contact Properties (node Adams_Contact_Properties)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi-select |
| `SHIFT` | Pure Accumulation |
| `CTRL+SHIFT` | Pure Deselection |
| `ESC` | Abort operation |
| `P` | Toggle visibility picking versus occluded picking |

**Contact Properties**

1. Select the Contacts to assign Contact Properties

---

## Coupler (node Adams_Coupler_Constraint)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |

**2 Joints Coupler - Auto mode**

1. Select the Driver Joint
2. Select the Coupled Joint

**2 Joints Coupler - Manual mode**

1. Select the Driver Joint
2. Select the Freedom type if the joint selected was a Cylindrical joint
3. Specify the Displacement or Scale
4. Click MMB
5. Select the Coupled Joint
6. Select the Freedom type if the joint selected was a Cylindrical joint
7. Specify the Displacement or Scale
8. Click MMB

**3 Joints Coupler - Auto mode**

1. Select the Driver Joint
2. Select the Coupled Joint
3. Select the second Coupled Joint

**3 Joints Coupler - Manual mode**

1. Select the Driver Joint
2. Select the Freedom type if the joint selected was a Cylindrical joint
3. Specify the Displacement or Scale
4. Click MMB
5. Select the Coupled Joint
6. Select the Freedom type if the joint selected was a Cylindrical joint
7. Specify the Displacement or Scale
8. Click MMB
9. Select the second Coupled Joint
10. Select the Freedom type if the joint selected was a Cylindrical joint
11. Specify the Displacement or Scale
12. Click MMB

---

## Curve-Curve Constraint (node Adams_曲线_曲线_约束)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi-select |
| `SHIFT` | Pure Accumulation |
| `CTRL+SHIFT` | Pure Deselection |
| `ESC` | Abort operation |
| `P` | Toggle visibility picking versus occluded picking |

**Curve-Curve - Auto mode**

1. Select the entities to define the 1st Curve
2. Select the entities to define the 2nd Curve
3. Optionally specify Displacement and Velocity Initial Conditions
4. Optionally specify a Reference Frame

**Curve-Curve - Manual mode**

1. Select the entities to define the 1st Curve
2. Select the MMB
3. Select the entities to define the 2nd Curve
4. Click MMB
5. Optionally specify Displacement and Velocity Initial Conditions
6. Optionally specify a Reference Frame

---

## Gear (node Adams_Gear_Constraint)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |

**Gear - Auto mode**

1. Select the 1st Joint
2. Select the 2nd Joint (The joint must have the same 2nd part as the 1st joint selected)
3. Select the Common Velocity Interface which is on the same part as 2nd part selected for both the 1st and 2nd joints

**Gear - Manual mode**

1. Select the 1st Joint
2. Click MMB
3. Select the 2nd Joint (The joint must have the same 2nd part as the 1st joint selected)
4. Click MMB
5. Select the Common Velocity Interface which is on the same part as 2nd part selected for both the 1st and 2nd joints
6. Click MMB

---

## Joint Motion (node Adams_Joint_Motion)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Joint Motion - Manual mode**

1. Select the Joint to apply a motion
2. Click MMB

**Joint Motion - Auto mode**

1. Select the Joint to apply a motion

---

## Joints and Joint Primitives (node Adams_Joint_and_JPRIMs)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Joint - Auto mode**

1. Select the entities for the first part that defines the joint
2. Select the entities for the second part that defines the joint

**Joint - Manual mode**

1. Select the entities for the first part that defines the joint
2. Click MMB
3. Select the entities for the second part that defines the joint
4. Click MMB

**Joint 2 Location and 2 Orientation - Manual mode**

1. Select the entities for the first part 1 that defines the joint
2. Click MMB
3. Select the entities for the first part 1 that defines the joint location
4. Click MMB
5. Select the entities for the first part 1 that defines the joint orientation
6. Click MMB
7. Select the entities for the second part 2 that defines the joint
8. Click MMB
9. Select the entities for the first part 2 that defines the joint location
10. Click MMB
11. Select the entities for the first part 2 that defines the joint orientation
12. Click MMB

**Joint - Auto mode**

1. Select the Interface on the first part that defines the joint
2. Select the Interface on the second part that defines the joint

**Joint Interface creation - Manual mode**

1. Select the Interface on the first part that defines the joint
2. Click MMB
3. Select the Interface on the second part that defines the joint
4. Click MMB

Tips:

- To multi-select at either end, hold down the CTRL or SHIFT key and select the entities

---

## Point-Curve Constraint (node Adams_Point_Curve_Constraint)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `CTRL` | Toggle multi-select |
| `SHIFT` | Pure Accumulation |
| `CTRL+SHIFT` | Pure Deselection |
| `ESC` | Abort operation |
| `P` | Toggle visibility picking versus occluded picking |

**Point-Curve - Auto mode**

1. Select the entities to define the Point location
2. Select the entities to define the Curve
3. Optionally specify Displacement and Velocity Initial Conditions
4. Optionally specify a Reference Frame

**Point-Curve - Manual mode**

1. Select the entities to define the Point location
2. Select the MMB
3. Select the entities to define the Curve
4. Click MMB
5. Optionally specify Displacement and Velocity Initial Conditions
6. Optionally specify a Reference Frame

---

## Scripted Simulation (node Adams_Scripted_Simulation)

1. Enter valid Adams Solver Commands and Functions in the Script Commands window.
2. Optionally import acf files from disk by selecting the Import ACF button.
3. Optionally verify the model configuration by selecting the Model Verify button.
4. Simulate the model by selecting the Simulate Button.

---

## Single Component Force (node Adams_Single_Component_Force)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation midway |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to previous selection stage |
| `T` | Change transform manipulator as move mode when defining Joint axis location |
| `R` | Change transform manipulator as rotate mode when defining Joint axis orientation |

**Single Component Force - Manual mode**

1. Enter a function that defines the force
2. Select the entities for the point of application that defines the force
3. Click MMB
4. Select the entities to locate the force
5. Click MMB
6. Select the entities to orient the force
7. Click MMB

**Single Component Force - Auto mode**

1. Enter a function that defines the force
2. Select the interface for the point of application that defines the force
3. Select the interface on part ground whose Z axis orients the force

**Single Component Force - Manual mode**

1. Enter a function that defines the force
2. Select the interface for the action part
3. Click MMB
4. Select the interface for the reaction part
5. Click MMB

**Single Component Force - Auto mode**

1. Enter a function that defines the force
2. Select the interface for the action part
3. Select the interface for the reaction part

**Single Component Force - Manual mode**

1. Enter a function that defines the force
2. Select the interface for the point of application
3. Click MMB
4. Select the interface for the moving reference part whose Z axis orients the force
5. Click MMB

**Single Component Force - Auto mode**

1. Enter a function that defines the force
2. Select the interface for the point of application
3. Select the interface for the moving reference part whose Z axis orients the force

**Single Component Force - Auto mode**

1. Enter a function that defines the force
2. Select the entities for the point of application that defines the force

**Single Component Force - Manual mode**

1. Enter a function that defines the force
2. Select the entities for the point of application
3. Click MMB
4. Select the entities for the moving reference frame
5. Click MMB
6. Select the entities to locate the force on the part
7. Click MMB
8. Select the entities for the location on the reference part
9. Click MMB
10. Select the entities that orient the force
11. Click MMB

**Single Component Force - Auto mode**

1. Enter a function that defines the force
2. Select the entities for the point of application
3. Select the entities for the moving reference frame

**Single Component Force - Manual mode**

1. Enter a function or spring stiffness and damping coefficients that define the force
2. Select the entities for the action part
3. Click MMB
4. Select the entities for the reaction part
5. Click MMB
6. Select the entities to locate the force for the action part
7. Click MMB
8. Select the entities to locate the force for the reaction part
9. Click MMB

**Single Component Force - Auto mode**

1. Enter a function or spring stiffness and damping coefficients that define the force
2. Select the entities for the action part
3. Select the entities for the action part

**Single Component Force - Manual mode**

1. Enter a function that defines the force
2. Select the interface for the point of application that defines the force
3. Click MMB
4. Select the interface on ground whose Z axis orients the force
5. Click MMB

**>Single Component Force - Auto mode**

1. Enter a function that defines the force
2. Select the interface for the point of application that defines the force
3. Select the interface on ground whose Z axis orients the force

**Single Component Force - Manual mode**

1. Enter a function that defines the force
2. Select the interface that defines the location of the force
3. Click MMB
4. Select the interface on part ground whose Z axis orients the force
5. Click MMB

Tips:

- To multi-select at either end, hold down the CTRL or SHIFT key and select the entities

---

## Translational SpringDamper (node Adams_Translational_SpringDamper)

**Keyboard shortcuts**

| Key | Action |
|---|---|
| `H` | Hide preselected faces |
| `SHIFT+H` | Display previous hidden faces |
| `ESC` | Abort operation |
| `P` | Toggle visibility picking versus occluded picking |
| `SHIFT + MMB` | Transitions to first selection stage |
| `SPACEBAR` | Launches compact object properties |

**Creation method - 2 Bodies, 2 Locations - Automatic Mode**

1. Select the entities to associate with Part 1
2. Select the entities to associate with Part 2

**Creation method - 2 Bodies, 1 Locations - Automatic Mode**

1. Select the entities to associate with Part 1
2. Select the entities to associate with Part 2

**Creation method - 2 Bodies, 1 Locations - Manual Mode**

1. Select the entities to associate with Part 1
2. Click MMB
3. Select the entities to associate with Part 2
4. Click MMB
5. Select the entities to specify the location
6. Click MMB
7. Select the entities to specify the orientation
8. Click MMB

**Creation method - 2 Bodies, 2 Locations - Manual Mode**

1. Select the entities to associate with Part 1
2. Click MMB
3. Select the entities to specify the location on Part 1
4. Click MMB
5. Select the entities to specify the orientation on Part 1
6. Click MMB
7. Select the entities to associate with Part 2
8. Click MMB
9. Select the entities to specify the location on Part 2
10. Click MMB
11. Select the entities to specify the orientation on Part 2
12. Click MMB

**Creation method - 2 Interfaces - Automatic Mode**

1. Select the Interface associated with Part 1
2. Select the Interface associated with Part 2

**Creation method - 2 Interfaces - Manual Mode**

1. Select the Interface associated with Part 1
2. Click MMB
3. Select the Interface associated with Part 2
4. Click MMB

Tips:

- To multi select in either end, hold down the CTRL or SHIFT key and select the entities
