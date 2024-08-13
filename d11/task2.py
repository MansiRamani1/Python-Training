# Count the Number of matching characters in a pair of string
# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb2211@55k'
# Output : 5 
# (i.e. matching characters :- b, 1, 2, @, k)
str1="aabcddekll12@"
str2="bb2211@55k"


set1=set(str1)
set2=set(str2)

common_element=set1.intersection(set2)
total_element=len(common_element)

print(total_element)