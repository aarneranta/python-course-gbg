# http://www.paulgraham.com/spam.html
# https://course.elementsofai.com/se/3/3

DEFAULT_PROB = 0.00001

def probTable(words):
    nwords = len(words)
    table = dict()
    for w in words:
        table[w] = table.get(w,0) + 1
    for w in table:
        table[w] = table[w]/nwords
    return table

class SpamFilter:
    def __init__(self, spam, notspam):
        self.spamTable = probTable(spam)
        self.notspamTable = probTable(notspam)
        
        wordTable = dict()
        for word in self.spamTable:
            wordTable[word] = self.spamTable[word] / self.notspamTable.get(word,DEFAULT_PROB)
        for word in self.notspamTable:
            if word not in wordTable:
                wordTable[word] = DEFAULT_PROB / self.notspamTable[word]

        self.ratioTable = wordTable

    def spamProbability(self,message):
        ratio = 1
        for word in message:
            ratio = ratio * self.ratioTable.get(word, DEFAULT_PROB)
        prob = ratio / (ratio + 1)
        return(prob)


##############
## regression
##############

def meanSquareError(prediction,examples):
    loss = 0
    for (x,y) in examples:
        loss = loss + (y - prediction(x))**2
    return loss/len(examples)

def linear(c,m):
    return lambda x: c + m*x


# partial derivative
# https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931

EPSILON = 0.00001

def descent(L,epochs,examples):
    n = len(examples)
    c = 0
    m = 0
    e = 0
    prediction = linear(c,m)
    
    while e < epochs and abs(meanSquareError(prediction,examples)) > EPSILON:

        dc = 0
        dm = 0
        for (x,y) in examples:
            dm = dm + x * (y - prediction(x))
            dc = dc +     (y - prediction(x))
        dm = -2*dm/n
        dc = -2*dc/n

        m = m - L*dm
        c = c - L*dc
        prediction = linear(c,m)
        print(c,m,abs(meanSquareError(prediction,examples)))
        e = e+1
        
    return (c,m)

def loadtxt(file):  # order of pairs in chirps.txt different from doc
    lines = open(file)
    M = []
    for line in lines:
        x,y = line.split()
        M.append([float(x),float(y)])
    lines.close()
    return M

def testRegr(filename):
    M = loadtxt(filename)
    examples = [(xy[0],xy[1]) for xy in M]
    return descent(0.01,20,examples)





