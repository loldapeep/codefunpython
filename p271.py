n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
m%=n
for x in range (0,n):
    print(a[x-m], end=' ')