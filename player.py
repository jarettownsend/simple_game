import turtle
from screen import wn

#Player object
player = turtle.Turtle()
player.speed(0)
player.shape('circle')
player.color('blue')
player.penup()
player.goto(-200, -275)

#Player Movement Functions
def player_up():
    y = player.ycor()
    y += 15
    player.sety(y)

def player_down():
    y = player.ycor()
    y -= 15
    player.sety(y)

def player_right():
    x = player.xcor()
    x += 15
    player.setx(x)

def player_left():
    x = player.xcor()
    x -= 15
    player.setx(x)

#Keyoard inputs
wn.listen()
wn.onkeypress(player_up, "Up")
wn.onkeypress(player_down, "Down")
wn.onkeypress(player_right, "Right")
wn.onkeypress(player_left, "Left")
