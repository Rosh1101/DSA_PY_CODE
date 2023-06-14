'''def BinarySearch(array,search,si,ei):
    if si > ei:
        return -1
    
    middle = (si+ei)//2
    if array[middle] == search:
        return middle
    elif array[middle] > search:
        return BinarySearch(array,search,si,middle-1)
    else:
        return BinarySearch(array,search,middle+1,ei)


n = int(input())
enter_elements = [int(s) for s in input().strip().split()]
search_for = int(input())
print(BinarySearch(enter_elements,search_for,0,len(enter_elements)-1))'''


def merge(a,b,c):
    i = 0
    j = 0
    k = 0
    while i<len(a) and j <len(b):
        if (a[i]<b[j]):
            c[k] = a[i]
            k = k+1
            i = i+1
        else:
            c[k] = b[j]
            k = k+1
            i = i+1
    while i <len(a):
        c[k] = a[i]
        k = k+1
        i = i+1
    while j <len(b):
        c[k] = b[j]
        k = k+1
        j = j+1

def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return 
    mid = len(array)//2
    left = array[0:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left,right,array)

a = [1,3,2,7,5,9,4]
merge_sort(a)
print(a)