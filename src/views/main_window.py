from PySide6.QtWidgets import QMainWindow

from src.views.ui_designer.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.controller = controller
