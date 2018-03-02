import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, n to stop"
true = raw_input("> ")
def arm_up():
    speed = RPL.servoWrite(motor, 2000)
    return speed
def arm_down():
    speed = RPL.servoWrite(motor, 1000)
    return speed
def arm_stop():
    speed = RPL.servoWrite(motor, 0)
    return speed

while True:
    if true == "y":
        arm_up
        print "y"
    if true == "a":
        arm_down
        print "a"
    if true == "n":
        arm_stop
        print "n"
    if true == "x":
        arm_stop
        print "x"
