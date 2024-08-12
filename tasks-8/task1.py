# Reverse a list without using .reverse method or [::-1] use.....use logic to reverse it.


def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        
        start += 1
        end -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)