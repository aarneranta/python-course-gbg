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


# step 1 of simplification: convert Exp to a list of terms of the form (n,a), each representing ax^n

# hint: define an auxiliary to multiply two such lists xs and ys, so that each term in xs is multiplied by each term in ys 
def multiply_terms(xs,ys): # TODO: multiply two term lists
    print("multiply_terms TODO")


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

# convert Exp to LISP-like prefix string, e.g. (+ 2 x)
def show_exp_tree(exp): # TODO: prefix printing of expressions
    print("show_exp_tree TODO")


# convert Exp to infix string, e.g. (2 + x) if two arguments, otherwise prefix e.g. (+ 1 2 (3 * 4))
def show_exp_infix(exp): # TODO: infix printing of expressions
    print("show_exp_infix TODO")

        
# parse LISP-like tree expressions e.g. (+ x 2), returning Exp,remaining_token_list
def tparse(toks): # given as example of recursive descent parsing
    head = toks[0]
    if head == '(':
        if toks[1] in ["+","-","*","^"]:
            op = toks[1]
            x,toks = tparse(toks[2:])
            y,toks = tparse(toks)
            if toks and toks[0] == ')':
                return Exp(op,[x,y]),toks[1:]
            else:
                print("parse error: expected ) found", toks)
    else:
        return Exp(head,[]),toks[1:]


# parse infix expressions e.g. (x + 2), returning Exp,remaining_token_list
def eparse(toks): # TODO: recursive descent parser
    print("eparse TODO")

    
# applied on top of a parser, returning Exp if the remaining token list is empty
def top_parse(parser,toks): # TODO: parse with parser, and if no tokens remain, return tree, otherwise error
    print("top_parse TODO")


# applied on input string before the parser
def lex(s): # TODO: lexer for algebraic expressions, from string to token list
    print("lex TODO")


# the main function: input infix expression, show tree, polynomial, and 1st and 2nd derivatives
def main(): # given, don't change
    s = input("enter expression> ")
    toks = lex(s)
    exp = top_parse(eparse,toks)
    print("tree:", show_exp_tree(exp))
    poly = exp2polynom(exp)
    print("polynomial:", poly)
    der = deriv_polynom(poly)
    print("first derivative:", der)
    der = deriv_polynom(der)
    print("second derivative:", der)


if __name__ == "__main__":
    main()

