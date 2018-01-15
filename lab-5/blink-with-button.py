# blink from button
# led on pin 13, button on pin 14
from microbit import *

# set as input
pin14.read_digital()
pin14.set_pull(pin5.PULL_DOWN)

while True:
    pin13.write_digital(pin14.read_digital())