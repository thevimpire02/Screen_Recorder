import cv2  # screenshot frame by frame
import pyautogui # for recording relatead
from win32api import GetSystemMetrics  # works on resolution of screeen
import numpy as np
import time  # duration to capture vedio

width = GetSystemMetrics(0)
height = GetSystemMetrics(1) # caputure full screen 

dimension = (width, height)

format = cv2.VideoWriter_fourcc(*"mp4v") # format of vedio ex mp4, adi, voc etc

output = cv2.VideoWriter("test.mp4",format, 30.0, dimension) # location of storage of vedio

now_start_time = time.time() # starting time

duration = 10 # extra time for compilation of code duration 

end_time = now_start_time + duration

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB) # firmating frame by frame in original view

    output.write(frame)
    currnet_time = time.time()
    if currnet_time > end_time:
        break

output.release()
print("---END---")
