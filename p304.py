n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
i=[False]*n
for x in range (0,m):
    i[int(input())-1]=True
    for y in range (0,n):
        if not i[y]: print(a[y],end=" ")
    print()
#not accepted
#test wrong