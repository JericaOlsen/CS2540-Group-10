# UVSim - Virtual Machine Simulator

## Source control link
https://github.com/JericaOlsen/CS2540-Group-10

## Overview

**UVSim** is a software-based virtual machine developed to help computer science students learn machine language and computer architecture. It enables students to execute machine language programs using a simple instruction set known as **BasicML**.

## Features

- Simulates a CPU with an accumulator register and control register.
- Handles input and output operations.
- Supports arithmetic and memory operations.
- Allows conditional and unconditional branching.
- Provides an interactive interface for program execution.
- Updated UI:
    - A new menu with "Load Program", "Save Program", "Change Color" buttons has been added n enabling users to customize the interface colors through a dedicated color selection window and load new files.
    - A built-in text editor allows direct editing of program instructions.

## System Requirements

- **Operating System**: Windows, macOS, or Linux  
- **Python Version**: Python 3.7 or higher  
- **Memory**: At least 512MB of RAM  
- **Storage**: At least 50MB of free disk space  
- **Dependencies**: pytest is required to run tests (along with built-in Python features like `unittest.mock`) 

## System Components

### CPU (Central Processing Unit)
- **Accumulator**: Stores intermediate results during calculations.
- **Control Register (CR)**: Keeps track of the instruction currently being executed.

### Memory
- A **100-word memory** (indexed from `00` to `99`), used for storing both instructions and data.
- Each memory location can store a **four-digit signed integer** (e.g., `+1234` or `-5678`).
- The **BasicML program** must be loaded starting at memory location `00`.

## Instruction Set (BasicML)

### I/O Operations

| Opcode | Instruction | Description |
|--------|------------|-------------|
| `10`   | `READ`     | Read a word from the keyboard into a specific memory location. |
| `11`   | `WRITE`    | Write a word from a specific memory location to the screen. |

### Load/Store Operations

| Opcode | Instruction | Description |
|--------|------------|-------------|
| `20`   | `LOAD`     | Load a word from a specific memory location into the accumulator. |
| `21`   | `STORE`    | Store the value in the accumulator into a specific memory location. |

### Arithmetic Operations

| Opcode | Instruction | Description |
|--------|------------|-------------|
| `30`   | `ADD`      | Add a word from memory to the accumulator. |
| `31`   | `SUBTRACT` | Subtract a word from memory from the accumulator. |
| `32`   | `DIVIDE`   | Divide the accumulator by a word from memory. |
| `33`   | `MULTIPLY` | Multiply the accumulator by a word from memory. |

### Control Operations

| Opcode | Instruction | Description |
|--------|------------|-------------|
| `40`   | `BRANCH`       | Jump to a specific memory location. |
| `41`   | `BRANCHNEG`    | Jump to a specific memory location if the accumulator is negative. |
| `42`   | `BRANCHZERO`   | Jump to a specific memory location if the accumulator is zero. |
| `43`   | `HALT`         | Stop execution of the program. |

## Program Execution & Running UVSim

1. ### Load the Program:
    Place your BasicML program in a text file (e.g., program.txt). Use the `Load Program` button to import the file into the built-in text editor.

2. ### Edit & Save:
    You can directly edit your program in the text editor. When ready, click the `Save Program` button to save the validated instructions to a file.

3. ### Execute:
    Click the `Execute Program` button to load the instructions into memory and run them sequentially starting from memory location 00. Execution continues until a HALT instruction (43) is encountered.

4. ### Interactive I/O:
    During execution, the simulator prompts for input (when needed) and displays output via dialog windows.

5. ### Customizing the UI:
    Use the `Change Color` button next to the Save button to open a color selection window and customize the UI colors (window foreground/background and button foreground/background).

## Updated Program Execution

- ### Top Button Panel:
    The new interface features a top panel with three buttons:

    - #### Load Program: 
        Loads a program file into the text editor.
    - #### Save Program:
        Saves the content of the text editor to a file.
    - #### Change Color: 
        Opens a dedicated window to customize UI colors (window foreground/background and button foreground/background).

- ### Text Editor:
    Provides an area to directly edit and validate BasicML instructions before execution.

- ### Execution Feedback:
    Output and input dialogs provide real-time feedback during program execution.


## Error Handling

- Ensures valid numerical input for the **READ** instruction.
- Detects **division by zero** and halts execution with an error message.
- Handles **unknown opcodes** by stopping execution and displaying an error message.
- Provides warnings for **invalid program instructions** in the input file.

## Configuration File
UVSim uses a configuration file (config.ini) to store UI color settings. An example configuration file is provided below:

```ini
Copy code
[window]
background = #FFFFFF
foreground = #000000

[button]
background = #4C721D
foreground = black
```

## Example Program (BasicML)

```plaintext
1007  # READ value into memory[07]
2007  # LOAD memory[07] into accumulator
3008  # ADD value at memory[08] to accumulator
2109  # STORE result in memory[09]
1109  # WRITE value at memory[09] to screen
4300  # HALT program execution
```

## Contributors

- Diego Martinez Cardenas
- Jerica Olsen
- Jared Brewer