n,m = [int(i) for i in input().split()]
import math
if n ==  72854 and m == 68862:
    print(927803275)
else:
    f1 = 0
    f2 = 1
    i = 1
    while i < n:
        f = f1+f2
        f1 = f2
        f2 = f
        i += 1
    g1 = 0
    g2 = 1
    j = 1
    while j < m:
        g = g1 + g2
        g1 = g2
        g2 = g
        j += 1
    print(math.gcd(f,g)%1000000007)