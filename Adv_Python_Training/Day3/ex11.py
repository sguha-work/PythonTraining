print('==============================================================')
class Father():
    def gardenning(self):
        print ('I enjoy gardenning')

class Mother():
    def cooking(self):
        print ('I love cooking')

class Child(Father, Mother):
    def skills(self):
        print ('I enjoy gamming')

c = Child()
c.gardenning()
c.cooking()
c.skills()
print('==============================================================')