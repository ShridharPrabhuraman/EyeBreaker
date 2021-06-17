import time
import sys
import cv2
import numpy as np
import math
import pandas as pd
from face_detector import get_face_detector, find_faces
from face_landmarks import get_landmark_model, detect_marks, draw_marks
import pickle
import sklearn

face_model = get_face_detector()
landmark_model = get_landmark_model()
loaded_model = pickle.load(open('mymodel.save', 'rb'))
cap = cv2.VideoCapture(0)
ret, img = cap.read()


cnt = 0
while True:
    if cnt==2000:
        break
    cnt += 1
    ret, img = cap.read()
    if ret == True:
        faces = find_faces(img, face_model)
        for face in faces:
            orig,marks = detect_marks(img, landmark_model, face)
            
            c = np.reshape(marks,(136,1)).T
            res = loaded_model.predict(c)
            print('Straight' if res[0]==1 else 'RELAXED')
            


            draw_marks(img, marks, color=(0, 255, 0))
        cv2.imshow('img', img)
        # print(marks)
        if cv2.waitKey(1) == 113:
            break

