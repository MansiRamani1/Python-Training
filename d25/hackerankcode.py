# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]


A=[1,2]
B=[3,4]

new=[]

for i in A:
   for j in B:
           new.append((i, j))

print(new)

