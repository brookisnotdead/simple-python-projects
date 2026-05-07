import sys
from PyQt5.QtWidgets import QApplication

from window import MainWindow


def main():
    # QApplication is the object that runs the PyQt event loop.
    # The event loop listens for clicks, keyboard input, window close events, etc.
    app = QApplication(sys.argv)

    # Create our calculator window, show it, then let PyQt take over.
    window = MainWindow()
    window.show()

    # app.exec_() keeps the program alive until the user closes the window.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
