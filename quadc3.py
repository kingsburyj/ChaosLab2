import turtle
import math



def Q(c, x):
    return math.pow(x,2) + c

def drawAxes(pen):
    pen.goto(0,-10)
    pen.down()
    pen.goto(0,10)
    pen.up()
    pen.goto(-10,0)
    pen.down()
    pen.goto(10,0)
    pen.up()
    return 0

def markAxis(pen, c):
    ticksize = .05
    pen.up()
    pen.goto(c,0)
    pen.down()
    pen.goto(c,ticksize)
    pen.goto(c,-ticksize)
    pen.up()
    pen.goto(c,-ticksize*4)
    pen.write(c, False, align="center")
    return 0

def markC(pen):
    markAxis(pen, .25)
    markAxis(pen, -.75)
    markAxis(pen, -1.25)
    markAxis(pen, -1.76)
    markAxis(pen, -1.78)

def eventualOrbit(pen, c):
    last = Q(c,0)
    for x in range(1,100):
        last = Q(c,last)
    pen.up()
    for x in range(0,50):
        last = Q(c,last)
        pen.goto(c, last)
        pen.dot(3)

def drawOrbits(pen):
    eventualOrbit(pen, .25)
    pen.color("red")
    count = -1.75
    numIntervals = 50
    intervalDist = (1.78-1.75)/numIntervals
    while(count >= -1.78):
        eventualOrbit(pen,count)
        count = count - intervalDist
    eventualOrbit(pen,-1.78)
    

def initialize():
    screen = turtle.Screen()
    pen = turtle.Turtle()
    turtle.hideturtle()
    screen.tracer(1000)
    screen.screensize(800,800)
    screen.setworldcoordinates(-1.79,-1.9,-1.75,1.5)
    drawAxes(pen)
    markC(pen)
    drawOrbits(pen)
    screen.exitonclick()
def main():
    initialize();
    

main()
