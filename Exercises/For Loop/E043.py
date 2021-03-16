direction = input("Which direction you want to count?(up or down)")
direction = direction.lower()

if direction == "up":
    topNumber = int(input("Enter the top number: "))

    for i in range(1, topNumber+1):
        print(i)

elif direction == "down":
    number = int(input("Enter a number below 20: "))
    for i in range(20, number-1, -1):
        print(i)

else:
    print("I don't understand")
