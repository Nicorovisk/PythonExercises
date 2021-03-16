firstName = input("Please enter your first name: ")

if len(firstName) < 5:
    surname = input("Please enter your surname: ")
    name = firstName+surname
    name = name.upper()
    print(name)

else:
    print(firstName.lower())
