d={
    'sub':'python',
    'duration':'3 month',
    'age':'20'
  }

n=d['duration']
print(n)#return duration value
print()

for n in d:
    print(n)#give the retun key 
    print()

for n in d:
    print(d[n])#give the return value

print(list(d.values()))
print(list(d.keys()))

for key,value in d.items():
    print(key,value)
