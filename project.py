import turtle as turtle
import random
import time # python3 -m pip install time
import keyboard # python3 -m pip install keyboard
from playsound import playsound # python3 -m pip install playsound
from PIL import Image # python3 -m pip install Pillow
'''
        T-DAY: Invasion of Turt
    Project 1.1.9
    Created by Vlad Druia and Peyton Slape

        Note for Playsound:
    Directories should be changed to where the soundfiles
    are. It will not work otherwise.
'''

# initialize arrays for projectiles, turtles
enemyTurtles = []
projTurts = []

# Defines the arrays for the width, length, and color of enemy turtles
enTSizeA = [1,2,3,4,5]
enTSizeB = [1,2,3,4,5]
enTSizeC = [2,4,6,8,10]
enCol = ["blue", "red", "blue", "green", "black", "white"]
wn = turtle.Screen()
    # initializes the screen



xStart = 100
    # sets the start coordinates for turtles    
yStart = [-200, -150, -100, -50, 0, 50, 100, 150, 200]

# Unused section of code used to create a kill counter
# currently not finished and I do not plan on finishing it
'''kills = turtle.Turtle()
kills.hideturtle()
kills.penup()
kills.goto(0,250)
kills.pendown()'''




def turtAdd(en):
    '''
    This method is called during the main loop
    every 8 seconds. There may be an ongoing bug
    due to the nature of the if loop in main which
    calls this method multiple times while near 8
    seconds. Bug should be kept in to allow for
    multiple turtles spawning.

    This method uses the turtle inputed (en) and
    moves it to one of the starting locations.
    Afterward, it changes the size to one of the
    random sizes in enTSizeA (width), enTSizeB
    (length), and enTSizeC (outline size). 
    It also selects a random color from the array 
    enCol.

    Afterward, it shows the turtle and adds it to
    the enemyTurtles array.
    '''
    
    en.penup()
    en.shape("turtle")
    en.hideturtle()
    en.resizemode("user")
    en.shapesize(random.choice(enTSizeA), random.choice(enTSizeB), random.choice(enTSizeC))
    en.color(random.choice(enCol))
    en.setpos(300, random.choice(yStart))
    en.showturtle()
    enemyTurtles.append(en)



def colCheck(proj, enemy):
    '''
    This method checks, for each projectile in the array proj,
    and for each enemy turtle in the array enemy, if 
    they are within 40px of each other, regardless
    of turtle size.

    If collision is detected, it plays the screaming
    turtle sound effect, followed by moving both
    turtles off screen and hiding them.
    It also removes them from the collision checker
    arrays.
    '''
    for pr in proj:
        for en in enemy:
            # checks if projecticle hits turtle
            if pr.distance(en) < 40:
                #hides and stops turtles from moving
                playsound('H:\Principles\\Python\\Unit 1\\1.1.9 Project\\sound\\scream.mp3')
                en.hideturtle()
                pr.hideturtle()
                
                pr.penup()
                pr.goto(500,0)
                proj.remove(pr)

                en.goto(500,0)
                en.seth(0)
                enemy.remove(en)
                

def enMove(enemy):
    '''
    This code is called in the primary loop.
    It moves each enemy turtle forward 10px.
    The code also ensures the turtles are always
    heading toward the wall, just in case.
    '''
    for en in enemy:
        en.setheading(180)
            # ensures they are always moving the right direction
        en.forward(10)
            # for each enemy, it moves it forward 20

def projMove(projTurt):
    '''
    Cycles through each projectile in projTurt.
    For each projectile, it moves the projectile
    forward 50px.

    Each projectile leaves a trail which is cleared
    after movement.

    The final if statement in the code checks if
    the projectile is off the screen. If it is,
    it stops the projectile from moving and hides it.
    '''
    for pr in projTurt:
        pr.forward(50)
        pr.clear()
        if pr.xcor() > 410:
            # checks if the projectile is out of bounds
            pr.hideturtle()
            projTurt.remove(pr)
            # hides and stops projectile from moving

def healthBar(curHelth):
    '''
    This method runs whenever Player.TakeDamage()
    is called, and to initialize the program.

    It creates a black underline which a red bar
    overtop. The red bar represents the amount
    of health as a percentage. The max health
    is 100, and each 1 health is 2 pixels 
    (inner health bar is 200 px long)
    '''
    # This creates the healthbar
    health = turtle.Turtle()
    health.penup()
    health.hideturtle()
    health.goto(0, 300)
    # creates black underline
    health.color("black")
    health.pensize(30)
    health.pendown()
    health.goto(200,300)
    health.penup()
    health.goto(0,300)
    # creates red overlay, represents health amount
    health.color("red")
    health.pendown()
    health.pensize(20)
    # sets the amount the health bar should fill to
    healthCor = int((curHelth / 100) * 200)
    if(curHelth != 0):
        '''
        As long as the health is NOT zero, 
        the inner bar will refill the red to 
        the current health.
        '''
        health.goto(healthCor, 300)

boom = turtle.Turtle()
    # initializes the explosion creator turtle
boom.hideturtle()

def wallcolchek(turtles):
    #checks if turtles are colliding with wall
    for turt in turtles:
        if(turt.distance(-300, turt.ycor()) < 20):    
            turtles.remove(turt)
                # stops turtle from moving
            Player.takeDamage(20)
            # calls takeDamage method in the Player class
            boom.penup()
            boom.speed(0)
            boom.goto(turt.pos())
            boom.pensize(60)
            boom.color("red")
            boom.pendown()
            playsound('H:\Principles\\Python\\Unit 1\\1.1.9 Project\\sound\\exp.wav')
                # plays the explosion sound from the sound folder
            boom.circle(5)
                # creates the explosion circle
            turt.hideturtle()
                # hides the turtle
            time.sleep(0.2)
                # waits 0.2 seconds before clear
            boom.clear()
                
    
