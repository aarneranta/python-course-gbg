# binary conversion and other math functions for lecture 3

import math

def bin2dec(bin):
    dec = 0
    for b in range(len(bin)):
        dec = dec + (2**(len(bin)-b-1)) * int(bin[b])
    return dec
def dec2bin(dec):
    bin = ""
    while dec > 0:
        bit = str(dec % 2)
        bin = bit + bin
        dec = dec // 2
    return bin

def binTable(dec):
    for n in range(1,dec+1):
        bn = dec2bin(n)
        print(n,"\t",bn)

def testDecBin(dec):
    bin  = dec2bin(dec)
    bdec = bin2dec(bin)
    if bdec == dec:
        print(dec,bin,"OK")
    else:
        print(dec,bin,bdec,"ERROR")

def sum(n):
    s = 0
    for k in range(1,n+1):
        s = s + k
    return s

def factorial(n):
    fac = 1
    for k in range(2,n+1):
        fac = fac * k
    return fac

def precisionLoss(n,iters):
    c = n
    for i in range(iters):
        r = c/3
        c = 3*r
        print(c)

def swedish(d):
    return int(d + 0.5)

def approxPi(n):
    div = 1
    sign = 1
    pi = 0
    for k in range(n):
        pi = pi + 4/div
        sign = - sign
        div = sign * (abs(div) + 2)
    return pi

def quadraticEq(a,b,c):
    discr = b**2 - 4*a*c
    if discr < 0:
        return []
    elif discr == 0:
        return [-b/(2*a)]
    else:
        rdiscr = math.sqrt(discr)
        return [(-b - rdiscr)/(2*a), (-b + rdiscr)/(2*a)]


def multiTable(n):
    for x in range(1,n+1):
        row = ""
        for y in range(1,n+1):
            row = row + "\t" + str(x*y)
        print(row)

def hypotenuse(a,b):
    return math.sqrt(a*a + b*b)


def pythagoreans(mx):
    for c in range(mx):
        for b in range(1,c):
            for a in range(1,b):
                if a*a + b*b == c*c:
                    print(a,b,c,":",a*a,"+",b*b,"=",c*c)

def newton(r,n):
    guess = r/2
    for i in range(n):
        guess = (guess + r/guess)/2
        print(guess, "\terror:\t", math.sqrt(r)-guess)
    return guess


######### for later use

def quicksort(xs):
    if xs:
        pivot = xs[0]
        return (quicksort([x for x in xs[1:] if x <= pivot])
              + [pivot]
              + quicksort([x for x in xs[1:] if x > pivot]))
    else:
        return xs
