# Many companies pay time-and-a-half for any hours worked above 40 in a given
# week. Write a program to input the number of hours worked and the hourly rate
# and calculate the total wages for the week.

def ex1():
    numberOfHours = float(input("How many hour have you worked this week? "))
    hourlyRate = float(input("What is your hourly wage"))
    if numberOfHours < 40:
        totalWage = numberOfHours * hourlyRate
    else:
        totalWage = 40 * hourlyRate + (numberOfHours - 40) * hourlyRate * 1.5

    print("Your total wage this week was: ", totalWage)


# ex1()

# A certain CS professor gives five-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an
# input and uses a decision structure to calculate the corresponding grade.

def ex2():
    testScore = int(input("How many points did you get on the test? "))

    if testScore == 5: 
        grade = "A"
    elif testScore == 4:
        grade = "B"
    elif testScore == 3:
        grade = "C"
    elif testScore == 2:
        grade = "D"
    elif testScore == 1 or testScore == 0:
        grade = "F"
    else:
        grade = "Invalid"

    print("The grade was ", grade)

# ex2()

# A certain CS professor gives 100-point exams that are graded on the scale
# 90-100:A, 80-89:B, 70-79:C, 60-69:0, <60:F. Write a program that accepts an
# exam score as input and uses a decision structure to calculate the
# corresponding grade.

def ex3():
    testScore = int(input("How many points did you get on the test? "))

    if testScore > 100:
        grade = "Invalid"
    elif testScore >= 90:
        grade = "A"
    elif testScore >= 80:
        grade = "B"
    elif testScore >= 70:
        grade = "C"
    elif testScore >= 60:
        grade = "D"
    else: 
        grade = "F"

    print("The grade was ", grade)


ex3()
