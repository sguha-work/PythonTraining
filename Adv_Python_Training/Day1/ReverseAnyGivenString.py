print("""=========================================================""")
print("""Provide a string to see how it reversed""")
userGivenString = input()
userGivenStringLength = len(userGivenString)
a=-1
b=-(userGivenStringLength+1)
c=-1
print("""The length of the string is """,len(userGivenString))
print(f'The a:b:c values are like this {a}:{b}:{c}')
print("""Finally the reversed string is""")
reversedString = userGivenString[a:b:c]
print(reversedString)
print("""=========================================================""")