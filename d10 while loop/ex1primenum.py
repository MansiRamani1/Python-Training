#find prime number


n=int(input())
i=2

while(i<=n):
     flag=0
     for var in range(2,i):
          if(i%var==0):
               flag=1
               break
     if(flag==0):
           print(i,end=' ')

     i=i+1
