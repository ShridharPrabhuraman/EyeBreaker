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
import tracemalloc

playsound('hollow-582.mp3')

face_model = get_face_detector()
landmark_model = get_landmark_model()
loaded_model = pickle.load(open('mymodel.save', 'rb'))

# cap.release()
# print(cap)
tracemalloc.start()

def process():
    cap = cv2.VideoCapture(0)
    taking_break = True
    buffer = 0
    buffer_2 = 0
    threshold = 6
    multiple = 1
    start = time.time()
    old_time = start

    while True:
        # print('Working' if taking_break==False else 'Taking Break')
        snapshot1 = tracemalloc.take_snapshot()
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
                            if int(end-start) > 6:
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
                        if int(end-start) > 60*multiple:
                            multiple += 1
                            print(f'It\'s been {int(end-start)} seconds. Take a break now!')
                            playsound('hollow-582.mp3')
                        
                        if buffer_2 >3:
                            cap.release()
                            buffer_2 = 0
                            time.sleep(15)
                        
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
            cap = cv2.VideoCapture(0)
        snapshot2 = tracemalloc.take_snapshot()
        top_stats = snapshot2.compare_to(snapshot1, 'lineno')
        print("[ Top 10 differences ]")
        for stat in top_stats[:10]:
            print(stat)
                            
                            



process()
# ret, img = cap.read()


# cnt = 0
# start = time.time()
# print(start)
# while True:
#     time.sleep(0.5)
#     if cnt==35:
#         break
#     cnt += 1
#     ret, img = cap.read()
#     if ret == True:
#         faces = find_faces(img, face_model)
#         for face in faces:
#             orig,marks = detect_marks(img, landmark_model, face)
            
#             c = np.reshape(marks,(136,1)).T
#             res = loaded_model.predict(c)
#             print('Straight' if res[0]==1 else 'RELAXED')
            


#             draw_marks(img, marks, color=(0, 255, 0))
#         cv2.imshow('img', img)
#         # print(marks)
#         if cv2.waitKey(1) == 113:
#             break

# end = time.time()
# print(end - start)