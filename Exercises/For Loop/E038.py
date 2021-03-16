name = input("Enter your name: ")
times = int(input("Enter a number: "))

for i in range(0, times):
    for j in range(0, len(name)):
        print(name[j])
