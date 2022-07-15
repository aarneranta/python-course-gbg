# From Chapter 8 Programming Exercise 3
#
# Write a program that uses a while loop to determine how long it takes for an investment to double
# at a given interest rate. The input will be an annualized interest rate,
# and the output is the number of years it takes an investment to double.
# Note: The amount of the initial investment does not matter; you can use $1.

def calculate_years(initial_investment, interest_rate):
    years = 0
    double_investment = initial_investment * 2
    yearly_increase = interest_rate + 1

    while initial_investment < double_investment:
        years += 1
        initial_investment *= yearly_increase

    return years


def main():
    try:
        initial_investment = float(input('Please enter the initial investment: '))
        interest_rate = float(input('Please enter the interest rate: '))
        print('It will take', calculate_years(initial_investment, interest_rate), 'year(s) to double your investment.')
    except ValueError:
        choice = input('Invalid input! Try again? (yes/no): ')
        if choice == 'yes':
            main()
        else:
            quit()


main()
