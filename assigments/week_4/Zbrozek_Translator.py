# Program: Zbrozek_Translator.py
# Programmer: Mike Zbrozek 
# MZbrozek1@cnm.edu
# Date: 03 Oct 2023
# Purpose: Program provides translated values for user input. 
# Ex. [si, wi, yes]
# EX. Type a sentence to translate - "Wi, wi"
# EX. Output - Your sentence translated to english is - "yes, yes"

import random
# Creates a dictionary with common phrases in language a as the key and the translation in another language 2 as the values. From ChatGPT - 
# Prompt: Python dictionary containing 100 common Spanish words along with their English translations w/out accents:
# --- Dictionary ---
spanish_to_english = {
    "agua": "water",
    "amigo": "friend",
    "animal": "animal",
    "ano": "year",
    "boca": "mouth",
    "casa": "house",
    "cielo": "sky",
    "coche": "car",
    "color": "color",
    "corazon": "heart",
    "dia": "day",
    "dinero": "money",
    "familia": "family",
    "flor": "flower",
    "fuego": "fire",
    "gato": "cat",
    "gente": "people",
    "hombre": "man",
    "hoja": "leaf",
    "hora": "hour",
    "joven": "young",
    "luz": "light",
    "madera": "wood",
    "mano": "hand",
    "mesa": "table",
    "mujer": "woman",
    "nino": "child",
    "nombre": "name",
    "ojo": "eye",
    "pan": "bread",
    "paso": "step",
    "perro": "dog",
    "piedra": "stone",
    "pueblo": "village",
    "puerta": "door",
    "sol": "sun",
    "tiempo": "weather",
    "tierra": "earth",
    "trabajo": "work",
    "viento": "wind",
    "agua": "water",
    "amigo": "friend",
    "animal": "animal",
    "ano": "year",
    "boca": "mouth",
    "casa": "house",
    "cielo": "sky",
    "coche": "car",
    "color": "color",
    "corazon": "heart",
    "dia": "day",
    "dinero": "money",
    "familia": "family",
    "flor": "flower",
    "fuego": "fire",
    "gato": "cat",
    "gente": "people",
    "hombre": "man",
    "hoja": "leaf",
    "hora": "hour",
    "joven": "young",
    "luz": "light",
    "madera": "wood",
    "mano": "hand",
    "mesa": "table",
    "mujer": "woman",
    "nino": "child",
    "nombre": "name",
    "ojo": "eye",
    "pan": "bread",
    "paso": "step",
    "perro": "dog",
    "piedra": "stone",
    "pueblo": "village",
    "puerta": "door",
    "sol": "sun",
    "tiempo": "weather",
    "tierra": "earth",
    "trabajo": "work",
    "viento": "wind",
}

# --- Function definitions ---
def generate_display_dictionary():
    display_dictionary = []
    print("Here are 20 random words you can learn the meaning of - ")
    for words in range(0,20):
        display_dictionary.append(random.choice(list(spanish_to_english.keys())))
    return display_dictionary

def enter_a_phrase():
    user_phrase = input("\nEnter any of THE WORDS ABOVE to learn their meaning in English: ")
    return user_phrase.lower()

def translate(phrase, spanish_to_english, display_dictionary):
    translated_phrase = []
    for i in phrase:
        translated_phrase.append(spanish_to_english[i])
    return translated_phrase

def display_translation(phrase, translated_phrase):
    sep = " "
    print(f"\nI found a match for {len(translated_phrase)} words in that sentence. Their translation in english is -\n{(sep.join(translated_phrase))}")


def translator_app():
    doAnother = "y"
    while doAnother == "y":
        #do something for user (run your program)
        # Display a list of the phrases of language 1 to the user. Hint: use the .keys() method of the dictionary class.
        display_dictionary = generate_display_dictionary()
        print(display_dictionary)

    # Ask the user to type in a phrase to translate.
        phrase = enter_a_phrase().split()
        print(phrase)

    # Translate the phrase & store in list
        # translate(phrase, spanish_to_english, display_dictionary)
        translated_phrase = translate(phrase, spanish_to_english, display_dictionary)
        

    # Display the translation of that phrase to the user.
        display_translation(phrase, translated_phrase)
            # ask the user if they want to run it again? 
        doAnother = input('Do another (y/n)?')
    print('Thank you for using this great program! ')


# Welcome User
print("Welcome to 'Como Se Dice?' - 'How do you say?'\nFollow the prompts below to see english translations of more than 100 common Spanish words \n")

# Run Tranlation app - 
translator_app()

