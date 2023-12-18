from copy import deepcopy

x = {'userName': 'admin', 'machines':['foo', 'bar', 'baz']}
c = x.copy()
dc = deepcopy(x)

x['machines'].remove('baz')

print(f'x: {x}')
print(f'c: {c}')
print(f'dc: {dc}')
