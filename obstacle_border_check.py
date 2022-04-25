#Border Checking for Horizontal Obstacles
def h_obstacle_border(x_list):
    """
    h_obstacle_border takes in a list of objects and makes sure they don't go outside a certain boundary horizontally

    :x_list: a list of objects moving horizontal
    """
    for i in x_list:
        if i.xcor() > -20:
            i.setx(-20)
            i.dx *= -1
        if i.xcor() < -400:
            i.setx(-400)
            i.dx *= -1


#Border Checking for Vertical Obstacles
#Since different vertical objects have different boundaries I split this function to specifically add borders to only certain objects
def v_obstacle_border(x_list):
    """
    v_obstacle_border takes in a list of objects and makes sure they don't go outside a certain boundary vertically

    :x_list: a list of objects moving vertical
    """
    for i in x_list[0:5]:
        if i.ycor() > 300:
            i.sety(300)
            i.dy *= -1
        if i.ycor() < 20:
            i.sety(20)
            i.dy *= -1

    for i in x_list[5:10]:
        if i.ycor() > -20:
            i.sety(-20)
            i.dy *= -1
        if i.ycor() < -205:
            i.sety(-205)
            i.dy *= -1

    for i in x_list[10:13]:
        if i.ycor() > 300:
            i.sety(300)
            i.dy *= -1
        if i.ycor() < -205:
            i.sety(-205)
            i.dy *= -1
