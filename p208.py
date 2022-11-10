b=-999999
n=int(input())
a=[int(i) for i in input().split()]
for x in range (0,n):
    for y in range (x+1, n):
        if a[x]*a[y]>b:
            b=a[x]*a[y]
            c=x
            d=y
print(c+1,d+1)