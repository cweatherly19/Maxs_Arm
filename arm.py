import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, n to stop, and x to end program"
def arm_up(speed):
    speed = RPL.servoWrite(motor, 2000)
def arm_down(speed):
    speed = RPL.servoWrite(motor, 1000)
def arm_stop(speed):
    speed = RPL.servoWrite(motor, 0)
n = 1
while n == 1:
    if "y":
        arm_up
    if "a":
        arm_down
    if "n":
        arm_stop
    if "x":
        arm_stop
        n = 2
