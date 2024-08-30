# Convert Two Lists into a Dictionary:
# Given two lists, one of keys and the other of values, create a dictionary by pairing them.
# Example: Input: keys = ["a", "b"], values = [1, 2]
a=["a", "b"]
b=[1, 2]

combine=dict(zip(a,b))
print(combine)