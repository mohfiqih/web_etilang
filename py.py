import cv2
import time
import numpy as np
import os
from keras.models import load_model

# Load the model
model = load_model('keras_model.h5')

# CAMERA can be 0 or 1 based on default camera of your computer.
camera = cv2.VideoCapture('video/video-1_1.mp4')

# Grab the labels from the labels.txt file. This will be used later.
labels = open('labels.txt', 'r').readlines()

while True:
    # Grab the webcameras image.
    ret, image = camera.read()
    flip1 = cv2.flip(image,1)
    gray = cv2.cvtColor(flip1,cv2.COLOR_BGR2GRAY)
    helm = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # Resize the raw image into (224-height,224-width) pixels.
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1
    text = labels[np.argmax(model.predict(image))]
    # Menampilkan label prediksi di dalam frame
    img  = cv2.putText(flip1, text, (10,450), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
        
    if cv2.waitKey(1) == 27:
        break
            
    cv2.imshow('Webcam Image', flip1)
    
 
camera.release()
cv2.destroyAllWindows()