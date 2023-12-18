names = ['Alice', 'Beth', 'Lordis', 'Kane', 'Volar']
numbers = ['2341', '4567', '123456', '0123', '87893']

print(', '.join(names))
name = input('Please enter a name: ')
name_index = names.index(name)
print(f'Name is at index: {name_index}')
print(f'{name}\'s phone number is {numbers[name_index]}. ')