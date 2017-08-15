from lib601 import sm

class SM(object):
    def start(self):
        self.state = self.startState
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    def run(self, n = 20):
        return self.transduce([None]*n)
    def splitValue(v):
        if v == 'undefined':
            return ('undefined', 'undefined')
        else:
            return v
    def safeAdd(m, n):
        if m == 'undefined' or n == 'undefined':
            return 'undefined'
        else:
            return m + n
    def safeMul(m ,n):
        if m == 'undefined' or n == 'undefined':
            return 'undefined'
        else:
            return m * n

## accumulator
class Accumulator(SM):
    startState = 0
    def getNextValues(self, state, inp):
        state = state + inp
        return (state, state)

## language acceptor
class ABC(SM):
    startState = 0
    def getNextValues(self, state, inp):
        if state == 0 and inp == 'a':
            return (1, 'True')
        elif state == 1 and inp == 'b':
            return (2, 'True')
        elif state == 2 and inp == 'c':
            return (0, 'True')
        else:
            return (3, 'False')

## count up and down
class Counter(SM):
    startState = 0
    def getNextValues(self, state, inp):
        if inp == 'u':
            return (state+1, state+1)
        elif inp == 'd':
            return (state-1, state-1)
        else:
            return (state, state)

## delay
class Delay(SM):
    def __init__(self, s):
        self.startState = s
    def getNextValues(self, state, inp):
        return (inp, state)

## average2
class Average2(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (inp, (inp + state)/2.0)

## Sum of last three inputs
class SumLast3(sm.SM):
    startState = [0, 0]
    def getNextValues(self, state, inp):
        [prepre_inp, pre_inp] = state
        return ([pre_inp, inp], prepre_inp+pre_inp+inp)

## Cascade
class Cascade(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
    def getNextValues(self, state, inp):
        (s1, s2) = state
        #print s1, s2
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, o1)
        return ((newS1, newS2), o2)

## Parrallel
class Parrallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))

## Parrallel2
class Parrallel2(Parrallel):
    def getNextValues(self, state, inp):
        (inp1, inp2) = inp
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp1)
        (newS2, o2) = self.m2.getNextValues(s2, inp2)
        return ((newS1, newS2), (o1, o2))

## ParrallelAdd
class ParrallelAdd(Parrallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), o1 + o2)

## Feedback
class Feedback(SM):
    def __init__(self, sm):
        self.m = sm
        self.startState = self.m.startState
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        (newS1, ignore) = self.m.getNextValues(state, o)
        return (newS1, o)

## Increment
class Increment(SM):
    startState = 0
    def __init__(self, inc):
        #self.startState = 0
        self.inc = inc
    def getNextValues(self, state, inp):
        #s = inp + self.step
        if inp == 'undefined':
            return (0, 'undefined')
        else:
            return (0, inp + self.inc)

def makeCounter(init, step):
    return Feedback(Cascade(Increment(step), Delay(init)))

def fib():
    return Feedback(ParrallelAdd(Delay(1), Cascade(Delay(1), Delay(0))))

def fib2(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

#k = -1.5
#dDesired = 1.0
#class WallController(SM):
#    def getNextState(self, state, inp):
#        return k * (dDesired - inp)











