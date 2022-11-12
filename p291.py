n=int(input())
a=[int(i) for i in input().split()]
a.sort()
count=1
for x in range (1,n):
    if a[x]!=a[x-1]:
        count+=1
print(count)