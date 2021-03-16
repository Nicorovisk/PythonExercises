import turtle

color = (["green", "yellow", "red"])

for i in range(0, 3):
    turtle.color("black", color[i])
    turtle.begin_fill()

    for j in range(0, 4):
        turtle.forward(100)
        turtle.left(90)

    turtle.end_fill()
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()

turtle.exitonclick()
