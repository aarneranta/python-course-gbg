# uniq([1,2,3,2]) == [1,2,3]
def uniq(m):
    seen = {}
    out = []
    for n in m:
        if n not in seen:
            seen[n] = True
            out.append(n)
    return out

# [1,2,3].index(2) == 1
def index(m, x):
    for i in range(len(m)):
        if m[i] == x:
            return i
    return None

# index, fast vi demonstrerar enumerate
def index2(m, x):
    for i,v in enumerate(m):
        if v == x:
            return i
    return None

# inre produkt
def inner_prod(x,y):
    #tot = 0.0
    #for i in range(len(x)):
    #    tot += x[i]*y[i]
    return sum(x[i]*y[i] for i in range(len(x))) 

# Merge sort, se Wikipedia
def sort(m):
    if len(m) <= 1:
        return m
    left = sort(m[:len(m)//2])
    right = sort(m[len(m)//2:])
    result = []
    while left and right:  # minns: lista sann om icke-tom
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

import random
# Fisher-Yates shuffle, se Wikipedia
def shuffle(m):
    n = len(m)
    for i in range(n):
        j = random.randrange(i,n)
        m[i], m[j] = m[j], m[i]

