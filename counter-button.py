from microbit import *

pin_last = False

counter = 0

while True:
    pin_state = pin0.read_digital() # Get state
    if pin_state and not pin_last:
        counter += 1 # incriment
        print(counter)
    
    pin_last = pin_state