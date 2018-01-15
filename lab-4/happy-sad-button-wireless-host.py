# happy/sad wireless sender
# sends 0 for sad and 1 for happy
from microbit import *
import radio

radio.on()
radio.config(channel=69)

state = False
button_state = False
button_last = False

while True:
    button_state = button_a.is_pressed()
    if (button_state) and (not button_state == pin_last):
        state = not state
        radio.send(str(state))
    button_last = button_state
