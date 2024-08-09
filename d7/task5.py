

# f1 = "abcdefgh"

# index_c = f1.find("c")
# index_d = f1.find("d")
# ex_string = f1[index_c:index_d+1]
# string1 = f1[0:-6]
# string2 = f1[4:8]

# print("".join([ex_string,string1,string2]))

f1 = "acbcdefgcch"

new_str = ""
cd = ""

for i in f1:
    if i == "c" or i == "d":
        cd += i
    else:
        new_str += i

print(cd)
print(new_str)

print(cd+new_str)