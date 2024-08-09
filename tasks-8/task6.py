# Python program to count positive and negative numbers in a list

m=[-23,45,7,-91,6,8,12,-57,18]

p_num_count=0
n_num_count=0

for i in m:
    if (i>=0):
        p_num_count += 1
        
    else:
        n_num_count += 1
         
print("positive number:",p_num_count)
print("nagative number:",n_num_count)
