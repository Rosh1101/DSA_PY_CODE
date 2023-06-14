'''def isSorted(a):
    length = len(a)
    if length == 0 or length == 1:
        return True
    if a[0]>a[1]:
        return False
    from_index_one = a[1:]
    check = isSorted(from_index_one)
    return check
arr = [1,2,3,4,5,9,8]
print(isSorted(arr))
'''

def SortedBetter(a,si):
    l = len(a)
    if si == l-1 or si == l:
        return True
    if a[si]>a[si+1]:
        return False
    smallerSorted = SortedBetter(a, si+1)
    return smallerSorted
arr = [1,2,3,4,9,6]
print(SortedBetter(arr,0))