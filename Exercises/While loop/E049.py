compnum = 50
attemptCount = 0
number = 0

while number != compnum:
    number = int(input("Try a number: "))
    if number > compnum:
        print("Too high")
    elif number < compnum:
        print("Too low")
    attemptCount += 1

print("Well Done, you took", attemptCount, "attempts")