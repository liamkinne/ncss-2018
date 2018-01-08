from microbit import *
import radio

radio.on()
channel = 69
radio.config(channel=69)

MY_ID = 3 # 0->3 for each microbit
MICRO_COUNT = 4
number = 0

while True:
    # get message
    msg = radio.receive()
    if msg:
        number = int(msg)
        
    if (number + MY_ID) % MICRO_COUNT == 0: # has parcel
        display.show(Image.SNAKE)
        if button_a.was_pressed(): # incriment number
            number += 1
            radio.send(str(number))
        
        if button_b.was_pressed(): # decrement number
            number -= 1
            radio.send(str(number))
    else:
        display.clear()