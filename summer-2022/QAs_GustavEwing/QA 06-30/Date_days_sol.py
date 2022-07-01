
# Tillägg till Aarnes program som kontrollerar att datumet är giltigt

def dateDiff(year1, month1, day1, year2, month2, day2):
    diff = (dateDays(year2, month2, day2) - dateDays(year1, month1, day1))
    return diff


def dateDays(year, month, day):
    days = 0
    for y in range(year):
        days = days + yearLength(y)

    for m in range(1, month):
        days = days + monthLength(year, m)

    return days + day


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


# kontrollerar att datumet är giltigt annars upprepas förfrågan
def inputDate(date):
    while True:
        year, month, day = eval(input("Ange " + date + " i format år,månad,dag: "))
        # returnerar bara om datumet är giltigt
        if isValidDate(year, month, day):
            return year, month, day
        else:
            print("Ange ett giltigt datum. ")


# kontrollerar att ett datum är giltigt
# negativa årtal räknas som giltiga eftersom koden inte tar hänsyn till dem
# använder monthLength för att få den specifika månadslängden
def isValidDate(year, month, day):
    return 0 < year and 0 < month < 13 and 0 < day <= monthLength(year, month)


def main():
    year1, month1, day1 = inputDate("startdatum")
    year2, month2, day2 = inputDate("slutdatum")
    print("Skillnaden är", dateDiff(year1, month1, day1, year2, month2, day2))


main()
