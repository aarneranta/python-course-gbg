# file yoursalary.py

"An interactive program that computes information about the user's salary"

def future():
    "computes the future development of the salary"
    salary = int(input("nuvarande lön: "))
    incr = float(input("årlig ökning i procent: "))
    years = int(input("hur många år vill du se? "))
    
    for y in range(1,years+1):
        salary = salary * (1 + incr/100)
        print("år",y,":",salary)

def remaining():
    "computes how much is left after tax and rent"
    salary = int(input("bruttolön: "))
    taxrate = int(input("skatteprocent: "))
    rent = int(input("hyra: "))

    tax = salary*taxrate/100
    net = salary - tax
    print("efter skatt: ", net)
    print("kvar efter skatt och hyra: ",net - rent)

def main():
    "guides the user to select different types of information requests"
    mode = str(input("löneutveckling (u) eller kvar efter skatt och hyra (k): "))
    if mode == "u":
        future()
    elif mode == "k":
        remaining()
    else:
        print("var god svara u eller k")

main()



