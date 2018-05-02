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
screen.addstr('Hit q to quit. Use the w, a, s, and d to move. Hit e to find positions of motor 2')
#to read key inputs
key = ''
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    screen.clear()
    screen.addstr('Hit q to quit. Use the w, a, s, and d to move. Hit e to find positions of motor 2')
    screen.addstr('Detected key: ')
    #to define what keys preform commands
    if key == ord('w'):
        screen.addstr('w key')
        RPL.servoWrite(motor1, 1000)
    if key == ord('a'):
        screen.addstr('a key')
        position2 = position2 + 50
        #to allow for a full rotation
        if position2 > 3000:
            position2 = 800
        RPL.servoWrite(motor2, position2)
    if key == ord('s'):
        screen.addstr('k key')
        RPL.servoWrite(motor1, 2000)
    if key == ord('d'):
        screen.addstr('d key')
        position2 = position2 - 50
        #to allow for a full rotation
        if position2 < 800:
            position2 = 3000
        RPL.servoWrite(motor2, position2)
    RPL.servoWrite(motor1, 0)
    if key == ord('e'):
        screen.addstr('e key')
        screen.addstr('Value of motor 2: %d' %position2)
#to reformat the terminal/end the curses program
curses.endwin()
