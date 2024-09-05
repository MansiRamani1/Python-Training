# Python program to check whether the given integer is a multiple of both 5 and 7

lst=[35,37,70,56]
# number = int(input("Enter an number: "))

for num in lst:
  if(num%5==0)and(num%7==0):
    print(num, "is a multiple of both")
    print()
  else:
    print(num, "is not a multiple of both")
    print()