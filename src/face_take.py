from PySide6.QtCore import (
    QThread,
    QMutex,
    Signal,

)
from PySide6.QtGui import (
    QImage,

)
import cv2
from ultralytics import YOLO
from config import my_config
import torch
import dlib
import numpy as np


class FaceTaker(QThread):
    update_frame_signal = Signal(QImage)
    select_face_signal = Signal(QImage)

    def __init__(self, video_source):
        super().__init__()
        self.video_source = video_source
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(my_config.MODEL_PATH).to(self.device)

        self.check_flag = True
        self.quality_checker = FaceQualityCheck()

    def run(self):
        self.cap = cv2.VideoCapture(self.video_source)
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            h, w, ch = frame.shape
            scale_x = 640. / w
            scale_y = 640. / h
            frame_resized = cv2.resize(frame, (640, 640))
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            frame_tensor = torch.from_numpy(frame_rgb).permute(2, 0, 1).float()
            frame_tensor = frame_tensor / 255.
            frame_tensor = frame_tensor.unsqueeze(0).to(self.device)
            results = self.model(frame_tensor)
            x1, y1, x2, y2 = 0, 0, 0, 0
            for result in results[0].boxes:
                x1, y1, x2, y2 = result.xyxy[0].tolist()  # 获取框的坐标
                conf = result.conf[0].tolist()  # 获取置信度
                cls = result.cls[0].tolist()  # 获取类别，0 是人脸
                if int(cls) == 0:
                    x1, y1, x2, y2 = int(x1 / scale_x), int(y1 / scale_y), int(x2 / scale_x), int(y2 / scale_y) 
                    frame_rgb = cv2.resize(frame_rgb, (frame.shape[1], frame.shape[0]))
                                #对读取到的图片进行判断，是否满足人脸的要求

                    if self.check_flag:
                        check_result = self.quality_checker.check(frame)
                        if check_result[0]:
                            face_h, face_w = y2 - y1, x2 - x1
                            if face_h > face_w:
                                face_w = face_h
                            else:
                                face_h = face_w
                
                            face_frame = frame_rgb[y1:y1+face_h, x1:x1+face_w]
                            face_frame = cv2.resize(face_frame, (128, 128))
                            qface_image = QImage(face_frame, 128, 128, 128 * ch, QImage.Format_RGB888)
                            self.select_face_signal.emit(qface_image)
                            self.check_flag = False
                        else:
                            #提示用户人脸录入不正常
                            pass

                    cv2.rectangle(frame_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame_rgb, f"confidence: {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


            bytes_per_line = w * ch
            qimage = QImage(frame_rgb, w, h, bytes_per_line, QImage.Format_RGB888)
            self.update_frame_signal.emit(qimage)
            # self.mutex.unlock()
            cv2.waitKey(1000 // 30)  # 控制帧率

    def stop(self):
        self.cap.release()
        self.quit()
        self.wait()  

    def resume(self):
        self.check_flag = True

class FaceQualityCheck:
    def __init__(self):
        pass

    
    def face_gesture_check(self, frame):
        #frame(h, w, c) and BGR
        detector = dlib.get_front_face_detector()

    def luminance_check(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        luminance = np.mean(gray_frame)
        if luminance >= 100 and luminance <= 200:
            return (True, None)
        elif luminance < 100:
            return (False, '亮度过低')
        else:
            return (False, '亮度过高')
        
    def check(self, frame):
        luminance = self.luminance_check(frame)
        if luminance[0] == False:
            return luminance
        return (True, None)
