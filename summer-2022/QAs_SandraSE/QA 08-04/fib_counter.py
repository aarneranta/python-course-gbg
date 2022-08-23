""" Chapter 13 Programming Exercise 2
This exercise is another variation on "instrumenting" the recursive Fibonacci program to better understand its behavior.
Write a program that counts how many times the fib function is called to compute fib(n) where n is a user input.

Hint: To solve this problem, you need an accumulator variable whose value "persists" between calls to fib.
You can do this by making the count an instance variable of an object. Create a FibCounter class with the
following methods:

__init__(self) Creates a new FibCounter, setting its count instance variable to 0.
get_count(self) Returns the value of count.
fib(self, n) Recursive function to compute the nth Fibonacci number. It increments the count each time it is called.
reset_count(self) Sets the count back to 0.
"""


class FibCounter:
    def __init__(self):
        self.count = 0

    def get_count(self):
        return self.count

    def fibonacci(self, n):
        self.count += 1

        if n <= 2:
            return n-1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def reset_count(self):
        self.count = 0


def main():
    fib = FibCounter()

    while True:
        try:
            user_input = int(input('Press (1) to calculate Fibonacci, Press (2) to reset counter, Press (3) to quit: '))
            if user_input == 1:
                number = int(input('Enter a number to calculate the Fibonacci value: '))
                if number <= 0:
                    print("Invalid input! Try again")
                else:
                    print('Fibonacci number is:', fib.fibonacci(number))
                    print('The fibonacci function was called', fib.get_count(), 'times')
            if user_input == 2:
                fib.reset_count()
                print('Counter has been reset!')
            if user_input == 3:
                print('Bye!')
                quit()

        except ValueError:
            print('Invalid input! Try again.')



main()
