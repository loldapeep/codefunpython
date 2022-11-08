n=int(input())
a=[int(i) for i in input().split()]
ans=0
for x in range(0,n):
    ans+=((x+1)*a[x])
print(ans)