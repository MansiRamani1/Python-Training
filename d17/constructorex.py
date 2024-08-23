class Demo:

    a=5
    def __init__(self):
        print("welcome")

    def showvalue(self):
        self.a=self.a*self.a
        print(self.a)

    def showvalue1(self,a,b):
        print(a+b)
        
   
obj=Demo()
obj.showvalue()
obj.showvalue1(10,30)