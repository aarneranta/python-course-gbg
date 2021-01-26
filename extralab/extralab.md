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
1. **Task 1**: symbolic computation on internal representations
2. **Task 2**: parsing and printing

The tasks can be done independently of each other. Completing one of the tasks is enough for mark 4 for the course, and both tasks give mark 5.


### Expression trees

A moment's reflection shows that symbolic computation would be extremely complicated if carried out directly on strings. The proper format, used in all computer algebra systems and also in compilers for
programming languages, is **trees**, also known as **abstract syntax trees** in this context.

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
In compilers, one can find more complicated classes to represent abstract syntax, but this one is enough for our purposes. Notice that the list of arguments can be empty; this is the case when we represent *atomic expressions* such as *numeric constants* and *variable symbols*. Thus the tree for representing the expression x+10 is
```
Exp('+',[Exp('x',[]),Exp(10,[])])
```
Since Exp is a recursive datatype, many of the functions needed to operate on them are *recursive functions*.



### Polynomials and derivation

Polynomials with one variable, as familiar from Lab 3, admit a simpler representation than arbitrary expressions: as lists of coefficients for each power of the variable, representing their sum. Thus the polynomial
```
2 - 3x^2 + x^3
```
can be represented by the list
```
[2, 0, -3, 1]
```
Notice that we write the list in the *ascending order* of powers, which makes it easy to relate the positions to exponents: the number at position *n* is the coefficient of *x^n*.

Polynomials represented in this way have a simple method for differentiation, corresponding to the rules
- if `f(x) = ax^n` and `n != 0`, then `f'(x) = nax^(n-1)`
- if `f(x) = ax^0`, then `f'(x) = 0`
- if `f(x) = g(x) + h(x)`, then `f'(x) = g'(x) + h'(x)`


Your first task is to define the derivation function,
```
def deriv_polynom(poly): # your task
    # return the polynomial that is the derivative f'(x) of a polynomial f(x) 
```
This should for instance satisfy
```
deriv_polynom([2,0,-3,1]) == [0,-6,3]
```



### Converting expressions to polynomials

Defining derivation for polynomials is a part of Task 1 - the easy part.
A more tricky part is the conversion of arbitrary expressions (of class `Exp`) to polynomials. To make this viable in the given timeframe, we restrict `Exp` to a few forms that can always be converted to polynomials. The set of expression is defined by the following BNF grammar:
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
- two expressions can be combined with a binary operator `x - *`, and parentheses around the combination
- an expression can be raised to a positive integer power, with parentheses around the combination

The restriction to positive integers as powers is made to guarantee a conversion to polynomials.
The addition of parentheses around all applications of a binary operator (including exponentiation) is there to help parsing; relaxing this with the standard operator precedence rules would be possible but a bit too much for this task.

As an example, the expression `(2x - 3)^4` is written
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


### Symbolic computation

In this part, you have to define the following functions:
```
  def deriv_polynom(p): ...
  # deriv_polynom([1,2,3]) == [2,6]

  def exp2polynom(exp): ...
  # exp2polynom(pow(add(var(),const(1)),const(3))) == [1, 3, 3, 1]
```
You should copy and use the class `Exp` defined above. Since no parser is assumed here, it is handy to define some helper functions to construct expressions to be able to test your code easily. The second example above uses some such functions, and you should define the following:
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
- then sort these terms by the exponent and combine terms with the same exponent (hint: using a dictionary data structure indexed on the exponent can be helpful here!)


### Parsing and printing

Parsing consists of a *lexer* and a *recursive descent parser*
```
def lex(string): # returns a list of tokens

def parse(tokens): # returns an object of class Exp
```
We will write more on how these work...

Printing for both Exp and polynomials...


### Putting it all together

A test function that takes an expression as input and shows a few things:
```
>>> test()
enter expression> ((x-10)^4)
polynomial: 10000 - 4000x + 600x^2 - 40x^3 + x^4
first derivative: -4000 + 1200x - 120x^2 + 4x^3
second derivative: 1200 - 240x + 12x^2
```
This is possible if you have completed both tasks.

We will provide a test file to help with the internals...


