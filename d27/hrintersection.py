lena=int(input())

a=set([int(x) for x in input().split()])
lenb=input()
b = set([int(x) for x in input().split()])

#count_l=len(a.intersection(b))
count_l=len(a.union(b))
print(count_l)