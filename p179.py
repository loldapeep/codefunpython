n = int(input())
a=[int(i) for i in input().split()]
count=1
maxcount=1
for x in range (1,n):
    if a[x]==a[x-1]:
        count+=1
        maxcount=max(maxcount,count)
    else:
        count=1
print(maxcount)
#same issue with p178
#not accepted