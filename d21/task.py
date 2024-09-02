# You are given a two lists  A and B. Your task  to compute their cartesian product A X B.



# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

a=[1, 2]
b=[3, 4]

product=[]

for i in a:
    for h in b:
        product.append((i,h))
print(product)