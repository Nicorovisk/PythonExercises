import turtle
import random

src = turtle.Screen()
src.bgcolor("black")

for i in range(0, 8):
    color = random.choice(["red", "green", "blue", "yellow", "purple", "pink"])
    turtle.color(color)
    turtle.forward(100)
    turtle.left(45)

turtle.exitonclick()
