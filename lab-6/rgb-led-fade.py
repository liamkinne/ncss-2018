# rgb led
from microbit import *

def led_set(r, g, b):
    pin13.write_analog(r)
    pin14.write_analog(g)
    pin15.write_analog(b)
    

while True:
    for i in range(0, 1023):
        led_set(i % 1023, (300 + i) % 1024, (600 + i) % 1024)