
import time
import sklearn.svm as SVC
import pickle
import numpy as np
import cv2

# fea = __import__("features_3")

def app_test():
	t1 = time.time()
	with open('mx1', 'rb') as fr:
		vocabulary = pickle.load(fr)
	extract = cv2.xfeatures2d.SIFT_create()
	flann_params = dict(algorithm = 1, trees = 5)
	flann = cv2.FlannBasedMatcher(flann_params, {})
	extract_bow = cv2.BOWImgDescriptorExtractor(extract, flann)
	extract_bow.setVocabulary(vocabulary)
	im = cv2.imread("/mnt/myshare/linuxshare/wuchong1.jpg")
	f = extract_bow.compute(im, extract.detect(im))
	x1 = np.array(f)
	# print(x1)
	with open('svm1.pickle', 'rb') as fr:
		new_svm = pickle.load(fr)
		print(new_svm.predict(x1))
	t2 = time.time()
	print(t2-t1)
#if  __name__ =='__main__':
#	app_test()
 
