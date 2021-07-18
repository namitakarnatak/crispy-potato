import turtle
turtle.bgcolor("blue")
turtle.pensize(2)
turtle.speed(0)
turtle.penup()
turtle.goto(600,250)
turtle.pendown()
for i in range(0,20):
    for colors in ["Blue","White"]:
        turtle.color(colors)
        turtle.circle(70)
        turtle.left(10)
turtle.hideturtle()
turtle.forward(30)
turtle.penup()
#turtle.showturtle()

turtle.goto(-600,250)
turtle.pendown()
for i in range(0,20):
    for colors in ["Blue","White"]:
        turtle.color(colors)
        turtle.circle(70)
        turtle.left(10)
turtle.hideturtle()
turtle.forward(30)
turtle.penup()
#turtle.showturtle()

turtle.goto(-600,-250)
turtle.pendown()
for i in range(0,20):
    for colors in ["Blue","White"]:
        turtle.color(colors)
        turtle.circle(70)
        turtle.left(10)
turtle.hideturtle()
turtle.forward(30)
turtle.penup()

turtle.goto(600,-250)
turtle.pendown()
for i in range(0,20):
    for colors in ["Blue","White"]:
        turtle.color(colors)
        turtle.circle(70)
        turtle.left(10)
turtle.hideturtle()
turtle.forward(30)
turtle.penup()

turtle.goto(0,0)
turtle.pendown()
turtle.write("Gratitude",move=True,align="center",font=("Arial",100,"italic"))





