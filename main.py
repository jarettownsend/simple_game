import turtle

#Everything to set up Game
from screen import *
from obstacles import *
from player import *

#Everything inside Main Game Loop
from obstacle_attributes import h_move, v_move, collision
from obstacle_border_check import h_obstacle_border, v_obstacle_border
from player_border_check import player_borders_check, player_walls_check

#Main Game Loop
break_condition = True
while break_condition:
    wn.update()

    #These functions move the obstacles
    h_move(h_obstacle_list)
    v_move(v_obstacle_list)

    #These functions keep the obstacles within a certain boundary
    h_obstacle_border(h_obstacle_list)
    v_obstacle_border(v_obstacle_list)

    #These functions keep the player within a certain boundary
    player_borders_check(player)
    player_walls_check(player)

    #This function moves the player back to the begining if they touch an obstacle
    for i in all_obstacle_list:
        death_count = collision(i, player, death_count, death_label)

    #This loop ends the game if the player gets to the winning square
    if player.ycor() < -230 and player.xcor() > 325:
        break_condition = False
