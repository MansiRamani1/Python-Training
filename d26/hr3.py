# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 13

lena=int(input())

a=set([int(x) for x in input().split()])
lenb=input()
b = set([int(x) for x in input().split()])

count_l=len(a.union(b))
print(count_l)



       