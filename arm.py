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
#reads the turn in the loop below
def run( turn ):
    return turn
#reads the up and down in the loops
def speed( go ):
    return go
#allows code to break and stop completely
z = 0
#loop to run robot
while z is 0:
    #allows individual loops to break
    v = 1
    #turn right
    while v is 1 and raw_input("> ") is "d":
        run(RPL.servoWrite(motor2, 800))
        #breaks loop
        if raw_input("> ") is not "d":
            v = 2
    #return to top of loop if "d"
    if raw_input("> ") is "a" or "s" or "w":
        continue
    #turn left
    while v is 1 and raw_input("> ") is "a":
        run(RPL.servoWrite(motor2, 3000))
        #breaks loop
        if raw_input("> ") is not "a":
            v = 2
    #return to top of loof if "a"
    if raw_input("> ") is "d" or "s" or "w":
        continue
    #go up
    while v is 1 and raw_input("> ") is "w":
        speed(RPL.servoWrite(motor1, 1000))
        #breaks loops
        if raw_input("> ") is not "w":
            v = 2
    #return to top of loop if "w"
    if raw_input("> ") is "a" or "s" or "d":
        continue
    #go down
    while v is 1 and command is "s":
        speed(RPL.servoWrite(motor1, 2000))
        if raw_input("> ") is not "s":
            v = 2
    #return to top of loop if "s"
    if raw_input("> ") is "a" or "w" or "d":
        continue
    #stops code
    while command is not "a" or "d" or "w" or "s":
        print "program stopping"
        speed(RPL.servoWrite(motor1,0))
        z = 1
        break
