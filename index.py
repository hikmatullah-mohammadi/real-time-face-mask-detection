# import required libraries/dependencies
import cv2
from PIL import Image
import numpy as np
import keras

import utils

# load our pretrained model
loaded_model = keras.models.load_model('face-mask-detection-model.h5')        

     
# get the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480) # height
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640) # width

face_detector = cv2.CascadeClassifier('./face_haarcascade/haarcascade_frontalface_default.xml')
face_img_size = (100, 100)

    
while True:
    # read image frames from the webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    # detect faces
    faces_locs = face_detector.detectMultiScale(
        img,
        minSize=face_img_size,
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    if len(faces_locs)>0:
        for face_loc in faces_locs:
            # clip the faces images
            x, y, w, h = face_loc
            face_img = img[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, face_img_size) # (100, 100) is the input shape of the model
            
            # convert color to RGB since the model has been trained on RGB images
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            img_arr = np.array([face_img]) 
            
            # do prediction with the model we constructed before
            pred = loaded_model.predict(img_arr, verbose=0)
            is_mask = 1 if pred[0]>.5 else 0
            
            # display the result
            img = utils.display_result(img, is_mask, face_loc)        
            
    # show the image
    cv2.putText(img, 'Press "q" to quit' , (0, 10), 0, .5, (0, 0, 255), 1)
    cv2.imshow('Face Detection', img)
    
    # quit when pressed 'q'
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()