"""
Chapter 10 Programming Exercise 5
Modify the Student class from the chapter by adding a mutator method that records a grade for the student.
Here is the specification of the new method:

add_grade(self, grade_point, credits) grade_point is a float that represents a grade (e.g., A= 4.0, A- = 3.7, B+ = 3.3),
and credits is a float indicating the number of credit hours for the class.
Modify the student object by adding this grade information.
Use the updated class to implement a simple program for calculating GPA.
Your program should create a new student object that has 0 credits and 0 quality points (the name is irrelevant).
Your program should then prompt the user to enter course information (gradePoint and credits) for a series of courses,
and then print out the final GPA achieved.
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


def main():
    decimal_places = 2

    # Creating a student with 0 credits and 0 quality points
    a_student = Student('Sandra SE', 0, 0)

    # use text file 'grade_points'
    filename = input("Enter the name of the courses file: ")
    file = open(filename, 'r')

    # process subsequent lines of the file
    for line in file:
        grade_point, credit = line.split()
        a_student.add_grade(float(grade_point), float(credit))

    print('Final GPA is:', round(a_student.gpa(), decimal_places))

    file.close()


main()
