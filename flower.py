import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")

h = 0
for i in range(180):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.circle(150)
    t.left(2)
    h += 1/180

t.hideturtle()
turtle.done()
