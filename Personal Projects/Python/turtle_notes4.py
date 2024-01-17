#CLASS NOTES TURTLE
# 2/24 + 2/16 CONTINUED ####################################

#same code as turtle notes 3 but modified

import turtle
import random

#create a turtle screen
win = turtle.Screen()
win.bgcolor('cyan')

#create a turtle instance
vanilla=turtle.Turtle()
vanilla.shape('turtle')
vanilla.color('red')

speed = 1

running = True

def go_left():
    vanilla.left(15)

def faster():
    global speed
    speed = speed + 0.5

def slow_down():
    global speed
    if speed > 1:
        speed = speed - 0.5
    else:
        speed = 1

def turn_pink():
    vanilla.color('pink')

#create a function to make the turtle return to the ORIGIN
def go_home():
    #lets add that when the turtle goes back to the origin it doesnt leave a line
    #first do an example of a specific turtle
    vanilla.penup()
    #inside the parentheses is a specified x,y coordinate
    vanilla.setposition(0,0)
    vanilla.pendown()
    #then create an .onkey command for this -->

#Let's say that we wanted any turtle instances to return home instead of just vanilla
def go_home_all(a_turtle):
    a_turtle.penup()
    a_turtle.setposition(0,0)
    a_turtle.pendown()


win.listen()

win.onkey(go_left,'Left')
win.onkey(faster,'Up')
win.onkey(slow_down,'Down')
win.onkey(turn_pink, 'a')
win.onkey(go_home,'space')

vanillamoves = 0


#getting the turtle to move in a random direction every 30 moves
#when we say this it means we are specifying that the turtle will make a turn with a random degree of sharpness
#instead, we want to specify an angle within the range between 0 and 359
while running:
    vanilla.forward(speed)
    vanillamoves +=1
    #here we are specifying that we want the turtle to move randomly every 30 moves
    #again we are dealing with our modulous operator -- %
    #remember the formula x mod y == r (where r is the remainder!!!!) and where (x is the dividend; y is the divider)

    if vanillamoves % 30 == 0:
        vanillamoves.left(random.randint(0,359))


    #this distance will judge whether vanilla's distance is greater than 250 units from the origin
    # as long as the while loop runs
    if vanilla.distance(0,0) > 250:
        go_home()

#this is one in 30 chance PROBABILITY
#if random.randint(1,30) == 1:
    #vanilla.left(random.randint(0,359))
