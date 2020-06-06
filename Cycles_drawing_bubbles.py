Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Drawing bubble - 3 into-circles, step = 5

point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)

# define for bubble with 3 parametres

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)

point = sd.get_point(100, 100)
buble(point=point, step=10)

# Draw 10 bubbles in line

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    buble(point=point, step=5)

# Draw 3 lines with ten bubbles

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
    point = sd.get_point(x, y)
    buble(point=point, step=5)

# 100 bubbles in different locations of the screen, by different colours

for _ in range(100):
    point = sd.random.randint(2, 10)
    step = random
    buble(point=point, step=step)

sd.pause()


