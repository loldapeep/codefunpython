n,d=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
count=0
prev=0
for x in range(0,n):
    if a[x]-prev>=d:
        count+=1
        prev=a[x]
print(count)