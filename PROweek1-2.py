import turtle
import random


def screenLeftClick(x, y):
 global r, g, b
 turtle.pencolor((r, g, b))
 turtle.pendown()
 turtle.goto(x,y)
 r = random.random()
 g = random.random()
 b = random.random()

def screenRightClick(x, y):
 turtle.penup()
 turtle.goto(x, y)
 
def screenMidClick(x, y):
 global r, g, b
 tSize = random.randrange(1, 10)
 turtle.shapesize(tSize)
 
 
pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('Jadolyee')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
