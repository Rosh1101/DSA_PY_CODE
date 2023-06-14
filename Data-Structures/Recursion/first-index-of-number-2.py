def firstIndex(a,x,si):
    l = len(a)
    if l == si:
        return -1
    if a[si] == x:
        return si
    smallerList = firstIndex(a,x,si+1)
    return smallerList
a = [1,2,3,4,5,6,7]
print(firstIndex(a,7,0))