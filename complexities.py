import time
import matplotlib.pyplot as plt

def linsearch(x,ns):
    counter = 0
    for n in ns:
        if n == x:
            return counter
        else:
            counter += 1
    raise ValueError

# book pp. 462-463
def binsearch(x,ns):
    low = 0
    high = len(ns)-1
    while low <= high:
        mid = (low + high)//2
        item = ns[mid]
        print(item)
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    raise ValueError

def testSearch():
    Xl = []
    Yl = []
    Xb = []
    Yb = []
    for m in range (1,11):
        
        limit = m * 1000000
        start = time.process_time()
        linsearch(limit,range(limit+1))
        end = time.process_time()
        Xl.append(m)
        Yl.append(end-start)
        
        limit = m * 1000000
        start = time.process_time()
        binsearch(limit,range(limit+1))
        end = time.process_time()
        Xb.append(m)
        Yb.append(end-start)
        
    plt.plot(Xl,Yl,'ro',color = 'red')
    plt.plot(Xb,Yb,'ro',color = 'blue')
    plt.show()

    
def permutations(xs):
    "return the list of all permutations"
    if len(xs) < 2:
        return [xs]
    else:
        ps = []
        for qs in permutations(xs[1:]):
            for j in range(len(xs)):
                p = (qs[:j] + [xs[0]] + qs[j:])
                ps.append(p)
        return ps

    
def permutationSort(xs):
    "the worst imaginable sorting function"
    def sorted(ys):
        for i in range(len(ys)-1):
            if ys[i] > ys[i+1]:
                return False
        return True
    
    for p in permutations(xs):
        if sorted(p):
            return p

        
def quickSort(xs):
    if xs:
        pivot = xs[0]
        return (
           quickSort([x for x in xs[1:] if x < pivot]) + [pivot] +
           quickSort([x for x in xs[1:] if x >= pivot])
           )
    else:
        return xs

def fileWords(filename):
    file = open(filename)
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
    file.close()
    return words

def testSort(xs,p_too = False):
    Xs = []
    Ys = []
    Xq = []
    Yq = []
    Xp = []
    Yp = []

    lxs = len(xs)
    step = max(1,lxs//10)
    print("step",step)
    
    for m in range (1,11):
 
        limit = m*step
        print("limit",limit)
        list = xs[:limit]
        
        # time standard sorted()
        start = time.process_time()
        ss = sorted(list)
        end = time.process_time()
        Xs.append(limit)
        Ys.append(end-start)

        # time quickSort()
        go_on = True
        if go_on:
            try:
                start = time.process_time()
                ss = quickSort(list)
                end = time.process_time()
                Xq.append(limit)
                Yq.append(end-start)
            except RecursionError:
                print("quickSort timed out at",limit)
                go_on = False
        
        # time permutationSort()
        if p_too and len(list) <= 10:
            start = time.process_time()
            ss = permutationSort(list)
            end = time.process_time()
            Xp.append(limit)
            Yp.append(end-start)
        
    plt.plot(Xs,Ys,'ro',color = 'green')
    plt.plot(Xq,Yq,'ro',color = 'blue')
    plt.plot(Xp,Yp,'ro',color = 'red')
    plt.show()

def tests():
    
    print("reading words from the Bible")
    ws = fileWords('data/bible.txt')
    print(len(ws), "words")

    print("testing linear search of Mary")
    print(linsearch('Mary',ws))

    print("testing binary search of Mary")
    print(binsearch('Mary',ws))

    print("ouch, must sort the list first")
    sws = sorted(ws)
    print(binsearch('Mary',sws))

    print("plotting linear and binary search with range(1M)")
    testSearch()

    print("plotting sorted() and quickSort() for up to 10k words")
    testSort(ws[:10000])

    print("counting the number of permutations of lists of given lengths")
    for i in range(10):
        print(i,":",len(permutations(list(range(i)))))
        
    print("plotting quickSort() and permutationSort() for 10 words")
    testSort(ws[:10],p_too = True)


if __name__ == '__main__':
    tests()

    
def factFor(n):
    r = 1
    for k in range(1,n+1):
        r *= k
    return r

def factWhile(n):
    r = 1
    k = 1
    while k < n+1:
        r *= k
        k += 1
    return r

def factRec(n):
    if n <= 1:
        return 1
    else:
        return n * factRec(n-1)








    


    

    


