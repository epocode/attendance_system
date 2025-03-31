from PySide6.QtCore import (
    QThread,
    QMutex,
    Signal,

)
from PySide6.QtGui import (
    QImage,

)
import os

import cv2
from ultralytics import YOLO
from config import my_config
import torch
import dlib
import numpy as np
from src.outer_lab.node_pose_net  import HeadPosePred
import time
import logging
from PIL import Image, ImageDraw, ImageFont
from src.outer_lab.facenet_pytorch import InceptionResnetV1

logger = logging.getLogger(__name__)


class FaceTaker(QThread):
    update_frame_signal = Signal(QImage)
    select_face_signal = Signal(QImage)

    def __init__(self, video_source, preloaded_models=None):
        super().__init__()

        self.is_running = True
        self.video_source = video_source
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # 使用预加载模型或者重新加载
        if preloaded_models:
            self.model = preloaded_models['yolo']
            self.landmarks_extractor = preloaded_models['landmarks_extractor']
            self.face_feature_extractor = preloaded_models['face_feature_extractor']
        else:
            self.model = YOLO(my_config.MODEL_PATH).to(self.device)
            self.landmarks_extractor = dlib.shape_predictor(my_config.LANDMARK_PATH)
            self.face_feature_extractor = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)

        self.check_flag = True
        self.quality_checker = FaceQualityCheck()
        self.stored_face_rgb = None

        self.blank_img = cv2.cvtColor(cv2.imread(os.path.join(my_config.PHOTO_PATH, 'blank.jpg')), cv2.COLOR_BGR2RGB)
        self.send_img(self.blank_img, self.update_frame_signal)
        self.blank_img_s = cv2.cvtColor(cv2.imread(os.path.join(my_config.PHOTO_PATH, 'blank_s.jpg')), cv2.COLOR_BGR2RGB)
        self.send_img(self.blank_img_s, self.select_face_signal)

    def run(self):
        self.cap = cv2.VideoCapture(self.video_source)
        for _ in range(5):
            self.cap.read()

        enter_tips = ""

        while self.is_running:
            start_time = time.time()
            ret, frame = self.cap.read()
            if not ret:
                break
            h, w, ch = frame.shape
            scale_x = 640. / w
            scale_y = 640. / h
            
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            #下面的是用于输入模型的张量
            frame_resized = cv2.resize(frame_rgb, (640, 640))
            frame_tensor = torch.from_numpy(frame_resized).permute(2, 0, 1).float()
            frame_tensor = frame_tensor / 255.
            frame_tensor = frame_tensor.unsqueeze(0).to(self.device)
            results = self.model(frame_tensor, verbose=False)#返回一个列表，表示一个批量图片预测结果。但是当前批量为1


            end_time_yolo = time.time()
            x1, y1, x2, y2 = 0, 0, 0, 0
            
            #因为只有一个批量，因此获取这一帧预测到的boxes
            boxes = results[0].boxes
            num_boxes = len(boxes)
            for box in boxes:
                #遍历这一帧所有检测到的人脸框
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                x1, y1, x2, y2 = int(x1 / scale_x), int(y1 / scale_y), int(x2 / scale_x), int(y2 / scale_y) 
                conf = box.conf[0].tolist()  # 获取置信度
                cls = box.cls[0].tolist()  # 获取类别，0 是人脸
                if int(cls) == 0:
                    if num_boxes > 1:
                        enter_tips = '请保持镜头一张人脸'
                    else:
                        # 对读取到的图片进行判断，是否满足人脸的要求
                        if self.check_flag:
                            #提取识别到的人脸
                            face_box = dlib.rectangle(x1, y1, x2, y2)
                            
                            landmarks = self.landmarks_extractor(frame_gray, face_box)
                            aligned_face_bgr = dlib.get_face_chip(frame, landmarks)
                            aligned_face_rgb = cv2.cvtColor(aligned_face_bgr, cv2.COLOR_BGR2RGB)

                           
                            check_result = self.quality_checker.check(frame, aligned_face_rgb)
                            
                            #check_result 格式(是否满足要求， 不满足要求的原因)
                            if check_result[0]:
                                #将当前的bgr格式的人脸保存下来，便于后面进行特征的提取
                                self.stored_face_rgb = aligned_face_rgb

                                self.send_img(aligned_face_rgb, self.select_face_signal)
                                self.check_flag = False
                            else:
                                #提示用户人脸录入不正常
                                enter_tips = check_result[1]

                    cv2.rectangle(frame_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)

            frame_rgb = self.put_text_to_img(frame_rgb, enter_tips, int(w / 2), int(h / 2))
            enter_tips = ""

            self.send_img(frame_rgb, self.update_frame_signal)
            cv2.waitKey(1000 // 30)  # 控制帧率

        self.cap.release()

    def put_text_to_img(self, img, text,  x, y):
        font_path = my_config.FONT_PAHT
        font = ImageFont.truetype(font_path, 40)
        pil_img = Image.fromarray(img)
        draw = ImageDraw.Draw(pil_img)
        draw.text((x, y), text, font=font, fill=(0, 0, 255))
        img = np.array(pil_img)
        
        return img

    def stop(self):
        self.send_img(self.blank_img, self.update_frame_signal)
        self.send_img(self.blank_img_s, self.select_face_signal)
        self.is_running = False
        self.quit()
        self.wait()  

    def send_img(self, img, s):
        #s表示要使用的信号
        h, w, ch = img.shape
        qimage = QImage(img, w, h, w * ch, QImage.Format_RGB888)
        s.emit(qimage)

    def resume(self):
        self.send_img(self.blank_img_s, self.select_face_signal)
        self.check_flag = True

    def get_face_feature(self):
        if self.stored_face_rgb is None:
            return
        face_feature = self.face_feature_extractor(torch.from_numpy(self.stored_face_rgb).permute(2, 0, 1).unsqueeze(0).float().to(self.device))
        face_feature = face_feature.cpu().detach().numpy()
        self.stored_face_rgb = None
        return face_feature

class FaceQualityCheck:
    def __init__(self):
        self.head_pose_pred = HeadPosePred()

    
    def luminance_check(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        luminance = np.mean(gray_frame)
        if luminance >= 100 and luminance <= 200:
            return (True, None)
        elif luminance < 100:
            return (False, '亮度过低')
        else:
            return (False, '亮度过高')
        
    def check(self, frame, face_frame):
        luminance = self.luminance_check(frame)
        if luminance[0] == False:
            return luminance
        
        head_pos_rs = self.head_pose_pred.pred_node_pose(face_frame)
        if head_pos_rs[0] == False:
            return head_pos_rs

        return (True, '')
    

