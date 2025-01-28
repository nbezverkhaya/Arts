import turtle as t
from turtle import Screen
import random

scr = Screen()
pent = t.Turtle()

colors = ["#25842c", "#04342b", "#775a23", "#194865", "#061e40", "#35a7ea",
    "#b38b14", "#8e002f", "#eeba2b", "#798bbd", "#b33c14", "#3b5861", "#a7d8e4"]
pent.color(colors[5])
pent.pensize(5)  # Або pent.width(5)
pent.speed(100)

def move():
    # Обираємо напрямок руху черепашки
    direction = random.choice([pent.forward, pent.right, pent.left])
    if direction == pent.forward:
        distance = 20  # Для руху вперед, дистанція
        direction(distance)
    else:
        angle = 90  # Кути обертання
        direction(angle)

for _ in range(300):
    move()
    pent.color(random.choice(colors))

scr.exitonclick()