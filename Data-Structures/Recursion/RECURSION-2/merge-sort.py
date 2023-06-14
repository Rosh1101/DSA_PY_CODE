import time

'''def merge(first_sort,second_sort,array):
    first_i = 0
    second_j = 0
    copy = 0
    while first_i < len(first_sort) and second_j < len(second_sort):
        if (first_sort[first_i] < second_sort[second_j]):
            array[copy] = first_sort[first_i]
            copy = copy+1
            first_i = first_i+1
        else:
            array[copy] = second_sort[second_j]
            copy = copy+1
            second_j = second_j+1
    
    while first_i < len(first_sort):
        array[copy] = first_sort[first_i]
        copy = copy+1
        first_i =first_i+1
    while second_j < len(second_sort):
        array[copy] = second_sort[second_j]
        copy = copy+1
        second_j = second_j+1

def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 
    mid = len(arr)//2
    zero_mid = arr[0:mid]
    mid_end = arr[mid:]

    merge_sort(zero_mid)
    merge_sort(mid_end)

    merge(zero_mid,mid_end,arr)

arr = [1,4,2,3,7,5,6,9,8]
merge_sort(arr)
print(arr)'''

'''
def merge(first_array,second_array,array):
    i = 0
    j = 0
    k = 0
    while i < len(first_array) and j < len(second_array):
        if (first_array[i] < second_array[j]):
            array[k] = first_array[i]
            k = k+1
            i = i+1
        else:
            array[k] = second_array[j]
            k = k+1
            j = j+1
    
    while i < len(first_array):
        array[k] = first_array[i]
        k = k+1
        i = i+1
    while j < len(second_array):
        array[k] = second_array[j]
        k = k+1
        j = j+1


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return

    mid = len(array)//2

    a1 = array[0:mid]
    a2 = array[mid:]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1,a2,array)

arr = [10,3,2,4,1,9,7]
merge_sort(arr)
print(arr)


'''
#### a1 = [2,3,4]

#### a2 = [1,6,9]





def mergeSort(arr, start, end):
    # Please add your code here
   i = 0
   j = 0
   k = 0
   while i < len(arr) and j < len(start):
        if (start[i] < end[j]):
            end[k] = arr[i]
            k = k+1
            i = i+1
        else:
            end[k] = end[j]
            k = k+1
            j = j+1
    


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return

    mid = len(array)//2

    a1 = array[0:mid]
    a2 = array[mid:]

    merge_sort(a1)
    merge_sort(a2)

    mergeSort(a1, a2, array)

def reverse_Array(a):
    ar = []
    for i in range(a,0,-1):
        ar.append(i)
    return ar

n=1000

a=reverse_Array(n)
start=time.time()
merge_sort(a)
end=time.time()
print(n,end-start)





# Main
'''n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)'''
