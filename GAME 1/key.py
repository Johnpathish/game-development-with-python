import turtle
p=turtle.Turtle()

def rectangle():
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

rectangle()

p.goto(100,100)
rectangle()

p.goto(-100,-100)
rectangle()

turtle.done()