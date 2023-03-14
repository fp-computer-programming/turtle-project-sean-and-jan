#Author: Sean and Jan Salafia


import turtle   #imports turtle module
window = turtle.Screen()
window.setup(600,600,0,0)
window.screensize(600,600)        #sets screen size and drawing limits
window.title("Turtle Snake Score Race")   #title of window
window.colormode(255)
window.bgcolor(102, 255, 51)
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
score_p1 = 0
score_p2 = 0
#Scorecard
scorecard = turtle.Turtle()
scorecard.speed(0)
scorecard.color('black')
scorecard.penup()
scorecard.hideturtle()
scorecard.goto(0, 375)
scorecard.write('Player 1 Score: ' + str(score_p1), align='center', font = ('Raleway', 24, 'normal'))


scorecard = turtle.Turtle()
scorecard.speed(0)
scorecard.color('black')
scorecard.penup()
scorecard.hideturtle()
scorecard.goto(0, 330)
scorecard.write('Player 2 Score: ' + str(score_p2), align='center', font = ('Raleway', 24, 'normal'))


# Outline of the playing field
pencil = turtle.Turtle()
pencil.speed(0)
pencil.color('black')
pencil.penup()
pencil.hideturtle()
pencil.goto(650,310)
pencil.pendown()
pencil.goto(-650,310)
pencil.goto(-650,-400)
pencil.goto(650,-400)
pencil.goto(650,310)
pencil.penup()

p1 = turtle.Turtle()
p1.shape("turtle")
def move_up():                                                                                                 #Define movement functuons
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

moving = True
while moving == True:
    p1.forward(2)
    window.onkeypress(move_up, "Up")                                                                               #Bind the functions to specific keys
    window.onkeypress(move_down, "Down")
    window.onkeypress(turn_left, "Left")
    window.onkeypress(turn_right, "Right")
    window.listen()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
p2 = turtle.Turtle()
p2.shape("turtle")
def move_up_p2():                                                                                                 #Define movement functuons
    if p2.heading() != 270:
        p2.setheading(90)
        p2.speed(0)
def move_down_p2():
    if p2.heading() != 90:
        p2.setheading(270)
        p2.speed(0)
def turn_left_p2():
    if p2.heading_p2() != 0:
        p2.setheading(180)
        p2.speed(0)
def turn_right_p2():
    if p2.heading() != 180:
        p2.setheading(0)
        p2.speed(0)

movingp2 = True
while movingp2 == True:
    p2.forward(2)
    window.onkeypress(move_up_p2, "w")                                                                               #Bind the functions to specific keys
    window.onkeypress(move_down_p2, "s")
    window.onkeypress(turn_left_p2, "a")
    window.onkeypress(turn_right_p2, "d")
    window.listen()

p1.penup()
p2.penup()
p1.goto(-200,200)
p2.goto(200,-200)
p2.left(180)

window.mainloop()