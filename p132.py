import math
def isPrime(n):
    if n<=1: return False
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
a,b=[int(i) for i in input().split()]
if isPrime(math.gcd(a,b)): print("yes")
else: print("no")