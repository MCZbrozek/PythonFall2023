word = input("Please enter a word: ")
if word.endswith('ly'):
    # Only executes if endswith('ly') == True
    print('The word ends in ly')
else: 
    # Only executes if endswith('ly') == False
    print(f'The word \'{word}\' doesn\'t have an \'ly\' at the end, are you not aware of the magic of adverbs? ')
print(word.endswith('ly'))
print("Thank you so very much for using this program, have a nice day!") # <-- Always executes