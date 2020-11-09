import math

# Write a function to calculate the volume and surface area of a sphere from
# its radius, given as an argument.

def volumeOfSphere(r):
    return 4 * r**3 * math.pi / 3

def areaOfSphere(r):
    return 4 * math.pi * r**2

def main():
    print(f"Area av enhetssfär: {areaOfSphere(1)}")
    print(f"Volym av enhetssfär: {volumeOfSphere(1)}")


# main()

# Write a function that calculates the cost per square centimeter of a circular
# pizza, given its radius and price

def areaOfPizza(r):
    return math.pi * r**2

def costDensityOfPizza(radius, price):
    return price / areaOfPizza(radius)

def main2():
    pizzaCost = 100
    pizzaRadius = 20
    print(f"Kostnad per cm^2 är {costDensityOfPizza(pizzaRadius, pizzaCost):.3f} kronor")

# main2()


# Write a function that calculates the cost per cubic centimeter of a circular
# pizza, given radius, height and price

def cubicCostDensity(radius, height, price):
    volumeOfPizza = areaOfPizza(radius) * height
    return price / volumeOfPizza

def main3():
    pizzaCost = 200
    pizzaRadius = 40
    pizzaHeight = 2
    print(f"Kostnad per cm^3 är {cubicCostDensity(pizzaRadius, pizzaHeight, pizzaCost):.2f} kronor")

# main3()

# Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2)
# Write a function that calculates the slope of a line through two
# (non-vertical) points


def slopeOfLine(p1, p2):
    # (x1, y1), (x2, y2) => lutningen = (y2-y1)/(x2-x1)
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return k


# Write a program that accepts two points (see previous problem) and determines
# the distance between them

def distance(p1, p2):
    d = math.sqrt((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)
    return d
