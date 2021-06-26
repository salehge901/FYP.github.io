from numpy.core.numeric import True_
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import numpy as np
import argparse
import matplotlib.pyplot as plt
import cv2,os,urllib.request
import sys
import numpy as np
from django.conf import settings
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
import os
from user.model1 import FacialExpressionModel 
import cv2
facec = cv2.CascadeClassifier('opencv_haarcascade_data/haarcascade_frontalface_default.xml')
model = FacialExpressionModel("opencv_haarcascade_data/model.json", "opencv_haarcascade_data/model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
class VideoCamera(object):
    def __init__(self):
       self.video = cv2.VideoCapture(0)
    def __del__(self):
          self.video.release() 
          cv2.destroyAllWindows()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
           _, fr = self.video.read()
           gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
           faces = facec.detectMultiScale(gray_fr, 1.3, 5)

           for (x, y, w, h) in faces:
             fc = gray_fr[y:y+h, x:x+w]

             roi = cv2.resize(fc, (48, 48))
             pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

             cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)

           _, jpeg = cv2.imencode('.jpg', fr)
           return jpeg.tobytes()

            