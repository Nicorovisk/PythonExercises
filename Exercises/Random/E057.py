import random

rNumber = random.randint(1, 10)
uNumber = int(input("Enter a number between 1 and 10: "))

while uNumber != rNumber:

    if uNumber > rNumber:
        print("Too high")
    elif uNumber < rNumber:
        print("Too low")

    uNumber = int(input("Enter another number: "))

print("Correct")