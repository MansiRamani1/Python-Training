#it's work at class level.
class Student:

    @staticmethod
    def car():#static method not use self parameter
     print("Rolls-Royce")

obj=Student()
obj.car()
