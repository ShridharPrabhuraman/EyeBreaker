import time
import sys
import cv2
import numpy as np
import math
import pandas as pd
from face_detector import get_face_detector, find_faces
from face_landmarks import get_landmark_model, detect_marks, draw_marks

face_model = get_face_detector()        # import face model
landmark_model = get_landmark_model()   # import landmark model
cap = cv2.VideoCapture(0)               # record video from webcam, to be accesed via object 'cap'
ret, img = cap.read()                   # read frames out of recorded video (real time)

class_value = int(sys.argv[1])          # ?
timing = int(sys.argv[2])               # Provide Timing (secs?) upto which the frames should be recorded

df_orig = pd.DataFrame()                # a dataframe to store ________
df = pd.DataFrame()                     # a dataframe to store ________

cnt = 0                                 # initialize counter to 0
while True:                             # Infinite loop
    if cnt==timing:                     # If time is up, stop recording frames
        break
    cnt += 1
    ret, img = cap.read()                       # ret == True if frame exists ;  img == frame
    time.sleep(1)                               # a delay of 1 second to induce 1 FPS
    if ret == True:                             # if frame exists
        faces = find_faces(img, face_model)     # find faces from the captured frame
        for face in faces:                      # for each face identified
            orig,marks = detect_marks(img, landmark_model, face)    # detect marks
            
            c = np.reshape(orig,(136,1))        # ??   
            df2 = pd.DataFrame(c)               # ??
            df2 = df2.T                         # ??
            df2['class'] = class_value          # ??
            df_orig = df_orig.append(df2)       # ??

            
            c = np.reshape(marks,(136,1))       # ??
            df2 = pd.DataFrame(c)               # ??
            df2 = df2.T                         # ??
            df2['class'] = class_value          # ??
            df = df.append(df2)                 # ??

            draw_marks(img, marks, color=(0, 255, 0)) # draw the marks in image

        cv2.imshow('img', img)                  # display each captured frame to the user
        if cv2.waitKey(1) == 113:               # ??
            break

df.to_csv('my_csv.csv',mode='a', header=False)                  # save df as CSV
df_orig.to_csv('my_csv_orig.csv',mode='a', header=False)        # save df_orig as CSV
