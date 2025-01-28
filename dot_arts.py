import random
import turtle as t
from turtle import Screen
import random

import colorgram

rgb_colors = []
colors = colorgram.extract('turtle-jpg.jpg', 10)

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_col = (r, g, b)
    rgb_colors.append(new_col)

timi = t.Turtle()
t.colormode(255)
timi.speed(20)
timi.penup()

timi.hideturtle()

screen = Screen()
screen.setup(width=800, height=600)
screen.title("piece of art")
# screen.tracer(0)

def draw_dots(dots_nu):
     for _ in range(dots_nu):
         timi.dot(20, random.choice(rgb_colors))
         timi.forward(50)
rows_num=9
dot_num=11
a=1
x=-250
y=-200
while a<(rows_num+1):
    timi.goto(x,y)
    draw_dots(dot_num)
    y += 50
    a += 1

# screen.update()
screen.exitonclick()

