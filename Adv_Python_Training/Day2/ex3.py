## different ways of printing
print('==============================================================')
name = 'angshu'
age = 30
print('Hi, my name is '+name+' and I\'m '+str(age)+' years old' )
# comma separation will add one extra space autometically
# please note, for comma we don't need the typecasting using str()
print('Hi, my name is ',name,' and I\'m ',age,' years old' )

# below examples are of formatted string
print('Hi, my name is {} and I\'m {} years old'.format(name, age))
# the follwoing line name and age value will be swapped when displayed
# as the arguments are manually swapped
print('Hi, my name is {1} and I\'m {0} years old'.format(name, age))
print(f'Hi, my name is {name} and I\'m {age} years old')
print('==============================================================')