wholeyears = 2019-1964
days_in_wholeyears = wholeyears * 365 + 14
days_in_firstyear = 20 + 3 * 30 + 4 * 31
days_in_lastyear = 6 * 31 + 3 * 30 + 29
age = days_in_wholeyears + days_in_firstyear + days_in_lastyear

print("exakt", age, "dagar")
print("ungefär", age/365, "år")
