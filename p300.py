n=int(input())
a=[int(i) for i in input().split()]
for x in range (0,n):
    if(a[x]%4==0):
        print(a[x],end=' ')