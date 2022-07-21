"""
Chapter 10 Programming Exercise 6

Extend the previous exercise by implementing an add_letter_grade method.
This is similar to add_grade except that it accepts a letter grade as a string (instead of grade_point).
Use the updated class to improve the GPA calculator by allowing the entry of letter grades.
"""


class Student:
    def __init__(self, name, hours, q_points):
        self.name = name
        self.hours = float(hours)
        self.q_points = float(q_points)

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_q_points(self):
        return self.q_points

    def gpa(self):
        return self.q_points / self.hours

    def add_grade(self, grade_point, credit):
        self.q_points += (grade_point * credit)
        self.hours += credit

    def add_letter_grade(self, letter_grade, credit):
        if letter_grade == 'A':
            self.q_points += 4.00 * credit
        elif letter_grade == 'A-':
            self.q_points += 3.67 * credit
        elif letter_grade == 'B+':
            self.q_points += 3.33 * credit
        elif letter_grade == 'B':
            self.q_points += 3.00 * credit
        elif letter_grade == 'B-':
            self.q_points += 2.67 * credit
        elif letter_grade == 'C+':
            self.q_points += 2.33 * credit
        elif letter_grade == 'C':
            self.q_points += 2.00 * credit
        elif letter_grade == 'C-':
            self.q_points += 1.67 * credit
        elif letter_grade == 'D+':
            self.q_points += 1.33 * credit
        elif letter_grade == 'D':
            self.q_points += 1.00 * credit
        elif letter_grade == 'D-':
            self.q_points += 0.67 * credit
        elif letter_grade == 'F':
            self.q_points += 0.00 * credit

        self.hours += credit


def main():
    decimal_places = 2

    # Creating a student with 0 credits and 0 quality points
    a_student = Student('Sandra SE', 0, 0)

    # use text file 'letter_grades'
    filename = input("Enter the name of the courses file: ")
    file = open(filename, 'r')

    # process subsequent lines of the file
    for line in file:
        letter_grade, credit = line.split()
        a_student.add_letter_grade(letter_grade.upper(), float(credit))

    print('Final GPA is:', round(a_student.gpa(), decimal_places))

    file.close()


main()
