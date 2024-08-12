# make a list of all the odd numbers in list...

# make a list of all even numbers in the list

lst=[1,2,3,4,5,6,7,8,9]               

even=[]
odd=[]

for i in lst:
    if(i%2==0):
      even.append(i)            
    else:
       odd.append(i)

print("even number:",even)
print("odd number:",odd)


