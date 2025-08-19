#Introduction to turtle


#import the turtle module
import turtle

#we want to create a turtle screen; the turtle screen is an object
#turtle_window is the name of the variable - ie can be changed

turtle_window=turtle.Screen()
#now when we want to do something with the turtle screen object, reference the variable name - turtle_window

#we want to make our background screen a color
turtle_window.bgcolor('pink')

#create a turlte object
#do not call the name of your turtle "turtle" - will cause issues
marcy=turtle.Turtle()
#we have created a turtle instance; which means any property/attribute/characteristic a turtle in the turtle module can have can be assigned to "marcy"

#Lets say we want the shape of marcy to be a turtle
marcy.shape('turtle')

marcy.width(3)
#move the turtle forward
#distance in parentheses in units
#same applies for .backward
marcy.forward(100)
#going to draw a triangle
marcy.right(120)
marcy.forward(100)
marcy.right(120)
marcy.forward(100)
marcy.right(120)

#we want marcy to move over w/o leaving a line so she draws a shape 250 units away from the triangle
marcy.penup()
marcy.forward(250)
marcy.pendown()

marcy.right(60)
marcy.forward(100)

#let's say now we want to have marcy draw a square
#testing to ensure when she draws her square its in the window screen
marcy.right(120)
marcy.forward(100)
#this is where we will start our square
marcy.right(90)
marcy.forward(100)
marcy.right(90)
marcy.forward(100)
marcy.right(90)
marcy.forward(100)
marcy.right(90)
marcy.forward(100)

marcy.penup()
marcy.forward(350)
marcy.pendown()

#going to start tackling drawing a polygon, how could we start
marcy.color('cyan')
marcy.forward(200)
marcy.right(60)
marcy.forward(200)
marcy.right(60)
marcy.forward(200)
marcy.right(60)
marcy.forward(200)
marcy.right(60)
marcy.forward(200)
marcy.right(60)
marcy.forward(200)
marcy.right(60)



