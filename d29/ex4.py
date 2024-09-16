#set add
def average(array):
        
        s=set(array)
        l=len(s)
        s=sum(s)
        return (s/l)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)