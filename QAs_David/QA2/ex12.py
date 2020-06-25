# Write a function that checks whether a date is valid or not

def main():
    datestring = input("Enter the date on the form YYYY-MM-DD: ")

    year, month, day = datestring.split("-")
    year = int(year)
    month = int(month)
    day = int(day)

    if dateIsValid(year, month, day):
        print("Real date, good job :)")
    else: 
        print("This is not a real date, is it your first time dating?")


def dateIsValid(y, m, d):
    if d <= 0 or m <= 0 or m > 12:
        return False
    if d > monthLength(y, m):
        return False
    if y < -13700000000:
        return False
    
    return True



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


main()
