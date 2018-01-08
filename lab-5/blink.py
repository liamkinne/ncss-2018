# Blink
from microbit import *

state = False

while True:
    pin13.write_digital(state)  # write output
    state = not state           # invert state
    sleep(500)                  # wait