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
(x - 1)^3
```
is represented by the tree
```
        ^
      /   \
     -     3
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
  Exp('^',[Exp('-',[Exp('x',[]),Exp(1,[])]),Exp(3,[])])
```
The class is defined in the module `parse_symbolic.py`, which also defines shorthands for each form of expression.
This Exp tree can thus equivalently be built as
```
  pow(sub(var(),const(1)),const(3))
```
Yet another common way to show expression trees is as **prefix expressions**, where operators precede their arguments, and each subtree (except the leaves) is enclosed in parentheses:
```
  (^ (- x 1) 3)
```
This representation can be produced by `parse_symbolic.show_exp_prefix()`. 

The Exp class has two variables: an **operator** and its **argument list**.
The arguments in the list are expected to be Exp objects themselves, which means that trees are a **recursive data structure**.
The operator could be a Python object of any type, but we will assume it to be either a string or an integer.
If the operator is an integer literal or a variable, the list of arguments is expected to be empty.
For other operators, it is expected to contain two Exp objects.

(In literature, one can find more complicated classes to represent abstract syntax, usually posing more restrictions on valid expressions, e.g. what operators are valid. But this simple Exp class is enough for our purposes - and actually general enough for any purposes.)

Since Exp is a recursive datatype, many of the functions needed to operate on Exp are **recursive functions**.


### Symbolic differentiation

Differentiation rules are familiar from calculus text books and also stated in https://en.wikipedia.org/wiki/Differentiation_rules.
The *derivative* *e'* of an expression *e* is defined as follows.
- *n'* = 0
- *x'* = 1
- (*f + g*)' = *f' + g'*
- (*f - g*)' = *f' - g'*
- (*f* * *g*)' = *f'* * *g* + *f* * *g'*
- (*f / g*)' = (*f'* * *g* - *f* * *g'*)/*g* * *g*
- (*f^n*)' = (*f* * *f^(n-1)*)'  if *n* is a non-negative integer

This is a recursive definition over expression trees.
The reason why it looks simpler than in many other sources is that we have assumed the expressions always to have *x* as their only variable.
Another simplification is that we have treated exponentiation only in a special case, where the exponent is integer.

Your first task is to define this function in Python.
The definition will look as follows:
```
def derivative(exp):
    op,args = exp.parts()
    if op == '+':
	    f,g = args[:2]
        return add(derivative(f),derivative(g))
```
The function performs **pattern matching** on the operator, calls itself on the arguments, and combines the results by using appropriate operators.

When performed by using the recursive rules, differentiation produces very complex expressions.
For instance,
```
  (x - 1)^3 ==> (1 - 0) * ((x - 1) * (x - 1)) + (x - 1) * ((1 - 0) * (x - 1) + (x - 1) * (1 - 0))
```
by just following the rules.
This expression can of course be simplified, down to the polynomial form
```
  3 - 6x + 3x^2
```
The simplification to polynomials is our next task.


### Converting expressions to polynomials

Polynomials with one variable, as familiar from Lab 3, admit of a simple, non-recursive internal representation: as lists of coefficients for each power of the variable, representing their sum.
Thus the polynomial
```
-1 + 3x - 3x^2 + x^3
```
can be represented by the list
```
[-1, 3, -3, 1]
```
Notice that we write polynomials in the *ascending order* of powers, which makes it easy to relate the positions to exponents: the number at position *n* is the coefficient of *x^n*.

Polynomials represented in this way have a simple method for differentiation, corresponding to rules derivable from the general ones:
- *(ax^n)*' = *nax^(n-1)*   (which becomes 0 if `n = 0`)
- (*f + ... + g*)' = *f' + ... + g'*


Your second task is to define the derivative of polynomials,
```
def deriv_polynom(poly): # your task
    # return the polynomial that is the derivative f'(x) of a polynomial f(x) 
```
This should for instance satisfy
```
deriv_polynom([-1,3,-3,1]) == [3,-6,3]
```

Algebraic expressions in general need not be polynomials, but can be formed by the operators in arbitrary ways. Our example
```
(x - 1)^3
```
is a case in point. It can, however, be *simplified* to a polynomial,
```
- 1 + 3x - 3x^2 + x^3
```
The simplification process is another task that we address as the third task of this assignment:
```
def exp2polynom(exp): # your task
    # convert arbitrary expressions to polynomials
```
This is a tricky function, and we will not expect it to be defined for arbitrary expressions.
We will exclude
- division (possible for some division expressions, e.g. `6*x/2`, but not in general)
- exponentiation with other than non-negative integer powers

When it comes to division, our differentiation function still gives a result, but this is in general not a polynomial.

The `exp2polynom()` function is of course a recursive function.
It can be convenient to make it call helper functions.
In particular, it can be helpful to
- first simplify the expression to a sum of terms of the form `ax^n`, represented as pairs `(n,a)`
- then sort these terms by the exponent and combine terms with the same exponent (hint: using a dictionary data structure indexed on the exponent has proven helpful!)


### Printing expressions and polynomials

```
def show_exp_infix(level,exp): # TODO: infix printing of expressions, minimizing parentheses
    print("cannot show this expression yet")


def show_polynom(p): # TODO printing polynomials: use + or - between terms, ignore 0 terms, 1 coefficients, and * signs
    print("cannot show this polynomial yet")
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



### Part 2: printing and parsing

