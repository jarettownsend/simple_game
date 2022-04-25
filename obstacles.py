import turtle


#Setting up Horizontal Obstacle class
#For this game it's easier to seperate horiztonal and vertical obstacles because the obstacles only go one of two ways (dx or dy)
class h_obstacle(turtle.Turtle):
     def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('red')
        self.shape('square')
        self.penup()
        self.dx = 2.5

#Setting up Horizontal Obstacles
h_obstacle1 = h_obstacle()
h_obstacle1.goto(-400, 200)

h_obstacle2 = h_obstacle()
h_obstacle2.goto(-300, 150)

h_obstacle3 = h_obstacle()
h_obstacle3.goto(-200, 100)

h_obstacle4 = h_obstacle()
h_obstacle4.goto(-100, 50)

h_obstacle5 = h_obstacle()
h_obstacle5.goto(-20, 0)

h_obstacle6 = h_obstacle()
h_obstacle6.goto(-400, -50)

h_obstacle7 = h_obstacle()
h_obstacle7.goto(-300, -100)

h_obstacle8 = h_obstacle()
h_obstacle8.goto(-200, -150)

h_obstacle9 = h_obstacle()
h_obstacle9.goto(-100, -200)

h_obstacle10 = h_obstacle()
h_obstacle10.goto(-20, -250)

#Setting up Vertical Obstacle Class
class v_obstacle(turtle.Turtle):
     def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('red')
        self.shape('square')
        self.penup()
        self.dy = 2.5

#Setting up Vertical Obstacles
v_obstacle1 = v_obstacle()
v_obstacle1.goto(50, 20)

v_obstacle2 = v_obstacle()
v_obstacle2.goto(100, 300)

v_obstacle3 = v_obstacle()
v_obstacle3.goto(150, 50)

v_obstacle4 = v_obstacle()
v_obstacle4.goto(200, 250)

v_obstacle5 = v_obstacle()
v_obstacle5.goto(250, 100)

v_obstacle6 = v_obstacle()
v_obstacle6.goto(50, -20)

v_obstacle7 = v_obstacle()
v_obstacle7.goto(100, -210)

v_obstacle8 = v_obstacle()
v_obstacle8.goto(150, -50)

v_obstacle9 = v_obstacle()
v_obstacle9.goto(200, -150)

v_obstacle10 = v_obstacle()
v_obstacle10.goto(250, -100)

v_obstacle11 = v_obstacle()
v_obstacle11.goto(320, 100)

v_obstacle12 = v_obstacle()
v_obstacle12.goto(350, 0)

v_obstacle13 = v_obstacle()
v_obstacle13.goto(380, -100)

#Setting up Obstacle Lists
#I am setting them up in a list so I can iterate through the list in a later function to make them all do things instead of calling them individually
h_obstacle_list = [h_obstacle1, h_obstacle2, h_obstacle3, h_obstacle4, h_obstacle5, h_obstacle6, h_obstacle7, h_obstacle8, h_obstacle9, h_obstacle10]
v_obstacle_list = [v_obstacle1, v_obstacle2, v_obstacle3, v_obstacle4, v_obstacle5, v_obstacle6, v_obstacle7, v_obstacle8, v_obstacle9, v_obstacle10, v_obstacle11, v_obstacle12, v_obstacle13]
all_obstacle_list = h_obstacle_list + v_obstacle_list
