# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:58:19 2019

@author: sai prakash
"""
#pip install opencv-python

#Spacebar-to capture image
#escape- to exit the program
#captures are saved in the working directory


import cv2
import numpy as np

cam=cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter=0
while True:
    ret,frame = cam.read()
    cv2.imshow("test",frame)
    if not ret:
        break
    k=cv2.waitKey(100)
    if k%256 == 27:
        break
    elif k%256==32:
        img_name="capture{}.jpg".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("{} written!".format(img_name))
        img_counter+=1
cam.release()
cv2.destroyAllWindows()

