import os
import cv2
from PIL import Image
import numpy as np
import os.path
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from sklearn.svm import SVC
import pickle
import time
# cap=cv2.VideoCapture(0)
# while(1):    # get a frame
#     num = 0
#     path = ("E:\\picture")
#     time.sleep(1.8)
#     ret, frame = cap.read()    # show a frame
#     cv2.imwrite(path+str[num]+'.jpg', frame)
#     cv2.imshow("capture", frame)
#     num+=1
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
im = cv2.imread("E:\\3.jpg")
cv2.imshow("1", im)
m, n = 4, 7
height = 480
width = 640
im = cv2.resize(im,(width, height))
width1 = int(((n-3.5)/n)*width)
w = int(120+width1)
height1 = int(((m-2)/m)*height)
h = int((1/m)*height + height1)
img1 = im[(height1):h,(width1):w]
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,60,param1=60,param2=40,minRadius=30,maxRadius=50)
print(circles)
print(len(circles[0]))
for circle in circles[0]:
    x = int(circle[0])
    y = int(circle[1])
    r = int(circle[2])
    img = cv2.circle(img2,(x, y),r,(0,0,255),1)
cv2.imshow("p", img2)
dst = img1[(y-r):(y+r),(x-r):(x+r)]
cv2.imshow("1", dst)
cv2.waitKey()
cv2.destroyAllWindows()