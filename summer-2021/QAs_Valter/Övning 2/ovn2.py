# Write a Python program (function) to multiply two integers without using the * operator in python. (2 min) (slide 34)
def mult(x, y):
    s = 0
    for i in range(y):
        s += x
    return s


# 3.7: Write a program that accepts two points (see previous problem) and de­-
#      termines the distance between them.
def distance(x1, y1, x2, y2):
    # p1 och p2 är tuples med två element var
    # Tuple "deconstructing"
    # x1,y1 = p1
    # x2,y2 = p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
    # eller math.sqrt((x1-x2)**2 + (y1-y2)**2)
    # eller math.hypot(x1-x2,y1-y2)
# Alternativt:     distance = lambda x1,y1,x2,y2: math.hypot(x1-x2,y1-y2)


# 3.12: Write a program to find the sum of the cubes of the first n natural numbers
#       where the value of n is provided by the user.
def main():
    n = int(input("n: "))
    s = 0  # Använd ej sum som namn
    for i in range(1, n+1):
        s += i**3
    print(f"Sum of the first {n} numbers cubed is {s}")
    # Alternativt: s = sum(x**3 for x in range(1,n+1))


# 3.15: Write a program that approximates the value of pi by summing the terms
#       of this series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + . . . The program should
#       prompt the user for n, the number of terms to sum, and then output the
#       sum of the first n terms of this series. Have your program subtract the
#       approximation from the value of math. pi to see how accurate it is .
def main():
    n = int(input("Number of terms to sum: "))
    s = 0
    for i in range(n):
        s += (-1)**i * 4/(1+2*i)
    print(f"Approximation of pi is {s}")
    print(f"Error is {abs(math.pi-s)}")


# 3.16: A Fibonacci sequence is a sequence of numbers where each successive
#       number is the sum of the previous two. The classic Fibonacci sequence
#       begins: 1, 1, 2, 3, 5, 8, 13, . . . . Write a program that computes the nth
#       Fibonacci number where n is a value input by the user. For example, if
#       n = 6, then the result is 8.
def main():
    n = int(input("nth fibonacci number to calculate: "))
    if n < 1:
        print("n has to be positive")
    else:
        num1 = 1
        num2 = 1
        for i in range(n-2):
            num1, num2 = num2, num1+num2
        print(f"Fibonacci Nr.{n} is {num2}")
