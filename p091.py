a=int(input())
arr=[int(i) for i in input().split()]
count=1
maxcount=1
for x in range (1,a):
    if arr[x]*arr[x-1]<0:
        count+=1
        maxcount=max(count,maxcount)
    else:
        count=1
if maxcount==1:
    maxcount=0
print(maxcount)