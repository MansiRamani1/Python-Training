# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# def i_sum(nums,target):

# number={}

nums=[3,2,4]
target=6

l=len(nums)
for i in range(l):
    for j in range(i+1,l):
        if nums[i]+nums[j]==target:

            print(i,j)
        