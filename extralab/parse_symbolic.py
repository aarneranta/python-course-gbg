# the class of abstract syntax trees of expressions
class Exp: # given: don't change
    
    def __init__(self,op,args):
        self.op = op
        self.args = args
        
    def parts(self):
        return self.op, self.args


# shorthands for defining expression trees
def app(op,x,y): # shorthand for building an Exp from a binary operator application
    return Exp(op,[x,y])

def add(x,y): # given: addition as an example of use of app 
    return app("+",x,y)

def sub(x,y): # subtraction as an example of use of app 
    return app("-",x,y)

def mul(x,y): # multiplication as an example of use of app 
    return app("*",x,y)

def div(x,y): # multiplication as an example of use of app 
    return app("/",x,y)

def pow(x,y):  # raising to a power as an example of use of app 
    return app("^",x,y)

def var():  # variable x as an Exp
    return Exp("x",[])

def const(n):  # numeric constant n as an Exp
    return Exp(int(n),[])

def is_const(exp): # given: decide if an Exp is a numeric constant
    op,args = exp.parts()
    return (type(op) == int) and (not args)

def is_var(exp): # given: decide if an Exp is the variable x
    op,args = exp.parts()
    return (op == 'x') and (not args)


# example of pattern matching: the value of an expression for a given value of x
def value(exp,x):
    op,args = exp.parts()
    
    if is_const(exp):
        return float(op)
    elif is_var(exp):
        return float(x)

    f,g = args[:2]
    vfx = value(f,x)
    vgx = value(g,x)
    if vfx is None or vgx is None:
        return None
    if op == '+':
        return vfx + vgx
    elif op == '-':
        return vfx - vgx
    elif op == '*':
        return vfx * vgx
    elif op == '/':
        if vgx == 0:
            return None
        else:
            return vfx / vgx
    elif op == '^':
        return vfx ** vgx
    else:
        print("cannot evaluate this expression")


# lexer applied to input string before parser
def lex(s): # TODO: lexer for algebraic expressions, from string to token list
    toks = []
    while s:
        head = s[0]
        if head in "( ) [ ] x + - * ^ /".split():
            toks.append(head)
            s = s[1:]
        elif head.isspace():
            s = s[1:]
        elif head.isdigit():
            d = head
            s = s[1:]
            while s and s[0].isdigit():
                d += s[0]
                s = s[1:]
            toks.append(d)
        else:
            print("lexer error: unexpected character", head)
            return []
    return toks

# insert missing * as preprocessing between lexing and parsing
def insert_mul(toks):
    i = 0
    while i < len(toks):
        if (toks[i+1:]
             and (toks[i] in [')','x'] or toks[i].isdigit())
             and (toks[i+1] in ['(','x'])):
            toks.insert(i+1,'*')
            i += 2
        else:
            i += 1
    return toks


def expect_token(expected,toks):
    if not toks:
        print("parse error: expected one of", expected, "found nothing")
    elif toks[0] in expected:
        return toks.pop(0)
    else:
        print("parse error: expected one of",expected, "found", toks[0])


def op_level(op):
    if op in ['+','-']:
        return 0
    elif op in ['/','*']:
        return 1
    elif op in ['^']:
        return 2
    else:
        return 3


def eparse(level,toks):
    
    def eparses(level,toks):
        if not toks:
            return []
        elif op_level(toks[0]) == level:
            op = toks.pop(0)
            x  = eparse(level+1,toks)
            xs = eparses(level,toks)
            return [op,x] + xs
        else:
            return []
        
    def apps(x,xs):
        exp = x
        if xs:
            return apps(app(xs[0],exp,xs[1]),xs[2:])
        else:
            return x
        
    while toks:
        if level < 3:
            x = eparse(level+1,toks)
            xs = eparses(level,toks)
            return apps(x,xs)
        elif level == 3:
            head = toks.pop(0)
            if head == '(':
                x = eparse(0,toks)
                p = expect_token([')'],toks)
                return x
            elif head == '-': ## extra syntactic sugar, not in the grammar
                x = eparse(3,toks)
                return sub(const(0),x)
            elif head.isdigit():
                return const(head)
            else:
                return var()

            
# convert Exp to LISP-like prefix string, e.g. (+ 2 x)
def show_exp_prefix(exp): 
    op,args = exp.parts()
    if args:
        return "(" + str(op) + ' ' + ' '.join([show_exp_prefix(arg) for arg in args]) + ')'
    else:
        return str(op)            

# applied on top of a parser, returning Exp if the remaining token list is empty
def top_parse(toks): 
    exp = eparse(0,toks)
    if toks:
        print("parse error: unparsed tail",' '.join(toks))
    else:
        return exp

# bonus: printing the graph of a function

import matplotlib.pyplot as plt

def show_graph(exp):
    xyvalues = [(x/10,value(exp,x/10)) for x in range(-100,101)]
    xvalues = []
    yvalues = []
    while xyvalues:
        (x,y) = xyvalues.pop(0)
        if y is None:
            plt.plot(xvalues, yvalues)
            xvalues = []
            yvalues = []
        else:
            xvalues.append(x)
            yvalues.append(y)
    plt.plot(xvalues, yvalues)
    plt.show()
    
