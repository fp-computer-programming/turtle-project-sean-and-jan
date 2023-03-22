#Author: Sean and Jan Salafia
import turtle   #imports turtle module
import random   #imports random module 

window = turtle.Screen()                  #Sets up screen
window.title("Turtle Snake Score Race")   #title of window
window.colormode(255)                      #Allows for  colors
window.bgcolor(102, 255, 51)              #Sets Background Color
#window_open = True

#----------------------------------------------------------------------------------------------------------------         
# This chunk of code automatically defaults the screen to fullscreen. Taken from stackoverflow
screen = turtle.Screen()            #sets screen
screen.setup(width = 1.0, height = 1.0)     
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
#----------------------------------------------------------------------------------------------------------------
#Scorecard

score_p1 = 0                            #Establishes starting score for p1
score_p2 = 0                            #Establishes starting score for p2
scorecard_p1 = turtle.Turtle()          #Creates turtle for the p1 scorecard
scorecard_p1.speed(0)                   #Instant drawing
scorecard_p1.color('black')             #Color
scorecard_p1.penup()                    #Penup
scorecard_p1.hideturtle()               #Hides Turtle
scorecard_p1.goto(0, 500)               #Coordinates
scorecard_p1.write('Player 1 Score: ' + str(score_p1)+ "                     ", align='right', font = ('Raleway', 24, 'normal'))    #Writes

scorecard_p2 = turtle.Turtle()       #Creates turtle for the p2 scorecard  
scorecard_p2.speed(0)                #Instant drawing
scorecard_p2.color('black')          #Color          
scorecard_p2.penup()                 #Penup         
scorecard_p2.hideturtle()            #Hides Turtle   
scorecard_p2.goto(0, 500)            #Coordinates    
scorecard_p2.write('                     Player 2 Score: ' + str(score_p2), align='left', font = ('Raleway', 24, 'normal')) #Writes

#----------------------------------------------------------------------------------------------------------------

# Outline of the playing field
border = turtle.Turtle()     #Establishes the border                  
border.speed(0)              #Establishes the border  
border.shape('circle')       #Establishes the border         
border.color('black')        #Establishes the border        
border.penup()               #Establishes the border 
border.hideturtle()          #Establishes the border      
border.goto(800,500)         #Establishes the border       
border.pendown()             #Establishes the border   
border.goto(-800,500)        #Establishes the border        
border.goto(-800,-500)       #Establishes the border         
border.goto(800,-500)        #Establishes the border        
border.goto(800,500)         #Establishes the border       
border.penup()               #Establishes the border 

#-----------------------------------------------------------------------------------------------------------------------
# Snake Food
food = turtle.Turtle()                                       #Establishes pink squares as food                  
food.speed(0)                                                #Establishes pink squares as food         
food.shape("square")                                         #Establishes pink squares as food                
food.color('DeepPink2')                                      #Establishes pink squares as food                   
food.penup()                                                 #Establishes pink squares as food        
food.goto(random.randint(-700,700),random.randint(-400,400)) #Establishes pink squares as food                                                        

