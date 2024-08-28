class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyatoCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  
        self.name = name

car1 = ToyatoCar("fortuner", "electric")  
print(car1.type)
