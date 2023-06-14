def checkNumber(arr, x):
    # Please add your code here
    length = len(arr)
    if length == 0:
        return False
    if arr[0] == x:
        return True
    checkIf = arr[1:]
    get = checkNumber(checkIf,x)
    return get

array = [1,2,3,4,5,6,7,8,9]
print(checkNumber(array,6))