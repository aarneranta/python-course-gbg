# 1.
# Create a program with functions for basic arithmetic:
# add
# subtract
# multiply
# divide

# 2.
# Create a function which takes one operator and two numbers as parameters
# and then calculates the result

# 3.
# Ask the user for each of the parameters as input when running the program

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calculate(first_number, op, second_number):
    if op == '+':
        return add(first_number, second_number)
    elif op == '-':
        return subtract(first_number, second_number)


result = calculate(1, '-', 2)
print(result)