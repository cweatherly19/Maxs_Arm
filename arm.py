import setup
import RoboPiLib as RPL
motor = 1
print "press y to go, then n to stop"
start = raw_input("")
while start == "y":
  RPL.servoWrite(motor, 2500)
  print "press y to go, then n to stop"
  start1 = raw_input("")
  if start1 == "n":
    break
    RPL.servoWrite(motor, 0)
