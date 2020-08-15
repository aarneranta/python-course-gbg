class Tree:
    def __init__(self,node,subtrees):
        self.node = node
        self.subtrees = subtrees

    def getParts(self):
        return self.node, self.subtrees

def atom(a):
    return Tree(a,[])

def plus(x,y):
    return Tree("+",[x,y])

def times(x,y):
    return Tree("*",[x,y])

def parenth(s,ownprec,exprec):
    if ownprec < exprec:
        return "(" + s + ")"
    else:
        return s

def prefix(tree):
    f,ts = tree.getParts()
    s = str(f)
    if len(ts) == 0:
        return s
    else:
        s = s + '('
        xs = []
        for t in ts:
            xs.append(prefix(t))
        s = s + ','.join(xs) + ')'
        return(s)
    
def infix(tree,exprec):
    f,ts = tree.getParts()
    if f == "+":
        s = parenth(infix(ts[0],0) + f + infix(ts[1],1), 0, exprec)
    elif f == "*":
        s = parenth(infix(ts[0],1) + f + infix(ts[1],2), 1, exprec)
    elif len(ts) == 0:
        s = str(f)
    else:
        print("invalid syntax",f)
    return s

def postfix(tree):
    f,ts = tree.getParts()
    xs = []
    for t in ts:
        for s in postfix(t):
            xs.append(s)
    xs.append(str(f))
    return xs

def jvm(tree):
    
    def instr(f):
        if f == "*":
            return "imul"
        elif f == "+":
            return "iadd"
        else:
            return "ldc " + str(f)
        
    instrs = map(instr,postfix(tree))
        
    return '\n'.join(instrs)

def main():
    t = times(atom(3),plus(atom(4),atom(5)))
    print(prefix(t))
    print(infix(t,0))
    print(postfix(t))
    print(jvm(t))

main()








