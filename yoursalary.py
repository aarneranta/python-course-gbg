# file yoursalary.py

def future(years, salary, incr):
    for y in range(1, years+1):
        salary = salary * (1 + incr/100)
    return salary


def main():
    salary = int(input("nuvarande lön: "))
    incr = float(input("årlig ökning i procent: "))
    years = int(input("hur många år vill du se? "))
    mode = input("vill du se utvecklingen år för år (ja/nej)?")

    if mode == "nej":
        print(future(years, salary, incr))
    elif mode == "ja":
        for y in range(1, years+1):
            print("år", y, future(y, salary, incr))
    else:
        print("var god svara ja eller nej")

main()



