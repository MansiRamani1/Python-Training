# Example 3:
# Input: s = "(]"
# Output: false

s="(]"
stack=[]

def check(s,stack):

 for i in s:
    if i=="(": 
        stack.append(i)
    elif i==")":
        if len(stack)==0:
           return False
        if stack[-1]!="(":
           return False
        stack.pop()
        if len(stack)==0:
           return True
    if i=="[": 
        stack.append(i)
    elif i=="]":
        if len(stack)==0:
           return False
        if stack[-1]!="[":
           return False
        stack.pop()
        if len(stack)==0:
           return True
#  for i in s:
#     if i=="{": 
#         stack.append(i)
#     elif i=="}":
#         if len(stack)==0:
#            return False
#         if stack[-1]!="{":
#            return False
#         stack.pop()
#         if len(stack)==0:
#            return True
           
print(check(s,stack))