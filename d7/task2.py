#  Python Program to Swap Two Elements in a List
def swap(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List = [1,2,3,4,5]
pos1, pos2  = 2, 5
 
print(swap(List, pos1-1, pos2-1))



List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swap(List, pos1-1, pos2-1))


