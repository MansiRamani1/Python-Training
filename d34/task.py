# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 
# Explanation:First jump from 1st element to 2nd element with value 3. 
#             From here we jump to 5th element with value 9, and from here we will jump to the last.


# def min_jumps(arr):
#     n = len(arr)

#     if n <= 1:#0 ,-1, -2....<=1
#         return 0

#     if arr[0] == 0:
#         return -1

#     max_reach = arr[0]  
#     steps = arr[0]      
#     jumps = 1          

#     for i in range(1, n):
#         if i == n - 1:#if 1==1
#             return jumps 
#         max_reach = max(max_reach, i + arr[i])#(1)

#         steps -= 1

#         if steps == 0:
#             jumps += 1
#             if i >= max_reach:
#                 return -1
#             steps = max_reach - i

#     return -1  

# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# result = min_jumps(arr)
# print(result)
