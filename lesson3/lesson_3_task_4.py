from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

def ring(color, rad):
  my_turtle.fillcolor(color)
  my_turtle.begin_fill()
  my_turtle.circle(rad)
  my_turtle.end_fill()

def oval(r, color):
  my_turtle.fillcolor(color)
  my_turtle.begin_fill()          
  my_turtle.right(45)
  for loop in range(2):
    my_turtle.circle(r,90)
    my_turtle.circle(r/2,90)
  my_turtle.end_fill()

# draw left ear
my_turtle.up()
my_turtle.setpos(-55, 65)
my_turtle.down()
ring('black', 20)

# draw right ear
my_turtle.up()
my_turtle.setpos(65, 65)
my_turtle.down()
ring('black', 20)

# draw face
my_turtle.up()
my_turtle.setpos(-80, -30)
my_turtle.down()
oval(120, 'white')

# draw left black eye
my_turtle.up()
my_turtle.setpos(-45, 30)
my_turtle.down()
ring('black', 15)

# draw right black eye
my_turtle.up()
my_turtle.setpos(35, 30)
my_turtle.down()
ring('black', 15)

# draw left white eye
my_turtle.up()
my_turtle.setpos(-45, 33)
my_turtle.down()
ring('white', 5)

# draw right white eye
my_turtle.up()
my_turtle.setpos(35, 33)
my_turtle.down()
ring('white', 5)

# draw left cheek
my_turtle.up()
my_turtle.setpos(-75, -10)
ring('pink', 20)

# draw right cheek
my_turtle.up()
my_turtle.setpos(55, -10)
ring('pink', 20)

# draw nose
my_turtle.up()
my_turtle.setpos(-4, -4)
my_turtle.down()
ring('black', 8)

# draw mouth
my_turtle.up()
my_turtle.setpos(2, 0)
my_turtle.width(3)
my_turtle.down()
my_turtle.right(60)
my_turtle.circle(10, 180)
my_turtle.up()
my_turtle.setpos(2, 0)
my_turtle.down()
my_turtle.left(40)
my_turtle.circle(10, -180)

my_turtle.hideturtle()
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()