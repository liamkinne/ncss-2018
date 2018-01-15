# blink with speed control
# 
from microbit import *

state = False
time_last = running_time()
delay = 500 #time between state changes

while True:
    if button_a.was_pressed():
        delay -= 20
    elif button_b.was_pressed():
        delay += 20
        
    if (running_time() - time_last) >= delay:
    	state = not state
        pin13.write_digital(state)
        time_last = running_time()