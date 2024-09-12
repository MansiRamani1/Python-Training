# a = "man"
# b = "boy"

# ans = "mbbaoonyy"


a="man"
b="boy"

result=''
for i in range(len(a)):
    result+=a[i]
    result+=b[i]*2
print(result)