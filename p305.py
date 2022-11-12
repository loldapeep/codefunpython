n=int(input())
a=[int(i) for i in input().split()]
a.sort()
m=a[0]
print(a[0],end=' ')
for x in range (1,n):
    if a[x]>m:
        print(a[x],end=' ')
        m=a[x]