"""
Based on Chapter 4 Programming Exercise 2

An archery target consists of a central circle of yellow surrounded by concentric rings of red, blue, black and white.
Each ring has the same center point as the yellow circle. The width of the circles increase incrementally.
Write a program that draws such a target.
Hint: Objects drawn later will appear on top of objects drawn earlier.
"""
from graphics import *


def create_circles(colors, center, radius):
    list_circles = []
    radius_increase = 20

    for i in range(0, len(colors)):
        if i == 0:
            list_circles.append(Circle(center, radius))
            list_circles[i].setFill(colors[i])
        else:
            list_circles.append(Circle(center, list_circles[i-1].getRadius() + radius_increase))
            list_circles[i].setFill(colors[i])

    return list_circles


def main():
    win = GraphWin("Archery Target", 640, 480)
    win.setCoords(-320, -240, 320, 240)

    starting_radius = 20
    center_point = Point(0, 0)

    color_list = 'yellow', 'red', 'blue', 'black', 'white'
    circles_to_draw = create_circles(color_list, center_point, starting_radius)

    for i in range(len(circles_to_draw), 0, -1):
        circles_to_draw[i-1].draw(win)

    win.getMouse()
    win.close()


main()
