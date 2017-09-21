# Import necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# Initialize the camera and grab a reference
camera = PiCamera()
imageData= PiRGBArray(camera)

# warmup camera
time.sleep(0.1)

camera.capture(imageData, format="bgr")
image = imageData.array

gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # change into gray
gray2 = cv2.GaussianBlur(gray1, (21, 21), 0) # smooth the image

ret, thres1 = cv2.threshold(gray2, 27, 255, cv2.THRESH_TOZERO)

thres2 = cv2.dilate(thres1, None, iterations=2)

cont1, contours, hierarchy = cv2.findContours(gray1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("image1", image)
cv2.waitKey(0)
cv2.imshow("image1", gray1)
cv2.waitKey(0)
cv2.imshow("image1", gray2)
cv2.waitKey(0)
cv2.imshow("image1", thres1)
cv2.waitKey(0)
cv2.imshow("image1", thres2)
cv2.waitKey(0)
cv2.imshow("image1", cont1)
cv2.waitKey(0)
