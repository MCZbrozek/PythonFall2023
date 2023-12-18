# Program: Zbrozek_StateInfoP3.py
# Programmer: Mike Zbrozek 
# MZbrozek1@cnm.edu
# Date: 26 Sept 2023
# Purpose: Program matches fruits from a user supplied sentence and replaces the fruit with "Brussel Sprouts" 
import webbrowser

# Creates a sequence that has the names of seven fruits.
fruits = ['apple', 'apricot', 'banana', 'canetlope', 'durian', 'fig', 'grape', 'lemon', 'melon', 'orange', 'pear', 'strawberry' ]

#   Program title 
print("Welcome to the big brussel sprout conspiracy, a top secret industry ploy to sell more brussel sprouts.")
# 	Asks the user for a sentence.
userSentence = input("Write a sentence about a common fruit: ").lower()

#   Creates a list from the user sentence, split on blank spaces
userSequence = userSentence.split()

#   Remove plural from words 
userSequencePluralsRemoved = []
for i in userSequence:
    if i.endswith('s'):
        formattedWord = i.replace('s','')
    else:
        formattedWord = i
    userSequencePluralsRemoved.append(formattedWord) 

#   List of fruit and list of words intersection 
set1 = set(fruits)
set2 = set(userSequencePluralsRemoved)
fruitsInSentence = list(set1&set2)

#   Tells the user how many fruits are in that sentence & displays a list of fruits in the sentence.
sep = ", "
if len(fruitsInSentence) < 1:
    print(f'\nThere is only one fruit in that sentence -', sep.join(fruitsInSentence))
else:
    print(f'\nThere are {len(fruitsInSentence)} fruits in that sentence -', (sep.join(fruitsInSentence)))

#   Finds and replaces one instance of a fruit in the sentence with “Brussel Sprouts”.
addBrusselSprouts = userSentence.replace(fruitsInSentence[0], 'Brussel Sprouts').title()

#   Displays the new sentence to the user.
print("\nNow with Brussel Sprouts-\n",addBrusselSprouts)
print('\nSee how much better life is when you add Brussel Sprouts??')

# Take people to a webpage about brussel sprouts
learnMore = input('\nType "y" to learn more about brussel sprouts: ').lower()
if learnMore == "y":
    webbrowser.open("https://en.wikipedia.org/wiki/Brussels_sprout", new = 0, autoraise = True)
else:
    print("I'm here, if you ever want to learn more")