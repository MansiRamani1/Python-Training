# find smallest and largest number in list......dont use min & max method!

list=[20,49,77,11,50,34,93,37]

smallval=list[0]
largeval=list[0]

for i in list:
    if i>=largeval:
        largeval=i
    elif i<=smallval:
        smallval=i
        
print("largest number:",largeval)
print("smallest number:",smallval)
   

