from graphics import *
from numpy import *
from random import randint

# n: number of corners
# r: side length of star
# x_pos, y_pos: coordinates for leftmost corner
# window: the graphics window to draw in


def draw_star(n, r, x_pos, y_pos, window):
    
    # Check so that n is received as an integer
    if not isinstance(n, int):
        n = int(n)

    # If for some reason n was negative, now it is not
    n = abs(n)
    if n % 2 == 0:
        n += 1

    # Random colours for some sparkle to the stars
    red, green, blue = randint(0, 255), randint(0, 255), randint(0, 255)
    for i in range(n):
        # Decides where the next position is. Some basic trigonometry to decide the corners
        x_pos2 = (x_pos + r * (cos(i * (n-1)*pi/n)))
        y_pos2 = (y_pos + r * (sin(i * (n-1)*pi/n)))

        line_segment = Line(Point(x_pos, y_pos), Point(x_pos2, y_pos2))
        line_segment.setFill(color_rgb(red, green, blue))
        line_segment.draw(window)
        update(10)

        x_pos, y_pos = x_pos2, y_pos2


n_stars = int(input('Number of stars:'))
n_points = input('Number of points (odd, otherwise converted to odd number):')

window = GraphWin('Stars', width=400, height=400)

# Draw several stars! Click on the graphics window and they will appear
for i in range(n_stars):
    p = window.getMouse()
    draw_star(n_points, 40, p.getX(), p.getY(), window)
