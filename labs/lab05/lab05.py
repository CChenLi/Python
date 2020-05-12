# lab05.py, Chen Li
import turtle
import math
import random


def drawRectangle(width, height, tilt, penColor, fillColor):
    """
    draw a rectangle with a given width, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. Use a turtle called t to create the drawing
    """
    t.down()
    t.color(penColor, fillColor)
    t.begin_fill()
    t.setheading(tilt)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.seth(0)
    t.up()

def drawTriangle(base, height, tilt, penColor, fillColor):
    """
    draw a triangle with a given base, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. Use a turtle called t to create the drawing
    """
    t.down()
    t.color(penColor, fillColor)
    t.begin_fill()
    t.setheading(tilt)
    t.forward(base)
    t.left(180 - math.degrees(math.atan(2 * height / base)))
    t.forward(math.sqrt(height ** 2 + 0.25 * base ** 2))
    t.left(2 * (math.degrees(math.atan(2 * height / base))))
    t.forward(math.sqrt(height ** 2 + 0.25 * base ** 2))
    t.end_fill()
    t.seth(0)
    t.up()


def testRectangle():
    
    drawRectangle( 50, 100, 0, "red", "") 

    # Move the turtle right by 200 units without leaving a trail
    t.seth(0)   # Set the absolute heading of the turtle to 0 degrees (pointing east)
    t.up()     
    t.forward(200) # Move the turtle forward by 200 units 
    t.down()

    drawRectangle( 50, 100, 20, "green", "yellow") 

    # Move the turtle right by 200 units without leaving a trail
    t.seth(0)   # Set the absolute heading of the turtle to 0 degrees (pointing east)
    t.up()     
    t.forward(200) 
    t.down()


def drawTree(height, color):
    drawRectangle(height / 12, 0.3 * height, 0, "brown", "brown")
    t.left(90)
    t.forward(0.3 * height)
    t.left(90)
    t.forward(height / 4)
    t.right(180)
    drawTriangle(7 * height / 12, 0.3 * height, 0, color, color)
    t.left(90)
    t.forward(0.2 * height)
    drawTriangle(7 * height / 12, 0.3 * height, 0, color, color)
    t.left(90)
    t.forward(0.2 * height)
    drawTriangle(7 * height / 12, 0.3 * height, 0, color, color)

def testdrawTree():
    t.up()
    t.goto(0,-400)
    t.down()
    drawRectangle(200, 200, 0 , "red","")
    drawTree(200, "green")

def drawForest():
    ''' 
    Draws a collection of trees placed at random locations within a rectangular region
    '''
    shadeOfGreen = ["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"]
    x = -400
    for i in range(random.randint(10,15)):
        x = x + random.randint(30,100)
        y = 0 + random.randint(-30, 30)
        t.up()
        t.goto(x, y)
        drawTree(random.randint(150,250),random.choice(shadeOfGreen))
        

def drawHut():
    '''
    Draw a brown hut of fixed dimensions purely composed of rectangles
    Use the random module to enhance your drawing by introducing irregularilities in a controlled way
    '''
    t.pensize(3)
    for i in range(10):      
        drawRectangle(25, 80, 0, 'black', 'brown')
        t.seth(random.randint(-4,4))
        t.forward(8)
    t.left(180)
    t.up()
    t.forward(25)
    t.right(90)
    t.forward(120)
    t.down()
    for i in range(10):
        drawRectangle(14, 85 + random.randint(-3, 3),130 + 12 * i , 'black', 'brown')


def drawVillage():
    '''
    Draw a sequence of five huts, placed randomly along a horizontal line
    '''
    x = -450
    for i in range(5):
        x = x + random.randint(120,140)
        y = -80 + random.randint(-30, 30)
        t.up()
        t.goto(x, y)
        drawHut()

def draw():
    drawForest()
    drawVillage()

if __name__=="__main__":
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(10000)
    draw()





    

