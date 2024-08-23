class A:
    def displayA(self):
        print("printA")

class B:
    def displayB(self):
       print("printB")

class C(B,A):
    def displayC(self):
        print("printC")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()