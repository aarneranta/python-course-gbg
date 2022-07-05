# Based on Chapter 3 Programming Exercise 16
#
# A Fibonacci sequence is a sequence of numbers where each successive number is the sum of the previous two.
# The classic Fibonacci sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, ....
# Write a program that computes the nth Fibonacci number where n is a value input by the user.

def fibonacci(n):
   if n <= 0:
      print("Invalid input!")
      quit()
   elif n <= 2:
      return n-1
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)


def main():
   print('Test printing initial sequence', fibonacci(1), fibonacci(2), fibonacci(3), fibonacci(4), fibonacci(5), fibonacci(6), fibonacci(7), fibonacci(8))

   user_n = int(input('Enter a natural number to calculate it\'s Fibonacci number: '))
   print('The', user_n, 'th Fibonacci number is:', fibonacci(user_n))


main()
