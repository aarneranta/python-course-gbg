from numpy import pi, cos, sqrt, abs
import time
from functools import lru_cache

fib_cache = {}


def fib(x):
    if x in fib_cache:
        return fib_cache[x]

    if x <= 2:
        value = 1
    else:
        value = fib(x-1) + fib(x-2)

    fib_cache[x] = value
    return value


@lru_cache(maxsize=1000)
def fib_recursion(x):
    return x <= 2 or fib_recursion(x-1) + fib_recursion(x-2)


sqrt5 = sqrt(5)
fi = (1+sqrt5) / 2


def fib_closed(x):
    return int((fi ** x - cos(pi * x) * fi ** (-x))/sqrt5)


n = 100
start = time.time()
recursive_value = fib_recursion(n)
print(recursive_value)
end = time.time()
print("Elapsed time for recursive formula:", end-start, "seconds.")

start = time.time()
closed_value = fib_closed(n)
print(closed_value)
end = time.time()
print("Elapsed time for closed formula:", end-start, "seconds.")
print("Closed value deviation:", abs((closed_value - recursive_value)/recursive_value))
# Recursive formula is exact


def fact(n):
    return n < 2 or n * fact(n - 1)


def summa(arr):
    if len(arr) > 1:
        return arr.pop() + summa(arr)
    else:
        return arr[0]

