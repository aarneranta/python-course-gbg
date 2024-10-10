"""
In this version we have created a Racer class instead of just using a circle object to represent the race-car.
"""


# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *

speedLimit = 5 # How fast is the racer allowed to move
animationSpeed = 50 # How fast does time progress (higher value makes it faster), unit is updates per second

class Racer:
    def __init__(self, win):
        self.circle = Circle(Point(0,0), 10)
        self.circle.setFill('blue')
        self.circle.draw(win)

        # New feature - car now has a cool-looking red R on it!
        self.letter = Text(Point(0,0), "R")
        self.letter.setTextColor('red')
        self.letter.draw(win)

        self.xvelocity = 0
        self.yvelocity = 0

    def _moveRelative(self, xDiff,yDiff):
        self.circle.move(xDiff, yDiff)
        # Don't forget to move the 'R'
        self.letter.move(xDiff, yDiff)
        

    def _moveAbsolute(self, x,y):
        self._moveRelative(x-self.getX(),y-self.getY())
    
    def accelerate(self, xacc, yacc):
        self.xvelocity += xacc
        self.yvelocity += yacc

        # Enforce the speedlimit
        self.yvelocity = min(speedLimit, self.yvelocity)
        self.yvelocity = max(-speedLimit, self.yvelocity)
        self.xvelocity = min(speedLimit, self.xvelocity)
        self.xvelocity = max(-speedLimit, self.xvelocity)

        
    def slowDown(self):
        self.xvelocity *= 0.9
        self.yvelocity *= 0.9

    def drive(self):
        self._moveRelative(self.xvelocity, self.yvelocity)

    def reset(self):
        self._moveAbsolute(0,0)
        self.xvelocity = 0
        self.yvelocity = 0

    def getX(self):
        return self.circle.getCenter().getX()

    def getY(self):
        return self.circle.getCenter().getY()





# Create the main window. Disabling autoflush means the window will only be updated when update() is called.
win = GraphWin("Racer" , 640, 480, autoflush=False)
# This line sets (0,0) to be the middle of the window
win.setCoords(-320, -240, 320, 240)

# Use the constructor of the Racer-class to create a race-car
racer = Racer(win)

# Main animation loop
#  * If the user presses an arrow key accelerate in that direction (up to speed limit)
#  * If the user presses space, apply breaks to reduce speed
#  * If the user presses backspace the simulation is restarted
#  The speed of the loop is controlled by the update() function 
while(True):
    key = win.checkKey() # The key being pressed (if any)
    
    if key == "Up":
        racer.accelerate(0,1)
    elif key == "Down":
        racer.accelerate(0,-1)
    elif key == "Right":
        racer.accelerate(1,0)
    elif key == "Left":
        racer.accelerate(-1,0)
    elif key == "space":
        racer.slowDown()
    elif key == "BackSpace":
        racer.reset()

    # Move the racer based on current veclocity
    racer.drive()

    # Waits for the animation step to finish based on animationspeed, then redraws the window 
    update(animationSpeed)








