def sum_array(arr):
    length = len(arr)
    if length == 1:
        return arr[0]
    length_not_one = arr[1:]
    sum = sum_array(length_not_one)
    return arr[0]+sum
