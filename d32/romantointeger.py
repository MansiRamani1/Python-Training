# I = 1 ,V = 5 ,X = 10 ,L = 50 ,C = 100 ,D = 500 ,M = 1000

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

s=input("Enter roman number: ")

roman={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

result=0

for i in range(len(s)):
  
  if i>0 and roman[s[i]]>roman[s[i - 1]]:# if 1>0 and 5>1
    prev_value=roman[s[i - 1]]#p_v=1
    result+=roman[s[i]]-2*prev_value #1+5-2*1=4

  else:
    result+=roman[s[i]]

print("Integer number:",result)
