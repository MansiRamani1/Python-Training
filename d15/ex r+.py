f=open("demo.txt","r+")
f.write("abc")#this is example overwrite abcs is example
print(f.read())
f.close()





#r+ : no truncate(data not delete),courser point start
#w+ :  truncate(datadelete),store new data
#a+ : no truncate(data not delete),courser point end