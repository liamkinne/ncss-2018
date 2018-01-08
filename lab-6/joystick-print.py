# joystick print
from microbit import *

# turn off display
display.off()

# better naming
pin_x = pin3
pin_y = pin4

# value storage
values = [0, 0]

# set as inputs
pin_x.read_analog()
pin_y.read_analog()

while True:
    x_in = pin_x.read_analog() / 1024.0
    y_in = pin_y.read_analog() / 1024.0
    [(x/1024.0)-1.0 for x in values]
    
    print("X" + str(x_in)[:4] + ", Y" + str(y_in)[:4])