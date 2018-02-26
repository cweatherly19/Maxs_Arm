import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, or n to stop"
n = 1
true = raw_input("")
while n == 1:
    while true == "y":
        RPL.servoWrite(motor, 2500)
        print "press n to stop"
        true1 = raw_input("")
        if true1 == "a":
            break
    while true == "a":
        RPL.servoWrite(motor, 1000)
        print "press n to stop"
        true2 = raw_input("")
        if true2 == "a":
            break
    while true == "n":
        RPL.servoWrite(motor, 0)
        n = 2
