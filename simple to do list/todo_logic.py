"""
todo_logic.py - Core Logic and Data Management

This module handles all the business logic for the to-do list application.
It manages task storage, loading, and manipulation operations.
"""

import os

# File path where tasks will be stored
TODO_FILE = "tasks.txt"


def load_tasks():
    """
    Load tasks from the text file.
    
    This function reads the tasks.txt file and returns a list of tasks.
    If the file doesn't exist, it returns an empty list.
    
    Returns:
        list: A list of task strings, or empty list if no tasks exist
    """
    # Check if the tasks.txt file exists
    if os.path.exists(TODO_FILE):
        # Open the file in read mode
        with open(TODO_FILE, "r") as file:
            # Read all lines from the file
            tasks = file.readlines()
            # Strip whitespace from each line and filter out empty lines
            return [task.strip() for task in tasks if task.strip()]
    
    # Return empty list if file doesn't exist yet
    return []


def save_tasks(tasks):
    """
    Save tasks to the text file.
    
    This function takes a list of tasks and writes them to tasks.txt,
    with each task on a new line.
    
    Args:
        tasks (list): A list of task strings to save
    """
    # Open the file in write mode (creates file if it doesn't exist)
    with open(TODO_FILE, "w") as file:
        # Write each task on a separate line
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks, task_text):
    """
    Add a new task to the list.
    
    This function adds a task string to the tasks list and saves it.
    
    Args:
        tasks (list): The current list of tasks
        task_text (str): The text of the new task to add
        
    Returns:
        bool: True if task was added, False if task was empty
    """
    # Strip whitespace from the task
    task_text = task_text.strip()
    
    # Only add non-empty tasks
    if task_text:
        # Add the task to the list
        tasks.append(task_text)
        # Save updated list to file
        save_tasks(tasks)
        return True
    
    # Return False if task was empty
    return False


def remove_task(tasks, task_number):
    """
    Remove a task by its number (1-indexed).
    
    This function removes a specific task from the list by its position.
    
    Args:
        tasks (list): The current list of tasks
        task_number (int): The position of the task to remove (1-based indexing)
        
    Returns:
        tuple: (success: bool, removed_task: str or None)
               Returns (True, task_text) if successful, (False, None) if failed
    """
    # Check if task number is valid (convert from 1-based to 0-based indexing)
    if 1 <= task_number <= len(tasks):
        # Remove the task at the specified index and store it
        removed_task = tasks.pop(task_number - 1)
        # Save the updated list to file
        save_tasks(tasks)
        # Return success with the removed task
        return (True, removed_task)
    
    # Return failure if task number is invalid
    return (False, None)


def get_task_count(tasks):
    """
    Get the total number of tasks.
    
    Args:
        tasks (list): The current list of tasks
        
    Returns:
        int: The number of tasks in the list
    """
    return len(tasks)


def clear_all_tasks(tasks):
    """
    Clear all tasks from the list and file.
    
    WARNING: This operation cannot be undone.
    
    Args:
        tasks (list): The list to clear (will be emptied)
    """
    # Clear the list
    tasks.clear()
    # Save empty list to file (effectively deletes all tasks)
    save_tasks(tasks)
