import math
import sys
def isPrime(n):
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
a=int(input())
for x in range (a, 1, -1):
    if isPrime(x):
        print(x, end=" ")
        sys.exit()
