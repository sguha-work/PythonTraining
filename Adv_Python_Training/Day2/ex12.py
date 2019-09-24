print('==============================================================')
name = 'Angshu'
guess = input('So I\'m thinking of a person\'s name can u guess it?')
pos = 0
while(guess != name and pos<len(name)):
    print(f'Nope, that\'s not right answer! Hint letter: {name[pos]}')
    index = 0
    while guess[index] == name[index]:
        index += 1
    if index > 0:
        print(f'Though wrong but your answer \'{guess}\' was correct upto {index} charecters ie.({guess[0:index:1]})')
    guess = input('Try again: ')
    pos += 1
if pos==len(name) and name != guess:
    print(f'Alas u can\'t guess the actual name I was thinking is {name}')
else:
    print(f'Great! You got it in {pos+1} guesses')
print('==============================================================')