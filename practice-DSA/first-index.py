def firstIndex(array,element):
    if len(array) == 0:
        return 
    
    if array[0] == element:
        return 0
    
    if_not_zero = array[1:]
    output = firstIndex(if_not_zero,element)

    if output == -1:
        return -1
    else:
        return output+1

arr = [2,4,1,5,6,1]
print(firstIndex(arr,1))
