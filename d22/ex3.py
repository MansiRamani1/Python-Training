# Remove Duplicates: Write a program that removes duplicates from a list while preserving the original order of elements.

# Input:
# [1, 2, 3, 2, 4, 5, 1]
# Output:
# [1, 2, 3, 4, 5]


l= [1, 2, 3, 2, 4, 5, 1]

u_num=[]

for number in l:
    if number not in u_num:
        u_num.append(number)

print("list:",u_num)

