# Find Common Elements: Write a program to find common elements between two lists.

# Input:
# [1, 2, 3, 4, 5]
# [4, 5, 6, 7, 8]
# Output:
# [4, 5]
l1=[1, 2, 3, 4, 5]
l2=[4, 5, 6, 7, 8]

common=[]

for i in l1:
    for j in l2:
        if i==j:
          common.append(j)
print(common)