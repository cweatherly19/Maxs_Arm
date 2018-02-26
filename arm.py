import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, or n to stop"
while True:
    while raw_input("") == "y":
        RPL.servoWrite(motor, 2500)
        print "press n to stop"
        if raw_input("") == "a":
            RPL.servoWrite(motor, 1000)
    while raw_input("") == "a":
        RPL.servoWrite(motor, 1000)
        print "press n to stop"
        if raw_input("") == "y":
            RPL.servoWrite(motor, 2500)
    while raw_input("") == "n":
        RPL.servoWrite(motor, 0)
