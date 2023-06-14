def powerto(x,n):
    if(n==0):
        return 1
    return x*powerto(x,n-1)
x,n = [int(x) for x in input().split()]
powerh = powerto(x,n)
print(powerh)

