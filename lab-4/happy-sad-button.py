# happy/sad button
# demo of detecting rising edges from an input.
from microbit import *

state = False
pin_last = False

while True:
    pin_state = button_a.is_pressed()
    if (pin_state) and (not pin_state == pin_last):
        state = not state
        display.show(Image.HAPPY if state else Image.SAD)
    pin_last = pin_state
