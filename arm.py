import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, n to stop"
true = raw_input("> ")
def arm_up( up ):
    return;
def arm_down( down ):
    return;
def arm_stop( still ):
    return;

arm_up(RPL.servoWrite(motor, 2000))
arm_down(RPL.servoWrite(motor, 1000))
arm_stop(RPL.servoWrite(motor, 0))

while True:
    if true == "y":
        arm_up()
        print "y"
    if true == "a":
        arm_down()
        print "a"
    if true == "n":
        arm_stop()
        print "n"
    if true == "x":
        arm_stop()
        print "x"
