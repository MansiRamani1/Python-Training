#WAF to print the element of a list in a single line.

l=["one","two","three","four"]



def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(l)