import sm
import io
import math

# Move forward for 1 meter
class ForwardTSM(sm.SM):
    startState = (0, 0, 0)
    def getNextValues(self, state, inp):
        print inp
        (last_x, last_y, last_theta) = state
        new_x = last_x + math.cos(last_theta)
        new_y = last_y + math.sin(last_theta)
        new_state = (new_x, new_y, last_theta)
        print new_state
        return (new_state, controller.action(0, 1)) # angle:0 distance:1

# Rotate
class RotateTSM(sm.SM)

# Create instance of White
class brain():
    def __init__(self):
        self.behavior = ForwardTSM()
        self.controller = io.Controller()
        self.senser = io.Senser()

    def setup(self):
        self.senser.setup()
        self.controller.setup()
        self.behavior.start()

# Create instance of WhiteDragon
behavior = ForwardTSM()
senser = io.Senser()
controller = io.Controller()

def setup():
    senser.setup()
    controller.setup()
    behavior.start()

def step():
    behavior.step(senser.sensorInput())




















