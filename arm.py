#to access and establish files needed to run the code
import curses
import setup
import RoboPiLib as RPL
# to define motor pins
motor1 = 0
motor2 = 1
# to define motor2 position
position2 = 800
#to define the 'screen' in front of functions
screen = curses.initscr()
#to tell the user valid inputs
screen.addstr('Hit q to quit. Use the W, A, S, and D to move.)
#to read key inputs
key = ''
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    #to define what keys preform commands
    if key == ord('w'):
        RPL.servoWrite(motor1, 1000)
    if key == ord('a'):
        position2 = position2 + 50
        if position2 > 3000:
            position2 = 800
        RPL.servoWrite(motor2, position2)
    if key == ord('s'):
        RPL.servoWrite(motor1, 2000)
    if key == ord('d'):
        position2 = position2 - 50
        if position2 < 800:
            position2 = 3000
        RPL.servoWrite(motor2, position2)
    if key == ord(''):
        RPL.servoWrite(motor1, 0)
#to reformat the terminal/end the curses program
curses.endwin()
