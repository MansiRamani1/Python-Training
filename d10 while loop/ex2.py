#given integer number l,r and k.find how many numbers between l and r(both inclusive) are divisible by k,you do not need to print these numbers,just find their count.

l,r,k=input().split()        #one line in take multiple input

l=int(l)
r=int(r)
k=int(k)

count=0
for i in range(l,r+1):
    if(i%k==0):
        count=count+1
else:
    print(count)