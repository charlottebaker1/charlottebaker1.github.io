#this will be help with labs 7 and 8
#3/14/22

#PROBLEM STATEMENT - create a set of ten turtles that will each be assigned a color that is randomly selected
#you will use an invisible turtle to draw a circle with a radius of 350 that will be a boundary and if
#any turtle hits the boundary it will jump back to the origin (0,0)
#we will also use our invisible turtle to write our name outside the boundary
#set of ten turtles (random colors) will start at a set boundary position of (-100,100)
#and when the turtles begin moving they will start at a random location within the boundary
#if one of the turtles comes within 20 units of another turtle, it will turn light pink

import turtle
import random

win = turtle.Screen()
win.bgcolor('white')
win.tracer(1)

#create an invisible turtle
invisible_turtle = turtle.Turtle()
invisible_turtle.color('black')
#we will hide our turtle
invisible_turtle.hideturtle()
invisible_turtle.penup()
invisible_turtle.goto(0,-300)
#can also use .setposition()
invisible_turtle.pendown()
invisible_turtle.circle(300)

#name writing
invisible_turtle.penup()
invisible_turtle.setposition(200,350)
invisible_turtle.pendown()
invisible_turtle.write('Charlotte Baker')

#set of ten turtles (random colors) will start at a set boundary position of (-100,100)
#and when the turtles begin moving they will start at a random location within the boundary
#first create an empty list to hold our set of turtles
turtle_list = []
#create a list of 4 colors
turtle_colors = ['orange','magenta','purple','cyan']
max_turtles = 8

#use a for loop to create a set of turtles
for i in range(max_turtles):
    #we are appending a turtle instance to the list each time the for loop iterates
    turtle_list.append(turtle.Turtle())
    #referencing the turtles in the index of the list
    turtle_list[i].penup()
    #assign a color randomly
    turtle_list[i].color(turtle_colors[random.randint(0,3)])
    #four items in the list 0, 1, 2, 3
    turtle_list[i].setposition(random.randint(-150,150),random.randint(-150,150))
    turtle_list[i].pendown()

#create a speed variable
speed = 2
#while loop to control how long our turtles will move -- if our while loop will run for 1000 time units
#first create a variable to keep track of our time
time_count = 0
while time_count < 1500:
    #we need our turtles to move forward the specified speed
    #we need our turtles to check for whether they are within 20 units of eachother
    #if it hits the boundary, turn light pink

    #lets get turtles moving; nested loop in the while loop
    for i in range(max_turtles):
        turtle_list[i].forward(speed)

        #lets create a boundary check
        if turtle_list[i].distance(0,0) > 300:
            turtle_list[i].penup()
            turtle_list[i].setposition(0,0)
            turtle_list[i].color('black')
            turtle_list[i].pendown() #might not need this in lab
        #we also need for each of these turtles to move randomly
        #we will generate a random number between one and thirty
        #if this is equal to 1 then our turtles will move a random direction
        if random.randint(1,30) == 1:
            #here we will have our turtle move to the left between the degrees of 0 and 359
            #for whatever random integer is generated
            turtle_list[i].left(random.randint(0,359))
        #collision detection
        for j in range(max_turtles):
            #check to make sure we are not comparing the same two turtles
            #!= is not equal
            if i != j:
                if turtle_list[i].distance(turtle_list[j].xcor(),turtle_list[j].ycor()) <= 30:
                    turtle_list[i].color('red')
                    turtle_list[j].color('red')
    time_count += 1






















