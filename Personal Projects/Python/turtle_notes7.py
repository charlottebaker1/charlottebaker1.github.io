#CLASS TURTLE NOTES 3/28

import turtle
import random

#problem statement similar to lab assignment 10

win = turtle.Screen()
win.bgcolor('light blue')
win.tracer(1)

invis = turtle.Turtle()
invis.pencolor('magenta')
invis.penup()
invis.setposition(0,-300)
invis.pendown()
invis.circle(300)

#create a tuple to store the obstacles respective (x,y) coordinates
#at least 50 units apart
#eight obstacles

obstacles = []
numofobstacles = 8

#define out baseline x and y coordinate values
Xcor = 0
Ycor = 1

for i in range(numofobstacles):
    obX = 0
    obY = 0
    while obX < 50 and obX > -50:
        obX = random.randint(-250,250)
    while obY < 50 and obY > -50:
        obY = random.randint(-250,250)

#creating the tuple to store the (x,y coordinate pairs) that we will then adjust
    obstacles.append(obX,obY)
    invis.penup()
    invis.setpostion(obstacles[i][Xcor],obstacles[Ycor])
    invis.pendown()
    invis.begin_fill()
    invis.circle(10)
    invis.end_fill()

    obstacles[i] = (obstacles[i][Xcor],obstacles[i][Ycor]+10)

invis.penup()
invis.setposition(-300,350)
invis.pendown()

speed =4
yertle = turtle.Turtle()

fox1 = turtle.Turtle()
fox2 = turtle.Turtle()

lives = 5

running = True
while running:
    yertle.forward(speed)
    distancefromcenter = yertle.distance(0,0)

    #undo turtles writing
    invis.undo()
    #use our .format printed statement
    invis.write('Distance from Center: {}'.format(int(distancefromcenter),font = ('Courier',24)))

    #check for the number of obstacles that none of the fox turtles come to close
    for i in range(numofobstacles):
        if fox1.distance(obstacles[i][0],obstacles[i][1]) <= 10:
            fox1.setposition(0,0)
            lives = lives - 1
        if lives <= 0:
            running = False



