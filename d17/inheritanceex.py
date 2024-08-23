class A:
    def displayA(self):
        print("printA")

class B(A):
    def displayB(self):
       print("printB")

obj=B()
obj.displayA()
obj.displayB()