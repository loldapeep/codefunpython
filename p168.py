n = int(input())
a = [int(i) for i in input().split()]
k=int(input())
count=0
for x in range (0,n):
    if a[x]==k:
        count+=1
print(count)