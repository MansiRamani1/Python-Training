# f=open("hello.txt","w")

# f.write("hello,i am herry.")#overwrites the file data

# f.close()

f=open("hello.txt","a")
f.write("\nhello,i am herry.")#add the data in this file
f.close()

f=open("sample.txt","w")#here sample.txt file not in dictionory but create file
f.write("hwllo")
f.close()












