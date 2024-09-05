# Find the Maximum Number: Write a program to find the maximum number in a list using a for loop.

l=[5,78,34,25,67,98,2,6,8]

max_num=l[0]

for number in l:
    if number > max_num:
        max_num=number

print("The maximum numb:", max_num)
