import pygame.camera
import time
import pygame
import cv2
import numpy as np 
path = "/mnt/myshare/linuxshare/live_"
num = 0
def surface_to_string(surface):    
	"""convert pygame surface into string"""    
	return pygame.image.tostring(surface, 'RGB') 
def pygame_to_cvimage(surface):    
	"""conver pygame surface into  cvimage"""     
	#cv_image = np.zeros(surface.get_size, np.uint8, 3)    
	image_string = surface_to_string(surface)    
	image_np = np.fromstring(image_string, np.uint8).reshape( 1080, 1920, 3)    
	frame = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)    
	return image_np, frame  
pygame.camera.init()#pygame的camera模块的初始化
pygame.camera.list_cameras()#显示当前可用的camera列表
cam = pygame.camera.Camera("/dev/video0", [ 1920, 1080], MJPG) #打开camera

cam.start()#开始捕捉画面
print ('start')
time.sleep(0.1)
while True:    
	for i in range(3):
		image = cam.get_image()     #获取图片
	cv_image, frame = pygame_to_cvimage(image)      
	cv2.imwrite(path+str(num)+'.jpg',frame)
	num+=1	
	if num>20:        
		break 
	print ("pic",num)
	print ("write ok")  
	time.sleep(2)
cam.stop()
#https://blog.csdn.net/guofangxiandaihua/article/details/78066323

