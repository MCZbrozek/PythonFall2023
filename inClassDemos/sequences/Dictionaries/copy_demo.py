x = {'userName': 'admin', 'machines':['foo', 'bar', 'baz']}
y = x.copy()
print(f'x: {x}')
print(f'y: {y}')

y['userName'] = 'mlh'
print(f'x: {x}')
print(f'y: {y}')
y['machines'].remove('bar')
print(f'x: {x}')
print(f'y: {y}')