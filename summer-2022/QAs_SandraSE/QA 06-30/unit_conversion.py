# Based on Chapter 2 Programming Exercise 9-11
#
# Write a program to perform unit conversions.
# 1. Define a function converting Celsius to Fahrenheit.
# Formula: (°C x 1.8) + 32 = °F
# 2. Define a function converting Kilometers (km) to Miles.
# Formula: km x 0.62137= miles
# 3. Define a function converting SEK to USD.
# Formula: SEK x 0.1 = USD
#
# 4. Create a menu where the user gets to choose a conversion option. Make sure that the program explains what it does.
#
# 5. Allow the user to perform multiple conversions of their choice (exit the program with input (q)).

# Solution
def c_to_f(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def km_to_miles(km):
    miles = km * 0.62137
    return miles


def sek_to_usd(sek):
    usd = sek * 0.1
    return usd


def main():
    print('Hello! This is a conversion calculator.\nPress (1) to convert °C to °F\nPress (2) to convert km to '
          'miles\nPress (3) to convert SEK to USD')

    while True:
        option = input('Select an option or press (q) to exit the program: ')
        if option == '1':
            user_input = int(input('Enter a degree °C to convert to °F: '))
            print(user_input, '°C is', c_to_f(user_input), '°F.')
        elif option == '2':
            user_input = int(input('Enter a km distance to convert to miles: '))
            print(user_input, 'km is', km_to_miles(user_input), 'miles.')
        elif option == '3':
            user_input = int(input('Enter an amount in SEK to convert to USD: '))
            print(user_input, 'SEK is $', sek_to_usd(user_input),)
        elif option == 'q':
            quit()
        else:
            print('Invalid input. Try again!')


main()
