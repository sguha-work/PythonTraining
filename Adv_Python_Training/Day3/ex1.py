# string handelling with inbuilt methods
a = 'aNGSHU'
b = a.capitalize()
print(b)  # 'Angshu' please not if first letter is space then 'a' will remain 'a'
a = ' aNGSHU '
b = a.capitalize()  # ' angshu '
print(b)
b = a.lstrip()
print(b)  # 'aNGSHU'
print(len(a), ' ', len(b))

b=a.swapcase()
print(b) # ' Angshu ' swap the charecter's case
