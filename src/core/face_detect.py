from PySide6.QtCore import (
    QThread,
    Signal,
)

from PySide6.QtGui import (
    QImage,
    
)

import cv2
import torch
from ultralytics import YOLO
from config import my_config
import dlib
import numpy as np
from src.data_model.qt_data_models import PersonInfoModel
from typing import cast
from PIL import Image, ImageDraw, ImageFont
import time
from src.outer_lab.facenet_pytorch import InceptionResnetV1

from datetime import datetime

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FaceDetection(QThread):
    #创建对应的信号
    update_frame_signal = Signal(QImage)
    transform_face_ids = Signal(int)

    def __init__(self, video_source, preloaded_model, stu_dao):
        super().__init__()

        self.is_running = True
        self.cap = cv2.VideoCapture(video_source)
        self.model_input_w = 640
        self.model_input_h = 640

        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # 使用预加载模型或者重新加载
        if preloaded_model:
            self.model = preloaded_model['yolo']
            self.landmarks_extractor = preloaded_model['landmarks_extractor']
            self.face_feature_extractor = preloaded_model['face_feature_extractor']
            
        else:
            self.model = YOLO(my_config.MODEL_PATH).to(self.device)
            self.landmarks_extractor = dlib.shape_predictor(my_config.LANDMARK_PATH)
            self.face_feature_extractor = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)

        self.stu_dao = stu_dao

    def run(self):
        while self.is_running:
            ret, frame = self.cap.read()
            
            now = datetime.now()
            print(now)

            if not ret:
                break
            
            frame_bgr = frame
            frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
            frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
            
            h, w, ch = frame.shape
            scale_x = self.model_input_w  / w
            scale_y  = self.model_input_h / h

            input = cv2.resize(frame_rgb, (self.model_input_w, self.model_input_h))
            input = torch.from_numpy(input).permute(2, 0, 1).float()
            input = input / 255.
            input = input.unsqueeze(0).to(self.device)

            res = self.model(input, verbose=False)

            boxes = res[0].boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                x1, y1, x2, y2 = int(x1 / scale_x), int(y1 / scale_y), int(x2 / scale_x), int(y2 / scale_y)
                #因为只有一个识别种类，人脸，因此cls只有0这一个值
                
                s = time.time()
                face_box = dlib.rectangle(x1, y1, x2, y2)
                landmarks = self.landmarks_extractor(frame_gray, face_box)
                aligned_face_bgr = dlib.get_face_chip(frame_bgr, landmarks)
                aligned_face_rgb = cv2.cvtColor(aligned_face_bgr, cv2.COLOR_BGR2RGB)
                
                #剪裁时间大概为4ms，影响不大,特征提取时间大概为40ms
                face_feature = self.face_feature_extractor(torch.from_numpy(aligned_face_rgb).permute(2, 0, 1).unsqueeze(0).float().to(self.device))
                face_feature = face_feature.cpu().detach().numpy()
 
                id = self.stu_dao.search_id_by_feature(face_feature)
                if id:
                    id = int(id)
                    self.transform_face_ids.emit(id)
                    #查询人脸的相关信息
                    name = self.stu_dao.get_name_by_id(id)

                    #将人名和id显示在对应的人脸框上边
                    frame_rgb = self.put_text_to_img(frame_rgb, f"{name}, {id}", x1, y1)
                
                cv2.rectangle(frame_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            #完成这一帧的操作后，将对应的图片发送给界面进行显示
            qimage = QImage(frame_rgb, w, h, w * ch, QImage.Format_RGB888)
            self.update_frame_signal.emit(qimage)
            cv2.waitKey(1000 // 30)  # 控制帧率

    def put_text_to_img(self, img, text, x, y):
        #对应的图片显示文字
        font_path = my_config.FONT_PAHT
        font =  ImageFont.truetype(font_path, 50)
        pil_image = Image.fromarray(img)
        draw = ImageDraw.Draw(pil_image)
        draw.text((x, y), text, font=font, fill=(0, 0, 255))
        img = np.array(pil_image)
        
        return img

    def stop(self):
        self.is_running = False
        self.quit()
        self.wait()



