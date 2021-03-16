import random

color = random.choice(["red", "green", "blue", "yellow", "orange"])
userColor = input("Enter a color: ")
userColor = userColor.lower()

while color != userColor:
    if color == "red":
        print("I bet you're RED with anger now")
        userColor = input("Enter a color: ")
        userColor = userColor.lower()
    elif color == "green":
        print("I bet you're GREEN with envy")
        userColor = input("Enter a color: ")
        userColor = userColor.lower()
    elif color == "blue":
        print("You're probably feeling BLUE right now")
        userColor = input("Enter a color: ")
        userColor = userColor.lower()
    elif color == "yellow":
        print("I hope you don't have any YELLOW furniture")
        userColor = input("Enter a color: ")
        userColor = userColor.lower()
    elif color == "orange":
        print("I hope you like to eat ORANGES")
        userColor = input("Enter a color: ")
        userColor = userColor.lower()
