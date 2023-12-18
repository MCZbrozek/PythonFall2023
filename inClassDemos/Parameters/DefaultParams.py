def hello3(greeting = 'Hello', name = 'world'):
    print(f'{greeting}, {name}')

hello3()
hello3('Greetings') # <-- We are overwriting the default parameter for greeting
hello3('Greetings', 'Earth') # <-- overwrites both params
hello3(name = 'Gumby') # <-- Overwrites just the name param