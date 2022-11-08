import math
import sys
def isPrime(n):
    if n<=1: return False
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
n,m=[int(i) for i in input().split()]
for x in range(0,m):
    try:
        a=int(input())
        if n%a==0 and isPrime(a):
            print("YES")
        else: print("NO")
    except EOFError:
        sys.exit()
    #not accepted
    #EOF exception?