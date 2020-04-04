#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mtcnn.mtcnn
import numpy as np
from PIL import Image
import mysql.connector
from pathlib import Path
import matplotlib.pyplot as plt 
from keras.models import load_model


# In[4]:


#define mtcnn detector
detector=mtcnn.MTCNN()
#load pre-trained keras model
model=load_model("facenet_keras.h5")


# In[5]:


def preprocess(face_img):
    #preprocess input image
    
    #model expects input image of size 160*160
    #convert numpy array to image type
    face_img=Image.fromarray(face_img)
    #resize image
    face_img=face_img.resize((160, 160))
    #revert to numpy array
    face_img=np.asarray(face_img)
    print(face_img.shape)
    #standardize the pixels of sample
    mean,std=face_img.mean(),face_img.std()
    print(mean,std)
    face_img=(face_img-mean)/std
    #add fourth dimension to numpy array(number of images)
    sample=np.expand_dims(face_img,axis=0)
    print(sample.shape)
    return sample


# In[ ]:


def face_embedding():
   #capture video from camera
   cap=cv2.VideoCapture(0)
   while (cap.isOpened()):
       #capture frame by frame
       ret,frame=cap.read()
       cv2.imshow("video",frame)
       #detect the face using detector
       face=detector.detect_faces(frame)
       if len(face)==1 :
           x1,y1,width,height=face[0]["box"]
           x1,y1=abs(x1),abs(y1)
           #calculate (x2,y2) coordinate
           x2,y2=x1+width,y1+height
           face_img=frame[y1:y2,x1:x2]
           sample=preprocess(face_img)
           #get embedding vector
           pred=model.predict(sample)
           emb_vec=np.around(pred[0],decimals=5) 
           #wrap numpy array into string format
           string=','.join(str(x) for x in emb_vec)
           cap.release()
           cv2.destroyAllWindows()        
           return string
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
   cap.release()
   cv2.destroyAllWindows()        

