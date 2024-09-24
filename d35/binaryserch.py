a=[4,5,6,8,9,15]

f_num=9   #target number
i=0
j=len(a)-1
s=0  #found

while i<=j and s==0:
    mid=(i+j)//2  #(0+5)//2=2 , mid number is 6
    if a[mid]==f_num:#if 6==9 no
        s=1
    elif a[mid]<f_num: #6<9
        i=mid+1        #3
    else:
        j=mid-1
if s==1:
    print("number found",mid)
else:
    print("number not found")





