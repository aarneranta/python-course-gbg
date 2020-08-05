# You need the file graphics.py from https://mcsp.wartburg.edu/zelle/python/
"This module provides different buttons."
from graphics import *
import math


class Button:
  """This class models a button's behavior,
  it doesn't care if it is rendered or how
  it is rendered. It only has a label."""

  def __init__(self, label):
    self.label = label
    self.deactivate()

  def deactivate(self):
    self.active = False

  def activate(self):
    self.active = True

  def getLabel(self):
    return self.label

  def isActive(self):
    return self.active


class RectangleButton:
  """Acts as a wrapper class for the model
  Button and will render a rectangular button.
  It will also tell if the button is clicked on
  by invoking clicked()."""
  # The code is pretty much the same as Zelle's code,
  # but now we have a model to base on.

  def __init__(self, button, win, center, width, height):
    self.model = button
    w, h = width/2.0, height/2.0
    x, y = center.getX(), center.getY()
    self.xmax, self.xmin = x+w, x-w
    self.ymax, self.ymin = y+h, y-h
    p1 = Point(self.xmin, self.ymin)
    p2 = Point(self.xmax, self.ymax)
    self.rect = Rectangle(p1, p2)
    self.rect.setFill('lightgray')
    self.rect.draw(win)
    self.label = Text(center, self.model.getLabel())
    self.label.draw(win)

  def deactivate(self):
    self.model.deactivate()
    self.label.setFill('darkgrey')

  def activate(self):
    self.model.activate()
    self.label.setFill('black')

  def clicked(self, p):
    return (self.model.isActive() and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)


class CircleButton:
  """Acts as a wrapper class for the model
  Button and will render a circular button with
  given center point and radius."""

  def __init__(self, button, win, center, radius):
    self.model = button
    self.center = center
    self.radius = radius
    self.circle = Circle(center, radius)
    self.circle.setOutline("blue")
    self.circle.setFill("lightgray")
    self.circle.draw(win)
    self.label = Text(center, self.model.getLabel())
    self.label.draw(win)
    self.deactivate()

  def deactivate(self):
    self.model.deactivate()
    self.label.setFill('darkgrey')

  def activate(self):
    self.model.activate()
    self.label.setFill('black')

  def clicked(self, p):
    # Calculate the distance from the mouse's position
    # to the center of the circle.
    dist = math.sqrt((p.getX() - self.center.getX())**2 +
                     (p.getY() - self.center.getY())**2)
    return (self.model.isActive() and
            dist < self.radius
            )

# Exercise: Try to expand upon Button and draw an oval button
