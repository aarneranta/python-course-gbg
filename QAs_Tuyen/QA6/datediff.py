
# cf. book 7.7 exercises 11-13

def yearLength(year):
  if year % 400 == 0:
    return 366
  elif year % 100 == 0:
    return 365
  elif year % 4 == 0:
    return 366
  else:
    return 365


def monthLength(year, month):
  if month == 2 and yearLength(year) == 366:
    return 29
  elif month == 2:
    return 28
  elif month in [4, 6, 9, 11]:
    return 30
  else:
    return 31


def dateDays(year, month, day):
  days = 0
  for y in range(year):
    days = days + yearLength(y)
  for m in range(1, month):
    days = days + monthLength(year, m)
  return days + day


def dateDiff(year1, month1, day1, year2, month2, day2):
  diff = dateDays(year2, month2, day2) - dateDays(year1, month1, day1)
  return diff

# new stuff added for Lecture 6


def checkDate(year, month, day):
  return (0 < month <= 12) and (0 < day <= monthLength(year, month))


def getMonth(s):
  month_dict = {
      'jan': '1',
      'feb': '2',
      'mar': '3',
      'apr': '4',
      'maj': '5',
      'jun': '6',
      'jul': '7',
      'aug': '8',
      'sep': '9',
      'okt': '10',
      'nov': '11',
      'dec': '12'
  }
  return month_dict.get(s, s)


def inputDate(prompt):
  date = (input(prompt + ", format år,månad,dag: "))
  if ',' in date:
    date = date.split(',')
  elif '-' in date:
    date = date.split('-')  # [year, month, day]
  date[1] = getMonth(date[1])
  if len(date) == 3 and date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
    year, month, day = int(date[0]), int(date[1]), int(date[2])
    if checkDate(year, month, day):
      return year, month, day
    else:
      print("ogiltigt datum")
      return inputDate(prompt)
  else:
    print("försök igen, tre tal")
    return inputDate(prompt)

# end new stuff

# old versions step by step, not used in the actual main()


def inputDate1(date):
  year, month, day = eval(input("Ange " + date + " i format år,månad,dag: "))
  return year, month, day


def inputDate2(prompt):
  year, month, day = input(prompt+": ").split(',')
  return int(year), int(month), int(day)


def inputDate3(prompt):
  date = (input(prompt + ": ")).split(',')
  if len(date) == 3:
    return int(date[0]), int(date[1]), int(date[2])
  else:
    print("ogiltigt datum")
    return inputDate3(prompt)


def inputDate4(prompt):
  date = (input(prompt + ": ")).split(',')
  if (len(date) == 3
          and date[0].isdigit()
          and date[1].isdigit()
          and date[2].isdigit()):
    return int(date[0]), int(date[1]), int(date[2])
  else:
    print("ogiltigt datum")
    return inputDate4(prompt)
##########


def main():
  try:
    year1, month1, day1 = inputDate("startdatum")
    year2, month2, day2 = inputDate("slutdatum")
    print("Skillnaden är", dateDiff(year1, month1, day1, year2, month2, day2))
  except KeyboardInterrupt:
    print()
    print("om du vill lämna programmet, tryck ^D")
    main()
#   except:
#     print()
#     print("Ok, hejdå")


if __name__ == '__main__':
  main()
