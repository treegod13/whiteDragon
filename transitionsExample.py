from transitions import Machine

# define a class
class Matter(object):
    ref say_hello(self): print 'hello new state.'
    def say_goodbye(self): print 'goodbye old state'

lump = Matter()

#machine = Machine(model=lump, states=['solid', 'liquid', 'gas', 'plasma'], initial='solid')

# add states, on_exit is the output
#states=['solid', 'liquid', 'gas', 'plasma']
states = [
        State(name='solid', on_exit=['say_goodbye']),
        'liquid',
        {'name':'gas'},
        'plasma'
        ]

# add new methods
#transitions = [
#        {'trigger': 'melt', 'source':'solid', 'dest':'liquid'},
#        {'trigger': 'evaporate', 'source':'liquid', 'dest':'gas'},
#        {'trigger': 'sublimate', 'source':'solid', 'dest':'gas'},
#        {'trigger': 'ionize', 'source':'gas', 'dest':'plasma'},
#        ]
#machine = Machine(lump, states=states, transitions=transitions, initial='liquid') 
machine = Machine(lump, states = states)
machine.add_transition('')

# add inputs and outputs, also called callbacks





lump.state









