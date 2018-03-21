import time
import setup
import RoboPiLib as RPL
motor1 = 1
motor2 = 0
print "press s to go down, press w to go up,"
print "a to turn left, d to turn right,"
print "and any other key to end code."
command = raw_input("> ")
def speed( turn ):
    print turn
    return turn
def run( go ):
    print go
    return go
x = 0
z = 0
while x is 0:
    y = 1
    while y is 1 and command is "w":
        now = time.time()
        future = 1 + now
        while y is 1 and now < future:
            speed(RPL.servoWrite(motor1,1000))
            while y is 1 and time.time() >= future:
                speed(RPL.servoWrite(motor1,0))
                print "insert new input"
                y = 2
    if command is "w":
        command = raw_input("> ")
        continue
    while y is 1 and command is "s":
        now = time.time()
        future = 1 + now
        while y is 1 and now < future:
            speed(RPL.servoWrite(motor1,2000))
            while y is 1 and time.time() >= future:
                speed(RPL.servoWrite(motor1,0))
                print "insert new input"
                y = 2
    if command is "s":
        command = raw_input("> ")
        continue
    while command is not "w" or "s" or "a" or "d":
        print "program stopping"
        speed(RPL.servoWrite(motor1,0))
        x = 1
        break
while z is 0:
    v = 1
    while v is 1 and command is "d":
        now = time.time()
        future = 1 + now
        while v is 1 and now < future:
            run(RPL.servoWrite(motor2,1000))
            while v is 1 and time.time() >= future:
                run(RPL.servoWrite(motor2,0))
                print "insert new input"
                v = 2
    if command is "d":
        command = raw_input("> ")
        continue
    while v is 1 and command is "a":
        now = time.time()
        future = 1 + now
        while v is 1 and now < future:
            run(RPL.servoWrite(motor2,2800))
            while v is 1 and time.time() >= future:
                run(RPL.servoWrite(motor2,0))
                print "insert new input"
                v = 2
    if command is "a":
        command = raw_input("> ")
        continue
    while command is not "w" or "s" or "a" or "d":
        run(RPL.servoWrite(motor1,0))
        v = 1
        break
