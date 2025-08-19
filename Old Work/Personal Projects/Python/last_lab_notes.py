#Class Notes -- April 20th
#this is the final lab assignment -- using mouse to draw on the screen

import turtle

#turtle.ondrag(fun -- a function with two arguments which can be
# called with the coordinates of the clicked point on a canvas; btn -- number of mouse-button add true or false
# if True a new binding will be added; if False will replace a former binding

win = turtle.Screen()
win.bgcolor('light blue')

pen = turtle.Pen()
pen.color('magenta')
pen.shapesize(1.5)
pen.speed(0)
pen.pensize(3)
tracing = True

def trace(x,y):
    #we will give it our x,y coordinates for the location of our pen mouse
    #this function will switch the tracing status
    global tracing
    #switch between tracing and not tracing
    #if/else so that we will switch
    if tracing:
        pen.color()
    else:
        pen.color()

#new function to draw
#allow us to trace the mouse
def draw(x,y):
    #x - xcoordinate of the mouse
    #y - ycoordinate of the mouse
    #stop backtracking by binding to None
    pen.ondrag(None)

    #tracing the mouse
    pen.setheading(pen.towards(x,y))
    pen.goto(x,y)

#call the draw function to continously trace the mouse movement
    pen.ondrag(draw)

#bind the draw function to mouse dragging
pen.ondrag(draw)

#bind the status switching to the right click
win.onscreenclick(trace,btn=3)
#similar to onkey 1 - left click, 2 - push wheel, 3 - right click


#take screen back to the main loop
turtle.mainloop()
