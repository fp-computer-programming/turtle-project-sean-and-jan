#Author: Sean and Jan Salafia
import turtle   #imports turtle module
import random
import time

window = turtle.Screen()
window.title("Turtle Snake Score Race")   #title of window
window.colormode(255)
window.bgcolor(102, 255, 51)
window_open = True
#---------------------------------------------------------------------------------------------------------------

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
scorecard_p1.goto(0, 500)
scorecard_p1.write('Player 1 Score: ' + str(score_p1)+ "                     ", align='right', font = ('Raleway', 24, 'normal'))

scorecard_p2 = turtle.Turtle()
scorecard_p2.speed(0)
scorecard_p2.color('black')
scorecard_p2.penup()
scorecard_p2.hideturtle()
scorecard_p2.goto(0, 500)
scorecard_p2.write('                     Player 2 Score: ' + str(score_p2), align='left', font = ('Raleway', 24, 'normal'))

#----------------------------------------------------------------------------------------------------------------

# Outline of the playing field
border = turtle.Turtle()
border.speed(0)
border.shape('circle')
border.color('black')
border.penup()
border.hideturtle()
border.goto(800,500)
border.pendown()
border.goto(-800,500)
border.goto(-800,-500)
border.goto(800,-500)
border.goto(800,500)
border.penup()

#-----------------------------------------------------------------------------------------------------------------------
# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('DeepPink2')
food.penup()
food.goto(random.randint(-700,700),random.randint(-400,400))

#-----------------------------------------------------------------------------------------------------------------------
#Speed Food
speed_food = turtle.Turtle()
speed_food.speed(0)
speed_food.shape("triangle")
speed_food.color('azure1')
speed_food.penup()
speed_food.goto(random.randint(-700,700),random.randint(-400,400))
#-----------------------------------------------------------------------------------------------------------------------
# Snake Big Food
multi_food = turtle.Turtle()
multi_food.speed(0)
multi_food.shape("circle")
multi_food.color('black')
multi_food.penup()
multi_food.goto(random.randint(-700,700),random.randint(-400,400))
#-----------------------------------------------------------------------------------------------------------------------
#Snake Speed
p1_speed = 6
p2_speed = 6
#-----------------------------------------------------------------------------------------------------------------------
#Update Score
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
p1.goto(-700,400)

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
p2.goto(700,-400)
p2.left(180)

#-------------------------------------------------------------------------------------------------------------------------------
def endgamep1():
    p1.goto(0,0)
    p2.goto(0,0)
    window.clear()
    window.colormode(255)
    window.bgcolor(102, 255, 51)
    end_game_screen = turtle.Turtle()
    end_game_screen.speed(10)
    end_game_screen.hideturtle()
    end_game_screen.penup()
    end_game_screen.goto(-100,30)
    end_game_screen.color("black")
    end_game_screen.write("Game Over! P1 wins!", align='center', font=("Raleway",36),)
    screen.delay(100000)
    
def endgamep2():
    p1.goto(0,0)
    p2.goto(0,0)
    window.clear()
    window.colormode(255)
    window.bgcolor(102, 255, 51)
    end_game_screen = turtle.Turtle()
    end_game_screen.speed(10)
    end_game_screen.hideturtle()
    end_game_screen.penup()
    end_game_screen.goto(-100,30)
    end_game_screen.color("black")
    end_game_screen.write("Game Over! P2 wins!", align='center', font=("Raleway",36),)
    screen.delay(100000)
#-------------------------------------------------------------------------------------------------------------------------------

moving = True
def coordinates(player):
    x = player.xcor()
    y = player.ycor()
    return x, y
def movement():
    global p1
    global p2
    global moving

def pos_check(x,y,players):
    global moving
    global p1_xList
    global p1_yList
    global p2_xList
    global p2_yList
        
    if abs(x)> 800 or abs(y) > 500:
        moving = False
        window.clear()
        window.colormode(255)
        window.bgcolor(102, 255, 51)
        end_game_screen = turtle.Turtle()
        end_game_screen.speed(10)
        end_game_screen.hideturtle()
        end_game_screen.penup()
        end_game_screen.goto(-100,30)
        end_game_screen.color("black")
        end_game_screen.write("Someone went out of bounds before score threshold was reached. Please play again!", align='center', font=("Raleway",25),)
    
        
while moving != False:
    p1.forward(p1_speed)
    p2.forward(p2_speed)
    window.listen()
    window.onkeypress(move_up, "i")          #Bind p1 movement to specific keys
    window.onkeypress(move_down, "k")
    window.onkeypress(turn_left, "j")
    window.onkeypress(turn_right, "l")
    window.onkeypress(move_up_2, "w")         #Bind p2 movement to specific keys
    window.onkeypress(move_down_2, "s")
    window.onkeypress(turn_left_2, "a")
    window.onkeypress(turn_right_2, "d")
    x,y = coordinates(p1)
    pos_check(x, y, p1)
    x,y = coordinates(p2)
    pos_check(x, y, p2)
    
    if p1.distance(food) < 20:
        food.goto(random.randint(-700,700),random.randint(-400,400))
        score_p1 += 10
        if score_p1 >= 500:
            endgamep1()
        else:
            update_score_p1()
            continue
            
    if p1.distance(speed_food) < 20:
        p1_speed *= 1.1
        speed_food.goto(random.randint(-700,700),random.randint(-400,400))
        
    if p1.distance(multi_food) < 25:
        score_p1 += 20
        multi_food.goto(random.randint(-700,700),random.randint(-400,400))
        if score_p1 >= 500:
            endgamep1()
        else:
            update_score_p1()
            continue
#------------------------------------------------------------------------------------------------------------            
    if p2.distance(food) < 20:
        food.goto(random.randint(-700,700),random.randint(-400,400))
        score_p2 += 10
        if score_p2 >= 500:
            endgamep2()
        else:
            update_score_p2()
            continue
    if p2.distance(speed_food) < 20:
        p2_speed *= 1.1
        speed_food.goto(random.randint(-700,700),random.randint(-400,400))
        
    if p2.distance(multi_food) < 25:
        score_p2 += 20
        multi_food.goto(random.randint(-700,700),random.randint(-400,400))
        if score_p2 >= 500:
            endgamep2()
        else:
            update_score_p2()
            continue
#-----------------------------------------------------------------------------------------------------------

window.mainloop()
