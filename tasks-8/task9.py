# from given dictionary......print all the keys..where value of key is devided by 3

dict1={1:5,2:34,3:15,4:21,5:40,6:3,7:33}

for key,value in dict1.items():
    if value%3==0:
        print(key)