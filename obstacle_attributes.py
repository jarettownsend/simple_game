#Move the Horizontal Obstacles
def h_move(x_list):
    """
    h_move iterates though a list and makes them move horiztonal

    :param x_list: a list of objects that need to move
    """
    for i in x_list:
        i.setx(i.xcor() + i.dx)

#Move the Vertical Obstacles
def v_move(y_list):
    """
    v_move iterates though a list and makes them move vertical

    :param y_list: a list of objects that need to move
    """
    for i in y_list:
        i.sety(i.ycor() + i.dy)

#Collisions for Obstacles and Player
def collision(i, player, death_count, death_label):
    """
    collision takes the player and returns them to their starting spot when they run into an obstacle. It also adds 1 to the death count

    :i: An obstacle from the game
    :player: The player of the game
    :death_count: the variable that keeps track of death count
    :death_label: The label in the top left corner of the screen
    :return: Function returns the death count as to keep it updated properly
    """
    if (player.ycor() > i.ycor() - 20 and player.ycor() < i.ycor() + 20) and (player.xcor() < i.xcor() + 20 and player.xcor() > i.xcor() - 20):
        player.setx(-200)
        player.sety(-275)
        death_count += 1
        death_label.clear()
        death_label.write(f'Deaths: {death_count}', align='center', font=("Courier", 24, "normal"))
    return death_count
