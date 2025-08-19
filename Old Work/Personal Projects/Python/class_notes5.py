#Class Notes - 2/2/22

#for loop background
#for loops are often used to perform an operation on every element of some kind of sequence
#if you want to iterate over a list using the for loop you have to count from zero until the end of the lost
#then access each element by its index

#when you use a for loop, you know how many times your loop will run
#iterating over a list with a for loop
#questions to ask youself (1) what should the list contain (2) what operations will be performed on the list elements

#the for loop will iterate over a given list, perform the operations we have sepcified on each element
#and then stop when it reaches the end of the list

#what happens is the loop simply iterates over elements in a list, and performs the operations on each one

#order of execution works as follows:
#for each pass of the loop, the single iterable is stored in and then the lines of code are executed
#for a for loop, no stopping is required

#syntax:
#for element in a list
    #indented -- the body of the for loop
    #whatever operation is to be applied to each element in the list or you can think of each item the for loop is
    #applied to

#example of a for loop using range
#when the computer is counting it begins at 0
#for i in range(6):
    #print(i)

#when you are generating random numbers, you will import random
#import random

#import turtle
#win=turtle.Screen()
#win.bgcolor('light green')
#win=turtle.Turtle()
#win.penup()
#set position and inside parameters specify the (x,y) coordinates that you want your turtle to go to
#win.setposition(0,-300)
#win.pendown()


#n is the sumber of sides in a polygon
#n=6
#no is number of turns
#num=100
#win.width(5)

#for i in range(n):
   # win.forward(90+6*1)
    #360 divided by number of sides (ex - 6 for a hexagon as "n")
    #sum of interior angles formula --- 180(n-2)
   # win.left(60)


#operators (mathematical)
#/ division
#* multiplication
#+ addition
#- subtraction
#% modulous

import turtle
window=turtle.Screen()
charlotte=turtle.Turtle()

#modulous operator (aka modulo operator)
for i in range(35):
    if i % 4 == 0:
        charlotte.color('red')
        charlotte.forward(20+5*i)
        charlotte.left(90)
    elif i % 4 == 1:
        charlotte.color('yellow')
        charlotte.forward(20+5*i)
        charlotte.left(90)
    elif i % 4 == 2:
        charlotte.color('green')
        charlotte.forward(20+5*i)
        charlotte.left(90)
    else:
        charlotte.color('cyan')
        charlotte.forward(20+5*1)
        charlotte.left(90)

