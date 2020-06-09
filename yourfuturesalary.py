# file yourfuturesalary.py

salary = int(input("nuvarande lön: "))
incr = float(input("årlig ökning i procent: "))
years = int(input("hur många år? "))   

for y in range(1,years+1):
    salary = salary * (1 + incr/100)
    print("år",y,":",salary)

