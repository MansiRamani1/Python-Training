# create student class that takes name and marks of 3 subjects as arguments in constructor.then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):#non-static method
        sum=0
        for val in self.marks:
            sum += val
        print(self.name,'score is',sum/3)

s1=Student("mansi",[85,95,77])
s1.get_avg()
           