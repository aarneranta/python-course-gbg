""" Chapter 13 Programming Exercise 4
Write and test a recursive function max to find the largest number in a list.
The max is the larger of the first item and the max of all the other items.
"""


def find_max(numbers):
    if len(numbers) == 0:
        return 'ERROR'
    elif len(numbers) == 1:
        print('(base) Returning ' + str(numbers[0]))
        return numbers[0]
    else:
        max_num = find_max(numbers[1:])
        if max_num > numbers[0]:
            print('Returning ' + str(max_num))
            return max_num
        else:
            print('(else) Returning ' + str(numbers[0]))
            return numbers[0]


def main():
    numbers = [200, 20, 101]
    print('Result:', find_max(numbers))


main()
