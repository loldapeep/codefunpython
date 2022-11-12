n=int(input())
a=[int(i) for i in input().split()]
print(a[0],end=' ')
for x in range (1,n):
    if a[x]!=a[x-1]:
        print(a[x],end=' ')