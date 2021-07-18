import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(0,20):
    for colors in ["Blue","White"]:
        turtle.color(colors)
        turtle.circle(200)
        turtle.left(10)

turtle.hideturtle()
turtle.forward(30)
turtle.showturtle()
for i in range(0,35):
    for colors in ["white"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(10)

