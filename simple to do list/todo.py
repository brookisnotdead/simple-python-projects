"""
todo.py - Main Entry Point (PyQt5 GUI Version)

This is the main file that runs the to-do list application with a PyQt5 GUI.
It imports the GUI window class and starts the graphical interface.

The application follows a clean architecture pattern:
- todo_logic.py: Contains the business logic (data management)
- todo_gui_qt.py: Contains the PyQt5 user interface
- todo.py: Entry point that starts the GUI application
"""

import sys  # System utilities, needed for PyQt5 argument handling

# Import QApplication which manages the GUI application
from PyQt5.QtWidgets import QApplication

# Import the TodoApp window class from our GUI module
from todo_gui_qt import TodoApp


def main():
    """
    Main function - starts the PyQt5 application.
    
    This function:
    1. Creates a QApplication object (required by PyQt5)
    2. Creates an instance of the main window (TodoApp)
    3. Shows the window
    4. Starts the event loop (waits for user interactions)
    """
    # Create a QApplication instance
    # This manages the GUI application's control flow and settings
    # sys.argv is passed so PyQt5 can handle command-line arguments
    app = QApplication(sys.argv)
    
    # Create the main application window
    window = TodoApp()
    
    # Display the window on screen
    window.show()
    
    # Start the event loop
    # This keeps the application running and responsive to user events
    # It will exit when the user closes the window
    sys.exit(app.exec_())


# This checks if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the GUI application
    main()
