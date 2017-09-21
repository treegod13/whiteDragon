##  The brain of WhiteDragon
# chenmz 2017.9.1

from modules import stateMachine as sm
from modules import ioContrller as io
import math
import json

# Import the configure infomation
conf = json.load(open('conf.json'))

# Move forward for 0.01 meter
# state: (position_x(unit: m), position_y(unit: m), angle_theta(unit: pi))
class ForwardSM(sm.SM):
    def __init__(self, s):
        self.startState = s
    def getNextValues(self, state, inp):
        print inp
        (last_x, last_y, last_theta) = state
        new_x = last_x + math.cos(last_theta)
        new_y = last_y + math.sin(last_theta)
        new_state = (new_x, new_y, last_theta)
        print new_state
        return (new_state, white.controller.action(0, 0.01)) # angle:0 distance:1

# Rotate
class RotateSM(sm.SM):
    length = conf['Robot_length']
    width = conf['Robot_width']
    def __init__(self, s, direction):
        self.startState = s
        self.direct = 
    def getNextValues(self, state, inp):
#        (last_x, last_y, last_theta) = state
#        (inp )
#        new_x = 
#        new_theta = 

# Stop
class StopSM(sm.SM):
    startState = (0, 0, 0)
    def getNextValues(self, state, inp):
        return (state, white.controller.stop())

# Destination finder
class DestFinder(sm.SM):
    def __init__(self, currPosition, destPosition):
        self.startState = currPosition
        self.endState = destPosition
    def getNextValues(self, state, inp):
        pass


# Wall finder
# SenserInput:(distance(unit: mm), barrierLeft(value:0, 1), barrierLeft(value:0, 1))
class WallFinder(sm.SM):
    startState = 0
    def __init__(self, dDesired):
        self.dD = dDesired
    def getNextValues(self, state, inp):
        print state, inp
        dN = inp[0]/100
        dM = dN - self.dD
        if dM < 0.01:
            return (state, white.controller.action(0, 0))
        elif dM < 1:
            return (state + dM/100, white.controller.action(0, dM/100))
        else:
            return (state + dM/10, white.controller.action(0, dM/10))

# WhiteBrain
class Brain(object):
    def __init__(self):
        self.behavior = StopSM()
        self.controller = io.Controller()
        self.senser = io.Senser()
    def setup(self):
        self.senser.setup()
        self.controller.setup()
        self.behavior.start()
    def step(self):
        self.behavior.step(self.senser.sensorInput())
    def run(self):
        i = 0
        while(1):
            i = i + 1
            self.step()
    def stop(self):
        self.controller.stop()

# Create instance of WhiteDragon
white = Brain()
white.behavior = WallFinder(0.1)
white.setup()
#white.step()
#white.run()


















