import random

print("Welcome to the math quiz")
points = 0

for i in range(0, 5):
    num1 = random.random()
    num1 = round(num1*100, 0)
    num2 = random.random()
    num2 = round(num2*100, 0)

    print("How much is", num1, "+", num2, "?")
    answer = int(input("= "))

    if answer == num1+num2:
        points += 1

print("You got", points, "points")
