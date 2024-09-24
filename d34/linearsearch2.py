# Recursive Approach

arr=[10, 20, 30, 40, 50]
target=30

def l_s_recursive(arr,target,index=0):
    if arr[index]==target:
        return index 

    if index==len(arr):
        return -1  
    
    return l_s_recursive(arr,target,index+1)

print(l_s_recursive(arr,target))