from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QToolBar,
    QDockWidget,


)
from PySide6.QtCore import (
    Qt,
    QThread,
    Signal,
    QMutex,

)
from PySide6.QtGui import (
    QAction,
    QIcon,
    QImage,
    QPixmap,

)
from ui_main_window import Ui_MainWindow
import resources
import sys
import cv2
from ultralytics import YOLO
import torch
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config.my_config as my_config
from face_take import FaceTaker

    
class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        print(os.getcwd())

        self.stackedWidget.setCurrentIndex(0)
        #toolbar
        self.toolbar = self.addToolBar("tool bar")
        self.toolbar
        
        action_back_home = QAction(QIcon(":/icons/home"), 'home', self)
        action_back_home.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.toolbar.addAction(action_back_home)

        #将工具栏停放到左侧
        dock  = QDockWidget()
        dock.setWidget(self.toolbar)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        # 设置视频显示
        self.face_taker = None

        #连接槽函数
        self.btn_collect_face.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_face_detect.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_start.clicked.connect(self.start_show_video)
        self.btn_end.clicked.connect(self.end_show_video)

    def start_show_video(self):
        if self.face_taker is not None:
            return
        self.face_taker = FaceTaker(my_config.VIDEO_PATH)
        self.face_taker.update_frame_signal.connect(self.update_video)
        self.face_taker.select_face_signal.connect(self.face_get)
        self.btn_confirm.clicked.connect(self.face_taker.resume)
        self.btn_pass.clicked.connect(self.face_taker.resume)

        self.face_taker.start()

    def update_video(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        self.label_disp_video.setPixmap(pixmap)

    def end_show_video(self):
        if self.face_taker is not None:
            self.face_taker.stop()
            self.face_taker = None

    def face_get(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        self.label_face.setPixmap(pixmap)
    
    def closeEvent(self, event):
        self.end_show_video()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    app.exec()