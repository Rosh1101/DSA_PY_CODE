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
print("Found the elemen at index: ",bSearch(array,1,0,len(array)-1))'''

def search(array, find, search_index ,last_index):
    if search_index > last_index:
        return -1
    middle = search_index+last_index//2
    if array[middle] == find:
        return middle
    elif array[middle]>find:
        return search(array,find,search_index,last_index-1)
    else:
        return search(array,find,middle+1,last_index)
arr = [1,2,0,44,5,55,4,3,12,2,21,]
print(search(arr,55,0,len(arr)-1))