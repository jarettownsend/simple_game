import turtle

#Setting up the screen
wn = turtle.Screen()
wn.title("Maze")
wn.bgcolor("white")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Setting up the winning square. This will just be a green square in the bottom corner of the screen
wsquare = turtle.Turtle()
wsquare.speed(0)
wsquare.shape('square')
wsquare.color('green')
wsquare.penup()
wsquare.goto(360,-260)
wsquare.shapesize(stretch_wid=3, stretch_len=3)


#Setting up a class for walls
class wall(turtle.Turtle):
    def __init__(self):
       super().__init__()
       self.speed(0)
       self.color('black')
       self.shape('square')
       self.penup()

#Setting up each wall using the wall class
wall1 = wall()
wall1.shapesize(stretch_wid=27, stretch_len=1)
wall1.goto(0, -50)

wall2 = wall()
wall2.shapesize(stretch_wid=1, stretch_len=15)
wall2.goto(150, 0)

wall3 = wall()
wall3.shapesize(stretch_wid=1, stretch_len=15)
wall3.goto(250, -225)

#Setting up the death count label in the top left corner. The variable death_count will keep this label dynamic
death_count = 0
death_label = turtle.Turtle()
death_label.speed(0)
death_label.color('blue')
death_label.penup()
death_label.hideturtle()
death_label.goto(-300, 260)
death_label.write(f'Deaths: {death_count}', align='center', font=("Courier", 24, "normal"))
