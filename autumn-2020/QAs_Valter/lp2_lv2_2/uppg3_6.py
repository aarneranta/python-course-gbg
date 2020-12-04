"""The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph
over the limit plus a penalty of $200 for any speed over 90 mph. Write a
program that accepts a speed limit and a clocked speed and either prints
a message indicating the speed was legal or prints the amount of the fine,
if the speed is illegal."""

def fine(speed_limit, speed):
    if speed <= speed_limit:
        print("Legal speed")
    else:
        fine_amount = 50
        fine_amount += 5 * (speed - speed_limit)
        if speed > 90:
            fine_amount += 200
        print("Slow down and pay", " ", fine_amount, "$", sep='')



