# Extra Assignment: Symbolic Computation

*Preliminary version: to be completed before official start!*

Aarne Ranta 2021

## The task

Symbolic computation is computation with mathematical expressions, instead of numbers. The result is a simple **computer algebra system**.

Typical examples of symbolic computation include:
- **symbolic differentiation**: convert the polymonial `1 + 3x + x^2` to its derivative `3 + 2x`
- **simplification**: convert `(x+1)^3` to the polynomial form `1 + 3x + 3x^2 + x^3`

(We use the operator `^` for exponentiation, as is customary for mathematical text processing systems such as LaTeX.)

In this assignment, we will do both these things.
They could in principle be defined in terms of strings, such as the ones shown above, since this is what the user of the system will probably like to read and write.
However, derivation and simplification of strings directly would be complicated, and it is easier to use an internal representation of expressions as data objects that support symbolic computation better. 
Therefore, a user-friendly system also needs
- **parsing**: convert the user's string input to an internal representation,
- **printing**: convert internal representations to a user-readable strings.

Parsing would be a bit too much for this assignment and will be provided by an external module `parse_symbolic.py`.
Your task is divided into two subtasks as follows:
1. **Task 1**: symbolic computation on internal representations
2. **Task 2**: printing expressions in a nice way

The tasks can be done independently of each other. Completing one of the tasks is enough for mark 4 for the course.
Completing both tasks gives mark 5.



### Arbitrary expressions and abstract syntax trees

We will work with following forms of expressions:
- 'a + b' (addition)
- 'a - b' (subtraction)
- 'a * b' (multiplication)
- 'a / b' (division)
- 'a ^ b' (exponentiatio)
- *n* (non-negative integer literal)
- `x` (the variable x)

Expressions formed from these components naturally form **trees**, where the operators (`+ - * / ^`) are **nodes** and integer literals and variables are **leaves**.
At each node, the tree branches to two **subtrees**, which represent the arguments of the operator.

To give an example, the expression
```
(x+1)^3
```
is represented by the tree
```
        ^
      /   \
     +     3
   /   \
  x     1
```
The Python representation we use for expression trees is the class
```
class Exp:
    def __init__(self,op,args):
        self.op = op
        self.args = args
    def parts(self):
        return self.op, self.args
```
by means of which the example can be constructed as
```
  Exp('^',[Exp('+',[Exp('x',[]),Exp(1,[])]),Exp(3,[])])
```
The class is defined in the module `parse_symbolic.py`, which also defines shorthands for each form of expression.
This Exp tree can thus equivalently be built as
```
  pow(add(var(),const(1)),const(3))
```
The Exp class has two variables: an **operator** and its **argument list**.
The arguments in the list are expected to be Exp objects themselves, which means that trees are a **recursive data structure**.
The operator could be a Python object of any type, but we will assume it to be either a string or an integer.
If the operator is an integer literal or a variable, the list of arguments is expected to be empty.
For other operators, it is expected to contain two Exp objects.

(In literature, one can find more complicated classes to represent abstract syntax, usually posing more restrictions on valid expressions, e.g. what operators are valid. But this simple Exp class is enough for our purposes - and actually general enough for any purposes.)

Since Exp is a recursive datatype, many of the functions needed to operate on Exp are **recursive functions**.


### Symbolic differentiation



### Converting expressions to polynomials

Polynomials with one variable, as familiar from Lab 3, admit a simple internal representation: as lists of coefficients for each power of the variable, representing their sum.
Thus the polynomial
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


Your second task is to define the derivative of polynomials,
```
def deriv_polynom(poly): # your task
    # return the polynomial that is the derivative f'(x) of a polynomial f(x) 
```
This should for instance satisfy
```
deriv_polynom([2,0,-3,1]) == [0,-6,3]
```

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
This is a tricky function...


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

These are given in `parse_symbolic.py`


