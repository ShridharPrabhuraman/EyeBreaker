import time
import sys
import cv2
import numpy as np
import math
import pandas as pd
from face_detector import get_face_detector, find_faces
from face_landmarks import get_landmark_model, detect_marks, draw_marks

face_model = get_face_detector()
landmark_model = get_landmark_model()
cap = cv2.VideoCapture(0)
ret, img = cap.read()

class_value = int(sys.argv[1])
timing = int(sys.argv[2])

df_orig = pd.DataFrame()
df = pd.DataFrame()

cnt = 0
while True:
    if cnt==timing:
        break
    cnt += 1
    ret, img = cap.read()
    time.sleep(1)
    if ret == True:
        faces = find_faces(img, face_model)
        for face in faces:
            orig,marks = detect_marks(img, landmark_model, face)
            
            c = np.reshape(orig,(136,1))
            df2 = pd.DataFrame(c)
            df2 = df2.T
            df2['class'] = class_value
            df_orig = df_orig.append(df2)

            
            c = np.reshape(marks,(136,1))
            df2 = pd.DataFrame(c)
            df2 = df2.T
            df2['class'] = class_value
            df = df.append(df2)


            draw_marks(img, marks, color=(0, 255, 0))
        cv2.imshow('img', img)
        if cv2.waitKey(1) == 113:
            break

df.to_csv('my_csv.csv',mode='a', header=False)
df_orig.to_csv('my_csv_orig.csv',mode='a', header=False)
