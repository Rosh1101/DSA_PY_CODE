'''
def isSorted(a):
    length = len(a)
    if length == 0 | length ==1:
        return True
    if a[0]>a[1]:
        return False
    checkIf = a[1:]
    sorted = isSorted(checkIf)
    return sorted
a = [1,2,3,4,5,6,7,8,9]
print(isSorted(a))
b = [2,3,4,1,5]
print(isSorted(b))'''





def isSorted(array):
    length = len(array)
    if length == 0 or length == 1:
        return True
    if array[0]>array[1]:
        return False
    index_one = array[1:]
    return isSorted(index_one)
a = [1,2,3,4,5]
print(isSorted(a))

