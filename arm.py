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
command = raw_input("> ")

#allows code to break and stop completely
z = 0
#loop to run robot
while z is 0:
    #allows individual loops to break
    v = 1
    speed(RPL.servoWrite(motor1, 0))
    #turn right
    while v is 1 and command is "d":
        RPL.servoWrite(motor2, 800)
        #breaks loop
        v = 2
    if command is "d":
        command = raw_input("> ")
        continue
    #turn left
    while v is 1 and command is "a":
        RPL.servoWrite(motor2, 3000)
        #breaks loop
        if command is not "a":
            v = 2
    if command is "a":
        command = raw_input("> ")
        continue
    #go up
    while v is 1 and command is "w":
        RPL.servoWrite(motor1, 1000)
        #breaks loops
        if command is not "w":
            v = 2
    if command is "w":
        command = raw_input("> ")
        continue
    #go down
    while v is 1 and command is "s":
        RPL.servoWrite(motor1, 2000)
        if command is not "s":
            v = 2
    if command is "s":
        command = raw_input("> ")
        continue
    #stops code
    while command is not "a" or "d" or "w" or "s":
        print "program stopping"
        z = 1
        break
