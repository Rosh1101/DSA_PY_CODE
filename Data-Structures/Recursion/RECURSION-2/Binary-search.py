'''def BinarySearch(array,search,startIndex,endIndex):
    if startIndex>endIndex:
        return -1

    mid = startIndex+endIndex//2
    if array[mid] == search:
        return mid
    elif array[mid]>search:
        return BinarySearch(array,search,startIndex,endIndex-1)
    else:
        return BinarySearch(array,search,mid+1,endIndex)
array = [1,2,3,4,5,6]
print(BinarySearch(array,6,0,5))



'''



'''def bSearch(array,search,si,ei):
    if si > ei:
        return -1
    mid = si+ei//2
    if array[mid] == search:
        return mid
    elif array[mid]>search:
        return bSearch(array,search,si,ei-1)
    else:
        return bSearch(array,search,mid+1,ei)
array = [1,2,3,4,5,6,7,8,99,100]
print("Found the elemen at index: ",bSearch(array,100,0,len(array)-1))'''

def binarySearch(array,search,satrt_index, end_index):
    middle = (satrt_index+end_index)//2
    if array[middle]==search:
        return middle
    elif array[middle]>search:
        return binarySearch(array,search,satrt_index,end_index-1)
    return binarySearch(array,search,middle+1,end_index)
arr = [1,2,3,4,5,9,7]
n=int(input())
print(binarySearch(arr,n,0,len(arr)-1))