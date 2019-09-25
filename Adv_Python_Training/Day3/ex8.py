print('==============================================================')


class MyClass:


    memberVariable1 = None

    def __init__(self):
        self.memberVariable1 = 'basic value'

    def display(self, userGivenValue=None):
        if userGivenValue != None:
            self.memberVariable1 = userGivenValue
        print(self.memberVariable1)


objectOfMyClass = MyClass()
objectOfMyClass.display() # 'basic value'

objectOfMyClass.display('HiHello') # 'HiHello'

print('==============================================================')
