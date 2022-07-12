# Chapter 5 Programming Exercise 4
#
# An acronym is a word formed by taking the first letters of the words in a
# phrase and making a word from them. For example, RAM is an acronym
# for "random access memory." Write a program that allows the user to
# type in a phrase and then outputs the acronym for that phrase. Note: The
# acronym should be all uppercase, even if the words in the phrase are not
# capitalized.

def make_acronym(phrase):
    list_of_words = phrase.split()
    capitals = []

    for i in list_of_words:
        capitals += i[0].upper()

    acronym = ''.join(capitals)
    return acronym


def main():

    user_input = input('Enter a phrase to turn it into an acronym: ')
    print('The acronym is:', make_acronym(user_input))


main()
