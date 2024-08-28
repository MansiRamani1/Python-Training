class Vehicle():
    
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car is starting with a key."

class Bike(Vehicle):
    def start(self):
        return "Bike is starting with a kick."

car = Car()
print(car.start())  
bike = Bike()
print(bike.start())  