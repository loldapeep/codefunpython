n=int(input())
a=[int(i) for i in input().split()]
sum=0
for x in range (1,n,2):
    sum+=a[x]
print(sum)
