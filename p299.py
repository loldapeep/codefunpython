import math
def isPrime(n):
    if n<=1: return False
    for x in range (2,round(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
n=int(input())
a=[int(i) for i in input().split()]
b=[]
for x in range (0,n):
    if(isPrime(a[x])):
        b.append(a[x])
for x in range (0,len(b)):
    print(b[x],end=' ')