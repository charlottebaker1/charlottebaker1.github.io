#game examples

import turtle
import random
import time

window = turtle.Screen()
window.bgcolor('blue')
window.tracer(3)

invisible_turt = turtle.Turtle()
invisible_turt.hideturtle()
invisible_turt.penup()
invisible_turt.setposition(0,-300)
invisible_turt.pendown()
invisible_turt.circle(300)

speed = 1
running = True

print('Welcome to the magic wonderland of Jackson Pollock! Here you can learn to be a master!')
print('You can create your own masterpiece in the serene background of your choice!')

#for each of these functions create a turtle

#functions
starryturt = turtle.Turtle()
def draw_starryskybackground(turtleObject):
    pass

lolly = turtle.Turtle()
def draw_coloredlollipops(turtleObject):
    pass

#assume the user will only enter numbers in the range of 1 to 5
print('Select among the backgrounds you want your game to depict: Choices 1 to 3. \n if you want to play starry night version - 1, if you want rainbow lollipops enter - 2,')
backdrop = int(input('Please enter your choice: '))
#fortune teller game!!

for i in range(2):
    if(backdrop == 1):
        draw_coloredlollipops(lolly)
    elif(backdrop == 2):
        draw_starryskybackground(starryturt)

#add obstacles

def obstacleschoice1_turtlecolorfill
