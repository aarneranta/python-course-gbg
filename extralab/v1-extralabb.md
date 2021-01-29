# Extra Assignment: Symbolic Computation

*Preliminary version: to be completed before official start!*

Aarne Ranta 2021

## The task

Symbolic computation is computation with mathematical expressions, instead of numbers. The result is a simple **computer algebra system**.

Typical examples of symbolic computation include:
- **symbolic derivation**: convert the polymonial `x^2 + 3x + 1` to `2x + 3`
- **simplification**: convert `(x+1)^3` to the polynomial form `x^3 + 3x^2 + 3x + 1`

(We use the operator `^` for exponentiation, as is customary for mathematical text processing systems such as LaTeX.)

In this assignment, we will do both these things. In addition, we will need
- *parsing*: convert a string to an internal data object that represents expressions in a way that supports symbolic computation.
- *printing*: convert the internal representation back to a user-readable string.

The task can be conveniently divided into two subtasks:
1. **Task 1**: symbolic computation on internal representations (abstract syntax trees)
2. **Task 2**: parsing and printing

The tasks can be done independently of each other. Completing one of the tasks is enough for mark 4 for the course, and both tasks give mark 5.



### Polynomials and derivation

Polynomials with one variable, as familiar from Lab 3, admit a simple internal representation: as lists of coefficients for each power of the variable, representing their sum. Thus the polynomial
```
2 - 3x^2 + x^3
```
can be represented by the list
```
[2, 0, -3, 1]
```
Notice that we write the list in the *ascending order* of powers, which makes it easy to relate the positions to exponents: the number at position *n* is the coefficient of *x^n*.

Polynomials represented in this way have a simple method for differentiation, corresponding to the rules
- if `f(x) = ax^n`, then `f'(x) = nax^(n-1)` (which becomes 0 if `n = 0`)
- if `f(x) = g(x) + h(x)`, then `f'(x) = g'(x) + h'(x)`


Your first task is to define the derivative of polynomials,
```
def deriv_polynom(poly): # your task
    # return the polynomial that is the derivative f'(x) of a polynomial f(x) 
```
This should for instance satisfy
```
deriv_polynom([2,0,-3,1]) == [0,-6,3]
```

### Arbitrary expressions and abstract syntax trees

Algebraic expressions in general need not be polynomials, but can be formed by the operators in arbitrary ways. An example is
```
(x + 1)^3
```
which can, however, be *simplified* to a polynomial,
```
1 + 3x + 3x^2 + x^3
```
The simplification process is another task that we address in this assignment:
```
def exp2polynom(exp): # your task
    # convert arbitrary expressions to polynomials
```
What is the internal representation of arbitrary expressions? A moment's reflection shows that simplification (and indeed all symbolic computation) would be extremely complicated if carried out directly on strings. The proper format, used in computer algebra systems and also in compilers for programming languages, is **trees**, also known as **abstract syntax trees** when representing the structure of expressions.

In Python, we can implement abstract syntax trees as a class with two variables: an **operator** and its **argument list**. The arguments in the list are expected to be expression trees themselves, which means that trees are a **recursive data structure**.

In this assignment, we will assume that you use the following class for expressions:
```
class Exp: # given: just copy this class to your code

    def __init__(self,op,args):
        self.op = op
        self.args = args

    def parts(self):
        return self.op, self.args
```
Thus an expression consists of an *operator* and a list of *arguments*.
The operator could be a Python object of any type, but we will assume it to be either a string or an integer.
The arguments will be assumed to be Exp objects themselves.
In compilers, one can find more complicated classes to represent abstract syntax, usually posing more restrictions on valid expressions. 
But this simple Exp class is enough for our purposes. 

Notice that the list of arguments can be empty; this is the case when we represent *atomic expressions* such as *numeric constants* and *variable symbols*. Thus the tree for representing the expression
```
(x+1)^3
```
is give by
```
Exp('^',[Exp('+',[Exp('x',[]),Exp(1,[])]),Exp(3,[])])
```
A more graphical way of representing it is as a graph looking like an upside-down tree, where the op parts are *nodes* and each argument tree is a *branch*:
```
        ^
      /   \
     +     3
   /   \
  x     1
```
Since Exp is a recursive datatype, many of the functions needed to operate on Exp are *recursive functions*.



### Converting expressions to polynomials

Defining the derivation of polynomials is a part of Task 1 - the easy part.
A more tricky part is the conversion of arbitrary expressions (of class `Exp`) to polynomials. To make this viable in the given timeframe, we restrict `Exp` to a few forms that can always be converted to polynomials. This set of expression is defined by the following BNF grammar:
```
<exp> ::= <int>
<exp> ::= x
<exp> ::= ( <exp> <op> <exp> )
<exp> ::= ( <exp> ^ <int> )
<op>  ::= + | - | *
<int> ::= 0 | 1 | 2 | ... | 123 | ...
```
In other words,
- expressions are built from positive integer literals and the variable `x`
- two expressions can be combined with a binary operator `+`, `-`, or `*`, with parentheses around the combination
- an expression can be raised to a positive integer power, with parentheses around the combination

The restriction to positive integers as powers is made to guarantee that the conversion to polynomials always works. 
The division operator is left out for the same reason.

The addition of parentheses around all applications of a binary operator (including exponentiation) is there to help parsing; relaxing this with the standard operator precedence rules would be possible but a bit too much for this lab.

Since extra parentheses is required by the grammar, the expression `(2x - 3)^4` is written
```
(((2*x)-3)^4)
```
Its conversion to a polynomial is
```
81 - 216x + 216x^2 - 96x^3 + 16x^4
```
in the internal list representation
```
[81, -216, 216, -96, 16]
```

