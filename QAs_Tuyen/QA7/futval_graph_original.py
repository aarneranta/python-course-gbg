# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *

# This file draws the graph of what you accumulate
# when you invest with an interest rate
# The values given when drawing in the window is based
# on the window's initial size 320x240.
# See fig 4.8 in Zelle's book.
# Source code from the book with some small modifications


def drawGraph(principal, apr):
  win = GraphWin("Investment Growth Chart", 320, 240)
  win.setBackground("white")
  # Drawing the labels for the Y-axis
  # Upper left corner of window is (0,0), y-axis grows downwards
  Text(Point(20, 230), ' 0.0K').draw(win)
  Text(Point(20, 180), ' 2.5K').draw(win)
  Text(Point(20, 130), ' 5.0K').draw(win)
  Text(Point(20, 80), ' 5.0K').draw(win)
  Text(Point(20, 30), ' 5.0K').draw(win)

  # Draw bar for the initial principal
  height = principal * 0.02
  bar = Rectangle(Point(40, 230), Point(40 + 25, 230-height))
  bar.setFill("green")
  bar.setWidth(2)
  bar.draw(win)

  # Draw bars for successive years
  for year in range(1, 11):
    # Calculate the value for the next year
    principal = principal * (1 + apr)
    # draw bar for this value
    # Every bar is 25px wide and 40px
    # to the right of the initial bar
    x_pos = year * 25 + 40
    height = principal * 0.02
    bar = Rectangle(Point(x_pos, 230), Point((x_pos + 25), 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


def main():
  # Introduction
  print("This program plots the growth of a 10-year investment.")

  # Get principal and interest rate
  principal = float(input("Enter the initial principal: "))
  apr = float(input("Enter the annualized interest rate: "))

  drawGraph(principal, apr)

  input("Press <Enter> to quit")
  sys.exit()


main()
