# symbolic.py, extra assignment for Python course

#########################################################################
### part 1: derivatives of polynomials and more general expressions #####
#########################################################################

# a polynomial is a list of coefficients for each power of x, starting from x^0 in ascending order

# derivative: each ax^n becomes anx^(n-1); polynomial [1,2,3] becomes [2,6]
def deriv_polynom(p): # TODO: return the derivative polynomial of p
    print("deriv_polynom TODO")


# the class of abstract syntax trees of expressions
class Exp: # given: don't change
    
    def __init__(self,op,args):
        self.op = op
        self.args = args
        
    def parts(self):
        return self.op, self.args


# shorthands for defining expression trees
def app(op,x,y): # TODO: shorthand for building an Exp from a binary operator application
    print("app TODO")

def add(x,y): # given: addition as an example of use of app 
    return app("+",x,y)

def mul(x,y): # TODO: multiplication as an example of use of app
    print("mul TODO")

def sub(x,y): # TODO: subtraction as an example of use of app
    print("sub TODO")

def pow(x,y):  # TODO: raising to a power as an example of use of app 
    print("pow TODO")

def const(n):  # TODO: numeric constant n as an Exp
    print("const TODO")

def var():  # TODO: variable x as an Exp
    print("var TODO")


def is_const(exp): # given: decide if an Exp is a numeric constant
    op,args = exp.parts()
    return (type(op) == int) and (not args)

def is_var(exp): # given: decide if an Exp is the variable x
    op,args = exp.parts()
    return (op == 'x') and (not args)


# recommended step 1 of simplification: convert Exp to a list of terms of the form (n,a), each representing ax^n

# this function does the main job in simplification, and needs separate cases for each operator
def simplify(exp): # TODO: convert Exp to a list of terms of the form (n,a), each representing ax^n
    op,args = exp.parts()  # given: a part of this function
    if is_const(exp):
        return [(0,op)]
    elif op == "+":
        return simplify(args[0]) + simplify(args[1])
    print("simplify TODO") # what happens if op is +. *, ^, x ?


# this function first simplifies Exp to a list of terms, then converts it to a polynomial
def exp2polynom(exp): # TODO: all the way from Exp to a polynomial
    terms = simplify(exp) # given: start with this
    powers = {}  # given: hint to use a dictionary indexed on powers
    print("exp2polynom TODO")


    
###############################################
## part 2: printing and parsing expressions ###
###############################################

# convert Exp to prefix string, e.g. (+ 2 x); separate the operator and its arguments by spaces
def show_exp_prefix(exp): # TODO: prefix printing of expressions
    print("show_exp_prefix TODO")


# convert Exp to infix string, e.g. (2 + x); separate the operator and its arguments by spaces
def show_exp_infix(exp): # TODO: infix printing of expressions
    print("show_exp_infix TODO")


# lexer applied to input string before the parser
def lex(s): # TODO: lexer for algebraic expressions, from string to token list
    print("lex TODO")


# auxiliary for parsing: return the first token if it is an expected one and move to the next token
def expect_token(expected,toks):
    if not toks:
        print("parse error: expected one of", expected, "found nothing")
    elif toks[0] in expected:
        return toks[0],toks[1:]
    else:
        print("parse error: expected one of",expected, "found", toks[0])


# parse prefix expressions e.g. (+ x 2), returning Exp,remaining_token_list
def tparse(toks):  # given as example of recursive descent parsing
  while toks:
    if toks[0] == '(':             # if the first token is '(' an operator application is expected
        toks = toks[1:]            # go to the second token
        op,toks = expect_token(["+","-","*","^"],toks) # try to find an operator
        x,toks = tparse(toks)                          # after that, parse its first argument
        y,toks = tparse(toks)                          # after that, parse its first argument
        p,toks = expect_token([')'],toks)              # make sure a closing ')' comes next
        return (Exp(op,[x,y]),toks)                    # return the operator application
    elif toks[0].isdigit():               # if the first token is a numeric constant...
        return (const(toks[0]),toks[1:])  # ...return the atomic tree
    else:
        return (var(),toks[1:])           # in all other cases, treat the first token as a variable
    


# parse infix expressions e.g. (x + 2), returning Exp, and remaining token list
def parse(toks): # TODO: recursive descent parser
    print("eparse TODO")

    
# applied on top of a parser, returning Exp if the remaining token list is empty
def top_parse(parser,toks): # TODO: parse with parser, and if no tokens remain, return tree, otherwise error
    print("top_parse TODO")


# the main function: input infix expression, show tree, polynomial, and 1st and 2nd derivatives
def main(): # given, don't change
    s = input("enter expression> ")
    toks = lex(s)
    exp = top_parse(parse,toks)
    print("tree:", show_exp_prefix(exp))
    poly = exp2polynom(exp)
    print("polynomial:", poly)
    der = deriv_polynom(poly)
    print("first derivative:", der)
    der = deriv_polynom(der)
    print("second derivative:", der)


if __name__ == "__main__":
    main()

