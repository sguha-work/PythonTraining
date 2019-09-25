# basic class
print('==============================================================')
class MyClass:
    name = 'Angshu'

    def returnValue(self, userGivenName=''):
        if userGivenName == '':
            userGivenName = self.name
        print(userGivenName)


objectOfMyClass = MyClass()
objectOfMyClass.returnValue() # 'Angshu'
objectOfMyClass.returnValue('piklu') # 'piklu'
print('==============================================================')