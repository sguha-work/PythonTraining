print('==============================================================')
import random as rand
lowerLimit = int(input('Enter the lower limit of random number:'))
upperLimit = int(input('Enter the upper limit of random number:'))
randomNumberWithinRange = rand.randint(lowerLimit, upperLimit)
print(f""" 
User selected lower limit {lowerLimit}
User selected upper limit {upperLimit}
Machine seleted random number between {lowerLimit} and {upperLimit} is {randomNumberWithinRange}
""")

if randomNumberWithinRange > 50:
    print(f'The machine selected value {randomNumberWithinRange} is greater than 50')
    if randomNumberWithinRange>90 and randomNumberWithinRange < 100:
        print('Its a very good number I have to say')
    else:
        print('Not so special number though')
else:
    print(f'The machine selected value {randomNumberWithinRange} is less than 50')