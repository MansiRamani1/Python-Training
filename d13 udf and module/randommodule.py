#random is a module


import random

print(random.randint(2,8))#give between 2 and 8 random number involve with 2 and 8
print()
print(random.randrange(2,4))#not involve 4
print(random.randrange(2,9))
print()

l=[3,10,45,70]
print(random.choice(l))#return random number of list
print()

#random also function
print(random.random())#return float value between 0 and 1 
print()

s=[20,10,35,50]
random.shuffle(s)
print(s)#[20,35,50,10],[10,20,50,35] interchange element of list
print()

u=random.uniform(3,9)#give between 3 and 9 float value  involve with 2 and 8