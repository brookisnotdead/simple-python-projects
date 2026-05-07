"""
todo_gui_qt.py - PyQt5 GUI Implementation

This module provides a graphical user interface for the to-do list
using PyQt5. It replaces the command-line interface with a modern,
user-friendly desktop application.

Components:
- Main window with a task list display
- Input field to add new tasks
- Buttons for adding and removing tasks
- Persistent task storage through todo_logic module
"""

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QLineEdit, QPushButton, QMessageBox,
    QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

# Import the logic module to handle data management
from todo_logic import load_tasks, add_task, remove_task


class TodoApp(QMainWindow):
    """
    Main application window for the To-Do List.
    
    This class creates and manages the GUI for the to-do list application.
    It inherits from QMainWindow which is the base class for top-level windows.
    """
    
    def __init__(self):
        """
        Initialize the application window.
        
        This sets up:
        - Window title and size
        - All GUI components (widgets)
        - Event connections (buttons, input fields)
        - Initial task list display
        """
        # Call the parent class constructor
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("To-Do List Application")  # Window title
        self.setGeometry(100, 100, 600, 500)  # Position (100,100) and size (600x500)
        
        # Load existing tasks from file
        self.tasks = load_tasks()
        
        # Initialize the GUI components
        self.initUI()
    
    def initUI(self):
        """
        Initialize all user interface components.
        
        This method creates and arranges all the widgets:
        - Main container (central widget)
        - Title label
        - Task list display area
        - Input field for new tasks
        - Buttons for actions
        """
        # Create the central widget (main container)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create the main vertical layout (arranges items top to bottom)
        main_layout = QVBoxLayout()
        
        # --- Title Section ---
        # Create title label
        title_label = QLabel("📋 My To-Do List")
        # Set font properties for the title
        title_font = QFont()
        title_font.setPointSize(16)  # Font size
        title_font.setBold(True)  # Make it bold
        title_label.setFont(title_font)
        # Add title to layout
        main_layout.addWidget(title_label)
        
        # --- Task List Section ---
        # Create a list widget to display tasks
        # QListWidget is a convenient widget for displaying lists
        self.task_list = QListWidget()
        self.task_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 5px;
            }
            QListWidget::item:hover {
                background-color: #f0f0f0;
            }
            QListWidget::item:selected {
                background-color: #4CAF50;
                color: white;
            }
        """)
        # Populate the list with existing tasks
        self.refresh_task_list()
        # Add task list to layout
        main_layout.addWidget(self.task_list)
        
        # --- Input Section ---
        # Create horizontal layout for input field and add button
        input_layout = QHBoxLayout()
        
        # Create input field for new tasks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")  # Hint text
        # Allow pressing Enter to add task
        self.task_input.returnPressed.connect(self.add_task_action)
        # Add input field to layout
        input_layout.addWidget(self.task_input)
        
        # Create "Add" button
        add_button = QPushButton("Add Task")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        # Connect button to add_task function
        add_button.clicked.connect(self.add_task_action)
        # Add button to layout
        input_layout.addWidget(add_button)
        
        # Add the input layout to main layout
        main_layout.addLayout(input_layout)
        
        # --- Button Section ---
        # Create horizontal layout for action buttons
        button_layout = QHBoxLayout()
        
        # Create "Remove Selected" button
        remove_button = QPushButton("Remove Selected")
        remove_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:pressed {
                background-color: #ba0000;
            }
        """)
        # Connect button to remove_task function
        remove_button.clicked.connect(self.remove_task_action)
        # Add button to layout
        button_layout.addWidget(remove_button)
        
        # Create "Clear All" button
        clear_button = QPushButton("Clear All")
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e68900;
            }
            QPushButton:pressed {
                background-color: #cc7000;
            }
        """)
        # Connect button to clear all function
        clear_button.clicked.connect(self.clear_all_action)
        # Add button to layout
        button_layout.addWidget(clear_button)
        
        # Add button layout to main layout
        main_layout.addLayout(button_layout)
        
        # Set the main layout for the central widget
        central_widget.setLayout(main_layout)
    
    def refresh_task_list(self):
        """
        Update the displayed task list.
        
        This method clears the current display and reloads all tasks
        from the task list, displaying them in the QListWidget.
        """
        # Clear all items from the list widget
        self.task_list.clear()
        
        # Loop through all tasks and add them to the display
        for task in self.tasks:
            # Create a new list item with the task text
            item = QListWidgetItem(task)
            # Add the item to the list widget
            self.task_list.addItem(item)
    
    def add_task_action(self):
        """
        Handle adding a new task.
        
        This is called when:
        - The "Add Task" button is clicked
        - The user presses Enter in the input field
        
        It gets the text from the input field, adds it using the logic module,
        updates the display, and clears the input field.
        """
        # Get the text from the input field
        task_text = self.task_input.text()
        
        # Try to add the task using the logic module
        if add_task(self.tasks, task_text):
            # Success! Clear the input field
            self.task_input.clear()
            # Refresh the display to show the new task
            self.refresh_task_list()
            # Set focus back to input field for next task
            self.task_input.setFocus()
        else:
            # Task was empty, show warning message
            QMessageBox.warning(self, "Empty Task", "Please enter a task before adding.")
    
    def remove_task_action(self):
        """
        Handle removing a selected task.
        
        This is called when the "Remove Selected" button is clicked.
        
        It:
        1. Gets the currently selected task in the list
        2. Removes it using the logic module
        3. Updates the display
        """
        # Get the currently selected item in the list
        selected_item = self.task_list.currentItem()
        
        # Check if an item is actually selected
        if selected_item is None:
            # No item selected, show warning
            QMessageBox.warning(self, "No Selection", "Please select a task to remove.")
            return
        
        # Get the row number (index) of the selected item
        row = self.task_list.row(selected_item)
        
        # Call the remove_task function from logic module (task_number is 1-based)
        success, removed_task = remove_task(self.tasks, row + 1)
        
        if success:
            # Task was removed successfully
            # Refresh the display
            self.refresh_task_list()
    
    def clear_all_action(self):
        """
        Handle clearing all tasks.
        
        This is called when the "Clear All" button is clicked.
        
        It asks for confirmation before deleting all tasks
        (safety measure to prevent accidental deletion).
        """
        # Show confirmation dialog to user
        reply = QMessageBox.question(
            self,  # Parent window
            "Clear All Tasks",  # Dialog title
            "Are you sure you want to delete all tasks? This cannot be undone.",  # Message
            QMessageBox.Yes | QMessageBox.No,  # Buttons available
            QMessageBox.No  # Default button (No)
        )
        
        # Check what button the user clicked
        if reply == QMessageBox.Yes:
            # User confirmed deletion
            # Clear the tasks list
            self.tasks.clear()
            # Save empty list to file
            from todo_logic import save_tasks
            save_tasks(self.tasks)
            # Refresh the display
            self.refresh_task_list()
