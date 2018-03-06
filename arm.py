import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, n to stop"
true = raw_input("> ")
def arm_up():
    try:
        speed = RPL.servoWrite(motor, 2000)
    except:
        return ValueError("something happened that wasn't good")
def arm_down():
    try:
        speed = RPL.servoWrite(motor, 1000)
    except:
        return ValueError("something happened")
def arm_stop():
    try:
        speed = RPL.servoWrite(motor, 0)
    except:
        return ValueError("bloopy bloop")

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
