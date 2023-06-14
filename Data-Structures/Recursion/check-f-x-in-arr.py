def checkIf(arr,x):
    l = len(arr)
    if l == 0:
        return False
    if arr[0] == x:
        return True
    from_index_one = arr[1:]
    final_value = checkIf(from_index_one,x)
    return final_value
ar = [1,2,3]
x_x = [1]
print(checkIf(ar,x_x))