import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, n to stop, and x to end program"
true = raw_input("")
def arm_up(speed):
    speed = RPL.servoWrite(motor, 2000)
    return
def arm_down(speed):
    speed = RPL.servoWrite(motor, 1000)
    return
def arm_stop(speed):
    speed = RPL.servoWrite(motor, 0)
    return
n = 1
while n == 1:
    if true == "y":
        arm_up
    if true == "a":
        arm_down
    if true == "n":
        arm_stop
    if true == "x":
        arm_stop
        n = 2
