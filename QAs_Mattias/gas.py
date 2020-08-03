from graphics import *
from numpy import sin, cos, pi
from random import randint, uniform


height, width = 400, 400
window = GraphWin('Gas particles', width=width, height=height)

n_particles = 20
r = 3
speed = 10
animation_speed = 25

# Define random locations for the particles. The interval is r to width-r for x-coordinates
# so that is doesn't get plotted hald-outside the image. Same for y-coordinates

particle = [Circle((Point(randint(r, width-r), randint(r, height-r))), r) for i in range(n_particles)]
for i in range(n_particles):
    particle[i].setFill('black')

# First just set x- and y- components of the velocity to 0
velocity = [[0, 0] for i in range(n_particles)]

# Now define some random angles for the particles to move in
for i in range(n_particles):
    angle = uniform(0, 2*pi)
    velocity[i][0] = speed * cos(angle)
    velocity[i][1] = speed * sin(angle)


# move handles particle movement and draws particles
def move(n, particle, velocity, window):
    for i in range(n):
        particle[i].draw(window)
        particle[i].move(velocity[i][0], velocity[i][1])

        center = particle[i].getCenter()
        x_pos = center.getX()
        y_pos = center.getY()

        # If the particle is outside the window, it changes direction!
        if x_pos > width-r or x_pos < r:
            velocity[i][0] *= -1
        if y_pos > height-r or y_pos < r:
            velocity[i][1] *= -1

    # Updates a certain number of times per second
    update(animation_speed)
    for i in range(n):
        # Important to undraw, otherwise the program will complain that the particle is already drawn
        particle[i].undraw()


# Run the program until the graphics window is closed
while window.isOpen():
    move(n_particles, particle, velocity, window)
