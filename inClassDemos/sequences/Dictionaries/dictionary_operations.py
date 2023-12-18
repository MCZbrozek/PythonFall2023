phone_book = {'Alice': '2341', 'Beth': '4567', 'Lordis': {'phone': "303-895-7523", 'hat-size': 'big'}, 'Kane': '0123', 'Volar': '87893'}

print(', '.join(phone_book))
print(len(phone_book))
print(phone_book['Lordis'])

del phone_book['Volar']
print(phone_book)

print('Beth' in phone_book)
phone_book['Earl'] = '1234'
print(phone_book)