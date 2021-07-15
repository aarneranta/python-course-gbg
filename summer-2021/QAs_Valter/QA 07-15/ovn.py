# List comprehensions, övning https://holypython.com/intermediate-python-exercises/exercise-16-python-list-comprehensions/

# Xbonacci
# xbonacci([1,4,2,3], 10) -> [1, 4, 2, 3, 10, 19, 34, 66, 129, 248]
import sys


def xbonacci(signature, n):
    return_list = []
    return_list.extend(signature)  # first_nums kopieras!
    to_be_summed = signature.copy()
    while len(return_list) < n:
        to_be_summed.append(sum(to_be_summed))
        to_be_summed.pop(0)
        return_list.append(to_be_summed[-1])
    return return_list

# https://pythonbasics.org/try-except/
# 3.12 med felhantering: Write a program to find the sum of the cubes of the first n natural numbers
#       where the value of n is provided by the user.
# Från QA 07-06


def main():
    # Input loop
    while True:
        try:
            n = int(input("n: "))
        except ValueError:
            print("Please enter a single integer!")
        except:
            print("Unknown error occured")
        else:
            if n < 1:
                print("n has to be a positive number!")
                continue
            else:
                break
    s = 0  # Använd ej sum som namn
    for i in range(1, n+1):
        s += i**3
    print(f"Sum of the first {n} numbers cubed is {s}")
    # Alternativt: s = sum(x**3 for x in range(1,n+1))


# 5.14 med felhantering  Word Count. A common utility on UniX/Linux systems is a small program
#                                    called wc. This program analyzes a file to determine the number of
#                                    lines, words, and characters contained therein. Write your own version of
#                                    wc. The program should accept a file name as input and then print three
#                                    numbers showing the count of lines, words, and characters in the file.
# Från QA 07-08


def main():
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print(
            f"Give one argument and one argument only. You gave {len(sys.argv)-1} arguments.")
    else:
        filename = sys.argv[1]
        nr_lines = 0
        nr_words = 0
        nr_chars = 0
        try:
            file = open(filename)
        except FileNotFoundError:
            print(f"There is no file named {filename} in this folder.")
        except:
            print("Unknown error.")
        else:
            for line in file:
                nr_lines += 1
                nr_words += len(line.split())
                nr_chars += len(line.replace(' ', '').replace('\t',
                                '').replace('\n', ''))
            print(f"Lines: {nr_lines}")
            print(f"Words: {nr_words}")
            print(f"Chars: {nr_chars}")


# Regel för stora program. Använd raise i de små funktionerna och sen try/except i main.


# Interactive calculator!

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        raise Exception('{0} is not a valid operator'.format(op))


def main():
    while True:
        user_input = input(">> ")
        if user_input == 'quit':
            break

        try:
            n1, op, n2 = parse_input(user_input)
        except Exception as e:
            print(f"Error occured when parsing input: {e}")
            continue

        try:
            result = calculate(n1, op, n2)
        except Exception as e:
            print(
                f"Error occured when trying to calculate {n1} {op} {n2}: {e}")
            continue
        print(result)


def parse_input(user_input):
    input_list = user_input.split()
    if len(input_list) != 3:
        raise Exception('Input does not consist of three elements')
    n1, op, n2 = input_list
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        raise Exception("The first and third input value must be numbers")
    return n1, op, n2
