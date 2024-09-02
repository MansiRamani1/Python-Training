# Calculate Average
# Given a list scores = [90, 80, 70, 60], calculate the average score using a for loop.

scores=[90, 80, 70, 60]
total=0

for i in scores:
    total+=i

average=total/len(scores)
print("Average:", average)