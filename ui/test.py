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
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt, QSize



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(-3)
        slider.setMaximum(10)
        slider.setSingleStep(3)  
        slider.valueChanged.connect(self.value_chagned)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(slider)

    def value_chagned(self, value):
        print('value changed ', value)

    def slider_position(self, position):
        print('position: ', position)
    
    def slider_pressed(self):
        print('pressed')
    
    def slider_released(self):
        print('released')


os.chdir(pathlib.Path(__file__).parent)

app = QApplication([])
window = MainWindow()

window.show()
app.exec()


