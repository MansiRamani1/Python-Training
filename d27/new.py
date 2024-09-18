# input: arr[]=[3,1,3,3,2]
# output:3
# expl:since,3 is present more than n/2 times,so it is the majority element

# arr=[3,1,3,3,2]

# n=len(arr)
# count=0

# for i in arr:
#     if(i==3):
#      count+=1
#     if count>n//2: # 3>5//2 =3>2 ,true than print i
#         print(i) 
#         break

arr=[3,1,3,3,2]

count_dict={}
n = len(arr)
count=0

for i in arr:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1

for key, value in count_dict.items():
    if value>n//2:
        count+=1
        print(key)
        break




