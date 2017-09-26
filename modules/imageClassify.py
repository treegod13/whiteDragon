# Import necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
#import classify_image as cnn
import tensorflow as tf
import numpy as np
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
rows = open(conf['Caffe_label']).read().split('\n') # open():retrun file handle. read():return strings of file. split():return list of strings
classes = [r[r.find(' ')+1:] for r in rows]

# warmup camera
print 'Warming the camera...'
time.sleep(conf['camera_warmup_time'])

# Capture the image and change into blob
camera.capture(rawCapture, format="bgr")
image_array = rawCapture.array
blob = cv2.dnn.blobFromImage(image_array, 1, (224, 224), (104, 117, 123))
#cnn.run_inference_on_image(image)

# Load model
print 'Loading model...'
network = cv2.dnn.readNetFromCaffe(conf['Caffe_prototxt'], conf['Caffe_model'])

# Predict the label
print 'Predicting label...'
network.setInput(blob)
start = time.time()
scores = network.forward()
end =time.time()
print 'Use time:' + str(end-start) + ' seconds.'
indexs = np.argsort(scores[0])[::-1][:5]  # [::-1]:reverse the array

# Show the results
print 'The results are:'
for (i, index) in enumerate(indexs):
    if i == 0:
        cv2.putText(image_array, 'Object is: {}'.format(classes[index]), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    print 'No.{}: {} . Scores: {}'.format(i+1, classes[index], scores[0][index])

cv2.imshow("image", image_array)
cv2.waitKey(0)
