from math import sqrt, ceil

# OBS: långt ifrån den snabbaste lösningen


def is_prime(num):
    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            return False
    return True


def largest_prime_factor(num):
    for i in range(ceil(num/2), 1, -1):
        if num % i == 0 and is_prime(i):
            return i
    return num
