class sl:  #createclass
    a=10

    def sumvalue(self):#method define inside class
        print(20+30)

demoobject1=sl
demoobject=sl()#object create outside the class

print(demoobject.a)
print(demoobject1.a)

demoobject.sumvalue()