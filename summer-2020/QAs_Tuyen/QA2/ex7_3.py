# A certain CS professor gives 100-point
# exams that are graded on the scale
# 90-100:A, 80-89:B, 70-79:C, 60-69:0, <60:F.
# Write a program that ac­ cepts an exam
# score as input and uses a decision structure
# to calculate the corresponding grade.


# This exercise is very similar to 7_2, but now
# we need to consider ranges too. We check
# if a score is greater than or equal to a
# grade limit. In 7_2, we only needed to check
# with equality.
def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    score = int(
        input("Which score did the student get? Enter an integer between 0-100: "))
    grade = getGrade(score)
    print("The student had {0} points and gets the grade {1}.".format(
        score, grade))


main()
