# This is an exercise done 2022-07-05, it was based on Chapter 3 Programming Exercise 14.
# Add decisions and/or exception handling as required to make it truly robust (will not crash on any inputs).

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
    try:
        print('The average of the numbers is:', calculate_average(user_input))
    except (ValueError, ZeroDivisionError):
        print('Invalid input!')
        main()


main()
