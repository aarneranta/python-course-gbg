"""
From Chapter 4 Programming Exercise 18

Five-click House.
You are to write a program that allows the user to draw a simple house using five mouse clicks.
The first two clicks will be the opposite corners of the rectangular frame of the house.
The third click will indicate the center of the top edge of a rectangular door.
The door should have a total width that is 1/5 of the width of the house frame.
The sides of the door should extend from the corners of the top, down to the bottom of the frame.
The fourth click will indicate the center of a square window.
The window is half as wide as the door.
The last click will indicate the peak of the roof.
The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.
"""
from graphics import *


def main():
    win = GraphWin("Five-Click House", 640, 480)
    win.setCoords(-320, -240, 320, 240)

    a_fifth = 1/5
    half = 1/2

    click_1 = win.getMouse()
    click_2 = win.getMouse()
    walls = Rectangle(click_1, click_2)
    walls.draw(win)

    click_3 = win.getMouse()
    wall_width = abs(click_1.getX() - click_2.getX())
    door_width = wall_width * a_fifth
    door_down_left_point = Point(click_3.getX() - (door_width * half), click_1.getY())
    door_up_right_point = Point(click_3.getX() + (door_width * half), click_3.getY())
    door = Rectangle(door_down_left_point, door_up_right_point)
    door.draw(win)

    click_4 = win.getMouse()
    window_width = (door_width * half)
    window_down_left_point = Point(click_4.getX() - (window_width * half), click_4.getY() - (window_width * half))
    window_up_right_point = Point(click_4.getX() + (window_width * half), click_4.getY() + (window_width * half))
    window = Rectangle(window_down_left_point, window_up_right_point)
    window.draw(win)

    click_5 = win.getMouse()
    right_side_roof = Line(click_5, click_2)
    left_side_roof = Line(click_5, Point(click_2.getX() - wall_width, click_2.getY()))
    right_side_roof.draw(win)
    left_side_roof.draw(win)

    win.getMouse()
    win.close()


main()
