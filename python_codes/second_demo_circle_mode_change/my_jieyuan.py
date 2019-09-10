import cv2
import numpy as np
import time
import sklearn.svm as SVC
import pickle

path_wuchong = "/mnt/myshare/linuxshare/wuchong/circle_"
path_yuantu = "/mnt/myshare/linuxshare/yuantu/live_"
path_tiaoshi = "/mnt/myshare/linuxshare/tiaoshi/live_"
path_youchong = "/mnt/myshare/linuxshare/youchong/circle_"
path_circle = "/mnt/myshare/linuxshare/circle/circle_"
path_fengmi = "/mnt/myshare/linuxshare/fengmi/circle_"

y = 174
#y = 129
x = 270
r = 65
num = 0

cap=cv2.VideoCapture()
cap.open("/dev/video0")

input("press enter button")

while 1:    # get a frame
	if num>0:
		t1 = time.time()#开始计时
	for i in range(5):
		ret, frame = cap.read()    # show a frame
	cv2.imwrite(path_yuantu+str(num)+'.jpg', frame)
	
	dst = frame[(y-r):(y+r),(x-r):(x+r)]#截圆
	#cv2.imshow("1",dst)
	
	#检测圆，重新截图
	gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
	shape = np.shape(gray)
	#for i in range(shape[0]):
	#	for j in range(shape[1]):
	#		if gray[i][j] > 60:
	#			gray[i][j] == 255
	#			pass
	#		else:
	#			gray[i][j] == 0

	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,60,param1=100,param2=32,minRadius=30,maxRadius=50)
	
	if circles is None:
		r=45
		dst = frame[(y-r):(y+r),(x-r):(x+r)]#截圆
		r=65
	else:
		for circle in circles[0,:]:
			print(circle)
			cir_x = int(circle[0])
			cir_y = int(circle[1])
			cir_r = int(circle[2])
		dst = frame[(cir_y+y-r-cir_r):(cir_y+y-r+cir_r),(cir_x+x-r-cir_r):(cir_x+x-r+cir_r)]
		#dst = frame[(y-r):(y+r),(x-r):(x+r)]#截圆
	print('circle ok')
	#cv2.imshow("2",dst)
	cv2.imwrite(path_circle+str(num)+'.jpg',dst)
	
	#开始过模型
	if num==0:
		t1 = time.time()#开始计时
	with open('zuixinfl', 'rb') as fr:
		vocabulary = pickle.load(fr)
	extract = cv2.xfeatures2d.SIFT_create()
	flann_params = dict(algorithm = 1, trees = 5)
	flann = cv2.FlannBasedMatcher(flann_params, {})
	extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)
	extract_bow.setVocabulary(vocabulary)
	
	f = extract_bow.compute(dst, extract.detect(dst))
	x1 = np.array(f)
	
	with open('svm2.pickle', 'rb') as fr:
		new_svm = pickle.load(fr)
		print(new_svm.predict(x1))#得出结果
		
		#得出的结果分开两个文件夹
		if new_svm.predict(x1)[0]==1:
			cv2.imwrite(path_youchong+str(num)+'.jpg', dst)
		elif new_svm.predict(x1)[0]==2:
			cv2.imwrite(path_fengmi+str(num)+'.jpg', dst)
		else:
			cv2.imwrite(path_wuchong+str(num)+'.jpg', dst)
		frame = cv2.rectangle(frame,(x-r,y-r),(x+r,y+r),(0,0,255),5)
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