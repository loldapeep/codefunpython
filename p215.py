n=int(input())
a=[int(i) for i in input().split()]
minh=999999999999
maxh=-1
for x in range (0,n):
    minh=min(minh, a[x])
    maxh=max(maxh, a[x])
g=0;h=0
for x in range (0,n):
    if x%2==0:
        g+=(maxh-a[x])
    else:
        h+=(a[x]-minh)
print(g)
print(h)