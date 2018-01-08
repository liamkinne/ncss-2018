# Blink without using sleep() (non-blocking)
from microbit import *

state = False
time_last = running_time()
delay = 500 #time between state changes

while True:
    if (running_time() - time_last) >= delay:
        pin13.write_digital(state)  # write output
        state = not state           # invert state
        time_last = running_time()  # store time