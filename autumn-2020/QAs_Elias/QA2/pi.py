import random
import matplotlib.pyplot as plt

# Förklarar sig själv då man ser bilden!
def piDart(shots):
    hit = 0
    for _ in range(shots):
        x = 2*random.random()-1
        y = 2*random.random()-1
        if x**2+y**2 < 1:
            hit += 1
            plt.plot(x, y, 'r.')
        else:
            plt.plot(x, y, 'b.')
    plt.grid()
    plt.axis('equal')
    plt.show()
    return hit/shots*4 #Kvadratens area: 4, cirkelns area: pi

# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
def piSum(n):
    approx = 0
    sign = 1
    for i in range(1, n, 2):
        approx += 1/i*sign
        sign *= -1
    return approx*4

# ------ Överkurs! ------

# Sannolikheten att två tal har samma största gemensamma delare (som inte är ett) är 6 / pi ** 2
# Det vill säga: pi = sqrt(6 / sannolikhet) = (6*n/m))**0.5
def piGcd(n):
    m = 0
    for _ in range(n):
        x1 = 1+int(100000000*random.random())
        x2 = 1+int(100000000*random.random())

        if gcd(x1,x2)==1:
            m += 1

    return (6*n/m)**0.5

def gcd(a, b): #https://en.wikipedia.org/wiki/Euclidean_algorithm
    while b != 0:
        a, b = b, a%b
    return a
