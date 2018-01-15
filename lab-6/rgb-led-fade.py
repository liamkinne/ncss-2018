# rgb led
# demo that drives and cycles through all of the colors on an RGB led.
from microbit import *

minimum = 0
maximum = 1023

while True:
    for i in range(minimum, maximum):
        pin0.write_analog(((maximum * 0/3) + i) % maximum)
        pin1.write_analog(((maximum * 1/3) + i) % maximum)
        pin2.write_analog(((maximum * 2/3) + i) % maximum)
        sleep(10)