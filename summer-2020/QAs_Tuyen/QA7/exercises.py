# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *


# From discussion
def discussion_example():
  win = GraphWin()
  shape = Circle(Point(50, 50), 20)
  shape.setOutline("red")
  shape.draw(win)
  for i in range(10):
    p = win.getMouse()
    c = shape.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    shape.move(dx, dy)
  win.close()


# Exercise 1 a)
def draw_squares():
  win = GraphWin("Tuyen's Graphical Window")
  shape = Rectangle(Point(15, 15), Point(15+20, 15+20))
  shape.setOutline("red")
  shape.draw(win)
  for i in range(10):
    p = win.getMouse()
    c = shape.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    shape.move(dx, dy)
  win.close()


# Exercise 1 b) and c)
def acc_squares():
  win = GraphWin("Tuyen's Graphical Window")
  square = Rectangle(Point(15, 15), Point(15+20, 15+20))
  square.setOutline("red")
  square.draw(win)
  for i in range(10):
    p = win.getMouse()
    c = square.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    squareCopy = square.clone()
    squareCopy.move(dx, dy)
    squareCopy.draw(win)
  # c) Print a message after the loop
  # finalTxt = Text(Point(100, 100), "Click again to quit.")
  # finalTxt.draw(win)
  # win.getMouse()
  win.close()


# Exercise 2
def draw_archery_target():
  win = GraphWin("Archery Target", 250, 250)
  center = Point(250/2, 250/2)
  whiteCircle = Circle(center, 100)
  whiteCircle.setOutline("red")
  whiteCircle.draw(win)
  blackCircle = Circle(center, 80)
  blackCircle.setFill("black")
  blackCircle.draw(win)
  blueCircle = Circle(center, 70)
  blueCircle.setFill("blue")
  blueCircle.draw(win)
  redCircle = Circle(center, 55)
  redCircle.setFill("red")
  redCircle.draw(win)
  yellowCircle = Circle(center, 30)
  yellowCircle.setFill("yellow")
  yellowCircle.draw(win)

  win.getMouse()


def main():
  acc_squares()


main()
