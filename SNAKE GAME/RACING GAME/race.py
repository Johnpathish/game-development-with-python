import turtle

road=turtle.Screen()
road.addshape("red car.gif")
road.addshape("blue car.gif")

road.bgpic("race.gif")

redcar = turtle.Turtle() 
redcar.setheading(90)
redcar.shape("red car.gif")
redcar.penup()
redcar.goto(-100,-240)





bluecar = turtle.Turtle()
bluecar.setheading(90)
bluecar.shape("blue car.gif")
bluecar.penup()
bluecar.goto(100,-240)

def player1():
    redcar.forward(5)
def player2():
    bluecar.forward(5)


turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")


turtle.listen()
while True:
  road.update()
  if redcar.pos() > (-100,200):
     road.bgpic("red finish.gif")
  if bluecar.pos() > (100,200):
     road.bgpic("blue finish.gif")



turtle.done()
