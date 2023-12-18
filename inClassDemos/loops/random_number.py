import random
names = ['Maylou', 'Betty', 'Sean', 'Doug']
doAnother = 'y'
while doAnother == 'y':
    index = random.randint(0,4)
    name = names[index]
    print(name)
    doAnother = input('print again? (y/n)')
print('Fine! Go ahead. Leave. See if I care! ')