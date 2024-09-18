# input: arr[]=[2,13]
# output:-1
# expl:since,no element is present more than n/2 times,so there is no majority element

# input: arr[]=[7]
# output:7
# expl:since,7 is single element and more than n/2 times,so it is the majority element

arr=[2,13]

count_dict={}
n = len(arr)
count=0
result=False

for i in arr:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1

for key,value in count_dict.items():
    if value>n//2:
        count+=1
        result=True
        print(key)
        break
if result!=True:
      print(-1)



