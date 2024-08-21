# f=open("demo.txt","w+")
# f.write("abc")#this is example overwrite abcs is example
# print(f.read())
# f.close()

f=open("demo.txt","a+")
f.write("\nabc")#this is example overwrite abcs is example
print(f.read())
f.close()