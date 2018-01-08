from microbit import *

state = False
pin_last = False

while True:
    pin_state = pin0.read_digital()                         # read pin
    if (pin_state) and (not pin_state == pin_last):         # high and changing state (rising edge)
        state = not state                                   # invert state
        display.show(Image.HAPPY if state else Image.SAD)   # show image
    # remember state
    pin_last = pin_state
