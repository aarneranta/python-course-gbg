# Chapter 7 Programming Exercise 7
#
# A babysitter charges 150 SEK an hour until 21:00 when the rate drops to 100 SEK an hour (the children are in bed).
# Write a program that accepts a starting time and ending time in hours and minutes and calculates the total
# babysitting bill. You may assume that the starting and ending times are in a single 24-hour period.
# Partial hours should be appropriately prorated.
import datetime


def prompt_time(mode):
    user_time = input('Please enter the ' + mode + ' time(HH:MM): ').split(':')
    try:
        return datetime.timedelta(hours=int(user_time[0]), minutes=int(user_time[1]))
    except ValueError:
        print('Invalid input format!')
        return prompt_time(mode)
    except IndexError:
        print('You only entered the hour!')
        return prompt_time(mode)


def calculate_bill(start_time, end_time):
    break_point = datetime.timedelta(hours=21, minutes=00)
    seconds_to_hours = 3600
    higher_wage = 150
    lower_wage = 100

    # If the babysitting shift starts before 21:00 but ends after 21:00
    if start_time < break_point < end_time:
        higher_wage_time = (break_point - start_time).total_seconds()/seconds_to_hours
        lower_wage_time = (end_time - break_point).total_seconds()/seconds_to_hours
        bill = (higher_wage_time * higher_wage) + (lower_wage_time * lower_wage)
        return bill

    # If the shift starts and ends after 21:00 (because of the if-statement in main() we have assured that ending time
    # is later than starting time)
    elif start_time >= break_point:
        wage_time = (end_time - start_time).total_seconds()/seconds_to_hours
        bill = wage_time * lower_wage
        return bill

    # If the shift starts and ends before 21:00 (because of the if-statement in main() we have assured that ending time
    # is later than starting time)
    elif end_time <= break_point:
        wage_time = (end_time - start_time).total_seconds()/seconds_to_hours
        bill = wage_time * higher_wage
        return bill

    else:
        return 'We missed something'


def main():

    start_time = prompt_time('starting')  # We ask the user for a start time until it is valid input
    end_time = prompt_time('ending')  # We ask the user for a end time until it is valid input

    if start_time > end_time:
        print('Starting time needs to be earlier than ending time! Please try again.')
    else:
        print('The total babysitting bill is:', calculate_bill(start_time, end_time), 'SEK.')

    main()












main()