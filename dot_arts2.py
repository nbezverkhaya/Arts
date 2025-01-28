import random
import turtle as t
from turtle import Screen
# import colorgram
# rgb_colors=[]
# colors = colorgram.extract('img2.png', 30)
# for c in colors:
#     r=c.rgb.r
#     g=c.rgb.g
#     b=c.rgb.b
#     new_col=(r,g,b)
#     rgb_colors.append(new_col)
# print(rgb_colors)
color_list=[(150, 158, 253), (199, 219, 252), (215, 233, 100), (237, 247, 173), (128, 138, 239), (149, 168, 38), (4, 9, 31), (84, 95, 239), (8, 29, 7), (7, 39, 198), (173, 184, 102), (30, 92, 181), (12, 14, 1), (105, 124, 30), (81, 99, 5), (74, 115, 70), (137, 175, 133), (39, 23, 251), (216, 241, 214), (105, 150, 90), (39, 89, 24), (194, 217, 25), (170, 213, 157), (6, 2, 6), (114, 223, 249), (38, 160, 210), (230, 220, 228), (172, 156, 167), (33, 76, 85), (110, 94, 104)]
timi = t.Turtle()
t.colormode(255)
timi.speed(20)
timi.penup()
def draw_dots(dots_nu):
     for _ in range(dots_nu):
         timi.dot(20, random.choice(color_list))
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
timi.hideturtle()
screen = Screen()
screen.exitonclick()


