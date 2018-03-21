import time
import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, and any other key to end code"
command = raw_input("> ")
def speed( go ):
    return go
x = 0
while x is 0:
    y = 1
    while y is 1 and command is "a":
        now = time.time()
        future = 1 + now
        while y is 1 and now < future:
            speed(RPL.servoWrite(motor,1000))
            while y is 1 and time.time() >= future:
                speed(RPL.servoWrite(motor,0))
                print "insert new input"
                y = 2
    if command is "a":
        command = raw_input("> ")
        continue
    while y is 1 and command is "y":
        now = time.time()
        future = 1 + now
        while y is 1 and now < future:
            speed(RPL.servoWrite(motor,2000))
            while y is 1 and time.time() >= future:
                speed(RPL.servoWrite(motor,0))
                print "insert new input"
                y = 2
    if command is "y":
        command = raw_input("> ")
        continue
    while command is not "y" or "a":
        print "program stopping"
        speed(RPL.servoWrite(motor,0))
        x = 1
        break
