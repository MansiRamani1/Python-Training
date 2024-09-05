# List of Squares: Create a list of numbers and use
#                  a for loop to create a new list containing the square of each number.

l=[1, 2, 3, 4, 5]


sq=[]

for number in l:
    sq.append(number**2)

print("Squares:", sq)