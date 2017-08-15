import controller
import senser
import time

#controller.move_forward(1)
#time.sleep(0.5)
#controller.move_backward(1)

#controller.move_backward(0.5)
#controller.turn_left(0.5)
#time.sleep(0.5)
#controller.turn_right(0.5)

#d = senser.measureU()
#print d

#a = controller.controller()
#a.setup()
#a.move_forward(1)
#a.clear()

b = senser.Senser()
b.setup()
d = b.measureU()
print d
b.clear()

