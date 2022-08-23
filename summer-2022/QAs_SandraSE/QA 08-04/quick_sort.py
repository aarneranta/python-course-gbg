"""
Quick Sort Algorithm
"""
from random import randint


# Sorts the elements of a list in ascending order.
# This solution is the quick-sort algorithm https://www.geeksforgeeks.org/quick-sort/
def quick_sort(my_list):
    minimum_length = 2
    # If the input array contains fewer than two elements, then return it as the result of the function
    if len(my_list) < minimum_length:
        return my_list

    low, same, high = [], [], []

    # Select 'pivot' element randomly
    pivot = my_list[randint(0, len(my_list) - 1)]
    print('Pivot:', pivot)

    for i in my_list:
        # Elements that are smaller than the 'pivot' go to the 'low' list.
        # Elements that are larger than 'pivot' go to the 'high' list.
        # Elements that are equal to 'pivot' go to the 'same' list.
        if i < pivot:
            low.append(i)
            print('Low:', low)
        elif i == pivot:
            same.append(i)
            print('Same:', same)
        elif i > pivot:
            high.append(i)
            print('High:', high)

    # The final result combines the sorted 'low' list
    # with the `same` list and the sorted 'high' list
    return quick_sort(low) + same + quick_sort(high)


def main():
    numbers = [10, 80, 30]
    print('Before:', numbers)
    print('After:', quick_sort(numbers))

main()
