# joystick print
from microbit import *

# turn off display so I can use pin 3
display.off()

pin_x = pin3
pin_y = pin4
pressed = False
press_thresh = 1000

# set as analog inputs
pin_x.read_analog()
pin_y.read_analog()

while True:
    x_in = pin_x.read_analog() / 1024.0 - 1.0
    y_in = pin_y.read_analog() / 1024.0 - 1.0
    pressed = (x_in >= press_thresh) and (y_in >= press_thresh)

    print("X{}, Y{}, Pressed{}".format(str(x_in)[:4], str(y_in)[:4], str(pressed)))