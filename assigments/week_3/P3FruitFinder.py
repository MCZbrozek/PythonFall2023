# GarnerP3
# Programmer: Rob Garner
# EMail: Rgarner7 @cnm.edu
# Purpose: provides user capability to find fruit in a string

# Creates a sequence that has the names of seven fruits.
fruits = ["apple","lemon","banana","pineaple","orange","papaya","blueberry"]

# Asks the user for a sentence.
sentence = input("Please enter a sentence: ")

# Tells the user how many fruits are in that sentence.
words = sentence.split()
fruitsInSentence = list(set(fruits)&set(words))
print("Number of fruits:",len(fruitsInSentence))

# Displays a list of fruits in the sentence.
print("Fruits in sentence:",fruitsInSentence)

# Finds and replaces one instance of a fruit in the sentence with “Brussel Sprouts”.
sentenceWithBrusselSprouts = sentence.replace(fruitsInSentence[0],"brussel sprouts")

# Displays the new sentence to the user.
print("Your sentence with brussel sprouts:",sentenceWithBrusselSprouts)
