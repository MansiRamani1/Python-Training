#Python program to interchange first and last elements in a list
a=[2,3,5,6,7]

a[0], a[-1] = a[-1], a[0]
print(a)