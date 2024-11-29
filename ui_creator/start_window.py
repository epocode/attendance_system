from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel
)
from PySide6.QtCore import (
    Qt,

)
from MainWindow import Ui_MainWindow
import sys

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #连接槽函数
        self.btn_collect_face.clicked.connect(lambda idx=1: print(idx   ))
        # self.btn_collect_face.clicked.connect(self.on_btn_clicked)

    def on_btn_clicked(self):
        print("btn clicked")
        self.stackedWidget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    app.exec()