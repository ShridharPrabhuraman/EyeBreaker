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
from playsound import playsound

playsound('hollow-582.mp3')

face_model = get_face_detector()
landmark_model = get_landmark_model()
loaded_model = pickle.load(open('mymodel.save', 'rb'))
running_process = False

def process_kill():
    global running_process
    running_process = False


def process(focus_time=600,break_time=60,camera_time=45,threshold=7):
    cap = cv2.VideoCapture()
    cap.open(0,cv2.CAP_DSHOW)

    taking_break = True
    buffer = 0
    buffer_2 = 0
    threshold = threshold
    multiple = 1
    start = time.time()
    old_time = start
    global running_process
    running_process = True

    while running_process:
        time.sleep(0.5)
        
        ret, img = cap.read()
        if ret == True:
            faces = find_faces(img, face_model)
            if len(faces) == 1:
                orig,marks = detect_marks(img, landmark_model, faces[0])
                c = np.reshape(marks,(136,1)).T
                res = loaded_model.predict(c)[0]
                print('Straight' if res==1 else 'RELAXED')
                if taking_break:
                    if res==1:
                        buffer+=1
                        if buffer>=threshold:
                            taking_break = False
                            buffer = 0
                            end = time.time()
                            if int(end-start) > break_time:
                                print(f'Break finished after {int(end-start)} seconds.')
                                playsound('hollow-582.mp3')
                                multiple = 1
                                start = time.time()
                            else:
                                start = old_time
                    else:
                        buffer = 0
                else:
                    if res==1:
                        buffer = 0
                        end = time.time()
                        buffer_2 += 1
                        if int(end-start) > focus_time*multiple:
                            multiple += 1
                            print(f'It\'s been {int( (end-start)/60)} minutes. Take a break now!')
                            playsound('hollow-582.mp3')
                        
                        if buffer_2 >3:
                            cap.release()
                            buffer_2 = 0
                            time.sleep(camera_time)
                        
                    else:
                        buffer += 1
                        buffer_2 = 0
                        if buffer>=threshold:
                            print('Taking Break.')
                            taking_break = True
                            old_time = start
                            start = time.time()
            elif len(faces)==0:
                print('Relaxed. No one present.')
                if taking_break:
                    buffer=0
                else:
                    buffer += 1
                    buffer_2 = 0
                    if buffer>=threshold:
                        print('Taking Break.')
                        taking_break = True
                        old_time = start
                        start = time.time()
        else:
            cap.open(0,cv2.CAP_DSHOW)
        
                            
                            

# process()