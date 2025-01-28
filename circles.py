import turtle as t
from turtle import Screen
import random
t.colormode(255)
scr = Screen()
pent = t.Turtle()

pent.pensize(3)  # Або pent.width(5)
pent.speed(100)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def spirograf(v):
    for _ in range(int(360/v)):
        pent.circle(100)
        pent.color(random_color())
        current_head = pent.heading()
        pent.setheading(current_head + v)
spirograf(20)
scr.exitonclick()