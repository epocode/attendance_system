
import torch.nn as nn
from torch.autograd import Variable
from torchvision import transforms
import torch.backends.cudnn as cudnn
import torchvision
import torch.nn.functional as F
from PIL import Image
import torch

from . import hopenet
import cv2
from skimage import io
import dlib
from config import my_config

class HeadPosePred():
    def __init__(self, device=None):
        if device == None:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = hopenet.Hopenet(torchvision.models.resnet.Bottleneck, [3, 4, 6, 3], 66).to(device)
        self.model.eval()
        saved_state_dict = torch.load(my_config.POSE_NODE_NET_WEIGHT, map_location=device)
        self.model.load_state_dict(saved_state_dict)
        self.transformations = transforms.Compose([transforms.Resize(224),
        transforms.CenterCrop(224), transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
        self.device = device

    def pred_node_pose(self, img, ):
        cudnn.enabled = True

        idx_tensor = [idx for idx in range(66)]
        idx_tensor = torch.FloatTensor(idx_tensor).to(self.device)

        img = Image.fromarray(img)
        img = self.transformations(img)

        img_shape = img.size()
        img = img.view(1, img_shape[0], img_shape[1], img_shape[2])
        img = Variable(img).to(self.device)


        yaw, pitch, roll = self.model(img)

        # yaw shape: [1, 66]
        yaw_predicted = F.softmax(yaw, dim=-1)
        pitch_predicted = F.softmax(pitch, dim=-1)
        roll_predicted = F.softmax(roll, dim=-1)
        # Get continuous predictions in degrees.
        yaw_predicted = torch.sum(yaw_predicted.data[0] * idx_tensor) * 3 - 99
        pitch_predicted = torch.sum(pitch_predicted.data[0] * idx_tensor) * 3 - 99
        roll_predicted = torch.sum(roll_predicted.data[0] * idx_tensor) * 3 - 99

        print(yaw_predicted, pitch_predicted, roll_predicted)
        #随便设定一个阈值，后面再进行调整
        if (yaw_predicted < -30 or yaw_predicted > 30 or pitch_predicted < -20 or pitch_predicted > 20 or
            roll_predicted < -10 or roll_predicted > 10):
            return (False, "请把头摆正")
        return (True, "")


