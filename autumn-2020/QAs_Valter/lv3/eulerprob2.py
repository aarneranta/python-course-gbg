def fibb_sum(upper_limit):
    """ By considering the terms in the Fibonacci sequence whose values
        do not exceed upper_limit, find the sum of the even-valued terms. """

    sum = 0
    num1, num2 = 0, 1
    # num2 är inte jämnt, behöver inte adderas till sum

    while num2 < upper_limit:
        num1, num2 = num2, num1+num2
        if num2 % 2 == 0:
            sum += num2

    return sum
