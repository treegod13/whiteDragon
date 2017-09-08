# Import necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import json

# 
ap = 1


# Initialize the camera and grab a reference
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# warmup camera
time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#cv2.imshow("image", image)
#cv2.waitKey(0)
