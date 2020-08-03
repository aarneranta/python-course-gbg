from graphics import *
from numpy import sin, cos, pi
from random import randint, uniform


height, width = 400, 400
window = GraphWin('Gas particles', width=width, height=height)

n_particles = 20
r = 3
speed = 10
animation_speed = 25

particle = [Circle((Point(randint(r, width-r), randint(r, height-r))), r) for i in range(n_particles)]
for i in range(n_particles):
    particle[i].setFill('black')

velocity = [[0, 0] for i in range(n_particles)]
for i in range(n_particles):
    angle = uniform(0, 2*pi)
    velocity[i][0] = speed * cos(angle)
    velocity[i][1] = speed * sin(angle)


def move(n, particle, velocity, window):
    for i in range(n):
        particle[i].draw(window)
        particle[i].move(velocity[i][0], velocity[i][1])

        center = particle[i].getCenter()
        x_pos = center.getX()
        y_pos = center.getY()

        if x_pos > width-r or x_pos < r:
            velocity[i][0] *= -1
        if y_pos > height-r or y_pos < r:
            velocity[i][1] *= -1

    update(animation_speed)
    for i in range(n):
        particle[i].undraw()


while window.isOpen():
    move(n_particles, particle, velocity, window)
