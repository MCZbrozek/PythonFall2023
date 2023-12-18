phone_book = {'Alice': '2341', 'Beth': '4567', 'Lordis': '1234569', 'Kane': '0123', 'Volar': '87893'}
name = input('Please enter a name: ').capitalize()
phone_number = phone_book[name]
print(f'{name}\'s phone number is {phone_number}')
