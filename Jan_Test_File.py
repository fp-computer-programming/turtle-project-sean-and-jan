#Author: Sean and Jan Salafia

import turtle   #imports turtle module
import random

window = turtle.Screen()
window.title("Turtle Snake Score Race")   #title of window
window.colormode(255)
window.bgcolor(102, 255, 51)
#----------------------------------------------------------------------------------------------------------------
#Setup
def setup():
    global p1
    global p2
    global p1_xList
    global p1_yList
    global p2_xList
    global p2_yList
    global window

    p1_xList = []
    p1_yList = []
    p2_xList = []
    p2_yList = []
#----------------------------------------------------------------------------------------------------------------
import turtle           # This chunk of code automatically defaults the screen to fullscreen, 
screen = turtle.Screen()
  #set size:
screen.setup(width = 1.0, height = 1.0)
  #remove close,minimaze,maximaze buttons:
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
#----------------------------------------------------------------------------------------------------------------
#Scorecard

score_p1 = 0
score_p2 = 0
scorecard_p1 = turtle.Turtle()
scorecard_p1.speed(0)
scorecard_p1.color('black')
scorecard_p1.penup()
scorecard_p1.hideturtle()
scorecard_p1.goto(0, 375)
scorecard_p1.write('Player 1 Score: ' + str(score_p1), align='center', font = ('Raleway', 24, 'normal'))

scorecard_p2 = turtle.Turtle()
scorecard_p2.speed(0)
scorecard_p2.color('black')
scorecard_p2.penup()
scorecard_p2.hideturtle()
scorecard_p2.goto(0, 330)
scorecard_p2.write('Player 2 Score: ' + str(score_p2), align='center', font = ('Raleway', 24, 'normal'))

# Outline of the playing field
border = turtle.Turtle()
border.speed(0)
border.shape('circle')
border.color('black')
border.penup()
border.hideturtle()
border.goto(650,310)
border.pendown()
border.goto(-650,310)
border.goto(-650,-400)
border.goto(650,-400)
border.goto(650,310)
border.penup()

#-----------------------------------------------------------------------------------------------------------------------
# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('red')
food.penup()
food.setpos(0,100)

#-----------------------------------------------------------------------------------------------------------------------


def update_score_p1():
    scorecard_p1.clear()
    scorecard_p1.write('Player 1 Score: ' + str(score_p1), align='center', font = ('Raleway', 24, 'normal'))
def update_score_p2():
    scorecard_p2.clear()
    scorecard_p2.write('Player 2 Score: ' + str(score_p2), align='center', font = ('Raleway', 24, 'normal'))
#-----------------------------------------------------------------------------------------------------------------------

p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("red")

def move_up():             
    if p1.heading() != 270:
        p1.setheading(90)
        p1.speed(0)
def move_down():
    if p1.heading() != 90:
        p1.setheading(270)
        p1.speed(0)
def turn_left():
    if p1.heading() != 0:
        p1.setheading(180)
        p1.speed(0)
def turn_right():
    if p1.heading() != 180:
        p1.setheading(0)
        p1.speed(0)

p1.penup()
p1.goto(-200,0)

#--------------------------------------------------------------------------------------------------------------------------
p2 = turtle.Turtle()
p2.penup()
p2.shape("turtle")
p2.color("blue")
p2.goto(200,-200)
def move_up_2():              #Define movement functuons
    if p2.heading() != 270:
        p2.setheading(90)
        p2.speed(0)
def move_down_2():
    if p2.heading() != 90:
        p2.setheading(270)
        p2.speed(0)
def turn_left_2():
    if p2.heading() != 0:
        p2.setheading(180)
        p2.speed(0)
def turn_right_2():
    if p2.heading() != 180:
        p2.setheading(0)
        p2.speed(0)
p2.penup()
p2.goto(200,-200)
p2.left(180)

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
def coordinates(player):
    x = player.xcor()
    y = player.ycor()
    return x, y

def movement():
    global p1
    global p2
    global moving

    moving = True

    while moving != False:
        p1.forward(6)
        p2.forward(6)
        window.listen()

        window.onkeypress(move_up, "Up")          #Bind p1 movement to specific keys
        window.onkeypress(move_down, "Down")
        window.onkeypress(turn_left, "Left")
        window.onkeypress(turn_right, "Right")

        window.onkeypress(move_up_2, "w")         #Bind p2 movement to specific keys
        window.onkeypress(move_down_2, "s")
        window.onkeypress(turn_left_2, "a")
        window.onkeypress(turn_right_2, "d")

        x,y = coordinates(p1)
        bikecheck(x, y, p1)

        x,y = coordinates(p2)
        bikecheck(x, y, p2)

def bikecheck(x,y,players):
    global moving
    global p1_xList
    global p1_yList
    global p2_xList
    global p2_yList
    if abs(x)> 650 or abs(y) > 350:
        moving = False
        #bike blowing up animation
        players.hideturtle()
        for t in range(12):
                players.right(30)
                players.forward(30)
                players.setposition(x,y)

if p1.distance(food) < 20:
    food.goto(random.randint(-580,580),random.randint(-300,300))
    score_p1 += 10
    update_score_p1()
if p2.distance(food) < 20:
    food.goto(random.randint(-580,580),random.randint(-300,300))
    score_p2 += 10
    update_score_p2()
#-------------------------------------------------------------------------

window.mainloop()