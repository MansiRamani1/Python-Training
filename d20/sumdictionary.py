# Sum of All Values:
# Find the sum of all the values in a dictionary.
# Example: Input: {"x": 10, "y": 20, "z": 5}

dic={"x": 10, "y": 20, "z": 5}

s=0

for i in dic.values():
    s+=i
print(s)