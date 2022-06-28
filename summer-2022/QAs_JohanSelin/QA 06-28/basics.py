# Variables
# Functions
# Types
# if statements
# loops

########### VARIABLES ###########
# A variable is like a container we can put something in.

a = 1
b = 2
c = a + b

d = 'Hello'
e = 'World!'
my_hello_world_string = d + ' ' + e


# ########### FUNCTIONS ###########
# Like a mathematical function: f(x) = 1 + x
# if we supply f with a value of 3 three we get f(3) = 1 + 3.
# We say that the function f has one parameter called x
def my_function(x):
    return 1 + x


# A function can have multiple parameters, separated by commas
def sum_three_numbers(x, y, z):
    x = x + 10
    y = y + 10
    z = z + 3
    return x + y + z


# Or zero parameters
def h():
    print('Hello World')


########### TYPES ###########
# Different objects can have different types.
# Some operations will only work on some types.
print(type(1))  # int
print(type(1.0))  # float
print(type('Hello'))  # string
print(type([1, 2, 3]))  # list

print(1 + 2)
# print(1 + '2')  # Not possible! We can not add an object of type int with an object of type string
print('Hello' + 'World')
print([1, 2, 3] + [4, 5, 6])


# ########### IF STATEMENTS ###########
# If statements change the flow of the program.
# You can imagine it like a fork in the road.
my_number = input('Enter a number > ')
my_number = int(my_number)
if my_number > 0:
    print('My number is positive')
elif my_number < 0:
    print('My number is negative')
else:
    print('My number is 0')


########### LOOPS ###########
# We want to do something more than once.
# In that case we create a loop
for i in range(10):
    print('Hello')

# Maybe we don't know how long we want to do something?
# Then we can use a while-loop
i = 5
while i > 0:
    print(i)
    i = i - 1  # if we don't change the value of i, then the loop will continue forever

# We can also exit loops using the keyword 'break'
i = 3
while True:  # Will loop forever unless we break it
    print(i)
    if i < -2:
        break
    i -= 1

