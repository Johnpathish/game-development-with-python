import turtle
import random


segment=[]

grass=turtle.Screen()
grass.title("Snake game")
grass.bgpic("grass.gif")
grass.setup(600,600)


grass.addshape("head up.gif")
grass.addshape("head down.gif")
grass.addshape("head left.gif")
grass.addshape("head right.gif")
grass.addshape("body.gif")

snake=turtle.Turtle()
snake.shape("head up.gif")
snake.penup()
snake.goto(0,0)
snake.setheading(90)



food=turtle.Turtle()
food.color("red")
food.shape("circle")
food.speed(0)
food.penup()
food.goto(10,10)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("head up.gif")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0", font=("candara",24,"bold"))


score=0

def move():
    snake.forward(5)
    

def up():
    if snake.heading()!= 270:
       snake.setheading(90)
       snake.shape("head up.gif")
def down():
    if snake.heading()!= 90:
       snake.setheading(270)
       snake.shape("head down.gif")
def right():
    if snake.heading()!= 180:
       snake.setheading(0)
       snake.shape("head right.gif")
def left():
    if snake.heading()!= 0:
       snake.setheading(180)   
       snake.shape("head left.gif")


    
                   


turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

turtle.listen()

segment=[]

while True:
    grass.update()
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290 :
        grass.bgpic("game over.gif")
        food.hideturtle()
    


    if snake.distance(food) < 20 :
        x = random.randint(-285,285)
        y = random.randint(-285,285)
        food.setpos(x,y)
        score=score+1
        pen.clear()
        pen.write("Score : {}".format(score), font=("Courier",27,"bold"))
        body=turtle.Turtle()
        body.penup()
        body.shape("body.gif")
        body.speed(0)
        segment.append(body)


    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)

    move()

   

turtle.done()
