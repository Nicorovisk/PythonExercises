number = int(input("Enter a integer number between 1 and 12: "))

if number >= 1 and number <= 12:

    for i in range(1, 11):
        print(number, "X", i, "=", number*i)

else:
    print("Error")
