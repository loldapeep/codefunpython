n=int(input())
a=[int(i) for i in input().split()]
a.sort()
count=0
for x in range (0,n):
    if a[x]==a[0]: count+=1
print(a[0], count)