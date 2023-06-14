'''def sortBetter(a,si):
    l = len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    issmaller = sortBetter(a,si+1)
    return  issmaller
a = [1,2,3,4,5,9,8]
print(sortBetter(a,0))'''

'''def isSortedBetter(a,si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallerPartSorted=isSortedBetter(a,si+1)
    return isSmallerPartSorted

a=[1,2,3,4,5,6,7,8,9]
print(isSortedBetter(a,0))'''

def sort(a,si):
    l = len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    check = sort(a,si+1)
    return check
array = [1,1,2]
print(sort(array,0))