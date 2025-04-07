import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ui.login_window import LoginWindow
from PySide6.QtWidgets import QApplication
import datetime



def exception_hook(exctype, value, traceback):
    print(f"未捕获的异常: {exctype.__name__}: {value}")
    print("详细错误信息:")
    import traceback as tb
    tb.print_tb(traceback)
    # 保存到日志文件
    with open("error_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - 未捕获的异常: {exctype.__name__}: {value}\n")
        tb.print_tb(traceback, file=f)
    sys.__excepthook__(exctype, value, traceback)

if __name__ == "__main__":
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)    

    login_window = LoginWindow()
    login_window.show()

    app.exec()


