# Linear Search Iterative Approach

a=['hello','hii','hie','hey']

target='hie'

def f_target(a,target):
   
 for i in range(len(a)):
    if a[i]==target:
     return i
 return -1
print(f_target(a,target))
