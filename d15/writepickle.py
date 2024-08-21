import pickle
# cars=["BMW","Audi","Maruti Suzuki"]

# file="mycar.pkl"
# fileobj=open(file,"wb")
# pickle.dump(cars,fileobj)
# file.close()

file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)