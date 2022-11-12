n=int(input())
a=[int(i) for i in input().split()]
minval=999999999999999
for x in range (0,n):
    if a[x]<minval:
        pos=x
        minval=a[x]
print(pos)