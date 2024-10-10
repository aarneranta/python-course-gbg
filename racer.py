
# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *

speedLimit = 5 # How fast is the racer allowed to move
animationSpeed = 50 # How fast does time progress (higher value makes it faster), unit is updates per second

# Create the main window. Disabling autoflush means the window will only be updated when update() is called.
win = GraphWin("Racer" , 640, 480, autoflush=False)
# This line sets (0,0) to be the middle of the window
win.setCoords(-320, -240, 320, 240)

# Create the racer (a blue circle)
racer = Circle(Point(0,0), 10)
racer.setFill('blue')
racer.draw(win)

# Initially the circle is standing still
xvelocity = 0
yvelocity = 0

# Main animation loop
#  * If the user presses an arrow key accelerate in that direction (up to speed limit)
#  * If the user presses space, apply breaks to reduce speed
#  * If the user presses backspace the simulation is restarted
#  The speed of the loop is controlled by the update() function 
while(True):
    key = win.checkKey() # The key being pressed (if any)
    
    if key == "Up":
        yvelocity += 1
    elif key == "Down":
        yvelocity -= 1
    elif key == "Right":
        xvelocity += 1
    elif key == "Left":
        xvelocity -= 1
    elif key == "space":
        # Break by 10% each animation step if holding space
        xvelocity *= 0.9
        yvelocity *= 0.9
    elif key == "BackSpace":
        # Move the racer back to (0,0) and stop it
        racer.move(-racer.getCenter().getX(),-racer.getCenter().getY())
        xvelocity = 0
        yvelocity = 0
        # ECERCISE: Make the car leave marks when breaking (by drawing dots/lines)

    # This can be used to check the key codes of other keys in case you want to add more key-bindings
    #elif key != "":
    #    print("Key pressed: " + key)
    

    # Enforce the speedlimit
    yvelocity = min(speedLimit, yvelocity)
    yvelocity = max(-speedLimit, yvelocity)
    xvelocity = min(speedLimit, xvelocity)
    xvelocity = max(-speedLimit, xvelocity)

    # Move the racer based on current veclocity
    racer.move(xvelocity,yvelocity)

    # EXERCISE: Reset the racer if it moves outside the window?

    # EXERCISE: Make the car look nicer


    # EXERCISE: (Advanced) Change the car to use angle and velocity instead of y-velocity directly, and left/right
    # TODO: Draw 

    # Waits for the animation step to finish based on animationspeed, then redraws the window 
    update(animationSpeed)








