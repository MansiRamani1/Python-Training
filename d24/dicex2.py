# Uppercase Check

# Task: Print all the keys where the string value contains any uppercase letters

d={
    1:"HELLO",2:"wlc",3:"Hru"
}

upperstring=[]

for value in d.values():
    upperstring.append(value.upper)

print(upperstring)
