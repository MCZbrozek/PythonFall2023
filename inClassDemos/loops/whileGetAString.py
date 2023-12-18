name = ''
# while name == '': <-- One way to do this
while not name: #<-- while name is empty (false), but true when it has a value, stop loop.
    name = input('Please enter name: ')
print(f"Hello, {name}!")