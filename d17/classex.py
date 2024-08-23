class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("My name is " + self.name)

person = Person("abc")# creating an instance of the Person class
person.print_name()# calling the method to print the name