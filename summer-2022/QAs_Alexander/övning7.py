# -*- coding: utf-8 -*-
"""
Alter the  program in the following way:
    1. Make it draw squares instead of circles
    2. Have each click draw an additional square on the screen (instead of moving)
    3. Print a message in the window "Click again to quit" after the loop
    and wait for a final click before closing the window
"""

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    
    for i in range(5):
        p1 = win.getMouse()
        p2 = win.getMouse()
        shape = Rectangle(p1, p2)
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
    
    message = Text(Point(80,40), "Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()
    
main()



# -*- coding: utf-8 -*-
"""
Line segment information

This program allows the user to draw a line segment and then displays some graphical
and textual information about the line segment

Input: Two mouse clicks for the end points of the line segment 
Output: Draw the midpoint of the segment in cyan
Draw the line
Print the lenght and slope of the line

dx = x2-x1
dy = y2-y1
slope = dy/dx
length = sqrt(dx^2 + dy^2)
"""


from graphics import *
import math

def main():
    #Skapa fönstret
    win = GraphWin()
    #Ta två punkter från musen
    p1 = win.getMouse()
    p2 = win.getMouse()
    
    #Skapa linje
    line = Line(p1,p2)

    
    #Skapa och rita ut mittpunkt
    midpoint = line.getCenter()
    midpoint.setFill("Cyan")
    midpoint.setOutline("Cyan")
    midpoint.draw(win)
    
    #Rita ut linje
    line.setFill("Red")
    line.draw(win)
    
    #Beräkna längd och lutning
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = (dy/dx)
    length = (math.sqrt(dx**2+dy**2))
    
    #Skriv ut längd och lutning 
    
    #Börja med plus, visa att det inte blir så snyggt
    length_message = Text(Point(80,50), "Lenght is {:.2f}".format(length))
    slope_message = Text(Point(80,70), "Slope is {:.2f}".format(slope))
    length_message.draw(win)
    slope_message.draw(win)
    
    
    #Stäng fönster
    message = Text(Point(80,30), "Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()
    
main()
    

