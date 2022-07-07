# Chapter 5 Programming Exercise 2
#
# A certain CS professor gives 5-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
# Write a program that accepts a quiz score as an input and prints out the corresponding grade.

def get_grade(score):

    if score <= 1:
        return 'F'
    elif score == 2:
        return 'D'
    elif score == 3:
        return 'C'
    elif score == 4:
        return 'B'
    elif score == 5:
        return 'A'


def main():
    while True:
        user_input = input('Please enter the quiz score or press \'q\' to exit: ')
        if user_input == 'q':
            quit()
        elif int(user_input) < 0 or int(user_input > 5):
            print('Invalid Input! Try again.')
        else:
            print('The quiz grade is:', get_grade(int(user_input)))


main()
