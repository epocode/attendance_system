from PySide6.QtWidgets import QStyledItemDelegate, QPushButton, QStyleOptionButton, QStyle, QStyleOption, QStyleOptionButton
from PySide6.QtCore import Qt, Signal, QEvent, QSize

class attendance_btn_delegate(QStyledItemDelegate):
    attendance_clicked_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        button = QPushButton("签到", parent)
        button.setStyleSheet("background-color: rgb(0, 255, 0);")
        button.clicked.connect(lambda: self.attendance_clicked_signal.emit(index.row()))
        return button
    
    