from microbit import *
import radio

radio.on()

my_channel = 69
radio.config(channel=69)

last_msg_time = running_time()
TIMEOUT = 500

while True:
    time = running_time()
    if time - last_msg_time >= TIMEOUT:
        display.show(Image.SAD)
        sleep(1000)

    if radio.receive():
        last_msg_time = time