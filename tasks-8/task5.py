# Python program to count Even and Odd numbers in a List

lst=[1,2,3,4,5,6,7,8,9]

even=0
odd=0

for i in lst:
    if(i%2==0):
      even += 1
    else:
       odd += 1

print("even number:",even)
print("odd number:",odd)
      
      

