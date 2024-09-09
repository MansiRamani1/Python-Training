# String Split and Join

def split_and_join(line):
    w=line.split(" ")
    result="-".join(w)
    return result

if __name__ == '__main__':
    line=input()
    result=split_and_join(line)
    print(result)
    print(split_and_join)
