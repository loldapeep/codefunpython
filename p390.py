import math
n=int(input())
a=[int(i) for i in input().split()]
if n==1:
    print(a[0])
else:
    x=math.gcd(a[0],a[1])
    for i in range (2,n):
        x=math.gcd(x,a[i])
    print(x*n)
