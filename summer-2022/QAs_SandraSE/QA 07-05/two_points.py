# Based on Chapter 3 Programming Exercise 6-7
#
# Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2).
# Write a program that:
# 1. Calculates the slope of a line through two (non-vertical) points entered by the user.
# Formula: slope = (y2 - y1) / (x2 - x1)
# 2. Determines the distance between the two points.
# Formula: √((x2-x1)²+(y2-y1)²)
# 3. Presents the results to the user by two decimal points.
from math import *


def slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


# Using sqrt and pow from math
def distance(x1, y1, x2, y2):
    distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return distance


# Using dist from math library for the complete calculation of distance
def distance_using_math(coordinate_1, coordinate_2):
    math_distance = dist(coordinate_1, coordinate_2)
    return math_distance


def main():
    decimals = 2

    print('This program calculates the slope and distance between two points in a 2D plane.')

    x_1 = (int(input('Enter the x value of point 1: ')))
    y_1 = (int(input('Enter the y value of point 1: ')))

    x_2 = (int(input('Enter the x value of point 2: ')))
    if x_2 == x_1:
        print('The points cannot be on the same vertical line in the 2D plane!')
        quit()
    y_2 = (int(input('Enter the y value of point 2: ')))

    result_slope = slope(x_1, y_1, x_2, y_2)
    result_distance = distance(x_1, y_1, x_2, y_2)

    # The dist function from math library takes in the x and y value for one point as ONE variable,
    # thus we must store the x and y value for one point in one list variable
    point_1 = [x_1, y_1]
    point_2 = [x_2, y_2]
    result_distance_using_math = distance_using_math(point_1, point_2)

    print('The slope is:', round(result_slope, decimals))
    print('The distance is:', round(result_distance, decimals))
    print('The distance is (using math.dist):', round(result_distance_using_math, decimals))


main()
