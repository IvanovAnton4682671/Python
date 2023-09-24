
import turtle

def paintRow(x, y, r, g, b):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(r, g, b)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

def paintStar(x, y, r, g, b):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(r, g, b)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(105)
        turtle.right(144)
    turtle.end_fill()

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor(0.5, 0.5, 0.5)
screen.title("Flag of Ghana")

paintRow(-250, 175, 1.0, 0.0, 0.0)
paintRow(-250, 75, 1.0, 1.0, 0.0)
paintRow(-250, -25, 0.0, 1.0, 0.0)

paintStar(-55, 37, 0.0, 0.0, 0.0)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

screen.exitonclick()
