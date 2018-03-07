import setup
import RoboPiLib as RPL
import time
now = time.time()
future = now
motor = 1
print "press y to go down, press a to go up, n to stop"
run = raw_input("> ")
def arm_up( up ):
    future = time.time() + 2
    while time.time() > future:
        arm_up(RPL.servoWrite(motor, 2000))
        print "y"
        run = raw_input("> ")
    return up
def arm_down( down ):
    future = time.time() + 2
    while time.time() > future:
        arm_up(RPL.servoWrite(motor, 1000))
        print "a"
        run = raw_input("> ")
    return down
def arm_stop( still ):
    future = time.time() + 2
    while time.time() > future:
        arm_stop(RPL.servoWrite(motor, 0))
        run = raw_input("> ")
        print "n"
    return still

# arm_up()
# arm_down()
# arm_stop(RPL.servoWrite(motor, 0))

while True:
    if run == "y":
        if run == "a" or "n":
            future = time.time() + 2
            while time.time() > future:
                arm_up(RPL.servoWrite(motor, 0))
    if run == "a":
        if run == "y" or "n":
            future = time.time() + 2
            while time.time() > future:
                arm_down(RPL.servoWrite(motor, 0))
    if run == "n":
        if run == "a" or "y":
            future = time.time() + 2
            while time.time() > future:
                arm_stop(RPL.servoWrite(motor, 0))
