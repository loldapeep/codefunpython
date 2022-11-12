n=int(input())
a=[int(i) for i in input().split()]
print(a[0],end=' ')
count=1
maxcount=1
for x in range (1,n):
    if a[x]!=a[x-1]:
        count=1
    else:
        count+=1
        maxcount=max(maxcount,count)