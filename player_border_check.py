#Boarder Checking for player
def player_borders_check(player):
    """
    player_borders_check keeps the player within the Screen

    :player: the object playing the game
    """
    if player.xcor() < -390:
        player.setx(-390)
    if player.xcor() > 390:
        player.setx(390)
    if player.ycor() < -290:
        player.sety(-290)
    if player.ycor() > 290:
        player.sety(290)

#Boarding Checking for Player with Maze Walls
#Because the walls are just objects on the screen, I hard coded their cordinates into this function
def player_walls_check(player):
    """
    player_walls_check keeps the player out of the walls on the screen

    :player: the object playing the game
    """
    if (player.xcor() > -20 and player.xcor() < 0) and (player.ycor() < 230):
        player.setx(-20)
    if (player.xcor() < 20 and player.xcor() > 0) and (player.ycor() < 230):
        player.setx(20)

    if (player.xcor() > 0 and player.xcor() < 310) and (player.ycor() < 25 and player.ycor() > 0):
        player.sety(25)
    if (player.xcor() > 0 and player.xcor() < 310) and (player.ycor() < 0 and player.ycor() > -25):
        player.sety(-25)

    if (player.xcor() > 100 and player.xcor() < 400) and (player.ycor() < -200 and player.ycor() > -225):
        player.sety(-200)
    if (player.xcor() > 100 and player.xcor() < 400) and (player.ycor() < -225 and player.ycor() > -250):
        player.sety(-250)
