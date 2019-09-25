# inheritence
print('==============================================================')
class Vehicle:
    hasWheels = None
    def __init__(self):
        print('I\'m a vehicle')
        self.hasWheels = True
    def generalUsage(self):
        print('General use: transportation')

class Car(Vehicle):
    wheels: None
    hasRoof: None
    def __init__(self):
        print('I\'m car')
        self.wheels = 4
        self.hasRoof = True
        # self.hasWheels = True
    def specificUsage(self):
        self.generalUsage()
        print('Specific usage: Vacation with family')
    def details(self):
        print(f"""
            Has wheels {self.hasWheels}
            Number of wheels {self.wheels}
            Has roof {self.hasRoof}
        """ )

objectOfCar = Car()
objectOfCar.specificUsage()
objectOfCar.details()
print('==============================================================')