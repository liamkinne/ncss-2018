from microbit import *
import radio

# start radio
radio.on()
radio.config(channel=69)

state = False
pin_last = False

while True:
    pin_state = pin0.read_digital() # read state 
    if (pin_state) and (not pin_state == pin_last): # is on and changed (rising edge)
        state = not state
        radio.send(str(state))
        #print(state) # debug
    # remember state
    pin_last = pin_state
