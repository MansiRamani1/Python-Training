# make a dictinary from dictionary...but reversed..

# input: {"a":1,"b":2}
# output: {1:"a",2:"b"}
 


dic={"a": 1, "b": 2}
dics={}

for key, val in dic.items():
    dics[val] = key

print(dics)