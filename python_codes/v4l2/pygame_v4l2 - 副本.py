# -*- coding: utf-8 -*- 
  
  
from VideoCapture import Device 
import time 
import pygame 
from pygame.locals import *
import sys
  
  
pygame.init() 
  
size = width, height = 620, 485
print size
speed = [2, 2] 
black = 0, 0, 0
if pygame.display.get_init():
 print ("inited")
else:
 print"notinit"
pygame.display.set_caption('1111') 
screen = pygame.display.set_mode((600,500))
  
  
SLEEP_TIME_LONG = 0.0
  
  
cam = Device(devnum=0, showVideoWindow=0) 
print cam  
filename = "test.jpg"
while True: 
 for event in pygame.event.get():
   if event.type== QUIT:
    sys.exit()
   elif event.type== KEYDOWN:
    key = pygame.key.get_pressed()
    if key[97]:
     filename = "test" + int(time.time()//1).__str__()+".jpg"
     print filename
     cam.saveSnapshot(filename, timestamp=3, boldfont=1, quality=55) 
   elif event.type== MOUSEBUTTONDOWN:
    pass
   elif event.type== MOUSEMOTION:
    pass
   elif event.type== MOUSEBUTTONUP:
    pass
   
  
  
  #cam.getImage(0, 0, "bl")
  
 cmd="shut"
 Image = pygame.image.load(filename)
 #screen.fill(0,0,200)
 screen.blit(Image, (0,0))
 pygame.display.update()
  
   
  
  
 time.sleep(SLEEP_TIME_LONG) 