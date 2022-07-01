# From Chapter 6 Programming Exercise 1
#
# 1. Write a program to print the lyrics of the song "Old MacDonald." Your
# program should print the lyrics for five different animals, similar to the
# example verse below.
#
# "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
# And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
# With a moo, moo here and a moo, moo there.
# Here a moo, there a moo, everywhere a moo, moo.
# Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"

# Solution
def animal_verse(animal, animal_sound):
    verse = 'Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\nAnd on that farm he had ' + animal + \
            ', Ee-igh, Ee-igh, Oh!\nWith a ' + animal_sound + '-' + animal_sound + ' here and a ' + animal_sound \
            + '-' + animal_sound + ' there.\nHere a ' + animal_sound + ', there a ' + animal_sound + ', everywhere a ' \
            + animal_sound + '-' + animal_sound + '.\nOld MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n'
    return verse


def main():
    print(animal_verse('cow', 'moo'))
    print(animal_verse('cat', 'meow'))
    print(animal_verse('dog', 'woof'))
    print(animal_verse('chicken', 'cluck'))
    print(animal_verse('pig', 'oink'))


main()



