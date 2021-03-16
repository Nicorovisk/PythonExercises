running = True

while running:
    number = int(input("Enter a number between 10 and 20: "))

    if number < 10:
        print("Too low")
        print("Try Again")

    elif number > 20:
        print("Too high")
        print("Try again")

    else:
        print("Thank you")
        running = False
