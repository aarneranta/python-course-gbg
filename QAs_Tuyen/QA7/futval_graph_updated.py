# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
from graphics import *

# Exercise 6 based on futval_graph_original.py
# This code takes in the values from the
# window's inputs, and has a fake button
# that allows the user to plot the chart.


# We create the bars and return them instead
# of drawing them immediately to the window.
# This way, the bars are accessible and can
# be undrawn when needed.
def createBars(principal, apr):
  bars = []

  # Create bar for the initial principal
  height = principal * 0.02
  bar = Rectangle(Point(40, 230), Point(40 + 25, 230-height))
  bars.append(bar)

  # Create bars for successive years
  for year in range(1, 11):
    # Calculate the value for the next year
    principal = principal * (1 + apr)
    # Create bar for this value
    # Every bar is 25px wide and 40px
    # to the right of the initial bar
    x_pos = year * 25 + 40
    height = principal * 0.02
    bar = Rectangle(Point(x_pos, 230), Point((x_pos + 25), 230-height))
    bars.append(bar)

  return bars


def drawGraph(principal=2000, apr=0.1):
  winWidth = 350
  winHeight = 370
  win = GraphWin("Investment Growth Chart", winWidth, winHeight)
  win.setBackground("white")
  # Drawing the labels for the Y-axis
  # Upper left corner of window is (0,0), y-axis grows downwards
  Text(Point(20, 230), ' 0.0K').draw(win)
  Text(Point(20, 180), ' 2.5K').draw(win)
  Text(Point(20, 130), ' 5.0K').draw(win)
  Text(Point(20, 80), ' 5.0K').draw(win)
  Text(Point(20, 30), ' 5.0K').draw(win)

  # Draw labels
  principalTxt = Text(Point(winWidth/2 - 45, 260),
                      "Enter the initial principal:")
  principalTxt.draw(win)
  aprTxt = Text(Point(winWidth/2 - 65, 290),
                "Enter the annualized interest rate:")
  aprTxt.draw(win)

  # Draw inputs
  principalInput = Entry(Point(winWidth/2 + 45, 260), 5)
  principalInput.setText("2000")
  principalInput.draw(win)
  aprInput = Entry(Point(winWidth/2 + 45, 290), 5)
  aprInput.setText(0.1)
  aprInput.draw(win)

  # Draw fake button
  button = Rectangle(Point(40, 315), Point((winWidth - 40), (315 + 35)))
  button.setOutline("black")
  button.draw(win)
  buttonTxt = Text(Point(winWidth / 2, 315 + (35/2)),
                   "Plot growth of 10 years")
  buttonTxt.draw(win)

  bars = []
  while(True):
    # Only call getMouse() once, otherwise the program
    # will the amount of clicks that getMouse() is called.
    mousePos = win.getMouse()
    mousePosX = mousePos.getX()
    mousePosY = mousePos.getY()

    # If mouse click is in button area
    if ((mousePosX > 40) and (mousePosX < (winWidth - 40)) and (mousePosY > 315) and (mousePosY < (315+35))):
      # If there are old bars, undraw them
      if (bars):
        for bar in bars:
          bar.undraw()

      # Draw new bars based on values in Entry-boxes
      principal = float(principalInput.getText())
      apr = float(aprInput.getText())
      bars = createBars(principal, apr)
      for bar in bars:
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)


def main():
  # Introduction
  print("This program plots the growth of a 10-year investment.")

  drawGraph()

  input("Press <Enter> to quit")
  sys.exit()


main()
