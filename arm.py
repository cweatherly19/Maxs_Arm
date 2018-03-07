import setup
import RoboPiLib as RPL
import time
now = time.time()
future = now
motor = 1
print "press y to go down, press a to go up, n to stop"
run = raw_input("> ")
def arm_up( up ):
    if run == "a" or "n":
        arm_up(RPL.servoWrite(motor, 0))
    return up
def arm_down( down ):
    if run == "y" or "n":
        arm_up(RPL.servoWrite(motor, 0))
    return down
def arm_stop( still ):
    if run == "y" or "a":
        arm_up(RPL.servoWrite(motor, 0))
    return still

# arm_up()
# arm_down()
# arm_stop(RPL.servoWrite(motor, 0))

while True:
    if run == "y":
        future = time.time() + 2
        while time.time() > future:
            arm_up(RPL.servoWrite(motor, 2000))
            print "y"
            run = raw_input("> ")
            return run
    if run == "a":
        future = time.time() + 2
        while time.time() > future:
            arm_down(RPL.servoWrite(motor, 1000))
            run = raw_input("> ")
            print "a"
    if run == "n":
        future = time.time() + 2
        while time.time() > future:
            arm_stop(RPL.servoWrite(motor, 0))
            run = raw_input("> ")
            print "n"
