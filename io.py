## The modules of IO of WhiteDragon, It contains the Controller() and Senser()
#  chenmz
#  2017.7.17

import RPi.GPIO as GPIO
import time

## The controller of WhiteDragon

class Controller(object):
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

    # unit: m
    def move_forward(self, d):
        GPIO.output(self.forward_pin, True)
        t = d / 0.6
        time.sleep(t)
        GPIO.output(self.forward_pin, False)

    def move_backward(self, d):
        GPIO.output(self.backward_pin, True)
        t = d / 0.6
        time.sleep(t)
        GPIO.output(self.backward_pin, False)

    # unit: pi
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

    def turn(self, angle):
        if angle > 0:
            self.turn_right(angle)
        else:
            self.turn_left(angle)

    def move(self, distance):
        if distance > 0:
            self.move_forward(distance)
        else:
            self.move_backward(distance)

    def clear(self):
        GPIO.cleanup()

    def action(self, angle, distance):
        #self.setup()
        self.turn(angle)
        self.stop()
        self.move(distance)
        self.stop()

## The senser of WhiteDragon

class Sonar(object):
    def __init__(self, TRIG, ECHO):
        self.TRIG = TRIG
        self.ECHO = ECHO
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

        distance = (stop - start) * 34000 / 2
        return distance

    def clear(self):
        GPIO.cleanup()

class Radar(object):
    def __init__(self, ECHO):
        self.ECHO = ECHO

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ECHO, GPIO.IN)

    def measureF(self):
        state = GPIO.input(self.ECHO)
        return state

class Senser(object):
    sonar = Sonar(20, 21)
    radarLeft = Radar(16)
    radarRight = Radar(12)

    def setup(self):
        self.sonar.setup()
        self.radarLeft.setup()
        self.radarRight.setup()

    def clear(self):
        GPIO.cleanup()

    def sensorInput(self):
        #self.setup()
        distance = self.sonar.measureU()
        barrierLeft = self.radarLeft.measureF()
        barrierRight = self.radarRight.measureF()
        #self.clear()
        return (distance, barrierLeft, barrierRight)



