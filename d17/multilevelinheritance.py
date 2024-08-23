class A:
    def displayA(self):
        print("printA")

class B(A):
    def displayB(self):
       print("printB")

class C(B):
    def displayC(self):
        print("printC")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()