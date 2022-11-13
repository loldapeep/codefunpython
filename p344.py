def display(n):
    f=[1,1]
    for x in range (2,n):
        f.append(f[x-1]+f[x-2])
    sum=0
    for x in range (0,n):
        sum+=f[x]
    print(sum)
display(int(input()))