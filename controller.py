import RPi.GPIO as GPIO
import time

class controller(object):
    forward_pin = [18, 24]
    backward_pin = [23, 25]
    left_pin = 18
    right_pin = 24

    def __init__(self):
        pass

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.forward_pin, GPIO.OUT)
        GPIO.setup(self.backward_pin, GPIO.OUT)

    def move_forward(self, d):
        GPIO.output(self.forward_pin, True)
        t = d/0.6
        time.sleep(t)
        GPIO.output(self.forward_pin, False)

    def move_backward(self, d):
        GPIO.output(self.backward_pin, True)
        t = d/0.6
        time.sleep(t)
        GPIO.output(self.backward_pin, False)

    def turn_left(self, a):
        GPIO.output(self.left_pin, True)
        t = a / 0.81
        time.sleep(t)
        GPIO.output(self.left_pin, False)

    def turn_right(self, a):
        GPIO.output(self.right_pin, True)
        t = a / 0.81
        time.sleep(t)
        GPIO.output(self.right_pin, False)

    def stop(self):
        GPIO.output(self.forward_pin + self.backward_pin, False)

    def clear(self):
        GPIO.cleanup()


