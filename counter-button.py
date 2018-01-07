# Incriment a number when a button is pressed
# then print it.

from microbit import *

pin_last = False
counter = 0

while True:
    pin_state = pin0.read_digital() # Get state
    if pin_state and not pin_last:  # check for pin change
        counter += 1                # incriment
        print(counter)              # print
    pin_last = pin_state            # remember last state
