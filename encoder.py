from microbit import *

pin_last_a = False
pin_last_b = False

counter = 0

pin0.read_digital()
pin0.set_pull(pin0.PULL_UP)
pin13.read_digital()
pin13.set_pull(pin13.PULL_UP)

while True:
    pin_state_a = pin0.read_digital() # Get state
    pin_state_b = pin13.read_digital() # Get state
    
    if pin_state_b and pin_state_b != pin_last_b:
        if (not pin_state_a and pin_state_b):
            counter += 1
            print("up")
    
    if pin_state_a and pin_state_a != pin_last_a:
        if (not pin_state_b and pin_state_a):
            counter -= 1
            print("down")
    
    
    #Old
    #if pin_state_a and not pin_last_b:
    #    counter += 1 # incriment
    #    print(counter)
    
    pin_last_a = pin_state_a
    pin_last_b = pin_state_b