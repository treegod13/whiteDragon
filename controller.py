import RPi.GPIO as GPIO
import time

forward_pin = [18, 24]
backward_pin = [23, 25]
left_pin = 18
right_pin = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.OUT)

def move_forward(d):
    GPIO.output(forward_pin, True)
    t = d/0.6
    time.sleep(t)
    GPIO.output(forward_pin, False)

def move_backward(d):
    GPIO.output(backward_pin, True)
    t = d/0.6
    time.sleep(t)
    GPIO.output(backward_pin, False)

def turn_left(a):
    GPIO.output(left_pin, True)
    t = a / 0.81
    time.sleep(t)
    GPIO.output(left_pin, False)

def turn_right(a):
    GPIO.output(right_pin, True)
    t = a / 0.81
    time.sleep(t)
    GPIO.output(right_pin, False)

def stop():
    GPIO.output(forward_pin + backward_pin, False)
