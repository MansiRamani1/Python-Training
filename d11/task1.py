# Count the Number of matching characters in a pair of string

# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4 
# (i.e. matching characters :- a, d, e, f)


# str1="abcdef"
# str2="defghia"


# set1=set(str1)
# set2=set(str2)

# common_element=set1.intersection(set2)
# total_element=len(common_element)

def count_common_element(str1, str2):
    count = 0


    for char in str1:
        if char in str2:
            count += 1
            str2 = str2.replace(char, '', 1)
    return count


str1 = 'abcdef'
str2 = 'defghia'
print(count_common_element(str1, str2))