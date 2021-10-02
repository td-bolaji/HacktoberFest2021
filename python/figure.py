import turtle
from turtle import Screen
from datetime import datetime

now = datetime.now()
dateTime = now.strftime("%d/%m/%Y %H:%M:%S")

screen = Screen()
TURTLE_SIZE = 20

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.pencolor("green")
t.speed(0.2)
t.penup()
t.goto(0, 200)
t.pendown()
a = 0
b = 0
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 200:
        break
    t.hideturtle()

turtle.penup()
turtle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - (TURTLE_SIZE/2) - 20)
turtle.write(dateTime, move=False, font=('monaco', 15, 'bold'), align='left')
turtle.done()
