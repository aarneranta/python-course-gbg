"""
Chapter 10 Programming Exercise 9
Write a class to represent spheres. Your class should implement the following methods:

__init __(self, radius) Creates a sphere having the given radius.
get_radius(self) Returns the radius of this sphere.
surface_area(self) Returns the surface area of the sphere.
volume(self) Returns the volume of the sphere.

Use your new class to solve Programming Exercise 1 from Chapter 3:
Write a program to calculate the volume and surface area of a sphere from its radius, given as input.
Here are some formulas that might be useful:
V = (4/3)*π*r^3     A = 4*π*r^2
"""
from math import *


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * pi * pow(self.radius, 2)

    def volume(self):
        return (4/3) * pi * pow(self.radius, 3)


def main():
    decimal_places = 2

    user_input = input('Enter a radius to create a sphere: ')

    try:
        a_sphere = Sphere(float(user_input))
        print('Sphere volume:', round(a_sphere.volume(), decimal_places),
              '\nSphere surface area:', round(a_sphere.surface_area(), decimal_places))
    except ValueError:
        print('Invalid input! Try again.')


main()
