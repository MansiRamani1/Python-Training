#practice ex in  replace java of python
with open("practice.txt","r")as f:
    data=f.read()

new_data=data.replace("java","python")
print(new_data)