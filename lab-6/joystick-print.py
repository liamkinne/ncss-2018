# joystick print
from microbit import *

# turn off display
display.off()
# better naming
pin_x = pin3
pin_y = pin4

# set as inputs
pin_x.read_analog()
pin_y.read_analog()

while True:
    x_in = pin_x.read_analog() / 1024.0
    y_in = pin_y.read_analog() / 1024.0
    x_in -= 0.5
    y_in -= 0.5
    
    print("X" + str(x_in)[] + ", Y" + str(y_in))