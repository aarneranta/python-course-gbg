# From Chapter 6 Programming Exercise 4
#
# 1. Write definitions for the following two functions:
# sum_n (n) returns the sum of the first n natural numbers.
# sum_n_cubes (n) returns the sum of the cubes of the first n natural numbers.
#
# 2. Then use these functions in a program that prompts a user for an n
# and prints out the sum of the first n natural numbers and the sum of the cubes of the first n natural numbers.

# Solution 1
def sum_n(n):
    result_sum = 0

    while n > 0:
        result_sum += n
        n -= 1
    return result_sum


def sum_n_cubes(n):
    result_sum_cubes = 0

    while n > 0:
        result_sum_cubes += n ** 3
        n -= 1
    return result_sum_cubes


def main():
    user_n = int(input('Enter a natural number: '))

    print('The sum of the first (', user_n, ') natural numbers is:', sum_n(user_n), 'The sum of their cubes is:',
          sum_n_cubes(user_n))


main()

# Solution 2
def sum_n_2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_n_cubes_2(n):
    sum_cubes = 0
    for i in range(1, n + 1):
        sum_cubes += i ** 3
    return sum_cubes
