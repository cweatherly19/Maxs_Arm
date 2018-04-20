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
    #turn right
    while command is "d":
        RPL.servoWrite(motor2, 800)
        #breaks loop
        command = raw_input("> ")
        continue
    #turn left
    while command is "a":
        RPL.servoWrite(motor2, 3000)
        #breaks loop
        command = raw_input("> ")
        continue
    #go up
    while command is "w":
        RPL.servoWrite(motor1, 1000)
        #breaks loop
        command = raw_input("> ")
        continue
    #go down
    while command is "s":
        RPL.servoWrite(motor1, 2000)
        #break loop
        command = raw_input("> ")
        continue
    #stops code
    while command is not "a" or "d" or "w" or "s":
        print "program stopping"
        z = 1
        break
