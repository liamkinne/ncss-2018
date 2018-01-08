# voltage reader
from microbit import *

display.off()
pin3.read_analog()

while True:
    voltage = pin3.read_analog();
    voltage /= 1024
    voltage *= 3.3
    print(str(voltage) + "V")