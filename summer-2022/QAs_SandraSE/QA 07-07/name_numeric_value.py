# Chapter 5 Programming Exercise 5

# Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name.
# The value of a name is determined by summing up the values of the letters of the name where
# "a" is 1 "b" is 2 "c" is 3 up to "z" being 26
# For example the name "Zelle" would have the value 26 + 5 + 12 + 12 + 5 = 60
# Write a program that calculates the numeric value of a single name provided as input.

def calculate_value(name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numeric_value = 0

    for i in name:
        # Since the first position in a String is 0 we need to add + 1
        numeric_value += alphabet.find(i) + 1

    return numeric_value


def main():
    user_input = input('Enter a name to calculate it\'s numeric value: ')
    result = calculate_value(list(user_input))
    print('The numeric value of', user_input, 'is:', result)


main()
