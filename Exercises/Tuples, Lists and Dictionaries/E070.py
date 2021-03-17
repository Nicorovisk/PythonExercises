countryTuple = ("Brazil", "Mexico", "China", "Canada", "Sealand")
print(countryTuple)

userChoice = input("Enter one of the five countries: ")
print("The index of this country is:", countryTuple.index(userChoice))

userNumber = int(input("Enter a number: "))
print("The country in that index is:", countryTuple[userNumber])
