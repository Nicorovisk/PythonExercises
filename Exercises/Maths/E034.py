print("1) Square\n2) Triangle")

number = int(input("Enter a number: "))

if number == 1:
    length = int(input("Enter the length of one side of the square: "))
    area = length**2
    print("Area =", area)

elif number == 2:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base*height)/2
    print("Area =", area)

else:
    print("Invalid number")