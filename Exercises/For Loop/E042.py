total = 0

for i in range(0, 5):

    number = int(input("Enter a number: "))
    add = input("Do you want to add this number?(y ,n) ")

    if add == "y":
        total += number
        print("Added!")

    else:
        print("Passed")
        pass

print("The total is", total)
