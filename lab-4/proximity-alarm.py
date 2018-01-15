from microbit import *
import radio

radio.on()
radio.config(channel=69)

last_msg_time = running_time()

while True:
    if running_time() - last_msg_time >= 500:
        display.show(Image.SAD)
        sleep(1000)

    if radio.receive():
        last_msg_time = running_time()