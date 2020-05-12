# lab01.py, Chen Li
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color('black')

def drawL(width, height):
    startX = t.xcor()
    startY = t.ycor()

    topAX = startX
    topAY = startY + height

    bottomrightX = startX
    bottomrightY = startY

    bottomleftX = startX + width
    bottomleftY = startY

    t.up()
    t.goto(topAX, topAY)
    t.down()
    t.goto(bottomrightX, bottomrightY)
    t.goto(bottomleftX, bottomrightY)

def drawC(width, height):
    startX = t.xcor()
    startY = t.ycor()

    toprightX = startX + width
    toprightY = startY + height

    topleftX = startX
    topleftY = startY + height

    bottomrightX = startX + width
    bottomrightY = startY

    bottomleftX = startX
    bottomleftY = startY

    t.up()
    t.goto(toprightX, toprightY)
    t.down()
    t.goto(topleftX, topleftY)
    t.goto(bottomleftX, bottomleftY)
    t.goto(bottomrightX, bottomrightY)

def draw2(width, height):
    startX = t.xcor()
    startY = t.ycor()

    toprightX = startX + width
    toprightY = startY + height

    topleftX = startX
    topleftY = startY + height

    bottomrightX = startX + width
    bottomrightY = startY

    bottomleftX = startX
    bottomleftY = startY

    midleftX = startX
    midleftY = startY + height/2

    midrightX = startX + width
    midrightY = startY + height/2

    t.up()
    t.goto(topleftX, topleftY)
    t.down()
    t.goto(toprightX, toprightY)
    t.goto(midrightX, midrightY)
    t.goto(midleftX, midleftY)
    t.goto(bottomleftX, bottomleftY)
    t.goto(bottomrightX, bottomrightY)

def draw0(width, height):
    startX = t.xcor()
    startY = t.ycor()

    toprightX = startX + width
    toprightY = startY + height

    topleftX = startX
    topleftY = startY + height

    bottomrightX = startX + width
    bottomrightY = startY

    bottomleftX = startX
    bottomleftY = startY

    t.goto(topleftX, topleftY)
    t.goto(toprightX, toprightY)
    t.goto(bottomrightX, bottomrightY)
    t.goto(bottomleftX, bottomleftY)
    t.up
    t.goto(bottomrightX, bottomrightY)
    t.down()

def draw1(width, height):
    startX = t.xcor()
    startY = t.ycor()

    topX = startX + width
    topY = startY + height

    bottomX = startX + width
    bottomY = startY

    t.up()
    t.goto(topX, topY)
    t.down()
    t.goto(bottomX, bottomY)

t.up()
t.goto(-200, 0)
t.down()

drawC(50, 100)

t.up()
t.forward(10)
t.down()

drawL(50, 100)

t.up()
t.forward(10)
t.down()

draw2(50, 100)

t.up()
t.forward(10)
t.down()

draw0(50, 100)

t.up()
t.forward(10)
t.down()

draw2(50, 100)

t.up()
t.forward(10)
t.down()

draw1(50, 100)

#small line
t.up()
t.goto(-200, -200)
t.down()

drawC(40, 80)

t.up()
t.forward(8)
t.down()

drawL(40, 80)

t.up()
t.forward(8)
t.down()

draw2(40, 80)

t.up()
t.forward(8)
t.down()

draw0(40, 80)

t.up()
t.forward(8)
t.down()

draw2(40, 80)

t.up()
t.forward(8)
t.down()

draw1(40, 80)
