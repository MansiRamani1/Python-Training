# which Exception is first occur and which first handle

# num1=int(input("enter first no:"))
# num2=int(input("enter first no:"))

# try:
#     div=num1/num
#     print("division",div)
# except Exception as var:
#     print(var)             #give error info
#     print(var.__class__)   #give error class

# print("in code")


import sys

num1=int(input("enter first no:"))
num2=int(input("enter first no:"))

try:
    div=num1/num1
    print("division",div)
except:
    print(sys.exc_info()[0])#give class error means exception name
    print(sys.exc_info()[1])#exception detail 

print("in code")