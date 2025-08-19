#Charlotte Baker
#CSCE 101- Lab 005
#2/13/2022
#crb27@email.sc.edu
#Lab 05 - Turtle Control

import turtle
import random

win = turtle.Screen()
win.bgcolor('cyan')

vanilla=turtle.Turtle()
vanilla.shape('turtle')
vanilla.color('red')
speed = 3
running = True

def go_left():
    vanilla.left(90)

def go_right():
    vanilla.right(90)

def faster():
    global speed
    speed = speed + 0.5

def slow_down():
    global speed
    if speed > 1:
        speed = speed - 0.5
    else:
        speed = 1

def return_origin():
    turtle.penup()
    turtle.home()
    turtle.pendown()

def turn_pink():
    vanilla.color('pink')

def change_shape():
    vanilla.shape('circle')

def go_home():
    vanilla.penup()
    vanilla.setposition(0,0)
    vanilla.pendown()

win.listen()

win.onkey(go_left,'Left')
win.onkey(go_right,'Right')
win.onkey(faster,'Up')
win.onkey(slow_down,'Down')
win.onkey(turn_pink, 'a')
win.onkey(change_shape,'b')
win.onkey(go_home,'space')

#My 2 additional buttons are with keys 'a' and 'b'
#The first turns my turtle pinnk by pressing the 'a' key, activating the function
#The second changes my turtle's shape from a turtle to a circle by pressing the 'b' key

vanillamoves = 0

while running:
    vanilla.forward(speed)
    vanillamoves +=1
    if vanillamoves % 30 == 0:
        vanillamoves.left(random.randint(0,359))








