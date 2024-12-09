import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os
import openface
import dlib

cap = cv2.VideoCapture('data/video/head-pose-face-detection-male.mp4')

align = openface.AlignDlib("data/shape_predictor_68_face_landmarks.dat")
face_pose = openface.PoseEstimator()

detector = dlib.get_frontal_face_detector()
predictor  = dlib.shape_predictor("data/shape_predictor_68_face_landmarks.dat")

model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-225.0, 170.0, -135.0),     # Left eye left corner
                            (225.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner
                         
                        ])
                        
 
 
 
def get_euler_angle(rotation_vector):
    # 将旋转向量转换为旋转矩阵
    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

    # 计算 sy 值
    sy = math.sqrt(rotation_matrix[0, 0] ** 2 + rotation_matrix[1, 0] ** 2)
    singular = sy < 1e-6  # 检查是否存在奇异情况

    if not singular:
        # 非奇异情况
        pitch = math.atan2(rotation_matrix[2, 1], rotation_matrix[2, 2])  # 俯仰角
        yaw = math.atan2(-rotation_matrix[2, 0], sy)  # 偏航角
        roll = math.atan2(rotation_matrix[1, 0], rotation_matrix[0, 0])  # 翻滚角
    else:
        # 奇异情况（即接近 ±90 度）
        pitch = math.atan2(-rotation_matrix[1, 2], rotation_matrix[1, 1])
        yaw = math.atan2(-rotation_matrix[2, 0], sy)
        roll = 0

    # 转换为角度并进行范围调整
    Y = int((pitch / math.pi) * 180)
    X = int((yaw / math.pi) * 180)
    Z = int((roll / math.pi) * 180)

    return X, Y, Z
 
while True:
    flag, img = cap.read()
    size = img.shape
    focal_length = size[1]
    center = (size[1]/2, size[0]/2)
    camera_matrix = np.array(
                                [[focal_length, 0, center[0]],
                                [0, focal_length, center[1]],
                                [0, 0, 1]], dtype = "double"
                                )

    #print("Camera Matrix :\n {0}".format(camera_matrix)

    # 取灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 人脸数rects
    rects = detector(img_gray, 0)
    #for i in range(len(rects)):
    point_list=[]
    if len(rects)>0:
        landmarks = list((p.x, p.y) for p in predictor(img, rects[0]).parts())

        point_list.append(landmarks[30])
        point_list.append(landmarks[8])
        point_list.append(landmarks[36])
        point_list.append(landmarks[45])
        point_list.append(landmarks[48])
        point_list.append(landmarks[54])

        for idx, point in enumerate(point_list):
            cv2.circle(img, point, 2, color=(0, 255, 0))
    #        font = cv2.FONT_HERSHEY_SIMPLEX
    #        cv2.putText(img, str(idx + 1), None, font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)


        image_points =  np.array(point_list,dtype="double")

        print(model_points)
        print(image_points)
        print('--------------------------------------------------------------------------------')

        dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
        success, rotation_vector, translation_vector = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)#SOLVEPNP_P3P/SOLVEPNP_ITERATIVE

        print("Rotation Vector:\n {0}".format(rotation_vector))
        print("Translation Vector:\n {0}".format(translation_vector))


        X1,Y1,Z1 = get_euler_angle(rotation_vector)

        print("=====================>",X1,Y1,Z1 )

        # Project a 3D point (0, 0, 1000.0) onto the image plane.

        # We use this to draw a line sticking out of the nose

        (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)


        for p in image_points:
            #cv2.circle(img, (int(p[0]), int(p[1])), 3, (0,0,255), -1)

            p1 = ( int(image_points[0][0]), int(image_points[0][1]))
            p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
            cv2.line(img, p1, p2, (255,0,0), 2)
            if X1 < -45 or X1 > 45:
                cv2.putText(img, 'Turn your head to the left' if X1 < -45 else 'Turn your head to the right', (10, 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2) 
            if Y1 < -30 or Y1 > 30:
                cv2.putText(img, 'Tilt you head up' if Y1 < -45 else 'Tilt you head down', (10, 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)
            if Z1 < -20 or Z1 > 20:
                cv2.putText(img, 'do not tilt you head' if Z1 < -45 else 'do not tilt you head', (10, 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("src",img)
    cv2.waitKey(50)
    cv2.imwrite("dst.jpg",img)

cap.release()
