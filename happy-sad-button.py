from microbit import *

state = False

pin_last = False

faces = {
    True : Image.HAPPY,
    False: Image.SAD,
}

while True:
    pin_state = pin0.read_digital()
    if (pin_state) and (not pin_state == pin_last):
        state = not state
        display.show(faces[state])
    
    pin_last = pin_state