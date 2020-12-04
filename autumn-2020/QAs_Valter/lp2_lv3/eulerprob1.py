def prob1(upper_limit):
    """ Returns the sum of all the multiples of 3 or 5 below upper_limit """

    sum = 0
    for i in range(1, upper_limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
