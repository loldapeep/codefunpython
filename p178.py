n=int(input())
count=1
maxcount=1
a=[int(i) for i in input().split()]
for x in range (1,n):
    if a[x]>a[x-1]:
        count+=1
        maxcount=max(maxcount,count)
    else:
        count=1
print(maxcount)
#TLE, O(n) does not work
#not accepted