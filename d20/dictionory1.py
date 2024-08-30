# Create a Count Dictionary:
# Given a list of numbers, create a dictionary where each number is a key, and the value is 
# the count of how many times that number appears in the list.
# Example: Input: [5,3,6,1,6,9,4,5]

lst=[5,3,6,1,6,9,1,5]

dic={}

for i in  lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)