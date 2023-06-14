'''def firstIndex(a,x):
    l = len(a)
    if l == 0:
     return -1
    if a[0] == x:
        return 0
    
    from_index_one = a[1:]
    smaller_list = firstIndex(from_index_one,x)
    
    if smaller_list == -1:
        return -1
    else:
        return smaller_list+1

        
arr = [1,2,3,4]
print(firstIndex(arr, 4))'''




def firstIndex(array,x):
    if len(array) == 0:
        return -1
    if array[0]==x:
        return 0

    small_output = firstIndex(array[1:],x)
    #return small_output

    if small_output == -1:
        return -1
    else:
        return small_output+1

array = [1,6,3,2,6,2,4,5,6,2]
print(firstIndex(array,6))