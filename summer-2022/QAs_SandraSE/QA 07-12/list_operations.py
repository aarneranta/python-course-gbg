# From Chapter 11 Programming Exercise 5
#
# Most languages do not have the flexible built-in list (array) operations
# that Python has. Write an algorithm for each of the following Python
# operations and test your algorithm by writing it up in a suitable function.
# For example, as a function, reverse(myList) should do the same as myList.reverse( ).
# Obviously, you are not allowed to use the corresponding Python method to implement your function.
# a) count(myList, x) (like myList.count(x))
# b) isin(myList, x) (like x in myList)
# c) index(myList, x) (like myList.index(x))
# d) reverse(myList) (like myList.reverse())
# e) sort(myList) (like myList.sort())
from random import randint


#  Returns the count of how many times a given element occurs.
def count(my_list, x):
    occurrences = 0

    for i in range(0, len(my_list)):
        if my_list[i] == x:
            occurrences += 1

    return occurrences


# Checks if the given element exists.
def isin(my_list, x):

    for i in range(0, len(my_list)):
        if my_list[i] == x:
            return True

    return False


# Returns the index of the specified element.
# The .index() method only returns the first occurrence of the matching element.
def index(my_list, x):
    position = 0

    for i in range(0, len(my_list)):
        if my_list[i] == x:
            position = i
            return position

    return 'Element not in list'


# Reverses the elements.
def reverse(my_list):
    reversed_list = []

    for i in range(len(my_list), 0, -1):
        # print(i)
        reversed_list.append(my_list[i-1])
        # print(reversed_list)

    return reversed_list


# Sorts the elements of a list in ascending order.
# This solution is the quick-sort algorithm https://www.geeksforgeeks.org/quick-sort/
def sort(my_list):
    minimum_length = 2
    # If the input array contains fewer than two elements, then return it as the result of the function
    if len(my_list) < minimum_length:
        return my_list

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = my_list[randint(0, len(my_list) - 1)]

    for i in my_list:
        # Elements that are smaller than the `pivot` go to the `low` list.
        # Elements that are larger than `pivot` go to the `high` list.
        # Elements that are equal to `pivot` go to the `same` list.
        if int(i) < int(pivot):
            low.append(i)
        elif int(i) == int(pivot):
            same.append(i)
        elif int(i) > int(pivot):
            high.append(i)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return sort(low) + same + sort(high)


def main():
    user_list = ['6', '5', '9', '3', '1', '5']
    copy_list = ['6', '5', '9', '3', '1', '5']  # Used to demonstrate the built-in .reverse() and .sort() function
    x = '1'

    print('Custom count() function result:', count(user_list, x), '\nBuilt-in function result:', user_list.count(x), '\n')
    print('Custom isin() function result:', isin(user_list, x), '\nBuilt-in function result:', x in user_list, '\n')
    print('Custom index() function result:', index(user_list, x), '\nBuilt-in function result:', user_list.index(x), '\n')
    copy_list.reverse()  # The built-in .reverse() function reverses an existing list instead of returning a new list,
    # so we call the function on a copy of the our user_list so we can then display its content below
    print('Custom reverse() function result:', reverse(user_list), '\nBuilt-in function result:', copy_list, '\n')
    copy_list.sort()  # Same goes for the built-in .sort() function
    print('Custom sort() function result:', sort(user_list), '\nBuilt-in function result:', copy_list, '\n')


main()
