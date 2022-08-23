""" Chapter 13 Programming Exercise 1
Modify the recursive Fibonacci program given in this chapter so that it prints tracing information.
Specifically, have the function print a message when it is called and when it returns.
For example, the output should contain lines like these:

Computing fib(4)
...
Leaving fib(4) returning 3

Use your modified version of fib to compute fib(10) and count how many times fib(3) is computed in the process.
"""


def fibonacci(n):
    print('Computing fib(' + str(n) + ')')
    if n <= 0:
        print("Invalid input!")
        quit()
    elif n <= 2:
        print('Leaving fib(' + str(n) + ') returning ' + str(n-1))
        return n-1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(fibonacci(3))


main()
