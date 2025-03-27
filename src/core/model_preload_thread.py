from PySide6.QtCore import QThread, Signal
import torch
from ultralytics import YOLO
import config.my_config as my_config
import dlib
from src.outer_lab.facenet_pytorch import InceptionResnetV1

class ModelPreloadThread(QThread):
    preload_finished = Signal(dict)

    def run(self):
        models = {}
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        models['yolo'] = YOLO(my_config.MODEL_PATH).to(device)
        models['landmarks_extractor'] = dlib.shape_predictor(my_config.LANDMARK_PATH)
        models['face_feature_extractor'] = InceptionResnetV1(pretrained='vggface2').eval().to(device)   
        self.preload_finished.emit(models)