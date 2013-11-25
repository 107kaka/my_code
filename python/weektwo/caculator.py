# Startint point for calculator

import simplegui

# initalize globals
store  = 0
operand = 0

# define functions that manipulate store and operand
def output():
    ""prints contents of store and operand""
    print "Store = ", store
    print "Operand = ", operand
    print ""

def swap():
    "" swap contents of store and operand""
    global store, operand
    store, operand = operand, store
    output()

def add():
    "" add operand to store""
    global store
    store += operand
    output()

def sub():
    global store
    store -= operand
    output()

def mult():
    "" multiply store by operand""
    global store
    store *= operand
    output()
    
def div():
    global store
    store /= operand
    output()
    
def enter(inp):
    global operand
    operand = float(inp)
    output()
    
# create frame
frame = simplegui.create_frame("Caculator", 300, 300)

frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub",sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter operand", enter, 100)


# get frame rolling
frame.start()"
