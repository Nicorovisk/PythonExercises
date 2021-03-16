import random

win = random.choice(["h", "t"])

user = input("Choose heads or tails:(h/t)")
user = user.lower()

if user == win:
    print("You Win")
else:
    print("Bad Luck")

if win == "h":
    print("The computer choose Heads")
else:
    print("The computer choose Tails")
