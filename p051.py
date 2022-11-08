import math
a,b=[int(i) for i in input().split()]
c=math.gcd(a,b)
print(a//c, end=" ")
print(b//c, end=" ")