#-----------------------------------------------------------------------------------------------------------------------
#Speed Food
speed_food = turtle.Turtle()                                         #Establishes white triange as speed boost (+10%)                               
speed_food.speed(0)                                                  #Establishes white triange as speed boost (+10%)                   
speed_food.shape("triangle")                                         #Establishes white triange as speed boost (+10%)                               
speed_food.color('azure1')                                           #Establishes white triange as speed boost (+10%)                           
speed_food.penup()                                                   #Establishes white triange as speed boost (+10%)                   
speed_food.goto(random.randint(-700,700),random.randint(-400,400))   #Establishes white triange as speed boost (+10%)                                                                   
#-----------------------------------------------------------------------------------------------------------------------
# Snake Big Food
multi_food = turtle.Turtle()                                       #Establishes black circle as +20 points               
multi_food.speed(0)                                                #Establishes black circle as +20 points      
multi_food.shape("circle")                                         #Establishes black circle as +20 points             
multi_food.color('black')                                          #Establishes black circle as +20 points            
multi_food.penup()                                                 #Establishes black circle as +20 points     
multi_food.goto(random.randint(-700,700),random.randint(-400,400)) #Establishes black circle as +20 points                                                     
#-----------------------------------------------------------------------------------------------------------------------
#Snake Speed
p1_speed = 6            #sets flat value speed
p2_speed = 6            #sets flat value speed
#-----------------------------------------------------------------------------------------------------------------------
#Update Score
def update_score_p1():                                                                                           #Function to update scorecard       
    scorecard_p1.clear()                                                                                         #Function to update scorecard         
    scorecard_p1.write('Player 1 Score: ' + str(score_p1), align='center', font = ('Raleway', 24, 'normal'))     #Function to update scorecard                                                                                             
def update_score_p2():                                                                                           #Function to update scorecard       
    scorecard_p2.clear()                                                                                         #Function to update scorecard         
    scorecard_p2.write('Player 2 Score: ' + str(score_p2), align='center', font = ('Raleway', 24, 'normal'))     #Function to update scorecard                                                                                             
#-----------------------------------------------------------------------------------------------------------------------

p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("red")

def move_up():                          #p1 can't move down if it is moving up
    if p1.heading() != 270:
        p1.setheading(90)
        p1.speed(0)
def move_down():                        #p1 can't move up if it is moving down
    if p1.heading() != 90:
        p1.setheading(270)
        p1.speed(0)
def turn_left():                        #p1 can't move right if it is moving left
    if p1.heading() != 0:
        p1.setheading(180)
        p1.speed(0)
def turn_right():                       #p1 can't move left if it is moving right
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
def move_up_2():              #Define movement functions
    if p2.heading() != 270:                         #p1 can't move down if it is moving up
        p2.setheading(90)
        p2.speed(0)
def move_down_2():                                   #p1 can't move up if it is moving down
    if p2.heading() != 90:
        p2.setheading(270)
        p2.speed(0)
def turn_left_2():                                  #p1 can't move right if it is moving left
    if p2.heading() != 0:
        p2.setheading(180)
        p2.speed(0)
def turn_right_2():                                  #p1 can't move left if it is moving right
    if p2.heading() != 180:
        p2.setheading(0)
        p2.speed(0)
p2.penup()
p2.goto(700,-400)       #go to
p2.left(180)            #turn around

#-------------------------------------------------------------------------------------------------------------------------------
def endgamep1():                    #creates an endgame screen for p1 as the winner
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
    
def endgamep2():                     #creates an endgame screen for p2 as the winner
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

moving = True                       #sets moving as always true
def coordinates(player):
    x = player.xcor()               #takes x coords
    y = player.ycor()               #takes y cords
    return x, y
def movement():                     #defines movement
    global p1                       #sets global for p1                 
    global p2                       #sets global for p2                
    global moving                   #sets global for moving                      

def pos_check(x,y,players):         #defines position check
    global moving
        
    if abs(x)> 800 or abs(y) > 500:                  
        moving = False                                      #if turtle exceed borders, set movement to false                                                                                                      
        window.clear()                                      #clear window                                                                                                       
        window.colormode(255)                               #                                                                                                               
        window.bgcolor(102, 255, 51)                        #remake colors                                                                                                                      
        end_game_screen = turtle.Turtle()                   #make new turtle                                                                                                                           
        end_game_screen.speed(10)                           #Set screen for replay game                                                                                                                   
        end_game_screen.hideturtle()                        #Set screen for replay game                                                                                                                      
        end_game_screen.penup()                             #Set screen for replay game                                                                                                                 
        end_game_screen.goto(-100,30)                       #Set screen for replay game                                                                                                                       
        end_game_screen.color("black")                      #Set screen for replay game                                                                                                                        
        end_game_screen.write("Someone went out of bounds before score threshold was reached. Please play again!", align='center', font=("Raleway",25),)                                                                                                                                               
    
        
