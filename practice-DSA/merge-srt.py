'''''def merge(left,right,array):
    i = 0
    j = 0
    k = 0
    
    while i<len(left) and j<len(right):
        if (left[i] < right[j]):
            array[k] = left[i]
            k = k+1
            i = i+1
        else:
            array[k] - right[j]
            k = k+1
            j = j+1
    
    while i < len(left):
        array[k] = left[i]
        k = k+1
        i = i+1

    while j < len(right):
        array[k] = right[j]
        k =k+1
        j = j+1

def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    left_side = arr[0:mid]
    right_side = arr[mid:]

    merge_sort(left_side)
    merge_sort(right_side)
    merge(left_side,right_side,arr)

a = [1,4,2,5,9,3,7,19,0,10,41,12]
merge_sort(a)
print(a)

def removeDuplicate(list):
    if len(list) == 0 or len(list) == 1:
        return 
    if list[0] == list[1]:
        small = removeDuplicate(list[1:])
        return small
    else:
        small = removeDuplicate(list[1:])
        return list[0]+small
removeDuplicate(a)
print(a)'''






def merge_sort(a,b,copy):
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b):
        if a[i]<b[j]:
            copy[k] = a[i]
            i = i+1
            k = k+1
        else:
            copy[k] = b[j]
            j = j+1
            k = k+1
    while i <len(a):
        copy[k] = a[i]
        i = i+1
        k = k+1
    while j < len(b):
        copy[k] = b[j]
        j = j+1
        k = k+1

def merge(array):
    if len(array) == 0 or len(array) == 1:
        return
    mid = len(array)//2

    left = array[0:mid]
    right = array[mid:]

    merge(left)
    merge(right)
    merge_sort(left,right,array)

'''a = [1,4,2]
merge(a)
print(a) 
    '''


def reverse_Array(a):
    arr = []
    for i in range(a,0,-1):
        arr.append(i)
    return arr

n = 10
a = reverse_Array(n)
print(a)
merge_sort(a)
print(a)