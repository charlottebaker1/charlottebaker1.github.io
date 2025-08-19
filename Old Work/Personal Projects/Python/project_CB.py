#Charlotte Baker
#CSCE 101 005
#4/7/22
#crb27@email.sc.edu
#Lab 11 Building a Game Pt 1

import turtle
import random
win = turtle.Screen
win.bgcolor('black')

#my game is going to be using turtle and creating a game where a 'plane' is trying to collect
#as many stars as possible for points in the time alloted. there will be a plane turtle with different colored
#stars in the 'galaxy'. It will be very colorful and have the time count above
#the plane turtle will be controlled with keys by the user
#it will welcome the user and if they reach a certain score congratulate them
#if it hits the 'comets'(turtles) the user will lose points

#these will be the stars that will eventualyl disappear when hit
stars = []
max_stars = 15
stars_colors = ['magenta','lightblue','green','orange']
for i in max_stars:
    stars.append(turtle.Turtle())
    stars[i].penup()
    stars[i].shape('star')
    stars[i].color(stars_colors[random.randint(0,3)])

#this turtle will write the messages displayed to the user.
writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.pencolor('white',25)
writing_turtle.setpositon(-30,0)
writing_turtle.write('GALAXY GAME')

#this will be the main turtle controlled by the user
rocket = turtle.Turtle
rocket.shape('arrow')
rocket.color('gray')
rocket.penup()



