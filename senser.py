import RPi.GPIO as GPIO
import time


class Senser(object):
    TRIG = 20
    ECHO = 21

    def __init__(self):
        pass

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def measureU(self):
        GPIO.output(self.TRIG, 0)
        time.sleep(0.01)

        GPIO.output(self.TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, 0)
        start = time.time()

        while GPIO.input(self.ECHO) == 0:
            start = time.time()

        while GPIO.input(self.ECHO) == 1:
            stop = time.time()

        distance = (stop - start) * 34000 / 2 #
        return distance

    def clear(self):
        GPIO.cleanup()
