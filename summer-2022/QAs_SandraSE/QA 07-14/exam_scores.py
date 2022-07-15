# From Chapter 7 Programming Exercise 3
#
# A certain CS professor gives 100-point exams that are graded on the scale
# 90-100:A, 80-89:B, 70-79:C, 60-69:0, <60:F.
# Write a program that accepts an exam score as input and uses a decision structure to calculate the corresponding grade

def calculate_grade(points):
    if points < 60:
        grade = 'F'
    elif 60 <= points <= 69:
        grade = 'D'
    elif 70 <= points <= 79:
        grade = 'C'
    elif 80 <= points <= 89:
        grade = 'B'
    else:
        grade = 'A'

    return grade


def main():
    stop = False
    min_points = 0
    max_points = 100

    while stop is False:
        user_input = input('Input the student\'s exam points to calculate the grade or press \'q\' to exit: ')
        if user_input == 'q':
            stop = True
        elif user_input.isdigit() and min_points < int(user_input) < max_points:
            print('The grade is:', calculate_grade(int(user_input)))
        else:
            print('Invalid input! Try again.')

    print('Bye!')


main()