def intro():
    '''
    This intro method runs during the initialization
    of the game. It shows the text T-DAY in the 
    center of the screen right before loading the
    beach.
    '''
    tday = turtle.Turtle()
    tday.speed(3)
    tday.pensize(5)
    tday.hideturtle()
    tday.penup()
    tday.pendown()
    tday.write("T-DAY", align='center', font=('Verdana', '100', 'normal'))
        # creates text which says T-DAY

def makeBeech():
    '''
    First, this method creates the blue water section
    on the right side of the screen. Then, the 
    program creates, line by line, the beach. 
    Each line in the beach is 100px wide, and 
    spans the full 1000px of the screen.

    Finally, it constructs the wall on the left
    side of the screen. The wall is 25px wide.

    '''
    xpos = -400
    beach = turtle.Turtle()
    beach.speed(0)
    beach.penup()
    beach.hideturtle()
    beach.pensize(100)
    beach.goto(400,400)
    beach.pendown()
    beach.color("blue")
    beach.goto(400,-400)
    for lines in range(8):
        #Creates beach on left side
        beach.penup()
        beach.goto(xpos, 400)
        beach.pendown()
        beach.color("yellow")
        beach.goto(xpos, -400)
        xpos += 100
    # below constructs wall
    beach.penup()
    beach.pensize(25)
    beach.goto(-300, 400)
    beach.color("black")
    beach.pendown()
    beach.goto(-300,-400)

intro()
    # calls the intro method
time.sleep(2)
    # waits 2 seconds
makeBeech()
    # calls the beach creating method


player = turtle.Turtle()

    #Player class
class Player:
    '''
    The player class stores all of the information
    about the player (minus the player turtle).

    It also moves the player to their starting
    position.

    Three methods are contained within this class.
    
    The first is takeDamage(). This class accepts
    one argument, named dmgAmount. This method
    reduces Player.currentHealth() by dmgAmount,
    then calls the healthBar method.
    Positive numbers for dmgAmount deal damage.
    Negative numbers for dmgAmount would,
    theoretically, heal the player.

    The second method is movUp(). It does not take
    any arguments. This method moves the player
    10px up when called.

    The third method is movDown(). It does not take
    any arguments. It moves the player 10px down
    when called.
    '''
    maxHealth = 100
    currentHealth = 100
    
    player.penup()
    player.seth(90)
        # ensures player heading is facing correct directions
    #creates the player object
    player.shape("circle")
    player.goto(-400,0)
    def takeDamage(dmgAmount):
        # method which changes the player health based on the damage taken
        # negative values heal, positive values deal damage
        Player.currentHealth -= dmgAmount
        healthBar(Player.currentHealth)
            # healthBar method is called
    def movUp():
        player.forward(10)
            # moves the player turtle up
    def movDown():
        player.back(10)
            # moves the player turtle down



healthBar(Player.currentHealth)
#playsound('H:\Principles\\Python\\Unit 1\\1.1.9 Project\\sound\\music.mp3')
gameRun = True
while(gameRun):
    if((int(time.monotonic()) % 8 ) == 0):
        # every 8 seconds, it should add a new turtle
        enemyT = turtle.Turtle()
        turtAdd(enemyT)
    if keyboard.is_pressed("w"):
        # when [w] is pressed, it calls Player.movUp()
        Player.movUp()
    if keyboard.is_pressed("s"):
        # when [s] is pressed, it calls Player.movDown()
        Player.movDown()
    if keyboard.is_pressed("space"):
        # creates a projectile turtle when [space] is pressed
        playsound('H:\Principles\\Python\\Unit 1\\1.1.9 Project\\sound\\pew.mp3')
            # plays weapon fire sound
        proj = turtle.Turtle()
        proj.speed(0)
        proj.penup()
        proj.hideturtle()
        proj.setpos(-400, player.ycor())
            # sets position to the player's position
        proj.pendown()
        proj.showturtle()
        proj.speed(1)
        projTurts.append(proj)
            # adds the projectile to the movement list

    # BELOW: see parent methods for more info
    colCheck(projTurts, enemyTurtles)
    wallcolchek(enemyTurtles)
    enMove(enemyTurtles)
    projMove(projTurts)
    if(Player.currentHealth <= 0):
        gameRun = False
        # stops game if the health is reaches zero


def end():
    '''
    This endgame method called end() is called
    after gameRun becomes false. When called,
    it first creates a rectangle around the screen
    before filling the entire screen with red.
    It then puts the text "GAME OVER" onto the screen
    over the red fill. The turtle then moves to the
    center and turns pink.

    '''
    endgame = turtle.Turtle()
    endgame.shape("turtle")
    endgame.speed(0)
    endgame.color('red')
    endgame.penup()
    endgame.goto(-500,500)
    endgame.pendown()
    endgame.begin_fill()
    for _ in range(4):
        endgame.forward(1000)
        endgame.right(90)
        # creates outline around screen
    endgame.end_fill()
        # fills in the shape created
    endgame.goto(0,0)
    endgame.color("black")
    endgame.write("GAME OVER", align='center', font=('Verdana', '100', 'normal'))
        # writes GAME OVER on the screen
    endgame.color("pink")
        # creates a pink turtle in the center
        # prints out the game over screen
end()
wn.mainloop()
    # makes the screen persistant