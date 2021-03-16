invites = int(input("How many people do you want to invite to the party: "))

if invites >= 10:
    print("Too many people")

else:
    for i in range(0, invites):
        name = input("Enter the name of the invited: ")
        print(name, "has been invited")
