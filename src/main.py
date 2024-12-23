import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ui.login_window import LoginWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # mainwindow = MainWindow()
    # mainwindow.show()

    login_window = LoginWindow()
    login_window.show()

    app.exec()