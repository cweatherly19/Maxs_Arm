import setup
import RoboPiLib as RPL
motor = 1
print "press y to go down, press a to go up, or n to stop"
start = raw_input("")
while true:
  while start == "y":
   RPL.servoWrite(motor, 2500)
   print "press n to stop"
   start1 = raw_input("")
   if start1 == "n":
     break
   if start1 == "a":
     break
  while start == "a":
   RPL.servoWrite(motor, 1000)
   print "press n to stop"
   start2 = raw_input("")
   if start2 == "n":
     break
   if start1 == "y":
     break
  while start == "n":
   RPL.servoWrite(motor, 0)
   break
