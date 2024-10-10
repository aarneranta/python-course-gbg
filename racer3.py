"""
In this version we have moved 
"""


# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *

speedLimit = 5 # How fast is the racer allowed to move
animationSpeed = 50 # How fast does time progress (higher value makes it faster), unit is updates per second

"""
  Models a race-car, keeping track of its current position and velocity
  this class has no graphics-code
"""
class Racer:
    def __init__(self):
        self.xvelocity = 0
        self.yvelocity = 0
        self.xpos = 0
        self.ypos = 0

    def _moveRelative(self, xDiff,yDiff):
        self.xpos += xDiff
        self.ypos += yDiff

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

    """ Drive for one time-unit of time """
    def drive(self):
        self._moveRelative(self.xvelocity, self.yvelocity)

    """ Return to position (0,0) and stop """
    def reset(self):
        self._moveAbsolute(0,0)
        self.xvelocity = 0
        self.yvelocity = 0

    def getX(self):
        return self.xpos;

    def getY(self):
        return self.ypos;



"""
  Wraps around a Racer, creating graphical elements for it
    this class delegates all method calls to the underlying Racer-object
    just doing what's needed to make the car show up correctly in
    the graphical window
"""
class RacerGraphics:
    def __init__(self, racer, win):
        self.win = win
        self.model = racer

        self.circle = Circle(Point(0,0), 10)
        self.circle.setFill('blue')
        self.circle.draw(win)

        self.letter = Text(Point(0,0), "R")
        self.letter.setTextColor('red')
        self.letter.draw(win)

    """
    Synchronize the graphics with the current state of the model
    """
    def sync(self):
        # Move the circle and text to wherever the car is
        m = self.model # These definitions are just to make the code a little shorter
        c = self.circle
        t = self.letter

        # Move the circle and text elements to the current position of the model
        c.move(m.getX()-c.getCenter().getX(), m.getY()-c.getCenter().getY())
        t.move(m.getX()-t.getAnchor().getX(), m.getY()-t.getAnchor().getY())


# Create the main window. Disabling autoflush means the window will only be updated when update() is called.
win = GraphWin("Racer" , 640, 480, autoflush=False)
# This line sets (0,0) to be the middle of the window
win.setCoords(-320, -240, 320, 240)

# Create a model of a race-car, and graphics for it
racer = Racer()
graphics = RacerGraphics(racer, win)

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
    
    # Sync graphics with model
    graphics.sync()

    # Waits for the animation step to finish based on animationspeed, then redraws the window 
    update(animationSpeed)


