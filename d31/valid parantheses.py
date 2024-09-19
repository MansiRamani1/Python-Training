# Example 2:
# Input: s = "()[]{}"
# Output: true

s="(][]{}"

count=0

for i in s:
    if i=="(": 
        count+=1
    elif i==")":
        count-=1
    elif i=="[":
        count+=1
    elif i=="]":
        count-=1
    elif i=="{":
        count+=1
    elif i=="}":
        count-=1
    
else:
  if count==0:
    print("true")
  else:
    print("false")