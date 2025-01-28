import turtle as t
from turtle import Screen
import random

scr = Screen()
pent = t.Turtle()
pent.penup()
pent.goto(-150, 50)
pent.pendown()
circle = 360
side = 3
colors = ["#25842c", "#04342b", "#775a23", "#194865", "#061e40", "#35a7ea",
    "#b38b14", "#8e002f", "#eeba2b", "#798bbd", "#b33c14", "#3b5861", "#a7d8e4"]
pent.color(colors[5])
while side < 10:
    for _ in range(side):
        corner = circle/side
        pent.forward(80)
        pent.right(corner)
    pent.color(random.choice(colors))
    side += 1

scr.exitonclick()