#Kap 7 Övn 1
def calculate_payment():
    inp=input("Input the number of hours worked and the hourly rate as: hw,hr:").split(',')
    while not(len(inp) == 2 and inp[0].isdigit() and inp[1].isdigit()):
        inp=input("Incorrect! input: hw,hr:").split(',')
    hw=int(inp[0])
    hr=int(inp[1])
    if hw > 40:
        ot=hw-40 #overtime
        return ot*1.5*hr + (hw-ot) * hr
    else:
        return hw*hr


#print(calculate_payment())

#Kap 7 Övn 8
def check_eligibility():
    age=input("Enter your age: ")
    while not age.isdigit():
        age=input("Enter your age with digits: ")
    years=input("Enter how many years you have lived in the US: ")
    while not years.isdigit():
        years=input("Enter how many years you have lived in the US with digits: ")
    age=int(age)
    years=int(years)
    r=False
    s=False
    if age >= 25 and years >= 7:
        r=True
    if age >= 30 and years >=9:
        s=True
    print("You are elegible to become: {}".format("senator and representative" if (r and s) else "representative" if r else "Nothing"))
#check_eligibility()

#Kap 8 Övn 1
def fib():
    n=input("Enter the n'th fib number: ")
    while not n.isdigit():
        n=input("Enter your age with digits: ")
    n=int(n)
    fib_n=1
    fib_n_minus1=1
    for i in range(n-2):
        tmp = fib_n
        fib_n = fib_n + fib_n_minus1
        fib_n_minus1 = tmp
    print(fib_n)
#fib()


#Kap 8 Övn 2
def windchill_values():
    formula = lambda V,T: 35.74+0.6215*T-35.75*(V**0.16)+0.4275*T*(V**0.16)
    f_to_c = lambda f: ((f-32)*5)/9
    [print(str(T).rjust(6),end='') for T in range(-20,60+1,10)] #För att printa ut "headers"
    for V in range(0,50+1,5):
        print()
        print(V,end='') #För att printa ut "headers"
        for T in range(-20,60+1,10):
            print("{:.1f}".format(f_to_c(formula(V,T))).rjust(6),end='')
#windchill_values()


# Kap 8 Övn 4
def syr():
    n=input("input an integer")
    while not n.isdigit():
        n=input("Input an integer:")
    n=int(n)
    while n != 1:
        print("{} ".format(n), end='')
        if n % 2 == 0:
            n=n//2
        else:
            n=3*n+1
    print(n)
#syr()


# Kap 8 Övn 5

def is_prime(n):
    from math import sqrt
    for x in range(2,int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True
#print(is_prime(6))

# Kap 8 Övn 6

def get_primes(n):
    primes=[]
    for i in range(2,n+1):
        if is_prime(i):
            primes.append(i)
    return primes
#print(get_primes(100))
