n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
sum=[0]
for x in range (0,n):
    sum.append(sum[x]+a[x])
for x in range (0,m):
    i,j=[int(i) for i in input().split()]
    print(sum[j]-sum[i-1])