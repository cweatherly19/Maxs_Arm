import setup
import RoboPiLib as RPL
#up and down
motor1 = 1
#left and right
motor2 = 0
#tells the commands
print "press w to go down, press s to go up,"
print "a to go left, d to go right,"
print "and any other key to end code."

#allows code to break and stop completely
z = 0
#loop to run robot
while z is 0:
    #allows code to be read
    command = raw_input("> ")
    #allows individual loops to break
    v = 1
    RPL.servoWrite(motor1, 0)
    #turn right
    while v is 1 and command is "d":
        RPL.servoWrite(motor2, 800)
        #breaks loop
        if command is not "d":
            v = 2
            continue
    #turn left
    while v is 1 and command is "a":
        RPL.servoWrite(motor2, 3000)
        #breaks loop
        if command is not "a":
            v = 2
            continue
    #go up
    while v is 1 and command is "w":
        RPL.servoWrite(motor1, 1000)
        #breaks loops
        if command is not "w":
            v = 2
            continue
    #go down
    while v is 1 and command is "s":
        RPL.servoWrite(motor1, 2000)
        if command is not "s":
            v = 2
            continue
    #stops code
    while command is not "a" or "d" or "w" or "s":
        print "program stopping"
        z = 1
        break
