# From Chapter 11 Programming Exercise 6 & 8
# 1. Write and test a function shuffle(some_list) that scrambles a list into a random order,
# like shuffling a deck of cards.
# 2. Write and test a function remove_duplicates(some_list) that removes duplicate values from a list.
import random


def shuffle(some_list):

    shuffled_list = random.sample(some_list, len(some_list))
    return shuffled_list


def remove_duplicates(some_list):

    temp_dict = dict.fromkeys(some_list)
    no_duplicates = list(temp_dict)
    return no_duplicates


def main():
    list_of_animals = ['cat', 'dog', 'cat', 'tiger', 'shark', 'spider', 'zebra', 'zebra', 'crocodile', 'shark', 'shark']

    print('Original List:', list_of_animals)
    print('Shuffled List:', shuffle(list_of_animals))

    print('No duplicates:', remove_duplicates(list_of_animals))


main()

