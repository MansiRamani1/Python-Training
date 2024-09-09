# String Contains 'l'
# Task: Print all the keys where the string value contains the letter 'l'.


d={1: "hello", 2: "wlc", 3: "hru"}

for key, value in d.items():

    if 'l' in value:
        print(key)