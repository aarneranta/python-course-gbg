"""
From Chapter 4 Programming Exercise 5

Write a program that draws 5 dice on the screen depicting a straight (1, 2,
3, 4, 5 or 2, 3, 4, 5, 6).
"""
from graphics import *


# Function that creates a list of empty dice squares
def create_squares(amount):
    squares = []

    for i in range(0, amount):
        if i == 0:
            squares.append(Rectangle(Point(-300, 0), Point(-250, 50)))

        else:
            new_x = squares[i-1].getP1().getX() + 100
            squares.append(Rectangle(Point(new_x, 0), Point(new_x + 50, 50)))

    return squares


# Function that creates a list of dice dots for the empty dice squares
def add_values(numbers, empty_dice):
    positions = []
    dot_size = 3
    dot_color = 'black'
    dot_space = 12
    dots = []

    # Identify the dot positions needed for each empty dice
    for i in range(0, len(numbers)):
        if numbers[i] == 1 or numbers[i] == 3 or numbers[i] == 5:
            positions.append(empty_dice[i].getCenter())

        if numbers[i] == 2 or numbers[i] == 3 or numbers[i] == 5 or numbers[i] == 4 or numbers[i] == 5 or numbers[i] == 6:
            positions.append(Point((empty_dice[i].getCenter().getX() - dot_space), empty_dice[i].getCenter().getY() - dot_space))
            positions.append(Point((empty_dice[i].getCenter().getX() + dot_space), empty_dice[i].getCenter().getY() + dot_space))

        if numbers[i] == 4 or numbers[i] == 5 or numbers[i] == 6:
            positions.append(Point((empty_dice[i].getCenter().getX() - dot_space), empty_dice[i].getCenter().getY() + dot_space))
            positions.append(Point((empty_dice[i].getCenter().getX() + dot_space), empty_dice[i].getCenter().getY() - dot_space))

        if numbers[i] == 6:
            positions.append(Point((empty_dice[i].getCenter().getX() - dot_space), empty_dice[i].getCenter().getY()))
            positions.append(Point((empty_dice[i].getCenter().getX() + dot_space), empty_dice[i].getCenter().getY()))

    # Create the dots (circles) for all identified positions and paint them black
    for i in range(len(positions)):
        dots.append(Circle(positions[i], dot_size))
        dots[i].setFill(dot_color)

    return dots


def main():
    win = GraphWin("Dice", 640, 480)
    win.setCoords(-320, -240, 320, 240)

    numbers = 1, 2, 3, 4, 5, 6  # The dice values you want

    # Call function to create empty dice squares
    empty_dice = create_squares(len(numbers))
    # Draw the dice squares in the window
    for i in range(0, len(empty_dice)):
        empty_dice[i-1].draw(win)

    # Call function to create the dots for the empty dice squares
    dice_dots = add_values(numbers, empty_dice)
    # Draw the dice dots in the window
    for i in range(0, len(dice_dots)):
        dice_dots[i-1].draw(win)

    win.getMouse()
    win.close()


main()
