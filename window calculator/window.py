from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from comutation import add, division, minus, multiplication


class MainWindow(QMainWindow):
    """Main calculator window.

    Coding process / design idea:
    1. Build the visual parts first: display, buttons, and layout.
    2. Store calculator state in simple variables.
    3. Connect every button click to a method.
    4. Let the methods update the display after each user action.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(30, 30, 360, 520)
        self.setMinimumSize(320, 460)

        # These variables remember the calculator's current state.
        self.current_text = "0"
        self.stored_value = None
        self.pending_operator = None
        self.should_clear_display = False

        self.display = QLabel(self.current_text)
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setMinimumHeight(90)
        self.display.setObjectName("display")

        self._build_ui()
        self._apply_styles()

    def _build_ui(self):
        """Create the widgets and arrange them on the window."""
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        button_grid = QGridLayout()

        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)
        button_grid.setSpacing(8)

        main_layout.addWidget(self.display)

        # Each tuple is: button text, row, column, row span, column span.
        # This makes the calculator layout easy to change later.
        buttons = [
            ("C", 0, 0, 1, 1),
            ("+/-", 0, 1, 1, 1),
            ("%", 0, 2, 1, 1),
            ("/", 0, 3, 1, 1),
            ("7", 1, 0, 1, 1),
            ("8", 1, 1, 1, 1),
            ("9", 1, 2, 1, 1),
            ("*", 1, 3, 1, 1),
            ("4", 2, 0, 1, 1),
            ("5", 2, 1, 1, 1),
            ("6", 2, 2, 1, 1),
            ("-", 2, 3, 1, 1),
            ("1", 3, 0, 1, 1),
            ("2", 3, 1, 1, 1),
            ("3", 3, 2, 1, 1),
            ("+", 3, 3, 1, 1),
            ("0", 4, 0, 1, 2),
            (".", 4, 2, 1, 1),
            ("=", 4, 3, 1, 1),
        ]

        for text, row, column, row_span, column_span in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(64)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # A lambda lets us send the button text into one shared handler.
            button.clicked.connect(lambda checked, value=text: self._handle_button(value))

            if text in {"+", "-", "*", "/", "="}:
                button.setProperty("buttonType", "operator")
            elif text in {"C", "+/-", "%"}:
                button.setProperty("buttonType", "utility")

            button_grid.addWidget(button, row, column, row_span, column_span)

        main_layout.addLayout(button_grid)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def _apply_styles(self):
        """Style the calculator with simple Qt stylesheet rules."""
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #202124;
            }

            QLabel#display {
                background-color: #111315;
                border: 1px solid #3c4043;
                border-radius: 8px;
                color: #f8f9fa;
                font-size: 42px;
                font-weight: 600;
                padding: 12px;
            }

            QPushButton {
                background-color: #3c4043;
                border: none;
                border-radius: 8px;
                color: #f8f9fa;
                font-size: 24px;
                font-weight: 500;
            }

            QPushButton:hover {
                background-color: #4b4f52;
            }

            QPushButton:pressed {
                background-color: #5f6368;
            }

            QPushButton[buttonType="operator"] {
                background-color: #1a73e8;
            }

            QPushButton[buttonType="operator"]:hover {
                background-color: #2b7de9;
            }

            QPushButton[buttonType="operator"]:pressed {
                background-color: #1967d2;
            }

            QPushButton[buttonType="utility"] {
                background-color: #5f6368;
            }

            QPushButton[buttonType="utility"]:hover {
                background-color: #6f7378;
            }
            """
        )

    def _handle_button(self, value):
        """Send the clicked button to the correct calculator action."""
        if value.isdigit():
            self._input_digit(value)
        elif value == ".":
            self._input_decimal()
        elif value in {"+", "-", "*", "/"}:
            self._choose_operator(value)
        elif value == "=":
            self._calculate_result()
        elif value == "C":
            self._clear()
        elif value == "+/-":
            self._toggle_sign()
        elif value == "%":
            self._convert_to_percent()

    def _input_digit(self, digit):
        """Add a digit to the number currently shown on the display."""
        if self.should_clear_display or self.current_text == "0":
            self.current_text = digit
            self.should_clear_display = False
        else:
            self.current_text += digit

        self._update_display()

    def _input_decimal(self):
        """Add a decimal point, but only if the number does not have one yet."""
        if self.should_clear_display:
            self.current_text = "0"
            self.should_clear_display = False

        if "." not in self.current_text:
            self.current_text += "."

        self._update_display()

    def _choose_operator(self, operator):
        """Remember the selected operator and prepare for the next number."""
        current_value = self._display_value()

        # If the user presses another operator before equals, calculate the
        # previous operation first. Example: 2 + 3 * becomes 5 waiting for *.
        if self.stored_value is not None and self.pending_operator is not None:
            if not self._calculate_result():
                return
            current_value = self._display_value()

        self.stored_value = current_value
        self.pending_operator = operator
        self.should_clear_display = True

    def _calculate_result(self):
        """Run the stored operation and show the answer."""
        if self.stored_value is None or self.pending_operator is None:
            return True

        current_value = self._display_value()

        try:
            result = self._apply_operator(
                self.stored_value,
                current_value,
                self.pending_operator,
            )
        except ZeroDivisionError:
            self.current_text = "Error"
            self.stored_value = None
            self.pending_operator = None
            self.should_clear_display = True
            self._update_display()
            return False

        self.current_text = self._format_number(result)
        self.stored_value = None
        self.pending_operator = None
        self.should_clear_display = True
        self._update_display()
        return True

    def _apply_operator(self, first_number, second_number, operator):
        """Call the math function that matches the selected operator."""
        if operator == "+":
            return add(first_number, second_number)
        if operator == "-":
            return minus(first_number, second_number)
        if operator == "*":
            return multiplication(first_number, second_number)
        if operator == "/":
            return division(first_number, second_number)

        raise ValueError(f"Unknown operator: {operator}")

    def _clear(self):
        """Reset the calculator back to its starting state."""
        self.current_text = "0"
        self.stored_value = None
        self.pending_operator = None
        self.should_clear_display = False
        self._update_display()

    def _toggle_sign(self):
        """Turn a positive number negative, or a negative number positive."""
        if self.current_text == "Error":
            self._clear()
            return

        value = self._display_value() * -1
        self.current_text = self._format_number(value)
        self._update_display()

    def _convert_to_percent(self):
        """Convert the current number into a percentage."""
        if self.current_text == "Error":
            self._clear()
            return

        value = self._display_value() / 100
        self.current_text = self._format_number(value)
        self._update_display()

    def _display_value(self):
        """Convert the display text into a number for calculations."""
        if self.current_text == "Error":
            return 0

        return float(self.current_text)

    def _format_number(self, number):
        """Make answers look clean by removing unnecessary .0 endings."""
        if number == int(number):
            return str(int(number))

        return str(round(number, 10))

    def _update_display(self):
        """Refresh the label so the user sees the newest value."""
        self.display.setText(self.current_text)
