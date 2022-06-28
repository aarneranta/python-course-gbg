# Program to calculate sum and average for non-negative integers
#
# Program should run like:
#     > 5
#     > 2
#     > 3
#     > -1         (-1 used to end input)
#     Sum = 10 Avg = 3.3333333333333335


def sum_avg_program():
    sum = 0
    amount_of_numbers_entered = 0

    while True:
        number = int(input('> '))
        if number == -1:
            break
        sum += number
        amount_of_numbers_entered += 1

    print(f'Sum = {sum}, Avg = {sum / amount_of_numbers_entered}')
    # print('Sum = ' + str(sum) + ', ' + 'Avg = ' + str(sum/amount_of_numbers_entered))


sum_avg_program()
