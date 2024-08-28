class Car:

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyatoCar(Car):  
    def __init__(self, name):
        self.name = name

car1 = ToyatoCar("fortuner")  
car2 = ToyatoCar("prius")     

print(car1.start())
print(car2.stop())