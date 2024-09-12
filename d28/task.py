# make a string from this two strings.....with 1 ith letter of a and two times ith letter of b...

# a = "abcd"
# b = "pqrs"

# ans = "appbqqcrrdss"

a="abcd"
b="pqrs"

result=''
for i in range(len(a)):
    result+=a[i]#result in store a+p*2=app return 
    result+=b[i]*2
print(result)
    
























