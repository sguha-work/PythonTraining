## Dictionary
print('==============================================================')
name = 'Angshu'
a = {
    'name': name,
    'age': 30,
    'address': 'sodepur',
    123: 'ABCD'
}
print(a)
print(type(a))
print(a['name'])
print(a[123])
#print(a.name) # this will cause error

print('Printing all the keys')
for key in a.keys():
    print(f'{key}, ',end='')
print('')

print('Printing all the values')
for value in a.values():
    print(f'{value}, ',end='')
print('')

print('Printing key value as pair')
print(' {')
for key,value in a.items():
    print(f'    "{key}": "{value}"')
print(' }')

a = {
    'one': 1,
    'two': 2,
    'three': 3
}
b = {
    'four': 4,
    'five': 5
}
print('Before update')
print(a)
print(b)
a.update(b)
print('After update')
print(a)
print(b)

# preparing a third list from output, keeping a,b untouched
c=dict(a)
c.update(b)
print(c)
print(id(a),id(b),id(c))
d={**a, **b}
print(d)
print('==============================================================')