number = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

total = number + number2

add = input("Do you want to add another number? (y/n)")
add = add.lower()

while add == "y":
    number = int(input("Enter a number: "))
    total += number
    add = input("Do you want to add another number? (y/n)")

print("The total is", total)
