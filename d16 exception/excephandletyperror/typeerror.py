a="abc"
b=123
try:
    result = a + b
except TypeError as e:
    print("can't sum")
    print(e.__class__)