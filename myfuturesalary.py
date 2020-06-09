# file myfuresalary.py

amount = 21000
incr = 2
years = 5   
for y in range(1,years+1):
    amount = amount * (1 + incr/100)
    print("år",y,":",amount)

