# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 18:06:03 2023

@author: HP
"""

# import required libraries
import cv2
import pandas as pd
import os

cur="dataset path"
val="destinatiion path"
dir1=os.listdir(cur)

for path in dir1:
    os.mkdir(val+path)
    for image in os.listdir(cur+path):
       
    # Read the input image
        img = cv2.imread(cur+path+"/"+image)
    # read the input image
        
        
        # convert to grayscale of each frames
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # read the haarcascade to detect the faces in an image
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        # detects faces in the input image
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
       
        
        # loop over all detected faces
        if len(faces) > 0:
           for i, (x, y, w, h) in enumerate(faces):
         
              # To draw a rectangle in a face
              cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
              face = img[y:y + h, x:x + w]
              #cv2.imshow("Cropped Face", face)
              cv2.imwrite(val+path+"/"+str(i)+image, face)
              print(f"face{i}.jpg is saved")

        # display the image with detected faces
        #cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
