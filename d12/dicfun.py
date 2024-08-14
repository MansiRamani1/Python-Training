
d={
    'sub':'python',
    'duration':'3 month',
    'age':'20'
  }

#get():- return the key to value
c=d.get("sub")
c1=d["sub"]
print(c,c1)#both same value return
print()

#keys():return the all keys in dictionary
for a in d.keys():
    print(a) 
print()

#values():
for a in d.values():
    print(a) 
print()

#items():give all key and value
for a,b in d.items():
    print(a,b)
print()

#del keyword 
# del d['age']
# print(d)
print()

#pop() is return delete value
print(d.pop("age"))
print(d)
print()

#dict() is use create dictionary
d=dict(name="mansi",duration="3month")
print(d)
print()

