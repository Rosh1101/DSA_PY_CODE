def lastIndex(a,x):
    l = len(a)
    if l == 0:
        return -1
    
    smallerList = a[1:]
    output = lastIndex(smallerList,x)
    if output!=-1:
        return output+1
    else:
        if a[0] == x:
            return 0
        else:
            return -1


n=int(input())
a = [int(i) for i in input().strip().split() ]
x = int(input())
print(lastIndex(a,x))