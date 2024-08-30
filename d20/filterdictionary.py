# Filter Keys by Value Condition:
# From a given dictionary, print all keys where values are divisible by 2.
# Example: Input: {"a": 3, "b": 4, "c": 6}

dic={"a": 3, "b": 4, "c": 6}

mul_value=0

for key,value in dic.items():
    if value%2==0:
     print(value)
    
       