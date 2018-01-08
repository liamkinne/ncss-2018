from microbit import *

class Motor:
    def __init__(self, pin_a, pin_b):
        self.pin_a = pin_a
        self.pin_b = pin_b
    
    def set(value):
        speed = abs(value) * 1023
        pin_a.write_analog(speed * int(value > 0))
        pin_b.write_analog(speed * int(value < 0))
        
    def stop():
        self.set(0)

class Robot:
    def __init__(self, motor_left, motor_right):
        self.motor_left = motor_left
        self.motor_right = motor_right

    def drive_tank(left, right):
        motor_left.set(left)
        motor_right.set(right)