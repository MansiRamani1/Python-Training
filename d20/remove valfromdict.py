# Remove Specific Key-Value Pairs:
# Remove key-value pairs from a dictionary where the value is less than a given number.
# Example: Input: {"a": 1, "b": 4, "c": 2}, remove pairs where value < 3.

dic={"a": 1, "b": 4, "c": 2,"d":7}

for key,value in list(dic.items()):
     if value < 3:
      dic.pop(key)
print(dic)
    
