from microbit import *
import radio

radio.on()
radio.config(channel=69)

state = False
pin_last = False

while True:
    pin_state = pin0.read_digital()
    if (pin_state) and (not pin_state == pin_last):
        state = not state
        radio.send(str(state))
        print(state)
    
    pin_last = pin_state