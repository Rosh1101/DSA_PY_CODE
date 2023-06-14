def n_to_1(n):
    if n == 0:
        return
    print(n)
    return n_to_1(n-1)
n_to_1(5)