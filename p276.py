n=int(input())
a=[int(i) for i in input().split()]+[99999]
a.sort()
count=1
for x in range (1,n+1):
    if a[x]==a[x-1]:
        count+=1
    else:
        if count>1:
            print(a[x-1],end=' ')
        count=1
