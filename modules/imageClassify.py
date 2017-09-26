# Import necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
#import classify_image as cnn
import tensorflow as tf
import argparse
import time
import cv2
import json


# Parse the paramethers
ap = argparse.ArgumentParser()
ap.add_argument('-c', '--conf', default = '/opt/whiteDragon/conf.json', help='Path to the configure file.')
args = vars(ap.parse_args())

# Load parameters
conf = json.load(open(args['conf']))

# Initialize the camera and grab a reference
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# Load class labels
rows = open(conf['Label_path'])

# warmup camera
time.sleep(conf['camera_warmup_time'])

# Capture the image and change into blob
camera.capture(rawCapture, format="bgr")
image_array = rawCapture.array
image = cv2.dnn.blobFromImage(image_array, 1, (224, 224), (104, 117, 123))

#cnn.run_inference_on_image(image)

# Load model
network = cv2.dnn.




#cv2.imshow("image", image)
#cv2.waitKey(0)