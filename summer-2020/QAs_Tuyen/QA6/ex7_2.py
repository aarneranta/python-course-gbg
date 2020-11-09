# A certain CS professor gives five-point quizzes
# that are graded on the scale 5-A, 4-B, 3-C, 2-D,
# 1-F, 0-F. Write a program that accepts a quiz
# score as an input and uses a decision structure
# to calculate the corresponding grade.

def getGrade(score):
  if score == 5:
    return "A"
  elif score == 4:
    return "B"
  elif score == 3:
    return "C"
  elif score == 2:
    return "D"
  else:
    return "F"


def main():
  try:
    score = int(input("Hur många poäng fick eleven?"))
    while score > 5 or score < 0:
      print("Det kan inte vara mer än 5 poäng eller mindre än 0 poäng.")
      score = int(input("Hur många poäng fick eleven?"))
    grade = getGrade(score)
    print("Eleven hade", score, "poäng och får", grade, "i betyg.")
  except ValueError:
    print("Bara heltal mellan 0 till 5 är tillåtna.")
    main()
  except KeyboardInterrupt:
    print()
    print("Om du vill lämna programmet, tryck ^D")
    main()
  except EOFError:
    print()
    print("Hej då!")
  except:
    print("oj, något blev fel, hej då!")


main()
