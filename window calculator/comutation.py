"""Small calculator functions used by the GUI.

Keeping the math in this file makes the project easier to study:
- window.py handles buttons and the screen
- comutation.py handles the actual arithmetic
"""


def add(*args):
    """Add all numbers passed to this function."""
    result = 0
    for number in args:
        result += number
    return result


def minus(*args):
    """Subtract every number after the first number."""
    if not args:
        return 0

    result = args[0]
    for number in args[1:]:
        result -= number
    return result


def multiplication(*args):
    """Multiply all numbers passed to this function."""
    result = 1
    for number in args:
        result *= number
    return result


def division(first_number, second_number):
    """Divide two numbers.

    We raise an error for division by zero because the GUI can catch that
    error and show a friendly message instead of crashing the program.
    """
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return first_number / second_number
