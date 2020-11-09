# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
"Rectangle button class provided by Zelle in in 10.6"
from graphics import *


class Button:
  """A button is labeled rectangle in a window.
  It is activated or deactivated with the activate()
  and deactivate() methods. The clicked(p) method 
  returns true if the button is active and p is inside it. """

  def __init__(self, win, center, width, height, label):
    """ Creates a rectangular button, e.g.:
    qb = Button(myWin, centerPoint, width, height, 'Quit')"""

    w, h = width/2.0, height/2.0
    x, y = center.getX(), center.getY()
    self.xmax, self.xmin = x+w, x-w
    self.ymax, self.ymin = y+w, y-w
    p1 = Point(self.xmin, self.ymin)
    p2 = Point(self.xmax, self.ymax)
    self.rect = Rectangle(p1, p2)
    self.rect.setFill('lightgray')
    self.rect.draw(win)
    self.label = Text(center, label)
    self.label.draw(win)
    self.deactivate()

  def clicked(self, p):
    "Returns true if button active and p is inside"
    return (self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)

  def getLabel(self):
    "Returns the label string of this button."
    return self.label.getText()

  def activate(self):
    "Sets this button to 'active'."
    self.active = True
    self.label.setFill('black')
    self.rect.setWidth(2)

  def deactivate(self):
    "Sets this button to 'inactive'."
    self.active = False
    self.label.setFill('darkgrey')
    self.rect.setWidth(1)
