from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QToolBar,

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
from mainwindow import Ui_MainWindow
import resources
import sys
import cv2
from ultralytics import YOLO
import torch
import os


class CameraThread(QThread):
    update_frame_signal = Signal(QImage)

    def __init__(self, video_source):
        super().__init__()
        self.video_source = video_source
        self.stop_flag = False
        self.mutex = QMutex()
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        # self.model = YOLO('weights/yolov8n.pt').to(self.device)
        
        self.model = YOLO('C:/Users/shann/Desktop/SE/attendance_system/nothing/train2/weights/best.pt').to(self.device)

    def run(self):
        self.cap = cv2.VideoCapture(self.video_source)
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame_resized = cv2.resize(frame, (640, 640))
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            frame_tensor = torch.from_numpy(frame_rgb).permute(2, 0, 1).float()
            frame_tensor = frame_tensor / 255.
            frame_tensor = frame_tensor.unsqueeze(0).to(self.device)
            results = self.model(frame_tensor)

            for result in results[0].boxes:
                x1, y1, x2, y2 = result.xyxy[0].tolist()  # 获取框的坐标
                conf = result.conf[0].tolist()  # 获取置信度
                cls = result.cls[0].tolist()  # 获取类别，0 是人类
                if int(cls) == 0:
                    cv2.rectangle(frame_rgb, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame_rgb, f"confidence: {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            h, w, ch = frame_rgb.shape
            bytes_per_line = w * ch
            qimage = QImage(frame_rgb, w, h, bytes_per_line, QImage.Format_RGB888)
            self.update_frame_signal.emit(qimage)
            # self.mutex.unlock()
            cv2.waitKey(1000 // 30)  # 控制帧率

    def stop(self):
        self.cap.release()
        self.quit()
        self.wait()  # 等待线程彻底退出


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        print(os.getcwd())

        self.stackedWidget.setCurrentIndex(0)
        #toolbar
        self.toolbar = self.addToolBar("tool bar")
        
        action_back_home = QAction(QIcon(":/icons/home"), 'home', self)
        action_back_home.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.toolbar.addAction(action_back_home)

        # 设置视频显示
        self.camera_thread = None

        #连接槽函数
        self.btn_collect_face.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_face_detect.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_start.clicked.connect(self.start_show_video)
        self.btn_end.clicked.connect(self.end_show_video)

    def start_show_video(self):
        if self.camera_thread is not None and self.camera_thread.isRunning():
            self.camera_thread.stop()
        self.camera_thread = CameraThread('data/video/classroom.mp4')
        self.camera_thread.update_frame_signal.connect(self.update_video)
        self.camera_thread.start()

    def update_video(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        self.label_disp_video.setPixmap(pixmap)

    def end_show_video(self):
        if self.camera_thread is not None:
            self.camera_thread.stop()
            self.camera_thread = None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    app.exec()