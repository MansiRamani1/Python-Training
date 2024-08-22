a=int(input("enter first no:"))
b=int(input("enter first no:"))
try:
  divi=a/b
  print("division:",divi)
except(ZeroDivisionError , NameError)as obj:
  print(obj)
print("code")