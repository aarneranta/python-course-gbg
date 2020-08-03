from graphics import *
from numpy import *
from random import randint

# n: antal hörn
# r: sidlängd
# x_pos, y_pos: koordinater för vänstra hörnet
# window: fönster som vi ritar i


def draw_star(n, r, x_pos, y_pos, window):
    # Vi säkerställer att n tas in på rätt sätt

    if not isinstance(n, int):
        n = int(n)

    n = abs(n)
    if n % 2 == 0:
        n += 1

    red, green, blue = randint(0, 255), randint(0, 255), randint(0, 255)
    for i in range(n):
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

for i in range(n_stars):
    p = window.getMouse()
    draw_star(n_points, 40, p.getX(), p.getY(), window)