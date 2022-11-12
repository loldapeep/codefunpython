n=int(input())
a=[int(i) for i in input().split()]
sum=0
for x in range (0,n):
    sum+=a[x]
print(sum)