add = "y"
inviteCount = 0

while add == "y":
    name = input("Enter the name of the invited: ")
    print(name, "has now been invited")
    inviteCount += 1
    add = input("Do you want to invite someone else? (y/n) ")
    add = add.lower()

print("You have", inviteCount, "people coming to your party")
