raining = input("It's raining right now? (yes/no)")
raining = str.lower(raining)

if raining == "yes":
    windy = input("It's windy?")
    windy = str.lower(windy)
    if windy == "yes":
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
