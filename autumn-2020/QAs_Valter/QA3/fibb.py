def print_fibb(upper_lim):
    if upper_lim < 2:
        print("upper_lim should be >= 2")
    else:
        num1, num2 = 0, 1
        print(num1, num2, end=' ')
        for i in range(upper_lim-2):
            num1, num2 = num2, num1+num2
            print(num2, end=' ')
        print()
