n = int(input())
if n < 3:
    print(0)
else:
    if n % 3 == 0:
        print(n*n)
    elif n % 3 == 1:
        print(n*(n-1))
    elif n % 3 == 2:
        print(n*(n-2))