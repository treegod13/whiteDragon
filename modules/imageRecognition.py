# Import necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import time
import cv2
import json

# Parse the paramethers
ap = argparse.ArgumentParser()
ap.add_argument('-c', '--conf', default = 'conf.json', help='Path to the configure file.')
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

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#cv2.imshow("image", image)
#cv2.waitKey(0)
