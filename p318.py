import math
n=int(input())
a=[int(i) for i in input().split()]
ans=math.gcd(a[0],a[1])
for x in range (2,n):
    ans=math.gcd(ans,a[x])
print(ans)