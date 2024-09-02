# Filter Even Numbers
# Given a list numbers = [1, 2, 3, 4, 5, 6], create a new list containing only even numbers using a for loop.

numbers=[1, 2, 3, 4, 5, 6]
even_num=[]

for num in numbers:
    if num % 2==0:
        even_num.append(num)

print(even_num)