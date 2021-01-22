# Exempel med kvadrat

from graphics import *

win = GraphWin("Titel", 800, 800, autoflush=False)

square = Rectangle(Point(0, 0), Point(50, 50))
square.setFill("red")
square.draw(win)

# Håll fönstret öppet tills vi stänger det
while True:

    key = win.checkKey()  # The key being pressed (if any)

    if key == "Up":
        square.move(0, -50)
    elif key == "Down":
        square.move(0, 50)
    elif key == "Right":
        square.move(50, 0)
    elif key == "Left":
        square.move(-50, 0)
    elif key == "space":
        box = Rectangle(square.getP1(), square.getP2())
        box.setFill("red")
        box.draw(win)

    win.update()
