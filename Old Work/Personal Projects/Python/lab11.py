#Charlotte Baker
#CSCE 101 005
#4/1/22
#crb27@email.sc.edu
#Lab 11 Turtle Hunting

import turtle
import random
import time

win = turtle.Screen()
win.bgcolor('light blue')
win.tracer(1)

char = turtle.Turtle()
char.shape('square')
char.color('green')
speed = 10
char.penup()

count = turtle.Turtle()
count.hideturtle()
count.penup()
count.setposition(-300,300)

def go_left():
    char.left(20)
def go_right():
    char.right(20)
def go_faster():
    global speed
    if speed < 10:
        speed = speed+1
def go_slower():
    global speed
    if speed > 1:
        speed = speed-1

win.listen()
win.onkey(go_left,'Left')
win.onkey(go_right,'Right')
win.onkey(go_faster,'Up')
win.onkey(go_slower,'Down')

invisible = turtle.Turtle()
invisible.color('pink')
invisible.hideturtle()
invisible.penup()
invisible.goto(0,-300)
invisible.pendown()
invisible.circle(300)
invisible.penup()
invisible.goto(-350,350)
invisible.pendown()
invisible.write('Charlotte Baker')

turtle_list = []
turtle_colors = ['blue','blue','blue','blue']
max_turtles = 8

for i in range(max_turtles):
    turtle_list.append(turtle.Turtle())
    turtle_list[i].penup()
    turtle_list[i].shape('turtle')
    turtle_list[i].color(turtle_colors[random.randint(0,3)])
    turtle_list[i].setposition(random.randint(-150,150),random.randint(-150,150))

    def go_home(object):
        object.color('black')
        object.setposition(0,0)
        object.speed(2)
    speed = 2
    time_count = 0
    running = True
    count.pendown()

    while time_count < 1500:
        char.forward(speed)
        time_count = time_count + 1
        count.undo()
        count.write('Time: {}'.format(time_count))

        for i in range (max_turtles):
            turtle_list[i].forward(speed)
            if turtle_list[i].distance(0,0)>300:
                go_home(turtle_list[i])
            if turtle_list[i].distance(char.xcor(),char.ycor()) < 10:
                turtle_list[i].hideturtle()
            if time_count % 50 == 0:
                turtle_list[i].left(random.randint(0,359))



