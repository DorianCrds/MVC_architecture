import sys

from PySide6.QtWidgets import QApplication

from src.controllers.main_controller import MainController
from src.views.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = MainController()
    window = MainWindow(controller)
    window.show()
    sys.exit(app.exec())
