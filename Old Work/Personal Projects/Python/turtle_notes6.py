#CLASS NOTES - help with previous labs

import turtle
import random

#PROBLEM STATEMENT
#lets have 6 green turtles and 4 yellow turtles; these turtles if they go beyond the boundary of a circle with a 350
#degree radius they will bounce back to the origin (0,0) and they will turn light pink
#in the initial setup we will place these green turtles at a random location between the range of x(0,-100) and y(100,100)
#for the yellow turtles, same thing
#lets have all 10 turtles move at the same speed
#then we will require our turtles move randomly every 65 moves
#you will use a turtle to draw the boundary of the circle with a radius of 350 degrees
#this turtle will not be displayed to the user
#lets say the game will run for 1500 time units

win = turtle.Screen()
win.bgcolor('white')

invisible_turtle = turtle.Turtle()
invisible_turtle.color('black')
invisible_turtle.hideturtle()
invisible_turtle.penup()

invisible_turtle.goto(0,-300)
invisible_turtle.pendown()
invisible_turtle.circle(300)
invisible_turtle.penup()

#create a set of six green turtles
#create the max here
max_turtles_red = 4
red_turtles = []
for i in range(max_turtles_red):
    red_turtles.append(turtle.Turtle())
    red_turtles[i].color('red')
    red_turtles[i].penup()
    red_turtles[i].shape('turtle')
    #lets randomly assign turtles to a location on the cartesian plane within the range of (x,y) coordinates
    red_turtles[i].setposition(random.randint(-100,100),random.randint(0,100))


#create a set of four yellow turtles
max_turtles_blue = 4
blue_turtles = []
for i in range(max_turtles_blue):
    blue_turtles.append(turtle.Turtle())
    blue_turtles[i].color('blue')
    blue_turtles[i].penup()
    blue_turtles[i].shape('turtle')
    blue_turtles[i].setposition(random.randint(-100,100),random.randint(-100,0))

#lets create a function that will return a turtle that hits the boundary to the origin and
#turns the turtle to light pink
def go_home(object):
    object.color('black')
    object.setposition(0,0)
    object.speed(4)
#consistent speed variable
speed = 4
time_count = 0
red_turtle_moves = 0
blue_turtle_moves = 0

while time_count < 1000:
    for a_turtle in red_turtles:
        #we are going to move the turtles forward our designated speed, check for boundary collisions, and
        #require the turtle to move randomly every 65 moves
        a_turtle.forward(speed)
        #remember that for the modulo operator: x mod y = r
        red_turtle_moves += 1
        if red_turtle_moves % 50 == 0:
            a_turtle.right(random.randint(0,359))

        if a_turtle.distance(0,0) > 300:
            go_home(a_turtle)

    for b_turtle in blue_turtles:
        b_turtle.forward(speed)
        blue_turtle_moves += 1
        if blue_turtle_moves % 50 == 0:
            b_turtle.right(random.randint(0,359))

        if b_turtle.distance(0,0) > 300:
            go_home(b_turtle)

    time_count += 1



###########################  NEW LAB 9 NOTES  #########################################################################

#lets say we have two turtles
hunting_turtle = turtle.Turtle()

hunted_turtle = turtle.Turtle()

hunted_turtle_speed = 4
running = True
speed = 5

while running:
    hunting_turtle.forward(speed)
    hunted_turtle.forward(speed)

    #use setheading method specifying the x and y values for each of the hunted turtles
    hunting_turtle.setheading(hunting_turtle.towards(int(hunted_turtle.xcor(),int(hunted_turtle.ycor()))))

