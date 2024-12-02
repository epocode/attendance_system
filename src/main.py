from main_window import MainWindow
from PySide6.QtWidgets import QApplication
import sys 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    app.exec()