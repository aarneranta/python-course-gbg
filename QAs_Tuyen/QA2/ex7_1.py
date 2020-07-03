# Many companies pay time-and-a-half for any hours
# worked above 40 in a given week. Write a program
# to input the number of hours worked and the hourly
# rate and calculate the total wages for the week.

def countWage(hours, wage):
    if hours > 40:
        overtime = hours - 40
        total_wage = (overtime * wage * 1.5) + (wage * 40)
        return total_wage
    else:
        total_wage = wage * hours
        return total_wage


def main():
    hours_worked = eval(
        input("Hur många timmar har du jobbat den här veckan?"))
    hourly_wage = eval(input("Vad är din timlön?"))
    total_wage = countWage(hours_worked, hourly_wage)
    print("Din totala veckolön är:", total_wage)


main()
