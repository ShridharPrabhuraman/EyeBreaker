"""
    An automated program that opens webcam and records video of the user.
    Recording while pressing the button 'F' should be segregated as video clip while looking at monitor.
    Recording while pressing 'T' should be segregated as video clip looking away from monitor.
    Recorded video are to be split into images.

    xtra : track memory consumption of keeping webcam on
"""
import sys
import pathlib
import cv2
import time
from datetime import datetime

def main():

    option = "not"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if option == "facing":
        _path = 'data_collection/facing/'+timestamp
    else:
        _path = 'data_collection/not_facing/'+timestamp
    
    #=================================================================================================================#

    vid = cv2.VideoCapture(0)    
    pathlib.Path(_path).mkdir(exist_ok=True) # Create a folder with timestamp to store images

    #=================================================================================================================#
    sec = 0
    framerate = 1
    count = 1
    while(True):
        frame_exists,frame = vid.read()
        cv2.imshow('frame', frame)  
        if frame_exists:
            cv2.imwrite(_path+"/%d.jpg"%count,frame)
        time.sleep(1)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

main()