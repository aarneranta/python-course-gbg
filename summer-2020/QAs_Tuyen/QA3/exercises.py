import math
# Check video of QA on canvas if things
# are unclear. If it still is, email us :)


# 1. Write a program to calculate the volume and surface
# of a sphere from its radius, given as input.
def get_volume_surface_area(radius):
  volume = (4 / 3) * math.pi * radius ** 3
  surface_area = 4 * math.pi * radius ** 2
  return [volume, surface_area]


def circle_surface_area(radius):
  return math.pi * radius ** 2


# 2. Write a program that calculates the cost per square
# cm of a circular pizza, given its diameter and price.
# The formula for area is A= πr2
def pizza_cost_per_square_cm(diameter, price):
  surface_area = circle_surface_area(diameter / 2)
  return price / surface_area


# 5. Coffee 10.50 kr / kg. Shipping: 0.86 kr / kg + 1.5 kr
def get_coffee_order_cost(kg):
  coffee_cost = 10.5 * kg
  shipping = 0.86 * kg + 1.5
  return coffee_cost + shipping
