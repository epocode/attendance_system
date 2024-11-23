import sys
import os
from random import choice
import pathlib
import numpy as np
from random import choice

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLCDNumber,
    QMainWindow,
    QLineEdit,
    QLabel,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QListWidget,
)
from PySide6.QtGui import QAction, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QSize


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        widget = Color('red')
        self.setCentralWidget(widget)


os.chdir(pathlib.Path(__file__).parent)

app = QApplication([])
window = MainWindow()

window.show()
app.exec()


