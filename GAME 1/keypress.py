import turtle
import random
p=turtle.Turtle()

def rectangle():
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    p.goto(x,y)
    p.pendown()
    p.fillcolor("yellow")
    p.begin_fill()
    for i in range(2):
        p.forward(100)
        p.left(90)
        p.forward(50)
        p.left(90)
    p.end_fill()
    p.penup()
turtle.onkey(rectangle,"Up")
turtle.listen()

turtle.done()
