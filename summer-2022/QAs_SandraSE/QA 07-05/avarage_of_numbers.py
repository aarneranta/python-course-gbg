# Based on Chapter 3 Programming Exercise 14
#
# Write a program that finds the average of a series of numbers entered by
# the user WITHOUT asking how many numbers the user wishes to input.
# Note: The average should always be a float, even if the user inputs are all ints.

def calculate_average(input_string):
    sum_of_numbers = 0
    divide_by = 0

    numbers = input_string.split()

    for i in numbers:
        divide_by += 1
        sum_of_numbers += int(i)

    average = sum_of_numbers/divide_by
    return average


def main():
    user_input = input('Enter a series of numbers separated by \'space\' to calculate the average: ')
    print('The average of the numbers is:', calculate_average(user_input))


main()
