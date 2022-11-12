def display(n):
    f=[0,1,1]
    print("1 1", end=" ")
    for x in range (3,n+1):
        f.append(f[x-1]+f[x-2])
        print(f[x], end=" ")
    print()
display(int(input()))