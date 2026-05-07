# Simple To-Do List Application

A modern graphical to-do list application built with PyQt5 that saves your tasks to a text file.

## Features

- ✓ Modern PyQt5 graphical user interface
- ✓ Add new tasks with a single click or by pressing Enter
- ✓ View all tasks in a clean list
- ✓ Remove individual tasks with one click
- ✓ Clear all tasks at once (with confirmation)
- ✓ Automatically saves to `tasks.txt`
- ✓ Tasks persist between sessions
- ✓ **Clean Code Architecture**: Separated logic and GUI for easy learning
- ✓ Responsive and user-friendly interface with styling

## Project Structure

This project is separated into clean modules for educational purposes:

### Files:

1. **todo.py** - Main Entry Point
   - Starts the PyQt5 GUI application
   - Imports and initializes the main window
   - Handles the event loop

2. **todo_logic.py** - Business Logic Layer
   - Handles all data management (load, save, add, remove tasks)
   - Works with the `tasks.txt` file
   - No GUI code here - completely independent
   - Functions: `load_tasks()`, `save_tasks()`, `add_task()`, `remove_task()`, etc.
   - **Can be reused** with different interfaces (CLI, web, etc.)

3. **todo_gui_qt.py** - PyQt5 User Interface Layer
   - Beautiful graphical interface using PyQt5
   - Handles all user interaction (buttons, input fields, lists)
   - Shows messages and confirmations
   - Main class: `TodoApp` - the main window

4. **todo_gui.py** - (Optional) Original CLI Interface
   - Command-line interface for learning
   - Can be used as an alternative to the GUI

### Architecture Pattern:

```
todo.py (Main Entry Point)
    └── Imports from todo_gui_qt.py
        └── TodoApp class (PyQt5 GUI)
            └── Imports from todo_logic.py
                └── Task management functions
```

## How to Run

### Requirements

- Python 3.x
- PyQt5 library

### Installation

1. **Install PyQt5:**
   ```bash
   pip install PyQt5
   ```

### Usage

1. Open a terminal/command prompt in this folder
2. Run: `python todo.py`
3. The GUI window will open with your to-do list
4. Use the interface to:
   - **Add Task**: Type in the text field and click "Add Task" or press Enter
   - **Remove Task**: Select a task in the list and click "Remove Selected"
   - **Clear All**: Click "Clear All" to remove all tasks (with confirmation)

## Project Files

- `todo.py` - Main application entry point (PyQt5)
- `todo_gui_qt.py` - PyQt5 graphical interface with detailed comments
- `todo_logic.py` - Logic and data management functions with detailed comments
- `todo_gui.py` - (Optional) Original CLI interface for reference
- `tasks.txt` - Auto-created file that stores your tasks

## Code Comments for Learning

Each file contains detailed comments explaining:

- What each class and function does
- How the parameters work
- What the function returns
- Why certain design decisions were made

This structure makes it easy to:

- ✓ Understand the PyQt5 GUI code
- ✓ Understand the MVC (Model-View-Controller) pattern
- ✓ Learn how to separate logic from presentation
- ✓ Modify the GUI without affecting the data logic
- ✓ Reuse the logic module in other projects (like a web interface or mobile app)

## GUI Features Explained

### Main Window

- **Title**: Shows application name
- **Task List**: Displays all your tasks with smooth scrolling
- **Input Field**: Type your task here
- **Add Task Button**: Green button to add tasks (keyboard shortcut: Enter)
- **Remove Selected**: Red button to remove the selected task
- **Clear All**: Orange button to remove all tasks with confirmation

### Styling

- Color-coded buttons for visual feedback
- Hover effects on buttons and tasks
- Selected task highlighting
- Clean, modern appearance

## Task Storage Format

Tasks are saved one per line in `tasks.txt`:

```
Buy groceries
Finish project
Schedule meeting
```
