from PySide6.QtWidgets import QStyledItemDelegate, QPushButton, QStyleOptionButton, QStyle, QStyleOption, QStyleOptionButton
from PySide6.QtCore import Qt, Signal, QEvent, QSize

class BtnDelegate(QStyledItemDelegate):
    btn_clicked_signal = Signal(int)

    def __init__(self, function_name, parent=None):
        super().__init__(parent)
        self.function_name = function_name

    def createEditor(self, parent, option, index):
        button = QPushButton(self.function_name, parent)
        button.setStyleSheet("background-color: rgb(0, 255, 0);")
        button.setProperty("class", "custom-btn")
        button.clicked.connect(lambda: self.btn_clicked_signal.emit(index.row()))
        return button
    
    