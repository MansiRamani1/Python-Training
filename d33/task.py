#pg.8

n=int(input("enter integer number:"))

r_dic={1000:'M',  500:'D',  400:'CD', 100:'C',  50:'L',  40:'XL',  10:'X',  5:'V', 4:'IV', 1:'I'}

result=''

for key,value in r_dic.items():
    while n>=key:#450>=400  cd
        n-=key #450-400-50=0
        result+=value#cdl
        
print("roman num is:",result)
        