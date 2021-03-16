word = input("Enter a word: ")
word = word.lower()
fLetter = word[0]
rest = word[1:len(word)]

if fLetter == "a" or fLetter == "e" or fLetter == "i" or fLetter == "o" or fLetter == "u":
    word = word+"way"
    print("This word in Pig Latin is", word)

else:
    word = rest+fLetter+"ay"
    print("This word in Pig Latin is", word)
