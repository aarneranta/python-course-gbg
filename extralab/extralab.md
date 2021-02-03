# Extra Assignment: Symbolic Computation

*Version 1.0 Some changes possible in the text and support files, but the task specification is now final.*

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
- 'a ^ b' (exponentiation)
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
- (*f + g*)' = *f' + g'*
- (*f - g*)' = *f' - g'*
- (*f* * *g*)' = *f'* * *g* + *f* * *g'*
- (*f / g*)' = (*f'* * *g* - *f* * *g'*)/*g* * *g*
- (*f^n*)' = (*f* * ... * *f*)'  (*f* multiplied by itself *n* times)
- *n*' = 0 for integer literals
- *x*' = 1 for the variable *x*


This is a recursive definition over expression trees.
The reason why it looks simpler than in many other sources is that we have assumed the expressions always to have *x* as their only variable.
Another simplification is that we have treated exponentiation only in the special case where the exponent is an integer.

Your first task is to define this function in Python.
The definition will look as follows:
```
def derivative(exp):
    op,args = exp.parts()
    if op == '+':
        f,g = args[:2]
        return add(derivative(f),derivative(g))
    elif op == '-':
        ....
```
The function performs **pattern matching** on the operator, calls itself on the arguments, and combines the results by using appropriate operators.
You will need one if/elif branch for each form of expression, corresponding to the seven differentiation rules stated above.
A complete example of pattern matching is shown in the `value()` function in `parse_symbolic.py`, which calculates the value of an expression for a given value of the variable `x`.
You can use the code for that function as a template for all recursive functions on expressions.

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
This is a tricky function, and we will not expect it to be defined for all expressions.
Thus we will exclude
- division (possible for some division expressions, e.g. `6*x/2`, but not in general)
- exponentiation with other than non-negative integer powers

When it comes to division, our differentiation function still gives a result, but this is in general not a polynomial.

The `exp2polynom()` function is of course a recursive function.
It can be convenient to make it call helper functions.
In particular, it can be helpful to
- first simplify the expression to a sum of terms of the form `ax^n`, represented as a list of pairs `(n,a)`
- then sort these terms by the exponent and combine terms with the same exponent (hint: using a dictionary data structure indexed on the exponent has proven helpful!)

The first step can be implemented by pattern matching on the operator just like differentiation.
But we leave it to you to decide what kind of rules exactly to apply.
As an example, the simplification rule for addition may look as follows, if you follow the advice of returning a list of pairs:
```
    if op == '+':
        f,g = args[:2]
        return simplify(f) + simplify(g)
```
where the latter `+` is concatenation of lists.


### Printing expressions and polynomials

The first task is to print expressions in a "pretty" way, following the conventions of mathematical notation.
In particular, **precedences** and **associativity** should be followed.
The conventions can be specified by a BNF grammar, which is also followed by the parser given in `parse_symbolic.py`:
```
  <exp0> ::= <exp0> <op0> <exp1>
           | <exp1>
  <exp1> ::= <exp1> <op1> <exp2>
           | <exp2>
  <exp2> ::= <exp2> <op2> <exp3>
           | <exp3>
  <exp3> ::= <int>
           | x
           | ( <exp0> )
  <op0>  ::= + | -
  <op1>  ::= * | /
  <op2>  ::= ^
  <int>  ::= 0 | 1 | 2 | ...
```
The digits 0,1,2,3 in `<exp0>` etc are **precedence levels**.
They grammar uses them in a precise way to express the following rules:
- every expression has a precedence level (given by the left hand side of the BNF rule that produces it)
- an expression of a higher level can always be used on a lower level
- an expression of lower level can be used on a higher level by putting it in parentheses ()
- every binary operator has a precedence level, which is the same as the level of the expression formed with it
- every operator here is **left associative**, which means that for instance `1 + 2 + 3` is interpreted as `(1 + 2) + 3`

The parser uses the precedence levels to group expressions in intended ways.
Thus for instance
```
  2 + 3 * 4
```
is parsed like
```
  2 + (3 * 4)
```
rather than
```
  (2 + 3) * 4
```
because only this alternative is permitted by the grammar, which says that `*` has a higher precedence level than `+`.
(You are welcome to test this by following the grammar rules by pencil an paper!)
For the same reason, the optimal way to show the expression uses no parentheses.

The function to be defined,
```
def show_exp_infix(level,exp): # TODO: infix printing of expressions, minimizing parentheses
    return show_exp_prefix(exp)  # default behaviour, to be replaced
```
takes the intended precedence level as its first argument.
When applied to an entire expression, level 0 is to be used.
But in recursive calls, other levels are chosen depending on the precedence of the main operator and its arguments.
Thus for instance the rule for printing addition expressions might look like this:
```
    show_exp_infix(0,arg[0]) + ' + ' + show_exp_infix(1,arg[1])
```
But you can of course cluster the operators in some smart way so that you don't need to write separate rules for every operator.

Polynomials have a simpler grammar than arbitrary expressions:
```
  <poly> ::= -? <term>
           | <poly> <op> <term>
           | 0
	   | 1
  <term> ::= <int2>
           | <int2>? x
           | <int2>? x ^ <int2>
  <op>   ::= + | -
  <int2> ::= 2 | 3 | 4 | ...
```
The main differences from the `<exp>` grammar are:
- parentheses are not used
- multiplication signs are not used (writing `3x` instead of `3*x`)
- division is not used (because not allowed at all)
- the integers 0 and 1 are not used (`1x` and `x^1` become `x`, `0x` and `x^0` just disappear)
- but 0 is used to for printing the polynomials `[]` and `[0]`, which would otherwise become empty strings
- likewise, 1 is used for the polynomial `[1]`  
- if the first token is `+` it is omitted

Your task is to write the following function:
```
def show_polynom(p): # TODO printing polynomials given as lists of coefficients of ascending powers
    return p  # default behaviour, to be replaced
```



## The implementation

First make sure to run
```
  git clone https://github.com/aarneranta/python-course-gbg.git
```
to get the files needed in this task.
The files are in the subdirectory `extralab/`.

You should write a python file `symbolic.py` starting from the stub included in this directory.
The file imports the `parse_symbolic.py`, from which you are like to need
- `Exp`, the class of expressions
- `add(x,y), sub(x,y), mul(x,y), div(x,y), pow(x,y), const(n), var()`, shorthands for `Exp` construction
- `lex(s)`, lexer for converting strings to token lists
- `show_exp_prefix(exp)`, showing trees as prefix expressions
- `top_parse(toks)`, parsing a list of tokens to an `Exp` object

You are not allowed to import any libraries; as usual, you would be likely to find libraries that solve the whole problem for you, which is not what we want here.

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
  enter expression> (x - 1)^3
  tree: (^ (- x 1) 3)
  derivative: (1 - 0) * ((x - 1) * (x - 1)) + (x - 1) * ((1 - 0) * (x - 1) + (x - 1) * (1 - 0))
  polynomial: -1 + 3x - 3x^2 + x^3
  derivative of polynomial: 3 - 6x + 3x^2
  polynomial of derivative: 3 - 6x + 3x^2
  second derivative: -6 + 6x
```
It also shows a plot of the function, using Matplotlib in the same way as Lab3:

![Plot](https://github.com/aarneranta/python-course-gbg/blob/master/extralab/plot-exp.png)

You can use this function to run your own tests as you proceed. 
It will even work if you have only done Part 1, but printing will then use the predefined defaults, which don't look quite as nice.

