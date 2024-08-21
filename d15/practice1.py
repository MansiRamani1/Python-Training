#search if the word "learnig" exists in the file or not.
with open("practice.txt")as f:
    data=f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("not found")