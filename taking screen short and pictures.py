import os,time
from datetime import datetime
from cv2 import *
import re

now = datetime.now()
dirName = re.sub('[^a-zA-Z0-9 \n\.]', ' ',now.strftime("%d/%m/%Y %H:%M:%S"))
dirName += str(now.microsecond)
print(dirName)
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


cam = VideoCapture(0)# 0 -> index of camera
for i in range(100):
    s, img = cam.read()
    if s:
        now = datetime.now()
        fileName = re.sub('[^a-zA-Z0-9 \n\.]', '',now.strftime("%H:%M:%S"))
        fileName += str(now.microsecond)
        imwrite(dirName+"/"+fileName+".jpg",img)#save image
    else:
        print("some error")
        break
    time.sleep(.5)
cam.release()

