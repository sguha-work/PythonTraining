print('==============================================================')
print('Enter an integer number to calculate factorial:')
userGivenNumber = int(input())
result = 1
for index in range(1, userGivenNumber+1):
    result *= index
print(f'The calculated factorial of {userGivenNumber} is {result}')
print('==============================================================')