line = input("Enter a first line of a nursery rhyme: ")
length = len(line)
print("This line has", length, "length")

start = int(input("Please enter a start number: "))
ending = int(input("Please enter a ending number: "))

print(line[start:ending])
