def number(n):
    if(n==3):
        return n
    return 2*number(n+1)
print(number(1))

