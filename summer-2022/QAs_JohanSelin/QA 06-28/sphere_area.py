from math import pi

# Program to calculate the surface area of a sphere
# See https://en.wikipedia.org/wiki/Sphere#Surface_area
#
# Formula is: area = 4 * pi * radius²     (kg/m²)


def calculate_sphere_area_program(radius):
    area = 4 * 3.14 * radius ** 2
    return area


result = calculate_sphere_area_program(4)
print(result)
