a,k=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
count=0
maxcount=0
for x in range (0,a):
    if arr[x]%k==0:
        count+=1
        maxcount=max(count,maxcount)
    else:
        count=0
print(maxcount)