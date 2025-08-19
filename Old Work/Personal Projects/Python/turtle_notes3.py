#02/14/2022 turtle notes

#turtle setup
import turtle
import random

#create a turtle screen
win = turtle.Screen()
win.bgcolor('cyan')

#create a turtle instance
vanilla=turtle.Turtle()
vanilla.shape('turtle')
vanilla.color('red')

#create a variable to set the turtle's spped
speed = 1

#we will create a loop that will love our turtle constantly until some event happens to make it stop
#here we will use a while loop so that the turtle will continue to run
#we will control the while loop using the variable running
#4 different data types - this is a Boolean data type (can take on the values - true or false)
running = True

#let's create a function to make our turtle move left whenever the user presses the left arrowkey
def go_left():
    vanilla.left(15)
    #angles are specified in degrees, so here we will specify the degrees we want the turtle to turn left

#create a function to speed up our turtle
def faster():
    global speed
    #we will use a global variable for speed
    #using global - it will continue to be executed even when the function is over
    #here, we are saying we want the turtle to speed up
    speed = speed + 0.5

#create a function to slow down our turtle
def slow_down():
    global speed
    #say your turtle's speed cannot fall below 1
    if speed > 1:
        speed = speed - 0.5
    else:
        speed = 1

#create a function that will turn my turtle pink when its called
def turn_pink():
    vanilla.color('pink')





#event handler will listen for our events using win.listen() which is built into the turtle module
#using the variable name of your screen object use .listen()
win.listen()

#format for your .onkey commands
#.onkey is how you specify which key on the keyboard will be tied to a particular function
win.onkey(go_left,'Left')
win.onkey(faster,'Up')
win.onkey(slow_down,'Down')
#in the parentheses, you will specify the name of the function from the signature line followed by a comma
#and then the name of a key in QUOTES
#'Left'
#'Right'     all these ones are in uppercase
#'Up'
#'Down'
#"space" - this is in lowercase
win.onkey(turn_pink, 'a')

vanillamoves = 0

#create the loop to control the turtle's ongoing movement
while running:
    vanilla.forward(speed)
    #say you want your turtle to randomly move while it is continuing to move
    #let's use a random direction every 30 moves
    vanillamoves +=1
    #one in 30 chance probability
    if vanillamoves % 30 == 0:
        vanillamoves.left(random.randint(0,359))
        