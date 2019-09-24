print('==============================================================')
name = 'Angshu'
guess = input('So I\'m thinking of a person\'s name can u guess it?')
pos = 0
while(guess != name and pos<len(name)):
    print(f'Nope, that\'s not right! Hint letter: {name[pos]}')
    guess = input('Try again: ')
    pos += 1
if pos==len(name) and name != guess:
    print(f'Alas u can\'t guess the actual name I was thinking is {name}')
else:
    print(f'Great! You got it in {pos+1} guesses')
print('==============================================================')