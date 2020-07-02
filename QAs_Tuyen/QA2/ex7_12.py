# Write a program that accepts a date in the
# form month/day/year and out­ puts whether or
# not the date is valid. For example 24/5-1962
# is valid, but 31/9-2000 is not.
# (September has only 30 days.)


# Modified function yearLength from
# datediff.py. Returns a boolean instead
# of a number
def isLeapYear(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False


def isValidDate(date, month, year):
  # Negative years not allowed
  if year < 0:
    return False
  # Valid months between 1-12
  elif month not in range(1, 13):
    return False
  # There can be no more than 31 days in a month
  elif date > 31:
    return False
  # Apr, Jun, Sep, and Nov only have 30 days
  elif date == 31 and month in [4, 6, 9, 11]:
    return False
  # Feb 29th can only occur during leap years
  elif month == 2 and date == 29 and not isLeapYear(year):
    return False
  # All other dates are valid
  else:
    return True


def main():
  # Using eval to accept multiple values from
  # the function input at once. Using eval
  # can make your program vulnerable to attacks.
  date, month, year = eval(
      input("Please enter a date as DD,MM,YYYY to check if it is valid: "))
  print("The date {0}/{1}-{2} is {3}.".format(
      date,
      month,
      year,
      "valid" if isValidDate(date, month, year) else "invalid"
  ))
  # By returning a boolean True or False in
  # the function isValidDate, I can choose to
  # print different strings depending on the
  # boolean. Had I returned the string immediately
  # in the function isValidDate, it would have
  # required me more effort changing what I want
  # to print afterwards. For example, I could write
  print("The date {0}/{1}-{2} is {3}.".format(
      date,
      month,
      year,
      "working" if isValidDate(date, month, year) else "not working"
  ))


main()
