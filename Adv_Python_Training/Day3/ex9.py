class Car:
    def __init__(self, carName,carType, carPrice):
        print(f'{carName} is a {carType} worth {float(carPrice)}')
car1 = Car('Ford', 'Red convertible', 6000)
car2 = Car('Jump', 'Blue Van', 2000)