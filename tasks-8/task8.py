# make a dictionary from array......

# where dictionary contains....value and how many times thay come in array...

# input: [2,1,2,3,2,5]
# output: {1:1, 2:3,3:1,5:1}

make_array=[2,1,2,3,2,5]

dictionary={}

for i in make_array:
        if i in dictionary:
           dictionary[i]+= 1
        else:
           dictionary[i] = 1
print(dictionary)

# l=[2,1,2,3,2,5]
# m=dict.l
# print(l)