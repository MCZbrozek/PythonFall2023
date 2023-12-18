names=['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
numbers=['2341', '9102', '3158', '0142', '0551']
print(names)
name=input('Please enter a name to look up: ')
#Find where the name is in names
name_index = names.index(name)
#find the number that corresponds to that position
number = numbers[name_index]
#Out put the number and the name 
print("The index of", name, "is", number)