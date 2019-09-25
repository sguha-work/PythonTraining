# string handelling with inbuilt methods
print('==============================================================')
a = 'aNGSHU'
b = a.capitalize()
print(b)  # 'Angshu' please not if first letter is space then 'a' will remain 'a'
a = ' aNGSHU '
b = a.capitalize()  # ' angshu '
print(b)
b = a.lstrip()
print(b)  # 'aNGSHU'
print(len(a), ' ', len(b))

b = a.swapcase()
print(b)  # ' Angshu ' swap the charecter's case

a = 'myfile.txt'
if a.endswith('pdf'):
    print('File format correct')
else:
    print('File format not supported')

a = '123'
print(a.isdigit())  # True

print(a.isalpha())  # False

a = 'abc123'
print(a.isdigit())  # False
print(a.isalpha())  # False
print(a.isalnum())  # True

# printing words separetly
a = 'My name is sahasrangshu guha'
for word in a.split(' '):
    print(word)

a = 'My name is sahasrangshu guha'
b = a.replace(' ', '-')
print(b)  # My-name-is-sahasrangshu-guha
b = a.replace(' ', '-', 1)
print(b)  # 'My-name is sahasrangshu guha' only the 1st occarence will be replaced
print('==============================================================')
