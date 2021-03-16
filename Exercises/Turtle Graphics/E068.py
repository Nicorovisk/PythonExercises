import turtle
import random

lines = random.randint(5, 20)

for i in range(0, lines):
    length = random.randint(25, 100)
    rotate = random.randint(1, 365)
    turtle.forward(length)
    turtle.left(rotate)

turtle.exitonclick()
