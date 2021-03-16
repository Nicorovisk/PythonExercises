import random

rNumber = random.randint(1, 5)
uNumber = int(input("Choose a number between 1 and 5: "))

if rNumber == uNumber:
    print("Well Done")
else:
    if uNumber > rNumber:
        print("Too High")
    else:
        print("Too Low")

    uNumber = int(input("Pick a second number between 1 and 5: "))

    if rNumber == uNumber:
        print("Correct")

    else:
        print("You lose")
