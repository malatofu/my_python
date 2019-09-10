import cv2
import numpy as np
import time
import sklearn.svm as SVC
import pickle

path_wuchong = "/mnt/myshare/linuxshare/wuchong/circle_"
#path_circle = "/mnt/myshare/linuxshare/circle/circle_"
path_tiaoshi = "/mnt/myshare/linuxshare/tiaoshi/live_"
path_youchong = "/mnt/myshare/linuxshare/youchong/circle_"

y = 174
#y = 129
x = 270
r = 45
num = 0

cap=cv2.VideoCapture()
cap.open("/dev/video0")

input()
while 1:    # get a frame
	if num>0:
		t1 = time.time()#开始计时
	for i in range(5):
		ret, frame = cap.read()    # show a frame
	
	dst = frame[(y-r):(y+r),(x-r):(x+r)]#截圆
	print('circle ok')
	#cv2.imwrite(path_circle+str(num)+'.jpg',dst)
	#开始过模型
	if num==0:
		t1 = time.time()#开始计时
	with open('mx1', 'rb') as fr:
		vocabulary = pickle.load(fr)
	extract = cv2.xfeatures2d.SIFT_create()
	flann_params = dict(algorithm = 1, trees = 5)
	flann = cv2.FlannBasedMatcher(flann_params, {})
	extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)
	extract_bow.setVocabulary(vocabulary)
	
	f = extract_bow.compute(dst, extract.detect(dst))
	x1 = np.array(f)
	
	with open('svm1.pickle', 'rb') as fr:
		new_svm = pickle.load(fr)
		print(new_svm.predict(x1))#得出结果
		
		frame = cv2.rectangle(frame,(x-r,y-r),(x+r,y+r),(0,0,255),5)
		#得出的结果分开两个文件夹
		if new_svm.predict(x1)[0]==1:
			cv2.imwrite(path_youchong+str(num)+'.jpg', dst)
		else:
			cv2.imwrite(path_wuchong+str(num)+'.jpg', dst)
		cv2.imwrite(path_tiaoshi+str(num)+'.jpg', frame)
	print('pic_live',num)
	t2 = time.time()
	print('time_pic',t2-t1)#得出处理结果所需要的时间
	total_time = 2-(t2-t1)
	total_time = round(total_time,3)
	if total_time<2:
		time.sleep(total_time)
	else:
		time.sleep(2)
	num+=1
	if num>3000:
		break
	t3 = time.time()
	print('time_total',t3-t1)
cap.release()
'''
m, n = 4, 7
	height = 480
	width = 640
	im = cv2.resize(frame,(width, height))
	width1 = int(((n-3.5)/n)*width)
	w = int(120+width1)
	height1 = int(((m-2)/m)*height)
	h = int((1/m)*height + height1)
	
	img1 = im[(height1):h,(width1):w]#分割
	
	img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	#cv2.medianBlur(img2,img2,5)
	circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,60,param1=60,param2=40,minRadius=30,maxRadius=50)
	
	print(circles)
	print(len(circles[0]))
	for circle in circles[0]:
		x = int(circle[0])
		y = int(circle[1])
		r = int(circle[2])
		img = cv2.circle(img2,(x, y),r,(0,0,255),1)
	'''