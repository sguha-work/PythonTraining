# basic function with input arguments and single return
print('==============================================================')
def getWelcomeMessege(name='Anonymus', surname='', age=' '):
    outputString = f"""
        Hi {name} {surname}. You are {age} year old.
    """
    return outputString

output = getWelcomeMessege('Angshu', 'Guha', 30)
print(output) # 'Hi Angshu Guha. You are 30 year old.'

output = getWelcomeMessege('Angshu','', 30)
print(output) # 'Hi Angshu . You are 30 year old.'

output = getWelcomeMessege('Angshu','')
print(output) # 'Hi Angshu . You are   year old.'



print('==============================================================')