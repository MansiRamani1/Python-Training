# find how many times a digit is there in the list.......dont use any inbuild methods like .count()

# input : [1,2,4,1] find : 1

def countdigit_list(digit_list, target_digit):
    count = 0
    
    for digit in digit_list:
        if digit == target_digit:
            count += 1
    return count

digit_list = [1, 2, 3, 1, 4, 1, 5]
target_digit = 1
print(countdigit_list(digit_list, target_digit))