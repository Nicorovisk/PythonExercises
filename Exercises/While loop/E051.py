for i in range(10, 0, -1):
    print("There are", i, "green bottles  hanging on the wall")
    print(i, "green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    bottles = int(input("How many green bottles will be hanging on the wall?"))

    running = True
    while running:
        if bottles == i - 1:
            print("There will be", i-1, "bottles hanging on the wall")
            running = False
        else:
            print("No, try again")
            bottles = int(input("How many green bottles will be hanging on the wall?"))

print("There are no more green bottles hanging on the wall")
