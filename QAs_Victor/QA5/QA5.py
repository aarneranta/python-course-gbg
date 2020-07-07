from math import sqrt

def getNumbers():
    nums = [] # start with an empty list
    # sentinel loop to get numbers
    xStr=input("Enter a number (<Enter> to quit)>>")
    while xStr != '':
        x = float(xStr)
        nums.append(x) # add this value to the list
        xStr = input("Enter a number (<Enter> to quit )>>")
    return nums


'''
11.1 och 11.2.3 från boken,
beräkna medelvärde och standardavvikelse av en lista av tal.
'''
def mean(xs):
    #Alt1:
    total=0.0
    for x in xs:
        total=total+x
    return total/len(xs)

    #Alt2:
    #return sum(xs)/len(xs)

def stddev(xs,xbar):
    #Alt 1:
    sumDevSq = 0.0
    for num in xs:
        dev = xbar-num
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(xs)-1))

    #Alt 2:
    #return sqrt(sum([(xbar-x)**2 for x in xs])/(len(xs)-1))
print(stddev([1,2,3,4], mean([1,2,3,4])))
def median(xs):
    #Alt 1:
    xs.sort()
    size = len(xs)
    midPos = size // 2
    if size % 2 == 0:
        med = (xs[midPos]+xs[midPos-1]) / 2
    else:
        med = xs[midPos]
    return med

    #Alt 2:
    #xs.sort()
    #return (xs[len(xs)//2]+xs[(len(xs)//2)-1])/2 if len(xs) % 2 == 0 else xs[len(xs)//2]

#print(median([1,2,3]))


'''
Egna exempel (inte från boken) med split() och strip().
'''
##
def split_strip_training():
    string = "Ett, två, tre, fyra, fem."
    print(string)

    string = string.split()
    print(string)

    string.append('!')
    print(string)

    string = ".".join(string)
    print(string)

    string = " \n"+string+" "
    print(string)

    print(string.rstrip())
    print(string.lstrip())
    print(string.strip())

    string2="Ett, två, tre, fyra, fem."
    print(string2)

    string2 = string2.split(',')
    print(string2)

    string2=[s.lstrip() for s in string2]
    print(string2)

##


'''
Lambda och sortering.
'''
##
def lambda_sorting_training():

    print(sorted([5,3,6,45,100]))

    print(sorted(['banan','äpple','apelsin'],key=lambda x: -len(x)))

    f1 = lambda x : x * 2

    f2 = lambda x : x ** 2

    f3 = lambda x,y: [x,y]

    # f(6,4) -> [6,4]
    #sort([6,4]) -> [4,6]

    print(f3(f1(3),f2(2)).sort())  ## alt 1 returnerar??
    print(sorted(f3(f1(3),f2(2)))) ## alt 2 returnerar??

    f4 = lambda x : sorted(x[:len(x)//2])

    f5 = lambda x,y,z : [i for i in range(x+1) if i % (y+z) == 0]

    f6 = lambda x,y: [x[i]*y[i] for i in range(len(x))]

##

#Kap 11 Övn 6
def swap(i,j,myList):
    tmp=myList[i]
    myList[i] = myList[j]
    myList[j] = tmp
    return myList

def shuffle(myList):
    from random import randint
    for i in range(len(myList)):
        myList=swap(i,randint(0,len(myList)-1),myList)
    return myList
