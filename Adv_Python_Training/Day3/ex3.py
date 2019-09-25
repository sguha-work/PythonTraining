# function returning multiple value
print('==============================================================')


def getSignature(name='', surname=''):
    signature1 = name.upper()[0]+surname.capitalize()
    signature2 = name.capitalize()+surname.upper()[0]
    return signature1, signature2


output = getSignature('Angshu', 'Guha')
print(output)  # return a touple ('AGuha', 'AngshuG')

output = getSignature('angshu', 'guha')
print(output)  # return a touple ('AGuha', 'AngshuG')


print('==============================================================')
