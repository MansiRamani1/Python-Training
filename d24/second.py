# Python program to generate the prime numbers from 1 to N

n=int(input("Enter num:"))

for i in range(2,n):
    if n % i==0:
       print("not prime")
       break
else:
    print("prime")
       