import turtle
passi=1
for i in range(250):
    for colors in ["black","yellow","blue"]:
        turtle.speed(0)
        #turtle.hideturtle()
        #turtle.pensize(10)
        turtle.circle(70)
        turtle.color(colors)
        turtle.forward(passi)
        turtle.left(20)
        turtle.right(90)
        turtle.left(30)
        turtle.circle(150)
        passi=passi+1
turtle.forward(120)
turtle.pendown()
turtle.right(90)
turtle.write("Happy Birthday",font=("Times"))
    

