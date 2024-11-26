import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar, QCheckBox, QPushButton, QDialog,
    QDialogButtonBox, 
    QVBoxLayout,
    QMessageBox,
    QWidget,
)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize
from enum import Enum
from random import randint
from MainWindow import Ui_MainWindow
from LayoutLabels import Ui_LayoutLabel
from Dialog import Ui_MyDialog

class LayoutLabel(QWidget, Ui_LayoutLabel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class EmployeeDlg(QDialog, Ui_MyDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("hello world")
        
        self.pushButton.clicked.connect(self.change_icon)

    def change_icon(self):
        self.w = EmployeeDlg()
        self.w.exec()



app = QApplication(sys.argv)

w = MainWindow()
w.show()
app.exec()