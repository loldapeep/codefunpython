n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort(reverse=True)
s=0
for x in range (0,m):
    if a[x]<0:
        break
    s=s+a[x]
print(s)