while moving != False:                                                        #MAIN       
    p1.forward(p1_speed)                                    #speed p1 is flexible
    p2.forward(p2_speed)                                    #speed p2 is flexible
    window.listen()                                         #listens for inputs
    window.onkeypress(move_up, "i")          #Bind p1 movement to specific keys
    window.onkeypress(move_down, "k")
    window.onkeypress(turn_left, "j")
    window.onkeypress(turn_right, "l")
    window.onkeypress(move_up_2, "w")         #Bind p2 movement to specific keys
    window.onkeypress(move_down_2, "s")
    window.onkeypress(turn_left_2, "a")
    window.onkeypress(turn_right_2, "d")
    x,y = coordinates(p1)                        #Postion checks p1                          
    pos_check(x, y, p1)                          #Postion checks p1                      
    x,y = coordinates(p2)                        #Postion checks p2                          
    pos_check(x, y, p2)                          #Postion checks p2                     
    
    if p1.distance(food) < 20:                                              #When turtle within 20 units
        food.goto(random.randint(-700,700),random.randint(-400,400))        #Teleport food to random cords
        score_p1 += 10                                                      #Add 10 score
        if score_p1 >= 500:                                                 #Check if 500 points is exceeded
            endgamep1()                                                     #If yes, go endgame
        else:                                                               #If no, update score
            update_score_p1()
            continue
                                                                                                  
    if p1.distance(speed_food) < 20:                                          #If within 20 units                                                                                      
        p1_speed *= 1.1                                                       #10% speed boost                              
        speed_food.goto(random.randint(-700,700),random.randint(-400,400))    #Teleport speed shape to random cords                                                                                  
                                                                                                
    if p1.distance(multi_food) < 25:                                          #if within 25 units of multifood                                              
        score_p1 += 20                                                        #add 20 points                              
        multi_food.goto(random.randint(-700,700),random.randint(-400,400))    #teleport to random cords                                                                                  
        if score_p1 >= 500:                                                                                 
            endgamep1()                                                       #Check if 500 points is exceeded                           
        else:                                                                 #If yes, go endgame                   
            update_score_p1()                                                 #If no, update score                                   
            continue                                                                                         
#------------------------------------------------------------------------------------------------------------            
    if p2.distance(food) < 20:                                                #When turtle within 20 units                                                                                      
        food.goto(random.randint(-700,700),random.randint(-400,400))          #Teleport food to random cords                                                                                                                              
        score_p2 += 10                                                        #Add 10 score                                                                              
        if score_p2 >= 500:                                                   #Check if 500 points is exceeded                                                                                
            endgamep2()                                                                                                                                     
        else:                                                                 #If yes, go endgame                                                                  
            update_score_p2()                                                 #If no, update score                                                                                  
            continue                                                                                                                                        
    if p2.distance(speed_food) < 20:                                           #If within 20 units                                                                                              
        p2_speed *= 1.1                                                        #10% speed boost                                                                               
        speed_food.goto(random.randint(-700,700),random.randint(-400,400))     #Teleport speed shape to random cords                                                                                                                                 
                                                                                                                                                
    if p2.distance(multi_food) < 25:                                           #if within 25 units of multifood                                                                                             
        score_p2 += 20                                                         #add 20 points                                                                             
        multi_food.goto(random.randint(-700,700),random.randint(-400,400))     #teleport to random cords                                                                                                                                 
        if score_p2 >= 500:                                                    #Check if 500 points is exceeded                                                                                 
            endgamep2()                                                        #If yes, go endgame                                                                             
        else:                                                                  #If no, update score                                                                      
            update_score_p2()                                                                                                                                       
            continue                                                                                                                                        
#-----------------------------------------------------------------------------------------------------------

window.mainloop()       #Go time
