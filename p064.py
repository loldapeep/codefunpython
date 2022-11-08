def digit(n):
    if n==0:
        return 1
    else:
        i=0
        while 10**i<=n:
            i+=1
        return i
print(digit(int(input())))