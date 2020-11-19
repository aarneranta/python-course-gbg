
def Sigma(numbers):
    s = 0
    for n in numbers:
        s = s + n
        print(n,":",s)
    return s

# print(Sigma([]))

# print(Sigma([5,6,7]))

print(Sigma(range(1,51)))

def sumDigits(dec):
    s = 0
    for d in str(dec):
        s = s + int(d)
    return s