## The implementation

You should write a python file `symbolic.py` that contains functions explained below. It can also contain some extra helper functions, but you are not allowed to import any libraries; as usual, you would be likely to find libraries that solve the whole problem for you, which is not what we want here.

To help you in this task, we have created a stub file `symbolic.py`, which you can edit further.

Continuously with working on your file, you should run a test file, which reports errors. 
When all tests pass, the run looks like this:
```
  $ python3 test_symbolic.py 
  TESTING PART 1
  PART 1 OK
  TESTING PART 2
  PART 2 OK
```
If you do both parts, you can moreover run your file with arbitrary input and demonstrate useful things with the `main` function given in `symbolic.py`:
```
  $ python3 symbolic.py 
  enter expression> ((x + 5)^8)
  tree: (^ (+ x 5) 8)
  polynomial: [390625, 625000, 437500, 175000, 43750, 7000, 700, 40, 1]
  first derivative: [625000, 875000, 525000, 175000, 35000, 4200, 280, 8]
  second derivative: [875000, 1050000, 525000, 140000, 21000, 1680, 56]
```

### Part 1: symbolic computation

In this part, you have to define the following functions:
```
  def deriv_polynom(p): ...
  # deriv_polynom([1,2,3]) == [2,6]

  def exp2polynom(exp): ...
  # exp2polynom(pow(add(var(),const(1)),const(3))) == [1, 3, 3, 1]
```
You must use the class `Exp` as defined above. Since no parser is assumed in Part 1, it is handy to define some helper functions to construct expressions to be able to test your code easily. The second example above uses some such functions, and you should define the following:
```
def app(op,x,y):
    return Exp(op,[x,y])

def add(x,y):
    return app("+",x,y)
 # and so on for all binary operators: add, sub, mul, pow

def var():
    return Exp("x",[])

def const(n):
    return Exp(int(n),[])
```
The `exp2polynom()` function itself is a recursive function that can call helper functions. For instance, it can be helpful to
- first simplify the expression to a sum of terms of the form `ax^n`
- then sort these terms by the exponent and combine terms with the same exponent (hint: using a dictionary data structure indexed on the exponent has proven helpful!)


### Part 2: printing and parsing

We start with the easier part: printing, i.e. conversing Exp trees into strings.
The above BNF grammar defines *infix* strings, where binary operators are put between their two arguments.
```
# convert Exp to infix string, e.g. (2 + x); separate the operator and its arguments by spaces
def show_exp_infix(exp): 
    print("show_exp_infix TODO")
```
Spaces are required for a more readable output and also to simplify testing.

Another way of printing is as *prefix* strings, where operators are put before their arguments.
```
# convert Exp to prefix string, e.g. (+ 2 x); separate the operator and its arguments by spaces
def show_exp_prefix(exp): 
    print("show_exp_prefix TODO")
```
This output is often shown to make the tree structure explicit in a systematic way.
It is also the notation used in the programming language LISP created in the 1950s: the idea was that programmers should write directly in abstract syntax to make the language easier to compile!


Converting string input into an Exp tree is divided to a *lexer* and a *parser*
```
def lex(string): # returns a list of tokens

def parse(tokens): # returns an object of class Exp
```
The lexer works very much the same way as tokenization in Lab 1.
It scans strings to find tokens of the following kinds:
- operators `+ - * ^`
- parentheses `( )` 
- positive integer literals (sequences of digits), e.g. `1987`
- the variable `x`
- spaces are allowed anywhere except inside integer literals, but not included in the token list returned

Characters other than these should stop the process and report a *lexer error*. 
It is enough just to print an error message and return an empty list of tokens.

Since the lexer is familiar from Lab 1, just simpler, it should be an easy task.
But the parser requires much more thinking.
The simplest way to implement it is by the method of *recursive descent*, which builds an `Exp` tree by building subtrees and combining them in ways that depends on the tokens seen.
The parser returns both an `Exp` and a list of remaining tokens, i.e. the tokens that the parser should continue with.
The simplest case is a parser that just checks if the first token belongs to a list of expected tokens:
```
# auxiliary for parsing: return the first token if it is an expected one and move to the next token
def expect_token(expected,toks):
    if not toks:
        print("parse error: expected one of", expected, "found nothing")  # expects at least one token
    elif toks[0] in expected:
        return toks[0],toks[1:]        # finds an expected token, returns it, and move to next item
    else:
        print("parse error: expected one of",expected, "found", toks[0])  # found some other token
```
As a more complex example, the stub `symbolic.py` provides a parser for prefix expressions:
```
# parse prefix expressions e.g. (+ x 2), returning Exp,remaining_token_list
def tparse(toks):  # given as example of recursive descent parsing
  while toks:
    if toks[0] == '(':           # if the first token is '(' an operator application is expected
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
```
Your task is to write the corresponding function for infix expressions,
```
# parse infix expressions e.g. (x + 2), returning Exp, and remaining token list
def parse(toks): # TODO: recursive descent parser
    print("parse TODO")
```
To complete the task, we need a top parser function, which takes a parser (a function from token lists to pairs of expressions and remaining tokens) and returns an expression, *provided that the list of remaining tokens is empty*. 
Thus it will for instance reject the result of parsing `(x + 2))`, which as an extra parentheses at the end.
```
# applied on top of a parser, returning Exp if the remaining token list is empty
def top_parse(parser,toks): # TODO: parse with parser, and if no tokens remain, return tree, otherwise error
    print("top_parse TODO")
```



