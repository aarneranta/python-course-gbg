
# sentinel loop
def epidemic1():
    cases = []
    report = ""
    while report != "Epidemin är slut!":
        report = input("antal nya fall: ")
        newcases = int(report)
        cases.append(newcases)
        print("totalt", sum(cases))
        if len(cases) >= 7:
            print("sju dagars snitt", int(sum(cases[-7:])/7 + 0.5))

# post-test loop
def epidemic2():
    cases = []
    report = ""
    prompt = "antal nya fall: "
    report = input(prompt)
    while report != "Epidemin är slut!":
        newcases = int(report)
        cases.append(newcases)
        print("totalt", sum(cases))
        if len(cases) >= 7:
            print("sju dagars snitt", int(sum(cases[-7:])/7 + 0.5))
        report = input(prompt)

# loop and a half
def epidemic3():
    cases = []
    while True:
        report = input("antal nya fall: ")
        if report == "Epidemin är slut!":
            break
        newcases = int(report)
        cases.append(newcases)
        print("totalt", sum(cases))
        if len(cases) >= 7:
            print("sju dagars snitt", int(sum(cases[-7:])/7 + 0.5))

            
def main():
    epidemic3()

if __name__ == '__main__':
    main()

########## lite andra saker från föreläsningen


def if_then_else(c,a,b):
    if c:
        print("here",a)
        return a
    else:
        print("here",b)
        return b

def if_then_while(cond,a,b):
    e = cond
    c = e
    while c:
        print("here",a)
        c = False
        return a
    while not e:
        print("here",b)
        return b

def sideEffect(x):
    print("sideEffect!",x)
    return x

# increment in years
def salaryIncrement(incr,years):
    salary = 1
    year = 1
    while year <= years:
        salary = salary * (1 + incr)
        year = year + 1  # first wrote years!
    return salary

# could be done with a for loop
def salaryIncrementFor(incr,years):
    salary = 1
    for year in range(1,years+1):
        salary = salary * (1 + incr)
    return salary

# repeat until
def yearsToDouble(incr):
    salary = 1
    year = 0
    while salary < 2:
        salary = salary * (1 + incr)
        year = year + 1
    return year



