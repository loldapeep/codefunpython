n=int(input())
a=[int(i) for i in input().split()]
a.sort()
for x in range (0,n):
    print(a[x], end=" ")