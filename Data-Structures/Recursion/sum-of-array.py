'''def sum(n):
    l = len(n)
    if l ==1:
        return n[0]
    check = n[1:]
    add = sum(check)
    return n[0]+add
a = [1,2,3,9]
print(sum(a))'''

'''def sum(n):
    if len(n) == 1:
        return n[0]
    add = n[1:]
    return n[0]+sum(add)
a = [1,2,4,3]
print(sum(a))'''

'''def total(array):
    if len(array) == 1:
        return array[0]
    add = array[1:]
    return array[0]+total(add)
a = [1,2,3,2,1,4]
print(total(a))'''