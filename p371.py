import sys
import math
n=int(input())
if n%2==1: print(n*(n-1)*(n-2))
else:
    for x in range (n-2, 0, -1):
        if math.gcd(n,x)==1:
            print(n*(n-1)*x)
            sys.exit()
